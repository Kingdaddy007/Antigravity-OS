# Planetary Orbit Masking (Cinematic Radial Layout)

## Contents

- [Concept](#concept)
  - [The Spatial Metaphor](#the-spatial-metaphor)
- [1. Radial Layout CSS & Text Anti-Overlap](#1-radial-layout-css-text-anti-overlap)
  - [React / TSX Implementation (Math)](#react-tsx-implementation-math)
- [2. GSAP Choreography Timeline](#2-gsap-choreography-timeline)
- [3. Reverse Parallax (Background Depth)](#3-reverse-parallax-background-depth)

## Concept

**Name:** Planetary Orbit Masking
**Type:** Scroll-Driven Spatial Layout

Use this reference when designing a leadership, team, or category section where elements must establish an orbit around a central anchor figure, revealing themselves in a highly choreographed sequence. 

Instead of standard "static cards", this technique treats the central object as a gravitational anchor, with surrounding objects expanding outward, fading in, rotating around it, and vanishing upon lock.

### The Spatial Metaphor
We reject basic "grids" for team pages. We map the leadership hierarchy into a literal unified orbit:

1. **Silent Flyout (Structural Expansion):** The orbiters begin hidden perfectly behind the central anchor. On scroll, they slide outward radially to a fixed distance. The structure is pure and silent—no text is visible during this movement.
2. **The Lock & Fade-in:** The exact moment the orbiters reach their radial slots, their associated text fades in instantly.
3. **Planetary Rotation (Reverse Parallax Depth):** As the scroll continues, the entire constellation of orbiters slowly rotates 180 degrees. The individual portraits counter-rotate by the exact negative amount, ensuring faces and typography remain perfectly upright. A massive background watermark scales down and moves backward, creating reverse parallax.
4. **The Fade-Out Mask:** Right as the rotation completes and the constellation reaches its second fixed position, the text elegantly fades out again, returning the focus entirely to the visual structure.

---

## 1. Radial Layout CSS & Text Anti-Overlap

Radial layouts typically suffer from typography overlap. To fix this, text must be dynamically positioned outward based on its angle.

### React / TSX Implementation (Math)

```tsx
// Inside your map over orbiters:
const totalOrbiters = orbiters.length;
const angle = (index / totalOrbiters) * Math.PI * 2;
const offsetAngle = angle - Math.PI / 2; // Start at top center (-90deg)

// Radii (vw and vh)
const rx = typeof window !== 'undefined' && window.innerWidth < 768 ? 42 : 36; 
const ry = typeof window !== 'undefined' && window.innerWidth < 768 ? 45 : 40; 

const targetLeft = `calc(50% + ${Math.cos(offsetAngle) * rx}vw)`;
const targetTop = `calc(50% + ${Math.sin(offsetAngle) * ry}vh)`;

// Radial Text Positioning Logic (Anti-Overlap)
const sin = Math.sin(offsetAngle);
const cos = Math.cos(offsetAngle);

let textPositionClass = "";
if (sin < -0.5) {
   // Top Area: Text goes above the image
   textPositionClass = "bottom-full mb-3 left-1/2 -translate-x-1/2 text-center flex-col";
} else if (sin > 0.5) {
   // Bottom Area: Text goes below the image
   textPositionClass = "top-full mt-3 left-1/2 -translate-x-1/2 text-center flex-col";
} else if (cos > 0) {
   // Right Area: Text goes right of the image
   textPositionClass = "top-1/2 -translate-y-1/2 left-full ml-4 text-left flex-col items-start";
} else {
   // Left Area: Text goes left of the image
   textPositionClass = "top-1/2 -translate-y-1/2 right-full mr-4 text-right flex-col items-end";
}
```

---

## 2. GSAP Choreography Timeline

This timeline handles the Flyout, Fade-In, Rotation, and Fade-Out sequence mapped perfectly to the scroll position.

```javascript
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

// Inside your GSAP Hook/Effect:
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: sectionRef.current,
    start: "top top",
    end: "+=300%", // 300% gives a long, smooth scrub for the rotation
    pin: pinRef.current,
    scrub: 1, 
  }
});

// Phase 1: Silent Fly Out (0s to 1.5s)
// Orbiters move from 50%/50% to their radial targets. No text.
tl.to(".director-portrait", {
  left: function(i, target) { return target.getAttribute("data-left"); },
  top: function(i, target) { return target.getAttribute("data-top"); },
  scale: 1,
  opacity: 1,
  duration: 1.5,
  ease: "power2.out",
}, 0); 

// Phase 2: Fade in Names (1.5s to 2.0s)
// Names appear instantly AFTER the flyout finishes.
tl.fromTo(".team-text",
  { opacity: 0 },
  { opacity: 1, duration: 0.5, ease: "power2.out" },
  1.5
);

// Phase 3: Planetary Rotation (2.0s to 5.0s)
// The container rotates clockwise, while individual portraits rotate counter-clockwise to stay upright.
tl.to(".orbit-container", {
  rotation: 180,
  duration: 3,
  ease: "none"
}, 2.0);

tl.to(".director-portrait", {
  rotation: -180, // Counter-rotation
  duration: 3,
  ease: "none"
}, 2.0); 

// Phase 4: Fade out Names (4.5s to 5.0s)
// The names cleanly fade away exactly as the rotation locks into its final 180deg position.
tl.to(".team-text", {
  opacity: 0,
  duration: 0.5,
  ease: "power2.in"
}, 4.5);
```

---

## 3. Reverse Parallax (Background Depth)

Add a massive background watermark text to emphasize the depth. The background text should scale *down* and move *up* while the foreground orbit rotates.

```javascript
// Add this to the start of the timeline (time 0)
tl.to(".bg-text-parallax", {
  y: "-20vh",
  scale: 0.85,
  opacity: 0.05,
  duration: 4.5, // Runs during the entire flyout and rotation
  ease: "none"
}, 0);
```
