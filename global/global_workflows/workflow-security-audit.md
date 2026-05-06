---
description: The systematic sequence for evaluating the security posture of code, features, or system components — identifying vulnerabilities, assessing risk, and recommending mitigations using the STRIDE framework.
---

# WORKFLOW: SECURITY AUDIT (MASTER UI)

> **[CONTEXT AMNESIA FAILSAFE]**
> YOU MUST USE TOOL CALLS TO READ THE FULL SOURCE FILE AND THE REQUIRED SKILLS/CONTEXTS BEFORE EXECUTING THIS.
> Verify silently in your internal reasoning that you have done this.

> **IMPORTANT [REQUIRED]:** This is the UI Trigger. For the full 18,000-character logic, STRIDE framework analysis, and trust boundary mapping protocols, the Agent MUST load and follow the [SOURCE FILE](file:///C:/Users/Oviks/.gemini/antigravity/workflows/workflow-security-audit.md).

## WHAT THIS WORKFLOW DOES

Applies structured threat analysis (STRIDE) to code and architecture. It forces agents to map trust boundaries and identify how attackers could spoof, tamper, or escalate privileges, ensuring security review is evidence-based.

---

## REQUIRED ACTIVATION (AGENT MUST LOAD)

### 1. Load Full Instructions

- [ ] **Load Source [REQUIRED]:** [workflow-security-audit.md](file:///C:/Users/Oviks/.gemini/antigravity/workflows/workflow-security-audit.md) (Follow all 6 steps).

### 2. Load Core Contexts & Skills (Always)

- **Core:** `anti-gravity-core.md`, `system-thinking.md`, `execution-workflow.md`, `operating-modes.md`.
- **Skills:** `skill-security`, `skill-review-audit`.
- **Contexts:** `security-baselines.md`, `architecture-context.md`, `stack-context.md`, `domain-rules.md`.

### 3. Load Conditional Assets

| Condition | Skill/Context to Load |
| :--- | :--- |
| API/Endpoint review | `skill-api-design`, `api-conventions.md` |
| Database/Data layer | `skill-database`, `database-context.md` |
| Infra/Networking | `skill-devops-infra`, `infra-context.md` |

---

## AUDIT PROTOCOL (HIGH-LEVEL)

| Phase | Goal | Gate |
| :--- | :--- | :--- |
| **P1. Scope** | Identify Assets | Define WHAT is being protected and from WHOM |
| **P2. Boundaries** | Map Trust | Draw zones where data crosses security limits |
| **P3. STRIDE** | Threat Model | Apply S-T-R-I-D-E analysis to every boundary |
| **P4. Baselines** | Compliance | Check against `security-baselines.md` standards |
| **P5. Classify** | Prioritize | Assign 🔴Critical to 🟢Low severity to findings |
| **P6. Deliver** | Report | Provide prioritized remediation and approval status |

---

## SECURITY QUALITY GATES

- **G1 (Scope):** Stop if the trust boundary is vague.
- **G2 (Authz):** Verify server-side enforcement, not just UI visibility.
- **G3 (Misuse):** Audit must include abuse scenarios, not just happy-path use.
- **G4 (Status):** Report must explicitly state blocking vs. advisory findings.

> **Final Instruction:** The Gold v1.1 security audit process requires deep analysis defined in the Source file. Read it now.
