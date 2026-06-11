# FLIP Layout Scroll Orchestration

## Visual Description
During a scroll sequence, an image or block of text appears to seamlessly un-parent itself from one section of the grid and fly into a completely different container, resizing fluidly as it travels.

## Emotional Register
Fluid and unbroken.

## Technical Mechanics
- **DOM Structure:** Two distinct containers in the DOM structure representing the start and end states of the animated element.
- **CSS Properties:** Standard layout properties (flex/grid, width, height, absolute/relative positioning).
- **JS Engine:** GSAP FLIP Plugin.
- **Key Timeline Logic:** Records the element's bounding box, alters the DOM state (re-parenting), calculates the delta, and animates the inversion.

## Code Snippet / Reverse Engineering Brief
**Code Unavailable — Reverse Engineering Brief**
This uses the First, Last, Invert, Play (FLIP) technique. 
1. Get the current state of the element (`Flip.getState(element)`).
2. Change the DOM (e.g., move the element to its new parent container, or toggle a class that changes its styling/size).
3. Call `Flip.from(state, { duration: 1, ease: "power2.inOut" })`. This animates the element from its old position and size to its newly calculated position and size in the DOM smoothly. 
When bound to a scroll event, this can be scrubbed using ScrollTrigger.

Source Reference: https://www.noqode.fr/en/outils/gsap

## Metadata
- **Industry Name(s):** First-Last-Invert-Play Transitions
- **Rarity:** UNCOMMON
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH
- **Accessibility / Reduced Motion:** Simply execute the DOM state change without calling `Flip.from()` to instantly snap the element to its new position.
