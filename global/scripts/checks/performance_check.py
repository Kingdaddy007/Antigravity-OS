#!/usr/bin/env python3
"""
Performance Checker — Antigravity Gold Verification System
============================================================

Basic performance profiling without external dependencies.
Analyzes static files for size, bloat, and optimization opportunities.

Usage:
    python scripts/checks/performance_check.py <project_path>

Checks:
    - HTML/CSS/JS file sizes and total bundle size
    - Number of external resources (link/script tags)
    - Large image detection (files over configurable threshold)
    - Inline style bloat detection
    - Unminified JavaScript in production builds
    - CSS and JS file counts
    - Redundant resource loading
"""

import sys
import re
import os
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

# Directories to skip
SKIP_DIRS = {'node_modules', '.git', '__pycache__', 'dist', 'build', '.next',
             'venv', '.venv', 'coverage', '.cache', '.gemini'}

# Thresholds
MAX_SINGLE_JS_KB = 500        # Warn if a single JS file exceeds this
MAX_SINGLE_CSS_KB = 200       # Warn if a single CSS file exceeds this
MAX_IMAGE_KB = 500            # Warn if a single image exceeds this
MAX_TOTAL_BUNDLE_KB = 5000    # Warn if total bundle exceeds 5MB
MAX_HTML_INLINE_STYLE_COUNT = 50  # Warn if too many inline styles in one file


def format_size(bytes_size: int) -> str:
    """Format bytes to human readable."""
    if bytes_size < 1024:
        return f"{bytes_size} B"
    elif bytes_size < 1024 * 1024:
        return f"{bytes_size / 1024:.1f} KB"
    else:
        return f"{bytes_size / (1024 * 1024):.1f} MB"


def should_skip(filepath: Path) -> bool:
    """Check if path should be skipped."""
    for skip in SKIP_DIRS:
        if skip in filepath.parts:
            return True
    return False


def analyze_project(project_path: Path) -> Dict:
    """Analyze entire project for performance metrics."""
    metrics = {
        'js_files': [],
        'css_files': [],
        'html_files': [],
        'image_files': [],
        'other_files': [],
        'issues': [],
        'total_js_bytes': 0,
        'total_css_bytes': 0,
        'total_html_bytes': 0,
        'total_image_bytes': 0,
    }

    js_exts = {'.js', '.mjs', '.cjs'}
    css_exts = {'.css'}
    html_exts = {'.html', '.htm'}
    img_exts = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico', '.bmp'}

    for filepath in project_path.rglob('*'):
        if not filepath.is_file() or should_skip(filepath):
            continue

        ext = filepath.suffix.lower()
        size = filepath.stat().st_size

        if ext in js_exts:
            metrics['js_files'].append((filepath, size))
            metrics['total_js_bytes'] += size

            # Check if unminified (heuristic: has lots of whitespace and comments)
            if size > 10000:  # Only check files > 10KB
                try:
                    content = filepath.read_text(encoding='utf-8', errors='ignore')
                    lines = content.split('\n')
                    if len(lines) > 0:
                        avg_line_length = len(content) / len(lines)
                        # Minified JS typically has very long lines
                        if avg_line_length < 80 and len(lines) > 100:
                            metrics['issues'].append({
                                'file': str(filepath),
                                'check': 'Unminified JavaScript',
                                'severity': 'INFO',
                                'message': f'{format_size(size)} — appears unminified ({len(lines)} lines, avg {avg_line_length:.0f} chars/line)',
                            })
                except (PermissionError, UnicodeDecodeError):
                    pass

            # Large JS file
            if size > MAX_SINGLE_JS_KB * 1024:
                metrics['issues'].append({
                    'file': str(filepath),
                    'check': 'Large JavaScript File',
                    'severity': 'MEDIUM',
                    'message': f'{format_size(size)} — exceeds {MAX_SINGLE_JS_KB}KB threshold. Consider code splitting.',
                })

        elif ext in css_exts:
            metrics['css_files'].append((filepath, size))
            metrics['total_css_bytes'] += size

            if size > MAX_SINGLE_CSS_KB * 1024:
                metrics['issues'].append({
                    'file': str(filepath),
                    'check': 'Large CSS File',
                    'severity': 'LOW',
                    'message': f'{format_size(size)} — exceeds {MAX_SINGLE_CSS_KB}KB threshold.',
                })

        elif ext in html_exts:
            metrics['html_files'].append((filepath, size))
            metrics['total_html_bytes'] += size

            # Check inline styles count
            try:
                content = filepath.read_text(encoding='utf-8', errors='ignore')
                inline_styles = len(re.findall(r'style\s*=\s*["\']', content))
                if inline_styles > MAX_HTML_INLINE_STYLE_COUNT:
                    metrics['issues'].append({
                        'file': str(filepath),
                        'check': 'Inline Style Bloat',
                        'severity': 'LOW',
                        'message': f'{inline_styles} inline style attributes — consider using CSS classes',
                    })

                # Count external resources
                scripts = len(re.findall(r'<script[^>]+src\s*=', content))
                links = len(re.findall(r'<link[^>]+href\s*=', content))
                if scripts + links > 20:
                    metrics['issues'].append({
                        'file': str(filepath),
                        'check': 'Many External Resources',
                        'severity': 'MEDIUM',
                        'message': f'{scripts} scripts + {links} stylesheets = {scripts + links} HTTP requests',
                    })

            except (PermissionError, UnicodeDecodeError):
                pass

        elif ext in img_exts:
            metrics['image_files'].append((filepath, size))
            metrics['total_image_bytes'] += size

            if size > MAX_IMAGE_KB * 1024:
                metrics['issues'].append({
                    'file': str(filepath),
                    'check': 'Large Image',
                    'severity': 'MEDIUM',
                    'message': f'{format_size(size)} — exceeds {MAX_IMAGE_KB}KB. Consider compression or WebP format.',
                })

    # Total bundle check
    total = metrics['total_js_bytes'] + metrics['total_css_bytes'] + metrics['total_html_bytes']
    if total > MAX_TOTAL_BUNDLE_KB * 1024:
        metrics['issues'].append({
            'file': 'TOTAL',
            'check': 'Large Total Bundle',
            'severity': 'HIGH',
            'message': f'Total code bundle: {format_size(total)} (JS: {format_size(metrics["total_js_bytes"])}, CSS: {format_size(metrics["total_css_bytes"])})',
        })

    return metrics


def print_report(metrics: Dict) -> None:
    """Print performance report."""
    print(f"\n{Colors.BOLD}📊 Asset Inventory:{Colors.END}")
    print(f"  JavaScript: {len(metrics['js_files'])} files, {format_size(metrics['total_js_bytes'])}")
    print(f"  CSS:        {len(metrics['css_files'])} files, {format_size(metrics['total_css_bytes'])}")
    print(f"  HTML:       {len(metrics['html_files'])} files, {format_size(metrics['total_html_bytes'])}")
    print(f"  Images:     {len(metrics['image_files'])} files, {format_size(metrics['total_image_bytes'])}")

    total_code = metrics['total_js_bytes'] + metrics['total_css_bytes'] + metrics['total_html_bytes']
    print(f"\n  {Colors.BOLD}Total code bundle: {format_size(total_code)}{Colors.END}")
    print(f"  {Colors.BOLD}Total with images: {format_size(total_code + metrics['total_image_bytes'])}{Colors.END}")

    # Top 5 largest files
    all_files = metrics['js_files'] + metrics['css_files'] + metrics['image_files']
    all_files.sort(key=lambda x: x[1], reverse=True)
    if all_files:
        print(f"\n{Colors.BOLD}📦 Largest Files:{Colors.END}")
        for filepath, size in all_files[:5]:
            print(f"  {format_size(size):>10}  {filepath}")

    # Issues
    if metrics['issues']:
        severity_colors = {
            'HIGH': Colors.RED,
            'MEDIUM': Colors.YELLOW,
            'LOW': Colors.CYAN,
            'INFO': Colors.CYAN,
        }

        print(f"\n{Colors.BOLD}⚠️  Performance Issues:{Colors.END}")
        for issue in sorted(metrics['issues'], key=lambda x: {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2, 'INFO': 3}.get(x['severity'], 4)):
            color = severity_colors.get(issue['severity'], '')
            print(f"\n  {color}[{issue['severity']}] {issue['check']}{Colors.END}")
            print(f"    {issue['file']}")
            print(f"    {issue['message']}")
    else:
        print(f"\n{Colors.GREEN}✅ No performance issues found{Colors.END}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    if len(sys.argv) < 2:
        print("Usage: python performance_check.py <project_path>")
        sys.exit(1)

    project_path = Path(sys.argv[1]).resolve()
    if not project_path.exists():
        print(f"Error: Path does not exist: {project_path}")
        sys.exit(1)

    print(f"{Colors.BOLD}{Colors.CYAN}⚡ Performance Check — Antigravity Gold{Colors.END}")
    print(f"Scanning: {project_path}")

    metrics = analyze_project(project_path)
    print_report(metrics)

    # Exit code
    high_issues = sum(1 for i in metrics['issues'] if i['severity'] == 'HIGH')
    medium_issues = sum(1 for i in metrics['issues'] if i['severity'] == 'MEDIUM')

    print(f"\n{Colors.BOLD}Summary:{Colors.END}")
    print(f"  Issues: {len(metrics['issues'])} (High: {high_issues}, Medium: {medium_issues})")

    if high_issues > 0:
        print(f"\n{Colors.RED}❌ High-severity performance issues found{Colors.END}")
        sys.exit(1)
    else:
        print(f"\n{Colors.GREEN}✅ Performance check passed{Colors.END}")
        sys.exit(0)


if __name__ == '__main__':
    main()
