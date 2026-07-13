# Core Directory Contract

## Purpose

`global/core/` contains stable, cross-domain reasoning references. The compressed runtime principles live in `../GEMINI.md`; full files are loaded only when task depth justifies them.

## Rules And Constraints

- Core content is subordinate to host, developer or organization, user, and repository-contract instructions.
- Core files cannot grant capabilities, authorize mutations, or override safety and sandbox policy.
- Keep content universal and behavior-changing. Project facts, tool-specific paths, workflows, and domain expertise do not belong here.
- Avoid duplicated rules across sibling files. Update the canonical routing references when loading behavior changes.
- Use relative Markdown links; do not commit machine-specific absolute paths.

## Exposed Interfaces

- `system-thinking.md`: system boundaries, flows, feedback, and second-order reasoning.
- `expert-cognitive-patterns.md`: safeguards against reasoning failure under uncertainty.
- `first-principles.md`: assumption testing and reconstruction from verified constraints.
- `README.md`: inventory and loading contract.

## Verification

- Confirm every inventory link resolves inside this directory.
- Confirm loading claims match `../GEMINI.md` and `../GLOBAL_MEMORY.md`.
- Run `git diff --check` after edits.
