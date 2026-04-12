---
description: The systematic sequence for reviewing code — evaluating correctness, security, maintainability, and quality against project standards.
---

# WORKFLOW: REVIEW CODE (MASTER UI)

> **[CONTEXT AMNESIA FAILSAFE]**
> YOU MUST USE TOOL CALLS TO READ THE FULL SOURCE FILE IN `global/workflows/` AND THE REQUIRED SKILLS/CONTEXTS BEFORE EXECUTING THIS.
> PROVE YOU HAVE DONE THIS IN A `<thought_process>` BLOCK.
>


> **IMPORTANT [REQUIRED]:** This is the UI Trigger. For the full technical review methodology, security checklists, and maintainability criteria, the Agent MUST load and follow the [SOURCE FILE](global/workflows/workflow-review-code.md).

## WHAT THIS WORKFLOW DOES

Ensures code reviews are structured, objective, and focus on high-impact risks like logic failure and security vulnerabilities. It transforms "gut feel" reviews into evidence-based quality audits.

---

## REQUIRED ACTIVATION (AGENT MUST LOAD)

### 1. Load Full Instructions

- [ ] **Load Source [REQUIRED]:** [workflow-review-code.md](global/workflows/workflow-review-code.md) (Follow all 8 steps).

### 2. Load Core Contexts & Skills (Always)

- **Core:** `anti-gravity-core.md`, `system-thinking.md`, `execution-workflow.md`, `operating-modes.md`.
- **Skills:** `skill-review-audit`, `skill-security`.
- **Contexts:** `coding-standards.md`, `stack-context.md`, `architecture-context.md`, `domain-rules.md`.

### 3. Load Conditional Assets

| Condition | Skill/Context to Load |
| :--- | :--- |
| Data/API logic | `skill-performance`, `api-conventions.md` |
| Structural/Module changes | `skill-architecture`, `database-context.md` |
| Test coverage being reviewed | `skill-testing`, `testing-standards.md` |
| High debt areas | `skill-refactoring` |

---

## REVIEW PROTOCOL (HIGH-LEVEL)

| Phase | Goal | Gate |
| :--- | :--- | :--- |
| **P1. Intent** | Understand Why | Stop if intent is ambiguous |
| **P2. CI Gates** | Verify Baseline | Stop if tests/lint fail |
| **P3. Correctness** | Verify Logic | Priority #1 over style |
| **P4. Security** | Verify Safety | Never skipped for any PR |
| **P5. Maintenance** | Verify Future | Check readability/conventions |
| **P6. Architecture** | Verify Fit | Check module boundaries |
| **P7. Findings** | Classify Risk | Use Severity Model (🔴🟠🟡🟢) |
| **P8. Delivery** | Direct Feedback | Clear approval/block status |

---

## QUALITY GATES

- **G1 (Intent):** Do not judge implementation before understanding intent.
- **G2 (Automation):** Humans should not review what machines can catch.
- **G3 (Severity):** Calibrate findings to actual risk, not preference.
- **G4 (Clarity):** Always state specific conditions for approval.

> **Final Instruction:** Every detail of the Gold v1.1 review process is preserved in the Source file. Read it now.


