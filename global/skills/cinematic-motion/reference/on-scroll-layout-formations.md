# On-Scroll Layout Formations

## Contents

- [Concept](#concept)
  - [The Spatial Metaphor](#the-spatial-metaphor)
- [Required Context Before Implementation](#required-context-before-implementation)
- [1. Spatial Convergence (Exploded 3D Assembly)](#1-spatial-convergence-exploded-3d-assembly)
  - [CSS Structure](#css-structure)
  - [GSAP & Math Implementation](#gsap-math-implementation)
- [2. Cinematic Window (Dual-Axis Threshold Wipe)](#2-cinematic-window-dual-axis-threshold-wipe)
  - [CSS Structure](#css-structure)
  - [GSAP Implementation](#gsap-implementation)
- [3. Tactile Swinging Cabinet (Y-Axis Panel Swing)](#3-tactile-swinging-cabinet-y-axis-panel-swing)
  - [CSS Structure](#css-structure)
  - [GSAP Implementation](#gsap-implementation)
- [4. The Arc Procession (Distant Pivot Sweep)](#4-the-arc-procession-distant-pivot-sweep)
  - [CSS Structure](#css-structure)
  - [GSAP Implementation](#gsap-implementation)
- [Anti-Patterns](#anti-patterns)
- [Quality Gate](#quality-gate)

## Concept

**Name:** The Cinematic Layout Formation

Use this reference when a portfolio showcase, material archive, or process timeline needs grid-elements or image items to transition dynamically into a completed structure as the visitor scrolls.

This mechanic is reverse-engineered and adapted from the Codrops `OnScrollLayoutFormations` repository:
```text
https://github.com/codrops/OnScrollLayoutFormations.git
```

### The Spatial Metaphor
We reject standard "jumping grids" or "floating cards." We map the layout calculations onto physical showroom events:

1.  **Spatial Convergence (Exploded 3D Assembly):** Raw, unaligned visual fragments (macro close-ups, fabric weaves, marble veins, lighting sketches) start scattered in Z-depth and rotation, representing the raw, chaotic ideation phase. As the visitor scrolls, they fly together and align into a perfect flat mosaic grid representing the completed, unified room design.
2.  **Cinematic Window (Dual-Axis Threshold Wipe):** An image slides open vertically while its internal content slides in the opposite direction at the exact same velocity. This creates the optical sensation of looking through a window or crossing a sliding physical door threshold.
3.  **Tactile Swinging Cabinet (Y-Axis Panel Swing):** Portfolios or materials swing out on a vertical axis like heavy doors in a wood showroom cabinet, revealing details, client brief answers, and proof on their faces.
4.  **The Arc Procession (Distant Pivot Sweep):** Portfolios sweep into view along a curved radial path, mimicking a physical walk down a circular architectural gallery corridor.

---

## Required Context Before Implementation

Add this layout formation to `contexts/spatial/showroom-choreography.md` before coding:

```text
Section:
Journey stage:
Formation Archetype: Spatial Convergence | Cinematic Window | Tactile Cabinet | Arc Procession
Grid Setup: columns x rows
Elements List:
  - element_id:
    proof_role:
    initial_offset: (for 3D assembly or swing)
    active_rotation:
Scroll behavior: pinned scrub
Enter range:
Leave range:
Text overlay behavior:
Mobile fallback:
Reduced-motion fallback:
```

---

## 1. Spatial Convergence (Exploded 3D Assembly)

### CSS Structure
Use perspective on the grid container and absolute/grid positioning for items.

```css
.convergence-stage {
  min-height: 300vh;
  position: relative;
  background: #11110f;
  color: #f5f0e8;
}

.convergence-grid-wrapper {
  height: 100vh;
  width: 100%;
  display: grid;
  place-items: center;
  position: sticky;
  top: 0;
  overflow: hidden;
  perspective: 1200px;
}

.convergence-grid {
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  grid-template-rows: repeat(4, 1fr);
  gap: 1.5vw;
  width: 90vw;
  height: 80vh;
  transform-style: preserve-3d;
}

.convergence-item {
  position: relative;
  overflow: hidden;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
}

.convergence-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
```

### GSAP & Math Implementation
The 3D coordinates are calculated dynamically based on each item's distance from the center of the viewport. Farthest items translate and rotate the most.

```js
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const grid = document.querySelector('[data-convergence-grid]');
const items = grid.querySelectorAll('.convergence-item');

/**
 * Calculates translation and 3D rotation relative to viewport center.
 */
function calculateExplodeTransform(element, offsetDistance = 600, maxRotation = 180, maxZTranslation = 2000) {
  const viewportCenter = { width: window.innerWidth / 2, height: window.innerHeight / 2 };
  
  // Find element center coordinates
  const rect = element.getBoundingClientRect();
  const elementCenter = {
    x: rect.left + rect.width / 2,
    y: rect.top + rect.height / 2
  };

  // Find angle relative to center
  const angle = Math.atan2(
    Math.abs(viewportCenter.height - elementCenter.y),
    Math.abs(viewportCenter.width - elementCenter.x)
  );

  const translateX = Math.abs(Math.cos(angle) * offsetDistance);
  const translateY = Math.abs(Math.sin(angle) * offsetDistance);

  // Maximum screen diagonal
  const maxDistance = Math.sqrt(Math.pow(viewportCenter.width, 2) + Math.pow(viewportCenter.height, 2));
  const currentDistance = Math.sqrt(
    Math.pow(viewportCenter.width - elementCenter.x, 2) + 
    Math.pow(viewportCenter.height - elementCenter.y, 2)
  );

  const distanceFactor = currentDistance / maxDistance;

  // Scale rotate and translate based on distance from center
  const rotationX = ((elementCenter.y < viewportCenter.height ? -1 : 1) * (translateY / offsetDistance) * maxRotation * distanceFactor);
  const rotationY = ((elementCenter.x < viewportCenter.width ? 1 : -1) * (translateX / offsetDistance) * maxRotation * distanceFactor);
  const translateZ = maxZTranslation * distanceFactor;

  return {
    x: elementCenter.x < viewportCenter.width ? -translateX : translateX,
    y: elementCenter.y < viewportCenter.height ? -translateY : translateY,
    z: translateZ,
    rotateX: rotationX,
    rotateY: rotationY
  };
}

// Build timeline
gsap.timeline({
  scrollTrigger: {
    trigger: '.convergence-stage',
    start: 'top top',
    end: 'bottom bottom',
    scrub: 0.3,
    pin: '.convergence-grid-wrapper',
  }
})
.fromTo(items, {
  x: (_, el) => calculateExplodeTransform(el).x,
  y: (_, el) => calculateExplodeTransform(el).y,
  z: (_, el) => calculateExplodeTransform(el).z * -1.5, // Push back into negative space
  rotateX: (_, el) => calculateExplodeTransform(el).rotateX,
  rotateY: (_, el) => calculateExplodeTransform(el).rotateY,
  autoAlpha: 0,
  scale: 0.3
}, {
  x: 0,
  y: 0,
  z: 0,
  rotateX: 0,
  rotateY: 0,
  autoAlpha: 1,
  scale: 1,
  stagger: {
    amount: 0.25,
    from: 'center',
    grid: [4, 9]
  }
});
```

---

## 2. Cinematic Window (Dual-Axis Threshold Wipe)

Reveals content by sliding the mask up while sliding the image down inside it. This creates the optical illusion of static spatial layers behind moving wall panels.

### CSS Structure
```css
.window-stage {
  min-height: 250vh;
  position: relative;
  background: #11110f;
}

.window-grid-wrapper {
  height: 100vh;
  position: sticky;
  top: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.window-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 3vw;
  width: 80vw;
}

.window-item {
  position: relative;
  overflow: hidden;
  height: 55vh;
  width: 100%;
}

.window-img-inner {
  height: 100%;
  width: 100%;
  object-fit: cover;
  transform: scale(1.15); /* Provide translation margin */
}
```

### GSAP Implementation
```js
const section = document.querySelector('.window-stage');
const items = section.querySelectorAll('.window-item');
const innerImages = section.querySelectorAll('.window-img-inner');

gsap.timeline({
  scrollTrigger: {
    trigger: section,
    start: 'top top',
    end: 'bottom bottom',
    scrub: 0.4,
    pin: '.window-grid-wrapper'
  }
})
// Slide the mask container up
.fromTo(items, {
  yPercent: -102
}, {
  stagger: 0.1,
  yPercent: 0,
  ease: 'power1.inOut'
})
// Simultaneously slide inner images down to anchor them
.fromTo(innerImages, {
  yPercent: 102
}, {
  stagger: 0.1,
  yPercent: 0,
  ease: 'power1.inOut'
}, 0);
```

---

## 3. Tactile Swinging Cabinet (Y-Axis Panel Swing)

Grid items swing open around their left edge like heavy cupboard panels.

### CSS Structure
```css
.cabinet-grid {
  perspective: 2000px;
}

.cabinet-item {
  transform-origin: 0% 50%; /* Anchor on left edge */
  backface-visibility: hidden;
}
```

### GSAP Implementation
```js
const cabinetItems = document.querySelectorAll('.cabinet-item');

gsap.timeline({
  scrollTrigger: {
    trigger: '.cabinet-stage',
    start: 'top top',
    end: 'bottom bottom',
    scrub: true,
    pin: '.cabinet-wrapper'
  }
})
.from(cabinetItems, {
  stagger: {
    amount: 0.8,
    from: 'start'
  },
  rotationY: 65,
  z: -200,
  yPercent: 10,
  autoAlpha: 0,
  ease: 'expo.out'
});
```

---

## 4. The Arc Procession (Distant Pivot Sweep)

Elements sweep into view along a curved radius by using a remote center rotation origin.

### CSS Structure
```css
.arc-item {
  transform-origin: 100% -450%; /* Remote pivot center high and right */
}
```

### GSAP Implementation
```js
const arcItems = document.querySelectorAll('.arc-item');

gsap.timeline({
  scrollTrigger: {
    trigger: '.arc-stage',
    start: 'top top',
    end: 'bottom bottom',
    scrub: true,
    pin: '.arc-wrapper'
  }
})
.from(arcItems, {
  stagger: 0.08,
  scaleX: 1.05,
  skewX: 15,
  xPercent: 50,
  rotation: -10,
  autoAlpha: 0,
  ease: 'power3.out'
});
```

---

## Anti-Patterns

| Anti-Pattern | What It Is | Fix |
| --- | --- | --- |
| Chaotic Assemblage | Grid items fly in randomly without shared focal length | Maintain consistent photographic lens and lighting across the grid elements |
| Text Swallowing | Exploded items block reading | Confine text content to static edge panels or keep it hidden until grid is fully converged |
| Seam Exposure | Items overlap messy backgrounds | Sample background colours from border pixels and keep canvas layers clear |
| Scroll Jack Sticking | Scrub triggers are too slow or snap loops freeze | Keep the end trigger limits relative to container height (`+=200%` max) |

---

## Quality Gate

Before declaring layout formation complete:
1.  **Metaphor Verification:** The formation matches one of the four spatial metaphors (Atelier Mosaic, Window Reveal, Swinging Archive, Arc Corridor).
2.  **Calculations Locked:** The 3D distance calculations adapt to resizing and do not result in stretched items on viewport edge.
3.  **Contrast Gate:** Faded grid elements (e.g., `brightness(20%)` on non-active items) preserve contrast ratios for overlay text labels.
4.  **Assisted Tech Access:** Grid elements carry meaningful alt attributes and text remains readable outside WebGL wrappers.
5.  **Reduced Motion:** Scroll scrubs are replaced by discrete tabs, fading animations, or stacked layouts when `prefers-reduced-motion` is active.
