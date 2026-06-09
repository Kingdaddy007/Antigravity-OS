# TEMPLATE: FEATURE PLAN

**Version:** Gold v1.1 (Master Merge)
**Layer:** 9 — Output Contract
**Tier:** 3 — Loaded on demand
**File:** templates/feature-plan.md
**Purpose:** Standardized format for scoping and planning a feature before implementation — ensuring the problem is defined, scope is bounded, success is measurable, and the riskiest assumption is identified before a line of code is written.
**Loaded When:** Scoping a new feature, creating a feature brief, planning sprint work, or evaluating whether a feature request is worth building. Referenced by `workflow-build-feature.md` and `skill-product-thinking.md`.

***

## WHEN TO USE THIS TEMPLATE

Use this template when:

- Starting a new feature that will take more than a few hours
- Scoping work for a sprint
- Turning a request into an implementation-ready spec
- Communicating what will be built and why to the team
- Evaluating whether a feature request is worth building

Do NOT use for bug fixes, small improvements, or refactoring tasks. A brief commit message or ticket description is sufficient for those.

***

## THE TEMPLATE

```markdown

# Feature Plan: [Feature Name]

***

## Date

[YYYY-MM-DD]

## Author

[Who wrote this plan]

## Owner(s)

- [Owner 1]
- [Owner 2]

***

## The Problem

### User Problem Statement

<!-- One sentence, no technical jargon.
     If you cannot state the problem in one sentence,
     the problem is not yet understood well enough. -->

[User problem in plain language]

### Job-to-be-Done

<!-- Frame as: "When [situation], the user wants to [motivation]
     so that they can [expected outcome]." -->

When [situation], the user wants to [motivation] so that they can [expected outcome].

### Who Has This Problem

- Primary user: [user type]
- Secondary stakeholders: [list]
- Affected teams or systems: [list]
- Frequency: [how often do they encounter this problem?]
- Severity: [how painful is the current state?]

### Evidence

<!-- How do we know this problem exists?
     Data, user feedback, observation, support tickets? -->

- [Evidence 1]
- [Evidence 2]
- [Evidence 3]

### Current Experience

<!-- What does the user do TODAY to solve this problem?
     What is painful about the current approach? -->

[Description of current state and friction]

***

## The Solution

### Proposed Approach

<!-- High-level description of what is being built.
     Focus on the user experience first, not the implementation. -->

[What is being built and how it solves the problem]

### Objective Statement

We are building [X] so that [user/system] can [achieve outcome].

### User Flow or System Flow

1. [Step 1]
2. [Step 2]
3. [Step 3]

***

## Success Criteria

### Success Metric

<!-- How will success be known? Must be measurable.
     Define before building, not after. -->

We will know this succeeded when [measurable behavior] changes by [amount] within [timeframe].

| Metric | Baseline | Target | Timeframe |
| :--- | :--- | :--- | :--- |
| [metric 1] | [current] | [goal] | [when] |
| [metric 2] | [current] | [goal] | [when] |

### Measurement Plan

<!-- How will the success metric be tracked?
     What instrumentation is needed? -->

- Track: [what events or metrics]
- Tool: [analytics tool or custom logging]
- Dashboard: [where to view results]

### Additional Success Criteria

- [Criterion 1 — specific behavior or outcome]
- [Criterion 2]
- [Criterion 3]

***

## Scope

### In Scope — This Version

<!-- The minimum set of capabilities that tests the core hypothesis.
     Mark each as essential to core value. -->

- [x] [Capability 1 — essential to core value]
- [x] [Capability 2 — essential to core value]
- [x] [Capability 3 — essential to core value]

### MVP — Smallest Valuable Slice

[What is the smallest version worth building first that still tests the core hypothesis?]

### Out of Scope — Phase 2 or Future

<!-- Explicitly listed to prevent scope creep.
     Include reason each item is deferred. -->

- [Deferred item 1 — why not essential now]
- [Deferred item 2 — why not essential now]
- [Deferred item 3 — why not essential now]

***

## Riskiest Assumption

<!-- The assumption that, if wrong, invalidates the entire effort.
     This should be tested FIRST before heavy implementation. -->

**Assumption:** [State the assumption clearly]

**Test:** [How to validate it with minimal effort]

**If wrong:** [What would be done instead]

***

## Additional Assumptions

- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

***

## Technical Approach

### Architecture Impact

<!-- Does this require new modules, schema changes, new services? -->

- New module needed: [yes / no — where]
- Schema changes: [yes / no — what]
- New API endpoints: [yes / no — what]
- New UI pages or components: [yes / no — what]
- Background jobs or async changes: [yes / no — what]

### Affected System Areas

- [Module / service / screen / endpoint 1]
- [Area 2]
- [Area 3]

### Key Technical Decisions

<!-- Non-obvious technical choices that should be documented -->

- [Decision 1 and brief rationale]
- [Decision 2 and brief rationale]

### States and Edge Cases

- Loading:
- Empty:
- Error:
- Permission or role restrictions:
- Other important edge conditions:

### Dependencies

<!-- What must exist before this can be built? -->

- [Dependency 1]
- [Dependency 2]
- [Dependency 3]

### Security Considerations

<!-- Auth, input validation, data exposure concerns? -->

- [Security consideration 1]
- [Security consideration 2]

***

## Implementation Plan

### Recommended Build Sequence

<!-- What order should this be built in? -->

1. [Step 1 — what and estimated effort]
2. [Step 2 — what and estimated effort]
3. [Step 3 — what and estimated effort]

### Estimated Total Effort

[X days / X story points]

***

## Tradeoffs and Risks

### Tradeoffs Accepted

- [What is being sacrificed and why it is acceptable]
- [Tradeoff 2]

### Risks

| Risk | Likelihood | Impact | Mitigation |
| :--- | :--- | :--- | :--- |
| [Risk 1] | [Low/Med/High] | [Low/Med/High] | [How to mitigate] |
| [Risk 2] | [Low/Med/High] | [Low/Med/High] | [How to mitigate] |
| [Risk 3] | [Low/Med/High] | [Low/Med/High] | [How to mitigate] |

### Opportunity Cost

<!-- What is NOT being built by choosing to build this?
     Why is this feature higher priority? -->

[What is being deferred and why this feature takes precedence]

***

## Verification Plan

- Unit tests: [what to test]
- Integration tests: [what to test]
- Manual testing: [key scenarios to verify]
- E2E tests: [if critical path — what to cover]
- Observability or monitoring: [what signals indicate success or failure]

***

## Rollout Plan

### Release Strategy

[How this should be released — direct / feature flag / staged / canary]

### Rollout Notes

- Feature flag: [yes / no — flag name if yes]
- Staged rollout: [yes / no — sequence if yes]
- Migration need: [yes / no — what if yes]
- Rollback path: [how to revert if needed]
- Support or training implications: [if any]

### Monitoring After Release

- [Signal 1 — what to watch]
- [Signal 2 — what to watch]
- [Signal 3 — what to watch]

***

## Exit Strategy

### If This Does Not Work

<!-- What happens if the feature does not achieve its success metric? -->

- Monitor adoption for: [timeframe]
- If adoption is below [threshold]: [iterate / pivot / remove]
- Removal complexity: [easy — feature flag / moderate — code removal / hard — data migration]

***

## Open Questions

- [Question 1]
- [Question 2]
- [Question 3]

***

## Follow-Up and Deferred Work

- [Deferred item 1]
- [Deferred item 2]
- [Deferred item 3]

***

## Related Files

- `workflows/workflow-build-feature.md`
- `skill-product-thinking.md`
- [contexts/...]
- [workflows/...]
- [skills/...]

***

## Approval Checklist

- [ ] Problem is validated — evidence exists
- [ ] Problem statement is in user language, no technical jargon
- [ ] Job-to-be-Done is properly framed
- [ ] Success metric is defined and measurable
- [ ] Scope clearly separates IN from OUT
- [ ] Riskiest assumption is identified with a validation plan
- [ ] Technical approach addresses architecture, security, and dependencies
- [ ] Effort is estimated
- [ ] Opportunity cost is acknowledged
- [ ] Exit strategy exists
- [ ] Rollout and rollback plan defined

```

***

## FIELD GUIDANCE

- Problem statement must be in user language — no implementation jargon. If it cannot be stated in one sentence, the problem is not yet understood.
- Job-to-be-Done must follow the full frame: situation, motivation, outcome. Do not shortcut this.
- Success metric must be measurable and defined before building. "Users like it" is not a success metric.
- Scope must be explicit or the feature will drift. Out of scope items are as important as in scope items.
- Riskiest assumption should be tested first with minimal implementation. If the assumption is wrong, the feature may not be worth building.
- Opportunity cost is not optional — naming what is not being built forces honest prioritization.
- Exit strategy prevents sunk cost thinking — define upfront what would trigger removal or pivot.

***

## QUALITY CRITERIA FOR A GOOD FEATURE PLAN

Before filing this plan, verify:

- [ ] Problem statement is in user language — no technical jargon
- [ ] Job-to-be-Done is properly framed: situation, motivation, outcome
- [ ] Evidence is cited — not just intuition
- [ ] Success metric is specific and measurable — not "users like it"
- [ ] Scope clearly separates IN from OUT with deferred items explained
- [ ] MVP slice is identified — the smallest version that tests the hypothesis
- [ ] Riskiest assumption is identified with a concrete validation plan
- [ ] Technical approach addresses architecture, schema, security, and dependencies
- [ ] States and edge cases are listed — not just the happy path
- [ ] Effort estimate is realistic
- [ ] Opportunity cost is acknowledged — not ignored
- [ ] Exit strategy exists — what if it does not work?
- [ ] Rollout and rollback plan defined before build begins
