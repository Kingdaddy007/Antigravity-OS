# FBO Ping-Pong Fluid Displacement Simulation

## Visual Description
The viewport captures cursor movements and converts them into dynamic velocity fields on the GPU. As the cursor sweeps across the screen, it acts as a fluid emitter, leaving behind an organic trail of fluid displacement. This trail spreads, rotates, and dissolves across the layout like ink in water, distorting background typography, images, and layout elements with realistic fluid dynamics before slowly dissipating.

## Emotional Register
The effect is immersive and tactile, creating a physical, responsive connection between user movement and the visual environment.

## Technical Mechanics
- **DOM Structure:** Standard layout wrapper containing the WebGL renderer canvas overlay.
- **CSS Properties:** The canvas and HTML content match dimensions perfectly.
- **JS Engine:** Three.js coordinates the feedback loop rendering.
- **Key Timeline Logic:** The fluid simulation uses a ping-pong feedback loop with two render targets. Each frame, the simulation reads state from the first target and writes the updated physics pass to the second target, swapping them for the next cycle. The resulting velocity map is passed as a displacement uniform to the main rendering pass, shifting coordinates dynamically.
- **Easing Curve:** Controlled by physics-based fluid solvers: dynamic viscosity decay.
- **Shader/WebGL (if applicable):** Written in TSL. Coordinates are displaced using FBM noise: `const disp = mul(fbm(add(mul(uv(), float(20.0)), uTime)), float(0.01));` The shader blends neighbors using a custom darken function: `min(blend, base)`.
- **Performance Notes:** Highly advanced. Instancing (`InstancedMesh`) is used to render multiple model copies in a single draw call. The ping-pong buffers are scaled down (e.g., to 512x512) to maintain performance on integrated GPUs.

## Code Snippet / Reverse Engineering Brief

```javascript
import { uv, texture, vec2, add, sub, mul, min, float } from 'three/tsl';

export const FluidSimulationNode = (prevNode, inputNode, aspectVec) => {
  const uvCoord = uv();
    
  // Calculate displacement offset
  const disp = mul(vec2(0.01), aspectVec);
    
  // Sample adjacent coordinates
  const sampleCenter = prevNode.sample(uvCoord);
  const sampleLeft = prevNode.sample(vec2(add(uvCoord.x, disp.x), uvCoord.y));
  const sampleRight = prevNode.sample(vec2(sub(uvCoord.x, disp.x), uvCoord.y));
  const sampleTop = prevNode.sample(vec2(uvCoord.x, add(uvCoord.y, disp.y)));
  const sampleBottom = prevNode.sample(vec2(uvCoord.x, sub(uvCoord.y, disp.y)));
    
  // Apply darken blend comparison
  const blendValue = min(sampleCenter, min(min(sampleLeft, sampleRight), min(sampleTop, sampleBottom)));
    
  // Mix dynamic input
  const pointerInput = inputNode.sample(uvCoord);
  const composite = min(blendValue, pointerInput);
    
  // Decay output
  const fadeValue = add(composite.rgb, float(0.015));
  return min(vec2(1.0), fadeValue);
};
```

## Metadata
- **Industry Name(s):** FBO Fluid Simulation, GPU Velocity Displacement
- **Rarity:** ULTRA-RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** MEDIUM (Highly demanding on GPU resources; mobile execution requires resolution downscaling.)
- **Accessibility / Reduced Motion:** Disable the fluid solver and fallback to static rendering if reduced motion is preferred.
