# Staggered Structural Columns (Vertical Blinds)

## Overview
A highly architectural, structural transition where the incoming element (image or video) is sliced into vertical columns (like pillars) that shoot up from the bottom of the screen staggering one after another. 
This is incredibly performant as it relies on a single DOM element using a complex CSS `mask-image` driven by GSAP, rather than duplicating DOM nodes.

## Best Used For
- Architectural portfolios, luxury real estate, and spatial design.
- Works flawlessly with both static images and background videos (especially scroll-scrubbed videos).
- Replaces standard crossfades or zooms with a very mechanical, "pieced together" construction feel.

## Implementation Pattern

### 1. The Mask Setup (CSS/React)
Apply this style to the absolute positioned wrapper of the incoming element.
It creates 5 vertical columns, each 20% wide.

```tsx
const stripsMaskStyle = {
  "--s1": "0%", "--s2": "0%", "--s3": "0%", "--s4": "0%", "--s5": "0%",
  WebkitMaskImage: `
    linear-gradient(to top, black var(--s1), transparent var(--s1)),
    linear-gradient(to top, black var(--s2), transparent var(--s2)),
    linear-gradient(to top, black var(--s3), transparent var(--s3)),
    linear-gradient(to top, black var(--s4), transparent var(--s4)),
    linear-gradient(to top, black var(--s5), transparent var(--s5))
  `,
  WebkitMaskSize: "20% 100%, 20% 100%, 20% 100%, 20% 100%, 20% 100%",
  WebkitMaskPosition: "0 0, 25% 0, 50% 0, 75% 0, 100% 0",
  WebkitMaskRepeat: "no-repeat",
  maskImage: `
    linear-gradient(to top, black var(--s1), transparent var(--s1)),
    linear-gradient(to top, black var(--s2), transparent var(--s2)),
    linear-gradient(to top, black var(--s3), transparent var(--s3)),
    linear-gradient(to top, black var(--s4), transparent var(--s4)),
    linear-gradient(to top, black var(--s5), transparent var(--s5))
  `,
  maskSize: "20% 100%, 20% 100%, 20% 100%, 20% 100%, 20% 100%",
  maskPosition: "0 0, 25% 0, 50% 0, 75% 0, 100% 0",
  maskRepeat: "no-repeat",
} as React.CSSProperties;

// Inside the component:
<div style={stripsMaskStyle} className="absolute inset-0 z-20 w-full h-full overflow-hidden">
  <img className="absolute inset-0 w-full h-full object-cover" />
</div>
```

### 2. The GSAP ScrollTrigger Sequence
Animate the CSS variables in a timeline to stagger the columns upwards.

```javascript
const hiddenVars = { "--s1": "0%", "--s2": "0%", "--s3": "0%", "--s4": "0%", "--s5": "0%" };

// Assume phase starts at time 0
tl.fromTo(elementRef.current, { scale: 1.1 }, { scale: 1, duration: 1, ease: "none" }, 0)
  .fromTo(elementRef.current, { ...hiddenVars }, { "--s1": "100%", duration: 0.6, ease: "power2.inOut" }, 0)
  .to(elementRef.current, { "--s2": "100%", duration: 0.6, ease: "power2.inOut" }, 0.1)
  .to(elementRef.current, { "--s3": "100%", duration: 0.6, ease: "power2.inOut" }, 0.2)
  .to(elementRef.current, { "--s4": "100%", duration: 0.6, ease: "power2.inOut" }, 0.3)
  .to(elementRef.current, { "--s5": "100%", duration: 0.6, ease: "power2.inOut" }, 0.4);
```

## Critical Rules
- **Do not wipe horizontally over text.** If slicing vertically (columns), wipe vertically (bottom to top). Wiping horizontally across text creates an illegible "bar chart" look. 
- **Scale under the mask:** For added depth, slowly scale the incoming element (`scale: 1.1` to `1`) over the entire duration of the wipe (e.g., 1s) so the image moves independently of the mask columns.
