# Baselines Contract

## Purpose

This directory contains concise, stable, cross-project policy that may constrain execution without pretending to be project-specific truth.

## Rules & Constraints

- Baselines may narrow behavior but cannot override host, organization, developer, or user authority.
- Keep each baseline concise and free of project-specific values.
- Do not duplicate detailed skill procedures or context-template scaffolding.
- Changes to safety or approval semantics require regression tests.

## Exposed Interfaces

- `authority-and-trust.md`: authority, untrusted-content, and capability boundaries.
- `engineering.md`: portable engineering defaults.
- `context-integrity.md`: runtime-context activation and freshness rules.

## Verification

- Run `python global/scripts/os.py validate`.

