# SVG Filter Distorted Link Hover

## Visual Description
Large navigational typographic links rest cleanly on a menu. Hovering a link does not change its color or draw an underline. Instead, the text geometry warps instantly, rippling with a liquid, glitchy, or noisy distortion effect strictly restricted to the bounding box of the text. It looks as though the text was momentarily dragged underwater.

## Emotional Register
Subversive and artistic. It breaks the sanctity of standard typographic legibility to indicate an active state.

## Technical Mechanics
- **DOM Structure:** `<nav>` links paired with hidden `<svg><defs>` elements containing `<filter>` primitives.
- **CSS Properties:** `filter: url(#distortion)` updated via hover state or JS event listener.
- **JS Engine:** GSAP for animating the SVG attributes.
- **Shader/WebGL:** Pure SVG `<feTurbulence>` combined with `<feDisplacementMap>`.

## Code Snippet / Reverse Engineering Brief
Define an `<feTurbulence>` with `type="fractalNoise"` and `baseFrequency="0.01"`. Apply an `<feDisplacementMap>` mapped to the source text. Bind a GSAP `mouseenter` event to animate the `baseFrequency` to 0.05 and the scale of the displacement map from 0 to 30. On `mouseleave`, animate both back to 0.

## Metadata
- **Industry Name(s):** Filter Displacement Hover, Liquid Link
- **Rarity:** UNCOMMON
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH. Excellent browser support for basic SVG filters, provided they are not continuously animated over massive spatial areas.
- **Accessibility / Reduced Motion:** Use standard CSS underlines for `.no-js` and `prefers-reduced-motion`.
