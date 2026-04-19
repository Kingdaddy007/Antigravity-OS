---
description: The systematic sequence for making architectural decisions — from understanding requirements through evaluating options to documenting the decision with tradeoffs and implementation guidance.
---

# WORKFLOW: PLAN ARCHITECTURE (MASTER UI)

> **[CONTEXT AMNESIA FAILSAFE]**
> YOU MUST USE TOOL CALLS TO READ THE FULL SOURCE FILE AND THE REQUIRED SKILLS/CONTEXTS BEFORE EXECUTING THIS.
> Verify silently in your internal reasoning that you have done this.


> **IMPORTANT [REQUIRED]:** This is the UI Trigger. For the full 15,000-character logic, Evaluation Matrix protocols, and ADR (Architecture Decision Record) structure, the Agent MUST load and follow the [SOURCE FILE]({{GLOBAL_CONFIG_URI}}/workflows/workflow-plan-architecture.md).

## WHAT THIS WORKFLOW DOES

Ensures architectural decisions are made deliberately, not by default. It forces agents to evaluate at least 3 options (including the "boring" one), apply the "2 AM Test," and document tradeoffs before committing to a structural shape.

---

## REQUIRED ACTIVATION (AGENT MUST LOAD)

### 1. Load Full Instructions

- [ ] **Load Source [REQUIRED]:** [workflow-plan-architecture.md]({{GLOBAL_CONFIG_URI}}/workflows/workflow-plan-architecture.md) (Follow all 7 steps).

### 2. Load Core Contexts & Skills (Always)

- **Core:** `anti-gravity-core.md`, `system-thinking.md`, `execution-workflow.md`, `operating-modes.md`.
- **Skills:** `skill-architecture`, `skill-product-thinking`, `skill-research-analysis`.
- **Contexts:** `project-context.md`, `architecture-context.md`, `business-priorities.md`, `stack-context.md`, `domain-rules.md`.

### 3. Load Conditional Assets

| Condition | Skill/Context to Load |
| :--- | :--- |
| Data Layer decisions | `skill-database`, `database-context.md` |
| API/Service boundaries | `skill-api-design`, `api-conventions.md` |
| Security-sensitive | `skill-security`, `security-baselines.md` |
| Infra/Deployment | `skill-devops-infra`, `infra-context.md` |

---

## ARCHITECTURE PROTOCOL (HIGH-LEVEL)

| Phase | Goal | Gate |
| :--- | :--- | :--- |
| **P1. Requirements** | Quantify Needs | Define "Success" before "Shape" |
| **P2. Tensions** | Expose Pain | Identify major tradeoffs (Speed vs Scale) |
| **P3. Options** | Generate 3+ | **Crucial:** Always include the "Boring" option |
| **P4. Evaluate** | Matrix Comparison | Run the 2 AM Test & Pre-Mortem |
| **P5. Boundaries** | Define Shape | Set explicit responsibility limits |
| **P6. Document** | ADR Logic | Formally record Decision & Assumptions |
| **P7. Path** | Implementation | Define phases and migration sequence |

---

## ARCHITECTURAL QUALITY GATES

- **G1 (Options):** Stop if only one approach is considered.
- **G2 (2 AM Test):** Can a mid-level engineer fix it under pressure?
- **G3 (Reversibility):** Identify if this is a Type 1 (Hard to undo) decision.
- **G4 (Boundaries):** Architecture is not aspiration; boundaries must be explicit.

> **Final Instruction:** Every detail of the Gold v1.1 architectural process is preserved in the Source file. Read it now.


