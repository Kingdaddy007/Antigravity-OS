---
description: The complete step-by-step sequence for transforming feature requests into production-quality code. Ensures problem definition, architectural alignment, and rigorous verification before delivery.
---

# WORKFLOW: BUILD FEATURE (MASTER)

> **[CONTEXT AMNESIA FAILSAFE]**
> YOU MUST USE TOOL CALLS TO READ THE FULL SOURCE FILE AND THE REQUIRED SKILLS/CONTEXTS BEFORE EXECUTING THIS.
> Verify silently in your internal reasoning that you have done this.

> **IMPORTANT [REQUIRED]:** This is the UI Trigger. For the full 21,000-character logic, instructions, and implementation stages, the Agent MUST load and follow the [SOURCE FILE](file:///C:/Users/Oviks/.gemini/antigravity/workflows/workflow-build-feature.md).

## WHAT THIS WORKFLOW DOES

Chains Architect, Developer, and Reviewer modes to prevent coding before understanding. It ensures a rigorous sequence from Problem Definition to Shipped Code.

---

## REQUIRED ACTIVATION (AGENT MUST LOAD)

### 1. Load Full Instructions

- [ ] **Load Source [REQUIRED]:** [workflow-build-feature.md](file:///C:/Users/Oviks/.gemini/antigravity/workflows/workflow-build-feature.md) (Follow all 11 steps).

### 2. Load Core Contexts & Skills (Always)

- **Core:** `anti-gravity-core.md`, `system-thinking.md`, `execution-workflow.md`.
- **Skills:** `skill-coding`, `skill-architecture`, `skill-testing`.
- **Contexts:** `stack-context.md`, `coding-standards.md`, `architecture-context.md`, `domain-rules.md`, `project-context.md`.

### 3. Load Conditional Assets

| Condition | Skill/Context to Load |
| :--- | :--- |
| UI/Frontend | `skill-ui-ux`, `design-system.md` |
| Security/Auth | `skill-security`, `security-baselines.md` |
| Database/Schema | `skill-database`, `database-context.md` |
| API/Endpoints | `skill-api-design`, `api-conventions.md` |

---

## EXECUTION SUMMARY (HIGH-LEVEL)

| Phase | Goal | Gate |
| :--- | :--- | :--- |
| **P1. Objective** | Define Why | Stop if objective is vague |
| **P2. Grounding** | Define Where | Stop if placement is unclear |
| **P3. Scope** | Define What | Lock [In/Out] Scope immediately |
| **P4. Risks** | Define Safety | Identify high-risk assumptions |
| **P5. Design** | Define How | Detail data/API/components |
| **P6. Verification** | Define Proof | Set test targets before coding |
| **P7. Implementation** | Execute Detail | **SEE SOURCE FILE STAGES 7a-7d** |
| **P8. Memory Capture** | Lock In Learning | Log decisions, patterns, mistakes to `memory/` |

---

## QUALITY GATES

- **G1 (Ambiguity):** Do not proceed without a clear objective.
- **G2 (Scope):** If work grows, split it into phases—do not expand silently.
- **G3 (Mismatch):** Resolve architectural placement before implementation.
- **G4 (Safety):** Ensure all failure paths are tested, not just the happy path.

> **Final Instruction:** Every detail from your original 20k word workflow is preserved in the Source file. Read it now.
