---
name: workflow-impeccable-animate
description: Plan and implement motion for high-end interior storytelling websites
id: impeccable-animate
version: 1
status: active
intent: Execute impeccable animate with explicit authority, state, outputs, and evidence.
use_when: [the task matches impeccable animate]
do_not_use_when: [another workflow more precisely matches the requested outcome]
inputs: [user objective, workspace context, constraints, requested authority mode]
required_resources: [applicable AGENTS.md files, referenced skills and contexts]
mutation_class: local_edit
approval_gates: [confirm scope expansion or destructive action before mutation]
states: [intake, assess, propose, approve-if-needed, execute-if-authorized, verify, deliver]
outputs: [task result, changed-artifact list when applicable, evidence, residual risks]
verification: [run proportionate checks, record raw evidence, label anything unverified]
failure_paths: [stop on authority or contract conflict, preserve state, report blocker and safe next action]
resume_contract: task-scoped .agents/workflows/impeccable-animate.json using the workflows directory contract
next_workflows: [none]
profiles: [spatial]
---

# WORKFLOW: SPATIAL ANIMATE

## WHAT THIS WORKFLOW DOES

Plan and implement motion for high-end interior storytelling websites using four tracks: arrival, ambient, scroll-bound, and interaction. Motion must come from the room, material, threshold, object, proof, or inquiry logic.

## ACTIVATION

Use when:

- Adding GSAP, ScrollTrigger, parallax, image sequence, canvas, WebGL, before/after reveal, stacked panels, or cinematic transitions to a spatial/interior website.
- A spatial concept includes a hero event, scene kit, depth map, or material transition.

Do NOT use when:

- Motion is decorative only.
- The spatial concept artifacts are missing.
- The task is backend/API/security/database/DevOps.

## REQUIRED FILES

Load:

- `skills/cinematic-motion/SKILL.md`
- `skills/spatial-experience-design/SKILL.md`
- `skills/cinematic-showroom-strategy/SKILL.md` when video-led or showroom choreography is present
- `skills/cinematic-motion/reference/gsap-cookbook.md`
- `skills/cinematic-motion/reference/video-to-website-choreography.md` when video, canvas, or scroll-led media is present
- `skills/cinematic-motion/reference/transition-library.md`
- `skills/cinematic-motion/reference/mobile-fallbacks.md`
- `skills/cinematic-motion/reference/motion-performance.md`
- `skills/spatial-experience-design/reference/scene-kit-and-asset-directive.md`
- `.agents/contexts/spatial/motion-board.md`
- `.agents/contexts/spatial/showroom-choreography.md` when media-led sections exist
- `.agents/contexts/spatial/cinematic-prompt-pack.md` when generated media is used
- `.agents/contexts/spatial/depth-map.md`
- `.agents/contexts/spatial/hero-event-blueprint.md`
- `.agents/contexts/spatial/asset-boundary.md`

## EXECUTION SEQUENCE

### STEP 1: Validate Motion Contract

Confirm:

- physical law
- primary motion archetype
- four motion tracks
- audit mechanics being adapted
- assets and fallbacks
- reduced-motion plan
- mobile simplification
- showroom choreography for video/canvas sections

Gate: If the motion board does not separate arrival, ambient, scroll-bound, and interaction, revise it before code.
Gate: Do not implement scroll-led video/canvas scenes until showroom choreography defines section enter/leave points, text zone, media type, loading plan, mobile fallback, and reduced-motion behavior.

### STEP 2: Plan DOM And Layer Ownership

Map:

- which elements are static
- which elements arrive once
- which elements loop ambiently
- which elements are scroll-bound
- which elements respond to interaction
- which layers need pointer-events
- which layers must remain accessible

### STEP 3: Implement Arrival

Use the hero-event blueprint.

Examples:

- curtain split
- mural reveal
- door open
- light spill
- fabric pull
- before/after threshold
- object entrance

Arrival runs once and must have a reduced-motion still/crossfade.

### STEP 4: Implement Ambient

Use low-amplitude, low-attention loops:

- dust motes
- textile drift
- light shimmer
- plant shadow
- slow object float

Pause or simplify ambient motion offscreen and for reduced motion.

### STEP 5: Implement Scroll-Bound Motion

Use scroll as playhead only when physical causality is clear:

- stacked panels
- room procession
- object spine
- material wipe
- transformation reveal
- gallery plate sequence
- canvas walkthrough

When scroll stops, scrubbed motion stops.

### STEP 6: Implement Interaction

Use interaction for:

- material swatch previews
- project index previews
- before/after controls
- inquiry form focus and progress
- gallery navigation

Provide keyboard and touch equivalents.

### STEP 7: Verify

Check:

- no universal fade-up pattern
- no timeline collisions
- no hidden inquiry
- no scroll trap
- no broken mobile layout
- no reduced-motion failure
- no heavy media without poster/fallback
- no background video wallpaper without a section-specific proof, atmosphere, transformation, or inquiry job

## QUALITY GATE CHECKLIST

- [ ] Four motion tracks are separate.
- [ ] Arrival follows hero-event blueprint.
- [ ] Ambient loops pause/simplify.
- [ ] Scroll-bound motion has physical causality.
- [ ] Interaction motion is accessible.
- [ ] Asset loading and fallback match asset-boundary.
- [ ] Video/canvas sections have choreography maps, not only motion descriptions.
- [ ] Reduced-motion behavior exists.
- [ ] Motion strengthens the visual thesis.
