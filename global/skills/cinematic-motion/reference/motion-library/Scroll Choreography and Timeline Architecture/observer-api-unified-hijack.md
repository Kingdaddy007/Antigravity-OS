# Observer API Unified Hijack

## Visual Description
The traditional scrollbar is missing. Scrolling the wheel or swiping the screen triggers distinct, non-continuous 3D animations or slide changes without moving the viewport natively.

## Emotional Register
App-like and highly immersive.

## Technical Mechanics
- **DOM Structure:** Hidden scrollbar (`overflow: hidden` on body or main wrapper) with full viewport sections.
- **CSS Properties:** `height: 100vh; overflow: hidden;`
- **JS Engine:** GSAP Observer Plugin.
- **Key Timeline Logic:** Normalizes wheel, touch, and pointer events into unified callbacks to trigger discrete timelines, bypassing native scrolling entirely.

## Code Snippet / Reverse Engineering Brief
**Code Unavailable — Reverse Engineering Brief**
The GSAP Observer plugin is used to listen to intent rather than actual scroll events. By setting up `Observer.create({ target: window, type: "wheel,touch,pointer", onUp: () => previousSlide(), onDown: () => nextSlide() })`, the developer hijacks the user's input devices. Instead of native scrolling, an explicit timeline (like a WebGL transition or a DOM slide animation) is fired. State management (e.g., a variable tracking `currentSlide`) ensures animations don't overlap if the user scrolls too quickly.

Source Reference: https://www.noqode.fr/en/outils/gsap

## Metadata
- **Industry Name(s):** Wheel/Touch Hijacking
- **Rarity:** RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH
- **Accessibility / Reduced Motion:** Provide explicit keyboard navigation (up/down arrows) or fallback native scrolling for users requiring standard interactions. Ensure focus management works across the "slides."
