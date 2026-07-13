# Context Templates Contract

## Purpose

This directory contains blank authoring scaffolds copied into a project's `.agents/contexts/` directory. Files here are never live project truth.

## Rules & Constraints

- Every template must declare `status: template` metadata.
- Placeholders and examples must be visibly marked and must not be interpreted as facts.
- Generic policy belongs in `../baselines/`; domain behavior belongs in `../skills/`.
- Generated installations may copy these templates, but agents must activate project-local copies before relying on them.

## Exposed Interfaces

- Markdown context templates consumed by project-inception workflows and host adapters.

## Verification

- Run `python global/scripts/os.py validate`.

