# Kinetic WebGL Render-Target Text Projection

## Visual Description
A 3D geometry (such as a cylinder, box, or wave plane) rotates slowly in a pitch-black scene. The surface of this geometry serves as a mapping layer for highly detailed, repeated kinetic typography. The text is rendered dynamically in code onto an offscreen Render Target texture, meaning the typography is infinitely crisp and updates in real-time. The text moves, repeats, and flows across the deformed mesh's surface, sliding over its faces and bending around its corners.

## Emotional Register
The viewer experiences sculptural authority and experimental digital craft, conveying high complexity and technological prestige.

## Technical Mechanics
* **DOM Structure:** A single full-screen canvas wrapper.
* **CSS Properties:** Absolute viewport positioning with a transparent alpha channel.
* **JS Engine:** Three.js combined with a library like `three-bmfont-text` to generate vector-based text within an isolated sub-scene.
* **Key Timeline Logic:** An offscreen sub-scene containing the text mesh is rendered into a WebGLRenderTarget. This render target's texture is passed as a uniform `uTexture` into the material of the main mesh (e.g., a rotating box). The rendering loop processes the sub-scene first, updates the texture, and then renders the main scene.
* **Easing Curve:** Continuously driven by time variables (`uTime`) or smooth inertial inputs: linear for constant movement, or custom easing transitions.
* **Shader/WebGL:** Inside the main fragment shader, the uv coordinates are repeated and offset using time-based uniforms. The material sample is drawn using a texture2D lookup: `vec3 textSample = texture2D(uTexture, shiftedUv).rgb;`
* **Performance Notes:** Requires careful execution; the sub-scene should only render when the text changes or is moving. Unnecessary render cycles on stationary text will trigger thermal throttling on mobile devices.

## Code Snippet / Reverse Engineering Brief
```javascript
import * as THREE from 'three';

// Render Target Initialization for Dynamic Text Texture
const rtWidth = 1024;
const rtHeight = 1024;
const renderTarget = new THREE.WebGLRenderTarget(rtWidth, rtHeight, {
  minFilter: THREE.LinearFilter,
  magFilter: THREE.LinearFilter,
  format: THREE.RGBAFormat
});

const rtScene = new THREE.Scene();
const rtCamera = new THREE.PerspectiveCamera(45, 1, 0.1, 10);
rtCamera.position.z = 2.5;

// Main mesh using Render Target as texture mapping
const mainGeometry = new THREE.BoxGeometry(1, 1, 1);
const mainMaterial = new THREE.ShaderMaterial({
  vertexShader: `
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
  fragmentShader: `
    varying vec2 vUv;
    uniform sampler2D uTexture;
    uniform float uTime;
    void main() {
      // Offset texture to animate scrolling typography over surface
      vec2 shiftedUv = vec2(fract(vUv.x + uTime * 0.05), vUv.y);
      vec3 color = texture2D(uTexture, shiftedUv).rgb;
      gl_FragColor = vec4(color, 1.0);
    }
  `,
  uniforms: {
    uTexture: { value: renderTarget.texture },
    uTime: { value: 0 }
  }
});
const mainMesh = new THREE.Mesh(mainGeometry, mainMaterial);

// Render loop skeleton
const clock = new THREE.Clock();

function animate(renderer, mainScene, mainCamera) {
  requestAnimationFrame(() => animate(renderer, mainScene, mainCamera));
  const elapsedTime = clock.getElapsedTime();
  
  // Update uniforms
  mainMaterial.uniforms.uTime.value = elapsedTime;

  // 1. Render the text scene into the offscreen render target
  renderer.setRenderTarget(renderTarget);
  renderer.render(rtScene, rtCamera);

  // 2. Render the main scene to the screen
  renderer.setRenderTarget(null);
  renderer.render(mainScene, mainCamera);
}
```

## Metadata
- **Industry Name(s):** Kinetic RT Text Projection, WebGL Typographic Mesh Deformation
- **Rarity:** RARE
- **Implementation Confidence:** Medium (Requires Three.js text rendering setup)
- **Production Feasibility:** Medium (Needs optimization for mobile devices)
- **Accessibility / Reduced Motion:** Render target animations should be paused based on `prefers-reduced-motion`. Fallback to standard 2D static typography.
