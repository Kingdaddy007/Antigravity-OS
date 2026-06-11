# Assembly Layout Construction Pinning

## Visual Description
The user scrolls into a section consisting merely of scattered horizontal and vertical lines and isolated typographic blocks. Upon hitting the section boundary, the scroll is arrested (pinned). Continuing to scroll down does not move the page; instead, it physically pulls the scattered lines and blocks together. They slide along tracks, assembling into a perfectly structured, cohesive layout (e.g., an article preview). Only when the assembly is 100% complete does the scroll un-pin, allowing the user to proceed down the page.

## Emotional Register
Architectural and highly deliberate. Turns the user's scroll wheel into a physical construction mechanism.

## Technical Mechanics
- **DOM Structure:** Complex absolute positioning mapping elements to precise final coordinates.
- **CSS Properties:** `transform: translate()` arrays.
- **JS Engine:** GSAP ScrollTrigger.
- **Key Timeline Logic:** A master `gsap.timeline({ scrollTrigger: { scrub: true, pin: true } })`. Specific `.to()` calls interpolate the starting coordinate of every element toward 0,0 relative to their parent containers.

## Code Snippet / Reverse Engineering Brief
**Code Unavailable — Reverse Engineering Brief**
Requires defining the final layout visually in CSS first. Then, in JS, calculate the initial offset state for every element (e.g., title starts -500px left, image starts 1000px down). Bind these to a master timeline. The pinning duration is dictated by the `end: "+=2000"` parameter, meaning the user must scroll 2000 pixels to complete the assembly sequence. 

## Metadata
- **Industry Name(s):** Deconstructed Grid Assembly, Line-to-Content Pin
- **Rarity:** RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** LOW (Reflow and responsive breakage are highly probable. Requires separate timeline definitions for mobile vs. desktop layouts using `ScrollTrigger.matchMedia()`.)
- **Accessibility / Reduced Motion:** If `prefers-reduced-motion` is detected, elements should be displayed in their final assembled state immediately without scroll tracking.
