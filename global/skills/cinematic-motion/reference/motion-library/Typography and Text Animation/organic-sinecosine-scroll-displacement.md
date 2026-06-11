# Organic Sine/Cosine Scroll Displacement

## Visual Description
A fluid, wave-like distortion applied to large typographic columns where text dynamically ripples in direct response to scroll velocity. Initially appearing as a static, elegant block of text, vertical scrolling triggers an organic oscillation. Characters on the left edge of the column undulate according to a sine wave pattern, while characters on the right track a cosine wave. The typography moves with a liquid elasticity, resembling aquatic flora swaying in a current. The resting state returns to perfect linear rigidity as scroll inertia dissipates smoothly over time.

## Emotional Register
Mesmerizing and surreal. The viewer feels a profound sense of fluid instability, as though the text is a living, breathing organism reacting intimately to the user's physical scroll inputs.

## Technical Mechanics
- **DOM Structure:** Block-level text containers wrapped in `div.column`, broken down to individual `span.word` or `span.char` elements via JavaScript logic.
- **CSS Properties:** Primarily utilizing `transform: translate3d()` calculated via custom CSS variables updated per frame. Drop caps are styled precisely to maintain baseline alignment during the distortion phase.
- **JS Engine:** Custom `requestAnimationFrame` loop combined with GSAP or custom lerping logic for easing matrices.
- **Key Timeline Logic:** Tracks `window.scrollY` (or `pageYOffset`) to calculate scroll velocity (`scrolled`). Values are passed into a linear interpolation (`lerp`) function to determine a "volatility" metric.
- **Easing Curve:** Continuous trigonometric easing; linear interpolation applied at a factor of 0.05 for smooth velocity decay.
- **Performance Notes:** Highly performant due to pure transform animations, but requires `will-change: transform` on heavily nested `span` elements to avoid layout thrashing. The translation occurs strictly on the compositor thread.

## Code Snippet / Reverse Engineering Brief
```javascript
const MathUtils = {
  lerp: (a, b, n) => (1 - n) * a + n * b,
  // Maps a value from one range to another
  lineEq: (y2, y1, x2, x1, currentVal) => {
    const m = (y2 - y1) / (x2 - x1);
    const b = y1 - m * x1;
    return m * currentVal + b;
  }
};

let volatility = 0;
const maxscroll = 10;
const uniformValuesRange = [0, 0.9];
let currentScroll = window.scrollY;

const render = () => {
  const newScroll = window.scrollY;
  const scrolled = Math.abs(newScroll - currentScroll);
  
  // Interpolate volatility based on scroll speed
  // Assuming lineEq maps scroll speed (0 to maxscroll) to volatility (0 to 0.9)
  const targetVolatility = MathUtils.lineEq(
    uniformValuesRange[1], 
    uniformValuesRange[0], 
    maxscroll, 
    0, 
    Math.min(scrolled, maxscroll) // clamp scrolled
  );
  
  volatility = MathUtils.lerp(
    volatility,
    targetVolatility,
    0.05
  );
  
  // Apply sine/cosine displacement to split text nodes
  // Example placeholder logic:
  // elements.forEach((el, index) => {
  //   const offset = Math.sin(index * 0.1) * volatility * 50;
  //   el.style.transform = `translate3d(${offset}px, 0, 0)`;
  // });
  
  currentScroll = newScroll;
  requestAnimationFrame(render);
};

// Initialize the render loop
requestAnimationFrame(render);
```

## Metadata
- **Industry Name(s):** Infinite Scroll Wave Typography, Organic Text Distortion
- **Rarity:** RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** MEDIUM. Requires rigorous debouncing of the split-text logic on window resize. Generating hundreds of span tags poses a potential memory leak if nodes are not properly garbage-collected during route changes in single-page applications.
- **Accessibility / Reduced Motion:** Must inject an `aria-label` on the parent container with the full text string, hiding the animated spans with `aria-hidden="true"`. If `prefers-reduced-motion` is active, the `requestAnimationFrame` loop must be bypassed entirely.
