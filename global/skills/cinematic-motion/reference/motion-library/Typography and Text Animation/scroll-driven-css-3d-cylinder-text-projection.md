# Scroll-Driven CSS 3D Cylinder Text Projection

## Visual Description
The layout locks in place as the user scrolls into the viewport. A series of large, elegant typographic phrases appear positioned along the outer curvature of an invisible 3D cylinder floating in the center of the screen. As the scroll progress advances, the cylinder rotates around its horizontal X-axis. The text phrases rise from a tilted, compressed -80° background perspective, resolve into a crisp, flat front-facing layout, and then curve backward and compress into a 270° perspective, disappearing into the depth of the screen.

## Emotional Register
The viewer experiences structural depth, a sense of scale, and architectural order, as if interacting with a kinetic sculpture.

## Technical Mechanics
* **DOM Structure:** A parent container `.cylinder__wrapper` contains a `.cylinder__text__wrapper` which holds individual text block elements `.cylinder__item`.
* **CSS Properties:** The parent wrapper establishes a 3D perspective: `perspective: 70vw;`. The text wrapper preserves the coordinates: `transform-style: preserve-3d;`. Individual elements use `position: absolute; backface-visibility: hidden;` to hide the reversed backfaces of the cylinder.
* **JS Engine:** GSAP (v3) with the ScrollTrigger plugin.
* **Key Timeline Logic:** The position of each item is calculated using trigonometry. The vertical spacing angle is calculated by dividing 180 degrees (representing the visible front half of the cylinder) by the total number of text items: `spacing = 180 / textItems.length`. For each item, its angle in radians determines its coordinates: `y = sin(angle) * radius`, `z = cos(angle) * radius`. GSAP ScrollTrigger pins the container and animates the rotation of the main wrapper from `rotateX: -80` to `rotateX: 270`.
* **Easing Curve:** Linear easing (`ease: "none"`) is applied to tie the physical rotation speed of the cylinder directly to the scroll velocity of the user.
* **Performance Notes:** Extremely performant; uses standard GPU-accelerated CSS 3D transforms (`translate3d` and `rotateX`) to keep layout reflows at zero during scroll.

## Code Snippet / Reverse Engineering Brief
```html
<div class="cylinder__wrapper">
  <div class="cylinder__text__wrapper">
    <div class="cylinder__item">The Atelier</div>
    <div class="cylinder__item">Of Spatial</div>
    <div class="cylinder__item">Silence</div>
    <div class="cylinder__item">And Light</div>
  </div>
</div>
```

```javascript
import gsap from "gsap";
import ScrollTrigger from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

// Mathematical layout configuration for Cylinder items
const textItems = document.querySelectorAll('.cylinder__item');
const textWrapper = document.querySelector('.cylinder__text__wrapper');

if (textWrapper && textItems.length > 0) {
  const radius = Math.min(window.innerWidth, window.innerHeight) * 0.4; // offset metric
  const spacing = 180 / textItems.length;

  textItems.forEach((item, index) => {
    const angle = (index * spacing * Math.PI) / 180;
    const rotationAngle = index * -spacing;
    const y = Math.sin(angle) * radius;
    const z = Math.cos(angle) * radius;
      
    item.style.transform = `translate3d(-50%, -50%, 0) translate3d(0, ${y}px, ${z}px) rotateX(${rotationAngle}deg)`;
  });

  // GSAP ScrollTrigger
  gsap.fromTo(textWrapper, 
    { rotateX: -80 },
    { 
      rotateX: 270, 
      ease: "none", 
      scrollTrigger: {
        trigger: ".cylinder__wrapper",
        start: "center center",
        end: "+=2000svh", // Extended scroll distance
        pin: true,
        scrub: 2 // Lag smoothing
      }
    }
  );
}
```

## Metadata
- **Industry Name(s):** 3D Cylindrical Kinetic Typography, Scroll-Triggered Text Cylinder, Cylinder Text Roll
- **Rarity:** RARE
- **Implementation Confidence:** High
- **Production Feasibility:** High
- **Accessibility / Reduced Motion:** Respect `prefers-reduced-motion` by disabling ScrollTrigger rotation and presenting text items in a standard vertical flow.
