# Video To Website Choreography

## Contents

- [Core Rule](#core-rule)
- [Section Choreography Schema](#section-choreography-schema)
- [Text And Layout](#text-and-layout)
- [Scroll Rhythm](#scroll-rhythm)
- [Media Types](#media-types)
- [Lenis Scroll Foundation](#lenis-scroll-foundation)
- [Infinite Parallax Gallery Loop](#infinite-parallax-gallery-loop)
- [Canvas Frame Scroll Implementation](#canvas-frame-scroll-implementation)
- [WebGL Cinematic Mechanics](#webgl-cinematic-mechanics)
- [CSS 3D Room Box](#css-3d-room-box)
- [Loading And Fallback](#loading-and-fallback)
- [Anti-Patterns](#anti-patterns)
- [Output](#output)

Use this when a spatial website depends on video, canvas frames, image sequences, scroll-driven media, or full-bleed room films. The goal is not video wallpaper; the goal is a readable website whose media performs spatial proof.

## Core Rule

Every media section must define what the video does for the website.

Allowed jobs:

1. Establish atmosphere.
2. Open a threshold.
3. Reveal taste.
4. Prove transformation.
5. Show material intelligence.
6. Carry portfolio proof.
7. Slow the visitor into inquiry.

If the video does none of these, replace it with a still or remove it.

## Section Choreography Schema

```text
Section:
Journey stage:
Belief/proof job:
Media type: still | loop | source-image-to-video | frame sequence | WebGL | SVG mask
Scroll behavior: pinned | scrubbed | stacked | held | free-scroll | interaction-led
Enter range:
Leave range:
Text zone: left | right | edge | bottom label | none | overlay with veil
Reveal rhythm: label -> headline -> body -> CTA/proof
Motion track:
Fallback:
Prompt required:
```

## Text And Layout

- Keep text in outer zones or quiet edge labels when room media occupies the center.
- Use center text only when the media is intentionally subdued by an overlay or the section is proof/stat-focused.
- Stagger text reveals: label -> heading -> body -> CTA/proof.
- Define text-safe zones in the source image prompt, not only in CSS.
- Never let text cover the signature object, threshold, face/hand, material proof, or light behavior.

## Scroll Rhythm

- Use pinned or held sections only when the visitor must read or witness a reveal.
- Use scrubbed media when scroll is the playhead for light, camera, object, or transformation.
- Use stacked panels for room-to-room procession.
- Use short loops for ambient life, not narrative transformation.
- Let final inquiry persist long enough to feel reachable.

## Media Types

| Media | Use When | Required Planning |
| --- | --- | --- |
| Still | Atmosphere or fallback is enough | Crop, text-safe zone, alt text |
| Short loop | Ambient material or light life | Poster, pause offscreen |
| Source-image-to-video | AI scene continuity matters | Source image lock, start/end frames |
| Frame sequence | Scroll must control exact progression | Load `reference/canvas-frame-scroll-implementation.md`; define frame count, preload, mobile tier |
| WebGL | Depth/camera/object inspection is core | Fallback, performance budget |
| SVG mask | Reveal edge must be authored | Mask source, semantic text outside mask |

## Lenis Scroll Foundation

Load `reference/lenis-gsap-scroll-foundation.md` when smooth scroll drives GSAP, parallax, snap sections, canvas frames, infinite loops, or WebGL camera choreography.

Use Lenis as infrastructure. The concept still comes from `visual-thesis.md` and `showroom-choreography.md`.

## Infinite Parallax Gallery Loop

Load `reference/infinite-parallax-gallery-loop.md` when a project needs an endless showroom corridor, material archive, portfolio reel, or gallery wall with Lenis infinite scrolling and GSAP parallax.

Use it only when the loop performs atmosphere, taste, proof, or portfolio browsing. Never use it as a decorative screensaver.

Required context fields:

- Mechanic purpose.
- Panel list and proof job per panel.
- Duplicate seam strategy.
- Text-safe zones.
- Snap behavior.
- Parallax range.
- Mobile fallback.
- Reduced-motion fallback.
- Exit path to project or inquiry.

## Canvas Frame Scroll Implementation

Load `reference/canvas-frame-scroll-implementation.md` when an MP4/MOV or AI-generated video must be extracted into WebP frames and rendered through a scroll-controlled canvas.

Use it only when scroll must control exact visual progression. For ambient motion, prefer a normal video loop with poster and pause behavior.

Required context fields:

- Source video path.
- Sequence purpose.
- Target frame count and FPS.
- Canvas scale/crop rule.
- Loader/preload plan.
- Frame speed.
- Section enter/leave ranges.
- Text zones.
- Mobile frame tier or fallback.
- Reduced-motion poster/crossfade.

## WebGL Cinematic Mechanics

Load `reference/codrops-canvas-cylinder-gallery.md` when project, material, or room images should wrap into a rotating 3D gallery.

Load `reference/scroll-mapped-3d-camera-scenes.md` when a GLB/model/3D world needs a scroll-controlled camera path with text positions and progress ranges.

Use WebGL only when depth, camera path, object inspection, or spatial proof cannot be achieved with stills, video, canvas frames, or DOM layers.

## CSS 3D Room Box

Load `reference/scroll-driven-3d-cube.md` when the selected mechanic is a scroll-controlled CSS 3D cube, rotating room-wall set, Architectural Room Box, or Material Plinth.

Use this when the website needs to rotate through four walls of a curated room or six sides of a material sample without requiring WebGL. Every face still needs context inheritance, a strategic source block, a proof job, and a text-safe zone.

## Loading And Fallback

- Load poster first.
- Preload first frames or first loop before heavy sequences.
- Lazy-load later chapters.
- Mobile may use chapter stills, short loops, or reveal cascades.
- Reduced motion uses poster, crossfade, manual navigation, or static chapter stack.

## Anti-Patterns

| Anti-Pattern | What It Is | Fix |
| --- | --- | --- |
| Background Video Wallpaper | Video behind ordinary sections | Give video a section job or remove it |
| Text Collision | Copy covers the room's evidence | Define prompt-level text-safe zones |
| Same Beat Everywhere | Every section fades over video | Vary by spatial job: hold, scrub, stack, label, reveal |
| Scroll Trap | Pinned media hides inquiry/nav | Keep navigation and inquiry reachable |
| Tech Demo Motion | Frame sequence proves tooling only | Tie frames to room, material, proof, or threshold |

## Output

Create `contexts/spatial/showroom-choreography.md` before implementation. Use the section schema for every video-led or media-led section.
