# Dual-Scene Fluid X-Ray Transition

## Visual Description
The viewport renders a highly detailed architectural structure in its primary state (e.g., concrete texture and warm lighting). When the cursor sweeps across the screen, it acts as a fluid emitter, leaving behind an organic, bleeding mask of liquid distortion. Inside the track of this fluid trail, the underlying scene shifts to reveal a completely separate, perfectly aligned secondary scene (e.g., a wireframe blueprint glowing with electric Fresnel edges). The liquid mask bleeds outward with procedural fluid dynamics and then slowly dissipates, closing the structural portal.

## Emotional Register
The viewer experiences a sense of revelation and structural curiosity, peeling back aesthetic skin to discover hidden complexity.

## Technical Mechanics
- **DOM Structure:** A single full-screen canvas wrapper capturing cursor events.
- **CSS Properties:** The canvas coordinates match the window dimensions precisely.
- **JS Engine:** Three.js utilizing WebGPU capabilities or standard WebGL2 rendering targets.
- **Key Timeline Logic:** The pipeline runs two parallel scenes containing identically positioned geometries: the solidScene and the wireScene. In the main post-processing composition step, both scenes are rendered into individual framebuffers. A dynamic fluid simulation (using a ping-pong feedback loop) records cursor movements into a black-on-white texture. This texture acts as the interpolation weight between the two render targets.
- **Easing Curve:** Controlled by physics-based fluid solvers: dynamic viscosity decay.
- **Shader/WebGL:** The fluid simulation runs on the GPU via two swapped texture outputs (Ping-Pong). The compositing step samples the fluid mask texture: `const fluidMask = sub(float(1.0), this.fluidMaskNode.sample(screenUV).r);` A TSL `mix()` node interpolates the pixels: `mix(solidColor, wireColor, fluidMask)`.
- **Performance Notes:** Highly advanced. Instancing (`InstancedMesh`) is used to render multiple model copies in a single draw call. The ping-pong buffers are scaled down (e.g., to 512x512) to maintain performance on integrated GPUs.

## Code Snippet / Reverse Engineering Brief
```javascript
// Render logic executing Ping-Pong Buffer Swap
// Post-processing pipeline setup from WebGL dual-scene tutorials
class FluidTransitionPass {
  constructor(renderer, width, height) {
    this.renderer = renderer;
    // Two rendering targets for ping-pong feedback loop
    this.targetA = new THREE.WebGLRenderTarget(width, height);
    this.targetB = new THREE.WebGLRenderTarget(width, height);
    this.currentSource = this.targetA;
    this.currentDestination = this.targetB;
  }

  swap() {
    const temp = this.currentSource;
    this.currentSource = this.currentDestination;
    this.currentDestination = temp;
  }

  render(simulationScene, orthoCamera) {
    // Render simulation shader to current destination target
    this.renderer.setRenderTarget(this.currentDestination);
    this.renderer.render(simulationScene, orthoCamera);
    this.renderer.setRenderTarget(null);
      
    // Swap source and destination for the next frame's read operation
    this.swap();
  }
}
```

## Metadata
- **Industry Name(s):** Dual-Scene Fluid Mask Reveal, WebGL X-Ray Wipe
- **Rarity:** ULTRA-RARE
- **Implementation Confidence:** MEDIUM
- **Production Feasibility:** LOW. Requires robust understanding of WebGL buffer management, and substantial GPU resources.
- **Accessibility / Reduced Motion:** Avoid intense visual distortion by utilizing a simple dissolve or linear wipe fallback.
