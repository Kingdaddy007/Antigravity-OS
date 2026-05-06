# GLOBAL MEMORY — SYSTEM MAP & ROUTING

**Version:** Gold v2.0 (Compressed)
**Purpose:** Routing logic, layer interaction, and runtime assembly for Anti-Gravity.
This file routes. `GEMINI.md` governs. Neither overrides the other's job.

---

## SYSTEM LAYERS

| Layer | Folder | Job | When Loaded |
| :--- | :--- | :--- | :--- |
| Constitution | `GEMINI.md` + this file | Identity + routing | Always |
| Deep reference | `core/` | System-thinking, cognitive patterns | On demand (architectural/high-stakes tasks) |
| Domain behavior | `skills/` | Specialized expertise packs | By task |
| Project truth | `contexts/` | Live project state | By task |
| Execution | `workflows/` | Step-by-step sequences | By task |
| Output scaffolds | `global_templates/` | Deliverable structures | On demand |
| Quality evaluation | `rubric/` | Critique and audit support | On demand |
| OS evaluation | `benchmark/` | Testing Anti-Gravity itself | Evaluation only |
| Retained learning | `memory/` | Cross-project lessons | On demand |

**Lean loading rule:** Load the smallest bundle that produces a strong answer. Better selection beats heavier selection.

---

## TASK ROUTING TABLE

### Architect Mode

**Trigger words:** "how should I structure", "design the system", "plan the architecture", "folder structure", "monolith vs microservices", "service boundaries", "system design"

| **Load:** `skills/architecture/SKILL.md` | workflow: `workflow-plan-architecture.md` | contexts: `architecture-context.md`, `stack-context.md` |

### Builder Mode

**Trigger words:** "build this", "implement", "create a component", "add this feature", "write the code", "create the endpoint", "wire this together"

| **Load:** `skills/coding/SKILL.md` | workflow: `workflow-build-feature.md` | contexts: `stack-context.md`, `coding-standards.md`, `architecture-context.md` |

### Debugger Mode

**Trigger words:** "fix", "broken", "not working", "error", "bug", "failing", "crash", "regression", stack traces, "why is this happening"

| **Load:** `skills/debugging/SKILL.md` | workflow: `workflow-debug-issue.md` | contexts: `stack-context.md`, `architecture-context.md` |

### Reviewer Mode

**Trigger words:** "review this", "check this code", "audit", "any issues with", "PR review", "give me feedback on"

| **Load:** `skills/review-audit/SKILL.md` + `skills/security/SKILL.md` | workflow: `workflow-review-code.md` | contexts: `coding-standards.md`, `security-baselines.md` |

### Designer Mode

**Trigger words:** "design", "UI", "UX", "user flow", "layout", "dashboard", "landing page", "accessibility", "how should this look/feel"

| **Load:** `skills/skills/ui-ux/SKILL.md` | workflow: `workflow-design-ui.md` | contexts: `design-system.md`, `visual-identity.md`, `stack-context.md` |

### Security Mode

**Trigger words:** "secure", "vulnerability", "auth", "permissions", "tokens", "secrets", "XSS", "CSRF", "injection", "PII", "trust boundary"

| **Load:** `skills/security/SKILL.md` | workflow: `workflow-security-audit.md` | contexts: `security-baselines.md`, `architecture-context.md` |

### Performance Mode

**Trigger words:** "slow", "optimize", "speed up", "bottleneck", "memory leak", "query is slow", "N+1", "Core Web Vitals", "lighthouse"

| **Load:** `skills/performance/SKILL.md` | workflow: `workflow-optimize-performance.md` | contexts: `stack-context.md`, `infra-context.md` |

### Research Mode

**Trigger words:** "compare", "which is better", "pros and cons", "should I use X or Y", "evaluate", "alternatives", "tradeoffs between"
**Load:** Domain-relevant skill | contexts: `stack-context.md`, `project-context.md`

### Optimizer Mode

**Trigger words:** "simplify", "refactor", "clean up", "technical debt", "reduce duplication", "code smell", "this is getting messy"

| **Load:** `skills/refactoring/SKILL.md` | workflow: `workflow-refactor-module.md` | contexts: `architecture-context.md`, `coding-standards.md` |

### Teacher Mode

**Trigger words:** "explain", "how does X work", "I don't understand", "what is", "teach me", "walk me through"
**Load:** Domain-relevant skill | no workflow needed for explanations

### Product/Inception Mode

**Trigger words:** "new project", "starting from scratch", "I have an idea", "what should I build", "project plan", "MVP"
**Load:** `skills/product-thinking/SKILL.md` + `skills/architecture/SKILL.md` | workflow: `workflow-project-inception.md`

### Marketer Mode

**Trigger words:** "write copy", "headline", "improve conversion", "landing page text", "sales strategy", "competitor profile"
**Load:** `skills/copywriting/SKILL.md` + `skills/marketing-psychology/SKILL.md` | workflow: `workflow-marketing-copy.md` | contexts: `product-marketing-context.md`, `project-context.md`

---

## RUNTIME ASSEMBLY PROTOCOL

When a task arrives:

1. **Classify** — determine mode, task type, risk level
2. **Skill selection** — 1 primary + 0–2 secondary (only when task genuinely spans domains)
3. **Workflow selection** — 1 workflow for multi-step work
4. **Context selection** — start with 1–2 files, expand only if required
5. **Support layers** — templates when producing structured output; memory when history matters; rubrics during critique only

---

## MEMORY ROUTING

**Workspace memory first** (`.agents/memory/` in project):

- `decisions-log.md` — decisions made in this project
- `common-patterns.md` — proven patterns in this project
- `mistakes-to-avoid.md` — known traps in this project

**Global memory second** (`antigravity/memory/`):

- Only for cross-project or system-level lessons
- Never write project-specific knowledge here

**Rule:** Load memory because it changes the current decision — not by default.

---

## CONTEXT FILES — WHAT THEY ARE

Context files in `contexts/` are **project-specific fill-in templates.** They are blank by default and get populated during project inception. They ground execution in your actual project truth. Never load more than needed.

| Context File | Load When |
| :--- | :--- |
| `stack-context.md` | Any coding, building, or debugging task |
| `architecture-context.md` | Architecture, debugging complex issues |
| `coding-standards.md` | Building, reviewing, refactoring |
| `design-system.md` + `visual-identity.md` | UI/UX work |
| `security-baselines.md` | Security, auth, review |
| `infra-context.md` | DevOps, performance, deployment |
| `project-context.md` | Project inception, new feature scoping |
| `product-marketing-context.md` | Copywriting, marketing, sales strategy |
| `domain-rules.md` | Business logic tasks |
| `database-context.md` | Database design, query optimization |

---

## FOLDER INTERACTION MAP

```text
GEMINI.md + GLOBAL_MEMORY.md
  → skills/ (domain behavior)
    → contexts/ (grounds skill in project reality)
      → workflows/ (sequences the work)
        → global_templates/ (shapes deliverables)
        → rubric/ (evaluates output during critique)
        → memory/ (stores durable lessons)
```

Task → execution → learning → memory → better future routing.

---

## INTEGRATION RULES

1. `GEMINI.md` always governs behavior.
2. This file routes — it does not override the constitution.
3. Contexts ground execution; they should not flood it.
4. Skills specialize; they should not restate the constitution.
5. Templates shape output or authoring — not masquerade as runtime truth.
6. Rubrics belong near critique, not startup.
7. Benchmarks never belong in ordinary task execution.
8. Lean loading beats heavy loading — always.

---

## WORKFLOW STATE TRACKING

Every active workflow must maintain a state file at `.agents/workflow-state.json` in the project workspace. This enables resuming work across sessions without restarting.

### On Workflow Start

1. Check if `.agents/workflow-state.json` exists for the current task area.
2. If it exists and matches the current task: ask "You have an active **[workflow]** workflow at **Phase [N] ([name])** — [pct]% complete. Resume?"
3. If starting fresh: create a new state file immediately.

### State File Format

```json
{
  "workflow": "build-feature",
  "started_at": "2026-04-10T14:00:00Z",
  "updated_at": "2026-04-10T15:30:00Z",
  "current_phase": "IMPLEMENT",
  "phase_number": 7,
  "total_phases": 11,
  "completion_pct": 64,
  "status": "in_progress",
  "feature_summary": "Brief description of what is being built",
  "phases": {
    "1_define_objective": { "status": "done", "completed_at": "..." },
    "2_ground_context":   { "status": "done", "completed_at": "..." },
    "7_implement":        { "status": "in_progress", "started_at": "..." },
    "8_self_review":      { "status": "pending" }
  },
  "notes": "Current progress notes — most useful field for resuming.",
  "key_decisions": ["Decision 1", "Decision 2"],
  "blockers": []
}
```

### Status Values

| Value | Meaning |
| :--- | :--- |
| `pending` | Phase not yet started |
| `in_progress` | Phase currently active |
| `done` | Phase completed |
| `blocked` | Cannot proceed — see `blockers` |
| `skipped` | Not needed for this task |

### Rules

1. **Check for active state at the start of any workflow activation.**
2. **Never silently overwrite an existing state file.** Ask first.
3. **Update state after every completed phase** — not at the end.
4. **Keep `notes` current** — it's the most useful field for resuming.
5. **Only ONE active workflow at a time.** Complete, pause, or archive before starting another.

### Workflow Phase Maps (for state file phase keys)

| Workflow | Phases |
| :--- | :--- |
| `build-feature` | define_objective → ground_context → define_scope → identify_risks → design_shape → verification_plan → implement → self_review → verify → deliver → post_ship |
| `debug-issue` | observe_symptoms → reproduce → isolate → hypothesize → verify_cause → fix → verify_fix → regression_check → document → post_ship |
| `design-ui` | user_goals → information_architecture → component_inventory → state_coverage → visual_design → implement → accessibility → verify → deliver → post_ship |
| `plan-architecture` | understand_requirements → identify_constraints → enumerate_options → evaluate_tradeoffs → make_decision → document_adr → communicate |
| `project-inception` | understand_idea → define_scope → choose_stack → design_architecture → sequence_work → create_contexts → deliver_plan |
| `marketing-copy` | context_gathering → psychology_alignment → drafting → refinement → delivery |

---

## BELOVED'S TECH STACK PREFERENCES

- **Logic:** TypeScript 7.0 (Native) via `tsgo`
- **Motion:** `motion` (Modern rebranded Framer Motion)
- **Standard:** Production-quality polish and motion-first UI by default.
