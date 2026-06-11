# Velocity-Driven Chromatic Aberration & Wave Distortion

## Visual Description
During static states, the scene is clean and razor-sharp. As the user scrolls, a post-processing pass is activated, warping the screen with organic sine-wave distortions and separating color channels into red, green, and blue fringes. The intensity of both the waves and the RGB splitting scales linearly with the real-time velocity of the scroll engine, resolving back to perfect visual clarity when the scroll momentum naturally dissipates.

## Emotional Register
The visual shift creates a strong sense of kinetic energy and visual momentum, mirroring the physical effort of navigation.

## Technical Mechanics
- **DOM Structure:** Standard wrapper element containing the container node.
- **CSS Properties:** Absolute viewport positioning with transparent alpha channel.
- **JS Engine:** Three.js coordinates the WebGL rendering.
- **Key Timeline Logic:** Lenis or a similar smooth scroll engine tracks scroll velocity. This raw velocity is smoothed using a linear interpolation (lerp) loop inside the rendering loop to avoid abrupt visual jumps: `lerpedVelocity = lerpedVelocity + (targetVelocity - lerpedVelocity) * lerpFactor`. This smoothed velocity is updated as a uniform `uVelocity`. When `uVelocity > 0`, the post-processing shader shifts texture lookup offsets by channel to produce chromatic aberration, and deforms uv coordinates along a sine wave to create the wave distortion.
- **Easing Curve:** Spring-like decay using dynamic velocity damping.
- **Performance Notes:** High performance is maintained by avoiding continuous DOM layout reflows; bounding client rectangles are cached on window resize and never queried during scroll.

## Code Snippet / Reverse Engineering Brief

```javascript
// WebGL Post-Processing Composer Shader with Velocity RGB Shift & Wave
const PostProcessingShader = {
  uniforms: {
    tDiffuse: { value: null },
    uVelocity: { value: 0.0 },
    uTime: { value: 0.0 }
  },
  vertexShader: `
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
  fragmentShader: `
    uniform sampler2D tDiffuse;
    uniform float uVelocity;
    uniform float uTime;
    varying vec2 vUv;

    void main() {
      // Sine wave distortion scaling with velocity
      vec2 distortedUv = vUv;
      distortedUv.x += sin(vUv.y * 10.0 + uTime) * uVelocity * 0.05;
        
      // RGB Shift aberration scaling with velocity
      float shift = uVelocity * 0.02;
      float redChannel = texture2D(tDiffuse, distortedUv + vec2(shift, 0.0)).r;
      float greenChannel = texture2D(tDiffuse, distortedUv).g;
      float blueChannel = texture2D(tDiffuse, distortedUv - vec2(shift, 0.0)).b;
        
      gl_FragColor = vec4(redChannel, greenChannel, blueChannel, 1.0);
    }
  `
};
```

## Metadata
- **Industry Name(s):** Velocity Chromatic Aberration, Scroll-Wavy Post-Processing
- **Rarity:** RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH
- **Accessibility / Reduced Motion:** Ensure scroll velocity passes 0 into the `uVelocity` uniform if the user prefers reduced motion, bypassing the distortion entirely.
