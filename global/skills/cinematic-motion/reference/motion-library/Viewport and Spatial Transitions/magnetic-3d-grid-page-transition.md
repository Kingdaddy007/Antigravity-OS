# Magnetic 3D Grid Page Transition

## Visual Description
A grid of projects is displayed. When hovering, the grid physically tilts in 3D space toward the cursor. Upon clicking, the selected image breaks free from the grid, rushing forward to fill the entire viewport, while the rest of the grid recedes into extreme depth and darkness, seamlessly transitioning the user to the project detail page.

## Emotional Register
Vast, physical, and deeply engaging.

## Technical Mechanics
- **DOM Structure:** Grid layout with heavy perspective.
- **CSS Properties:** perspective, transform: rotateX() rotateY() translateZ().
- **JS Engine:** GSAP FLIP or explicit coordinate mapping.
- **Key Timeline Logic:** Cursor coordinates mapped to grid rotation. Click events trigger a timeline that maps the clicked item's bounding box to 100vw / 100vh.

## Code Snippet / Reverse Engineering Brief
Utilize `gsap.utils.mapRange` to tie the mousemove event to the wrapper's `rotateX` and `rotateY` properties (e.g., -15deg to 15deg). On click, utilize the FLIP plugin: record the state of the image, reparent it to the body, and animate it to a `position: fixed; top: 0; left: 0; width: 100%; height: 100%` state, while animating the wrapper's z translation negatively.

## Metadata
- **Industry Name(s):** 3D Grid Preview Transition, Magnetic Portal
- **Rarity:** RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** MEDIUM. FLIP transitions are robust, but managing the state between single-page application routes requires highly careful lifecycle management.
- **Accessibility / Reduced Motion:** Disable 3D tilt on hover and replace page expansion with a standard fade transition for reduced motion users.
