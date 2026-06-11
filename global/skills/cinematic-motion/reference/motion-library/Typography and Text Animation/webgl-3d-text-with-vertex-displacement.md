# WebGL 3D Text with Vertex Displacement

## Visual Description
Text is rendered as 3D geometry in WebGL (using Three.js TextGeometry), then vertex positions are manipulated via custom shaders. A common pattern: vertices are displaced along their normals based on noise functions (Simplex, Perlin) or sine waves, creating a "breathing" or rippling effect. The text appears to pulse, wave, or undulate in 3D space. Unlike SVG morphing, this is true volumetric distortion with depth and lighting. Can be combined with post-processing effects (bloom, chromatic aberration) for cyberpunk aesthetics. The effect is computationally expensive and typically reserved for hero text on high-end sites. Text remains legible at rest but distorts expressively during animation or interaction (mouse proximity, scroll progress).

## Emotional Register
Futuristic, technical, immersive, high-concept. The 3D volumetric nature makes digital text feel like a tangible, physical material reacting to unseen forces. Appropriate for tech product launches, gaming brands, and speculative design showcases.

## Technical Mechanics
* **DOM Structure:** WebGL canvas element overlaying page, text rendered via Three.js scene
* **CSS Properties:** N/A (rendered via WebGL, not DOM text)
* **JS Engine:** Three.js + custom GLSL shaders
* **Key Timeline Logic:** Animate shader uniforms (time, displacement amount) via `requestAnimationFrame` or GSAP `.to(uniforms.uDisplacement, {value: 0.5})`
* **Easing Curve:** Handled in shader via smoothstep or custom easing functions
* **Shader/WebGL:** Vertex shader displaces positions along normals: `position += normal * sin(position.x * frequency + time) * amplitude;`
* **Performance Notes:** GPU-intensive; requires discrete GPU for smooth 60fps. Fallback to 2D text for mobile/low-power devices. Use lower-poly geometry (reduce `curveSegments` in TextGeometry) for performance.

## Code Snippet / Reverse Engineering Brief
```javascript
import * as THREE from 'three';
import { FontLoader } from 'three/examples/jsm/loaders/FontLoader.js';
import { TextGeometry } from 'three/examples/jsm/geometries/TextGeometry.js';

// Basic Scene Setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 5;

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Load Font and Create Displaced Text Geometry
const fontLoader = new FontLoader();
let material; // Keep reference to animate uniforms

fontLoader.load('path/to/font.json', (font) => {
  const textGeo = new TextGeometry('ATELIER', {
    font: font,
    size: 1,
    height: 0.3,
    curveSegments: 10,
  });
  textGeo.center();
  
  material = new THREE.ShaderMaterial({
    uniforms: {
      uTime: { value: 0 },
      uAmplitude: { value: 0.1 }
    },
    vertexShader: `
      uniform float uTime;
      uniform float uAmplitude;
      varying vec3 vPosition;
      
      void main() {
        vPosition = position;
        vec3 pos = position;
        
        // Displacement along normal using a simple sine wave
        pos += normal * sin(position.x * 2.0 + uTime) * uAmplitude;
        
        gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
      }
    `,
    fragmentShader: `
      void main() {
        // Output solid white text
        gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
      }
    `
  });
  
  const mesh = new THREE.Mesh(textGeo, material);
  scene.add(mesh);
});

// Animation loop
const clock = new THREE.Clock();

function animate() {
  requestAnimationFrame(animate);
  if (material) {
    material.uniforms.uTime.value = clock.getElapsedTime() * 2.0; // Speed adjustment
  }
  renderer.render(scene, camera);
}
animate();
```

## Metadata
- **Industry Name(s):** Displaced Text Geometry, Shader-Based Text Distortion, Three.js Text Morph
- **Rarity:** ULTRA-RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** LOW (Requires WebGL expertise, font conversion, and careful performance tuning)
- **Accessibility / Reduced Motion:** For `prefers-reduced-motion` or on mobile, replace WebGL canvas with standard DOM text. Use `<noscript>` fallback with plain text for screen readers. Provide a "Reduce Motion" toggle in UI for user control.
