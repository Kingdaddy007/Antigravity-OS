# Architectural Text Mask Reveal

## Contents

- [Concept](#concept)
- [Best Used For](#best-used-for)
- [HTML / SVG Structure](#html-svg-structure)
- [CSS](#css)
- [GSAP Implementation (ScrollTrigger)](#gsap-implementation-scrolltrigger)
- [Anti-Patterns and Gotchas](#anti-patterns-and-gotchas)

## Concept
The "Text Mask Video Reveal" (or "Architectural Threshold") is an elite Awwwards-tier spatial transition where typography acts as a physical window into a background video/scene. Instead of overlaying text on a video, the screen is covered by a solid editorial color (e.g., Ivory or Charcoal), and the brand typography is literally "punched out" as a transparent hole. The video plays exclusively *through* the letters.

As the user scrolls, the typography scales up massively. The gap between the letters (or the negative space inside a letter) expands to consume the entire screen, pulling the user "through" the word and into the video. The solid background gracefully fades away exactly as the typography clears the viewport, creating a seamless, zero-lag immersion.

## Best Used For
- High-end architectural and interior design portfolios.
- Luxury hospitality hero sections.
- When the brand messaging focuses on "thresholds," "entering," or "revealing."
- Transforming static editorial design into immersive motion.

## HTML / SVG Structure

The core trick is using an inline `<svg>` with a `<mask>`.
- `<rect fill="white">` makes the solid background layer opaque.
- `<text fill="black">` punches a transparent hole in the shape of the text.

```html
<div class="threshold-container" style="position: absolute; inset: 0; z-index: 2; pointer-events: none;">
  <svg width="100%" height="100%" style="position: absolute; inset: 0;">
    <defs>
      <!-- Optional: Fog/Blur Filter for initial load -->
      <filter id="distort-blur">
        <feGaussianBlur in="SourceGraphic" stdDeviation="15" result="blur" />
        <feDisplacementMap in="blur" in2="SourceGraphic" scale="80" xChannelSelector="R" yChannelSelector="G" />
      </filter>
      
      <!-- The Mask Definition -->
      <mask id="text-mask">
        <!-- White = Opaque Background -->
        <rect width="100%" height="100%" fill="white" />
        <!-- Black = Transparent Hole -->
        <g id="mask-scale-group" style="transform-origin: 50% 50%;">
          <text x="50%" y="50%" text-anchor="middle" dominant-baseline="central" 
                font-family="Your Display Font" font-size="10vw" letter-spacing="0.1em" text-transform="uppercase"
                fill="black" style="filter: url(#distort-blur);">YOUR BRAND</text>
        </g>
      </mask>
    </defs>
    <!-- The Solid Background Layer (e.g. Ivory) -->
    <rect width="100%" height="100%" fill="#F7E8CF" mask="url(#text-mask)" />
  </svg>
</div>
```

## CSS
The container must be transparent because the SVG `<rect>` provides the background color.
```css
.threshold-container {
  position: absolute;
  inset: 0;
  background-color: transparent; /* Crucial! */
  z-index: 2;
  pointer-events: none;
  will-change: opacity;
}
```

## GSAP Implementation (ScrollTrigger)

```javascript
// 1. Initial Load (Fog Reveal / Breathing)
const arrivalTl = gsap.timeline({
  onComplete: () => {
    // Free up GPU after intro animation
    gsap.set('#arrival-brand', { filter: 'none', clearProps: 'filter' });
  }
});

// Clear the blur and expand letter spacing
arrivalTl.fromTo('#arrival-brand', 
  { letterSpacing: "0.1em" },
  { letterSpacing: "0.25em", duration: 3.5, ease: "power1.out" }, 0.5
).to('#arrival-blur', { attr: { stdDeviation: 0 }, duration: 2.5, ease: "power2.inOut" }, 0.5)
 .to('#arrival-displacement', { attr: { scale: 0 }, duration: 2.5, ease: "power2.inOut" }, 0.5);

// 2. Scroll Interaction (The Massive Zoom)
const masterTl = gsap.timeline({
  scrollTrigger: {
    trigger: '.pinned-wrapper',
    start: 'top top',
    end: '+=500%',
    pin: true,
    scrub: 1,
    anticipatePin: 1
  }
});

// Scale the SVG <g> massively from the center.
// Fade the container exactly when the scale is large enough to cover the screen.
masterTl.to('#mask-scale-group', { 
    scale: 120, // Huge scale to fly through
    transformOrigin: "50% 50%", // Force center
    ease: "power2.in", // Accelerate into the hole
    duration: 1.5 
  }, 0)
  // The fade happens at 0.8 to ensure no "blank wall lag"
  .to('.threshold-container', { 
    opacity: 0, 
    ease: "power1.inOut", 
    duration: 0.5 
  }, 0.8);
```

## Anti-Patterns and Gotchas
- **GSAP Transform Origin Bug**: SVG `<g>` scaling can zoom off-center (to the top-left) in some browsers. Always explicitly set `transformOrigin: "50% 50%"` in the GSAP `.to()` tween.
- **Opacity Conflict**: Do NOT animate opacity in the `arrivalTl` and the `masterTl` on the same element. It creates a state recording bug where scrolling backwards (`scrub` reverse) fails to restore the text. Keep opacity fades restricted to the `masterTl` or the container.
- **The "Blank Wall Lag"**: If the scale duration is `2.0s` and the container fade doesn't start until `1.5s`, the user will stare at a solid colored wall as the gap between the letters fills the screen. Always dissolve the container slightly early (`duration: 1.5`, fade start at `0.8`) so the edges of the window melt away gracefully.
