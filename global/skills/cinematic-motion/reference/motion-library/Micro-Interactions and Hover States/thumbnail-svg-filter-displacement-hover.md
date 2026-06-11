# Thumbnail SVG Filter Displacement Hover

## Visual Description
Hovering over a standard image thumbnail causes the image to temporarily bulge, liquefy, or swirl. It transitions from a flat, static jpeg to a fluid medium, then smoothly settles back into clarity when the cursor is removed.

## Emotional Register
Tactile and liquid. Transforms static media into a physical element.

## Technical Mechanics
- **DOM Structure:** Standard `<img>` with SVG filters defined in `<defs>`.
- **CSS Properties:** `filter: url(#hover-distort)`.
- **JS Engine:** GSAP.

## Code Snippet / Reverse Engineering Brief
**Reverse Engineering Brief:** Apply `<feTurbulence>` and `<feDisplacementMap>`. Tie a GSAP `.to()` tween to the `mouseenter` event, animating the `scale` attribute of the displacement map up to `20`. Revert to `0` on `mouseleave`.

## Metadata
- **Industry Name(s):** Card Filter Bulge, Image Liquid Hover
- **Rarity:** UNCOMMON
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH
- **Accessibility / Reduced Motion:** Ensure the filter effect is bypassed or disabled for users who prefer reduced motion.
