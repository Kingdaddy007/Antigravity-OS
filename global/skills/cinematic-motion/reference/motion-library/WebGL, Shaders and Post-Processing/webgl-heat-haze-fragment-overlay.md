# WebGL Heat Haze Fragment Overlay

## Visual Description
The background imagery or hero text is visually modulated by a slow-moving, shimmering distortion, identical to the optical illusion of heat radiating off a tarmac. The distortion does not change the layout or geometry but bends the pixels underneath smoothly.

## Emotional Register
Visceral, sweltering, and heavily atmospheric. Perfect for setting an intense mood before any user interaction occurs.

## Technical Mechanics
- **DOM Structure:** Canvas rendering a single plane geometry covering the entire viewport.
- **JS Engine:** Three.js or raw WebGL.
- **Shader/WebGL:** Fragment shader utilizing Simplex Noise or Perlin Noise math to alter UV coordinates before sampling the main texture.

## Code Snippet / Reverse Engineering Brief
**Reverse Engineering Brief:** Load the target image as a uniform `sampler2D`. Pass a continuously updating `u_time` uniform. In the fragment shader, generate a noise map `float noise = snoise(uv * scale + u_time)`. Displace the uv coordinates by the noise value (`uv += noise * intensity`) before rendering the final `texture2D` output.

## Metadata
- **Industry Name(s):** Heat Distortion Shader, Atmospheric Noise Overlay
- **Rarity:** RARE
- **Implementation Confidence:** HIGH
- **Production Feasibility:** HIGH (A relatively inexpensive shader to run. Can be easily layered over other standard DOM elements utilizing CSS `pointer-events: none`.)
- **Accessibility / Reduced Motion:** Provide a static fallback or freeze the `u_time` uniform for users requesting reduced motion.
