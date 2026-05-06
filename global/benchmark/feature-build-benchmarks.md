# BENCHMARK: FEATURE BUILDING

**Version:** Gold v1.0
**Layer:** 11 — Verification
**Loading Tier:** 3 — **LOADED ON DEMAND**

***

## PURPOSE

This file contains repeatable test scenarios for evaluating Anti-Gravity's
feature building capability — from problem definition through
implementation to delivery.

### Evaluate With

- [rubric-code-quality.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-code-quality.md)
- [rubric-communication.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-communication.md)
- [rubric-testing.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-testing.md)
- [rubric-security.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-security.md)

### Tests

- `skill-coding.md`
- `skill-product-thinking.md`
- `workflow-build-feature.md`

***

## WHAT THIS BENCHMARK TESTS

This benchmark evaluates whether Anti-Gravity can:

- Understand a feature request correctly and identify the real goal
- Ask useful clarifying questions before acting
- Fit implementation into the existing architecture
- Scope the solution appropriately — not over- or underbuilding
- Produce maintainable implementation guidance or code
- Surface security, testing, UX, and edge-case concerns
- Show domain rule and authorization awareness where relevant
- Verify and communicate the solution clearly

This benchmark should reveal whether Anti-Gravity behaves like a
senior builder or a generic code generator.

***

## HOW TO USE THESE BENCHMARKS

1. Pick a scenario below
2. Present it to Anti-Gravity as a real task — do not mention it is a benchmark
3. Let Anti-Gravity process it using its full system — skills, contexts, and workflows active as appropriate
4. Evaluate the output against the rubrics listed above
5. Record the score in `memory/benchmark-results.md`
6. Compare scores across runs and versions to track improvement

***

## EVALUATION DIMENSIONS

Score benchmark outputs across these dimensions:

1. Objective clarity — did it understand the real feature goal?
2. Question quality — did it ask what it needed to know first?
3. Architecture fit — does the solution belong in the right layer?
4. Scope discipline — proportionate to the actual problem?
5. Implementation quality — correct, maintainable, standard-compliant?
6. Edge-case and state awareness — loading, empty, error, failure paths?
7. Testing awareness — what should be verified and how?
8. Security awareness — auth, authz, trust boundaries where relevant?
9. Communication clarity — can a teammate act on this output?
10. Next-step usefulness — does it move work forward concretely?

***

## SCENARIO 1 — Simple CRUD Feature

### Prompt [SCENARIO 1]

Build a feature that lets users add tags to tasks. A task can have
multiple tags. Tags are simple text labels. Users should be able to
add tags when creating or editing a task, and filter tasks by tag
on the sprint board.

### What Excellent Output Looks Like [SCENARIO 1]

- Asks clarifying questions BEFORE building — tag uniqueness? per-project or global? maximum tags per task?
- Defines the user problem and Job-to-be-Done
- Designs the data model first — junction table, not JSON array in the task record
- Considers schema migration approach
- Implements with proper validation — tag length limits, duplicate prevention, special character handling
- Handles edge cases — empty tags, very long tags, special characters
- Includes error handling across UI and backend
- Follows project coding standards and surrounding patterns
- Mentions what to test and how
- Addresses the filtering requirement including index considerations

### Red Flags [SCENARIO 1]

- Jumps straight to code without understanding requirements
- Stores tags as a JSON array in the task record — poor data model
- No input validation on tag content
- No mention of migration strategy
- No consideration of how filtering works at the database level
- Ignores existing patterns in the codebase

***

## SCENARIO 2 — Feature With Business Logic

### Prompt [SCENARIO 2]

Build a feature that prevents users from moving more than 20 story
points into a single sprint. When a user tries to add a task that
would exceed 20 points, show a warning but still allow it if they
confirm.

### What Excellent Output Looks Like [SCENARIO 2]

- Asks about the 20-point limit — is this configurable? Per-project setting or global?
- Identifies this as a business rule that belongs in domain rules
- Implements the check server-side, not just client-side
- Designs the UX — warning modal with current points, task points, and resulting total visible
- Handles edge cases — task with no story points, sprint with no tasks, recalculation on task removal
- Implements as a soft limit with confirmation, not a hard block — per the stated requirement
- Considers concurrent state — what happens if two users add tasks simultaneously?
- Follows existing Server Action and Result type patterns

### Red Flags [SCENARIO 2]

- Implements only client-side validation — bypassable
- Hard-blocks instead of warning — does not match the requirement
- No consideration of concurrent additions
- No mention of where this business rule should be documented
- Skips the UX design for the warning modal states

***

## SCENARIO 3 — Feature With External Integration

### Prompt [SCENARIO 3]

Add Slack notifications when a task is marked as blocked. Send a
message to the project's configured Slack channel with the task
title, who blocked it, and a link back to the task.

### What Excellent Output Looks Like [SCENARIO 3]

- Identifies this as an async operation — should not block the task status change
- Designs for failure — what if the Slack API is down? Queue with retry; do not fail the status change
- Asks about Slack configuration — where is the webhook URL stored? per-project setting?
- Considers security — webhook URL is a secret, stored encrypted, not hardcoded
- Implements via background job, not a synchronous API call
- Handles edge cases — no Slack channel configured, invalid webhook URL, rate limiting
- Designs the message format — clear, actionable, includes link
- Considers mute or opt-out behavior for notifications
- Follows existing integration patterns from the architecture context

### Red Flags [SCENARIO 3]

- Synchronous Slack API call inside the status change endpoint
- No error handling for Slack API failures
- Webhook URL hardcoded or stored in plain text
- No mention of async processing
- No consideration of what happens when Slack is unavailable
- Blocks the task status change if notification fails

***

## SCENARIO 4 — Feature Requiring Scope Discipline

### Prompt [SCENARIO 4]

Build a complete project analytics dashboard with charts showing
sprint velocity over time, task completion rates by team member,
burndown charts for the current sprint, cycle time distribution,
and a predictive completion forecast.

### What Excellent Output Looks Like [SCENARIO 4]

- Pushes back on scope — "This is five distinct features. Which is most important to the user right now?"
- Applies product thinking — what user problem does each chart solve?
- Identifies the riskiest assumption — "Do users actually want analytics, or are we assuming they do?"
- Suggests a phased approach starting with the highest-value, lowest-effort chart
- Recommends starting with the cheapest win, measuring adoption, and expanding only if users engage
- For whichever chart is built first — proper implementation with loading, empty, and error states
- Considers performance — pre-computed metrics versus real-time aggregation
- Defines a success metric for the analytics feature before building

### Red Flags [SCENARIO 4]

- Attempts to build all five charts at once
- No scope pushback
- No phasing suggestion
- No success metric defined
- No question of whether users actually need analytics
- Over-engineering the data pipeline before validating demand

***

## SCENARIO 5 — Feature Modification Changing Existing Behavior

### Prompt [SCENARIO 5]

Change the task assignment flow. Currently anyone in the project can
assign any task to any member. We need to add a restriction: only
admins and the task creator can reassign tasks. Members can only
assign unassigned tasks to themselves.

### What Excellent Output Looks Like [SCENARIO 5]

- Identifies this as a business rule change and flags it for domain rule documentation
- Identifies this as an authorization change — high-risk, loads security thinking
- Reviews the current implementation before modifying
- Updates the authorization check server-side in the appropriate layer
- Updates the UI to disable or contextually adjust the reassign option based on role — disabled with tooltip, not silently hidden
- Considers edge cases — bulk reassignment, tasks assigned before this change is enforced
- Writes a migration rationale — existing assignments are grandfathered
- Adds tests for the new authorization rules
- Updates the role permissions matrix in security baselines

### Red Flags [SCENARIO 5]

- Changes only the UI without server-side authorization enforcement
- Does not consider existing assignments
- No test for the new authorization rule
- Does not update documentation — domain rules or security baselines
- Ignores the UX for unauthorized users — silent failure or confusing missing control

***

## SCENARIO 6 — Build a Background Export Feature

### Prompt [SCENARIO 6]

Users should be able to request a CSV export of filtered report data.
The export should run asynchronously, notify the user when complete,
handle failures, enforce permissions, avoid blocking the UI, and expire
old export files after a defined period.

### What Excellent Output Looks Like [SCENARIO 6]

- Identifies this as a multi-surface feature spanning UI, API, background processing, permissions, and file lifecycle
- Designs for async — job queue, background processing, not synchronous response
- Addresses permission enforcement before job is queued
- Defines notification path — how does the user know the export is ready?
- Thinks through file expiration and cleanup
- Considers observability and failure handling — what happens if the job fails partway through?
- Designs the user flow — request → waiting state → completion → download
- Notes testing and verification expectations

### Red Flags [SCENARIO 6]

- Synchronous export that blocks the UI and request lifecycle
- No background processing
- No permissions discussion
- No file lifecycle or expiration thinking
- No failure or monitoring consideration

***

## SCENARIO 7 — Build a Team Invitation Flow

### Prompt [SCENARIO 7]

Implement a team invitation flow where an admin can invite a user by
email, assign a role, resend pending invites, revoke unused invites,
prevent duplicate active invitations, and show invite status in the
admin UI.

### What Excellent Output Looks Like [SCENARIO 7]

- Identifies role and authz sensitivity — only admins can invite
- Designs the invite lifecycle and state model — pending, accepted, revoked, expired
- Addresses duplicate prevention logic explicitly
- Designs admin visibility of invite state in the UI
- Handles domain and permission edge cases throughout
- Surfaces likely DB and API implications
- Notes testing around edge cases — duplicate, revocation, expiry

### Red Flags [SCENARIO 7]

- Naive "send email and create row" solution
- No duplicate or revocation logic
- No state model for the invite lifecycle
- No role or permission enforcement thinking
- No verification or testing plan

***

## SCORING GUIDE

For each scenario, evaluate using `rubric-code-quality.md` dimensions:

| Dimension | Weight for Feature Building |
| :--- | :--- |
| Correctness | High — does it solve the actual problem? |
| Readability | High — can a teammate understand and use this? |
| Error Handling | High — are failure paths covered? |
| Simplicity | Medium — is it appropriately scoped? |
| Convention Compliance | Medium — does it match the codebase? |
| Security | Conditional — higher weight when auth is involved |
| Testability | Medium — can the behavior be verified? |
| Maintainability | Medium — can this be changed later safely? |

Record all scores in `memory/benchmark-results.md`.

***

## FINAL RULE

A strong feature-building benchmark response does not just produce
code — it shows that Anti-Gravity understands:

- What is being built and why it matters
- Where it belongs in the architecture
- What can go wrong and how to handle it
- How to verify it works correctly
- How to keep the implementation proportionate to the actual goal

A system that produces the right feature, in the right shape, with
the right constraints visible is behaving like a senior builder —
not a generic code generator.
