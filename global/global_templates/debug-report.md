# TEMPLATE: DEBUG REPORT

**Version:** Gold v1.1 (Master Merge)
**Layer:** 9 — Output Contract
**Tier:** 3 — Loaded on demand
**File:** templates/debug-report.md
**Purpose:** Standardized format for documenting bug investigations — symptom, root cause, fix, and prevention. Ensures symptoms, evidence, hypotheses, root cause, and regression protection are captured consistently and not blurred together.
**Loaded When:** Completing a significant debugging session. Referenced by `workflow-debug-issue.md`. Especially important for P1/P2 incidents and recurring bugs.

***

## WHEN TO USE THIS TEMPLATE

Use this template when:

- Completing a P1 or P2 incident fix
- Fixing a bug that took significant investigation effort
- Fixing a bug that has recurred before
- Any fix where the root cause was non-obvious and worth documenting
- Bug investigation summaries for handoff
- Regression analysis reports
- Flaky-test investigation reports

Do NOT use for trivial fixes — typos, obvious one-line fixes. A commit message is sufficient for those.

***

## THE TEMPLATE

```markdown

# Debug Report: [Brief Description of Bug]

***

## Date

[YYYY-MM-DD]

## Severity

[P1 — Critical / P2 — Major / P3 — Minor / P4 — Cosmetic]

## Reporter

[Who reported it — user, monitoring alert, team member]

## Investigator

[Who investigated and fixed it]

## Owner

[Person or team responsible for this fix and follow-up]

***

## Symptom

### Observed Behavior

<!-- What was actually happening? Be precise. Not "it was broken." -->

[Exact observed behavior]

### Expected Behavior

<!-- What should have been happening? -->

[Correct expected behavior]

### Affected Scope

- Users affected: [all / subset — describe which]
- Systems or modules: [list]
- Environments: [Production / Staging / Local / Multiple]
- Duration: [how long was this happening before detection?]
- Frequency: [Always reproducible / Intermittent — approximately X% / One-time]
- Data impact: [any data corruption or loss?]
- Immediate mitigation needed: [yes / no]

***

## Environment

- Environment: [Production / Staging / Local / Preview]
- Browser or client: [if relevant]
- User conditions: [specific user type, data state, or timing]
- Relevant environment notes: [differences from other environments that matter]

***

## Reproduction

### Reproduction Status

[Reproducible / Intermittent / Production-only / Not yet reproducible]

### Reproduction Steps

<!-- Minimum steps to trigger the bug -->

1. [Step 1]
2. [Step 2]
3. [Step 3]

Observe: [what goes wrong]

### Bounded Search Area

- Reproduces when: [conditions]
- Does not reproduce when: [conditions]
- Narrowed system area: [what was ruled out]

***

## Evidence Collected

<!-- What data was collected during investigation? -->

- Logs: [relevant log entries]
- Error messages: [exact error text or stack trace]
- Traces: [distributed traces if available]
- Metrics: [relevant metric observations]
- Screenshots: [if applicable]
- Data state: [relevant database or state observations]
- Recent changes: [relevant recent deployments, config changes, dependency updates]
- Other evidence: [anything else that informed the investigation]

***

## Hypotheses Considered

### Hypothesis 1 — [Name] (most likely)

- Description: [what was suspected]
- Why considered: [what made this plausible]
- Evidence for: [what supported this]
- Evidence against: [what contradicted this]
- Verdict: [Confirmed / Eliminated]

### Hypothesis 2 — [Name]

- Description: [what was suspected]
- Why considered: [what made this plausible]
- Evidence for: [what supported this]
- Evidence against: [what contradicted this]
- Verdict: [Confirmed / Eliminated]

### Hypothesis 3 — [Name]

- Description: [what was suspected]
- Why considered: [what made this plausible]
- Evidence for: [what supported this]
- Evidence against: [what contradicted this]
- Verdict: [Confirmed / Eliminated]

***

## Root Cause

### What Caused It

<!-- The actual root cause — not the symptom, not the immediate trigger,
     but the structural reason this bug existed. -->

[Root cause explanation]

### Why It Was Not Caught Earlier

<!-- What allowed this bug to reach production?
     Missing test? Untested edge case? Configuration difference
     between environments? Observability gap? -->

[Explanation]

### 5 Whys Analysis (if applicable)

1. Why did [symptom] happen? → [immediate cause]
2. Why did [immediate cause] happen? → [deeper cause]
3. Why did [deeper cause] happen? → [structural cause]
4. Why did [structural cause] happen? → [systemic cause]
5. Why did [systemic cause] happen? → [root organizational or architectural cause]

***

## Fix

### What Was Changed

<!-- Specific code changes made -->

- File: [path] — [what changed and why]
- File: [path] — [what changed and why]

### Whether This Is Full Resolution or Mitigation Only

[Permanent fix / Temporary mitigation — if mitigation, what remains unresolved]

### Why This Fix Is Correct

<!-- Explain why this addresses the root cause, not just the symptom -->

[Explanation linking fix to root cause]

### Regression Test Added

<!-- What test was written to prevent recurrence?
     The test must fail WITHOUT the fix and pass WITH it. -->

- Test: [description]
- Location: [file path]
- Verifies: [what specific behavior it locks]

***

## Verification

- [ ] Original symptom is resolved
- [ ] Regression test passes — and fails without the fix
- [ ] Full test suite passes
- [ ] Adjacent functionality checked for side effects
- [ ] Fix deployed and verified in [staging / production]
- [ ] Monitoring confirms no new errors introduced
- [ ] Manual spot-check of key flows if applicable

### What Is Verified

- [Item 1]
- [Item 2]

### Not Yet Verified

- [Item 1 — and why it remains open]

### Regression Risk

[What nearby behavior might still be affected or worth watching?]

***

## Prevention

### What Would Have Prevented This Bug

<!-- What could be done to prevent this CLASS of bug in the future?
     Prevention measures must be actionable — not just "be more careful." -->

- [Prevention measure 1 — e.g., add input validation at the API boundary]
- [Prevention measure 2 — e.g., add integration test for this edge case]
- [Prevention measure 3 — e.g., add monitoring alert for this failure mode]

### Regression Protection Added

- [Test added]
- [Alert or instrumentation added]
- [Validation rule added]
- [Logging improvement added]
- Remaining guardrail gap: [if any protection was not yet added, explain why]

***

## Follow-Up Actions

| Action | Owner | Deadline | Status |
| :--- | :--- | :--- | :--- |
| [Action 1] | [Who] | [When] | [Done / Pending] |
| [Action 2] | [Who] | [When] | [Done / Pending] |
| [Action 3] | [Who] | [When] | [Done / Pending] |

***

## Lessons Learned

<!-- What did this bug teach us?
     Consider: process, observability, validation, architecture,
     ownership, testing gaps.
     Add to memory/mistakes-to-avoid.md if this is a pattern
     worth remembering. -->

- [Key takeaway 1]
- [Key takeaway 2]
- [Key takeaway 3]

***

## Related Files

- `workflows/workflow-debug-issue.md`
- `memory/mistakes-to-avoid.md` (if pattern recorded)
- [contexts/...]
- [skills/...]
- [Other related ADRs or reports]

```

***

## FIELD GUIDANCE

- Do not blur symptom, hypothesis, and root cause — they are three distinct things and must stay separate
- Be explicit if the result is mitigation rather than full resolution — do not call it fixed if it is not
- If no regression defense was added, explain why — do not leave it blank
- Root cause must be structural — not just "the code was wrong"
- Prevention measures must be actionable — not just "be more careful next time"
- The regression test must fail without the fix and pass with it — this is non-negotiable

***

## QUALITY CRITERIA FOR A GOOD DEBUG REPORT

Before filing this report, verify:

- [ ] Symptom is precisely described — not "it was broken"
- [ ] Reproduction steps are specific enough for someone else to reproduce the issue
- [ ] Multiple hypotheses were considered — not just the first guess
- [ ] Each hypothesis has evidence for and against, not just a verdict
- [ ] Root cause is structural — explains why the bug existed, not just what triggered it
- [ ] 5 Whys applied to reach systemic cause where relevant
- [ ] Fix addresses root cause, not just symptom
- [ ] Regression test is included — and verified to fail without fix
- [ ] Prevention measures are actionable and specific
- [ ] Remaining uncertainty is stated honestly — not hidden
- [ ] Lessons learned are recorded for the team's future benefit
