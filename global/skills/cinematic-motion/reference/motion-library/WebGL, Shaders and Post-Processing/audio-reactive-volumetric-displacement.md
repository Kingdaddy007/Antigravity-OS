# Audio-Reactive Volumetric Displacement

## Visual Description
An image or graphic sits dormant. When audio playback begins, the image distorts, swells, and glitches in perfect synchronization with the frequencies of the audio track. The low-end bass kicks create massive radial bulges, while high-frequency hi-hats create sharp, static noise shifts across the horizontal plane.

## Emotional Register
Synesthetic and highly dynamic. Bridges auditory and visual senses seamlessly.

## Technical Mechanics
- **DOM Structure:** Canvas wrapper.
- **JS Engine:** p5.js, p5.sound library, WebGL context.
- **Key Timeline Logic:** `requestAnimationFrame` loop fetching `fft.analyze()`.
- **Shader/WebGL:** Audio frequency bands (bass, mid, treble) are mapped to arrays, normalized, and passed as uniforms to the fragment shader.

## Code Snippet / Reverse Engineering Brief
**Reverse Engineering Brief:** Initialize `p5.FFT`. During the draw loop, extract `fft.getEnergy("bass")` and map the value from (0, 255) to (0.0, 1.0). Pass this as `u_bass` to a custom shader. Inside the GLSL code, multiply the displacement map scalar by `u_bass`, ensuring the visual distortion scales exactly with the amplitude of the frequency band.

## Metadata
- **Industry Name(s):** Audio WebGL Distortion
- **Rarity:** UNCOMMON
- **Implementation Confidence:** HIGH
- **Production Feasibility:** MEDIUM (Requires user interaction - a click - to initialize the Web Audio API due to strict browser autoplay policies.)
- **Accessibility / Reduced Motion:** Provide an option to disable visual distortions independent of audio playback.
