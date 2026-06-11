# Infinite Auto-Scrolling Spatial Cylinder

## Visual Description
An infinite carousel of images scrolling vertically. However, the viewport acts as a massive cylinder rather than a flat plane. As images approach the top or bottom edges of the screen, they physically curve backward into the Z-axis, shrinking and fading as if rolling over the edge of a massive wheel.

## Emotional Register
Expansive and highly structured. Provides a perception of infinite spatial depth within limited screen real estate.

## Technical Mechanics
- **DOM Structure:** Canvas element managed by the OGL library.
- **JS Engine:** OGL (lightweight WebGL alternative to Three.js).
- **Key Timeline Logic:** Smooth scroll velocity mapped to infinite wrap logic (modulo math on image positions).
- **Shader/WebGL:** Vertex shader deforms the Y-axis position and Z-axis depth based on the distance from the screen's horizontal center.

## Code Snippet / Reverse Engineering Brief
**Reverse Engineering Brief:** Using OGL, calculate the distance of each plane from the center uv of the screen. Pass this distance to a vertex shader. In the vertex shader, calculate `float curve = distance * distance * u_curveFactor;` and apply it: `position.z -= curve; position.y += curve * direction;`. This effectively bends the geometry dynamically without altering the actual DOM.

## Metadata
- **Industry Name(s):** Infinite OGL Gallery, Spatial Distortion Scroll
- **Rarity:** RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH (OGL is significantly lighter than Three.js, making this specific spatial warp highly performant even on low-end devices.)
- **Accessibility / Reduced Motion:** If reduced motion is requested, disable the Z-axis curve in the vertex shader, defaulting to a standard flat scroll.
