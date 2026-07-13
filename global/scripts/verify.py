#!/usr/bin/env python3
"""
Master Verification Runner — Antigravity Gold
===============================================

Orchestrates all verification scripts in priority order.
This is the single entry point for project quality checks.

Usage:
    python scripts/verify.py <project_path>                    # Core checks only
    python scripts/verify.py <project_path> --full             # All checks
    python scripts/verify.py <project_path> --only security    # Single check
    python scripts/verify.py <project_path> --skip performance # Skip one check

Priority Order:
    P0: Security Scan (secrets, dangerous code, env files)
    P1: Code Quality (console.log, empty catch, unhandled fetch)
    P2: Accessibility Audit (WCAG basics on HTML files)
    P3: Performance Check (file sizes, bundle analysis)

All scripts are located in: scripts/checks/
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Optional

# ANSI colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def print_header(text: str):
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(60)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.END}\n")


def print_step(text: str):
    print(f"{Colors.BOLD}{Colors.BLUE}🔄 {text}{Colors.END}")


def print_success(text: str):
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")


def print_warning(text: str):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")


def print_error(text: str):
    print(f"{Colors.RED}❌ {text}{Colors.END}")


# Check definitions: (name, script_filename, is_critical, description)
CHECKS = [
    ("Security Scan", "security_scan.py", True, "Secrets, dangerous code, env file exposure"),
    ("Code Quality", "code_quality.py", False, "Console logs, empty catch, unhandled errors"),
    ("Accessibility", "accessibility_audit.py", False, "WCAG basics on HTML files"),
    ("Performance", "performance_check.py", False, "File sizes, bundle analysis, image optimization"),
]


def find_scripts_dir() -> Path:
    """Find the checks directory relative to this script."""
    return Path(__file__).parent / "checks"


def run_check(name: str, script_path: Path, project_path: str) -> dict:
    """Run a single verification script."""
    if not script_path.exists():
        print_warning(f"{name}: Script not found at {script_path}")
        return {"name": name, "passed": True, "skipped": True, "duration": 0}

    print_step(f"Running: {name}")
    start = datetime.now()

    try:
        result = subprocess.run(
            [sys.executable, str(script_path), project_path],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env={**os.environ, "PYTHONUTF8": "1"},
            timeout=300,  # 5 minute timeout
        )

        duration = (datetime.now() - start).total_seconds()
        passed = result.returncode == 0

        if passed:
            print_success(f"{name}: PASSED ({duration:.1f}s)")
        else:
            print_error(f"{name}: ISSUES FOUND ({duration:.1f}s)")

        return {
            "name": name,
            "passed": passed,
            "output": result.stdout,
            "error": result.stderr,
            "skipped": False,
            "duration": duration,
        }

    except subprocess.TimeoutExpired:
        duration = (datetime.now() - start).total_seconds()
        print_error(f"{name}: TIMEOUT (>{duration:.0f}s)")
        return {"name": name, "passed": False, "skipped": False, "duration": duration}

    except Exception as e:
        duration = (datetime.now() - start).total_seconds()
        print_error(f"{name}: ERROR - {str(e)}")
        return {"name": name, "passed": False, "skipped": False, "duration": duration}


def print_summary(results: List[dict], start_time: datetime) -> bool:
    """Print final summary and return True if all passed."""
    total_duration = (datetime.now() - start_time).total_seconds()

    print_header("📊 VERIFICATION SUMMARY")

    passed = sum(1 for r in results if r["passed"] and not r.get("skipped"))
    failed = sum(1 for r in results if not r["passed"] and not r.get("skipped"))
    skipped = sum(1 for r in results if r.get("skipped"))

    print(f"Duration: {total_duration:.1f}s")
    print(f"Total Checks: {len(results)}")
    print(f"{Colors.GREEN}✅ Passed: {passed}{Colors.END}")
    print(f"{Colors.RED}❌ Issues: {failed}{Colors.END}")
    if skipped:
        print(f"{Colors.YELLOW}⏭️  Skipped: {skipped}{Colors.END}")

    print()

    for r in results:
        if r.get("skipped"):
            status = f"{Colors.YELLOW}⏭️ {Colors.END}"
        elif r["passed"]:
            status = f"{Colors.GREEN}✅{Colors.END}"
        else:
            status = f"{Colors.RED}❌{Colors.END}"

        duration_str = f"({r.get('duration', 0):.1f}s)" if not r.get("skipped") else ""
        print(f"  {status} {r['name']} {duration_str}")

    print()

    if failed > 0:
        print_error(f"{failed} check(s) found issues — review output above")

        # Print failed check outputs
        for r in results:
            if not r["passed"] and not r.get("skipped") and r.get("output"):
                print(f"\n{Colors.BOLD}--- {r['name']} Output ---{Colors.END}")
                # Print last 20 lines of output (summary section)
                output_lines = r["output"].strip().split('\n')
                for line in output_lines[-20:]:
                    print(f"  {line}")

        return False
    else:
        print_success("Baseline checks passed. Deployment readiness requires project-native verification and approval.")
        return True


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(
        description="Antigravity Gold — Project Verification System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/verify.py .                       # Run all checks
  python scripts/verify.py . --only security       # Run security only
  python scripts/verify.py . --skip performance    # Skip performance
  python scripts/verify.py . --stop-on-fail        # Stop at first failure
        """
    )
    parser.add_argument("project", help="Project path to verify")
    parser.add_argument("--only", help="Run only this check (security, quality, accessibility, performance)")
    parser.add_argument("--skip", nargs='*', default=[], help="Skip these checks")
    parser.add_argument("--stop-on-fail", action="store_true", help="Stop on first failure")
    parser.add_argument("--full", action="store_true", help="Run all checks (default behavior)")

    args = parser.parse_args()

    project_path = Path(args.project).resolve()
    if not project_path.exists():
        print_error(f"Project path does not exist: {project_path}")
        sys.exit(1)

    scripts_dir = find_scripts_dir()
    if not scripts_dir.exists():
        print_error(f"Checks directory not found: {scripts_dir}")
        sys.exit(1)

    print_header("🚀 ANTIGRAVITY GOLD — PROJECT VERIFICATION")
    print(f"Project: {project_path}")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    start_time = datetime.now()
    results = []

    # Filter checks based on --only and --skip flags
    skip_names = [s.lower() for s in args.skip]

    for name, script_file, is_critical, description in CHECKS:
        short_name = name.lower().split()[0]  # "Security", "Code", "Accessibility", "Performance"

        # --only filter
        if args.only and args.only.lower() != short_name:
            continue

        # --skip filter
        if short_name in skip_names:
            results.append({"name": name, "passed": True, "skipped": True, "duration": 0})
            continue

        script_path = scripts_dir / script_file
        result = run_check(name, script_path, str(project_path))
        results.append(result)

        # Stop on critical failure if flag set
        if args.stop_on_fail and is_critical and not result["passed"] and not result.get("skipped"):
            print_error(f"CRITICAL: {name} failed. Stopping verification.")
            break

    all_passed = print_summary(results, start_time)
    sys.exit(0 if all_passed else 1)


if __name__ == '__main__':
    main()
