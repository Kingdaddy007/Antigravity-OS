# Volumetric Fog & Depth-of-Field Post-Processing

## Visual Description
As the camera orbits, visual elements dissolve into soft, atmospheric fog in the background. Foreground elements are framed by a shallow depth-of-field blur, creating a cinematic sense of depth.

## Emotional Register
The volumetric fog creates an ethereal, mysterious atmosphere, drawing focus to key spatial structures with physical depth.

## Technical Mechanics
- **DOM Structure:** WebGL canvas overlay absolute-positioned to cover the viewport.
- **CSS Properties:** Styled with absolute coordinates and `pointer-events: none` disabled.
- **JS Engine:** Three.js with post-processing effect composers.
- **Key Timeline Logic:** Depth buffers are sampled dynamically to calculate focal distances. Blur kernels are scaled based on distance coordinates, fading background elements into volumetric fog.
- **Easing Curve & Timing:** Gradual decelerating curve: `sine.out`.
- **Performance Notes:** Highly advanced post-processing; requires downscaled depth buffers to run smoothly on mobile devices.

## Code Snippet / Reverse Engineering Brief
**Code Unavailable — Reverse Engineering Brief**
This effect utilizes Three.js post-processing effect composers. The depth buffer is sampled dynamically to calculate focal distances. Blur kernels scale based on distance coordinates, fading background elements into volumetric fog. Due to its advanced nature, it requires downscaling depth buffers to maintain performance, especially on mobile devices. 

Source Reference: https://tympanus.net/codrops/2025/11/19/how-to-build-cinematic-3d-scroll-experiences-with-gsap/

## Metadata
- **Industry Name(s):** Volumetric Atmospheric Fog, Depth of Field Pass
- **Rarity:** RARE
- **Implementation Confidence:** MEDIUM
- **Production Feasibility:** MEDIUM
- **Accessibility / Reduced Motion:** Bypasses post-processing passes when prefers-reduced-motion is enabled.
