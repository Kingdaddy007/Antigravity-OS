---
status: template
scope: project
project_id: null
updated_at: null
owner: null
confidence: unset
---

# DOMAIN RULES

**Version:** Gold v1.2 (Master Merge)
**Layer:** 6 — Context (Ground Truth)
**Tier:** 2 — Loaded by task
**File:** contexts/domain-rules.md
**Purpose:** Captures business logic rules, domain invariants, state machines, edge cases, and validation rules that Anti-Gravity must respect when building or modifying features. This is the business logic source of truth — what the product MUST do and MUST NOT do, regardless of how it's implemented.
**Loaded When:** Feature development, bug fixing, code review, testing, or any task that involves business logic decisions.
**Maintenance:** Update when business rules change, new state transitions are added, edge cases are discovered, or domain terminology evolves. Treat this as living documentation — every bug caused by a misunderstood business rule should result in an update to this file. Review quarterly.

---

## HOW ANTI-GRAVITY USES THIS FILE

This file is the business logic rulebook. It prevents Anti-Gravity from generating code that works technically but violates the product's business rules.

Domain rules are not implementation details. They are the real-world constraints and meanings that the software exists to preserve.

A system can be technically elegant, well-tested, fast, and maintainable — and still be wrong if it violates the domain.

**When loaded**, Anti-Gravity will:

- Enforce domain invariants in every piece of generated code
- Validate state transitions against the defined state machines
- Use YOUR exact domain terminology in code, variable names, and explanations
- Handle edge cases using YOUR documented expected behaviors
- Apply YOUR validation rules to form inputs and API requests
- Respect YOUR calculation formulas for metrics and derived values
- Treat permission rules as part of domain correctness, not just security

**When missing or incomplete**, Anti-Gravity will:

- Generate code that may violate business rules
- Use generic terminology instead of your domain language
- Handle edge cases inconsistently or incorrectly
- Implement calculations differently from how the product defines them
- Miss validation rules, allowing invalid data into the system

**When stale**, Anti-Gravity will:

- Enforce old business rules that have been changed
- Allow state transitions that are no longer valid
- Use deprecated terminology
- Apply outdated calculation formulas
- Miss new edge cases discovered since the last update

---

## CORE PRINCIPLE

Domain rules are first-class constraints.

When domain logic conflicts with generic engineering convenience, the domain wins.

Anti-Gravity must:

1. Treat domain rules as real constraints, not implementation suggestions
2. Use project-specific domain vocabulary consistently
3. Re-check domain invariants when recommending changes to state, permissions, calculations, or lifecycle logic
4. Not simplify away domain distinctions just because they are inconvenient
5. Treat known confusion areas as high-caution zones
6. Flag conflicts between implementation and domain rules explicitly
7. Ask before assuming when a domain rule is unclear
8. Preserve exception handling where it is truly part of the domain
9. Let this file override generic assumptions about how the business should probably work

---

## DOMAIN SUMMARY

<!-- Fill in your actual domain summary using this template:

This product operates in the domain of [domain name], helping [users]
achieve [goal].

The domain is governed by rules around [important concepts: e.g.
permissions, billing, approvals, transactions, compliance, lifecycle
state, timing].

Correct system behavior depends on preserving these domain meanings
and constraints.
-->

[Fill in]

---

## CORE DOMAIN INVARIANTS

### Data Ownership Invariants

| # | Invariant | Why It Exists | Enforcement |
| --- | --- | --- | --- |
| 1 | [invariant] | [why] | [how enforced] |
| 2 | [invariant] | [why] | [how enforced] |
| 3 | [invariant] | [why] | [how enforced] |

### Access Control Invariants

| # | Invariant | Why It Exists | Enforcement |
| --- | --- | --- | --- |
| 1 | [invariant] | [why] | [how enforced] |
| 2 | [invariant] | [why] | [how enforced] |

### Data Integrity Invariants

| # | Invariant | Why It Exists | Enforcement |
| --- | --- | --- | --- |
| 1 | [invariant] | [why] | [how enforced] |
| 2 | [invariant] | [why] | [how enforced] |

---

## STATE MACHINES

### [Entity Name] — Generic Placeholder

#### States (Generic)

- [State A]
- [State B]
- [State C]

#### State Diagram (Generic)

```text
┌─────────┐     ┌─────────┐     ┌─────────┐
│ State A │────▶│ State B │────▶│ State C │
└─────────┘     └─────────┘     └─────────┘
```

#### Transition Rules (Generic)

| From | To | Allowed? | Who Can Do It | Preconditions | Side Effects |
| --- | --- | --- | --- | --- | --- |
| [A] | [B] | ✅ | [who] | [conditions] | [effects] |
| [B] | [C] | ✅ | [who] | [conditions] | [effects] |
| [A] | [C] | ❌ | — | — | — |

#### Implementation Notes (Generic)

- [note 1]
- [note 2]

---

### Task Status — Example (Replace or delete when you fill in your real entities)

#### States (Task)

- `backlog`
- `todo`
- `in_progress`
- `in_review`
- `done`
- `archived`

#### State Diagram (Task)

```text
                  ┌──────────────────────────────────────┐
                  │         Can move backward            │
                  │                                      │
┌─────────┐  ┌────┴───┐  ┌─────────────┐  ┌────────────┴┐  ┌──────┐
│ backlog │─▶│  todo  │─▶│ in_progress │─▶│  in_review  │─▶│ done │
└─────────┘  └───┬────┘  └──────┬──────┘  └──────┬──────┘  └──────┘
                 │              │                  │
                 └──────────────┴──────────────────┘
                        (can move backward freely)

Any status ──▶ [archived]
(one-way — reversible only by project admin)
```

#### Transition Rules (Task)

| From | To | Allowed? | Who Can Do It | Side Effects |
| --- | --- | --- | --- | --- |
| `backlog` | `todo` | ✅ | Any member | None |
| `todo` | `in_progress` | ✅ | Any member | None |
| `in_progress` | `in_review` | ✅ | Any member | None |
| `in_review` | `done` | ✅ | Any member | Increments sprint completed points |
| `done` | `in_review` | ✅ | Any member | Decrements sprint completed points |
| `done` | `in_progress` | ✅ | Any member | Decrements sprint completed points |
| `in_progress` | `todo` | ✅ | Any member | None |
| `todo` | `backlog` | ✅ | Any member | Removes from sprint if assigned |
| `backlog` | `done` | ❌ | — | Cannot skip directly to done |
| `backlog` | `in_review` | ❌ | — | Cannot skip to review |
| Any | `archived` | ✅ | Any member | Task hidden from active views |
| `archived` | Any | ✅ | Admin only | Task restored to previous status |

#### Implementation Notes (Task)

- Status transitions validated in `updateTaskStatus` Server Action
- Invalid transitions return `{ success: false, error: 'Invalid status transition', code: 'BUSINESS_RULE_VIOLATION' }`
- Side effects such as point counting execute in the same database transaction as the status change
- UI should only show valid transition buttons based on current status

---

### Sprint Status — Example (Replace or delete when you fill in your real entities)

#### States (Sprint)

- `planning`
- `active`
- `completed`

#### State Diagram (Sprint)

```text
┌──────────┐     ┌────────┐     ┌───────────┐
│ planning │────▶│ active │────▶│ completed │
└──────────┘     └────────┘     └───────────┘

(cannot go backward)
```

#### Transition Rules (Sprint)

| From | To | Allowed? | Who Can Do It | Preconditions | Side Effects |
| --- | --- | --- | --- | --- | --- |
| `planning` | `active` | ✅ | Admin or Member | No other sprint in this project is `active` | None |
| `active` | `completed` | ✅ | Admin or Member | — | Unfinished tasks move to project backlog. Sprint velocity calculated and stored. |
| `completed` | `planning` | ❌ | — | — | Completed sprints cannot be reopened |
| `completed` | `active` | ❌ | — | — | Completed sprints cannot be reactivated |
| `planning` | `completed` | ❌ | — | — | Cannot complete a sprint that was never active |

#### Implementation Notes (Sprint)

- Sprint activation checks that no other sprint in the project has status `active`
- Sprint completion side effects run in a transaction: move tasks, calculate velocity, update status
- Velocity calculation: count of story points with status `done` in this sprint

---

### Project Membership Status — Example (Replace or delete when you fill in your real entities)

#### States (Membership)

- `invited`
- `active`
- `deactivated`
- `removed`

#### State Diagram (Membership)

```text
┌─────────┐     ┌────────┐     ┌──────────────┐
│ invited │────▶│ active │────▶│ deactivated  │
└─────────┘     └───┬────┘     └──────────────┘
                    │
                    └──▶ [removed]
                         (hard delete of membership record)
```

#### Transition Rules (Membership)

| From | To | Allowed? | Who Can Do It | Side Effects |
| --- | --- | --- | --- | --- |
| `invited` | `active` | ✅ | The invited user accepting | User gains access to project |
| `active` | `deactivated` | ✅ | Admin | User loses access. Assigned tasks show "Former member." |
| `active` | `removed` | ✅ | Admin | Membership record deleted. Tasks remain assigned showing "Former member." |
| `deactivated` | `active` | ✅ | Admin | User regains access |
| Any | removed if last admin | ❌ | — | Blocked — project must have at least one admin |

#### Implementation Notes (Membership)

- Removing the last admin is blocked at the application level before the database operation
- Deactivated users retain their assigned tasks — leads decide whether to reassign
- Hard deletion of membership record on remove, not soft delete

---

## PERMISSION AND ROLE RULES

### User Roles

| Role | What They Can Do | What They Cannot Do |
| --- | --- | --- |
| [Role 1] | [permissions] | [restrictions] |
| [Role 2] | [permissions] | [restrictions] |
| [Role 3] | [permissions] | [restrictions] |

### Important Permission Constraints (Roles)

- [constraint 1]
- [constraint 2]
- [constraint 3]

### Sensitive Actions

| Action | Who Can Do It | Notes |
| --- | --- | --- |
| [action 1] | [who] | [notes] |
| [action 2] | [who] | [notes] |

---

## BUSINESS LOGIC RULES

| # | Rule | Context | Implementation Detail | Why This Rule Exists |
| --- | --- | --- | --- | --- |
| 1 | [rule] | [context] | [detail] | [why] |
| 2 | [rule] | [context] | [detail] | [why] |
| 3 | [rule] | [context] | [detail] | [why] |

---

## CALCULATION RULES

| # | Calculation | Formula | Edge Cases | Display Format |
| --- | --- | --- | --- | --- |
| 1 | [name] | [formula] | [edge cases] | [how displayed] |
| 2 | [name] | [formula] | [edge cases] | [how displayed] |

### Time and Date Rules (Calculations)

- [time rule 1]
- [time rule 2]
- [time rule 3]

Examples of what belongs here:

- billing cycle anchored to signup date, not calendar month
- approvals expire after 48 hours
- deadlines evaluated in user-local timezone
- scheduled actions must remain idempotent across retries

---

## EDGE CASES AND SPECIAL HANDLING

| # | Edge Case | Expected Behavior | Why This Behavior | Discovered Via |
| --- | --- | --- | --- | --- |
| 1 | [case] | [behavior] | [why] | [source] |
| 2 | [case] | [behavior] | [why] | [source] |
| 3 | [case] | [behavior] | [why] | [source] |

---

## VALIDATION RULES

### [Entity Name] Fields

| Field | Type | Required | Constraints | Validation Message |
| --- | --- | --- | --- | --- |
| [field] | [type] | Yes/No | [constraints] | [message] |
| [field] | [type] | Yes/No | [constraints] | [message] |

### Implementation Notes (Validation)

- [validation library and approach]
- [where schemas live]
- [client vs server enforcement boundary]
- Server-side validation is the security boundary — client-side is for UX only

---

## MULTI-TENANT AND SCOPE RULES

- [scope rule 1]
- [scope rule 2]
- [scope rule 3]

Examples of what belongs here:

- users belong to exactly one tenant
- data must never cross tenant boundary
- role assignment is tenant-specific
- reports are scoped by organization, not user

---

## NOTIFICATION AND TRIGGER RULES

| # | Trigger Event | Notification Type | Recipients | Content | Timing |
| --- | --- | --- | --- | --- | --- |
| 1 | [event] | [type] | [who] | [content] | [timing] |
| 2 | [event] | [type] | [who] | [content] | [timing] |

### Notification Rules

- [rule 1]
- [rule 2]
- [rule 3]

---

## DOMAIN METRICS AND REAL MEANINGS

| Metric | What It Actually Means | What It Does NOT Mean |
| --- | --- | --- |
| [metric] | [real meaning] | [common wrong assumption] |
| [metric] | [real meaning] | [common wrong assumption] |

---

## FORBIDDEN SIMPLIFICATIONS

| Simplification | Why It Is Wrong | What To Do Instead |
| --- | --- | --- |
| [simplification] | [why wrong] | [correct approach] |
| [simplification] | [why wrong] | [correct approach] |

---

## KNOWN DOMAIN CONFUSIONS AND HISTORICAL BUG AREAS

| Area | The Confusion | What Actually Happens | Bug Severity |
| --- | --- | --- | --- |
| [area] | [the confusion] | [correct behavior] | [severity] |
| [area] | [the confusion] | [correct behavior] | [severity] |

---

## DOMAIN LANGUAGE PREFERENCES

| Term | Meaning | Used In Code As | DO NOT Call It |
| --- | --- | --- | --- |
| [term] | [meaning] | [code usage] | [wrong terms] |
| [term] | [meaning] | [code usage] | [wrong terms] |

---

## WHAT CORRECT BEHAVIOR LOOKS LIKE IN THIS DOMAIN

A feature or change is domain-correct when:

- state transitions respect domain lifecycle rules
- calculations follow the exact business rule order
- permissions reflect real-world authority boundaries
- user-visible behavior aligns with domain promises
- reporting and analytics reflect domain definitions accurately
- edge cases and exception paths preserve business integrity
- data remains scoped correctly by tenant, account, or workspace
- domain vocabulary is used consistently across code and UI

A feature or change is domain-incorrect when:

- it is technically valid but violates a business invariant
- it simplifies away a distinction that matters to the business
- it uses generic language where domain language is required
- it exposes internal structure that the domain does not intend to expose
- it treats an exception as a bug rather than a documented domain rule

---

## NON-NEGOTIABLE DOMAIN CONSTRAINTS

These are rules Anti-Gravity must not violate unless explicitly told the rule is changing:

- [constraint 1]
- [constraint 2]
- [constraint 3]
- [constraint 4]
- [constraint 5]

---

## OPEN DOMAIN QUESTIONS

- [question 1]
- [question 2]
- [question 3]

---

## CROSS-REFERENCES

| Related Context File | Relationship |
| --- | --- |
| `project-context.md` | Jobs-to-be-Done and user types that these rules serve |
| `database-context.md` | Schema implementation of these domain rules |
| `architecture-context.md` | Where business logic is enforced |
| `coding-standards.md` | Naming conventions align with domain terminology |
| `testing-standards.md` | State machine transitions are primary test targets |
| `api-conventions.md` | 422 errors map to business rule violations |
| `security-baselines.md` | Authorization rules intersect with domain access rules |
| `business-priorities.md` | Business priorities may temporarily alter rule enforcement |

---

## FINAL RULE

If code, design, or architecture looks technically correct but violates domain truth, it is still wrong.

Domain rules are not suggestions. They are the reason the software exists.

---
