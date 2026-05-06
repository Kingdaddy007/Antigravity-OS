---
name: DEBUGGING & SYSTEMATIC TROUBLESHOOTING
description: >
  Use this skill when investigating errors, crashes, unexpected behavior, or
  system failures. Activated when the user reports a bug, shares a stack trace
  or error message, describes tests failing unexpectedly, notices a regression
  (a feature that used to work no longer does), or when production telemetry
  alerts have fired. Examples: "this is broken", "I'm getting an error",
  "the tests are failing", "this stopped working after my last change",
  "the system is down". Do NOT use for general implementation work (use
  coding skill) or architecture decisions (use architecture skill).
---

# DEBUGGING & SYSTEMATIC TROUBLESHOOTING

## WHEN TO USE THIS

- User reports an error, crash, or unexpected behavior
- Stack trace or error message is provided
- Tests are failing unexpectedly
- A regression is suspected — something that previously worked no longer does
- Production telemetry alerts have fired

## NEVER DO

- Propose a fix before gathering evidence
- Change more than one variable at a time when testing a hypothesis
- Swallow exceptions or add null guards without finding why the bad state exists
- Declare a fix done without verifying the root cause, not just the symptom
- Leave failed experiments (commented blocks, abandoned print statements) in the code
- Say "I don't know why this works, but it does" and move on
- **Attempt a 4th fix if 3 fixes have already failed. Stop and question the architecture instead.**

---

## MINDSET

You are a detective. Do not guess; gather evidence. Assume your mental model of the codebase is flawed — rely exclusively on empirical data (logs, traces, state, errors).

The error message is a starting point, not the whole story. Fixing the symptom without understanding the cause guarantees the bug returns. Isolate variables, binary-search the execution path, apply the 5 Whys to find the structural flaw that allowed the bug to exist.

A bug is not just an error in the code. It is a failure of the system's boundaries, assumptions, or tests. The goal: understand exactly why it happened and prove the fix mathematically.

---

## DECISION FRAMEWORK — BY REPRODUCIBILITY

| Scenario | Characteristics | Approach |
| --- | --- | --- |
| **Consistently reproducible** | Happens every time a specific action is taken | Binary search via step-through or logging. Divide the execution path in half. Determine which half contains the error. Repeat. |
| **Intermittent / prod only** | Happens randomly, under load, or in specific environments | Telemetry analysis. Correlate structured logs across services. Formulate hypotheses around race conditions, state mutations, timeouts, environment discrepancies. |
| **System-wide outage** | System down or severely degraded | Mitigate first: roll back the deployment, isolate traffic, expand capacity. Once bleeding is stopped, begin root cause analysis. |

---

## DEBUGGING LENSES

Apply all eight before and during investigation:

### 1. Symptom Precision

- What exactly is wrong? Expected vs actual behavior?
- Under what conditions does it happen? Since when?

### 2. Reproducibility

- Can this be reproduced reliably? In which environment?
- What is the smallest environment where it can still be observed?

### 3. Scope Isolation

- Which component, module, boundary, or dependency is most implicated?
- Is this local, distributed, data-driven, environment-specific, timing-sensitive, or input-specific?

### 4. Change History

- What changed recently in code, config, dependencies, infrastructure, data, or usage patterns?
- Did this appear after a release, migration, flag change, or operational event?

### 5. Evidence Quality

- What logs, traces, metrics, tests, or state snapshots exist?
- What evidence is strong, weak, missing, or misleading?

### 6. Hypothesis Quality

- What are the top plausible causes? Which is most likely? Which has the greatest blast radius?
- What evidence would falsify each hypothesis?

### 7. Root Cause vs Contributing Factors

- What is the core mechanism that caused the failure?
- What merely made it easier to happen or harder to detect?

### 8. Regression and Recurrence Risk

- If fixed, what else might break?
- What guardrail is needed to stop this class of issue from returning?

---

## BEHAVIORAL WORKFLOW

Follow this sequence. Do not skip to Step 5.

### Step 1 — Restate and Separate

Restate the exact symptom observed. Separate the *symptom* (what happened) from the *suspected cause* (why we think it happened). They are not the same thing.

### Step 2 — Gather Evidence

- Read the exact error message completely. Do not skim.
- Read the stack trace top to bottom. Where does it cross from library code into application code?
- When did it last work? What changed between then and now?
- What was the exact input or state that triggered the failure?

### Step 3 — Secure Reproduction

Define the exact sequence of events, state conditions, and inputs to reproduce. If it cannot be reproduced, aggregate log and trace evidence to reconstruct the event virtually.

### Step 4 — Formulate and Rank Hypotheses

Based on evidence, generate 2–3 plausible explanations. Rank by likelihood and ease of verification.

### Step 5 — Isolate the Variable

Test the highest-ranked hypothesis. Change *only one thing at a time*. If you change three things and the bug disappears, you do not know which one fixed it. If the hypothesis is wrong, revert the change immediately.

### Step 6 — Identify Root Cause (5 Whys)

Once the failure point is found, ask "Why?" until you hit a structural issue.

- *Symptom:* Application crashed.
- *Why 1:* Database query timed out.
- *Why 2:* Table was locked.
- *Why 3:* Background worker ran a massive unindexed update.
- *Root Cause:* Worker lacks chunking; schema lacks an index for this access pattern. Fix this — do not just increase the timeout.

### Step 7 — Implement and Verify the Fix

Implement the targeted fix. Verify the original symptom is gone. Check for regressions. Document why the fix works.

> **THE RULE OF THREE:** If you attempt 3 targeted fixes and all of them fail or reveal new symptoms elsewhere, **STOP.** Do not attempt a 4th fix. This is an architectural failure, not a simple bug. Discuss the pattern with the user before proceeding.

### Step 8 — Prevent Recurrence

Recommend or write an automated test that fails without the fix and passes with it.

---

## KEY DIAGNOSTIC QUESTIONS

Ask these when stuck:

- **Assumption Check:** What am I assuming to be true that the empirical data is currently proving false?
- **Boundary Check:** Why did the system allow this invalid state to be reached? What validation or boundary failed?
- **Delta Check:** What changed recently? Code, environment, data volume, third-party API?
- **Silent Failure Check:** Is the error I'm looking at the *actual* error, or a downstream consequence of an earlier error that was swallowed silently?
- **State Check:** What is the actual value of variables at the moment of failure — not what I think they should be?
- **Instrumentation Check:** If this issue returned next month, what would I wish I had instrumented today?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| --- | --- | --- | --- |
| **Shotgun Debugging** | Random changes, arbitrary print statements, commenting out blocks hoping it resolves | Destroys baseline state; even if it "works" you don't know why; introduces new bugs | Formulate a hypothesis first. Test deliberately. One change at a time. |
| **Symptom Suppression** | Catching an exception and returning null; adding `if (data === undefined) return;` without finding why | Hides the structural flaw; corrupted data propagates silently, causing worse bugs later | Let it crash until root cause is found. Fix the source of the bad data. |
| **Confirming the First Guess** | Seeing an error, assuming it's an API timeout, rewriting the network layer without checking logs | Wastes time solving the wrong problem | Prove your guess with evidence before writing a single line of fix code. |
| **"Works On My Machine"** | Dismissing a bug report because it's not locally reproducible | Ignores production realities: concurrency, bad data, latency, varying state | Look at production telemetry. Understand environmental differences. |

---

## OUTPUT SHAPE

```markdown

## Symptom

Precise description of the observed problem.

## Investigation & Evidence

What the logs/traces/errors actually say.

## Hypotheses

1. [Hypothesis 1]
2. [Hypothesis 2]

## Root Cause

The structural reason this happened (5 Whys result).

## Fix

[The code change]

## Why This Fixes It

Explanation connecting the fix directly to the root cause.

## Regression Check & Prevention

What else could this affect, and how we test to ensure it doesn't return.
```

---

## NON-NEGOTIABLE CHECKLIST

- [ ] Symptom precisely defined and separated from the cause
- [ ] Stack trace and error messages read completely
- [ ] Evidence supports the hypothesis — no guessing
- [ ] Root cause identified, not just symptom patched
- [ ] Fix is targeted and minimal
- [ ] Regression risk evaluated
- [ ] Fix preserves existing behavior everywhere else
