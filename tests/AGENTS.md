# Tests Context & Contract

## Purpose

This directory verifies public Anti-Gravity OS behavior: validation, host builds, safe installation, routing, and scanner reliability.

## Rules & Constraints

- Test observable behavior, not private implementation details.
- Use temporary directories; never read from or write to a real user configuration directory.
- Installer tests must place unrelated sentinel files beside the Anti-Gravity namespace and prove they survive.
- Every safety defect fixed must gain a regression test.

## Verification

- Run `python -m unittest discover -s tests -p "test_*.py"`.

