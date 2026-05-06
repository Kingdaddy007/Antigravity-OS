# RUBRIC: DEBUGGING QUALITY

**Version:** Gold v1.0
**Layer:** 10 — Evaluation
**Tier:** 3 — Loaded on demand
**File:** rubrics/debugging-rubric.md
**Purpose:** Self-assessment matrix for evaluating debugging quality — was the investigation thorough, the root cause real, and the fix complete?
**Loaded When:** Phase 7 of any debugging task. Evaluating whether a bug fix is ready for delivery.
**References:** skill-debugging.md, workflow-debug-issue.md

***

## HOW TO USE THIS RUBRIC

After completing a debugging investigation, evaluate your work against
each dimension below. Score each dimension.

- If **Root Cause** scores **Failing** — do not deliver. The bug is not
  actually fixed.

- If **Regression Prevention** scores **Needs Work** or below — write a
  regression test before delivery.

- If **3 or more dimensions** score **Needs Work** — revisit the
  investigation before delivering.

Use this rubric:

- After debugging work is complete
- During postmortem or incident review
- During benchmark comparison of debugging approaches
- When checking the quality of a bug-fix workflow
- When comparing weak versus strong debugging practice

***

## WHAT THIS RUBRIC EVALUATES

This rubric evaluates debugging quality across:

- Problem definition and symptom clarity
- Evidence gathering and use
- Hypothesis quality and discipline
- Symptom versus cause separation
- Root-cause depth and identification
- Fix precision and quality
- Verification strength
- Regression prevention and defense
- Structural and learning awareness

This rubric is for judging whether a bug was truly understood
and responsibly fixed — not merely whether the symptom
temporarily disappeared.

***

## EVALUATION MATRIX

### 1. PROBLEM DEFINITION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Issue stated clearly and precisely. Expected versus actual behavior made explicit. Scope, frequency, impact, and reproduction conditions identified. Environment and trigger conditions known. |
| **Acceptable** | Problem reasonably well defined. Expected versus actual behavior mostly clear. Most conditions identified. Minor gaps in scope or environment context. |
| **Needs Work** | Vague issue description. No clear distinction between expected and actual behavior. No environmental context. Reproduction conditions unstated. |
| **Failing** | Problem never clearly defined. Investigation began without understanding what was actually wrong or under what conditions it occurred. |

***

### 2. EVIDENCE GATHERING

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Comprehensive evidence collected: logs, stack traces, reproduction steps, data state, recent changes, metrics, traces. Evidence documented clearly. Nothing assumed without data. Investigation driven by evidence rather than guesses. |
| **Acceptable** | Sufficient evidence to support diagnosis. Key data points collected. Minor gaps in evidence that do not affect the conclusion. Claims supported by observable data. |
| **Needs Work** | Limited evidence gathered. Some guesswork involved. Key data sources not checked. Conclusion based more on intuition than data. "Probably" reasoning with no supporting basis. |
| **Failing** | No evidence gathered. Jumped straight from symptom to fix. Shotgun debugging — random changes made hoping to fix the issue. Guesses presented as conclusions. |

***

### 3. HYPOTHESIS QUALITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Three or more hypotheses generated. Each ranked by likelihood and blast radius. Each tested against evidence. Eliminated systematically until root cause confirmed. No first-idea-as-truth bias. |
| **Acceptable** | Two or more hypotheses considered. Leading hypothesis confirmed with evidence before fixing. Alternative explanations acknowledged. Reasoning explicit enough to trust. |
| **Needs Work** | Only one hypothesis considered — the first guess. No alternatives explored. Confirmation bias likely: looked for evidence supporting the guess and ignored contradictions. No narrowing logic. |
| **Failing** | No hypotheses formed. Jumped from "it is broken" to "let me change this and see." No diagnostic process visible. First coherent story treated as truth without testing alternatives. |

***

### 4. SYMPTOM VERSUS CAUSE SEPARATION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Clear distinction between what was observed (symptom) and what caused it (root cause). Symptom precisely restated. Multiple layers of causation explored via five-whys or equivalent. Structural weakness understood and surfaced. |
| **Acceptable** | Symptom and cause are distinguished. Root cause identified one level deeper than the immediate trigger. Cause explains the timing and conditions of the issue. |
| **Needs Work** | Symptom and cause are conflated. Fix addresses the immediate trigger but not the underlying structural issue. Same class of bug could still return. |
| **Failing** | No distinction made. Symptom treated as the cause. Fix masks the problem rather than solving it. Bug will recur in a different form. |

***

### 5. ROOT CAUSE IDENTIFICATION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Root cause is structural — explains all observed symptoms. Confirmed with evidence, not just plausible. Investigation reaches a level where prevention is possible. Root cause is more than symptom-level. |
| **Acceptable** | Root cause identified and explains the primary symptom. Supported by evidence. May not reach the deepest structural level but is correct at the implementation level. |
| **Needs Work** | Cause identified but may be only the immediate trigger, not the root cause. The same class of bug could recur because the structural issue remains. Root cause confidence is lower than the issue's importance warrants. |
| **Failing** | No root cause identified. Fix applied to the symptom. Underlying problem persists. Issue declared fixed without understanding why. |

***

### 6. FIX QUALITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Targeted fix addressing root cause. Minimum effective change. No unnecessary modifications. Follows coding and project standards. Fix is self-explanatory or commented with WHY. Blast radius controlled. |
| **Acceptable** | Fix addresses the root cause correctly. Slightly broader than minimum necessary but does not introduce risk. Follows conventions. Scope is proportionate to the identified cause. |
| **Needs Work** | Fix addresses the symptom more than the cause. Changes are broader than needed. Some unrelated modifications included. Broad random fix mixed with debugging. |
| **Failing** | Fix is a workaround or hack. Introduces new complexity. Masks the symptom. Changes unrelated code. Creates regression risk. Solution too large or too vague for the identified cause. |

***

### 7. VERIFICATION STRENGTH

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Original symptom verified resolved. Full test suite passes. Adjacent functionality checked. Edge cases around the fix verified. No regressions introduced. Verified in the correct environment. Evidence supports "fixed" — not just "looks right." |
| **Acceptable** | Original symptom verified resolved. Test suite passes. Basic regression check done. Confidence gaps stated honestly where they exist. |
| **Needs Work** | Original symptom appears resolved but not thoroughly verified. Test suite not fully run. No regression checking. Declared fixed without re-verification or reproduction re-check. |
| **Failing** | No verification performed. Fix assumed to work. Test suite not run. No validation beyond "looks right." |

***

### 8. REGRESSION PREVENTION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Regression test written that fails before the fix and passes after. Test covers the exact conditions that triggered the bug. Recurrence is now detectable. Observability or alerting gaps improved where relevant. |
| **Acceptable** | Regression test written. Covers the main failure scenario. May not cover all edge variations. Recurrence is less likely now. |
| **Needs Work** | No regression test written, but existing tests updated. Partial coverage of the failure scenario. Same class of issue likely to return without durable guardrail. |
| **Failing** | No regression test. No test changes. The bug can return without detection. Fix is a temporary patch with no recurrence protection. |

***

### 9. STRUCTURAL AND LEARNING AWARENESS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | If the issue exposed a deeper structural weakness, that was surfaced clearly. Recurrence risk treated as part of the result. The debugging process improved understanding or observability. The failure mode is now clarified for future work. The team or system learned something from this issue. |
| **Acceptable** | Structural implications noted even if not fully resolved. Some process or observability improvement made or recommended. Issue closed with enough insight to be useful. |
| **Needs Work** | Issue closed with no structural insight. No process improvement. No observability gain. The same class of issue could return without recognition. |
| **Failing** | Issue closed with no insight. No learning captured. No improvement to the system's ability to detect or prevent this class of problem. |

***

## SCORING SUMMARY

| Dimension | Score | Notes |
| :--- | :--- | :--- |
| Problem Definition |||
| Evidence Gathering |||
| Hypothesis Quality |||
| Symptom vs Cause Separation |||
| Root Cause Identification |||
| Fix Quality |||
| Verification Strength |||
| Regression Prevention |||
| Structural and Learning Awareness |||
***

## DELIVERY DECISION

| Result | Decision |
| :--- | :--- |
| All Excellent / Acceptable | ✅ Ready to deliver |
| Regression Prevention Needs Work or below | ⚠️ Write regression test before delivery |
| Root Cause Failing | ❌ Do not deliver — the bug is not actually fixed |
| Any 3+ dimensions Needs Work | ❌ Revisit investigation before delivery |

***

## MINIMUM PASS STANDARD

A debugging effort should not be considered strong if it lacks:

- Evidence — investigation must be data-driven, not guess-driven
- Root-cause understanding — symptom disappearing is not enough
- Post-fix verification — confirmed resolved, not assumed resolved

If the symptom merely disappeared, that is not enough.

***

## COMMON FAILURE PATTERNS

### Guess-Then-Code

Changes made before strong evidence is gathered. Effort
is wasted and the real cause often survives untouched.

### First-Coherent-Story Bias

The first plausible explanation is treated as truth without
seriously testing alternatives. Confirmation bias throughout.

### Symptom Suppression Presented as Resolution

Visible failure is reduced but the real mechanism remains
poorly understood. Bug will recur in a different form.

### No Regression Memory

The same class of issue can easily return because no
durable guardrail, test, or alert was added.

### Vague Closure Language

The issue is called fixed without clear verification,
confidence boundaries, or evidence of resolution.

### Scope Creep Inside a Debug Task

Broad unrelated refactor mixed into the fix, making it
harder to verify what actually resolved the bug.

***

## FINAL QUESTIONS

Before closing this investigation, ask:

- If this issue happened again, would the team understand it faster now?
- Was the process strong enough that a bad outcome would still teach us something useful?
- If the fix is wrong, where is that most likely to show up?
- Would another engineer trust this fix enough to build on it?
- Was the process strong enough to call this truly resolved?

***

## A good debugging process does not merely make the error disappear — it makes the failure explainable, the fix trustworthy, and recurrence less likely
