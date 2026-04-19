---
description: The systematic sequence for taking a raw idea and turning it into a structured, sequenced, executable project plan — the bridge between "I have an idea" and "let's start building."
---

# WORKFLOW: PROJECT INCEPTION (MASTER)

> **[CONTEXT AMNESIA FAILSAFE]**
> YOU MUST USE TOOL CALLS TO READ THE FULL SOURCE FILE AND THE REQUIRED SKILLS/CONTEXTS BEFORE EXECUTING THIS.
> Verify silently in your internal reasoning that you have done this.


> **IMPORTANT [REQUIRED]:** This is the UI Trigger. For the full detailed logic, instructions, and implementation phases, the Agent MUST load and follow the [SOURCE FILE]({{GLOBAL_CONFIG_URI}}/workflows/workflow-project-inception.md).

## WHAT THIS WORKFLOW DOES

This workflow transforms a raw idea into a buildable plan. It acts as the "product manager" ensuring the "why" and "what" are locked before the "how" begins.

---

## REQUIRED ACTIVATION (AGENT MUST LOAD)

### 1. Load Full Instructions

- [ ] **Load Source [REQUIRED]:** [workflow-project-inception.md]({{GLOBAL_CONFIG_URI}}/workflows/workflow-project-inception.md) (Follow all 6 phases).

### 2. Load Core Contexts & Skills (Always)

- **Core:** `anti-gravity-core.md`, `system-thinking.md`, `execution-workflow.md`.
- **Skills:** `skill-product-thinking`, `skill-architecture`.
- **Contexts:** No existing context needed (it creates them).

### 3. Load Conditional Assets

| Condition | Skill/Context to Load |
| :--- | :--- |
| UI/Frontend | `skill-ui-ux`, `visual-brainstorming` |
| Database/Data | `skill-database` |
| API/Integration | `skill-api-design` |

---

## EXECUTION SUMMARY (HIGH-LEVEL)

| Phase | Goal | Gate |
| :--- | :--- | :--- |
| **P1. Problem** | Define Why | User confirms problem statement |
| **P2. Scope** | Define What | Lock Core vs Nice-to-Have |
| **P3. Design** | Define Structure | Stack, Data Model, Riskiest Decision |
| **P4. Sequence** | Define Order | Numbered Build Plan |
| **P5. Summary** | Finalize Brief | Create Project Brief Document |
| **P6. Launch** | Begin Build | Hand off to Build Workflow |

---

## QUALITY GATES

- **G1 (Problem):** Do NOT skip Phase 1. Understanding the problem is the foundation.
- **G2 (MVP):** Use the "20% question" to keep MVP focused only on core value.
- **G3 (Safety):** Identify the riskiest building block and validate it first.
- **G4 (Logic):** Sequence builds foundation before features (Infrastructure -> Data -> Auth -> Feature 1).

> **Final Instruction:** The detailed steps for problem extraction, feature categorization, and architecture design are in the Source file. Read it now.
