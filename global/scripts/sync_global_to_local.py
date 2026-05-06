from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


GLOBAL_ROOT = Path(r"{{USER_HOME_PATH}}\.gemini\antigravity")
LOCAL_ROOT = Path(r"{{USER_HOME_PATH}}\antigravitygold")


MAPPINGS = [
    ("skills", "skills"),
    ("contexts", "contexts"),
    ("core", "core"),
    ("memory", "memory"),
    ("rubrics", "rubric"),
    ("benchmarks", "benchmark"),
    ("global_templates", "templates"),
    ("workflows", "workflows"),
    ("global_workflows", ".agents/workflows"),
]


TEXT_EXTENSIONS = {
    ".md",
    ".mdx",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".cfg",
    ".ps1",
    ".py",
}


REPLACEMENTS = [
    (r"{{USER_HOME_PATH}}\.gemini\antigravity", r"{{USER_HOME_PATH}}\antigravitygold"),
    (r"{{USER_HOME_PATH}}\.gemini\antigravity", r"{{USER_HOME_PATH}}\antigravitygold"),
    (r"{{USER_HOME_PATH}}/.gemini/antigravity", r"{{USER_HOME_PATH}}/antigravitygold"),
    (r"{{USER_HOME_PATH}}/.gemini/antigravity", r"{{USER_HOME_PATH}}/antigravitygold"),
    (r"/global_workflows/", r"/.agents/workflows/"),
    (r"/global_templates/", r"/templates/"),
    (r"/rubrics/", r"/rubric/"),
    (r"/benchmarks/", r"/benchmark/"),
    (r".antigravity/rubrics/", r".antigravity/rubric/"),
    (r".antigravity/benchmarks/", r".antigravity/benchmark/"),
    (r"skills/context-formatting/SKILL.md", r"skills/skill-context-formatting.md"),
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_map(root: Path) -> dict[str, Path]:
    if not root.exists():
        return {}
    result: dict[str, Path] = {}
    for p in root.rglob("*"):
        if p.is_file():
            result[p.relative_to(root).as_posix()] = p
    return result


def remap_relative_path(global_rel: str, rel: str) -> str | None:
    if global_rel != "skills":
        return rel

    if rel == "context-formatting/SKILL.md":
        return "skill-context-formatting.md"

    if rel.endswith("/SKILL.md"):
        return None

    return rel


def maybe_transform_text(path: Path, data: bytes) -> bytes:
    if path.parent.name == "global_templates" and path.name == "README.md":
        return data

    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return data
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return data

    for old, new in REPLACEMENTS:
        text = text.replace(old, new)

    text = re.sub(r"/skills/([a-z0-9-]+)/SKILL\.md", r"/skills/skill-\1.md", text)

    return text.encode("utf-8")


def sync(overwrite_only: bool = False) -> dict:
    copied = 0
    updated = 0
    unchanged = 0
    missing_targets = 0
    errors: list[str] = []
    section_stats: dict[str, dict[str, int]] = {}

    for global_rel, local_rel in MAPPINGS:
        source_dir = GLOBAL_ROOT / global_rel
        target_dir = LOCAL_ROOT / local_rel

        key = f"{global_rel}->{local_rel}"
        section_stats[key] = {
            "source_files": 0,
            "written": 0,
            "unchanged": 0,
            "missing_source_dir": 0,
        }

        if not source_dir.exists():
            section_stats[key]["missing_source_dir"] = 1
            missing_targets += 1
            continue

        target_dir.mkdir(parents=True, exist_ok=True)

        for rel, src_path in file_map(source_dir).items():
            mapped_rel = remap_relative_path(global_rel, rel)
            if mapped_rel is None:
                continue

            section_stats[key]["source_files"] += 1

            dst_path = target_dir / mapped_rel
            dst_path.parent.mkdir(parents=True, exist_ok=True)

            try:
                src_bytes = src_path.read_bytes()
                out_bytes = maybe_transform_text(src_path, src_bytes)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"read-fail {src_path}: {exc}")
                continue

            if dst_path.exists():
                try:
                    dst_bytes = dst_path.read_bytes()
                except Exception as exc:  # noqa: BLE001
                    errors.append(f"read-fail {dst_path}: {exc}")
                    continue
                if sha256_bytes(dst_bytes) == sha256_bytes(out_bytes):
                    unchanged += 1
                    section_stats[key]["unchanged"] += 1
                    continue
                if overwrite_only is False:
                    try:
                        dst_path.write_bytes(out_bytes)
                        updated += 1
                        section_stats[key]["written"] += 1
                    except Exception as exc:  # noqa: BLE001
                        errors.append(f"write-fail {dst_path}: {exc}")
            else:
                if overwrite_only:
                    continue
                try:
                    dst_path.write_bytes(out_bytes)
                    copied += 1
                    section_stats[key]["written"] += 1
                except Exception as exc:  # noqa: BLE001
                    errors.append(f"write-fail {dst_path}: {exc}")

    return {
        "copied_new": copied,
        "updated_existing": updated,
        "unchanged": unchanged,
        "missing_source_dirs": missing_targets,
        "section_stats": section_stats,
        "errors": errors,
    }


def audit() -> dict:
    summary: dict[str, dict] = {}
    totals = {"same": 0, "different": 0, "missing_in_local": 0}

    for global_rel, local_rel in MAPPINGS:
        source_dir = GLOBAL_ROOT / global_rel
        target_dir = LOCAL_ROOT / local_rel
        key = f"{global_rel}->{local_rel}"

        if not source_dir.exists():
            summary[key] = {
                "same": 0,
                "different": 0,
                "missing_in_local": 0,
                "missing_source_dir": True,
                "sample_different": [],
                "sample_missing_in_local": [],
            }
            continue

        src_files = file_map(source_dir)
        diff: list[str] = []
        missing: list[str] = []
        same = 0

        for rel, src_path in sorted(src_files.items()):
            mapped_rel = remap_relative_path(global_rel, rel)
            if mapped_rel is None:
                continue

            dst_path = target_dir / mapped_rel
            src_bytes = maybe_transform_text(src_path, src_path.read_bytes())
            if not dst_path.exists():
                missing.append(mapped_rel)
                continue
            dst_bytes = dst_path.read_bytes()
            if sha256_bytes(src_bytes) == sha256_bytes(dst_bytes):
                same += 1
            else:
                diff.append(mapped_rel)

        summary[key] = {
            "same": same,
            "different": len(diff),
            "missing_in_local": len(missing),
            "sample_different": diff[:10],
            "sample_missing_in_local": missing[:10],
        }
        totals["same"] += same
        totals["different"] += len(diff)
        totals["missing_in_local"] += len(missing)

    return {"totals": totals, "sections": summary}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync global antigravity content to local"
    )
    parser.add_argument(
        "--audit-only", action="store_true", help="Only run audit and print JSON"
    )
    args = parser.parse_args()

    if args.audit_only:
        print(json.dumps(audit(), indent=2))
        return

    sync_result = sync(overwrite_only=False)
    audit_result = audit()
    print(json.dumps({"sync": sync_result, "audit": audit_result}, indent=2))


if __name__ == "__main__":
    main()
