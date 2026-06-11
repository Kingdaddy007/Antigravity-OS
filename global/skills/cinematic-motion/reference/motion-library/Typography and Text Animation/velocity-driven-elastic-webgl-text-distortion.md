# Velocity-Driven Elastic WebGL Text Distortion

## Visual Description
The screen display begins with standard typographic elements aligned perfectly within the viewport. As the user initiates a scroll, the underlying DOM text is hidden, and the WebGL-rendered character meshes are subjected to a custom vertex shader deformation. As scroll velocity increases, the text stretches vertically along its Y-axis or deforms along a sine-wave path, reaching maximum elongation during peak scroll acceleration. Once the scroll input ceases, the velocity-driven distortion decays elastically via a smooth ease-out, returning the letters to their razor-sharp, static vector positions. The animation feels organic, imitating a viscous liquid stretching under tension before reforming.

## Emotional Register
The viewer experiences a profound sense of tactile weight and physical responsiveness, making the digital medium feel plastic, elastic, and highly coordinated.

## Technical Mechanics
- **DOM Structure:** Standard HTML elements marked with `data-animation="webgl-text"` are parsed by the JavaScript engine. A full-screen `<canvas>` element is styled with `position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: -1;` to overlay the scene.
- **CSS Properties:** The original HTML text is styled responsively using viewport units (vw, vh) and then set to `opacity: 0` or `visibility: hidden` once WebGL synchronization is established.
- **JS Engine:** Three.js coordinates the 3D scene, using the `troika-three-text` library or `three-bmfont-text` to generate high-fidelity SDF/MSDF text geometry. Lenis handles the smooth scrolling input and exposes scroll velocity.
- **Key Timeline Logic:** During the initialization phase, the bounding rect of the DOM element is mapped to WebGL coordinates. Inside the `requestAnimationFrame` render loop, the raw scroll velocity is processed through a linear interpolation (lerp) equation to avoid jarring visual jitter. This smoothed value is continuously passed to the shader as the uniform `uVelocity`.
- **Easing Curve:** Decay uses an elastic ease-out modeled dynamically as a spring system: custom spring (mass: 1.2, stiffness: 120, damping: 14).
- **Shader/WebGL:** Custom vertex shader applying a sine wave distortion where the intensity scales with the `uVelocity` uniform: `displacement = sin(uv.y * PI) * uVelocity * amplitude`.
- **Performance Notes:** High performance is maintained by avoiding continuous DOM layout reflows; bounding client rectangles are cached on window resize and never queried during scroll.

## Code Snippet / Reverse Engineering Brief
```javascript
import * as THREE from 'three';
import { Text } from 'troika-three-text';

class WebGLTextElement {
  constructor(domElement, scene, camera) {
    this.domElement = domElement;
    this.scene = scene;
    this.camera = camera;
    this.mesh = new Text();
    this.init();
  }

  init() {
    const rect = this.domElement.getBoundingClientRect();
    const computed = window.getComputedStyle(this.domElement);
      
    this.mesh.text = this.domElement.innerText;
    // Strip "px" and parse float
    this.mesh.fontSize = parseFloat(computed.fontSize);
    
    // troika-three-text requires a URL to a font file (.ttf, .woff, .json)
    // Using computed.fontFamily directly won't work in WebGL context unless mapped to a URL.
    // Assuming 'fontUrl' is resolved based on computed.fontFamily logic
    // this.mesh.font = getFontUrl(computed.fontFamily); 
    
    this.mesh.color = computed.color;
    
    // Handle "normal" letterSpacing
    const spacing = computed.letterSpacing === 'normal' ? '0' : computed.letterSpacing;
    this.mesh.letterSpacing = parseFloat(spacing) || 0;
    
    // Add custom material with uniforms for vertex distortion
    this.mesh.material = new THREE.MeshBasicMaterial(); // Placeholder, requires custom ShaderMaterial
    // To apply troika's built-in shader injection:
    this.mesh.material.onBeforeCompile = (shader) => {
      shader.uniforms.uVelocity = { value: 0 };
      // Inject vertex shader logic here...
    };
      
    this.updatePosition(rect);
    this.scene.add(this.mesh);
    
    // Sync text to ensure geometry is created
    this.mesh.sync();
    
    // Hide DOM element after matching coordinates
    this.domElement.style.opacity = 0; 
  }

  updatePosition(rect) {
    // Convert DOM pixels to 3D world space coordinates
    // Assumes OrthographicCamera or correctly configured PerspectiveCamera matching screen pixels
    const x = rect.left - window.innerWidth / 2 + rect.width / 2;
    const y = -rect.top + window.innerHeight / 2 - rect.height / 2;
    this.mesh.position.set(x, y, 0);
  }
}
```

## Metadata
- **Industry Name(s):** Velocity-Driven Shader-Displaced Text, Scroll-Distorted Kinetic Typography, Scroll-Driven Text Stretch
- **Rarity:** ULTRA-RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** MEDIUM. Complex mapping between DOM coordinates and WebGL space required. `troika-three-text` requires fetching font files directly, meaning system fonts cannot be easily rendered via this method.
- **Accessibility / Reduced Motion:** Bypassed completely if reduced motion is requested. The WebGL canvas should not render text, and the original DOM element opacity should remain 1.
