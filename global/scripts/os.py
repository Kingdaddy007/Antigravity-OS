#!/usr/bin/env python3
"""Build, validate, and safely install Anti-Gravity OS.

The development CLI intentionally uses only Python's standard library. Release
payloads are built in CI, so end users do not need Python to consume them.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
GLOBAL_ROOT = REPO_ROOT / "global"
MANIFEST_PATH = GLOBAL_ROOT / "manifest.yaml"
SUPPORTED_HOSTS = ("gemini", "codex", "cursor", "windsurf", "opencode")
MUTATION_CLASSES = (
    "read_only",
    "local_edit",
    "dependency_or_network",
    "destructive",
    "external_or_production",
)
WORKFLOW_REQUIRED_FIELDS = (
    "id",
    "version",
    "status",
    "intent",
    "use_when",
    "do_not_use_when",
    "inputs",
    "required_resources",
    "mutation_class",
    "approval_gates",
    "states",
    "outputs",
    "verification",
    "failure_paths",
    "resume_contract",
    "next_workflows",
    "profiles",
)
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
UNRESOLVED_TOKEN_PATTERN = re.compile(
    r"(?<!\$)\{\{[A-Za-z_][A-Za-z0-9_.-]*\}\}"
)
PERSONAL_PATH_PATTERNS = (
    re.compile(r"(?i)file:///+[a-z]:/users/"),
    re.compile(r"(?i)[a-z]:[\\/]users[\\/]"),
    re.compile(r"(?i)file:///+[a-z]%3a/users/"),
    re.compile(r"(?i)/users/(?:godsw|oviks)(?:/|$)"),
)


class AntiGravityError(RuntimeError):
    """Base error for predictable CLI failures."""


class InstallationRefused(AntiGravityError):
    """Raised when an installation target or approval state is unsafe."""


class ValidationFailed(AntiGravityError):
    """Raised when a build is attempted with invalid canonical source."""


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    try:
        temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


@contextmanager
def exclusive_file_lock(path: Path, timeout_seconds: float = 5.0):
    deadline = time.monotonic() + timeout_seconds
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor: int | None = None
    while descriptor is None:
        try:
            descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(descriptor, str(os.getpid()).encode("ascii"))
        except FileExistsError:
            try:
                stale = time.time() - path.stat().st_mtime > 30
            except FileNotFoundError:
                stale = False
            if stale:
                path.unlink(missing_ok=True)
                continue
            if time.monotonic() >= deadline:
                raise TimeoutError(f"Timed out acquiring workflow index lock: {path}")
            time.sleep(0.05)
    try:
        yield
    finally:
        os.close(descriptor)
        path.unlink(missing_ok=True)


def write_workflow_state(workspace: Path, state: dict[str, Any]) -> Path:
    required = {
        "schema_version",
        "task_id",
        "workflow_id",
        "mode",
        "status",
        "current_state",
        "completed_states",
        "owner",
        "workspace",
        "evidence",
        "artifacts",
        "approvals",
        "blockers",
        "next_action",
        "created_at",
        "updated_at",
        "archived",
    }
    missing = required - set(state)
    if missing:
        raise ValueError(f"Workflow state is missing: {', '.join(sorted(missing))}")
    task_id = state["task_id"]
    if not isinstance(task_id, str) or not re.fullmatch(r"[A-Za-z0-9._-]+", task_id):
        raise ValueError("task_id must contain only letters, digits, dot, underscore, or hyphen")
    if state["schema_version"] != 1:
        raise ValueError("Unsupported workflow state schema_version")

    state_directory = workspace.resolve() / ".agents" / "workflows"
    state_path = state_directory / f"{task_id}.json"
    write_json_atomic(state_path, state)

    index_path = state_directory / "index.json"
    lock_path = state_directory / ".index.lock"
    with exclusive_file_lock(lock_path):
        if index_path.exists():
            index = load_json(index_path)
        else:
            index = {"schema_version": 1, "updated_at": state["updated_at"], "tasks": {}}
        tasks = index.setdefault("tasks", {})
        tasks[task_id] = state_path.name
        index["updated_at"] = state["updated_at"]
        write_json_atomic(index_path, index)
    return state_path


def file_map(root: Path) -> dict[str, Path]:
    if not root.exists():
        return {}
    return {
        path.relative_to(root).as_posix(): path
        for path in root.rglob("*")
        if path.is_file()
    }


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "":
        return ""
    if value in {"null", "~"}:
        return None
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if re.fullmatch(r"-?[0-9]+", value):
        return int(value)
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(item) for item in inner.split(",")]
    if value.startswith(("\"", "'")) and value.endswith(value[0]):
        if value[0] == "\"":
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                pass
        return value[1:-1]
    return value


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the deliberately small YAML subset used by OS metadata.

    Supported constructs are top-level scalar keys, inline lists, block lists,
    and folded/literal scalar blocks. Nested mappings belong in JSON registry
    files rather than Markdown frontmatter.
    """

    result: dict[str, Any] = {}
    lines = text.replace("\r\n", "\n").split("\n")
    index = 0
    while index < len(lines):
        raw = lines[index]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            index += 1
            continue
        if raw.startswith((" ", "\t")) or ":" not in raw:
            raise ValueError(f"Unsupported YAML at line {index + 1}: {raw}")
        key, raw_value = raw.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if not re.fullmatch(r"[A-Za-z0-9_-]+", key):
            raise ValueError(f"Invalid key at line {index + 1}: {key}")

        if raw_value in {">", "|"}:
            block: list[str] = []
            index += 1
            while index < len(lines):
                candidate = lines[index]
                if candidate and not candidate.startswith((" ", "\t")):
                    break
                block.append(candidate.strip())
                index += 1
            separator = " " if raw_value == ">" else "\n"
            result[key] = separator.join(part for part in block if part).strip()
            continue

        if raw_value == "":
            items: list[Any] = []
            index += 1
            while index < len(lines):
                candidate = lines[index]
                if candidate and not candidate.startswith((" ", "\t")):
                    break
                candidate = candidate.strip()
                if candidate:
                    if not candidate.startswith("-"):
                        raise ValueError(
                            f"Only block lists are supported at line {index + 1}"
                        )
                    items.append(parse_scalar(candidate[1:].strip()))
                index += 1
            result[key] = items
            continue

        result[key] = parse_scalar(raw_value)
        index += 1
    return result


def split_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    content = path.read_text(encoding="utf-8-sig")
    normalized = content.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = normalized.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unclosed YAML frontmatter")
    metadata = parse_simple_yaml(normalized[4:end])
    return metadata, normalized[end + 5 :]


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationFailed(f"Unable to load {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationFailed(f"Expected an object in {path}")
    return value


def load_manifest(repo_root: Path = REPO_ROOT) -> dict[str, Any]:
    path = repo_root / "global" / "manifest.yaml"
    return load_json(path)


def issue(code: str, path: Path | str, message: str) -> dict[str, str]:
    return {"code": code, "path": str(path), "message": message}


def validate_skill_files(repo_root: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    for path in sorted((repo_root / "global" / "skills").rglob("SKILL.md")):
        relative = path.relative_to(repo_root)
        try:
            metadata, _ = split_frontmatter(path)
        except (OSError, UnicodeDecodeError, ValueError) as exc:
            problems.append(issue("skill-frontmatter", relative, str(exc)))
            continue
        unexpected = set(metadata) - {"name", "description", "license"}
        if unexpected:
            problems.append(
                issue(
                    "skill-frontmatter-keys",
                    relative,
                    f"unsupported canonical keys: {', '.join(sorted(unexpected))}",
                )
            )
        name = metadata.get("name")
        description = metadata.get("description")
        if not isinstance(name, str) or not SKILL_NAME_PATTERN.fullmatch(name):
            problems.append(issue("skill-name", relative, "name must be hyphen-case"))
        elif name != path.parent.name:
            problems.append(
                issue("skill-name-folder", relative, f"name must match folder {path.parent.name}")
            )
        if not isinstance(description, str) or not description.strip():
            problems.append(issue("skill-description", relative, "description is required"))
        elif len(description) > 1024:
            problems.append(
                issue("skill-description-length", relative, "description exceeds 1024 characters")
            )
        ui_metadata_path = path.parent / "agents" / "openai.yaml"
        if not ui_metadata_path.exists():
            problems.append(issue("skill-ui-metadata", relative, "agents/openai.yaml is missing"))
        else:
            ui_metadata = ui_metadata_path.read_text(encoding="utf-8-sig", errors="replace")
            for field in ("interface:", "display_name:", "short_description:", "default_prompt:"):
                if field not in ui_metadata:
                    problems.append(
                        issue(
                            "skill-ui-metadata",
                            ui_metadata_path.relative_to(repo_root),
                            f"missing {field.rstrip(':')}",
                        )
                    )
    return problems


def validate_workflow_files(repo_root: Path) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]]]:
    problems: list[dict[str, str]] = []
    workflows: dict[str, dict[str, Any]] = {}
    directory = repo_root / "global" / "workflows"
    for path in sorted(directory.glob("workflow-*.md")):
        relative = path.relative_to(repo_root)
        try:
            metadata, _ = split_frontmatter(path)
        except (OSError, UnicodeDecodeError, ValueError) as exc:
            problems.append(issue("workflow-frontmatter", relative, str(exc)))
            continue
        missing = [field for field in WORKFLOW_REQUIRED_FIELDS if field not in metadata]
        if missing:
            problems.append(
                issue("workflow-fields", relative, f"missing fields: {', '.join(missing)}")
            )
        workflow_id = metadata.get("id")
        if not isinstance(workflow_id, str) or not SKILL_NAME_PATTERN.fullmatch(workflow_id):
            problems.append(issue("workflow-id", relative, "id must be hyphen-case"))
            continue
        if workflow_id in workflows:
            problems.append(issue("workflow-duplicate", relative, f"duplicate id {workflow_id}"))
        workflows[workflow_id] = metadata
        if metadata.get("mutation_class") not in MUTATION_CLASSES:
            problems.append(issue("workflow-mutation", relative, "invalid mutation_class"))
        for field in (
            "use_when",
            "do_not_use_when",
            "inputs",
            "required_resources",
            "approval_gates",
            "states",
            "outputs",
            "verification",
            "failure_paths",
            "next_workflows",
            "profiles",
        ):
            if field in metadata and not isinstance(metadata[field], list):
                problems.append(issue("workflow-field-type", relative, f"{field} must be a list"))

    known = set(workflows)
    for workflow_id, metadata in workflows.items():
        for next_id in metadata.get("next_workflows", []):
            if next_id in {None, "none", "None", ""}:
                continue
            if next_id not in known:
                problems.append(
                    issue(
                        "workflow-route",
                        directory / f"workflow-{workflow_id}.md",
                        f"unknown next workflow: {next_id}",
                    )
                )
    return problems, workflows


def validate_context_templates(repo_root: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    directory = repo_root / "global" / "context_templates"
    for path in sorted(directory.glob("*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        relative = path.relative_to(repo_root)
        try:
            metadata, _ = split_frontmatter(path)
        except (OSError, UnicodeDecodeError, ValueError) as exc:
            problems.append(issue("context-frontmatter", relative, str(exc)))
            continue
        if metadata.get("status") != "template":
            problems.append(issue("context-status", relative, "status must be template"))
        for field in ("scope", "project_id", "updated_at", "owner", "confidence"):
            if field not in metadata:
                problems.append(issue("context-metadata", relative, f"missing {field}"))
    return problems


def validate_adapters(repo_root: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    required = {
        "schema_version",
        "host",
        "namespace",
        "content_root",
        "instruction_target",
        "skills_target",
        "workflows_target",
        "supports_slash_commands",
        "approval_model",
        "capabilities",
    }
    for host in SUPPORTED_HOSTS:
        path = repo_root / "global" / "adapters" / host / "adapter.json"
        if not path.exists():
            problems.append(issue("adapter-missing", path.relative_to(repo_root), "adapter is missing"))
            continue
        try:
            adapter = load_json(path)
        except ValidationFailed as exc:
            problems.append(issue("adapter-json", path.relative_to(repo_root), str(exc)))
            continue
        missing = required - set(adapter)
        if missing:
            problems.append(issue("adapter-fields", path.relative_to(repo_root), f"missing {sorted(missing)}"))
        if adapter.get("host") != host or adapter.get("namespace") != "antigravity":
            problems.append(issue("adapter-identity", path.relative_to(repo_root), "host or namespace mismatch"))
        capabilities = adapter.get("capabilities", {})
        for capability in (
            "read_file",
            "list_files",
            "search_text",
            "edit_file",
            "run_command",
            "request_approval",
        ):
            if not capabilities.get(capability):
                problems.append(
                    issue("adapter-capability", path.relative_to(repo_root), f"missing {capability}")
                )
    return problems


def distributable_markdown(repo_root: Path) -> Iterable[Path]:
    global_root = repo_root / "global"
    roots = (
        global_root / "skills",
        global_root / "workflows",
        global_root / "core",
        global_root / "baselines",
        global_root / "context_templates",
        global_root / "global_templates",
        global_root / "reference",
        global_root / "design-audit",
    )
    for root in roots:
        if root.exists():
            yield from root.rglob("*.md")
    for path in (global_root / "GEMINI.md", global_root / "GLOBAL_MEMORY.md"):
        if path.exists():
            yield path


def validate_markdown(repo_root: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    for path in sorted(set(distributable_markdown(repo_root))):
        relative = path.relative_to(repo_root)
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if path.parent.name == "workflows" and UNRESOLVED_TOKEN_PATTERN.search(text):
            problems.append(issue("unresolved-token", relative, "contains unresolved {{...}} token"))
        for pattern in PERSONAL_PATH_PATTERNS:
            if pattern.search(text.replace("\\", "/")):
                problems.append(issue("personal-path", relative, "contains a personal absolute path"))
                break
        for raw_link in MARKDOWN_LINK_PATTERN.findall(text):
            link = raw_link.strip().split("#", 1)[0]
            if not link or link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if link.lower().startswith("file:///"):
                problems.append(issue("absolute-link", relative, f"non-portable link: {raw_link}"))
                continue
            if re.match(r"(?i)^[a-z]:[\\/]", link):
                problems.append(issue("absolute-link", relative, f"non-portable link: {raw_link}"))
                continue
            candidate = (path.parent / link.replace("%20", " ")).resolve()
            if candidate.suffix.lower() == ".md" and not candidate.exists():
                problems.append(issue("broken-link", relative, f"missing target: {raw_link}"))
    return problems


def validate_forbidden_files(repo_root: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    forbidden_directories = (
        repo_root / "global" / "projects",
        repo_root / "global" / "global_workflows",
    )
    for path in forbidden_directories:
        if path.exists():
            problems.append(issue("forbidden-directory", path.relative_to(repo_root), "must not exist"))
    for path in (repo_root / "global").rglob("*.bak"):
        problems.append(issue("backup-file", path.relative_to(repo_root), "tracked backup file is forbidden"))
    return problems


def validate_manifest(
    repo_root: Path, workflows: dict[str, dict[str, Any]]
) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    path = repo_root / "global" / "manifest.yaml"
    if not path.exists():
        return [issue("manifest-missing", path.relative_to(repo_root), "manifest is missing")]
    try:
        manifest = load_manifest(repo_root)
    except ValidationFailed as exc:
        return [issue("manifest-json", path.relative_to(repo_root), str(exc))]
    if manifest.get("schema_version") != 1:
        problems.append(issue("manifest-version", path.relative_to(repo_root), "schema_version must be 1"))
    if set(manifest.get("hosts", [])) != set(SUPPORTED_HOSTS):
        problems.append(issue("manifest-hosts", path.relative_to(repo_root), "host registry mismatch"))
    if set(manifest.get("mutation_classes", [])) != set(MUTATION_CLASSES):
        problems.append(issue("manifest-mutations", path.relative_to(repo_root), "mutation registry mismatch"))

    registries = ("skills", "workflows", "context_templates", "baselines", "templates")
    for registry_name in registries:
        seen: set[str] = set()
        for entry in manifest.get(registry_name, []):
            entry_id = entry.get("id")
            entry_path = entry.get("path")
            if entry_id in seen:
                problems.append(issue("manifest-duplicate", path.relative_to(repo_root), f"duplicate {entry_id}"))
            seen.add(entry_id)
            if not isinstance(entry_path, str) or not (repo_root / entry_path).exists():
                problems.append(
                    issue("manifest-path", path.relative_to(repo_root), f"missing path for {entry_id}: {entry_path}")
                )
            for profile in entry.get("profiles", []):
                if profile not in manifest.get("profiles", []):
                    problems.append(
                        issue("manifest-profile", path.relative_to(repo_root), f"unknown profile {profile}")
                    )

    manifest_workflows = {entry.get("id") for entry in manifest.get("workflows", [])}
    if manifest_workflows != set(workflows):
        missing = sorted(set(workflows) - manifest_workflows)
        stale = sorted(manifest_workflows - set(workflows))
        problems.append(
            issue(
                "manifest-workflows",
                path.relative_to(repo_root),
                f"registry mismatch; missing={missing}, stale={stale}",
            )
        )

    disk_skills = {
        skill.parent.name for skill in (repo_root / "global" / "skills").rglob("SKILL.md")
    }
    manifest_skills = {entry.get("id") for entry in manifest.get("skills", [])}
    if disk_skills != manifest_skills:
        problems.append(
            issue(
                "manifest-skills",
                path.relative_to(repo_root),
                f"registry mismatch; missing={sorted(disk_skills - manifest_skills)}, stale={sorted(manifest_skills - disk_skills)}",
            )
        )
    return problems


def validate_routing_fixtures(
    repo_root: Path, workflows: dict[str, dict[str, Any]]
) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    path = repo_root / "tests" / "fixtures" / "routing.json"
    if not path.exists():
        return [issue("routing-fixtures", path.relative_to(repo_root), "fixture file is missing")]
    try:
        fixture = load_json(path)
        manifest = load_manifest(repo_root)
    except ValidationFailed as exc:
        return [issue("routing-fixtures", path.relative_to(repo_root), str(exc))]
    required = {
        "id",
        "request",
        "workflow",
        "profile",
        "mode",
        "maximum_mutation_class",
        "approval_required",
    }
    seen: set[str] = set()
    valid_modes = {"diagnose", "propose", "implement", "incident-mitigate"}
    for scenario in fixture.get("scenarios", []):
        missing = required - set(scenario)
        scenario_id = scenario.get("id", "<unknown>")
        if missing:
            problems.append(
                issue("routing-fields", path.relative_to(repo_root), f"{scenario_id} missing {sorted(missing)}")
            )
            continue
        if scenario_id in seen:
            problems.append(
                issue("routing-duplicate", path.relative_to(repo_root), f"duplicate scenario {scenario_id}")
            )
        seen.add(scenario_id)
        if scenario["workflow"] not in workflows:
            problems.append(
                issue(
                    "routing-workflow",
                    path.relative_to(repo_root),
                    f"{scenario_id} references unknown workflow {scenario['workflow']}",
                )
            )
        if scenario["profile"] not in manifest.get("profiles", []):
            problems.append(
                issue("routing-profile", path.relative_to(repo_root), f"{scenario_id} has unknown profile")
            )
        if scenario["mode"] not in valid_modes:
            problems.append(
                issue("routing-mode", path.relative_to(repo_root), f"{scenario_id} has invalid mode")
            )
        mutation = scenario["maximum_mutation_class"]
        if mutation not in MUTATION_CLASSES:
            problems.append(
                issue("routing-mutation", path.relative_to(repo_root), f"{scenario_id} has invalid mutation")
            )
        if scenario["mode"] == "diagnose" and mutation != "read_only":
            problems.append(
                issue("routing-diagnose", path.relative_to(repo_root), f"{scenario_id} diagnosis must be read-only")
            )
        if mutation in {"destructive", "external_or_production"} and not scenario["approval_required"]:
            problems.append(
                issue("routing-approval", path.relative_to(repo_root), f"{scenario_id} requires approval")
            )
    if not fixture.get("scenarios"):
        problems.append(issue("routing-empty", path.relative_to(repo_root), "no routing scenarios declared"))
    return problems


def validate_repository(repo_root: Path = REPO_ROOT) -> dict[str, Any]:
    problems: list[dict[str, str]] = []
    problems.extend(validate_forbidden_files(repo_root))
    problems.extend(validate_skill_files(repo_root))
    workflow_problems, workflows = validate_workflow_files(repo_root)
    problems.extend(workflow_problems)
    problems.extend(validate_context_templates(repo_root))
    problems.extend(validate_adapters(repo_root))
    problems.extend(validate_markdown(repo_root))
    problems.extend(validate_manifest(repo_root, workflows))
    problems.extend(validate_routing_fixtures(repo_root, workflows))
    return {"ok": not problems, "issue_count": len(problems), "issues": problems}


def copy_entry(
    source: Path, destination: Path, additional_ignores: tuple[str, ...] = ()
) -> None:
    if source.is_dir():
        ignored_names = (
            "*.bak",
            "__pycache__",
            "README.md",
            "CHANGELOG.md",
            *additional_ignores,
        )
        shutil.copytree(
            source,
            destination,
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns(*ignored_names),
        )
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def validate_payload(payload: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    text_extensions = {".md", ".json", ".yaml", ".yml", ".txt", ".toml"}
    for path in payload.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(payload)
        if path.suffix.lower() == ".bak" or "projects" in relative.parts:
            problems.append(issue("payload-forbidden", relative, "forbidden runtime artifact"))
        if path.suffix.lower() not in text_extensions:
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if UNRESOLVED_TOKEN_PATTERN.search(text):
            problems.append(issue("payload-token", relative, "unresolved template token"))
        normalized = text.replace("\\", "/")
        if any(pattern.search(normalized) for pattern in PERSONAL_PATH_PATTERNS):
            problems.append(issue("payload-path", relative, "personal absolute path"))
        if path.suffix.lower() != ".md":
            continue
        for raw_link in MARKDOWN_LINK_PATTERN.findall(text):
            link = raw_link.strip().split("#", 1)[0]
            if not link or link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if link.lower().startswith("file:///") or re.match(r"(?i)^[a-z]:[\\/]", link):
                problems.append(issue("payload-link", relative, f"non-portable link: {raw_link}"))
                continue
            candidate = (path.parent / link.replace("%20", " ")).resolve()
            if candidate.suffix.lower() == ".md" and not candidate.exists():
                problems.append(issue("payload-link", relative, f"missing target: {raw_link}"))
    return problems


def build_payload(
    host: str,
    profile: str = "general",
    repo_root: Path = REPO_ROOT,
    output_root: Path | None = None,
) -> Path:
    if host not in SUPPORTED_HOSTS:
        raise AntiGravityError(f"Unsupported host: {host}")
    validation = validate_repository(repo_root)
    if not validation["ok"]:
        raise ValidationFailed(
            f"Canonical source has {validation['issue_count']} validation issue(s); run validate"
        )
    manifest = load_manifest(repo_root)
    if profile not in manifest["profiles"]:
        raise AntiGravityError(f"Unknown profile: {profile}")
    adapter = load_json(repo_root / "global" / "adapters" / host / "adapter.json")
    output_root = (output_root or repo_root / "dist").resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    final = output_root / host
    # Keep the sibling stage name short. Deep skill/reference trees can otherwise
    # cross the legacy Windows MAX_PATH boundary before atomic activation.
    stage = output_root / f".{host}-{uuid.uuid4().hex[:8]}"
    stage.mkdir(parents=True)
    try:
        instruction_source = repo_root / "global" / "GEMINI.md"
        instruction_target = stage / adapter["instruction_target"]
        instruction_target.parent.mkdir(parents=True, exist_ok=True)
        header = (
            f"<!-- Generated for {host} from canonical Anti-Gravity policy. "
            "Host authority and approval controls remain authoritative. -->\n\n"
        )
        instruction_target.write_text(
            header + instruction_source.read_text(encoding="utf-8-sig"),
            encoding="utf-8",
        )
        content_root = stage / adapter["content_root"]
        content_root.mkdir(parents=True, exist_ok=True)
        copy_entry(
            repo_root / "global" / "GLOBAL_MEMORY.md", content_root / "GLOBAL_MEMORY.md"
        )
        if (repo_root / "global" / "USER_PROFILE.md").exists():
            copy_entry(repo_root / "global" / "USER_PROFILE.md", stage / "USER_PROFILE.md")
        copy_entry(repo_root / "global" / "core", content_root / "core")
        copy_entry(repo_root / "global" / "memory", content_root / "memory")
        copy_entry(repo_root / "global" / "schemas", content_root / "schemas")

        selected_profiles = {"general", profile}
        registry_destinations = {
            "skills": Path(adapter["skills_target"]),
            "workflows": Path(adapter["workflows_target"]),
            "context_templates": Path("context_templates"),
            "baselines": Path("baselines"),
            "templates": Path("global_templates"),
        }
        for registry_name, destination_root in registry_destinations.items():
            for entry in manifest[registry_name]:
                if not selected_profiles.intersection(entry["profiles"]):
                    continue
                source = repo_root / entry["path"]
                if registry_name == "skills":
                    destination = content_root / destination_root / entry["id"]
                else:
                    destination = content_root / destination_root / source.name
                ignores = ("skills",) if registry_name == "skills" and entry["id"] == "seedance" else ()
                copy_entry(source, destination, additional_ignores=ignores)

        copy_entry(repo_root / "global" / "manifest.yaml", stage / "manifest.json")
        if (repo_root / "global" / "reference").exists():
            copy_entry(repo_root / "global" / "reference", content_root / "reference")
        if profile == "spatial" and (repo_root / "global" / "design-audit").exists():
            copy_entry(repo_root / "global" / "design-audit", content_root / "design-audit")
        copy_entry(
            repo_root / "global" / "adapters" / host / "adapter.json",
            stage / "adapter.json",
        )
        copy_entry(
            repo_root / "global" / "profiles" / profile / "profile.json",
            stage / "profile.json",
        )
        payload_problems = validate_payload(stage)
        if payload_problems:
            summary = "; ".join(
                f"{problem['path']}: {problem['message']}" for problem in payload_problems[:10]
            )
            raise ValidationFailed(
                f"Generated {host}/{profile} payload has {len(payload_problems)} issue(s): {summary}"
            )
        if final.exists():
            shutil.rmtree(final)
        stage.replace(final)
        return final
    except Exception:
        shutil.rmtree(stage, ignore_errors=True)
        raise


def resolve_install_root(target: Path) -> Path:
    base = target.expanduser().resolve()
    home = Path.home().resolve()
    anchor = Path(base.anchor).resolve()
    if base in {home, anchor}:
        raise InstallationRefused(
            "Refusing a home or filesystem-root target; select a host configuration directory"
        )
    if base.name.lower() == "antigravity":
        install_root = base
    else:
        install_root = base / "antigravity"
    if install_root == base.parent or not install_root.is_relative_to(base):
        raise InstallationRefused("Resolved namespace escaped the selected target")
    return install_root


def installation_changes(payload: Path, install_root: Path) -> dict[str, list[str]]:
    source_files = file_map(payload)
    target_files = file_map(install_root)
    additions: list[str] = []
    replacements: list[str] = []
    unchanged: list[str] = []
    removals = sorted(set(target_files) - set(source_files))
    for relative, source in sorted(source_files.items()):
        target = target_files.get(relative)
        if target is None:
            additions.append(relative)
        elif sha256_file(source) == sha256_file(target):
            unchanged.append(relative)
        else:
            replacements.append(relative)
    return {
        "add": additions,
        "replace": replacements,
        "remove_from_namespace": removals,
        "unchanged": unchanged,
    }


def install_payload(
    payload: Path,
    target: Path,
    host: str,
    dry_run: bool,
    assume_yes: bool,
) -> dict[str, Any]:
    payload = payload.resolve()
    if not payload.is_dir():
        raise InstallationRefused(f"Payload does not exist: {payload}")
    if host not in SUPPORTED_HOSTS:
        raise InstallationRefused(f"Unsupported host: {host}")
    install_root = resolve_install_root(target)
    changes = installation_changes(payload, install_root)
    result: dict[str, Any] = {
        "status": "dry-run" if dry_run else "pending",
        "host": host,
        "target": str(install_root),
        "changes": changes,
        "backup": None,
    }
    if dry_run:
        return result
    if not assume_yes:
        raise InstallationRefused(
            "Installation requires explicit confirmation; rerun with --yes after reviewing --dry-run"
        )

    parent = install_root.parent
    parent.mkdir(parents=True, exist_ok=True)
    stage = parent / f".antigravity-stage-{uuid.uuid4().hex}"
    backup_root = parent / ".antigravity-backups"
    backup = backup_root / utc_timestamp()
    activated_existing = False
    try:
        shutil.copytree(payload, stage)
        if install_root.exists():
            backup_root.mkdir(parents=True, exist_ok=True)
            install_root.replace(backup)
            activated_existing = True
            result["backup"] = str(backup)
        stage.replace(install_root)
        result["status"] = "installed"
        return result
    except Exception:
        shutil.rmtree(stage, ignore_errors=True)
        if activated_existing and backup.exists() and not install_root.exists():
            backup.replace(install_root)
        raise


def resolve_codex_home(target: Path) -> Path:
    """Validate a Codex home for direct global instruction integration."""
    base = target.expanduser().resolve()
    home = Path.home().resolve()
    anchor = Path(base.anchor).resolve()
    if base in {home, anchor}:
        raise InstallationRefused(
            "Refusing a home or filesystem-root Codex target; select the Codex home directory"
        )
    if base.name.lower() != ".codex" and not (base / "config.toml").exists():
        raise InstallationRefused(
            "Direct Codex integration requires an existing .codex/CODEX_HOME directory"
        )
    if not base.is_relative_to(base.anchor):
        raise InstallationRefused("Resolved Codex home escaped its filesystem anchor")
    return base


def codex_global_file_map(payload: Path, codex_home: Path) -> dict[Path, Path]:
    """Return only the explicit Codex discovery files/directories to replace."""
    mapping: dict[Path, Path] = {}
    for source_name, target_name in (
        (Path("AGENTS.md"), Path("AGENTS.md")),
        (Path("USER_PROFILE.md"), Path("USER_PROFILE.md")),
        (Path(".agents") / "GLOBAL_MEMORY.md", Path("GLOBAL_MEMORY.md")),
    ):
        source = payload / source_name
        if source.exists():
            mapping[source] = codex_home / target_name
    for source_root, target_root in (
        (payload / ".agents" / "skills", codex_home / "skills"),
        (payload / ".agents" / "workflows", codex_home / "workflows"),
    ):
        if not source_root.exists():
            continue
        for source in sorted(source_root.iterdir()):
            mapping[source] = target_root / source.name
    return mapping


def codex_global_changes(payload: Path, codex_home: Path) -> dict[str, list[str]]:
    mapping = codex_global_file_map(payload, codex_home)
    additions: list[str] = []
    replacements: list[str] = []
    unchanged: list[str] = []
    for source, target in mapping.items():
        label = str(target.relative_to(codex_home))
        if not target.exists():
            additions.append(label)
        elif source.is_file() and target.is_file() and sha256_file(source) == sha256_file(target):
            unchanged.append(label)
        else:
            replacements.append(label)
    return {"add": additions, "replace": replacements, "unchanged": unchanged}


def install_codex_global(
    payload: Path,
    target: Path,
    dry_run: bool,
    assume_yes: bool,
) -> dict[str, Any]:
    """Install generated Codex instructions while preserving unrelated Codex state."""
    payload = payload.resolve()
    codex_home = resolve_codex_home(target)
    mapping = codex_global_file_map(payload, codex_home)
    changes = codex_global_changes(payload, codex_home)
    result: dict[str, Any] = {
        "status": "dry-run" if dry_run else "pending",
        "host": "codex",
        "target": str(codex_home),
        "changes": changes,
        "namespace": str(codex_home / "antigravity"),
        "backup": None,
    }
    if dry_run:
        return result
    if not assume_yes:
        raise InstallationRefused(
            "Direct Codex integration requires explicit confirmation; rerun with --yes after reviewing --dry-run"
        )

    timestamp = utc_timestamp()
    backup_root = codex_home / ".antigravity-backups" / timestamp
    stage_root = codex_home / f".antigravity-codex-stage-{uuid.uuid4().hex}"
    namespace_source = stage_root / "namespace"
    activated: list[tuple[Path, Path]] = []
    try:
        namespace_source.mkdir(parents=True)
        shutil.copytree(payload, namespace_source)
        for source, target_path in mapping.items():
            staged = stage_root / "direct" / target_path.relative_to(codex_home)
            if source.is_dir():
                shutil.copytree(source, staged)
            else:
                staged.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, staged)
        for source, target_path in mapping.items():
            if target_path.exists():
                backup_path = backup_root / target_path.relative_to(codex_home)
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                target_path.replace(backup_path)
            staged = stage_root / "direct" / target_path.relative_to(codex_home)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            staged.replace(target_path)
            activated.append((target_path, backup_root / target_path.relative_to(codex_home)))
        namespace_target = codex_home / "antigravity"
        if namespace_target.exists():
            namespace_backup = backup_root / "antigravity"
            namespace_backup.parent.mkdir(parents=True, exist_ok=True)
            namespace_target.replace(namespace_backup)
        namespace_source.replace(namespace_target)
        record = {
            "schema_version": 1,
            "host": "codex",
            "installed_at": datetime.now(timezone.utc).isoformat(),
            "payload": str(payload),
            "codex_home": str(codex_home),
            "backup": str(backup_root),
            "direct_targets": sorted(changes["add"] + changes["replace"]),
        }
        write_json_atomic(namespace_target / "installation.json", record)
        result["backup"] = str(backup_root) if backup_root.exists() else None
        result["status"] = "installed"
        return result
    except Exception:
        for target_path, backup_path in reversed(activated):
            if target_path.exists():
                if target_path.is_dir():
                    shutil.rmtree(target_path)
                else:
                    target_path.unlink()
            if backup_path.exists():
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                backup_path.replace(target_path)
        shutil.rmtree(stage_root, ignore_errors=True)
        raise


def print_validation(result: dict[str, Any], as_json: bool) -> None:
    if as_json:
        print(json.dumps(result, indent=2))
        return
    if result["ok"]:
        print("Anti-Gravity OS validation passed.")
        return
    print(f"Anti-Gravity OS validation found {result['issue_count']} issue(s):")
    for problem in result["issues"]:
        print(f"- [{problem['code']}] {problem['path']}: {problem['message']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Anti-Gravity OS development CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="Validate canonical source")
    validate_parser.add_argument("--json", action="store_true", help="Emit JSON")

    build_parser_command = subparsers.add_parser("build", help="Build a host payload")
    build_parser_command.add_argument("--host", required=True, choices=SUPPORTED_HOSTS)
    build_parser_command.add_argument("--profile", default="general")
    build_parser_command.add_argument("--output", type=Path)

    install_parser = subparsers.add_parser("install", help="Safely install a host payload")
    install_parser.add_argument("--host", required=True, choices=SUPPORTED_HOSTS)
    install_parser.add_argument("--profile", default="general")
    install_parser.add_argument("--target", required=True, type=Path)
    install_parser.add_argument("--dry-run", action="store_true")
    install_parser.add_argument("--yes", action="store_true")
    install_parser.add_argument(
        "--codex-global",
        action="store_true",
        help="For host=codex, install into Codex discovery locations plus a rollback namespace",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = build_parser().parse_args(argv)
    try:
        if args.command == "validate":
            result = validate_repository()
            print_validation(result, args.json)
            return 0 if result["ok"] else 1
        if args.command == "build":
            payload = build_payload(args.host, args.profile, output_root=args.output)
            print(json.dumps({"status": "built", "payload": str(payload)}, indent=2))
            return 0
        if args.command == "install":
            if args.dry_run:
                with tempfile.TemporaryDirectory(prefix="antigravity-dry-run-") as directory:
                    payload = build_payload(
                        args.host,
                        args.profile,
                        output_root=Path(directory),
                    )
                    result = (
                        install_codex_global(payload, args.target, True, False)
                        if args.codex_global
                        else install_payload(payload, args.target, args.host, True, False)
                    )
            else:
                payload = build_payload(args.host, args.profile)
                result = (
                    install_codex_global(payload, args.target, False, args.yes)
                    if args.codex_global
                    else install_payload(payload, args.target, args.host, False, args.yes)
                )
            print(json.dumps(result, indent=2))
            return 0
    except AntiGravityError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
