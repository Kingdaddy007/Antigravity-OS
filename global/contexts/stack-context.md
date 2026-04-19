# STACK CONTEXT

**Version:** Gold v2.1
**Type:** Runtime context file
**Layer:** Ground truth
**Loaded When:** Code generation, debugging, architecture, dependency choices, deployment discussions

---

## RUNTIME SUMMARY

Use this file to tell Anti-Gravity what technologies are actually in play, what is still undecided, and which technical defaults should be respected.

When this file is stale or generic, Anti-Gravity will drift toward ecosystem defaults instead of the project's real stack.

---

## CURRENT STACK REALITY

### What This Stack Currently Is

[Short honest description of the current implementation medium and stack reality]

### What This Stack Is Not Yet

- [undecided technology or major open choice]
- [undecided technology or major open choice]
- [undecided technology or major open choice]

### Safe Assumptions

- [stable assumption]
- [stable assumption]
- [stable assumption]

---

## STACK SUMMARY

### Primary Languages

| Language | Version | Usage | Notes |
| :--- | :--- | :--- | :--- |
| [Language] | [Version] | [Where used] | [Important note] |
| [Language] | [Version] | [Where used] | [Important note] |

### Frontend

- Framework: [Framework and version]
- State management: [Approach]
- Styling: [Approach]
- Component library: [Library or custom approach]
- Build / package manager: [Tooling]

### Backend

- Runtime: [Runtime and version]
- Framework: [Framework]
- API style: [REST / GraphQL / RPC / Server Actions / other]
- Auth approach: [Approach]
- Validation / serialization: [Approach]

### Data And Infrastructure

- Primary database: [Engine and tooling]
- Caching / queues: [Approach]
- Hosting / deployment: [Platform]
- Observability: [Current tooling]

---

## DEFAULTS AND CONSTRAINTS

### Architectural Defaults

- Prefer [existing default pattern] for data fetching.
- Prefer [existing default pattern] for mutations.
- Prefer [existing default pattern] for validation.
- Prefer [existing default pattern] for deployment.

### Critical Version Constraints

| Dependency | Current | Constraint | Reason |
| :--- | :--- | :--- | :--- |
| [Dependency] | [Version] | [Constraint] | [Reason] |
| [Dependency] | [Version] | [Constraint] | [Reason] |

### Known Stack Limitations

- [limitation and impact]
- [limitation and impact]
- [limitation and impact]

---

## KEY LIBRARIES AND INTEGRATIONS

### Important Libraries

| Library | Version | Purpose | Notes |
| :--- | :--- | :--- | :--- |
| [Library] | [Version] | [Purpose] | [Notes] |
| [Library] | [Version] | [Purpose] | [Notes] |

### External Integrations

- [Integration] - [what it is used for and any key constraint]
- [Integration] - [what it is used for and any key constraint]

---

## MAINTENANCE NOTES

Update this file when:

- a framework version changes
- a major dependency is introduced or removed
- an architectural default changes
- an operational limitation becomes important

Keep this file factual. Longer scaffolding, extended examples, and fill guidance belong in the matching template under `global_templates/`.
