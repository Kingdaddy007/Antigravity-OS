from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ScannerBoundaryTests(unittest.TestCase):
    def test_security_scanner_does_not_scan_its_own_rule_definitions(self) -> None:
        module_path = REPO_ROOT / "global" / "scripts" / "checks" / "security_scan.py"
        scanner = load_module("security_scan_under_test", module_path)
        self.assertFalse(scanner.should_scan_file(module_path))

    def test_security_scanner_still_scans_project_source(self) -> None:
        module_path = REPO_ROOT / "global" / "scripts" / "checks" / "security_scan.py"
        scanner = load_module("security_scan_project_test", module_path)
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "application.py"
            source.write_text("print('safe')\n", encoding="utf-8")
            self.assertTrue(scanner.should_scan_file(source))

    def test_security_scanner_distinguishes_safe_and_unsafe_fixtures(self) -> None:
        module_path = REPO_ROOT / "global" / "scripts" / "checks" / "security_scan.py"
        scanner = load_module("security_scan_fixture_test", module_path)
        patterns = scanner.SECRET_PATTERNS + scanner.DANGEROUS_CODE_PATTERNS
        with tempfile.TemporaryDirectory() as directory:
            safe = Path(directory) / "safe.py"
            unsafe = Path(directory) / "unsafe.py"
            safe.write_text("value = int('42')\n", encoding="utf-8")
            dangerous_source = "result = ev" + "al(user_input)\n"
            unsafe.write_text(dangerous_source, encoding="utf-8")
            self.assertEqual([], scanner.scan_file(safe, patterns))
            findings = scanner.scan_file(unsafe, patterns)
            expected_pattern = "ev" + "al() Usage"
            self.assertTrue(any(item["pattern"] == expected_pattern for item in findings))

    def test_code_quality_scanner_does_not_scan_its_own_rules(self) -> None:
        module_path = REPO_ROOT / "global" / "scripts" / "checks" / "code_quality.py"
        scanner = load_module("code_quality_under_test", module_path)
        self.assertFalse(scanner.should_check_file(module_path))

    def test_code_quality_scanner_detects_debugger_fixture(self) -> None:
        module_path = REPO_ROOT / "global" / "scripts" / "checks" / "code_quality.py"
        scanner = load_module("code_quality_fixture_test", module_path)
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "unsafe.js"
            source.write_text("debug" + "ger;\n", encoding="utf-8")
            findings = scanner.check_file(source)
            expected_check = "Debug" + "ger Statement"
            self.assertTrue(any(item["check"] == expected_check for item in findings))


if __name__ == "__main__":
    unittest.main()
