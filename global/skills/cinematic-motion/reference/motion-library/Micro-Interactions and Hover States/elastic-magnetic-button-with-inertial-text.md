# Elastic Magnetic Button with Inertial Text

## Visual Description
A large, pill-shaped button sits in the viewport. When the cursor approaches, its proximity boundary captures the cursor. The button physically pulls toward the cursor, breaking its static alignment. Crucially, the text *inside* the button reacts with delayed inertia—it moves slightly further than the button casing itself, creating a parallax friction. When the cursor breaks the boundary, the button snaps back to the origin, vibrating elastically before settling. It feels physical, weighty, and highly responsive.

## Emotional Register
Playful yet incredibly robust. Imparts a sense of heavy material quality, like dragging a strong magnet across a frictionless steel plate.

## Technical Mechanics
- **DOM Structure:** Outer bounding box (.container or proximity zone), visual button element, inner text `<span>`.
- **CSS Properties:** `transform: translate(x, y)`.
- **JS Engine:** GSAP (specifically utilizing `gsap.quickTo` for performant, frame-by-frame tracking).
- **Key Timeline Logic:** Distance clamping and mapping. Interpolates the mouse coordinate against the absolute center of the bounding box.
- **Easing Curve:** Dynamic elastic easing injected via template literal: `elastic.out(${factor}, 0.5)` where the factor is a mapped clamp based on the exact exit distance of the cursor.
- **Performance Notes:** Extremely performant if relying on `gsap.quickTo()`, which updates properties directly in the rendering pipeline without spinning up full GSAP tweens and consuming memory.

## Code Snippet / Reverse Engineering Brief
```javascript
// Inertial Text Parallax Logic
const moveX = magnetize(relX);
const moveY = magnetize(relY);

gsap.to(target, { x: moveX * relX, y: moveY * relY });
if (magText) {
  gsap.to(target.querySelector("span"), {
    x: moveX * relX * 0.3, // 30% parallax amplification
    y: moveY * relY * 0.2  // 20% parallax amplification
  });
}

// Dynamic Elastic Exit
const dist = Math.sqrt(Math.pow(relX, 2) + Math.pow(relY, 2));
const calcFactor = gsap.utils.pipe(
  gsap.utils.clamp(10, 170),
  gsap.utils.mapRange(10, 170, 0.8, 1.75)
);
const factor = calcFactor(dist);

gsap.to(target, {
  x: 0, y: 0,
  ease: `elastic.out(${factor}, 0.5)`,
  duration: 1
});
```

## Metadata
- **Industry Name(s):** Magnetic Hover, CustomWiggle Elastic Boundary
- **Rarity:** UNCOMMON
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH. Clean vanilla JS logic. `pointer-events: none` must be applied to the inner span to prevent interaction flickering.
- **Accessibility / Reduced Motion:** Neutralize the XY movement mappings entirely on mobile devices and touch screens, relying solely on CSS `:active` states. Avoid for users with `prefers-reduced-motion`.
