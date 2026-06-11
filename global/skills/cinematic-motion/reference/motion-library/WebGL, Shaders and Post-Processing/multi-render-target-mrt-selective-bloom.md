# Multi-Render-Target (MRT) Selective Bloom

## Visual Description
The viewport displays a complex architectural model. As highlights pass over specific details, only those designated elements—such as vector lines or particle borders—glow with an intense, ethereal bloom, while the surrounding dark layout remains perfectly sharp and clean. The glowing effects remain isolated to their targets, avoiding the blurry, washed-out look typical of standard, full-screen bloom passes.

## Emotional Register
The isolated glows feel ethereal and modern, creating a high-contrast visual hierarchy that draws focus to key spatial structures.

## Technical Mechanics
- **DOM Structure:** WebGL overlay canvas element.
- **CSS Properties:** Absolute viewport overlay coordinates.
- **JS Engine:** Three.js using standard WebGL2 rendering targets.
- **Key Timeline Logic:** The scene utilizes Multi-Render-Target (MRT) configurations to write multiple outputs simultaneously. The primary target records normal color information, while a secondary target isolates glow-specific values (e.g., emissive colors). The bloom pass is applied exclusively to the secondary target's buffer, and then merged with the primary scene, keeping the overall viewport sharp.
- **Easing Curve:** Decoupled scroll-scrub using a heavy damping curve: `scrub: 2.2`.
- **Shader/WebGL:** Multi-render target allocations route emissive materials to a separate framebuffer attachment. Only this secondary buffer is passed to the downscaled bloom filter before compositing back to the main display.
- **Performance Notes:** Highly performant; isolates the expensive blur operations to a smaller, downscaled buffer, reducing GPU fill-rate demands.

## Code Snippet / Reverse Engineering Brief
```javascript
import * as THREE from 'three';

// Selective Bloom Target Setup
const initSelectiveBloomMRT = (renderer, width, height) => {
  // WebGLMultipleRenderTargets is used to render to multiple textures at once
  const mrtTarget = new THREE.WebGLMultipleRenderTargets(width, height, 2);
    
  // Set properties on target render frames
  mrtTarget.texture[0].name = "diffuse";
  mrtTarget.texture[1].name = "glow";
    
  return mrtTarget;
};
```

## Metadata
- **Industry Name(s):** MRT Selective Bloom, Glowing Edge Post-Processing
- **Rarity:** ULTRA-RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH
- **Accessibility / Reduced Motion:** Ensure bloom intensity can be reduced or disabled based on `prefers-reduced-motion`.
