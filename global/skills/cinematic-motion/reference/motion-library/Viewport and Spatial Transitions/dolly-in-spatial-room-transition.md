# Dolly-In Spatial Room Transition

## Visual Description
The viewport functions as a dynamic spatial narrative, where scrolling moves the virtual camera through three-dimensional space. The camera passes through a doorway or architectural opening, transitioning directly into the coordinate system of a secondary scene. As the camera passes through the boundary, the lighting and background environments shift seamlessly, creating an immersive, continuous spatial narrative.

## Emotional Register
The continuous camera sweep evokes a sense of architectural grandeur, providing structured perspective shifts that feel intentional.

## Technical Mechanics
- **DOM Structure:** Two distinct spatial rooms are modeled within a single Three.js viewport canvas.
- **CSS Properties:** Fullscreen absolute canvas container coordinates are used.
- **JS Engine:** Three.js coordinates the camera mathematics, while GSAP ScrollTrigger manages timeline orchestration.
- **Key Timeline Logic:** A master GSAP timeline maps coordinates along Bezier curves for both the camera's position vector and its target look-at vector. As the camera crosses the transition boundary, the primary room is culled from rendering, optimizing rendering resources.
- **Easing Curve:** Decoupled scroll-scrub using a heavy damping curve: scrub: 2.2.
- **Performance Notes:** Highly performant; isolates rendering operations to active 3D models on the GPU, avoiding layout reflows during camera transitions.

## Code Snippet / Reverse Engineering Brief
```javascript
// Camera Path Portal Interpolation Concept
const transitionCameraThroughPortal = (camera, targetZ, nextSceneSetup) => {
  const tl = gsap.timeline({
    scrollTrigger: {
      trigger: ".transition-trigger",
      start: "top top",
      end: "bottom top",
      scrub: 1.5
    }
  });

  // Dolly camera forward along Z-axis, passing through coordinates
  tl.to(camera.position, {
    z: targetZ,
    ease: "power2.inOut",
    onUpdate: () => {
      if (camera.position.z > targetZ * 0.8) {
        nextSceneSetup(); // Load assets into secondary coordinates
      }
    }
  });
};
```

## Metadata
- **Industry Name(s):** Spatial Camera Depth Transition, Dolly Zoom Portal Transition, Cinematic Dolly Pass
- **Rarity:** RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** MEDIUM
- **Accessibility / Reduced Motion:** Needs fallback standard CSS transitions (like fade or simple translate) for users with prefers-reduced-motion, as forced 3D camera movement can cause motion sickness.
