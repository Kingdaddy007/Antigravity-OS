---
description: The systematic pre-deployment and deployment sequence for shipping code to production safely — from release scope definition through staged rollout to post-deployment monitoring and stabilization.
---

# WORKFLOW: SHIP TO PRODUCTION (MASTER UI)

> **[CONTEXT AMNESIA FAILSAFE]**
> YOU MUST USE TOOL CALLS TO READ THE FULL SOURCE FILE IN `global/workflows/` AND THE REQUIRED SKILLS/CONTEXTS BEFORE EXECUTING THIS.
> PROVE YOU HAVE DONE THIS IN A `<thought_process>` BLOCK.
>


> **IMPORTANT [REQUIRED]:** This is the UI Trigger. For the full 18,000-character logic, deployment checklists, and staged rollout protocols, the Agent MUST load and follow the [SOURCE FILE](global/workflows/workflow-ship-to-production.md).

## WHAT THIS WORKFLOW DOES

Acts as the final safety gate between staging and production. It ensures code reaching users has been verified, the deployment process is followed, and post-deployment monitoring catches issues before users do.

---

## REQUIRED ACTIVATION (AGENT MUST LOAD)

### 1. Load Full Instructions

- [ ] **Load Source [REQUIRED]:** [workflow-ship-to-production.md](global/workflows/workflow-ship-to-production.md) (Follow all 9 steps).

### 2. Load Core Contexts & Skills (Always)

- **Core:** `anti-gravity-core.md`, `system-thinking.md`, `execution-workflow.md`, `operating-modes.md`.
- **Skills:** `skill-devops-infra`, `skill-review-audit`.
- **Contexts:** `infra-context.md`, `stack-context.md`, `testing-standards.md`.

### 3. Load Conditional Assets

| Condition | Skill/Context to Load |
| :--- | :--- |
| Performance risk | `skill-performance` |
| Security-sensitive | `skill-security`, `security-baselines.md` |
| Database migrations | `skill-database`, `database-context.md` |

---

## DEPLOYMENT PROTOCOL (HIGH-LEVEL)

| Phase | Goal | Gate |
| :--- | :--- | :--- |
| **P1. Scope** | Define Record | IDENTIFY exactly what is shipping and its risk level |
| **P2. Verify** | Staging Check | CONFIRM CI/CD, staging soak, and readiness evidence |
| **P3. Strategy** | Rollout Plan | SELECT rollout style (Direct, Canary, Feature Flag) |
| **P4. Rollback** | Safety Net | DEFINE how to reverse if production degrades |
| **P5. Deploy** | Execution | TRIGGER following `infra-context.md` procedures |
| **P6. Observe** | Monitoring | STABILIZE for 60 minutes before declaring success |

---

## PERFORMANCE & QUALITY GATES

- **G1 (Scope):** Stop if release candidate is fuzzy or untested.
- **G2 (Evidence):** Verify staging evidence matches production build.
- **G3 (Rollback):** Do not deploy if rollback path is untested/blocked.
- **G4 (Monitor):** Rollback immediately if smoke tests fail post-deploy.

> **Final Instruction:** Every deploy is a bet. Make it informed. Read the Source file now.


