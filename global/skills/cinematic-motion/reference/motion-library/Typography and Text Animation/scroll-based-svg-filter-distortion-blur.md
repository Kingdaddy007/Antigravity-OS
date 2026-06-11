# Scroll-Based SVG Filter Distortion Blur

## Visual Description
Large, bold HTML text appears heavily distorted, blurred, and slightly liquid. As the user scrolls the element into the vertical center of the viewport, the distortion smoothly resolves, snapping the text into perfect legibility and clarity. The process reverses symmetrically as the text scrolls out of view. The effect feels analogous to viewing a sharp object through thick, frosted, or water-streaked glass that suddenly becomes perfectly transparent.

## Emotional Register
Mysterious, atmospheric, and highly cinematic. It demands profound focus from the user as the legibility struggles and finally resolves into clarity.

## Technical Mechanics
- **DOM Structure:** Standard semantic HTML headings (`<h1>`, `<h2>`).
- **CSS Properties:** `filter: url(#distort-blur)` linking to an inline SVG filter specifically defined in the DOM.
- **JS Engine:** GSAP ScrollTrigger combined with basic DOM manipulation.
- **Key Timeline Logic:** ScrollTrigger tied to the element's bounding box, mapping progress to the specific numerical attributes of the SVG filter primitives.
- **Shader/WebGL:** None, relies entirely on pure SVG `<feGaussianBlur>` and `<feDisplacementMap>` primitives parsed by the browser.
- **Performance Notes:** Animating complex SVG filters (specifically displacement maps) across large text areas causes severe GPU strain and frame dropping on low-tier mobile devices. It forces continuous rasterization updates. Requires careful hardware acceleration evaluation.

## Code Snippet / Reverse Engineering Brief
```html
<svg style="display: none;">
  <defs>
    <filter id="distort-blur">
      <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur" />
      <feDisplacementMap in="blur" in2="SourceGraphic" scale="50" xChannelSelector="R" yChannelSelector="G" id="displacement" />
    </filter>
  </defs>
</svg>
<h1 class="distorted-text" style="filter: url(#distort-blur);">Atmosphere</h1>
```

```javascript
// Ensure GSAP and ScrollTrigger are registered
gsap.registerPlugin(ScrollTrigger);

// Animate both blur and displacement scale to 0 for perfect clarity
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".distorted-text",
    scrub: true,
    start: "top bottom",
    end: "center center"
  }
});

tl.to("#distort-blur feGaussianBlur", {
  attr: { stdDeviation: 0 },
  ease: "none"
}, 0)
.to("#distort-blur feDisplacementMap", {
  attr: { scale: 0 },
  ease: "none"
}, 0);
```

## Metadata
- **Industry Name(s):** Fog Reveal, Intersection Filter Typo, Gooey Displacement
- **Rarity:** RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** MEDIUM. Performance constraints on Safari/iOS when manipulating SVG filters dynamically must be rigorously tested. The rendering pipeline often struggles with continuous `feDisplacementMap` mutations.
- **Accessibility / Reduced Motion:** Degrades flawlessly by simply removing the SVG filter entirely via CSS media queries, leaving crisp, legible text for screen readers and reduced motion profiles.
