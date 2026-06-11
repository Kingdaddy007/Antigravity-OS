# SVG Mask Column Random Grid Wipe

## Visual Description
A full-screen image transitions into a completely new scene not via a slide or fade, but through a synchronized, digital grid manifestation. The viewport is divided into a rigid grid of invisible squares. A wave sweeps from left to right, but instead of a solid line, the grid squares flash into existence sequentially. The reveal sweeps structurally across columns, but within each column, the individual tiles pop in randomly. The edge is perfectly crisp, with zero anti-aliasing blur between the tiles. It feels algorithmic, mechanical, and flawlessly precise.

## Emotional Register
Architectural and highly technical. The user feels as though they are witnessing a digital construction process occurring in real-time.

## Technical Mechanics
* **DOM Structure:** An outer `.stage` section containing multiple `.layer` SVGs. The SVG utilizes `viewBox="0 0 100 100"` and `preserveAspectRatio="xMidYMid slice"` to act identically to CSS `object-fit: cover`.
* **CSS Properties:** `<mask id="mask*">` containing `<rect>` elements initialized with `fill="black"`. The dynamic grid logic is drawn into empty `<g>` tags using white SVG rects. `shape-rendering="crispEdges"` is mandatory to kill blurring.
* **JS Engine:** GSAP Timeline + ScrollTrigger tied tightly to smooth scrolling logic.
* **Key Timeline Logic:** Grid layout calculated dynamically (cols : rows ≒ vbWidth : vbHeight) to maintain perfect squares. A flat array of generated cells is reconstructed into columns. Each column array is shuffled using `gsap.utils.shuffle()` and pushed sequentially to a new master array.
* **Easing Curve:** `power3.out`.
* **Performance Notes:** Overlaps of +0.01 to +0.1 are dynamically injected into the math to solve subpixel calculation gaps. Must trigger `kill()` on the timeline during window resize to prevent total layout destruction.

## Code Snippet / Reverse Engineering Brief
```javascript
import gsap from "gsap";

// Array reconstruction logic for grid mask elements
function openBlinds({ cells, rows, cols }) {  
  const ordered = [];  
  
  for (let x = 0; x < cols; x++) {  
    const column = [];  
    for (let y = 0; y < rows; y++) {  
      const index = y * cols + x;   
      column.push(cells[index]);  
    }  
    // Randomize the order of cells within each column
    const shuffledColumn = gsap.utils.shuffle(column);  
    ordered.push(...shuffledColumn);  
  }  
    
  return gsap.timeline()  
   .to(ordered, {  
      opacity: 1, // Or scale: 1 depending on setup
      duration: 1,  
      ease: "power3.out",  
      stagger: { each: 0.02 }  
    });  
}
```

## Metadata
- **Industry Name(s):** Grid Reveal Transition, Subpixel Mask Sweep
- **Rarity:** ULTRA-RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** MEDIUM (Requires rigorous JS logic for debouncing screen resizing and complex recalculation of aspect ratios)
- **Accessibility / Reduced Motion:** Bypass the timeline execution entirely and utilize a standard, immediate opacity crossfade.
