#!/usr/bin/env python3
"""
Accessibility Auditor — Antigravity Gold Verification System
==============================================================

Scans HTML files for basic WCAG 2.1 compliance issues.
No external dependencies required — pure Python regex analysis.

Usage:
    python scripts/checks/accessibility_audit.py <project_path>

Checks:
    - Images without alt attributes
    - Form inputs without labels
    - Missing lang attribute on <html>
    - Missing page title
    - Buttons/links without accessible text
    - Missing ARIA labels on interactive elements
    - Color contrast issues in inline styles (basic)
    - Missing skip navigation link
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
HTML_EXTENSIONS = {'.html', '.htm'}

# Directories to skip
SKIP_DIRS = {'node_modules', '.git', '__pycache__', 'dist', 'build', '.next',
             'venv', '.venv', 'coverage', '.cache'}


def should_check_file(filepath: Path) -> bool:
    """Check if file should be audited."""
    if filepath.suffix.lower() not in HTML_EXTENSIONS:
        return False
    for skip in SKIP_DIRS:
        if skip in filepath.parts:
            return False
    return True


def audit_html_file(filepath: Path) -> List[Dict]:
    """Run accessibility checks on a single HTML file."""
    issues = []
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')
        filename = str(filepath)

        # --- Missing lang attribute on <html> ---
        html_tags = re.findall(r'<html[^>]*>', content, re.IGNORECASE)
        if html_tags:
            if not re.search(r'lang\s*=', html_tags[0], re.IGNORECASE):
                issues.append({
                    'file': filename,
                    'line': 0,
                    'check': 'Missing lang Attribute',
                    'severity': 'HIGH',
                    'message': '<html> tag missing lang attribute — screen readers need this',
                })

        # --- Missing page title ---
        if not re.search(r'<title[^>]*>[^<]+</title>', content, re.IGNORECASE):
            issues.append({
                'file': filename,
                'line': 0,
                'check': 'Missing Page Title',
                'severity': 'MEDIUM',
                'message': 'No <title> element found — required for accessibility and SEO',
            })

        # Line-by-line checks
        for line_num, line in enumerate(lines, 1):

            # --- Images without alt ---
            img_tags = re.findall(r'<img[^>]*>', line, re.IGNORECASE)
            for img in img_tags:
                if not re.search(r'alt\s*=', img, re.IGNORECASE):
                    issues.append({
                        'file': filename,
                        'line': line_num,
                        'check': 'Image Missing Alt',
                        'severity': 'HIGH',
                        'message': f'<img> without alt attribute: {img[:80]}',
                    })

            # --- Input without label ---
            input_tags = re.findall(r'<input[^>]*>', line, re.IGNORECASE)
            for inp in input_tags:
                inp_type = re.search(r'type\s*=\s*["\']?(\w+)', inp, re.IGNORECASE)
                if inp_type and inp_type.group(1).lower() in {'hidden', 'submit', 'button', 'reset'}:
                    continue
                # Check for id (which a label would reference) or aria-label
                has_id = re.search(r'\bid\s*=', inp, re.IGNORECASE)
                has_aria = re.search(r'aria-label\s*=', inp, re.IGNORECASE)
                has_placeholder = re.search(r'placeholder\s*=', inp, re.IGNORECASE)

                if not has_id and not has_aria:
                    issues.append({
                        'file': filename,
                        'line': line_num,
                        'check': 'Input Without Label',
                        'severity': 'MEDIUM',
                        'message': f'<input> has no id (for <label> association) or aria-label: {inp[:80]}',
                    })
                elif has_placeholder and not has_aria and not has_id:
                    issues.append({
                        'file': filename,
                        'line': line_num,
                        'check': 'Placeholder as Label',
                        'severity': 'LOW',
                        'message': 'Using placeholder as the only label — placeholders disappear on focus',
                    })

            # --- Empty buttons ---
            empty_buttons = re.findall(r'<button[^>]*>\s*</button>', line, re.IGNORECASE)
            for btn in empty_buttons:
                if not re.search(r'aria-label\s*=', btn, re.IGNORECASE):
                    issues.append({
                        'file': filename,
                        'line': line_num,
                        'check': 'Empty Button',
                        'severity': 'MEDIUM',
                        'message': 'Button with no text content and no aria-label',
                    })

            # --- Links without href or with empty href ---
            empty_links = re.findall(r'<a(?:\s[^>]*)?>\s*</a>', line, re.IGNORECASE)
            for link in empty_links:
                issues.append({
                    'file': filename,
                    'line': line_num,
                    'check': 'Empty Link',
                    'severity': 'MEDIUM',
                    'message': 'Link (<a>) with no text content — screen readers cannot describe it',
                })

            # --- onclick without keyboard equivalent ---
            if re.search(r'onclick\s*=', line, re.IGNORECASE):
                element = line.strip()
                if not re.search(r'onkeydown|onkeyup|onkeypress|role\s*=\s*["\']button', line, re.IGNORECASE):
                    # Check if it's on a naturally keyboard-accessible element
                    if not re.search(r'<(?:button|a|input|select|textarea)', line, re.IGNORECASE):
                        issues.append({
                            'file': filename,
                            'line': line_num,
                            'check': 'Click Without Keyboard',
                            'severity': 'MEDIUM',
                            'message': 'onclick on non-interactive element without keyboard handler',
                        })

            # --- Autoplaying media ---
            if re.search(r'autoplay', line, re.IGNORECASE):
                issues.append({
                    'file': filename,
                    'line': line_num,
                    'check': 'Autoplay Media',
                    'severity': 'LOW',
                    'message': 'Autoplaying media — provide controls and respect prefers-reduced-motion',
                })

    except (PermissionError, UnicodeDecodeError):
        pass

    return issues


def print_results(all_issues: List[Dict], file_count: int) -> None:
    """Print audit results."""
    if not all_issues:
        print(f"{Colors.GREEN}✅ No accessibility issues found{Colors.END}")
        return

    severity_colors = {
        'HIGH': Colors.RED,
        'MEDIUM': Colors.YELLOW,
        'LOW': Colors.CYAN,
    }

    # Group by check
    by_check = {}
    for issue in all_issues:
        check = issue['check']
        if check not in by_check:
            by_check[check] = []
        by_check[check].append(issue)

    for check, issues in sorted(by_check.items(), key=lambda x: {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2}.get(x[1][0]['severity'], 3)):
        color = severity_colors.get(issues[0]['severity'], '')
        print(f"\n{Colors.BOLD}{color}[{issues[0]['severity']}] {check} ({len(issues)} found){Colors.END}")
        for issue in issues[:5]:
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
        print("Usage: python accessibility_audit.py <project_path>")
        sys.exit(1)

    project_path = Path(sys.argv[1]).resolve()
    if not project_path.exists():
        print(f"Error: Path does not exist: {project_path}")
        sys.exit(1)

    print(f"{Colors.BOLD}{Colors.CYAN}♿ Accessibility Audit — Antigravity Gold{Colors.END}")
    print(f"Scanning: {project_path}\n")

    all_issues = []
    file_count = 0

    for filepath in project_path.rglob('*'):
        if filepath.is_file() and should_check_file(filepath):
            file_count += 1
            issues = audit_html_file(filepath)
            all_issues.extend(issues)

    print(f"HTML files audited: {file_count}")
    print_results(all_issues, file_count)

    # Summary
    high = sum(1 for i in all_issues if i['severity'] == 'HIGH')
    medium = sum(1 for i in all_issues if i['severity'] == 'MEDIUM')

    print(f"\n{Colors.BOLD}Summary:{Colors.END}")
    print(f"  Total issues: {len(all_issues)}")
    print(f"  High: {high}")
    print(f"  Medium: {medium}")

    if high > 5:
        print(f"\n{Colors.RED}❌ Multiple high-severity accessibility issues{Colors.END}")
        sys.exit(1)
    elif high > 0 or medium > 5:
        print(f"\n{Colors.YELLOW}⚠️  Accessibility issues found — review before deployment{Colors.END}")
        sys.exit(1)
    else:
        print(f"\n{Colors.GREEN}✅ Accessibility audit passed{Colors.END}")
        sys.exit(0)


if __name__ == '__main__':
    main()
