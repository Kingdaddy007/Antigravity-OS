# Fluid Simulation Background (Navier-Stokes)

## Visual Description
A real-time fluid simulation runs in the background, reacting to cursor movement or scroll. Fluid behaves according to physics (Navier-Stokes equations) — swirling, diffusing, and forming vortices. Cursor movement creates disturbances that propagate through the fluid field. Colors can be injected at interaction points, creating paint-like trails that blend and diffuse. The effect is mesmerizing and interactive, making the page feel alive and responsive. Often rendered at lower resolution and upscaled for performance. Used sparingly due to computational cost.

## Emotional Register
Mesmerizing, immersive, fluid, organic, premium, interactive. Makes every cursor movement feel consequential. Conveys technical sophistication and luxury. Appropriate for cutting-edge tech brands, creative agencies showcasing skill, art/design showcases.

## Technical Mechanics
- **DOM Structure:** Canvas element (WebGL)
- **CSS Properties:** N/A
- **JS Engine:** Custom WebGL implementation or library (e.g., `regl-fluid`, `WebGL-Fluid-Simulation`)
- **Key Timeline Logic:** Each frame: advect velocity field, apply forces (cursor input), compute divergence, solve pressure (Poisson), subtract pressure gradient, advect color field, render to screen
- **Easing Curve:** N/A (physics simulation)
- **Shader/WebGL:** Multiple shader passes:
  1. **Advection**: Move velocity/color field along its own flow
  2. **Force Application**: Add velocity at cursor position
  3. **Divergence**: Compute velocity field divergence
  4. **Pressure Solve**: Iterative Jacobi or multigrid solver
  5. **Gradient Subtraction**: Make velocity field divergence-free
  6. **Render**: Display color field to screen
- **Performance Notes:** Extremely GPU-intensive. Use low resolution (e.g., 128x128 or 256x256 simulation grid) and upscale to viewport. Requires discrete GPU; mobile devices will struggle. Consider disabling on low-end devices.

## Code Snippet / Reverse Engineering Brief
**Code Unavailable — Reverse Engineering Brief**
This is a highly complex multi-pass WebGL effect simulating the Navier-Stokes equations for fluid dynamics. To reverse engineer:
1. Initialize a WebGL canvas and framebuffers for velocity, pressure, divergence, and dye (color).
2. Set up shader programs for each step of the simulation (advection, splatting/forces, divergence calculation, pressure solving, and gradient subtraction).
3. On user interaction (pointer movement), calculate the delta and inject forces/dye into the simulation using a splat shader.
4. Run the physics loop on every frame, outputting the final dye texture to the screen. 
Libraries like `regl-fluid` or `WebGL-Fluid-Simulation` are often used as foundations for this effect.

## Metadata
- **Industry Name(s):** Fluid Sim, Interactive Fluid, Liquid Background
- **Rarity:** ULTRA-RARE
- **Implementation Confidence:** LOW
- **Production Feasibility:** LOW (Extremely GPU-intensive)
- **Accessibility / Reduced Motion:** Strongly recommend disabling or pausing simulation if `prefers-reduced-motion` is true, as continuous fluid motion can be disorienting.
