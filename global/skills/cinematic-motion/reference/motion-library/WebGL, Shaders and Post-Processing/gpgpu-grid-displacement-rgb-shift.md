# GPGPU Grid Displacement RGB Shift

## Visual Description
An image is rendered not as a flat texture, but as an array of thousands of dense, minuscule squares (a grid). When the cursor sweeps over the image, the grid physically deforms; the squares scatter and displace radially around the cursor's focal point. As they scatter, their colors undergo severe chromatic aberration (RGB Shift)—the red, green, and blue channels split apart at the edges of the displacement radius, creating a digital, holographic glitch. The grid smoothly snaps back into alignment as the cursor passes.

## Emotional Register
Cybernetic, profound, and overwhelmingly computational. Demonstrates immense processing power executed natively in the browser.

## Technical Mechanics
- **DOM Structure:** Canvas overlay.
- **JS Engine:** Three.js with GPGPU (General-Purpose computing on Graphics Processing Units) logic.
- **Shader/WebGL:** Custom vertex and fragment shaders. Utilizes an FBO (Framebuffer Object) to calculate particle positions entirely on the GPU, avoiding critical CPU bottlenecks.
- **Key Timeline Logic:** Mouse position is passed into the shader as a uniform (`u_mouse`). The displacement distance determines the intensity of the RGB shift.
- **Performance Notes:** GPGPU is an absolute necessity here. Calculating the scatter mathematics for thousands of grid particles on the CPU (`requestAnimationFrame`) would cause terminal frame lag and crash the browser tab.

## Code Snippet / Reverse Engineering Brief
**Reverse Engineering Brief:** Requires a `DataTexture` holding original positional data. A compute shader takes the `u_mouse` uniform, calculates the Euclidean distance to each particle, and applies an outward velocity vector to the particle's position. In the fragment shader, texture sampling (`texture2D`) is called three distinct times with slight uv-offsets scaled by the displacement distance to create the separated RGB channels, compositing them into a final output vector.

## Metadata
- **Industry Name(s):** GPGPU Particle Grid, Pixel RGB Displacement
- **Rarity:** ULTRA-RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** LOW (Requires deep GLSL and GPGPU architecture knowledge. Mobile execution may fail entirely due to precision limits in mobile GPU shaders.)
- **Accessibility / Reduced Motion:** Requires a pure `<img>` fallback tag strictly enforced if WebGL context creation fails or if the user requests reduced motion at the OS level.
