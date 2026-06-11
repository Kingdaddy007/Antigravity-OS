---
name: workflow-spatial-concept
description: Create the pre-build creative contract for high-end interior storytelling websites
---

# WORKFLOW: SPATIAL CONCEPT

## WHAT THIS WORKFLOW DOES

Create the pre-build creative contract for high-end interior storytelling websites. Force the assistant to define the room sequence, visual thesis, scene kit, material script, motion tracks, and asset boundary before mockup or code.

Default journey:

`Atmosphere -> Taste -> Transformation -> Proof -> Method -> Inquiry`

## ACTIVATION

Use when:

- Starting or redesigning an interior decorator, interior designer, spatial studio, staging, furniture, decor, gallery, architecture-adjacent, or luxury home website.
- The user asks for a premium, cinematic, 20k-quality, emotionally attractive, spatial, portfolio, showroom, or design-studio web experience.
- A visual direction is open-ended and could fall into template luxury.

Do NOT use when:

- The task is backend, API, database, security, DevOps, or CLI work.
- The user only needs a small component polish task that does not affect spatial concept.

## REQUIRED FILES

Load:

- `skills/spatial-experience-design/SKILL.md`
- `skills/storytelling/SKILL.md`
- `skills/brand-strategy/SKILL.md` when positioning is unclear
- `skills/cinematic-showroom-strategy/SKILL.md` when the concept is cinematic, video-led, portfolio-led, or AI-prompted
- `skills/cinematic-motion/SKILL.md` when the concept includes motion
- `skills/spatial-experience-design/reference/audit-mechanics-map.md`
- `skills/spatial-experience-design/reference/concept-forge-questions.md`
- `skills/spatial-experience-design/reference/scene-kit-and-asset-directive.md`
- `skills/spatial-experience-design/reference/cinematic-room-grammar.md` when image/video prompts are needed
- `skills/spatial-experience-design/reference/portfolio-proof-chapters.md` when portfolio is central
- `skills/spatial-experience-design/reference/material-recipes.md` only when implementation recipes are needed
- `skills/cinematic-motion/reference/video-to-website-choreography.md` when video, canvas, or scroll-led media is involved
- `skills/cinematic-motion/reference/transition-library.md` when reveals or thresholds are involved
- `skills/cinematic-motion/reference/mobile-fallbacks.md` when media/motion is involved
- `skills/ui-ux/reference/spatial-ui-patterns.md`
- `codex/reference/hero-layout-blueprints.md` as the composition reference and styling tokens library
- `design-audit/` reports as the living visual/motion reference library

## EXECUTION SEQUENCE

### STEP 1: Diagnose The Lazy Default

Write `contexts/spatial/anti-template-preflight.md`.

Include:

- The generic layout a weak AI would build.
- Which Tidescape failure modes are present.
- Banned structures, components, fonts, colors, animation presets, and placeholder types.
- The "cannot be swapped to another industry" test.

Gate: Do not propose a direction until the lazy/default direction is named and banned.

### STEP 2: Name The Visual Thesis

> **⚙ Cognitive Engine checkpoint — load `core/expert-cognitive-patterns.md`.**
> This is a Type 1.5 creative decision. Apply gray thinking — generate 3 genuinely distinct concept directions, not 3 variations of the same idea. Apply anti-comfort safeguard — if one concept feels obviously right immediately, actively challenge it before presenting. Apply first-principles assumption audit — strip away convention and ask what is provably true about this brand's spatial identity.
Before writing the thesis, run a short concept forge with Beloved using `skills/spatial-experience-design/reference/concept-forge-questions.md`.

Ask only high-leverage questions about:

- sensation
- boring default to destroy
- signature object
- physical opening event
- asset reality

If Beloved is unsure, propose three mixed concepts:

1. safe-but-premium
2. strange-and-memorable
3. atelier masterpiece

Each option must cite audit mechanics from `design-audit/` and identify asset requirements.

Write `contexts/spatial/visual-thesis.md`.

Include:

- One physical sentence the site must obey.
- Primary archetype and optional secondary archetype.
- Signature room, object, material, or threshold.
- The feeling the first 5 seconds must create.

Gate: Reject adjective-only theses like "modern luxury" or "clean elegant".
Gate: Do not skip Beloved collaboration unless Beloved explicitly gives you a complete concept.

### STEP 3: Build The Room Sequence

Write `contexts/spatial/room-sequence.md`.

Use:

1. Atmosphere.
2. Taste.
3. Transformation.
4. Proof.
5. Method.
6. Inquiry.

For each chapter define:

- Room/space metaphor.
- Visitor emotion.
- Primary visual.
- Copy posture.
- Proof or decision shown.
- UI responsibility.

Gate: Services/pricing cannot appear before atmosphere, taste, and transformation proof unless the user explicitly asks for a utilitarian site.

### STEP 4: Translate Brand To Scene

> **⚙ Cognitive Engine checkpoint — apply system decomposition.**
> Define current perception state, desired spatial experience, and the gap between them. Map how each scene decision connects to the brand positioning established in Step 2. Check for framing bias — are you translating the brand the way it was presented, or have you re-examined it from the visitor's perspective?
Use `skills/cinematic-showroom-strategy/SKILL.md`.

Write `contexts/spatial/brand-to-scene-translation.md`.

Include:

- Perception gap.
- Desired visitor belief.
- Taste world.
- Enemy/cliche to reject.
- Spatial metaphor.
- First scene.
- Whole-site scene sequence.
- Prompt implications.
- Portfolio/proof implications.
- Inquiry implication.

Gate: Do not write final image/video prompts until this translation exists.

### STEP 5: Map Showroom Choreography

Use `skills/cinematic-motion/reference/video-to-website-choreography.md`.

Write `contexts/spatial/showroom-choreography.md`.

For every media-led section define:

- Journey stage.
- Belief/proof job.
- Primary room/object/material.
- Media type.
- Scroll behavior.
- Text zone.
- Reveal rhythm.
- Motion track.
- Portfolio/proof role.
- Fallback.
- Whether an asset prompt is required.

Gate: Video cannot be used as decorative background. It must carry atmosphere, threshold, taste, transformation, proof, method, or inquiry.

### STEP 6: Plan Portfolio Proof Chapters

Use `skills/spatial-experience-design/reference/portfolio-proof-chapters.md` when portfolio is central.

Write `contexts/spatial/portfolio-proof-chapters.md`.

For each project chapter define:

- Client/context.
- Room or space.
- Original problem.
- Design decision.
- Material/light move.
- Before/after or transformation proof.
- Cinematic media.
- Caption/proof text.
- Interaction.
- Inquiry relevance.

Gate: Do not approve a broad portfolio grid until at least one curated project chapter proves judgment.

### STEP 7: Cite Audit Mechanics

Use `skills/spatial-experience-design/reference/audit-mechanics-map.md`.

Update `contexts/spatial/visual-thesis.md` or create `contexts/spatial/audit-adaptation-map.md` with:

- 2-4 source audit mechanics.
- How each mechanic is adapted to the current interior/spatial concept.
- Which motion track each mechanic belongs to.
- Which assets each mechanic requires.
- Which Tidescape/template smell each mechanic prevents.

Gate: Do not present a concept that does not cite specific mechanics from `design-audit/`.

### STEP 8: Write Beloved's Asset Directive

Use `skills/spatial-experience-design/reference/scene-kit-and-asset-directive.md`.

Write `contexts/spatial/beloved-asset-directive.md`.

For every image-native, video-native, SVG-native, canvas/WebGL-native, or transparent layer requirement, specify:

- exact asset
- file path
- draft still image prompt requirement when needed
- draft video source-image prompt requirement when needed
- draft final video prompt requirement when needed
- camera angle
- subject movement
- camera movement
- lighting direction
- perspective
- blur/depth role
- text-safe zone
- whether the asset blocks build

Build Gate:

Pause here. Do not write final layout styling for image-native scenes until Beloved places the blocking assets in the specified folders or explicitly approves temporary stand-ins.

### STEP 9: Define The Hero Event

Write `contexts/spatial/hero-event-blueprint.md`.

Include:

- Composition Reference: Consult [hero-layout-blueprints.md](file:///c:/Users/godsw/ANTIGRAVITY%20%20WORKSPACE/inyenbong/codex/reference/hero-layout-blueprints.md) for layout formula or aesthetic reference (e.g., Split, Magazine, Annotated) and define how it is adapted or hybridized for this brand's visual thesis.
- Start state.
- Physical event.
- Transformation vector.
- Mask/reveal/threshold mechanics.
- Final state.
- Assets required.
- Reduced-motion alternative.

Examples: curtain split, mural reveal, door opening, light spill, fabric pull, room-to-room camera move, before/after reveal, object entrance.

### STEP 10: Specify The Scene Kit

Write `contexts/spatial/scene-kit-brief.md`.

Include:

- Required image-native assets.
- Camera angle, light direction, shadow, crop, and mobile crop.
- Foreground/midground/background assets.
- Text-safe zones.
- Accepted temporary placeholders.
- Forbidden placeholders.

Gate: If a concept depends on rooms, furniture, murals, textiles, stone, or real material surfaces, do not approve CSS-only placeholders as final.

### STEP 11: Map Depth And Material

Write:

- `contexts/spatial/depth-map.md`
- `contexts/spatial/material-script.md`

Depth map must name all Z layers, overlap rules, pointer-events, text-safe zones, and mobile simplification.

Material script must name dominant materials, light behavior, surface finish, texture evidence, and how color is derived from material/light.

### STEP 12: Plan Motion And Asset Boundary

Write:

- `contexts/spatial/motion-board.md`
- `contexts/spatial/asset-boundary.md`

Motion board must separate:

- Arrival.
- Ambient.
- Scroll-bound.
- Interaction.

Asset boundary must classify each important element as:

- image-native
- CSS-native
- SVG-native
- canvas/WebGL-native

Gate: No motion or implementation begins until these classifications exist.

### STEP 13: Write Cinematic Prompt Pack

Use:

- `skills/cinematic-showroom-strategy/SKILL.md`
- `skills/spatial-experience-design/reference/cinematic-room-grammar.md`
- `skills/spatial-experience-design/reference/scene-kit-and-asset-directive.md`
- `skills/cinematic-motion/reference/video-to-website-choreography.md`

Write `contexts/spatial/cinematic-prompt-pack.md` when image-native or video-native assets are generated.

The prompt pack is not a standalone prompt dump. It is a downstream strategy artifact generated only after reading the approved context chain.

Start with `Context Inheritance` listing the approved context files used:

- `contexts/brand-diagnostics.md`
- `contexts/spatial/spatial-story.md`
- `contexts/spatial/visual-thesis.md`
- `contexts/spatial/room-sequence.md`
- `contexts/spatial/brand-to-scene-translation.md`
- `contexts/spatial/showroom-choreography.md`
- `contexts/spatial/portfolio-proof-chapters.md`
- `contexts/spatial/hero-event-blueprint.md`
- `contexts/spatial/scene-kit-brief.md`
- `contexts/spatial/material-script.md`
- `contexts/spatial/depth-map.md`
- `contexts/spatial/motion-board.md`
- `contexts/spatial/asset-boundary.md`

Every image/video prompt must include a `Strategic Source` block:

- Perception goal.
- Taste world.
- Section / journey stage.
- Desired visitor belief.
- Visual thesis connection.
- Room / material / object source.
- Motion role.
- Website placement.
- Text-safe requirement.
- Enemy / cliche rejected.

Gate: If a prompt cannot trace its choices back to approved context files, reject and rewrite it.
Gate: Reject prompts that say only "luxury room", "cinematic interior", "modern elegant", or any generic styling without light, camera, depth, belief, and section role.

### STEP 14: Present The Creative Contract

> **⚙ Cognitive Engine checkpoint — run self-evaluation.**
> Before presenting: check for over-simplification, binary thinking, and comfort bias across all prior steps. Verify second-order effects of the overall creative direction. Ask: if this creative contract fails in 6 months, what went wrong? (Pre-mortem.)
Summarize:

- Visual thesis.
- Audit mechanics being adapted.
- Primary archetype.
- Room sequence.
- Brand-to-scene translation.
- Showroom choreography.
- Portfolio proof chapters when relevant.
- Cinematic prompt pack when relevant.
- Beloved's Asset Directive and blocked assets.
- Hero event.
- Scene kit.
- Depth/material rules.
- Motion tracks.
- Asset boundary and blockers.

Ask for approval or revisions before build.

## QUALITY GATE CHECKLIST

- [ ] `anti-template-preflight.md` exists.
- [ ] `visual-thesis.md` exists and is physical/spatial.
- [ ] `room-sequence.md` follows Atmosphere -> Taste -> Transformation -> Proof -> Method -> Inquiry.
- [ ] `brand-to-scene-translation.md` translates positioning into scenes.
- [ ] `showroom-choreography.md` maps media, text, scroll, proof, and fallback.
- [ ] `cinematic-prompt-pack.md` includes Context Inheritance and Strategic Source blocks when prompts are needed.
- [ ] `portfolio-proof-chapters.md` exists when portfolio is central.
- [ ] `audit-adaptation-map.md` or equivalent audit citations exist.
- [ ] `beloved-asset-directive.md` exists and states blocking assets.
- [ ] `hero-event-blueprint.md` defines a physical opening event.
- [ ] `scene-kit-brief.md` identifies image-native requirements.
- [ ] `depth-map.md` defines Z-axis layers.
- [ ] `material-script.md` defines materials and light behavior.
- [ ] `motion-board.md` separates arrival, ambient, scroll-bound, interaction.
- [ ] `asset-boundary.md` classifies all major elements.
- [ ] The concept fails the template swap test.
