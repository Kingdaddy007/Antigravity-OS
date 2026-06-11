# Split Flap / Mechanical Counter

## Visual Description
Mimics the mechanical split-flap displays found in airports and train stations. Each character position is divided into two halves (top and bottom). When a character changes, the top half rotates down (around its bottom edge) to reveal the new character, while the bottom half remains static until the top half completes, then snaps to the new character. The rotation is fast (150-250ms) with a slight "snap" at the end, mimicking the mechanical click of physical flaps. Often paired with subtle motion blur during rotation and a faint shadow between the top and bottom halves. The effect cycles through intermediate characters when transitioning (e.g., A → B → C → D to reach D).

## Emotional Register
Nostalgic, mechanical, precise, analog-in-digital. Conveys time-sensitivity, urgency (departures/arrivals), and systematic information updates. The physicality of the effect makes digital content feel tangible and real.

## Technical Mechanics
* **DOM Structure:** Each character wrapped in container with two child elements (top-half, bottom-half), each clipped at 50% height. 3D transforms required on parent.
* **CSS Properties:** `transform: rotateX()`, `clip-path: inset()` or `overflow: hidden`, `transform-style: preserve-3d`, `backface-visibility: hidden`
* **JS Engine:** Custom JavaScript with `requestAnimationFrame` or GSAP with split geometry
* **Key Timeline Logic:** For top half: `.to(topHalf, {rotateX: -90, transformOrigin: "bottom", duration: 0.2, ease: "power2.in"})`, then swap character and reset. Repeat for each character in sequence.
* **Easing Curve:** `power2.in` for the flip down (mimics gravity), then instant snap
* **Performance Notes:** 3D transforms are GPU-accelerated; use `will-change: transform` conservatively. Animating many characters simultaneously can be heavy — consider staggering or limiting to small strings.

## Code Snippet / Reverse Engineering Brief
Most production implementations use proprietary animation libraries or tightly integrated design systems. To recreate:

1. **DOM Structure**: For each character position, create:
```html
<div class="flap-container"> 
  <div class="flap-top" data-char="A"></div> 
  <div class="flap-bottom" data-char="A"></div> 
</div>
```
2. **CSS**: Set `transform-style: preserve-3d` on container, `overflow: hidden` on each half, clip top half to upper 50% and bottom half to lower 50% using `clip-path: inset()` or positioned wrapper.
3. **Animation Sequence**: When changing from "A" to "D", cycle through B, C, D. For each transition: animate top half `rotateX(-90)`, swap its `data-char` attribute to next letter, animate `rotateX(0)`, then update bottom half `data-char` to match.
4. **Timing**: Use 150-200ms per flip, with 50ms pause between characters for mechanical feel.
5. **Polish**: Add subtle drop shadow between halves, slight motion blur during rotation using `filter: blur(0.5px)` during mid-flip.

## Metadata
- **Industry Name(s):** Split-Flap Display, Mechanical Counter, Flip Clock Effect, Airport Board Animation
- **Rarity:** RARE
- **Implementation Confidence:** MEDIUM
- **Production Feasibility:** MEDIUM
- **Accessibility / Reduced Motion:** For `prefers-reduced-motion`, use instant character swaps with no rotation. Ensure `aria-live="polite"` on container to announce changes to screen readers. Provide pause control for auto-updating content per WCAG 2.2 SC 2.2.2.
