---
name: workflow-project-inception
description: Turn a new high-end interior storytelling website idea into buildable spatial context
---

# WORKFLOW: PROJECT INCEPTION

## WHAT THIS WORKFLOW DOES

Turn a new high-end interior storytelling website idea into buildable spatial context. For interior decorators, spatial studios, furniture/decor showrooms, galleries, architecture-adjacent studios, and luxury home brands, route visual planning through the spatial experience system before technical build work.

Default journey:

`Atmosphere -> Taste -> Transformation -> Proof -> Method -> Inquiry`

## ACTIVATION

Use when:

- Starting a new interior decorator, interior design, spatial studio, staging, furniture, decor, gallery, architecture-adjacent, or luxury home website.
- Turning a rough premium website idea into a build plan.
- Creating first project contexts for a visual/spatial brand.

Do NOT use when:

- Adding a small feature to an already-planned project.
- Debugging an existing implementation.
- Doing backend/API/security/database/DevOps-only work.

## REQUIRED FILES

Load:

- `skills/brand-strategy/SKILL.md`
- `skills/storytelling/SKILL.md`
- `skills/spatial-experience-design/SKILL.md`
- `skills/cinematic-showroom-strategy/SKILL.md`
- `skills/ui-ux/SKILL.md`
- `workflows/workflow-spatial-concept.md`
- `skills/spatial-experience-design/reference/audit-mechanics-map.md`
- `skills/spatial-experience-design/reference/scene-kit-and-asset-directive.md`
- `skills/spatial-experience-design/reference/cinematic-room-grammar.md` when image/video prompts are needed
- `skills/spatial-experience-design/reference/portfolio-proof-chapters.md` when portfolio is central
- `skills/cinematic-motion/reference/video-to-website-choreography.md` when scroll-led media is involved
- `design-audit/` when premium inspiration is needed

## EXECUTION SEQUENCE

### PHASE 1: DEFINE THE SPATIAL BUSINESS PROBLEM

Capture:

- brand/studio type
- audience and desired client
- price/perception goal
- current or intended taste world
- existing assets and missing assets
- inquiry goal
- wrong-fit clients

Output:

- `contexts/project-context.md`
- `contexts/brand-diagnostics.md` when positioning is unclear

Gate: Do not discuss features before the brand perception and inquiry goal are clear.

### PHASE 2: DIAGNOSE POSITIONING AND STORY

> **⚙ Cognitive Engine checkpoint — load `core/system-thinking.md` + `core/expert-cognitive-patterns.md`.**
> This phase contains the highest-stakes creative and strategic decisions. Apply system decomposition to diagnose current brand state vs desired positioning. Apply gray thinking and framing bias safeguards when evaluating brand tension and audience self-image. Generate 3+ positioning directions with explicit tradeoffs before selecting. Classify each major decision as Type 1, 1.5, or 2 and invest the appropriate depth.
Use `brand-strategy` and `storytelling`.

Create:

- `contexts/spatial/spatial-story.md`
- `contexts/spatial/brand-to-scene-translation.md` when the project is cinematic, video-led, or portfolio-led

It must include:

- visual thesis input
- audience self-image
- brand tension
- entry room
- threshold event
- signature object/material
- room sequence
- transformation proof
- method reveal
- inquiry posture

`brand-to-scene-translation.md` must include:

- perception gap
- desired visitor belief
- taste world
- enemy/cliche to reject
- spatial metaphor
- first scene
- whole-site scene sequence
- prompt implications
- portfolio/proof implications
- inquiry implication

Gate: Do not create DESIGN tokens before the spatial story exists.

### PHASE 3: RUN SPATIAL CONCEPT

Run `workflow-spatial-concept.md`.

Required outputs:

- `contexts/spatial/anti-template-preflight.md`
- `contexts/spatial/visual-thesis.md`
- `contexts/spatial/room-sequence.md`
- `contexts/spatial/brand-to-scene-translation.md`
- `contexts/spatial/audit-adaptation-map.md`
- `contexts/spatial/showroom-choreography.md`
- `contexts/spatial/portfolio-proof-chapters.md` when portfolio is central
- `contexts/spatial/cinematic-prompt-pack.md` when image/video prompts are needed
- `contexts/spatial/beloved-asset-directive.md`
- `contexts/spatial/hero-event-blueprint.md`
- `contexts/spatial/scene-kit-brief.md`
- `contexts/spatial/depth-map.md`
- `contexts/spatial/material-script.md`
- `contexts/spatial/motion-board.md`
- `contexts/spatial/asset-boundary.md`

Gate: No mockup, design system, or implementation until these exist.

### PHASE 4: DEFINE THE VISUAL SYSTEM

Create or update:

- `DESIGN.md`
- `DESIGN.json`

Tokens must derive from:

- material script
- light behavior
- room sequence
- typography posture
- UI/inquiry model

Do not derive the palette from generic color preference.

### PHASE 5: PLAN BUILD ORDER

Build order:

1. Project setup and asset folders.
2. Scene choreography and prompt pack.
3. Video/still asset generation or sourcing.
4. Static semantic room sequence.
5. Scene kit integration and responsive crops.
6. Material/light styling.
7. Gallery/project/proof sections.
8. Inquiry path and states.
9. Motion tracks via `workflow-impeccable-animate.md`.
10. Browser verification and anti-template critique.

### PHASE 6: PACKAGE THE NORTH STAR

Deliver:

- spatial story summary
- visual thesis
- room sequence
- brand-to-scene translation
- showroom choreography
- cinematic prompt pack when media is generated
- portfolio proof chapters when portfolio is central
- scene kit requirements
- asset boundary
- build order
- verification checklist

## QUALITY GATE CHECKLIST

- [ ] Brand perception and inquiry goal are clear.
- [ ] `spatial-story.md` exists.
- [ ] Cinematic/video-led projects include brand-to-scene translation, showroom choreography, and prompt pack.
- [ ] Prompt pack derives from approved context files, not standalone inspiration.
- [ ] All spatial concept artifacts exist.
- [ ] DESIGN files derive from material/light/room sequence.
- [ ] Build order uses spatial craft and animate workflows.
- [ ] Backend/API/security/database concerns are not mixed into visual planning.
