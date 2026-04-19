# INTEGRATION STRATEGY

**Version:** Gold v1.1
**Purpose:** The routing and system-map file for Anti-Gravity. This document explains how the layers fit together, how files should be selected, and how the OS assembles a runtime bundle for a task.

> This file is **not** the constitution. `GEMINI.md` owns behavior and authority.
> This file owns routing, layer interaction, runtime assembly, and support-layer placement.

---

## SYSTEM MAP SUMMARY

Anti-Gravity is a layered cognitive operating system. It becomes powerful when the right files are loaded in the right order for the right task.

This file answers:

- what the layers are
- how they interact
- how a task is routed across them
- when memory, templates, rubrics, and benchmarks enter the flow

---

## AUTHORITY AND ROUTING

| Layer of Authority | Role |
| :--- | :--- |
| `GEMINI.md` | Constitution, identity, user alignment, operating rules |
| `GLOBAL_MEMORY.md` | Routing logic, system map, layer interaction |
| `core/` | Deep reference for permanent behavior |
| `skills/` | Domain-specific behavior packs |
| `contexts/` | Live project truth |
| `workflows/` | Execution sequences |
| `memory/` | Retained learning |
| `global_templates/` | Output scaffolds and authoring templates |
| `rubric/` | Support-layer evaluation during critique |
| `benchmark/` | Advanced evaluation infrastructure for the OS itself |

### Routing Rules

1. Read `GEMINI.md` fully first.
2. Read this file next.
3. Pick the task mode.
4. Load only the smallest effective set of skills, contexts, and workflows.
5. Load memory, templates, rubrics, or benchmarks only when the task actually calls for them.

---

## THE 8 SYSTEM LAYERS

| Layer | Folder | Job | Loading Tier |
| :--- | :--- | :--- | :--- |
| 1 | `core/` | Permanent mind and deep reference for the kernel | Always active through the constitution |
| 2 | `skills/` | Specialized domain behavior | By task |
| 3 | `contexts/` | Live project truth | By task |
| 4 | `workflows/` | Execution sequences | By task |
| 5 | `global_templates/` | Output and authoring scaffolds | On demand |
| 6 | `rubric/` | Quality evaluation support | On demand |
| 7 | `benchmark/` | OS evaluation and improvement measurement | Evaluation only |
| 8 | `memory/` | Institutional learning and continuity | On demand |

---

## HOW THE LAYERS INTERACT

### Information Flow

A task arrives.

1. The constitution (`GEMINI.md`) defines how Anti-Gravity should behave.
2. This file (`GLOBAL_MEMORY.md`) determines which layers are relevant.
3. Skills define how to think in the active domain.
4. Contexts ground that thinking in project reality.
5. Workflows sequence the steps.
6. Templates shape outputs when a structured artifact is needed.
7. Rubrics help judge the result during critique.
8. Memory stores the learning if the work produced durable lessons.

### Feedback Loop

The system is not linear:

Task -> execution -> learning -> memory -> better future routing

Without memory, each session starts colder. With memory, the OS compounds judgment over time.

---

## FOLDER-TO-FOLDER INTERACTION MAP

### Primary Interactions

- `core/` governs all lower layers.
- `skills/` inherit from core and operate on top of contexts.
- `contexts/` make skill behavior specific to the project at hand.
- `workflows/` orchestrate skills, contexts, templates, rubrics, and memory checkpoints.
- `global_templates/` provide scaffolds for deliverables and authoring tasks.
- `rubric/` evaluates outputs near the end of a task, not at startup.
- `benchmark/` evaluates the operating system itself, not ordinary project work.
- `memory/` receives learning from any layer when the lesson is durable enough to keep.

### Cross-Reference Matrix

| Source Folder | References | Relationship |
| :--- | :--- | :--- |
| `core/` | all folders | Highest deep-reference layer under the constitution |
| `skills/` | `core/`, `contexts/`, `rubric/` | Behavior specialized by domain and later evaluated if needed |
| `contexts/` | `core/`, `skills/`, `workflows/` | Live truth that grounds execution |
| `workflows/` | `skills/`, `contexts/`, `global_templates/`, `rubric/`, `memory/` | Orchestrates execution and checkpoints |
| `global_templates/` | `workflows/`, `contexts/` | Supports output shaping and context authoring |
| `rubric/` | `skills/`, `workflows/` | Critique support near verification and review |
| `benchmark/` | `rubric/`, `memory/` | Advanced evaluation of system quality over time |
| `memory/` | all folders | Retains important learning and reduces repeated mistakes |

---

## SKILL, WORKFLOW, AND SUPPORT-LAYER MAP

| Domain | Primary Skill | Primary Workflow | Typical Contexts | Optional Support Layers |
| :--- | :--- | :--- | :--- | :--- |
| Coding | `skill-coding` | `workflow-build-feature` | stack, coding-standards, architecture | rubric, templates, memory |
| Debugging | `skill-debugging` | `workflow-debug-issue` | stack, architecture, infra | rubric, memory |
| Architecture | `skill-architecture` | `workflow-plan-architecture` | architecture, project, business-priorities | templates, rubric, memory |
| UI/UX | `skill-ui-ux` | `workflow-design-ui` | design-system, stack, visual-identity | templates, rubric |
| Security | `skill-security` | `workflow-security-audit` | security-baselines, architecture, stack | rubric, memory |
| Product / inception | `skill-product-thinking` | `workflow-project-inception` | project, business-priorities, domain-rules | templates, rubric, memory |

Rubrics and benchmarks are deliberately outside the normal startup path. They are support layers, not the core runtime bundle.

---

## RUNTIME TASK ASSEMBLY

### Assembly Protocol

When a task arrives, assemble a runtime bundle in this order:

1. **Constitution**
   - `GEMINI.md`
   - `GLOBAL_MEMORY.md`

2. **Task Classification**
   - determine mode
   - determine task type
   - determine risk and reversibility

3. **Skill Selection**
   - 1 primary skill
   - 0-2 secondary skills if the task genuinely spans domains

4. **Workflow Selection**
   - 1 workflow for multi-step work
   - if the work spans multiple workflows, execute them sequentially

5. **Context Selection**
   - load only the live context files needed
   - start with 1-2 and expand only if required

6. **Support-Layer Selection**
   - templates when producing structured output or scaffolding context files
   - memory when history matters
   - rubrics during critique or explicit assessment
   - benchmarks only when evaluating the OS itself

### Example Runtime Bundle

**Build a feature**

- Constitution: `GEMINI.md`, `GLOBAL_MEMORY.md`
- Skills: `skill-coding`, `skill-testing`
- Workflow: `workflow-build-feature.md`
- Contexts: `stack-context.md`, `coding-standards.md`, `architecture-context.md`
- Optional support: `feature-plan.md`, `rubric-code-quality.md`, relevant memory files

**Start a new project**

- Constitution: `GEMINI.md`, `GLOBAL_MEMORY.md`
- Skills: `skill-product-thinking`, `skill-architecture`
- Workflow: `workflow-project-inception.md`
- Contexts: none or minimal at the start; runtime contexts are created during the workflow
- Optional support: `project-brief.md`, context templates, project-planning rubric, workspace memory initialization

---

## MEMORY ROUTING

Memory is first-class, but selective.

### Default Memory Rules

- Use **workspace memory first** for project-specific lessons.
- Use **global memory** only for cross-project or system-level lessons.
- Do not load memory by default; load it because it changes the current decision.

### Memory File Roles

| File | Use When |
| :--- | :--- |
| `decisions-log.md` | a similar decision has already been made or a new decision needs to be logged |
| `common-patterns.md` | a proven pattern may save time or prevent reinvention |
| `mistakes-to-avoid.md` | the task touches an area with known traps |
| `postmortems.md` | the task resembles a prior incident or failure mode |
| `benchmark-results.md` | evaluating changes to the OS itself |
| `version-notes.md` | documenting changes to Anti-Gravity |

### Memory Routing Principle

Contexts tell the system what is true now.
Memory tells the system what was learned over time.

Do not use memory to replace current truth. Use it to preserve judgment, history, and lessons.

---

## SUPPORT LAYERS

### Templates

`global_templates/` has two jobs:

- shape formal deliverables
- scaffold context and setup files during authoring flows such as project inception

Templates are not runtime truth. They help create or structure runtime truth.

### Rubrics

`rubric/` is a support layer for critique, review, and explicit evaluation. Rubrics are not startup context and should not sit in the normal critical path.

### Benchmarks

`benchmark/` is advanced evaluation infrastructure. Benchmarks are for testing the OS itself, comparing versions, and measuring improvement. They are not ordinary task context.

---

## PRACTICAL INTEGRATION EXAMPLES

### Example 1: Build Feature

- load coding + testing skill
- load build-feature workflow
- load live stack and standards context
- load memory only if similar history matters
- load rubric only during critique

### Example 2: Debug Production Issue

- load debugging skill
- load debug workflow
- load stack, architecture, and relevant operational context
- check local mistakes-to-avoid or postmortems if similar incidents occurred
- use a debug report template only if formal documentation is needed

### Example 3: Project Inception

- use product-thinking + architecture
- create runtime-ready context files from templates
- initialize workspace memory files
- log the first architectural decision locally

---

## THE FULL SYSTEM AT A GLANCE

```text
GEMINI.md
  -> identity, authority, user alignment, operating rules

GLOBAL_MEMORY.md
  -> routing, system map, layer interaction

core/
  -> deep permanent behavior
skills/
  -> domain-specific behavior
contexts/
  -> runtime project truth
workflows/
  -> execution sequences
global_templates/
  -> output scaffolds and authoring templates
memory/
  -> retained learning
rubric/
  -> critique support
benchmark/
  -> advanced OS evaluation
```

---

## INTEGRATION RULES

1. `GEMINI.md` always governs behavior.
2. `GLOBAL_MEMORY.md` routes, but does not override the constitution.
3. Contexts should ground execution, not flood it.
4. Skills should specialize; they should not restate the constitution.
5. Templates should shape output or authoring, not masquerade as runtime truth.
6. Memory should be selective and correctly scoped.
7. Rubrics belong near critique, not startup.
8. Benchmarks never belong in ordinary task execution.
9. Read folder READMEs when entering a layer for the first time in a task.
10. Lean loading beats heavy loading.

---

## FINAL PRINCIPLE

The power of Anti-Gravity is not raw document count. It is disciplined composition:

the constitution for behavior, the system map for routing, live contexts for truth, workflows for sequence, memory for continuity, and support layers loaded only when they add real value.
