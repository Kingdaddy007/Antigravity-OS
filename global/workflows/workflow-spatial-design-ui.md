---
name: workflow-spatial-design-ui
description: Convert an approved spatial experience blueprint into responsive UI systems, a risk prototype, and a representative vertical slice
id: spatial-design-ui
version: 2
status: active
intent: Resolve spatial website structure and UI behavior before broad production while preserving usability, proof, and inquiry.
use_when: [a spatial concept is selected and an approved experience blueprint needs production-ready UI architecture or prototyping]
do_not_use_when: [concept discovery, general product UI, backend-only work, or broad production before the vertical-slice gate]
inputs: [five core artifacts or approved equivalents, selected concept, asset constraints, implementation authority]
required_resources: [applicable AGENTS.md files, spatial-experience-design, ui-ux, master-design-director]
mutation_class: local_edit
approval_gates: [experience blueprint approved, production contract approved, vertical-slice verdict]
states: [contract-check, ui-map, systemize, risk-prototype, vertical-slice, audit, handoff]
outputs: [UI architecture in experience-blueprint.md, production-plan.md, optional DESIGN files, prototype evidence, vertical slice, residual risks]
verification: [desktop and mobile composition, accessibility, proof and inquiry usability, concept continuity, prototype verdict]
failure_paths: [return to experience architecture or concept selection at the earliest invalid assumption]
resume_contract: task-scoped .agents/workflows/spatial-design-ui.json using the workflows directory contract
next_workflows: [impeccable-craft, impeccable-animate]
profiles: [spatial]
---

# WORKFLOW: SPATIAL DESIGN UI

## PURPOSE

Translate approved experience architecture into a usable, responsive interface and test the riskiest assumption before full production. Spatial character and cinematic ambition never override navigation, evidence, accessibility, performance, or inquiry.

## ENTRY GATE

Confirm the five core contracts or approved equivalents exist and the concept-selection plus experience gates are approved. Conditional artifacts are required only when their feature is present.

Load:

- `skills/spatial-experience-design/SKILL.md`;
- `skills/ui-ux/SKILL.md`;
- `skills/master-design-director/SKILL.md`;
- `skills/cinematic-motion/SKILL.md` only when approved motion is non-trivial;
- exact spatial/UI references that answer current implementation questions.

## COGNITIVE ENGINE CHECKPOINT

UI architecture and the vertical-slice decision are Type 1.5. Load `core/system-thinking.md`, `core/expert-cognitive-patterns.md`, and `core/first-principles.md` before expanding production. Map the dependency chain between navigation, proof, inquiry, media, mobile composition, accessibility, performance, and maintenance. Distinguish a real visitor requirement from a familiar UI convention. Challenge the riskiest assumption with the smallest reversible prototype, and document the second-order cost if that assumption fails after several slices are built.

## EXECUTION

### 1. Map UI Responsibilities

Define semantic chapter structure, navigation, project/gallery browsing, proof presentation, inquiry path, forms and states, errors, responsive intent, keyboard behavior, focus, media controls, loading states, and reduced-motion behavior.

### 2. Define Visual and Asset Systems

Record type, color, composition, crop, material, density, image hierarchy, text-safe zones, asset boundaries, placeholders, and fallback rules in `experience-blueprint.md` and `production-plan.md`. Create `DESIGN.md` / `DESIGN.json` only when implementation needs token and component contracts.

### 3. Identify the Riskiest Assumption

Examples: unusual opening comprehension, before/after interaction, responsive crop, pinned proof sequence, generated-media continuity, type over imagery, WebGL performance, or an inquiry transition. Prototype the smallest test that can invalidate it.

### 4. Build a Representative Vertical Slice

With implementation authority, create one coherent sequence that includes:

- real or realistic-enough imagery and copy;
- actual typography hierarchy;
- desktop and mobile behavior;
- proof or inquiry responsibility;
- signature motion only when approved;
- reduced-motion and fallback behavior where relevant.

Do not build the entire site to discover that its governing system fails.

### 5. Director Verdict

Use the Risk Prototype and Vertical-Slice Gate. Record one verdict in `production-plan.md`: `expand`, `revise`, `simplify`, or `return to concept`. State evidence, affected assumptions, and required changes.

### 6. Handoff

Only `expand` permits broad production. `Revise` repeats the slice; `simplify` updates the system and retests material risk; `return to concept` returns to the selection record without concealing sunk cost.

## QUALITY GATE

- [ ] UI follows the approved concept and chapter jobs, not a fixed spatial sequence.
- [ ] Navigation, proof, inquiry, forms, and all states are usable and accessible.
- [ ] Desktop and mobile are composed intentionally.
- [ ] Optional media and motion have fallbacks.
- [ ] The riskiest assumption was tested directly.
- [ ] The vertical slice uses real-enough content.
- [ ] Director verdict is recorded before broad production.
