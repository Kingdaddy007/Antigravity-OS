# Dotted Keyword Scatter Wipe

## Visual Description
Hovering over a heavily styled, dotted keyword instantly triggers an explosive geometric scatter. The word fractures into distinct character fragments that are randomly expelled outward into the surrounding space. Immediately, a synchronized CSS clip-path wipe sweeps across the original container, smoothly revealing the text reconstructed in its secondary state. The exit choreography pulls the scattered elements back seamlessly. It feels algorithmic, sharply defined, and exceptionally crisp.

## Emotional Register
Tactile, surprising, and highly engineered. Evokes the feel of an advanced mechanical instrument, a hacker terminal, or a futuristic heads-up display.

## Technical Mechanics
- **DOM Structure:** Single HTML file container; the target word is split into absolute positioned spans wrapped within a relative bounding box.
- **CSS Properties:** `clip-path: polygon()`, `transform: translate()`, `transform: rotate()`, `opacity`.
- **JS Engine:** GSAP (Vanilla, strictly avoiding React or heavy frameworks).
- **Key Timeline Logic:** `gsap.timeline()` utilizing sequential `.to()` and `.fromTo()` calls. A complex stagger function handles the random spatial scatter, followed immediately by the wipe reveal.
- **Easing Curve:** Highly customized elastic or back easings (e.g. `back.out(1.7)`) to give the scatter a physical "snap" as the characters halt their outward momentum.

## Code Snippet / Reverse Engineering Brief
```javascript
// Ensure SplitText or a custom character splitting utility is used to define 'chars'
// Ensure 'revealText' is the secondary state element waiting to be wiped in
const tl = gsap.timeline({ paused: true });

tl.to(chars, {
  duration: 0.6,
  x: "random(-50, 50)",
  y: "random(-50, 50)",
  rotation: "random(-90, 90)",
  opacity: 0,
  ease: "power4.out",
  stagger: 0.02
})
.fromTo(revealText, 
  { clipPath: "polygon(0% 0%, 0% 0%, 0% 100%, 0% 100%)" },
  { clipPath: "polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)", duration: 0.8, ease: "expo.inOut" },
  "-=0.4"
);

// Trigger on hover
container.addEventListener('mouseenter', () => tl.play());
container.addEventListener('mouseleave', () => tl.reverse());
```

## Metadata
- **Industry Name(s):** Micro-interaction timeline burst, Clip-path text scatter
- **Rarity:** UNCOMMON
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH. Extremely lightweight, utilizing a single file without a heavy build step. Excellent for isolated micro-interactions without threatening main-thread performance.
- **Accessibility / Reduced Motion:** Replace the spatial scatter with a simple opacity cross-fade, maintaining the clip-path wipe if it does not violate specific user-defined reduced motion thresholds.
