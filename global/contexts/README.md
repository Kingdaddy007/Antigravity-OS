# README - CONTEXTS FOLDER

**Location:** `.antigravity/contexts/`
**Layer:** Ground truth
**Loading Tier:** Tier 2 - loaded by task

---

## PURPOSE

This folder contains the **live truth** Anti-Gravity should use when working inside a project.

Contexts are not the constitution and they are not generic teaching files. They are the active project facts that make recommendations less generic and more correct.

Skills answer **how to think**.
Contexts answer **what is true here**.

---

## WHAT BELONGS HERE

Context files should contain:

- facts
- constraints
- active standards
- known tradeoff posture
- real environment details
- current project reality

Context files should not contain:

- broad operating philosophy from `GEMINI.md`
- domain behavior instructions from `skills/`
- long fill-in tutorials
- large example libraries

Authoring scaffolds and longer examples now belong in `global_templates/`.

---

## INVENTORY

### Core runtime contexts

| File | What It Grounds |
| :--- | :--- |
| `project-context.md` | product identity, users, stage, priorities |
| `stack-context.md` | languages, frameworks, tools, runtime constraints |
| `architecture-context.md` | structural boundaries and design decisions |
| `coding-standards.md` | coding conventions and implementation defaults |

### Additional domain contexts

| File | What It Grounds |
| :--- | :--- |
| `testing-standards.md` | testing strategy and guardrails |
| `security-baselines.md` | trust boundaries and security requirements |
| `design-system.md` | design language and UI rules |
| `database-context.md` | data model, schema patterns, migrations |
| `api-conventions.md` | API contracts and consistency rules |
| `domain-rules.md` | business invariants and domain logic |
| `business-priorities.md` | current tradeoff posture |
| `infra-context.md` | deployment, runtime, and operational reality |
| `app-flow.md` | user journeys and flow logic |
| `visual-identity.md` | visual direction and design identity |

---

## LOADING RULES

Load only the contexts that materially improve the task.

| Task Type | Typical Contexts |
| :--- | :--- |
| Any code task | `stack-context.md`, `coding-standards.md` |
| New feature | add `architecture-context.md`, `project-context.md` |
| Database work | add `database-context.md` |
| UI work | add `design-system.md` or `visual-identity.md` |
| API work | add `api-conventions.md` |
| Security work | add `security-baselines.md` |
| Testing | add `testing-standards.md` |
| Deployment | add `infra-context.md` |
| Business logic | add `domain-rules.md` |

Start with 1-2 files and expand only if needed. Context overload is real.

---

## CONTEXT FILE CONTRACT

Runtime context files should be easy to scan. The preferred structure is:

1. **Runtime Summary** - fast orientation for normal use
2. **Operational Truth** - the facts, rules, and constraints that govern work
3. **Maintenance Notes** - how and when to update the file
4. **Optional Inline Guidance** - short hints only when they improve authoring without bloating runtime use

Long fill-in scaffolds, detailed examples, and teaching material should live in `global_templates/`.

---

## CONTEXT GAP HANDLING

When a context file is missing, stale, or thin:

1. name the gap
2. request the missing fact or derive it from the project when possible
3. record explicit assumptions if work must proceed
4. update the live context file when the truth is known

A stale context file is worse than no context file because it creates confident wrongness.

---

## INTERACTION WITH OTHER FOLDERS

| Folder | Relationship |
| :--- | :--- |
| `core/` | Core provides permanent rules; contexts provide project truth |
| `skills/` | Skills describe behavior; contexts ground that behavior here |
| `workflows/` | Workflows load the contexts needed for execution |
| `global_templates/` | Templates scaffold new contexts and formal outputs |
| `memory/` | Memory explains what was learned over time; contexts state what is true now |
| `rubric/` | Rubrics may use context to judge quality in the current project |

---

## MAINTENANCE

Update contexts when the project changes, not just on a calendar.

Typical triggers:

- product pivot
- stack change
- architecture shift
- convention change
- security or compliance change
- major new domain rule

---

## FINAL RULE

`contexts/` should make Anti-Gravity more correct in this project than general knowledge alone ever could.
