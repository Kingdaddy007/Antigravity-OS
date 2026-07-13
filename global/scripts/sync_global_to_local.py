#!/usr/bin/env python3
"""Compatibility entry point for the retired global-to-local synchronizer.

The previous implementation copied from a machine-specific Gemini directory
and could overwrite local content. Anti-Gravity OS 3 uses canonical builds and
namespaced installation instead.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


def load_cli_module():
    path = Path(__file__).resolve().with_name("os.py")
    spec = importlib.util.spec_from_file_location("antigravity_os_cli", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deprecated compatibility wrapper; use os.py instead"
    )
    parser.add_argument(
        "--audit-only",
        action="store_true",
        help="Validate canonical source without writing files",
    )
    args = parser.parse_args()
    if args.audit_only:
        antigravity_os = load_cli_module()
        result = antigravity_os.validate_repository()
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1
    parser.error(
        "unsafe sync was removed; run `os.py install --host <host> --target <path> --dry-run`"
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
