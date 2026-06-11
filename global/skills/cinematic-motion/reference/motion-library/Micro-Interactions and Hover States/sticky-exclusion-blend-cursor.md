# Sticky Exclusion Blend Cursor

## Visual Description
The native operating system cursor is hidden. A custom, smooth-following circle replaces it. When the cursor passes over specific background imagery, the circle perfectly inverts the colors beneath it. When hovering over a link or button, the circle snaps to the boundaries of the element, absorbing its shape (becoming a rounded rectangle) and locking onto it magnetically, rather than continuing to follow the exact mouse coordinate.

## Emotional Register
Integrated and highly cohesive. Reminds the user that the interface is a reactive, contextual ecosystem rather than a static document.

## Technical Mechanics
- **DOM Structure:** An absolutely positioned `<div class="cursor">` appended to the end of the `<body>`.
- **CSS Properties:** `mix-blend-mode: exclusion` or `difference`, `pointer-events: none`, `position: fixed`.
- **JS Engine:** React Creative Cursor or vanilla `requestAnimationFrame` interpolation.
- **Key Timeline Logic:** Lerp function calculating distance between current native mouse position and custom cursor div position to create trailing delay.

## Code Snippet / Reverse Engineering Brief
```javascript
// Pseudo-logic derived from sticky cursor libraries 
let mouse = { x: 0, y: 0 };
let pos = { x: 0, y: 0 };
let speed = 0.1;
const cursor = document.querySelector('.cursor');

window.addEventListener('mousemove', e => {
  mouse.x = e.clientX;
  mouse.y = e.clientY;
});

const loop = () => {
  pos.x += (mouse.x - pos.x) * speed;
  pos.y += (mouse.y - pos.y) * speed;
  if (cursor) {
    cursor.style.transform = `translate(${pos.x}px, ${pos.y}px)`;
  }
  requestAnimationFrame(loop);
}
loop();
```

## Metadata
- **Industry Name(s):** Magnetic Blend Cursor, Sticky Cursor
- **Rarity:** COMMON
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH
- **Accessibility / Reduced Motion:** Must be disabled entirely via CSS media queries on touch devices (`@media (pointer: coarse)`). Restores default OS cursor if reduced motion is preferred to prevent orientation loss for visually impaired users.
