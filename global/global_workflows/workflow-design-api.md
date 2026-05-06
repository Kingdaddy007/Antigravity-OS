---
description: The systematic sequence for designing API endpoints and contracts — from understanding the consumer's needs through contract definition to implementation with proper error handling, security, and documentation.
---

# WORKFLOW: DESIGN API (MASTER UI)

> **[CONTEXT AMNESIA FAILSAFE]**
> YOU MUST USE TOOL CALLS TO READ THE FULL SOURCE FILE AND THE REQUIRED SKILLS/CONTEXTS BEFORE EXECUTING THIS.
> Verify silently in your internal reasoning that you have done this.

> **IMPORTANT [REQUIRED]:** This is the UI Trigger. For the full 15,000-character logic, Error Taxonomy tables, and Server Action vs API Route decision matrices, the Agent MUST load and follow the [SOURCE FILE](file:///C:/Users/Oviks/.gemini/antigravity/workflows/workflow-design-api.md).

## WHAT THIS WORKFLOW DOES

Enforces a **Contract-First** discipline. It ensures APIs are designed for the consumer's job-to-be-done, not for server-side convenience. It prevents implementation leaks, provides explicit error mapping, and secures every endpoint before a single line of data-access code is written.

---

## REQUIRED ACTIVATION (AGENT MUST LOAD)

### 1. Load Full Instructions

- [ ] **Load Source [REQUIRED]:** [workflow-design-api.md](file:///C:/Users/Oviks/.gemini/antigravity/workflows/workflow-design-api.md) (Follow all 8 steps).

### 2. Load Core Contexts & Skills (Always)

- **Core:** `anti-gravity-core.md`, `system-thinking.md`, `execution-workflow.md`, `operating-modes.md`.
- **Skills:** `skill-api-design`, `skill-security`, `skill-architecture`.
- **Contexts:** `api-conventions.md`, `stack-context.md`, `security-baselines.md`, `coding-standards.md`, `architecture-context.md`, `domain-rules.md`.

### 3. Load Conditional Assets

| Condition | Skill/Context to Load |
| :--- | :--- |
| New Data/Queries | `skill-database`, `database-context.md` |
| New Boundaries | `skill-architecture` (deep) |
| Unclear Consumer | `skill-product-thinking` |
| Feature Context | `project-context.md`, `business-priorities.md` |

---

## API DESIGN PROTOCOL (HIGH-LEVEL)

| Phase | Goal | Gate |
| :--- | :--- | :--- |
| **P1. Consumer** | Task Audit | Identify WHO calls this & WHAT they need |
| **P2. Contract** | Shape Specs | **Contract-First:** Define Request, Response, Errors |
| **P3. Grounding** | Architecture Fit | Align with existing conventions & constraints |
| **P4. Pipeline** | Data Flow | Map **Auth -> Validate -> Authorize -> Execute** |
| **P5. Risk Audit** | Safety Pass | Check for data leaks & boundary violations |
| **P6. Implement** | Code Builders | Follow the Step 4 Pipeline exactly |
| **P7. Verify** | Compliance | Audit against Gold Contract standards |
| **P8. Deliver** | Summary Logic | Document endpoint, side effects, & auth |

---

## API QUALITY GATES

- **G1 (Contract-First):** Did you define the response shape before writing the route logic?
- **G2 (Auth Order):** Is authentication verified BEFORE any database operations?
- **G3 (Error Specificity):** Does the consumer get a specific code or a generic 500?
- **G4 (Implementation Leak):** Does the API shape expose private database IDs?

> **Final Instruction:** Every detail of the Gold v1.1 API design process is preserved in the Source file. Read it now.
