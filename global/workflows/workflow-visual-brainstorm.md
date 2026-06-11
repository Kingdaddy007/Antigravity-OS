---
name: workflow-visual-brainstorm
description: Route visual exploration for high-end interior storytelling websites
---

# WORKFLOW: VISUAL BRAINSTORM

## WHAT THIS WORKFLOW DOES

Route visual exploration for high-end interior storytelling websites through `workflow-spatial-concept.md`. Do not generate generic color, typography, or Stitch-style direction options before the spatial concept artifacts exist.

## ACTIVATION

Use when:

- The user asks to explore visual direction for an interior decorator, spatial studio, showroom, decor, furniture, gallery, or luxury home website.
- The user asks for mockups, visual brainstorms, premium direction, or "make it look like a 20k site."

Do NOT use when:

- The task is backend/API/security/database/DevOps.
- A complete spatial concept already exists and the task is implementation.

## REQUIRED FILES

Load:

- `workflows/workflow-spatial-concept.md`
- `skills/spatial-experience-design/SKILL.md`
- `skills/storytelling/SKILL.md`
- `skills/cinematic-motion/SKILL.md` when motion is involved
- `skills/spatial-experience-design/reference/audit-mechanics-map.md`
- `skills/spatial-experience-design/reference/scene-kit-and-asset-directive.md`

## EXECUTION SEQUENCE

### STEP 1: Check Spatial Artifacts

Look for:

- `contexts/spatial/visual-thesis.md`
- `contexts/spatial/anti-template-preflight.md`
- `contexts/spatial/room-sequence.md`
- `contexts/spatial/audit-adaptation-map.md`
- `contexts/spatial/beloved-asset-directive.md`
- `contexts/spatial/hero-event-blueprint.md`
- `contexts/spatial/scene-kit-brief.md`
- `contexts/spatial/depth-map.md`
- `contexts/spatial/material-script.md`
- `contexts/spatial/motion-board.md`
- `contexts/spatial/asset-boundary.md`

If any are missing, run `workflow-spatial-concept.md` first.

Gate: Do not create visual options until the spatial contract exists.

### STEP 2: Generate Direction Options From The Contract

> **⚙ Cognitive Engine checkpoint — apply cognitive safeguards.**
> Gray thinking: explore genuinely different visual territories, not safe variations of one idea. Framing bias: restate the visual problem from the visitor's emotional journey, not just the brand's intent. Anti-comfort: if one direction feels obvious, that's a signal to push harder on alternatives. First principles: what is provably true about how this space should feel, stripped of convention?
Create 2-3 options only within the approved visual thesis. Options may vary:

- archetype emphasis
- hero event treatment
- room sequence pacing
- material/light emphasis
- scene kit intensity
- motion restraint

Do not present palette-only variants.

### STEP 3: Check Against Anti-Template Smells

For each option, state:

- Why it cannot be mistaken for a generic decorator template.
- Which design-audit mechanics it adapts.
- Which image-native assets it depends on.
- Which motion track carries the signature experience.
- Which parts remain quiet for proof and inquiry.

### STEP 4: Lock Direction

Record the chosen direction by updating or creating:

- `contexts/spatial/selected-direction.md`
- updates to scene kit, depth map, material script, and motion board if the selected direction changes them.

## QUALITY GATE CHECKLIST

- [ ] Spatial concept artifacts exist before visual options.
- [ ] Options differ by spatial idea, not only color.
- [ ] Each option names asset requirements.
- [ ] The selected direction updates the spatial contract.
- [ ] Template luxury patterns are rejected.
