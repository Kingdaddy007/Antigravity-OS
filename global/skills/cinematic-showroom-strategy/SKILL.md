---
name: cinematic-showroom-strategy
description: >
  Use this skill when planning cinematic interior designer websites, video-led
  portfolios, AI-generated room films, scroll-driven showroom pages, or full
  spatial web experiences where brand diagnosis must become scene sequence,
  image/video prompts, portfolio proof, and website choreography. Activated by
  "cinematic showroom", "video-to-website", "AI room video", "cinematic
  portfolio", "scroll-driven interior website", "Awwwards interior site", or
  when `spatial-experience-design` needs prompts and section choreography. Do
  NOT use for generic video backgrounds, product launch pages, backend work, or
  decorative motion without brand/spatial proof.
---

# Cinematic Showroom Strategy

## WHEN TO USE THIS

- Load after brand, story, and spatial context exist and before writing final image/video prompts.
- Load when a website must become a full cinematic digital showroom, not only a cinematic hero.
- Load when portfolio, proof, AI video, scroll choreography, and text overlays must work as one experience.

## NEVER DO

- Never write standalone "luxury room" prompts detached from brand diagnosis and context files.
- Never treat video as wallpaper behind normal sections.
- Never make every project use the same Awwwards mechanic.
- Never let spectacle replace proof, inquiry clarity, or designer authority.
- Never approve prompts that lack belief, taste world, light, camera, depth, text-safe zone, and rejected cliche.
- Never turn portfolio work into generic cards before showing judgment, transformation, or material decisions.

## CORE MODEL

Translate strategy into cinema:

`Brand diagnosis -> Perception gap -> Taste world -> Story -> Room sequence -> Visual thesis -> Showroom choreography -> Asset directive -> Cinematic prompt pack -> Build`

Every scene must answer:

1. What should the visitor believe here?
2. Which brand context proves that belief?
3. What room, threshold, object, material, light, or human trace carries the scene?
4. What should be withheld, revealed, or transformed?
5. Where can text live without damaging the room?
6. What web behavior turns the media into a section?

## BRAND-TO-SCENE TRANSLATION

Create `contexts/spatial/brand-to-scene-translation.md`.

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

Reject translations that only describe style. The translation must explain why this brand needs these scenes.

## SHOWROOM CHOREOGRAPHY

Create `contexts/spatial/showroom-choreography.md`.

For each section define:

```text
Section:
Journey stage:
Belief/proof job:
Primary room/object/material:
Media type: still | loop | source-image-to-video | frame sequence | WebGL | SVG mask | CSS-native
Scroll behavior:
Text zone:
Reveal rhythm:
Motion track:
Portfolio/proof role:
Fallback:
Asset prompt required: yes | no
```

Use video only when it performs a spatial job: threshold, reveal, light movement, transformation, object guidance, material behavior, proof, or inquiry slowing.

## CINEMATIC PROMPT PACK

Create `contexts/spatial/cinematic-prompt-pack.md` only after approved context files exist.

The prompt pack is not a prompt dump. It is the final cinematic translation of the approved brand, story, spatial, material, motion, and choreography contexts.

Start with `Context Inheritance`:

```text
Derived from:
- contexts/brand-diagnostics.md
- contexts/spatial/spatial-story.md
- contexts/spatial/visual-thesis.md
- contexts/spatial/room-sequence.md
- contexts/spatial/brand-to-scene-translation.md
- contexts/spatial/showroom-choreography.md
- contexts/spatial/portfolio-proof-chapters.md
- contexts/spatial/material-script.md
- contexts/spatial/depth-map.md
- contexts/spatial/motion-board.md
- contexts/spatial/asset-boundary.md
```

Every image/video prompt must include `Strategic Source`:

```text
Perception goal:
Taste world:
Section / journey stage:
Desired visitor belief:
Visual thesis connection:
Room / material / object source:
Motion role:
Website placement:
Text-safe requirement:
Enemy / cliche rejected:
```

If a prompt cannot trace its choices back to approved context files, reject and rewrite it.

## PORTFOLIO PROOF

Create `contexts/spatial/portfolio-proof-chapters.md` for portfolio-led sites.

For each project chapter define:

- Client/context.
- Room or space.
- Original problem or weak state.
- Design decision.
- Material/light move.
- Before/after or transformation proof.
- Cinematic media.
- Caption/proof text.
- Interaction.
- Inquiry relevance.

Use broad grids only after at least one curated project chapter has proven the designer's judgment.

## OUTPUT SHAPE

**Showroom strategy:** Brand belief -> scene sequence -> choreography map -> prompt pack requirements -> portfolio proof -> gates.

**Prompt audit:** Context inheritance -> missing strategic source -> weak prompt risks -> rewrite direction.

**Implementation handoff:** Showroom choreography -> media/asset types -> section text zones -> scroll behavior -> fallback gates.

## NON-NEGOTIABLE CHECKLIST

1. Desired visitor belief is named before visuals.
2. `brand-to-scene-translation.md` exists before prompts.
3. `showroom-choreography.md` maps media, text, scroll, proof, and fallback.
4. `cinematic-prompt-pack.md` has Context Inheritance.
5. Every prompt has a Strategic Source block.
6. No generic luxury-room prompt survives.
7. Portfolio proves decisions before becoming a grid.
8. Video is section-specific proof, atmosphere, transformation, or inquiry, not wallpaper.
