# RUBRIC: PROJECT PLANNING QUALITY

**Version:** Gold v1.0
**Layer:** 10 — Evaluation
**Tier:** 3 — Loaded on demand
**File:** rubrics/project-planning-rubric.md
**Purpose:** Self-assessment matrix for evaluating whether a project
          inception / planning process was thorough enough to start
          building with confidence.
**Loaded When:** After completing workflow-project-inception.md.
              Before transitioning from planning to building.
              Evaluating whether planning is "done enough" to start.
**References:** workflow-project-inception.md, templates/project-brief.md,
             skill-product-thinking.md

---

## HOW TO USE THIS RUBRIC

After completing the Project Inception workflow and filling in the
Project Brief template, evaluate the planning quality against each
dimension below. The question this rubric answers is:

**"Have we planned enough to start building with confidence, or are
we about to code our way into confusion?"**

---

## EVALUATION MATRIX

### 1. PROBLEM CLARITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Problem stated in plain language. Target user specific and identifiable. Job-to-be-Done clearly framed. Evidence exists that this problem is real (personal experience, user research, market data). Current workaround identified and its inadequacy explained. |
| **Acceptable** | Problem is clear and understandable. Target user identified. JTBD makes sense. Based on reasonable assumption even if not validated with data. |
| **Needs Work** | Problem is vague or overly broad. Target user is "everyone." JTBD is unclear. Building based on assumption without questioning it. |
| **Failing** | No problem defined. Building a solution looking for a problem. "I want to build an app that does X" without explaining who needs X or why. |

### 2. SCOPE DISCIPLINE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Features categorized into Core / Important / Nice-to-Have / Out of Scope. MVP contains ONLY features essential to solving the core problem. "Out of Scope" is populated and specific. The "20% question" was applied. Scope can be built within the available timeline. |
| **Acceptable** | Core features identified. MVP scope is reasonable. Some Phase 2 items listed. Scope is buildable within timeline with some buffer. |
| **Needs Work** | MVP scope is too large. Too many "must have" features. No clear Phase 2 separation. Tight timeline with no buffer. |
| **Failing** | No scope boundaries. Everything is "must have." The plan is to "build everything." Timeline is impossible given scope. Recipe for 80% built, never shipped. |

### 3. DEFINITION OF DONE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Specific, checkable criteria for "shipped." Each criterion is binary (done or not done). Includes both functional criteria (features work) and quality criteria (no broken flows, basic security). Includes deployment target. For competitions: includes submission requirements. |
| **Acceptable** | Definition of done exists and is mostly specific. Core features have clear completion criteria. Deployment target identified. |
| **Needs Work** | Definition is vague ("app works") or incomplete. Missing quality criteria. No deployment target specified. |
| **Failing** | No definition of done. "I'll know it when I see it." No clear endpoint. Project will drift indefinitely. |

### 4. TECHNICAL FEASIBILITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Tech stack chosen with clear rationale. Data model designed and makes sense for the access patterns. Riskiest technical decision identified. Stack matches the builder's skills (or learning plan exists). No technology chosen for resume value over problem fit. |
| **Acceptable** | Tech stack chosen and reasonable. Data model exists. Builder is comfortable with the stack. |
| **Needs Work** | Tech stack chosen without evaluating alternatives. Data model not fully thought through. Some unfamiliar technology without a learning plan. |
| **Failing** | No technical decisions made. Or: technology chosen that the builder cannot use. Or: architecture massively over-engineered for the problem (microservices for a hackathon). |

### 5. BUILD SEQUENCE LOGIC

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Steps are ordered logically (foundation → data → auth → features → integration → deploy). Each step has a verification checkpoint. Dependencies between steps are identified. Steps are sized appropriately for the timeline. "Deploy early" principle followed. |
| **Acceptable** | Reasonable build order. Major steps identified. Some verification points. |
| **Needs Work** | Build order is vague or has logical gaps. No verification checkpoints. Steps are too large (no intermediate milestones). |
| **Failing** | No build sequence. Or: plan starts with UI polish before backend exists. Or: deployment is "the last step on the last day." |

### 6. TIMELINE REALISM

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Time mapped to build steps. Buffer exists for unexpected issues (~20% of total time). Scope pressure plan defined (what to cut if behind). Deploy early rule in place. For hackathons: last day reserved for polish + deploy + submit, NOT new features. |
| **Acceptable** | Timeline exists and is roughly realistic. Some buffer. General awareness of what to cut if needed. |
| **Needs Work** | Timeline is optimistic. No buffer. Every minute is planned with no slack. No plan for falling behind. |
| **Failing** | No timeline. Or: timeline is impossible (3 days for 3 months of work). Or: "I'll work 20 hours a day" as the plan. |

### 7. RISK AWARENESS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Top 3 risks identified with mitigation plans. Riskiest assumption named with a validation approach. Scope pressure plan exists (what to cut, what to keep). Worst-case scenario has a response plan. Known unknowns acknowledged. |
| **Acceptable** | Major risks identified. Some mitigation thinking. General awareness of what could go wrong. |
| **Needs Work** | Risks mentioned but not analyzed. No mitigation plans. Optimistic assumption that everything will go smoothly. |
| **Failing** | No risk assessment. "It'll be fine." No contingency planning. First unexpected problem will cause panic. |

### 8. COMMUNICATION QUALITY (Rubric)

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Project brief is complete, clear, and usable as a reference throughout the build. Someone who wasn't part of planning could read it and understand the project. No jargon in the problem definition. Build sequence is actionable. |
| **Acceptable** | Brief covers the essentials. Generally clear. Usable as a reference with some gaps. |
| **Needs Work** | Brief is incomplete or disorganized. Key sections missing. Would need verbal explanation to be useful. |
| **Failing** | No brief produced. Planning happened verbally with nothing written down. No reference document exists. |

---

## SCORING SUMMARY

| Dimension | Score | Notes |
| :--- | :--- | :--- |
| Problem Clarity |||
| Scope Discipline |||
| Definition of Done |||
| Technical Feasibility |||
| Build Sequence Logic |||
| Timeline Realism |||
| Risk Awareness |||
| Communication Quality |||
---

## READINESS DECISION

### ✅ READY TO BUILD — All Excellent or Acceptable

Planning is solid. Start executing the build sequence.

### ⚠️ MOSTLY READY — 1-2 Needs Work (non-critical)

Start building but address the gaps:

- If Scope Discipline is Needs Work → tighten scope before starting Feature 2
- If Timeline Realism is Needs Work → add buffer by cutting one feature to Phase 2
- If Risk Awareness is Needs Work → identify top risk before starting the riskiest step

### ❌ NOT READY — Any Failing, or 3+ Needs Work

Go back and strengthen the plan before writing any code:

- If Problem Clarity is Failing → STOP. Define the problem first. Building without understanding the problem wastes everything.
- If Scope Discipline is Failing → STOP. Reduce scope until it fits the timeline.
- If Definition of Done is Failing → STOP. Define "shipped" before building.
- If Build Sequence is Failing → STOP. You don't know what to build first.

### THE CRITICAL QUESTION

Before starting to build, answer honestly:

**"If I showed this plan to another developer, could they understand
what we're building, why, and in what order — without me explaining
anything verbally?"**

If yes → start building.
If no → the plan isn't clear enough yet.
