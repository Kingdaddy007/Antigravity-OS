# Profiles Context & Contract

## 1. Purpose

Profiles select optional capability bundles while preserving the general engineering base.

## 2. Rules & Constraints

- `general` is always active and cannot depend on an optional profile.
- Optional profiles may add routing and resources but may not replace global safety policy.
- Profile membership is declared in the canonical manifest.

## 3. Exposed Interfaces

- `general/profile.json`: default engineering profile.
- `spatial/profile.json`: optional spatial-design specialization.

## 4. Internal Dependencies

- `../manifest.yaml`: authoritative profile membership.

## 5. Verification

- Run `python global/scripts/os.py validate`.
