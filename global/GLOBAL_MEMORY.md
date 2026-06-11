# GLOBAL MEMORY — SYSTEM MAP & ROUTING

**Version:** Gold v2.0 (Compressed)
**Purpose:** Routing logic, layer interaction, and runtime assembly for Anti-Gravity.
This file routes. `GEMINI.md` governs. Neither overrides the other's job.

---

## SYSTEM LAYERS

| Layer | Folder | Job | When Loaded |
| :--- | :--- | :--- | :--- |
| Constitution | `GEMINI.md` + this file | Identity + routing | Always |
| Deep reference | `core/` | System-thinking, cognitive patterns | Compressed always-on (in GEMINI.md) + full files by task (Tier 2) |
| Domain behavior | `skills/` | Specialized expertise packs | By task |
| Project truth | `contexts/` | Live project state | By task |
| Execution | `workflows/` | Step-by-step sequences | By task |
| Output scaffolds | `global_templates/` | Deliverable structures | On demand |
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

| **Load:** `skills/ui-ux/SKILL.md` | workflow: See `workflow-design-ui.md` (master orchestrator — full Impeccable lifecycle map) | contexts: `PRODUCT.md`, `DESIGN.md`, `stack-context.md` |

**Impeccable is the design authority.** All visual design, UI craft, and motion work routes through the Impeccable workflow system. See `workflow-design-ui.md` for the full 3-tier lifecycle (Context → Build → Refine).

**Quick reference:**
- New project: `/impeccable-teach` → `/impeccable-document` → `/impeccable-craft`
- Brand build: Add storytelling + visual brainstorm before `/impeccable-document`
- Review: `/impeccable-critique` (design) | `/impeccable-audit` (technical)
- Polish: `/impeccable-polish` (after critique + audit)
- Specialized: `/impeccable-animate`, `/impeccable-colorize`, `/impeccable-typeset`, `/impeccable-layout`, `/impeccable-bolder`, `/impeccable-quieter`, etc.
- Full list: `workflow-design-ui.md` Tier 2 table

### Brand Diagnostics Mode

**Trigger words:** "audit the brand", "brand gap", "brand world", "perception gap", "founder lore", "diagnose the brand", "brand scorecard", "positioning diagnostic", "premium signaling", "counter-movement", "signature method", "brand world diagnostics"

| **Load:** `skills/brand-strategy/SKILL.md` | workflow: `workflow-storytelling.md` | contexts: `research-brief.md`, `story.md`, `PRODUCT.md` |

**skill-brand-strategy** is the brand diagnostics authority. Runs a 12-layer diagnostic model: perception gap → founder lore → brand world → enemy/counter-movement → signature language → behavioral persuasion → copy system → visual direction → cinematic motion → UX/conversion → content engine → scorecard. Produces structured audit output (`contexts/brand-diagnostics.md`) that feeds directly into `skill-storytelling` and `skill-copywriting`.

### Cinematic Motion Mode

**Trigger words:** "animate", "scroll animation", "3D", "parallax", "video scrub", "GSAP", "R3F", "cinematic", "motion", "make it come alive", "make it less static"

| **Load:** `skills/cinematic-motion/SKILL.md` | workflow: `/impeccable-animate` | contexts: `motion-direction.md`, `story.md`, `PRODUCT.md`, `DESIGN.md` |

**skill-cinematic-motion** is the animation authority. Register-aware (brand vs product). Contains: creative direction (diagnostic walkthrough, brand-to-motion matrix, hybrid archetypes, worked examples), GSAP patterns, R3F patterns, Framer Motion patterns, asset planning (image briefs for Figma AI, video prompts, 3D requirements), performance budgets, animation sequencing.

> [!IMPORTANT]
> **The Motion-Direction Authority Rule:**
> - `contexts/story.md` is the narrative authority (written using `skill-storytelling`). It defines the narrative "Why" (the emotional intent and pacing of motion).
> - `contexts/motion-direction.md` is the animation authority (written using `skill-cinematic-motion`). It defines the technical "How" (GSAP patterns, timelines, easing values, and asset specifications).
> - **Boundary:** Under no circumstances should `skill-storytelling` be used to author or edit `contexts/motion-direction.md`. If a task involves writing `motion-direction.md`, the agent must immediately load `skill-cinematic-motion`.

### Storytelling Mode

**Trigger words:** "story", "narrative", "brand story", "what should we say", "how should this feel", "positioning", "pre-suasion", "emotional journey", "copy direction"

| **Load:** `skills/storytelling/SKILL.md` + `skills/storytelling/library/matching-guide.md` | workflow: `workflow-storytelling.md` | contexts: `story.md`, `research-brief.md`, `PRODUCT.md` |

**skill-storytelling** is the narrative authority. Creates `story.md` — the master document that drives copy, visuals, animation, and layout. Contains: research framework, 6 narrative arcs, emotional journey mapping, copy-visual-animation integration, brand archetype storytelling patterns, iteration process.

**Storytelling Library** (`skills/storytelling/library/`) — 24 mechanics + support files:
- `index.md` — overview, quick reference, 24-mechanic index
- `matching-guide.md` — 10 brand archetypes → relevant mechanics (load always during research)
- `motion-personalities.md` — 7 personalities (brutal, glacial, mechanical, stuttered, liquid, surgical, jittery) with GSAP/Framer/CSS specs
- `density-levels.md` — 3 levels (minimal, moderate, maximalist)
- `psychological-levers.md` — 8 levers with web translations
- `mechanics/` — 24 individual mechanic files with full web translation specs

Source: 4 literary research documents extracting storytelling principles from masterworks (The Rook, Fever Dream, Interior Chinatown, Piranezi, The City & The City, Dark Matter, Annihilation, Trust, The Fifth Season, Mexican Gothic, Lincoln in the Bardo, We Have Always Lived in the Castle, The Remains of the Day, Blindness, The Blade Itself, Cloud Atlas, The Wasp Factory, The Bell Jar, Never Let Me Go, Circe, The Silent Patient, etc.).

**How to use the library:** 
- During research (Phase 1 of workflow-storytelling): check `matching-guide.md` for mechanics that fit the brand archetype
- During story construction (Phase 3): load the 2–3 library mechanics that match the chosen narrative arc (do not load all 24 — load only what the matching guide selects)
- During visual brainstorm: reference motion personalities and build specs
Like Pinterest/Dribbble for storytelling — seeds for inspiration, not templates to copy.

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

### Expert Positioning Mode

**Trigger words:** "positioning audit", "WWP audit", "expert posture", "submissive copy", "authority copy", "qualification gates", "RFP response", "paid diagnostic offer", "win without pitching"

| **Load:** `skills/expert-positioning/SKILL.md` | workflow: `workflow-marketing-copy.md` | contexts: `product-marketing-context.md`, `project-context.md` |

**skill-expert-positioning** is the authority positioning framework. Runs an 11-layer diagnostic system to convert submissive performer copy into practitioner-level expert copy. Restructures inquiry flows, CTAs, minimum level of engagements (MLE), and portfolios.

### ROUTING PRECEDENCE RULE (COLLISION RESOLUTION)

If a task contains trigger words that map to multiple operating modes simultaneously:
1. **Storytelling Mode & Cinematic Motion Mode** always override standard **Builder Mode** or **Designer Mode**.
2. **Security Mode & Performance Mode** always override standard **Builder Mode** or **Reviewer Mode**.
3. **Product/Inception Mode** always overrides generic **Builder Mode** triggers.
4. **Brand Diagnostics Mode** always overrides generic **Designer Mode** when the task involves brand auditing, positioning diagnostics, or perception analysis.
5. **Expert Positioning Mode** always overrides standard **Marketer Mode** or **Designer Mode** when the task involves copy auditing, CTA qualification, or positioning critiques.
*Example:* A request to "implement a scroll animation using GSAP" contains standard builder words ("implement") and cinematic motion words ("GSAP", "animation"). Under this rule, standard Builder Mode is bypassed; **Cinematic Motion Mode** is activated and loads `skill-cinematic-motion`.

---

## COGNITIVE ENGINE DEEP-LOADING

The core reasoning principles are always active via `GEMINI.md`. Load the FULL `core/` reference files beyond the compressed version when:

| Trigger | Load |
|:---|:---|
| Type 1 (irreversible) decisions | Both full files |
| Multi-component or multi-service tasks | `system-thinking.md` |
| Recurring bugs or persistent issues | Both full files |
| Pre-mortem required | `expert-cognitive-patterns.md` |
| Architecture or schema design | `system-thinking.md` |
| High-stakes creative direction (brand, spatial) | Both full files |

---

## RUNTIME ASSEMBLY PROTOCOL

When a task arrives:

1. **Classify task** — determine mode, task type, risk level
2. **Classify decision** — determine Type 1/1.5/2 using the Cognitive Engine before selecting skills or workflows
3. **Skill selection** — 1 primary + 0–2 secondary (only when task genuinely spans domains)
4. **Workflow selection** — 1 workflow for multi-step work
5. **Context selection** — start with 1–2 files, expand only if required
6. **Support layers** — templates when producing structured output; memory when history matters

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

> [!CAUTION]
> The files in this global `contexts/` folder are **authoring templates only**. Never write project-specific values into them. During project inception, copy the relevant templates into the active workspace's local `contexts/` directory and populate the copies. The global templates must remain blank scaffolds for future projects.

| Context File | Load When |
| :--- | :--- |
| `stack-context.md` | Any coding, building, or debugging task |
| `architecture-context.md` | Architecture, debugging complex issues |
| `coding-standards.md` | Building, reviewing, refactoring |
| `PRODUCT.md` (project root) | All UI/UX work — strategic design context (register, brand, anti-references) |
| `DESIGN.md` (project root) | All UI/UX work — visual system (tokens, typography, colors, components) |
| `security-baselines.md` | Security, auth, review |
| `infra-context.md` | DevOps, performance, deployment |
| `project-context.md` | Project inception, new feature scoping |
| `product-marketing-context.md` | Copywriting, marketing, sales strategy |
| `domain-rules.md` | Business logic tasks |
| `database-context.md` | Database design, query optimization |
| `story.md` (contexts/) | Storytelling — narrative arc, emotional journey, copy/visual/motion direction. Created by skill-storytelling. Drives all design and animation decisions. |
| `research-brief.md` (contexts/) | Research — brand, audience, competition, context. Created during inception Phase 3A Step 3. |
| `motion-direction.md` (contexts/) | **Scroll & cinematic motion only** — emotion diagnosis, archetype, motion vocabulary, scroll narrative (hook→build→climax→resolve), GSAP ScrollTrigger pattern selection per section, asset requirements. Created by visual brainstorm Phase 3C. Consumed by /impeccable-animate. Does NOT hold micro-interaction tokens (those belong in DESIGN.json). |

> **Motion boundary rule:** If both `DESIGN.json` and `motion-direction.md` are loaded, `motion-direction.md` is authoritative for all scroll-driven, narrative, and cinematic animation. `DESIGN.json` extensions.motion is authoritative only for state-change micro-interactions (hover, focus, open/close, toggle). Neither file may define tokens in the other's domain.

---

## FOLDER INTERACTION MAP

```text
GEMINI.md + GLOBAL_MEMORY.md
  → skills/ (domain behavior)
    → contexts/ (grounds skill in project reality)
      → workflows/ (sequences the work)
        → global_templates/ (shapes deliverables)
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
6. Lean loading beats heavy loading — always.

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
| `build-feature` | P1_Objective → P2_Grounding → P3_Scope → P4_Risks → P5_Design → P6_Verification → P7_Implementation → P8_Memory_Capture |
| `debug-issue` | observe_symptoms → reproduce → isolate → hypothesize → verify_cause → fix → verify_fix → regression_check → document → post_ship |
| `design-ui` | user_goals → information_architecture → component_inventory → state_coverage → visual_design → implement → accessibility → verify → deliver → post_ship |
| `impeccable-animate` | detect_context → select_vocabulary → plan_strategy → plan_assets → implement → iterate → verify → critique → deliver |
| `impeccable-teach` | interview → scan_codebase → draft_product_md → deliver |
| `impeccable-document` | gather_visual_signals → extract_tokens → draft_design_md → deliver |
| `storytelling` | load_context → present_directions → develop_direction → present_for_approval → lock_and_write |
| `plan-architecture` | understand_requirements → identify_constraints → enumerate_options → evaluate_tradeoffs → make_decision → document_adr → communicate |
| `project-inception` | initialize_state → discover_problem → define_mvp → technical_direction → design_identity_visual_system → create_runtime_contexts → initialize_workspace_memory → create_build_sequence → package_north_star |
| `marketing-copy` | context_gathering → psychology_alignment → drafting → refinement → delivery |

---

## USER'S TECH STACK PREFERENCES

- **Logic:** TypeScript 7.0 (Native) via `tsgo`
- **Motion Stack:**
  - Product register (UI micro-interactions, component transitions, dialogs): `motion` package (modern Framer Motion). Mandatory.
  - Brand register (scroll-driven storytelling, cinematic reveals, parallax, 3D): GSAP + ScrollTrigger. Primary tool for brand surfaces.
  - Both may coexist in the same project.
- **Standard:** Production-quality polish and motion-first UI by default.
