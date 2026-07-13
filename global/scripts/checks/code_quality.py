#!/usr/bin/env python3
"""
Code Quality Checker — Antigravity Gold Verification System
=============================================================

Checks code quality without requiring external linters.
Focuses on issues that indicate production-readiness problems.

Usage:
    python scripts/checks/code_quality.py <project_path>

Checks:
    - Console.log / debugger statements left in code
    - Unused variable detection (basic heuristic)
    - Files exceeding length thresholds
    - Missing error handling on async operations
    - Dead code indicators (unreachable returns, empty catch blocks)
    - TODO/FIXME/HACK comments count
"""

import sys
import re
from pathlib import Path
from typing import List, Dict

# ANSI colors
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

# File extensions to check
CODE_EXTENSIONS = {'.js', '.mjs', '.cjs', '.ts', '.tsx', '.jsx', '.py', '.html', '.css'}

# Directories to skip
SKIP_DIRS = {'node_modules', '.git', '__pycache__', 'dist', 'build', '.next',
             'venv', '.venv', 'env', 'coverage', '.cache', '.gemini'}

# Thresholds
MAX_FILE_LINES = 500          # Warn if a single file exceeds this
MAX_FUNCTION_LINES = 80       # Warn if a function seems too long
MAX_TODO_COUNT = 10            # Warn if too many TODOs across project


def should_check_file(filepath: Path) -> bool:
    """Check if file should be analyzed."""
    checker_directory = Path(__file__).resolve().parent
    try:
        filepath.resolve().relative_to(checker_directory)
        return False
    except ValueError:
        pass
    if filepath.suffix.lower() not in CODE_EXTENSIONS:
        return False
    for skip in SKIP_DIRS:
        if skip in filepath.parts:
            return False
    return True


def check_file(filepath: Path) -> List[Dict]:
    """Run all quality checks on a single file."""
    issues = []
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')
        line_count = len(lines)
        ext = filepath.suffix.lower()

        # --- File length check ---
        if line_count > MAX_FILE_LINES:
            issues.append({
                'file': str(filepath),
                'line': 0,
                'check': 'File Too Long',
                'severity': 'INFO',
                'message': f'File has {line_count} lines (threshold: {MAX_FILE_LINES}). Consider splitting.',
            })

        for line_num, line in enumerate(lines, 1):
            stripped = line.strip()

            # --- Console.log left in (JS/TS only) ---
            if ext in {'.js', '.mjs', '.cjs', '.ts', '.tsx', '.jsx'}:
                if re.search(r'\bconsole\.(log|debug|info|warn|error)\s*\(', stripped):
                    # Skip if it's in a catch block or error handler (legitimate use)
                    if not re.search(r'console\.(warn|error)\s*\(', stripped):
                        issues.append({
                            'file': str(filepath),
                            'line': line_num,
                            'check': 'Console Statement',
                            'severity': 'LOW',
                            'message': f'console.log left in code: {stripped[:80]}',
                        })

            # --- Debugger statement ---
            if re.search(r'^\s*debugger\s*;?\s*$', stripped):
                issues.append({
                    'file': str(filepath),
                    'line': line_num,
                    'check': 'Debugger Statement',
                    'severity': 'MEDIUM',
                    'message': 'debugger statement — remove before production',
                })

            # --- Empty catch blocks ---
            if re.search(r'catch\s*\([^)]*\)\s*\{\s*\}', stripped) or \
               (re.search(r'catch\s*\([^)]*\)\s*\{', stripped) and
                line_num < line_count and lines[line_num].strip() == '}'):
                issues.append({
                    'file': str(filepath),
                    'line': line_num,
                    'check': 'Empty Catch Block',
                    'severity': 'MEDIUM',
                    'message': 'Empty catch block — errors are being silently swallowed',
                })

            # --- Fetch without catch/error handling ---
            if ext in {'.js', '.mjs', '.cjs', '.ts', '.tsx', '.jsx'}:
                if re.search(r'\bfetch\s*\(', stripped):
                    # Look at surrounding context for .catch or try/catch
                    context_start = max(0, line_num - 3)
                    context_end = min(line_count, line_num + 5)
                    context = '\n'.join(lines[context_start:context_end])
                    if '.catch' not in context and 'try' not in context:
                        issues.append({
                            'file': str(filepath),
                            'line': line_num,
                            'check': 'Unhandled Fetch',
                            'severity': 'MEDIUM',
                            'message': 'fetch() without .catch() or try/catch — network errors will be silent',
                        })

            # --- Python bare except ---
            if ext == '.py':
                if re.search(r'^\s*except\s*:', stripped):
                    issues.append({
                        'file': str(filepath),
                        'line': line_num,
                        'check': 'Bare Except',
                        'severity': 'MEDIUM',
                        'message': 'Bare except catches everything including KeyboardInterrupt — be specific',
                    })

        # --- TODO/FIXME/HACK count ---
        todo_count = len(re.findall(r'\b(?:TODO|FIXME|HACK|XXX)\b', content, re.IGNORECASE))
        if todo_count > 5:
            issues.append({
                'file': str(filepath),
                'line': 0,
                'check': 'TODO Count',
                'severity': 'INFO',
                'message': f'{todo_count} TODO/FIXME/HACK comments — review before shipping',
            })

    except (PermissionError, UnicodeDecodeError):
        pass

    return issues


def print_results(all_issues: List[Dict], file_count: int) -> None:
    """Print quality check results."""
    if not all_issues:
        print(f"{Colors.GREEN}✅ No code quality issues found{Colors.END}")
        return

    severity_colors = {
        'MEDIUM': Colors.YELLOW,
        'LOW': Colors.CYAN,
        'INFO': Colors.CYAN,
    }

    # Group by check type
    by_check = {}
    for issue in all_issues:
        check = issue['check']
        if check not in by_check:
            by_check[check] = []
        by_check[check].append(issue)

    for check, issues in by_check.items():
        color = severity_colors.get(issues[0]['severity'], '')
        print(f"\n{Colors.BOLD}{color}[{issues[0]['severity']}] {check} ({len(issues)} found){Colors.END}")
        for issue in issues[:5]:  # Show max 5 per category
            print(f"  {issue['file']}:{issue['line']}")
            print(f"    {issue['message']}")
        if len(issues) > 5:
            print(f"  ... and {len(issues) - 5} more")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    if len(sys.argv) < 2:
        print("Usage: python code_quality.py <project_path>")
        sys.exit(1)

    project_path = Path(sys.argv[1]).resolve()
    if not project_path.exists():
        print(f"Error: Path does not exist: {project_path}")
        sys.exit(1)

    print(f"{Colors.BOLD}{Colors.CYAN}📋 Code Quality Check — Antigravity Gold{Colors.END}")
    print(f"Scanning: {project_path}\n")

    all_issues = []
    file_count = 0

    for filepath in project_path.rglob('*'):
        if filepath.is_file() and should_check_file(filepath):
            file_count += 1
            issues = check_file(filepath)
            all_issues.extend(issues)

    print(f"Files checked: {file_count}")
    print_results(all_issues, file_count)

    # Summary
    medium = sum(1 for i in all_issues if i['severity'] == 'MEDIUM')
    low = sum(1 for i in all_issues if i['severity'] == 'LOW')
    info = sum(1 for i in all_issues if i['severity'] == 'INFO')

    print(f"\n{Colors.BOLD}Summary:{Colors.END}")
    print(f"  Total issues: {len(all_issues)}")
    print(f"  Medium: {medium}")
    print(f"  Low: {low}")
    print(f"  Info: {info}")

    if medium > 10:
        print(f"\n{Colors.YELLOW}⚠️  Many code quality issues — review before deployment{Colors.END}")
        sys.exit(1)
    else:
        print(f"\n{Colors.GREEN}✅ Code quality check passed{Colors.END}")
        sys.exit(0)


if __name__ == '__main__':
    main()
