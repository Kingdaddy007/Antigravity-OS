# Transition Library

Use scene-native transitions. Do not use generic wipes when a room, material, object, or threshold can perform the transition.

## Symmetrical Curtain Reveal

Best for entry moments, textile brands, mural reveals, and theatrical room openings.

Required assets:

- left and right curtain/mask layers or solid veil panels
- room image/video behind
- reduced-motion still

Implementation:

- left layer moves `xPercent: -100`
- right layer moves `xPercent: 100`
- room settles from slight scale
- caption appears after room stabilizes

## Diegetic Wipe

Best for fog, shadow, sunlight, curtain, plant shadow, smoke, dust, or fabric crossing the lens.

Rules:

- Wipe matter must belong to the scene.
- The wipe hides a real chapter transition.
- Copy should appear after the wipe stabilizes.
- Use alpha PNG/WebP, SVG mask, or video overlay.

## Organic Alpha Mask

Best for plaster scrape, brush, torn paper, textile edge, mural paint, or liquid reveal.

Requirements:

- black/white alpha matte or SVG path
- high-resolution edge
- clear start/end state

Implementation options:

- CSS `mask-image`
- SVG `<clipPath>`
- GSAP path morph
- canvas alpha composite for advanced cases

## Portal Threshold

Best for doorways, arched openings, gallery portals, mirrors, windows, and room-to-room moves.

Rules:

- The threshold shape must be visible before transition.
- Camera or content moves through the threshold.
- The next chapter inherits geometry or light from the threshold.
- Mobile fallback becomes a stacked chapter reveal.

## Light Spill Reveal

Best for doorway openings, lamp glow, gallery spotlight, morning light, and shadow-to-room transitions.

Motion:

- Begin dark or partially obscured.
- Move a light gradient or mask across the surface.
- Reveal material texture before text.
- Keep the effect slow and quiet.

## Shape Inheritance

Best for signature object spines.

Example:

- lamp shade silhouette expands into circular mask
- chair back outline becomes project frame
- doorway edge becomes vertical wipe
- fabric roll edge becomes section mask

Rule: the object must have a structural role before and after the transition.
