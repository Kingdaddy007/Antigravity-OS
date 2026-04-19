---
description: The systematic sequence for designing and implementing user interfaces — from user goal identification through component implementation with full state coverage and accessibility.
---

# WORKFLOW: DESIGN UI (MASTER UI)

> **[CONTEXT AMNESIA FAILSAFE]**
> YOU MUST USE TOOL CALLS TO READ THE FULL SOURCE FILE AND THE REQUIRED SKILLS/CONTEXTS BEFORE EXECUTING THIS.
> Verify silently in your internal reasoning that you have done this.


> **IMPORTANT [REQUIRED]:** This is the UI Trigger. For the full 15,000-character logic, state maps, and accessibility non-negotiables, the Agent MUST load and follow the [SOURCE FILE]({{GLOBAL_CONFIG_URI}}/workflows/workflow-design-ui.md).

## WHAT THIS WORKFLOW DOES

Ensures UI work starts with the user goal, not the components. It forces full state coverage (loading, error, empty) and accessibility compliance, preventing "demo-only" code that breaks in production.

---

## REQUIRED ACTIVATION (AGENT MUST LOAD)

### 1. Load Full Instructions

- [ ] **Load Source [REQUIRED]:** [workflow-design-ui.md]({{GLOBAL_CONFIG_URI}}/workflows/workflow-design-ui.md) (Follow all 8 steps).

### 2. Load Core Contexts & Skills (Always)

- **Core:** `anti-gravity-core.md`, `system-thinking.md`, `execution-workflow.md`, `operating-modes.md`.
- **Skills:** `skill-ui-ux`, `skill-coding`, `skill-product-thinking`.
- **Contexts:** `design-system.md`, `stack-context.md`, `coding-standards.md`, `architecture-context.md`, `domain-rules.md`.

### 3. Load Conditional Assets

| Condition | Skill/Context to Load |
| :--- | :--- |
| New pages/routes | `skill-architecture`, `project-context.md` |
| Data-heavy/Auth | `skill-api-design`, `security-baselines.md` |
| Performance critical | `skill-performance`, `infra-context.md` |

---

## DESIGN PROTOCOL (HIGH-LEVEL)

| Phase | Goal | Gate |
| :--- | :--- | :--- |
| **P1. Goal** | Define Job | Stop if Job-to-be-Done is unclear |
| **P2. States** | Map Coverage | Map all 13 possible states first |
| **P3. Priority** | Hierarchy | Define primary vs. secondary actions |
| **P4. Layout** | Visual Plan | Select Design System components |
| **P5. Build** | Implement | Happy path + Error/Empty states |
| **P6. Verify** | QA States | Check responsive & keyboard nav |
| **P7. Critique** | UX Integrity | Challenge visual vs. functional quality |
| **P8. Deliver** | Full Specs | Include test steps for all states |

---

## QUALITY GATES

- **G1 (Goal):** No design without a Job-to-be-Done statement.
- **G2 (States):** Coding starts ONLY after the state map is complete.
- **G3 (A11y):** Accessibility is non-negotiable (Keyboard, Contrast, ARIA).
- **G4 (System):** Do not invent new patterns where the Design System serves the need.

> **Final Instruction:** Every detail of the Gold v1.1 design process is preserved in the Source file. Read it now.


