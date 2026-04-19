---
description: The systematic sequence for improving code structure without changing external behavior — from identifying what to improve through safe transformation to verified behavioral preservation.
---

# WORKFLOW: REFACTOR MODULE (MASTER UI)

> **[CONTEXT AMNESIA FAILSAFE]**
> YOU MUST USE TOOL CALLS TO READ THE FULL SOURCE FILE AND THE REQUIRED SKILLS/CONTEXTS BEFORE EXECUTING THIS.
> Verify silently in your internal reasoning that you have done this.


> **IMPORTANT [REQUIRED]:** This is the UI Trigger. For the full 15,000-character logic, characterization test protocols, and scope creep prevention rules, the Agent MUST load and follow the [SOURCE FILE]({{GLOBAL_CONFIG_URI}}/workflows/workflow-refactor-module.md).

## WHAT THIS WORKFLOW DOES

Ensures refactoring is safe, scoped, and valuable. It enforces the discipline of locking behavior with tests (Characterization Tests) BEFORE touching any code. It prevents "secret system rewrites" by keeping cleanup bounded to a specific module.

---

## REQUIRED ACTIVATION (AGENT MUST LOAD)

### 1. Load Full Instructions

- [ ] **Load Source [REQUIRED]:** [workflow-refactor-module.md]({{GLOBAL_CONFIG_URI}}/workflows/workflow-refactor-module.md) (Follow all 6 steps).

### 2. Load Core Contexts & Skills (Always)

- **Core:** `anti-gravity-core.md`, `system-thinking.md`, `execution-workflow.md`, `operating-modes.md`.
- **Skills:** `skill-refactoring`, `skill-coding`, `skill-testing`.
- **Contexts:** `coding-standards.md`, `stack-context.md`, `architecture-context.md`, `domain-rules.md`.

### 3. Load Conditional Assets

| Condition | Skill/Context to Load |
| :--- | :--- |
| Boundary Changes | `skill-architecture` |
| Underlying Bugs | `skill-debugging` |
| Significant Tests | `testing-standards.md` |
| Data Layer Refactor | `database-context.md` |

---

## REFACTORING PROTOCOL (HIGH-LEVEL)

| Phase | Goal | Gate |
| :--- | :--- | :--- |
| **P1. Assess** | Identify Problems | Define Module Boundary (In/Out of Scope) |
| **P2. Lock** | Characterization | **Non-Negotiable:** Pass tests BEFORE changes |
| **P3. Plan** | Strategy | Select strategy (Extract, Rename, Move, etc.) |
| **P4. Execute** | Iterative Change | **Rule:** Run tests after EVERY single change |
| **P5. Verify** | Audit Success | Confirm behavior preservation & structural gains |
| **P6. Deliver** | Summary Logic | Document What Changed vs Behavior Preserved |

---

## REFACTORING QUALITY GATES

- **G1 (Characterization):** Stop if current behavior is documented only by "trusting the code."
- **G2 (Golden Rule):** Tests must run after 100% of individual transformations.
- **G3 (Creep Check):** Is this a refactor or a disguised rewrite?
- **G4 (Leverage):** Does this change make the NEXT feature cheaper to build?

> **Final Instruction:** Every detail of the Gold v1.1 refactoring process is preserved in the Source file. Read it now.


