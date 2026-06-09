# Mobile Fallbacks

Premium spatial sites must remain authored on mobile. Do not collapse cinematic sections into raw stacked content.

## Device Tiers

| Tier | Behavior |
| --- | --- |
| Desktop | Full motion: GSAP pins, image sequences, WebGL when justified |
| Tablet | Simplified pins, lower particle/frame counts, shorter media, fewer simultaneous layers |
| Mobile | Static chapter stills, reveal cascades, compressed loops, no heavy scroll-jacked canvas |

## WebGL To WebM

Use when a R3F/canvas scene is heavy but non-interactive on mobile.

- Desktop: WebGL/canvas.
- Mobile: short WebM/MP4 loop with poster.
- Reduced motion: poster only.

## Image Sequence Caps

Suggested caps:

- Desktop hero sequence: 120-240 frames.
- Desktop long sequence: 240-500 frames only if progressively loaded.
- Tablet: 60-120 frames.
- Mobile: 24-60 frames or video loop.

Use chunked loading. Draw nearest loaded frame during fast scroll.

## Progressive Preloading

Load order:

1. Poster frame.
2. First 10-20 frames or first short loop.
3. Current chapter assets.
4. Next chapter assets.
5. Remaining frames after idle.

## Mobile Reveal Cascade

Replace pinned chapters with:

- one still/media per chapter
- visible chapter label
- preserved room sequence
- small reveal timing differences
- no horizontal overflow
- inquiry always reachable

## Reduced Motion

Replace:

- parallax -> static layered image
- image sequence -> poster or manual next/previous
- curtain split -> crossfade
- object spine -> static object with captions
- stacked panels -> normal chapter stack

Never hide content because motion is disabled.
