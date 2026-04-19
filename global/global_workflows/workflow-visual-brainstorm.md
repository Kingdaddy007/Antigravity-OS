---
description: The systematic sequence for generating visual design previews and Google Stitch design briefs during brainstorming — making design direction visible before implementation begins.
---

# WORKFLOW: VISUAL BRAINSTORMING (MASTER)

> **[CONTEXT AMNESIA FAILSAFE]**
> YOU MUST USE TOOL CALLS TO READ THE FULL SOURCE FILE AND THE REQUIRED SKILLS/CONTEXTS BEFORE EXECUTING THIS.
> Verify silently in your internal reasoning that you have done this.


> **IMPORTANT [REQUIRED]:** This is the Trigger. For the full detailed logic, dual-path execution (HTML Preview vs Google Stitch Brief), and design token export process, the Agent MUST load and follow the [SOURCE FILE]({{GLOBAL_CONFIG_URI}}/workflows/workflow-visual-brainstorm.md).

## WHAT THIS WORKFLOW DOES

Produces visual artifacts (live HTML previews or Google Stitch design briefs) that let the user SEE design decisions before committing to implementation. Prevents the most expensive UI mistake: building something that looks different from what the user imagined.

---

## REQUIRED ACTIVATION (AGENT MUST LOAD)

### 1. Load Full Instructions

- [ ] **Load Source [REQUIRED]:** [workflow-visual-brainstorm.md]({{GLOBAL_CONFIG_URI}}/workflows/workflow-visual-brainstorm.md) (Follow all 5 phases).

### 2. Load Core Contexts & Skills (Always)

- **Core:** `anti-gravity-core.md`, `system-thinking.md`.
- **Skills:** `visual-brainstorming`, `skill-ui-ux`.
- **Contexts:** `visual-identity.md` (if exists), `design-system.md` (if exists).

### 3. Load Conditional Assets

| Condition | Skill/Context to Load |
| :--- | :--- |
| During project inception | `skill-product-thinking`, `skill-architecture` |
| Complex UI / dashboards | `skill-coding` (for HTML preview generation) |
| Existing project with stack | `stack-context.md` |

---

## EXECUTION PROTOCOL (HIGH-LEVEL)

| Phase | Goal | Gate |
| :--- | :--- | :--- |
| **P1. Understand** | Clarify what needs visualization | Clear question before any preview |
| **P2. Choose Path** | Select HTML Preview or Stitch Brief | Path explicitly chosen |
| **P3A. HTML Preview** | Generate & iterate on live preview | User approves visual direction |
| **P3B. Stitch Brief** | Prepare detailed brief for Google Stitch | User completes Stitch session |
| **P4. Lock Direction** | Export design tokens to context files | Tokens written to visual-identity.md |
| **P5. Hand Off** | Transition to build workflow | Next workflow identified |

---

## DUAL-PATH DECISION

| Need | Path A: HTML Preview | Path B: Google Stitch |
| :--- | :--- | :--- |
| Color palette comparison | ✅ Best | Overkill |
| Typography preview | ✅ Best | Overkill |
| Full page layout mockup | ⚠️ Basic wireframe | ✅ Best |
| Production-quality mockup | ❌ Not the tool | ✅ Best |
| Fast decision (< 5 min) | ✅ Best | ❌ Too slow |

---

## QUALITY GATES

- **G1 (Clarity):** No preview without a clear question to answer.
- **G2 (Path):** Path A or B explicitly chosen — never assumed.
- **G3 (Approval):** User approves visual direction before tokens are exported.
- **G4 (Export):** Design tokens MUST be written to `contexts/visual-identity.md`.

> **Final Instruction:** The full dual-path execution logic, HTML preview templates, Stitch brief structure, and design token export process are in the Source file. Read it now.
