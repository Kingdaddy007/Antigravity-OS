# INTEGRATION STRATEGY

**Version:** Gold v1.0
**Location:** [GLOBAL_MEMORY.md]({{GLOBAL_CONFIG_URI}}/GLOBAL_MEMORY.md)
**Purpose:** The architectural integration map of the entire Anti-Gravity operating system. Explains how all folders, files, and layers work together as one coordinated system.

> [!NOTE]
> This is NOT a user prompt. This is NOT a loading strategy.
> This is the engineering blueprint of HOW the system interconnects.
> Read this to understand WHY the system is structured this way and HOW task execution flows across all layers.

---

## CORE THESIS

Anti-Gravity is not a prompt pack. It is not a collection of reference documents. It is a **layered cognitive operating system** where each layer has a distinct job and the layers work together as an integrated whole.

The system becomes powerful not when all files are loaded, but when the **right files are integrated in the right order for the right task.**

---

## THE 8 SYSTEM LAYERS

Each folder in [antigravity/]({{GLOBAL_CONFIG_URI}}/antigravity/) represents a functional layer. These layers are numbered by their role in the cognitive pipeline, not by their folder position.

**LAYER 1 — PERMANENT MIND ([core/]({{GLOBAL_CONFIG_URI}}/antigravity/core/))**
The stable operating kernel. Identity, cognition, modes, process, standards. Always active. Never unloaded.
│
▼
**LAYER 2 — SPECIALIZED EXPERTISE ([skills/]({{GLOBAL_CONFIG_URI}}/antigravity/skills/))**
Domain-specific behavioral instructions. Activated by task. Changes HOW Anti-Gravity thinks in a specific domain.
│
▼
**LAYER 3 — GROUND TRUTH ([contexts/]({{GLOBAL_CONFIG_URI}}/antigravity/contexts/))**
Project-specific facts. Stack, architecture, conventions, business rules. Prevents generic advice.
│
▼
**LAYER 4 — TASK EXECUTION ([workflows/]({{GLOBAL_CONFIG_URI}}/antigravity/workflows/))**
Step-by-step execution sequences. Chains skills together. Defines WHAT to do first, next, and last.
│
▼
**LAYER 5 — OUTPUT FORMALIZATION ([templates/]({{GLOBAL_CONFIG_URI}}/antigravity/global_templates/))**
Reusable output scaffolds. Ensures consistent, complete deliverables for formal artifacts.
│
▼
**LAYER 6 — QUALITY JUDGMENT ([rubrics/]({{GLOBAL_CONFIG_URI}}/antigravity/rubric/))**
Self-assessment matrices. Evaluates whether output is strong enough BEFORE delivery.
│
▼
**LAYER 7 — IMPROVEMENT MEASUREMENT ([benchmarks/]({{GLOBAL_CONFIG_URI}}/antigravity/benchmarks/))**
Repeatable test scenarios. Measures whether the system is getting better over time.
│
▼
**LAYER 8 — INSTITUTIONAL LEARNING ([memory/]({{GLOBAL_CONFIG_URI}}/antigravity/memory/))**
Retained knowledge. Decisions, patterns, mistakes, results, postmortems, system evolution. Compounds over time.

### Layer Characteristics

| Layer | Folder | Files | Loading Tier | Stability | Content Type |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `core/` | 9 | Tier 1 — Always on | Very stable | Behavioral rules |
| 2 | `skills/` | 14 | Tier 2 — By task | Stable | Domain instructions |
| 3 | `contexts/` | 12 | Tier 2 — By task | Variable | Project facts |
| 4 | `workflows/` | 11 | Tier 2 — By task | Stable | Execution sequences |
| 5 | `templates/` | 7 | Tier 3 — On demand | Stable | Output scaffolds |
| 6 | `rubrics/` | 11 | Tier 3 — On demand | Stable | Evaluation matrices |
| 7 | `benchmarks/` | 7 | Tier 4 — Evaluation only | Stable | Test scenarios |
| 8 | `memory/` | 6 | Tier 3 — On demand | Growing continuously | Accumulated knowledge |

---

## HOW THE LAYERS INTERACT

### The Information Flow

A TASK ARRIVES
│
▼
CORE (Layer 1) identifies:
├── Which MODE to activate ([operating-modes.md]({{GLOBAL_CONFIG_URI}}/antigravity/core/operating-modes.md))
├── Which SKILLS to load ([activation-engine.md]({{GLOBAL_CONFIG_URI}}/antigravity/core/activation-engine.md))
├── Which WORKFLOW to follow ([activation-engine.md]({{GLOBAL_CONFIG_URI}}/antigravity/core/activation-engine.md))
├── The PROCESS to follow ([execution-workflow.md]({{GLOBAL_CONFIG_URI}}/antigravity/core/execution-workflow.md))
└── The QUALITY BAR to meet ([quality-bar.md]({{GLOBAL_CONFIG_URI}}/antigravity/core/quality-bar.md))
│
▼
SKILLS (Layer 2) add domain expertise:
├── Primary skill loaded (1 file)
├── Secondary skills loaded (0-2 files)
└── Skill tells Anti-Gravity HOW to think in this domain
│
▼
CONTEXTS (Layer 3) ground the work:
├── Project-specific files loaded (1-4 files)
└── Context tells Anti-Gravity WHAT specific environment to work in
│
▼
WORKFLOW (Layer 4) sequences execution:
├── One workflow loaded
├── Workflow defines the step-by-step process
├── Each step may activate different mode + skill combinations
└── Workflow includes gates ("do not proceed until...")
│
▼
EXECUTION HAPPENS (following the workflow steps)
│
▼
TEMPLATES (Layer 5) shape output if needed:
├── Loaded only during the Communicate phase
└── Only if the output is a formal deliverable
│
▼
RUBRICS (Layer 6) evaluate quality:
├── Loaded during the Critique/Verify phase
├── Self-assessment against domain-specific criteria
└── Determines: ship, fix, or revisit
│
▼
MEMORY (Layer 8) stores learning: (NOTE: Project-specific knowledge MUST go to the workspace's LOCAL memory folder, e.g. .agents/memory/, instead of this global path)
├── Significant decisions → [decisions-log.md]({{GLOBAL_CONFIG_URI}}/antigravity/memory/decisions-log.md)
├── Useful patterns → [common-patterns.md]({{GLOBAL_CONFIG_URI}}/antigravity/memory/common-patterns.md)
├── Mistakes made → [mistakes-to-avoid.md]({{GLOBAL_CONFIG_URI}}/antigravity/memory/mistakes-to-avoid.md)
├── If incident → [postmortems.md]({{GLOBAL_CONFIG_URI}}/antigravity/memory/postmortems.md)
└── If system changed → [version-notes.md]({{GLOBAL_CONFIG_URI}}/antigravity/memory/version-notes.md)

### The Feedback Loop

The system is not linear — it has a feedback loop:
Task → Execute → Learn → Memory grows
│
▼
Next similar task → Load memory
│
▼
Better execution → Better learning
│
▼
System gets stronger over time

Without memory, every task starts from zero. With memory, every task builds on everything before.

---

## FOLDER-TO-FOLDER INTERACTION MAP

### Primary Interactions

[{{GLOBAL_CONFIG_URI}}/antigravity/core/]({{GLOBAL_CONFIG_URI}}/antigravity/core/) ─────────────────────────────────────────────┐
│ governs everything │
├──▶ [skills/]({{GLOBAL_CONFIG_URI}}/antigravity/skills/) (skills inherit from core) │
├──▶ [workflows/]({{GLOBAL_CONFIG_URI}}/antigravity/workflows/) (workflows implement core process)
├──▶ [templates/]({{GLOBAL_CONFIG_URI}}/antigravity/global_templates/) (templates implement core output contracts)
├──▶ [rubrics/]({{GLOBAL_CONFIG_URI}}/antigravity/rubric/) (rubrics implement core quality bar)
└──▶ ALL (core is the highest authority) │
│
[skills/]({{GLOBAL_CONFIG_URI}}/antigravity/skills/) ◀──▶ [workflows/]({{GLOBAL_CONFIG_URI}}/antigravity/workflows/) │
│ workflows activate skills │
│ skills define domain behavior │
│ │
[skills/]({{GLOBAL_CONFIG_URI}}/antigravity/skills/) ◀──▶ [contexts/]({{GLOBAL_CONFIG_URI}}/antigravity/contexts/) │
│ skills provide universal HOW │
│ contexts provide specific WHAT │
│ together = grounded expertise │
│ │
[skills/]({{GLOBAL_CONFIG_URI}}/antigravity/skills/) ──▶ [rubrics/]({{GLOBAL_CONFIG_URI}}/antigravity/rubric/) │
│ each skill has a corresponding rubric │
│ skill = how to do it │
│ rubric = how to judge it │
│ │
[workflows/]({{GLOBAL_CONFIG_URI}}/antigravity/workflows/) ──▶ [templates/]({{GLOBAL_CONFIG_URI}}/antigravity/global_templates/) │
│ workflows specify output templates │
│ templates are used during delivery phase │
│ │
[workflows/]({{GLOBAL_CONFIG_URI}}/antigravity/workflows/) ──▶ [rubrics/]({{GLOBAL_CONFIG_URI}}/antigravity/rubric/) │
│ workflows invoke rubrics at critique phase │
│ │
[benchmarks/]({{GLOBAL_CONFIG_URI}}/antigravity/benchmarks/) ──▶ [rubrics/]({{GLOBAL_CONFIG_URI}}/antigravity/rubric/) │
│ benchmarks are scored using rubrics │
│ │
[benchmarks/]({{GLOBAL_CONFIG_URI}}/antigravity/benchmarks/) ──▶ [memory/]({{GLOBAL_CONFIG_URI}}/antigravity/memory/) │
│ benchmark results stored in memory │
│ │
everything ──▶ [memory/]({{GLOBAL_CONFIG_URI}}/antigravity/memory/) │
learning from any layer feeds memory │
───────────────────────────────────────────────────┘

### Cross-Reference Matrix

| Source Folder | References | Relationship |
| :--- | :--- | :--- |
| `core/` | All folders | Governs all behavior. Highest authority. |
| `skills/` | `core/`, `contexts/`, `rubrics/` | Inherits from core. Grounded by contexts. Evaluated by rubrics. |
| `contexts/` | `core/`, `skills/` | Grounds core rules in project facts. Makes skills project-specific. |
| `workflows/` | `core/`, `skills/`, `contexts/`, `templates/`, `rubrics/` | Orchestrates everything. Loads skills, contexts, templates, and rubrics at appropriate phases. |
| `templates/` | `workflows/`, `core/` | Used by workflows during delivery. Implements core output standards. |
| `rubrics/` | `skills/`, `workflows/`, `core/` | Evaluates skill output. Invoked by workflows. Implements core quality bar. |
| `benchmarks/` | `rubrics/`, `memory/` | Scored by rubrics. Results stored in memory. |
| `memory/` | Everything | Receives learning from all layers. Consulted when history matters. |

---

## SKILL-TO-RUBRIC-TO-WORKFLOW MAP

This map shows how every domain connects across layers:

| Domain | Skill File | Primary Rubric | Primary Workflow | Key Contexts |
| :--- | :--- | :--- | :--- | :--- |
| Coding | `skill-coding` | `code-quality-rubric` | `workflow-build-feature` | stack, coding-standards, architecture |
| Architecture | `skill-architecture` | `architecture-rubric` | `workflow-plan-architecture` | architecture, stack, project, business-priorities |
| Debugging | `skill-debugging` | `debugging-rubric` | `workflow-debug-issue` | stack, architecture, infra |
| Review | `skill-review-audit` | `communication-rubric` | `workflow-review-code` | coding-standards, architecture, security |
| UI/UX | `skill-ui-ux` | `ux-rubric` | `workflow-design-ui` | design-system, stack, architecture |
| Security | `skill-security` | `security-rubric` | `workflow-security-audit` | security-baselines, architecture, stack |
| Testing | `skill-testing` | `testing-rubric` | `workflow-build-feature` | testing-standards, stack |
| Performance | `skill-performance` | `performance-rubric` | `workflow-optimize-performance` | stack, database, infra |
| Database | `skill-database` | `architecture-rubric` | `workflow-build-feature` | database, architecture |
| API | `skill-api-design` | `api-quality-rubric` | `workflow-design-api` | api-conventions, security, stack |
| DevOps | `skill-devops-infra` | `release-readiness-rubric` | `workflow-ship-to-production` | infra, security, testing-standards |
| Refactoring | `skill-refactoring` | `code-quality-rubric` | `workflow-refactor-module` | coding-standards, architecture, testing |
| Research | `skill-research-analysis` | `communication-rubric` | (direct mode) | project, stack, business-priorities |
| Product | `skill-product-thinking` | `project-planning-rubric` | `workflow-project-inception` | project, business-priorities, domain-rules |

---

## RUNTIME TASK ASSEMBLY

### The Assembly Protocol

When a task arrives, Anti-Gravity assembles a **runtime bundle** — the specific combination of files active for this task.

#### Step 1: Base Layer (Always Present)

ALWAYS LOADED:
└── core/ (all 9 files — via master system prompt)

#### Step 2: Task Classification

Determine:

- What MODE is this? (Architect, Builder, Debugger, etc.)
- What TYPE of task? (build feature, debug, review, etc.)
- What RISK level? (high = more files, low = fewer files)

#### Step 3: Skill Selection

LOAD:

- 1 PRIMARY skill (matches the mode)
- 0-2 SECONDARY skills (if task spans domains)

RULE: Never load more than 3 skill files.

#### Step 4: Workflow Selection

LOAD:
└── 1 workflow (matches the task type)

RULE: Never load multiple workflows simultaneously.

#### Step 5: Context Selection

LOAD:
└── 1-4 context files (relevant to the specific work)

RULE: Start with 1-2. Add more only if needed. RULE: Maximum 4 context files per task.

#### Step 6: On-Demand (During Execution)

LOAD WHEN NEEDED:

- 1 template (during Communicate phase)
- 1 rubric (during Critique phase)
- 0-2 memory files (if past decisions are relevant)

RULE: Don't pre-load these. Load at the moment of need.

### The Assembled Bundle

A typical task configuration looks like:
RUNTIME BUNDLE (Example: Build a New Feature)
│
├── CORE (always) [9 files — via system prompt]
├── PRIMARY SKILL: skill-coding [1 file]
├── SECONDARY SKILL: skill-testing [1 file]
├── WORKFLOW: workflow-build-feature [1 file]
├── CONTEXT: stack-context.md [1 file]
├── CONTEXT: architecture-context.md [1 file]
└── CONTEXT: coding-standards.md [1 file]
│
│ ... during execution ...
│
├── TEMPLATE: feature-plan.md [loaded at Phase 5]
├── RUBRIC: code-quality-rubric.md [loaded at Phase 7]
└── MEMORY: decisions-log.md [loaded if relevant]

---

## PRACTICAL INTEGRATION EXAMPLES

### Example 1: Build a Feature

**Assembly:**

| Layer | Files Loaded | When |
| :--- | :--- | :--- |
| Core | All 9 (via system prompt) | Always |
| Skills | `skill-coding`, `skill-testing` | Task start |
| Contexts | `stack-context`, `architecture-context`, `coding-standards`, `database-context` | Task start |
| Workflow | `workflow-build-feature` | Task start |
| Template | `feature-plan.md` | During scoping |
| Rubric | `code-quality-rubric.md` | During self-review |

---

### Example 2: Debug a Production Issue

**Assembly:**

| Layer | Files Loaded | When |
| :--- | :--- | :--- |
| Core | All 9 | Always |
| Skills | `skill-debugging`, `skill-security` | Task start |
| Contexts | `stack-context`, `architecture-context`, `infra-context`, `security-baselines` | Task start |
| Workflow | `workflow-debug-issue` | Task start |
| Template | `debug-report.md` | After fix |
| Rubric | `debugging-rubric.md` | Before delivery |

---

### Example 3: Start a New Project (Hackathon)

**Assembly:**

| Layer | Files Loaded | When |
| :--- | :--- | :--- |
| Core | All 9 | Always |
| Skills | `skill-product-thinking`, `skill-architecture` | Task start |
| Contexts | None initially (created during execution) | Task start |
| Workflow | `workflow-project-inception` | Task start |
| Template | `project-brief.md` | Phase 5 |
| Rubric | `project-planning-rubric.md` | After Phase 5 |

---

### Example 4: Ship to Production

**Assembly:**

| Layer | Files Loaded | When |
| :--- | :--- | :--- |
| Core | All 9 | Always |
| Skills | `skill-devops-infra`, `skill-review-audit` | Task start |
| Contexts | `infra-context`, `security-baselines`, `testing-standards` | Task start |
| Workflow | `workflow-ship-to-production` | Task start |

---

## INTEGRATION RULES

### Rule 1: Core Always Governs

No skill, context, workflow, template, or rubric should silently override the core layer. If a conflict exists, core wins.

### Rule 2: One Workflow at a Time

Multiple workflows should NOT compete simultaneously. If a task genuinely spans multiple workflow types, execute them SEQUENTIALLY.

### Rule 3: Context Should Ground, Not Flood

Load only the contexts that materially improve the current task. Maximum 4 context files per task.

### Rule 4: Skills Specialize, Core Generalizes

Skills add domain-specific behavior. They should NOT restate core principles.

### Rule 5: Templates Are Optional

Use templates when the output benefits from formal structure. Deliverables like ADRs, debug reports, and project briefs need them.

### Rule 6: Rubrics Belong Near Verification

Load rubrics during the Critique/Verify phase.

### Rule 7: Memory Is Selective

Load memory files when historical context matters. Do NOT load memory by default.

### Rule 8: Benchmarks Are Not Runtime Context

Benchmark files are evaluation tools for testing Anti-Gravity itself. They are NEVER loaded during normal task execution.

### Rule 9: README First

When entering any folder for the first time in a task, read the folder's `README.md` first.

### Rule 10: Lean Loading Beats Heavy Loading

A focused bundle of 3-5 relevant files produces better output than a bloated bundle.

---

## THE FULL SYSTEM AT A GLANCE

[antigravity/]({{GLOBAL_CONFIG_URI}}/antigravity/)

├── [core/]({{GLOBAL_CONFIG_URI}}/antigravity/core/) (9 files) ← Layer 1: Permanent Mind
├── [skills/]({{GLOBAL_CONFIG_URI}}/antigravity/skills/) (14 files) ← Layer 2: Domain Expertise
├── [contexts/]({{GLOBAL_CONFIG_URI}}/antigravity/contexts/) (12 files) ← Layer 3: Ground Truth
├── [workflows/]({{GLOBAL_CONFIG_URI}}/antigravity/workflows/) (11 files) ← Layer 4: Execution Patterns
├── [templates/]({{GLOBAL_CONFIG_URI}}/antigravity/global_templates/) (7 files) ← Layer 5: Output Scaffolds
├── [rubrics/]({{GLOBAL_CONFIG_URI}}/antigravity/rubric/) (11 files) ← Layer 6: Quality Judges
├── [benchmarks/]({{GLOBAL_CONFIG_URI}}/antigravity/benchmarks/) (7 files) ← Layer 7: Improvement Tests
└── [memory/]({{GLOBAL_CONFIG_URI}}/antigravity/memory/) (6 files) ← Layer 8: Institutional Learning

---

## FINAL PRINCIPLE

The power of this system is not in any individual file. The power is in the **integration** — the right files, loaded in the right order, for the right task, governed by stable principles, evaluated against consistent standards, and learning from every execution.
