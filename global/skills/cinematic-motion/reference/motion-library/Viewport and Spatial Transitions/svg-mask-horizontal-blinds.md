# SVG Mask Horizontal Blinds

## Visual Description
The screen splits into roughly 30 horizontal bands. However, the bands do not simply slide in from the edges. Each horizontal slit unfolds symmetrically from its own invisible center coordinate, expanding vertically in opposing directions until they perfectly interlock and reveal the full image underneath. The reveal cascades slightly from bottom to top, creating a wave. It evokes the feeling of mechanized metallic louvers snapping open.

## Emotional Register
Deeply satisfying and engineered. Provides a distinct physical, tactile weight to a digital scene transition.

## Technical Mechanics
* **DOM Structure:** Similar to the Grid Wipe, relying on a robust SVG `<mask>` overlay over an `<image>`.
* **CSS Properties:** `<mask id="...">` combined with CSS referencing it via `mask: url(#...)`.
* **JS Engine:** GSAP + Vanilla JS.
* **Key Timeline Logic:** `vbHeight` divided by `BLIND_COUNT` (e.g., 30 lines). Places two overlapping rectangles on a calculated `centerY` coordinate.
* **Easing Curve:** Easing managed via GSAP defaults; stagger set to `each: 0.02, from: "start"`.
* **Performance Notes:** Requires `+0.01` height offset to eliminate rendering gaps between bands where the browser's subpixel rendering logic fails.

## Code Snippet / Reverse Engineering Brief
```javascript
import gsap from "gsap";

// Coordinate mapping logic for blinds
const BLIND_COUNT = 30;
const vbHeight = 100; // viewBox height percentage
const h = vbHeight / BLIND_COUNT;
const blinds = []; // Populated with objects like { y: calculatedY, h: h/2 }

// Example timeline execution for SVG rects
// rects array should contain 2 elements per blind (top half, bottom half)
gsap.to(rects, {  
  y: (i) => {  
    const b = blinds[Math.floor(i / 2)];  
    return i % 2 === 0 ? b.y - b.h : b.y; // Even moves up, odd stays center  
  },  
  height: (i) => {  
    const b = blinds[Math.floor(i / 2)];  
    return b.h + 0.01; // Tiny offset eliminates hairline gaps  
  },  
  stagger: { each: 0.02, from: "start" }  
});
```

## Metadata
- **Industry Name(s):** Center-Split Horizontal Reveal
- **Rarity:** RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH (Significantly more reliable than the grid layout due to single-axis math and fewer DOM/SVG nodes)
- **Accessibility / Reduced Motion:** Ensure `prefers-reduced-motion` triggers a straightforward opacity fade instead of the complex SVG mask timeline.
