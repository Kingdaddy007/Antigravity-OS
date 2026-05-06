# RUBRIC: ARCHITECTURE QUALITY

**Version:** Gold v1.0
**Layer:** 10 — Evaluation
**Tier:** 3 — Loaded on demand
**File:** rubrics/architecture-rubric.md
**Purpose:** Self-assessment matrix for evaluating architectural decisions and designs before committing to implementation.
**Loaded When:** Phase 7 of architecture planning. Evaluating whether an architectural decision is ready to commit to.
**References:** skill-architecture.md, workflow-plan-architecture.md

***

## HOW TO USE THIS RUBRIC

After completing an architecture recommendation or design, evaluate
your work against each dimension below. Score each dimension.

- If **Requirements Clarity** scores **Failing** — STOP. Define
  requirements before designing architecture.

- If **Team Fit** scores **Needs Work** or below — reassess. An
  architecture the team cannot maintain will fail in operation.

- If **3 or more dimensions** score **Failing** — the architecture
  needs fundamental rework before committing.

Use this rubric:

- During architecture review before accepting a structural recommendation
- Before committing a decision to an ADR
- When comparing architecture options against project needs
- During benchmark evaluation of architecture approaches
- When evaluating service or module boundary decisions
- When critiquing a redesign proposal

***

## WHAT THIS RUBRIC EVALUATES

This rubric evaluates architecture across:

- Requirements clarity and problem fit
- Boundary clarity and ownership
- Options evaluation and alternatives
- Tradeoff honesty and transparency
- Failure mode and degradation awareness
- Simplicity and complexity discipline
- Team fit and operational realism
- Reversibility and evolvability
- Data ownership and source of truth
- Implementation guidance quality

This rubric is for judging whether a structure is actually good —
not merely diagrammable or sophisticated to describe.

***

## EVALUATION MATRIX

### 1. REQUIREMENTS CLARITY AND PROBLEM FIT

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Functional and non-functional requirements quantified. Constraints explicitly identified. Current state assessed. Scale targets defined with numbers. Success criteria measurable. Architecture is shaped by actual needs, constraints, and workflows — not prestige or hypothetical future problems. |
| **Acceptable** | Requirements identified and reasonably specific. Most constraints documented. Scale expectations understood qualitatively. Design grounded in real needs even if not fully quantified. |
| **Needs Work** | Requirements vague. Scale discussed in handwaves. Constraints assumed rather than verified. Architecture chosen before problem fully clarified. Complexity not tied to a real requirement. |
| **Failing** | No requirements defined. Architecture designed in a vacuum. Solution looking for a problem. Trend-driven structure with no connection to actual system needs. |

***

### 2. BOUNDARY CLARITY AND OWNERSHIP

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Module and component boundaries precisely defined. Ownership of behavior, data, and state transitions is clear. Interfaces documented. Data flow mapped. No ambiguity about what owns what. Responsibilities are separated clearly. Each boundary reduces confusion rather than creating it. |
| **Acceptable** | Boundaries defined and mostly clear. Minor ambiguity in one or two areas. Data flow understood. Responsibilities mostly separated. |
| **Needs Work** | Boundaries vague. Unclear ownership for some capabilities. Mixed responsibilities. Hand-wavy box boundaries. Overlapping domains without clear rules. |
| **Failing** | No defined boundaries. Responsibilities overlap. No clear interfaces. Ambiguous or overlapping control throughout. A distributed mess waiting to happen. |

***

### 3. DATA OWNERSHIP AND SOURCE OF TRUTH

| Score | Criteria |
| :--- | :--- |
| **Excellent** | It is clear where truth lives for every critical piece of state. Updates and responsibilities are explicit. Shared mutable ambiguity is avoided. Contract boundaries are well defined. Authority over critical state is unambiguous. |
| **Acceptable** | Data ownership mostly clear. Authority over primary state defined. Minor ambiguity in secondary or derived data that does not create serious risk. |
| **Needs Work** | Multiple systems potentially mutating the same truth without clear rules. Unclear authority over some critical state. Weak contract boundaries around shared data. |
| **Failing** | No clarity on where truth lives. Multiple systems owning the same state with no coordination rules. Data authority completely undefined. |

***

### 4. OPTIONS EVALUATION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Three or more genuine options evaluated — not one real option plus two strawmen. Each evaluated against requirements with pros, cons, risks, and effort. Boring technology option included. Alternatives considered meaningfully. A skeptical peer would understand why the chosen option was selected. |
| **Acceptable** | Two or three options considered with reasonable comparison. Chosen option justified against requirements. Alternatives acknowledged even if briefly. |
| **Needs Work** | Only one option seriously considered. Alternatives dismissed without evaluation. Decision feels predetermined. No meaningful comparison against requirements. |
| **Failing** | No alternatives considered. Architecture defaulted to whatever was familiar. No evaluation against requirements. One option presented with no justification. |

***

### 5. TRADEOFF TRANSPARENCY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Tradeoffs explicitly named — both what is gained AND what is sacrificed. Rationale for each tradeoff is explained. Stakeholders understand what they are accepting. Mitigation offered for losing concerns. Reasoning is honest rather than one-sided. |
| **Acceptable** | Key tradeoffs identified and explained. Gains and sacrifices documented. Costs of the design are visible. |
| **Needs Work** | Some tradeoffs acknowledged but not analyzed. Sacrifices downplayed or omitted. Only benefits presented prominently. Hidden costs or vague rationale. |
| **Failing** | No tradeoffs discussed. Architecture presented as having no downsides. Best-of-everything fantasy. One option presented as free of downside with alternatives ignored. |

***

### 6. FAILURE MODE ANALYSIS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Failure modes identified for each component. Degradation paths defined — graceful versus catastrophic. Blast radius is understandable. Detection mechanisms specified. Recovery paths documented. Risky assumptions made visible. Pre-mortem conducted for high-stakes decisions. |
| **Acceptable** | Major failure modes identified. Basic degradation and recovery paths considered. Most components have failure handling. Dependency failure considered. |
| **Needs Work** | Only happy-path architecture described. Some failure modes mentioned but not analyzed. No detection or recovery planning. No blast-radius consideration. |
| **Failing** | No failure analysis. Architecture designed only for the success case. First production incident will be a surprise. No recovery assumptions. |

***

### 7. SIMPLICITY AND COMPLEXITY DISCIPLINE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | The simplest architecture that meets all requirements. No speculative components. No premature abstraction. Boring technology by default. Complexity exists only where requirements demand it. Architecture is proportionate to the system's current real needs. |
| **Acceptable** | Generally simple. Minor over-engineering that is defensible given near-term roadmap. Abstractions are earning their cost. |
| **Needs Work** | Over-engineered for current requirements. Components built for imagined future needs. Unnecessary distribution or abstraction layers. Technology chosen for sophistication rather than problem fit. Architecture harder to explain than the problem itself. |
| **Failing** | Massively over-engineered. Microservices for a team of three. Event sourcing for a CRUD app. Kubernetes for one hundred users. Resume-driven architecture. Overfitting to speculative future scale at the cost of current simplicity. |

***

### 8. TEAM FIT AND OPERATIONAL REALISM

| Score | Criteria |
| :--- | :--- |
| **Excellent** | The team can build, operate, and maintain this architecture. Skills match requirements. Operational burden is manageable. Deployment and monitoring implications understood. Observability considered. A mid-level engineer can debug this at 2 AM. Conway's Law alignment considered. |
| **Acceptable** | Team can build this with some learning. Operational requirements are reasonable. Some new skills needed but achievable. Deployment and monitoring burden understood. |
| **Needs Work** | Significant skill gaps. Operational burden may exceed team capacity. Architecture assumes operational capabilities the team does not have. Deployment and monitoring complexity hidden or underestimated. |
| **Failing** | Team cannot realistically build or maintain this. Requires dedicated DevOps, SRE, or platform team that does not exist. Deployment and monitoring burden ignored entirely. Recipe for organizational failure. |

***

### 9. REVERSIBILITY AND EVOLVABILITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Reversibility cost assessed for each major decision. Irreversible decisions received the deepest analysis. Hard-to-reverse choices are explicitly acknowledged. Reversibility paths designed where possible. Review triggers and escape hatches defined. Evolution path is clear enough to follow. |
| **Acceptable** | Reversibility considered for the highest-stakes decisions. General awareness of which choices are hard to undo. Likely future changes are manageable. |
| **Needs Work** | Reversibility not explicitly evaluated. Some decisions may be harder to reverse than assumed. Evolution path unclear. High ceremony required for common future modifications. |
| **Failing** | No reversibility analysis. Irreversible decisions made without appropriate scrutiny. No review triggers. No escape hatch. Every future change likely to cross many boundaries painfully. |

***

### 10. IMPLEMENTATION GUIDANCE QUALITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Architecture actually guides implementation sequencing. Open decisions and fixed decisions are distinguished clearly. Interfaces and contracts are explicit and simple. Internal complexity does not leak across boundaries. Another engineer could implement from this design without fundamental ambiguity. |
| **Acceptable** | Implementation direction is mostly clear. Most interfaces defined. Open decisions noted even if not fully resolved. Sequencing guidance present for major components. |
| **Needs Work** | Architecture describes the end state but not how to get there. Open decisions not distinguished from fixed ones. Interfaces vague. Implementation would require many follow-up conversations. |
| **Failing** | No implementation guidance. Architecture exists only as an abstract diagram or concept. Boundaries and contracts too vague to implement from. Another engineer could not proceed without a complete rethink. |

***

## SCORING SUMMARY

| Dimension | Score | Notes |
| :--- | :--- | :--- |
| Requirements Clarity / Problem Fit |||
| Boundary Clarity and Ownership |||
| Data Ownership / Source of Truth |||
| Options Evaluation |||
| Tradeoff Transparency |||
| Failure Mode Analysis |||
| Simplicity / Complexity Discipline |||
| Team Fit / Operational Realism |||
| Reversibility / Evolvability |||
| Implementation Guidance Quality |||
***

## DELIVERY DECISION

| Result | Decision |
| :--- | :--- |
| All Excellent / Acceptable | ✅ Ready to commit — document as ADR |
| Requirements Clarity Failing | ❌ STOP — define requirements before designing architecture |
| Team Fit Needs Work or below | ⚠️ Reassess — an architecture the team cannot maintain will fail |
| Any 3+ Failing | ❌ Architecture needs fundamental rework |

***

## MINIMUM PASS STANDARD

Architecture should not be considered strong if it is weak
in any of these high-priority areas:

- Problem fit — solving a real problem, not a vague abstraction target
- Boundary clarity — responsibilities clear enough to implement from
- Simplicity — complexity proportionate to actual needs
- Changeability — future evolution is not unnecessarily painful
- Failure awareness — the design considers what goes wrong

Pretty diagrams do not compensate for weak structural thinking.

***

## COMMON FAILURE PATTERNS

### Diagram-First Architecture

The design looks structured visually but is weakly tied
to real constraints, team reality, or actual requirements.

### Pattern Worship

A named architecture pattern is chosen because it sounds
advanced, not because it fits the current reality.
Sophistication theater over structural honesty.

### Boundary Ambiguity

The proposal uses many terms but still does not make
responsibility and ownership clear enough to implement.

### Operational Blind Spot

The architecture looks clean conceptually but is weak in
deployment, observability, failure handling, or
coordination realism. The team cannot actually run it.

### Overfitting to Speculative Future Scale

Current simplicity sacrificed for imagined future
complexity that may never arrive. Resume-driven
over-engineering.

### Tradeoff Denial

One option presented as having no downsides. Alternatives
ignored. Costs hidden. Reasoning one-sided.

### Guess-Then-Commit

Architecture committed before requirements are clear.
Design shaped by preference rather than by the actual
problem and constraints.

***

## FINAL QUESTIONS

Before committing this architecture, ask:

- Does this architecture reduce future confusion or create it?
- Is this structure solving the real problem, or expressing an engineering preference?
- If this is wrong, how expensive will it be to undo?
- Can the team actually build, operate, and debug this?
- Would a skeptical peer understand and trust this decision?
- Is this architecture good, or merely sophisticated to describe?

***

## Good architecture makes the system easier to understand, change, and trust — not merely more sophisticated to describe
