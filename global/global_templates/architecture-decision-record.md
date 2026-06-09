# TEMPLATE: ARCHITECTURE DECISION RECORD (ADR)

**Version:** Gold v1.1 (Master Merge)
**Layer:** 9 — Output Contract
**Tier:** 3 — Loaded on demand
**File:** templates/architecture-decision-record.md
**Purpose:** Standardized format for documenting architectural decisions so they are not re-litigated and future engineers understand WHY choices were made, not just WHAT was chosen.
**Loaded When:** Making or documenting a Type 1 or Type 1.5 architectural decision. Referenced by `workflow-plan-architecture.md`.

***

## WHEN TO USE THIS TEMPLATE

Use this template when:

- Making a decision that will be expensive to reverse (Type 1 or Type 1.5)
- Choosing a technology, pattern, or architectural approach
- Changing existing architecture significantly
- Locking an important system boundary decision
- Recording a tradeoff with long-term implications
- Any decision where a future engineer might ask "why did we do it this way?"

Do NOT use for Type 2 decisions — easily reversible choices need only a brief comment or commit message.

***

## THE TEMPLATE

```markdown

# ADR-[NUMBER]: [Decision Title]

***

## Status

| <!-- One of: Proposed | Accepted | Deprecated | Superseded by ADR-[N] --> |

[Status]

## Date

[YYYY-MM-DD]

## Decision Makers

[Who was involved in this decision — names, roles, or teams]

## Owner

[Person / team / system owner responsible for this decision going forward]

***

## Context

### Problem Statement

<!-- What situation prompted this decision? What problem are we solving?
     Be specific — include metrics, user impact, and developer pain
     points where relevant. Not vague "we need to improve X." -->

[Description of the problem or need]

### Current State

<!-- What exists today? What is working? What is not? What had already
     been decided before this point? -->

[Description of current state]

### Constraints

<!-- What limits our options? Budget, team size, timeline, technical
     constraints, compatibility, compliance. -->

- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

### Requirements

<!-- What must the solution accomplish? -->

#### Functional Requirements

- [Requirement 1]
- [Requirement 2]

#### Non-Functional Requirements

- Performance: [target]
- Scalability: [target]
- Maintainability: [expectations]
- Security: [requirements]
- Reliability: [target]

***

## Options Considered

### Option A — [Name]

### Description

[1-2 paragraph description of this approach]

### Pros

- [Advantage 1]
- [Advantage 2]
- [Advantage 3]

### Cons

- [Disadvantage 1]
- [Disadvantage 2]

**Estimated Effort:** [Low / Medium / High — brief justification]

**Risk:** [Key risks with this approach]

**Why not chosen:** [If this is a rejected option, explain here]

***

### Option B — [Name]

### Description

[1-2 paragraph description]

### Pros

- [Advantage 1]
- [Advantage 2]

### Cons

- [Disadvantage 1]
- [Disadvantage 2]

**Estimated Effort:** [Low / Medium / High — brief justification]

**Risk:** [Key risks]

**Why not chosen:** [If this is a rejected option, explain here]

***

### Option C — [Name]

### Description

[1-2 paragraph description]

### Pros

- [Advantage 1]
- [Advantage 2]

### Cons

- [Disadvantage 1]
- [Disadvantage 2]

**Estimated Effort:** [Low / Medium / High — brief justification]

**Risk:** [Key risks]

**Why not chosen:** [If this is a rejected option, explain here]

***

## Decision

We chose **Option [X]: [Name]**

### Rationale

<!-- Why this option over the others? Reference specific requirements,
     constraints, and tradeoffs that drove the choice. Explain the
     reasoning — do not just restate what was chosen. A skeptical
     engineer reading this 6 months later must be able to follow
     the logic. -->

[Detailed reasoning tied to requirements and constraints]

***

## Tradeoffs Accepted

<!-- What are we explicitly giving up by choosing this option?
     Name each tradeoff and why it is acceptable. -->

- [Tradeoff 1 — what is sacrificed and why it is acceptable]
- [Tradeoff 2]
- [Tradeoff 3]

## Tradeoffs Rejected

<!-- What did other options offer that we are choosing NOT to have?
     Why is giving that up acceptable given our constraints? -->

- [What Option B offered that we are giving up, and why that is okay]
- [What Option C offered that we are giving up, and why that is okay]

***

## Consequences

### What Changes

- [Consequence 1 — what is different as a result of this decision]
- [Consequence 2]

### What This Enables

<!-- What future capabilities or improvements does this decision unlock? -->

- [Future capability 1]
- [Future capability 2]

### New Constraints Created

<!-- What future decisions are now constrained by this choice? -->

- [Constraint on future work 1]
- [Constraint on future work 2]

### Operational and Maintenance Impact

<!-- How does this affect day-to-day operations, debugging, monitoring,
     or the team's ability to change things later? -->

- [Impact 1]
- [Impact 2]

### Positive Consequences

- [Expected gain 1]
- [Expected gain 2]

### Negative Consequences and Risks

- [Risk or cost 1]
- [Risk or cost 2]

***

## Boundaries and Responsibilities

<!-- What lives where as a result of this decision?
     What does NOT belong where? -->

- [What lives here]
- [What does not belong here]
- [Ownership boundary]

***

## Assumptions

<!-- What must be true for this decision to remain valid?
     What would invalidate it? -->

- [Assumption 1]
- [Assumption 2]

***

## Reversibility

<!-- How easy is it to undo this decision later?
     What would rollback or migration look like?
     Is this a one-way door or a two-way door? -->

[Description of reversal difficulty and migration path if needed]

***

## Review Trigger

<!-- Under what conditions should this decision be reconsidered?
     How will we know it is working?
     Include a timeline for re-evaluation if applicable. -->

- [Condition that would invalidate this decision]
- [Signal that the decision is working correctly]
- [Timeline for re-evaluation if applicable]

***

## Implementation Guidance

### Build First

- [What to implement first as a result of this decision]
- [Foundation steps]

### Defer or Keep Open

- [What can safely wait]
- [What should remain intentionally flexible]

### Dependencies

- [What this decision depends on]
- [What depends on this decision]

***

## Follow-Up Actions

- [ ] [Action 1 — owner]
- [ ] [Action 2 — owner]
- [ ] [Action 3 — owner]

***

## Related Documents and Decisions

- [contexts/...]
- [skills/...]
- [workflows/...]
- [Related ADRs]
- [Links to diagrams, tickets, specs, benchmarks, research]

```

***

## FIELD GUIDANCE

- Keep the problem statement concrete — include metrics and impact, not vague improvement language
- Do not skip alternatives — the rejected options matter as much as the chosen one for future reasoning
- Always state tradeoffs accepted AND tradeoffs rejected — these are different questions
- Assumptions and review triggers preserve the decision's validity window — do not omit them
- Estimated effort per option forces realistic assessment alongside pros and cons
- Use this to preserve structural memory, not to celebrate the decision or justify it after the fact

***

## QUALITY CRITERIA FOR A GOOD ADR

Before filing this ADR, verify:

- [ ] Problem is clearly stated with concrete impact — not vague "we need to improve X"
- [ ] Current state is described — what exists today
- [ ] At least 3 options were genuinely considered — not 1 option plus 2 strawmen
- [ ] Pros AND cons listed for EVERY option — not just the chosen one
- [ ] Estimated effort included for each option
- [ ] Decision rationale explains WHY, not just restates WHAT
- [ ] Tradeoffs accepted are named explicitly — what are we sacrificing?
- [ ] Tradeoffs rejected are named — what did other options offer that we chose not to have?
- [ ] Consequences cover what changes, what this enables, and what new constraints are created
- [ ] Operational and maintenance impact noted
- [ ] Assumptions are stated — what would invalidate this decision?
- [ ] Reversibility is described — one-way door or two-way door?
- [ ] Review trigger is defined — when should we reconsider?
- [ ] A skeptical engineer reading this 6 months later can understand the full reasoning without asking anyone
