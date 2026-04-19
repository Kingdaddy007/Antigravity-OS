# CODING STANDARDS

**Version:** Gold v2.1
**Type:** Runtime context file
**Layer:** Ground truth
**Loaded When:** Code generation, modification, review, refactoring

---

## RUNTIME SUMMARY

This file defines the coding conventions Anti-Gravity should follow inside this project so generated code matches the surrounding codebase instead of drifting into generic AI style.

Use this file for active standards. Keep broader operating philosophy in `GEMINI.md` and language-agnostic skill behavior in `skills/`.

---

## PROJECT CODING POSTURE

### Core Standards

- Clarity over cleverness
- Change safety over short-term speed
- Stable responsibility boundaries
- Explicitness over hidden behavior
- Local simplicity before abstraction

### Review Priorities

1. Correctness
2. Safety and error handling
3. Structural fit
4. Naming quality
5. Testability
6. Consistency with the codebase

---

## NAMING AND FILE CONVENTIONS

### File Naming

| File Type | Convention | Example |
| :--- | :--- | :--- |
| Components | [Convention] | [Example] |
| Hooks | [Convention] | [Example] |
| Utilities | [Convention] | [Example] |
| Test files | [Convention] | [Example] |

### Symbol Naming

- Booleans use: `is`, `has`, `should`, `can`
- Event handler implementations use: `handle...`
- Event handler props use: `on...`
- Domain types use clear noun names, not vague technical labels

---

## IMPLEMENTATION DEFAULTS

### Structure

- Keep outer transport/framework layers thin.
- Push business logic inward where it is easier to test.
- Prefer small focused units over god functions.
- Match existing repository structure unless there is a strong reason not to.

### Error Handling

- Handle foreseeable failure paths explicitly.
- Do not swallow errors silently.
- Validate at meaningful boundaries.
- Use specific, actionable failures rather than vague generic ones.

### Security Floor

- Never interpolate user input into unsafe sinks.
- Never log secrets or sensitive tokens.
- Validate user-controlled input before business logic or persistence.
- Enforce auth and authz before mutations.

### Performance Floor

- Avoid obviously wasteful patterns.
- Do not optimize prematurely.
- If a less-readable optimization is necessary, document why.

---

## PATTERNS TO FOLLOW

- [Preferred mutation pattern]
- [Preferred data fetching pattern]
- [Preferred validation pattern]
- [Preferred testing pattern]
- [Preferred component or module organization]

## PATTERNS TO AVOID

- vague catch-all files like `utils.ts` when a concrete name is possible
- speculative abstractions
- empty catch blocks
- hidden side effects
- rewriting large modules when a narrow fix will do

---

## GIT AND REVIEW CONVENTIONS

### Branch Naming

`[type]/[short-description]`

### Commit Style

Use Conventional Commits:

- `feat: ...`
- `fix: ...`
- `refactor: ...`
- `docs: ...`
- `test: ...`
- `chore: ...`

### Pull Request Expectations

- keep changes reviewable
- explain what changed and why
- include testing notes
- call out migrations or risks clearly

---

## STACK-SPECIFIC SECTION

Use this section for conventions that only make sense once the concrete stack is known:

- language-specific typing rules
- framework-specific component patterns
- import ordering
- formatting and linting details
- test file structure

[Fill in concrete stack-specific conventions here]

---

## MAINTENANCE NOTES

Update this file when:

- the team adopts a new convention
- the framework stack becomes more specific
- review expectations change
- repeated code review friction reveals a missing standard

Long rationale, extended examples, and full fill-in guidance belong in the matching template under `global_templates/`.
