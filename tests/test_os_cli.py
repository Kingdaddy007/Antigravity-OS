from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "global" / "scripts" / "os.py"


def load_os_module():
    spec = importlib.util.spec_from_file_location("antigravity_os_cli", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load Anti-Gravity OS CLI")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class InstallerSafetyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.os_cli = load_os_module()
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.payload = self.root / "payload"
        self.payload.mkdir()
        (self.payload / "GEMINI.md").write_text("canonical\n", encoding="utf-8")
        (self.payload / "skills").mkdir()
        (self.payload / "skills" / "example.md").write_text("skill\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_dry_run_never_writes(self) -> None:
        target = self.root / "shared-rules"
        target.mkdir()
        sentinel = target / "unrelated-user-rule.md"
        sentinel.write_text("keep me", encoding="utf-8")

        result = self.os_cli.install_payload(
            payload=self.payload,
            target=target,
            host="cursor",
            dry_run=True,
            assume_yes=False,
        )

        self.assertEqual("dry-run", result["status"])
        self.assertTrue(sentinel.exists())
        self.assertFalse((target / "antigravity").exists())

    def test_install_preserves_unrelated_files_and_backs_up_namespace(self) -> None:
        target = self.root / "shared-rules"
        target.mkdir()
        sentinel = target / "unrelated-user-rule.md"
        sentinel.write_text("keep me", encoding="utf-8")
        existing = target / "antigravity"
        existing.mkdir()
        (existing / "GEMINI.md").write_text("old\n", encoding="utf-8")

        result = self.os_cli.install_payload(
            payload=self.payload,
            target=target,
            host="cursor",
            dry_run=False,
            assume_yes=True,
        )

        self.assertEqual("installed", result["status"])
        self.assertEqual("keep me", sentinel.read_text(encoding="utf-8"))
        self.assertEqual(
            "canonical\n",
            (target / "antigravity" / "GEMINI.md").read_text(encoding="utf-8"),
        )
        backup = Path(result["backup"])
        self.assertTrue(backup.exists())
        self.assertEqual("old\n", (backup / "GEMINI.md").read_text(encoding="utf-8"))

    def test_non_dry_run_requires_confirmation(self) -> None:
        target = self.root / "shared-rules"
        target.mkdir()
        with self.assertRaises(self.os_cli.InstallationRefused):
            self.os_cli.install_payload(
                payload=self.payload,
                target=target,
                host="cursor",
                dry_run=False,
                assume_yes=False,
            )

    def test_home_directory_is_refused_as_base_target(self) -> None:
        with self.assertRaises(self.os_cli.InstallationRefused):
            self.os_cli.resolve_install_root(Path.home())


class MetadataTests(unittest.TestCase):
    def setUp(self) -> None:
        self.os_cli = load_os_module()

    def test_simple_yaml_parser_supports_workflow_lists(self) -> None:
        parsed = self.os_cli.parse_simple_yaml(
            """
id: debug-issue
version: 1
status: active
use_when:
  - A user asks for diagnosis.
  - A failing test needs isolation.
mutation_class: read_only
profiles: [general]
""".strip()
        )
        self.assertEqual("debug-issue", parsed["id"])
        self.assertEqual(1, parsed["version"])
        self.assertEqual(["general"], parsed["profiles"])
        self.assertEqual(2, len(parsed["use_when"]))

    def test_adapter_records_are_valid_json(self) -> None:
        for adapter_path in sorted((REPO_ROOT / "global" / "adapters").glob("*/adapter.json")):
            adapter = json.loads(adapter_path.read_text(encoding="utf-8"))
            self.assertEqual(adapter_path.parent.name, adapter["host"])
            self.assertEqual("antigravity", adapter["namespace"])

    def test_canonical_repository_passes_validation(self) -> None:
        result = self.os_cli.validate_repository(REPO_ROOT)
        self.assertEqual([], result["issues"])
        self.assertTrue(result["ok"])

    def test_every_host_builds_and_spatial_profile_is_optional(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            for host in self.os_cli.SUPPORTED_HOSTS:
                payload = self.os_cli.build_payload(
                    host=host,
                    profile="general",
                    repo_root=REPO_ROOT,
                    output_root=output,
                )
                adapter = json.loads(
                    (REPO_ROOT / "global" / "adapters" / host / "adapter.json").read_text(
                        encoding="utf-8"
                    )
                )
                self.assertTrue((payload / adapter["instruction_target"]).exists())
                content_root = payload / adapter["content_root"]
                for spatial_skill in (
                    "brand-strategy",
                    "cinematic-motion",
                    "cinematic-showroom-strategy",
                    "master-design-director",
                    "scroll-storyboard",
                    "spatial-experience-design",
                    "storytelling",
                ):
                    self.assertFalse(
                        (content_root / adapter["skills_target"] / spatial_skill).exists()
                    )
                self.assertFalse(
                    (content_root / adapter["skills_target"] / "seedance" / "skills").exists()
                )
                for spatial_workflow in (
                    "workflow-impeccable-animate.md",
                    "workflow-impeccable-craft.md",
                    "workflow-spatial-concept.md",
                    "workflow-spatial-design-ui.md",
                    "workflow-spatial-project-inception.md",
                    "workflow-storytelling.md",
                    "workflow-visual-brainstorm.md",
                ):
                    self.assertFalse(
                        (content_root / adapter["workflows_target"] / spatial_workflow).exists()
                    )

            spatial_payload = self.os_cli.build_payload(
                host="gemini",
                profile="spatial",
                repo_root=REPO_ROOT,
                output_root=output / "spatial",
            )
            self.assertTrue(
                (spatial_payload / "skills" / "spatial-experience-design").exists()
            )
            self.assertTrue(
                (spatial_payload / "workflows" / "workflow-impeccable-craft.md").exists()
            )

    def test_spatial_build_uses_windows_safe_sibling_stage_name(self) -> None:
        # A repository-length output root reproduces failures hidden by the much
        # shorter system temporary directory on Windows.
        with tempfile.TemporaryDirectory(prefix=".build-test-", dir=REPO_ROOT) as directory:
            payload = self.os_cli.build_payload(
                host="codex",
                profile="spatial",
                repo_root=REPO_ROOT,
                output_root=Path(directory),
            )
            self.assertTrue(
                payload.joinpath(
                    ".agents", "skills", "cinematic-motion", "SKILL.md"
                ).exists()
            )


class WorkflowStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.os_cli = load_os_module()

    def state(self, task_id: str) -> dict:
        return {
            "schema_version": 1,
            "task_id": task_id,
            "workflow_id": "build-feature",
            "mode": "implement",
            "status": "in_progress",
            "current_state": "execute-if-authorized",
            "completed_states": ["intake", "assess"],
            "owner": {"agent": task_id, "thread": task_id, "worktree": None},
            "workspace": "temporary",
            "lease": None,
            "evidence": [],
            "artifacts": [],
            "approvals": [],
            "blockers": [],
            "next_action": "Continue implementation.",
            "created_at": "2026-07-13T00:00:00Z",
            "updated_at": "2026-07-13T00:00:00Z",
            "archived": False,
        }

    def test_independent_tasks_receive_distinct_state_and_index_entries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            first = self.os_cli.write_workflow_state(workspace, self.state("task-one"))
            second = self.os_cli.write_workflow_state(workspace, self.state("task-two"))

            self.assertNotEqual(first, second)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            index = json.loads(
                (workspace / ".agents" / "workflows" / "index.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual("task-one.json", index["tasks"]["task-one"])
            self.assertEqual("task-two.json", index["tasks"]["task-two"])

    def test_invalid_task_id_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                self.os_cli.write_workflow_state(
                    Path(directory), self.state("../escaped-task")
                )


if __name__ == "__main__":
    unittest.main()
