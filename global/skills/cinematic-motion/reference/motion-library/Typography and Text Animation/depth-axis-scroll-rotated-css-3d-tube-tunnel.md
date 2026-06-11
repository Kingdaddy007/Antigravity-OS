# Depth-Axis Scroll-Rotated CSS 3D Tube Tunnel

## Visual Description
The user transitions down into a dark void where individual characters or words are stacked along the Z-axis (depth axis). The text elements are arranged in a horizontal circular configuration, creating a physical "tube" or "tunnel" structure. As the user scrolls, the entire tunnel rotates around its vertical Y-axis, while the camera dollys forward through the center. The text scales up as it approaches the viewport boundary and is cropped cleanly at the screen edges, creating an immersive, infinite descent.

## Emotional Register
The visual triggers a feeling of deep spatial entry and immersion, pulling the viewer into a computational vortex.

## Technical Mechanics
* **DOM Structure:** A `.tube__wrapper` holds a parent container `.tube__text__wrapper` filled with multiple text elements.
* **CSS Properties:** The parent `.tube__wrapper` contains `perspective: 70vw; overflow: hidden;`. The `.tube__text__wrapper` maintains `transform-style: preserve-3d;`. Individual elements use `rotateY` transforms to face the center of the tunnel.
* **JS Engine:** GSAP (v3) and ScrollTrigger.
* **Key Timeline Logic:** Coordinate arrays are calculated in JavaScript. Horizontal positions are mapped using sine: `x = sin(angle) * radius`. Vertical positions are centered (`y = 0`). The rotation of individual elements uses `rotateY()` to align them inward along the tunnel walls. GSAP rotates the wrapper around the Y-axis (`rotateY: 0` to `rotateY: 360`) mapped directly to ScrollTrigger's progress.
* **Easing Curve:** Linear `ease: "none"`.
* **Performance Notes:** High rendering speed. Uses standard CSS hardware transformations. To prevent memory issues, elements that have crossed past the camera plane should have their rendering hidden via a dynamic opacity scale linked to scroll coordinates.

## Code Snippet / Reverse Engineering Brief
```html
<div class="tube__wrapper">
  <div class="tube__text__wrapper">
    <div class="tube__item">A</div>
    <div class="tube__item">B</div>
    <div class="tube__item">C</div>
    <div class="tube__item">D</div>
    <div class="tube__item">E</div>
    <div class="tube__item">F</div>
  </div>
</div>
```

```javascript
import gsap from "gsap";
import ScrollTrigger from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

// Positioning CSS elements in a true 3D Tube layout
const tubeItems = document.querySelectorAll('.tube__item');
const tubeWrapper = document.querySelector('.tube__text__wrapper');

if (tubeWrapper && tubeItems.length > 0) {
  const tubeRadius = Math.min(window.innerWidth, window.innerHeight) * 0.5;
  const tubeSpacing = 360 / tubeItems.length;

  tubeItems.forEach((item, index) => {
    const angle = (index * tubeSpacing * Math.PI) / 180;
    const rotationAngle = index * -tubeSpacing;
    const x = Math.sin(angle) * tubeRadius;
    const z = Math.cos(angle) * tubeRadius;
      
    // Center vertically, offset on X and Z axes, rotate Y
    item.style.transform = `translate3d(-50%, -50%, 0) translate3d(${x}px, 0px, ${z}px) rotateY(${rotationAngle}deg)`;
  });

  // GSAP ScrollTrigger configuration for tube rotation
  gsap.fromTo(tubeWrapper,
    { rotateY: 0 },
    {
      rotateY: 360,
      ease: "none",
      scrollTrigger: {
        trigger: ".tube__wrapper",
        start: "center center",
        end: "+=2000svh",
        pin: true,
        scrub: 2
      }
    }
  );
}
```

## Metadata
- **Industry Name(s):** Typographic Tunnel, Depth-Axis Tube Spin, Tube Text Tunnel
- **Rarity:** RARE
- **Implementation Confidence:** High
- **Production Feasibility:** High
- **Accessibility / Reduced Motion:** Tunnel motion should be disabled for `prefers-reduced-motion` to avoid severe motion sickness triggers. Provide a static fallback or simplified linear scrolling.
