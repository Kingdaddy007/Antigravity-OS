---
name: workflow-impeccable-craft
description: Build an approved interior or spatial website in coherent, verifiable slices
id: impeccable-craft
version: 2
status: active
intent: Expand a passed vertical slice into full production without losing concept continuity, proof, usability, or restraint.
use_when: [a spatial vertical slice has an expand verdict and full production is authorized]
do_not_use_when: [concept discovery, missing production contract, failed vertical slice, general product UI, or backend-only work]
inputs: [five core artifacts or approved equivalents, expand verdict, implementation stack, real or realistic assets]
required_resources: [applicable AGENTS.md files, spatial-experience-design, ui-ux, coding guidance, exact specialist references needed by the build]
mutation_class: local_edit
approval_gates: [expand verdict, scope changes, new heavy dependencies, slice critique, final Director and user approval]
states: [contract-check, slice-plan, static-build, assets, systems, interactions, critique, verify, deliver]
outputs: [implementation, per-slice evidence, verification report, changed-artifact list, residual risks]
verification: [browser and automated checks proportionate to risk, accessibility, responsive composition, performance, fallbacks, proof, inquiry, concept continuity]
failure_paths: [stop the affected slice, return to the earliest invalidated contract, preserve working state, report safe next action]
resume_contract: task-scoped .agents/workflows/impeccable-craft.json using the workflows directory contract
next_workflows: [impeccable-animate, verify-project]
profiles: [spatial]
---

# WORKFLOW: SPATIAL CRAFT

## ENTRY GATE

Do not begin broad production until:

- the five core contracts or approved equivalents exist;
- the selected concept and production contract are approved;
- the risk prototype is resolved;
- the representative vertical slice has an `expand` verdict;
- implementation authority is explicit.

Legacy context sets are valid when mapped to these logical contracts. Conditional files are required only when their corresponding feature exists.

## LOAD PURPOSEFULLY

Always load `spatial-experience-design` and `ui-ux`. Load cinematic motion, showroom strategy, scroll storyboard, prompt guidance, portfolio proof, material recipes, scene-kit guidance, or advanced rendering references only when the approved plan requires them. Do not load every spatial reference by default.

## BUILD IN COHERENT SLICES

Plan slices around complete visitor responsibilities rather than technical layers. A slice should connect semantic structure, content, image, proof, responsive behavior, accessibility, and applicable interaction.

Examples: opening plus first argument; representative project proof; material/process chapter; method and fit; selective inquiry. The actual order follows `experience-blueprint.md`.

For each slice:

1. Restate its chapter job and acceptance evidence.
2. Build semantic static structure first.
3. Integrate real or realistic-enough content and assets.
4. Apply type, color, crop, material, density, and layout rules.
5. Add interaction and approved motion only after the still composition works.
6. Verify desktop, tablet, mobile, keyboard, focus, loading, errors, and fallbacks.
7. Run a focused Director critique and resolve higher-level failures before polish.

## ASSET BOUNDARIES

- **Image-native:** use real, rendered, or approved generated imagery with crop and alt-text rules; do not replace rooms or materials with CSS shapes.
- **CSS-native:** use semantic, responsive layout and material treatments.
- **SVG-native:** keep editable geometry and accessible labels where needed.
- **Canvas/WebGL-native:** require approved prototype evidence, loading budget, lifecycle, mobile fallback, and reduced-motion equivalent.

If a blocking asset is missing, use only an explicitly approved stand-in that tests the same composition and clearly record replacement work.

## CONCEPT CONTINUITY AUDIT

After each slice verify:

- the controlling argument is still legible;
- adjacent chapters have intentional relationships;
- proof is specific and not buried by atmosphere;
- visual decisions trace to the selected territory;
- motion has a named job or is removed;
- inquiry remains visible, selective, and usable;
- the implementation has not drifted toward a generic decorator template.

Major drift returns to the earliest gate whose assumption changed. Do not silently redesign during production.

## FINAL VERIFICATION

Verify semantic structure, accessibility, responsive composition, crop integrity, contrast, keyboard/focus states, media controls, reduced motion, loading/failure states, performance budgets, navigation, proof comprehension, inquiry completion, and concept continuity. Record raw evidence and anything not verified.

Use `master-design-director` for the final audit. Resolve strategy and experience failures before composition, system, and polish issues.

## QUALITY GATE

- [ ] Vertical slice had an `expand` verdict.
- [ ] Work was built and critiqued in coherent slices.
- [ ] Still composition works before motion.
- [ ] Assets respect their implementation boundaries.
- [ ] Proof and inquiry remain clear and accessible.
- [ ] Desktop, tablet, mobile, and reduced-motion behavior are verified.
- [ ] No major deviation bypassed its originating gate.
- [ ] Final Director and user approval remain pending until evidence is presented.
