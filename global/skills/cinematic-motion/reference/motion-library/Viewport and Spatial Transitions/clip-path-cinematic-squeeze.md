# Spatial Re-framing: Cinematic Aspect Ratio Squeeze

## Visual Description
The transition begins with a full-bleed, edge-to-edge video or image filling the entire viewport. Rather than scaling or morphing the physical dimensions of the element (which can cause warping or stretching), a sharp, rectangular mask rapidly closes in from the edges. The viewport is "squeezed" into a smaller, precise geometric window (e.g., shifting to the left half of the screen), instantly creating a massive block of negative space on the opposite side to introduce new content.

## Emotional Register
Authoritative, structured, and highly editorial. It feels like a gallery curator suddenly placing a frame around a raw piece of art. It instantly shifts the user's attention and commands focus, providing a dramatic structural pivot without losing the continuity of the video.

## Technical Mechanics
- **Core Technology:** GSAP + CSS `clip-path: inset(...)`
- **Performance:** Exceptionally high. `clip-path` is heavily optimized by modern browsers and does not trigger expensive layout repaints or text reflows compared to animating `width` or `padding`.
- **Properties:** `clip-path: inset(top right bottom left round border-radius)`

## Execution Strategy
To achieve this, the target container must have the video set to `object-fit: cover` with 100% width and height. The GSAP animation then scrubs the `clipPath` property from `inset(0)` (fully open) to a constrained rectangle.

### Code
```javascript
// Example: Squeezing a full-bleed hero video into a left-aligned cinematic portrait
gsap.to('.hero-video-container', {
  // inset(top right bottom left round border-radius)
  // Here, we push in 15vh from top/bottom, 55vw from the right (creating massive negative space), and 5vw from the left.
  clipPath: "inset(15vh 55vw 15vh 5vw round 24px)",
  ease: "power3.inOut",
  duration: 1.5,
  scrollTrigger: {
    trigger: ".hero-section",
    start: "top top",
    scrub: true,
    pin: true
  }
});
```

## Accessibility / Reduced Motion
For users with `prefers-reduced-motion`, simply default the `clip-path` to the final inset state statically, or replace the morph with a subtle opacity fade of the new adjacent content.
