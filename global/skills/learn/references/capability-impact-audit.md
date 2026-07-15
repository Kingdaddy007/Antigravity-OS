# Capability Impact Audit

## INVENTORY EXISTING COVERAGE

Before proposing a change:

1. Search skill activation descriptions for the task and neighboring triggers.
2. Read the full candidate `SKILL.md` files.
3. Follow their reference-loading rules only to relevant guidance.
4. Inspect workflows that sequence those skills.
5. Inspect memory or evaluations only when they may already encode the lesson.
6. Separate a missing capability from failure to invoke or follow an existing one.

## GAP CLASSIFICATION

Classify the real gap:

| Gap | Signal | Preferred Change |
| --- | --- | --- |
| Routing | Correct capability exists but does not activate reliably | Tighten description and exclusions; add routing test |
| Core behavior | Skill omits a required decision or boundary | Patch `SKILL.md` |
| Deep guidance | Core behavior is correct but lacks a method, example, or diagnostic | Add or update a routed reference |
| Sequencing | Skills are sound but invoked in the wrong order | Update workflow and handoffs |
| Verification | Behavior regresses without detection | Add evaluation or completion gate |
| Memory | Durable project or cross-project fact is missing | Write scoped memory with approval |
| Ownership | A distinct recurring job has no coherent owner | Create a new skill |
| Execution | Guidance existed and routing was correct, but it was ignored | Change no capability; report discipline failure |

## NEW-SKILL TEST

Create a new skill only when all answers are yes:

1. Is the job reusable across multiple future tasks?
2. Does it have a distinct activation boundary?
3. Would placing it in a neighboring skill dilute that skill or create routing confusion?
4. Does it require its own workflow, output shape, or specialist references?
5. Can success and failure be evaluated?

Otherwise patch the smallest existing owner.

## OVERLEARNING CHECK

Challenge each proposed standard:

- What conditions made the lesson true here?
- Which future contexts share those conditions?
- Where would the rule become harmful?
- Is this a principle, preference, workaround, or temporary constraint?
- Is one dramatic occurrence outweighing contrary evidence?
- Would a reference example teach better than a hard rule?
- What observation would reverse the proposed change?

Record one steel-manned reason not to change the system.

## IMPACT MATRIX

| Proposed Change | Evidence | Destination | Routing Impact | Downstream Consumers | Risk | Rollback | Evaluation |
| --- | --- | --- | --- | --- | --- | --- | --- |

Flag conflicts where one update would cause a skill to activate over a better owner.

## APPROVAL PACKAGE

Present:

1. Verified learning.
2. Existing capability coverage.
3. Exact gap.
4. Recommended destination and smallest change.
5. Files or interfaces affected.
6. What remains unchanged.
7. Risks, rollback, and evaluation.
8. Explicit mutation boundary.

Stop after the approval package in audit mode.

## APPLY MODE

After explicit approval:

1. Re-read applicable directory contracts.
2. Preserve rollback copies for unversioned global files.
3. Load `skill-creator` for skill creation or refactoring.
4. Edit only the approved files.
5. Validate frontmatter, activation, exclusions, reference routing, output shape, and checklists.
6. Test positive and negative routing scenarios.
7. Verify all downstream workflow handoffs.
8. Report changed files, validation evidence, residual risks, and rollback location.
