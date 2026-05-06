# README — CORE FOLDER

**Location:** `.antigravity/core/`
**Layer:** 1-4 + Governance
**Loading Tier:** 1 — **ALWAYS LOADED**

***

## PURPOSE

This folder IS Anti-Gravity's permanent brain. These files define WHO
the AI is, HOW it thinks, WHICH mode it operates in, and WHAT standards
it holds itself to. They are active in EVERY conversation, EVERY task,
EVERY mode — without exception.

If Anti-Gravity were a person, this folder would be their personality,
education, values, and professional discipline combined.

If `skills/` define domain expertise, `core/` defines the mind that
governs all of them. Without this folder, the rest of the repository
becomes fragmented expertise without a stable operating system.

***

## INVENTORY

| # | File | Layer | Role | One-Line Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [anti-gravity-core.md](file:///C:/Users/Oviks/.gemini/antigravity/core/anti-gravity-core.md) | L1 — Identity | WHO it is | Constitution: identity, principles, non-negotiables, principles, and philosophy |
| 2 | [system-thinking.md](file:///C:/Users/Oviks/.gemini/antigravity/core/system-thinking.md) | L2 — Cognition | WHAT to think about | Boundaries, dependencies, flows, loops, and tradeoff reasoning |
| 3 | [expert-cognitive-patterns.md](file:///C:/Users/Oviks/.gemini/antigravity/core/expert-cognitive-patterns.md) | L3 — Meta-Cognition | HOW to guard thinking | Meta-cognitive safeguards, bias framing, and probabilistic thinking |
| 4 | [operating-modes.md](file:///C:/Users/Oviks/.gemini/antigravity/core/operating-modes.md) | L4 — Posture | WHICH mode to activate | Available postures (PLANNING/EXECUTION/VERIFICATION) and overrides |
| 5 | [activation-engine.md](file:///C:/Users/Oviks/.gemini/antigravity/core/activation-engine.md) | L7 — Orchestration | WHICH files to load | Task routing, skill/context/workflow loading maps, and context rules |
| 6 | [execution-workflow.md](file:///C:/Users/Oviks/.gemini/antigravity/core/execution-workflow.md) | L8 — Process | WHAT steps to follow | Universal 8-phase task processing sequence |
| 7 | [communication-standards.md](file:///C:/Users/Oviks/.gemini/antigravity/core/communication-standards.md) | L9 — Delivery | HOW to communicate | Tone, reasoning visibility, actionability, and tradeoff communication |
| 8 | [conflict-resolution.md](file:///C:/Users/Oviks/.gemini/antigravity/core/conflict-resolution.md) | L9 — Tradeoffs | HOW to resolve tensions | Priority hierarchy and common conflict patterns (Speed vs Quality) |
| 9 | [quality-bar.md](file:///C:/Users/Oviks/.gemini/antigravity/core/quality-bar.md) | L10 — Standards | WHAT "good enough" means | Quality tiers, universal standards, and mandatory quality gates |
| 10 | [workflow-state-tracker.md](file:///C:/Users/Oviks/.gemini/antigravity/core/workflow-state-tracker.md) | L8 — Persistence | HOW to resume work | Workflow state persistence across sessions via JSON state files |

***

## LOADING RULES

**ALL files in this folder are Tier 1 — always loaded.** They form the
permanent operating system kernel. The master system prompt contains a
compressed version. When deeper reasoning is needed, read the full files
from this directory.

### UNLOADING POLICY

**Never unload these files.** They govern every other file in the system.

If a task must drop context due to budget pressure, `core/` should be
the last thing dropped.

***

## WHAT THIS FOLDER ANSWERS

- Who is Anti-Gravity?
- What should it always care about?
- How should it think structurally?
- How should it avoid bad reasoning under uncertainty?
- Which mode should be active?
- How should work proceed?
- How are tradeoffs resolved?
- How should answers be delivered?
- What counts as good enough?

***

## WHAT LIVES HERE

Core files define stable, reusable, cross-domain behavior.

### Belongs in `core/`

- Universal reasoning rules
- General operating modes and posture discipline
- Cognitive and decision discipline
- Conflict handling rules
- Communication standards that apply across all work
- The minimum quality bar for any result

### Does not belong in `core/`

- Project-specific assumptions
- Runtime stack specifics
- One-off implementation notes
- Task-local procedures — those belong in `workflows/`
- Domain-specific expertise — that belongs in `skills/`
- Project-specific reality — that belongs in `contexts/`

***

## INTERACTION WITH OTHER FOLDERS

| Folder | Relationship |
| :--- | :--- |
| `skills/` | Skills inherit from core. Skills extend core — they do not contradict it. If a skill file conflicts with core, **CORE WINS.** |
| `contexts/` | Contexts ground core principles in project reality. Core provides the rules, contexts provide the facts. |
| `workflows/` | Workflows sequence and specialize the 8-phase process defined in `execution-workflow.md`. |
| `templates/` | Templates implement the output contracts and structure standards defined in `communication-standards.md`. |
| `rubrics/` | Rubrics implement and deepen the quality standards defined in `quality-bar.md` for specific domains. |

***

## HIERARCHY RULE

**This folder is the highest authority in the system.** If ANY file in
ANY other folder contradicts a file in this folder, the core file wins.

The ONLY exception: an explicit user override AFTER the conflict has
been surfaced and the user has acknowledged the tradeoff.

No skill should contradict the core layer without an explicit
contextual override.

***

## QUALITY BAR FOR FILES IN THIS FOLDER

A strong `core/` file:

- Has a unique role — no overlap with sibling files.
- Is stable and universal — applies across projects and domains.
- Is behavioral — tells the system how to act, not just what to know.
- Is concise — these files are always loaded, every word costs tokens.
- Improves reasoning quality across many tasks.
- Contains behavior-changing rules, not generic philosophy.
- Justifies always-on status.

***

## MAINTENANCE

These files change ONLY when the fundamental operating philosophy changes.

Expected frequency: one to two updates per quarter at most.

Any change to a core file should be treated as a Type 1 decision —
high-stakes, potentially hard to reverse, requiring careful analysis
before committing.

***

## FINAL RULE

`core/` defines how Anti-Gravity thinks before it specializes.
`core/` should make Anti-Gravity dependable even before any
specialized file is loaded.

If this folder is weak, the whole system becomes inconsistent.
