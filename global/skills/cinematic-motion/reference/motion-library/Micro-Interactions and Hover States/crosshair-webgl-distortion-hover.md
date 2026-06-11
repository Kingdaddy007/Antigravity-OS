# Crosshair WebGL Distortion Hover

## Visual Description
A massive, fullscreen crosshair lines up with the user's cursor. When the exact center intersection point of the crosshair passes over interactive elements, an intricate WebGL or SVG filter distortion ripples specifically at the intersection point, radiating outward along the axes of the crosshair.

## Emotional Register
Precise, aggressive, and highly gamified. Focuses the user's eye intensely on the target pixel.

## Technical Mechanics
- **DOM Structure:** Fullscreen SVG viewport overlapping the DOM.
- **CSS Properties:** `pointer-events: none` on the SVG overlay.
- **JS Engine:** GSAP for attribute manipulation.
- **Key Timeline Logic:** Coordinate mapping of the intersection point.

## Code Snippet / Reverse Engineering Brief
Requires creating a fullscreen `<svg>` containing a `<line>` for the X axis and a `<line>` for the Y axis. On `mousemove`, update the `x1`, `x2`, `y1`, `y2` attributes dynamically. Bind a displacement filter to a `<circle>` attached to the exact intersection node. Animate the radius and displacement scale simultaneously upon colliding with a `[data-hover-target]` element.

## Metadata
- **Industry Name(s):** Fullscreen SVG Crosshair, Filter Crosshair
- **Rarity:** RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** MEDIUM. Managing fullscreen absolute SVGs over interactive DOM elements requires exact `z-index` and `pointer-events` management to avoid breaking core site navigation logic.
- **Accessibility / Reduced Motion:** Needs graceful degradation to standard pointer cursor for users with reduced motion or low vision, as fullscreen tracking lines can be highly distracting.
