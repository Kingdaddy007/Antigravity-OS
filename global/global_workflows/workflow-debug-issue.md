---
description: The systematic sequence for diagnosing and fixing bugs — from symptom observation through root cause identification to verified fix with regression prevention.
---

# WORKFLOW: DEBUG ISSUE (MASTER UI)

> **[CONTEXT AMNESIA FAILSAFE]**
> YOU MUST USE TOOL CALLS TO READ THE FULL SOURCE FILE AND THE REQUIRED SKILLS/CONTEXTS BEFORE EXECUTING THIS.
> Verify silently in your internal reasoning that you have done this.


> **IMPORTANT [REQUIRED]:** This is the UI Trigger. For the full 12,000-character logic, evidence-gathering steps, and regression prevention strategies, the Agent MUST load and follow the [SOURCE FILE]({{GLOBAL_CONFIG_URI}}/workflows/workflow-debug-issue.md).

## WHAT THIS WORKFLOW DOES

Prevents "shotgun debugging" by enforcing evidence-based diagnosis. It ensures that the root cause is confirmed before a single line of fix code is written, followed by mandatory regression testing.

---

## REQUIRED ACTIVATION (AGENT MUST LOAD)

### 1. Load Full Instructions

- [ ] **Load Source [REQUIRED]:** [workflow-debug-issue.md]({{GLOBAL_CONFIG_URI}}/workflows/workflow-debug-issue.md) (Follow all 8 steps).

### 2. Load Core Contexts & Skills (Always)

- **Core:** `anti-gravity-core.md`, `system-thinking.md`, `execution-workflow.md`, `operating-modes.md`.
- **Skills:** `skill-debugging`, `skill-review-audit`, `skill-testing`.
- **Contexts:** `stack-context.md`, `architecture-context.md`, `domain-rules.md`.

### 3. Load Conditional Assets

| Condition | Skill/Context to Load |
| :--- | :--- |
| Security implications | `skill-security`, `security-baselines.md` |
| Performance issues | `skill-performance`, `infra-context.md` |
| Structural debt revealed | `skill-refactoring` |
| API/Contract mismatch | `api-conventions.md` |

---

## EXECUTION SUMMARY (HIGH-LEVEL)

| Phase | Goal | Gate |
| :--- | :--- | :--- |
| **S1. Symptom** | Define Error | Stop if symptom is vague |
| **S2. Evidence** | Gather Facts | Stop if no logs/traces found |
| **S3. Hypothesis** | Rank Causes | Generate at least 3 stories |
| **S4. Root Cause** | Isolate Truth | Confirm with evidence before fixing |
| **S5. Fix** | Target Cause | Must address mechanism, not symptom |
| **S6. Verify** | Prove Stability | Check regressions in adjacent flows |
| **S7. Defense** | Prevent Repeat | Add test/alert before closing |
| **S8. Post-Fix** | Lock In Learning | **MANDATORY:** Log to `memory/` — decisions, patterns, mistakes |

---

## QUALITY GATES

- **G1 (Evidence):** No code changes without supporting evidence.
- **G2 (Hypothesis):** Don't attach to the first story—consider alternatives.
- **G3 (Mechanism):** If the fix only suppresses the symptom, label it mitigation.
- **G4 (Recurrence):** Every bug fix must include a regression test and long-term guardrail.

> **Final Instruction:** Every detail of the Gold v1.1 debugging process is preserved in the Source file. Read it now.


