# Audit Report: Site 24 — HELIOS (Generative Simulation Surface)

### 1. Site Identity & Target Impression
* **Core Vibe:** High-Consequence Systems Aesthetic, Real-Time Volumetric Traversal, Sci-Fi Aerospace HUD, and Mathematical Spectacle.
* **Audience:** Operators, engineers, and technical enterprise buyers looking for speculative digital interfaces, fusion-reactor console designs, and creative coding authority.
* **Overall Aesthetic:** Pitch black void (`#000000`), a glowing Neon Green (`#baff29`) and white real-time particle simulation, and edge-only control room telemetry overlays.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Single-Canvas Volume:** The entire interface is a real-time calculated WebGL canvas. Conventional page grid blocks are rejected.
* **Annotative DOM Overlays:** HTML text blocks act purely as annotations (labels, brackets, coordinates) that frame and explain the underlying simulation rather than competing with it.
* **Centered HUD Focus:** The visual weight is dominated by the central reactor core, with typography layered directly on top of the glowing points.

#### Color & Texture
* **Monochrome Neon Contrast:** Strict dual-tone palette (Black and Neon Green) enforcing extreme readability.
* **Procedural Point Textures:** Glowing, shimmering points generated dynamically via custom GLSL fragment shaders, creating organic depth.

#### Motion & Restraint
* **Volumetric Traversal (Z-Axis Push):** Scroll progress is linked to the 3D camera's depth axis (`camera.position.z`). The user scrolls "into" and "through" the coordinate volume, creating a warp speed fly-through.
* **World-State Morphing:** Instead of section swaps, the scroll wheel drives the mathematical morphing of the particle coordinates, rearranging the same points into different target shapes (Spiral Galaxy -> Orbital Sphere -> Topographical Wave).
* **Autonomous Ambient Drift:** The particles maintain a constant, slow rotation and noise turbulence before scroll interaction, ensuring the console feels active.
* **Linear Scrub Easing:** Mapped directly to scroll depth with heavy smoothing (`scrub: 1`) to simulate camera mass.

#### Typography
* **Wide Monospace Sans:** Wide, technical sans-serif typography (e.g. Space Grotesk) mimicking military heads-up consoles.
* **HUD Bracket Details:** Heavy use of telemetry brackets `[ ]`, crosshair icons `+`, and numerical indices.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Mathematical Design Brief:** Formulas defining the particle layouts (spiral equations, coordinate mappings, and Perlin/Simplex noise vectors).
2. **Camera Coordinate Map:** Storyboard of camera path vectors, focusing pivots, and overlay markers.
3. **HUD telemetry assets:** Custom monospace UI icons, bracket vectors, and clean typographic content.

#### AI Execution (The "80-60%")
1. **Three.js Scaffolding:** Initializing the WebGL canvas, PerspectiveCamera, and responsive resize limits.
2. **Shader Uniform link:** Linking the ScrollTrigger timeline variables directly to uniform parameters in the GLSL vertex and fragment shaders.
3. **Z-Axis camera translation:** GSAP script translating scroll height to camera Z position.
4. **Responsive HUD overlays:** Positioning HTML microcopy elements at the margins.

---

### 4. Gaps in Current System

Comparing the HELIOS site to our active skills reveals the following gaps:

#### Gap A: Absence of the "Generative Simulation Surface" Category
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) describes offline pre-rendered sequence scrubs and standard model viewers, but misses **Real-Time Generative Simulation** (where visuals are calculated procedurally on the fly).
* **Why it matters:** The model defaults to static image frame folders when procedural math models would be lighter and more interactive.

#### Gap B: No Requirement for a "Math/Simulation Brief"
* **The Gap:** We lack a planning step requiring the user to supply target coordinate equations, noise metrics, and uniform scroll triggers before writing WebGL code.
* **Why it matters:** The model attempts to generate complex visual swarms with generic prompts like "make a cool galaxy," leading to chaotic failures.

#### Gap C: Lack of the "World-State Morphing" Pattern
* **The Gap:** We don't document GLSL vertex shader vertex interpolation (`mix`) triggered by scroll progress uniforms.
* **Why it matters:** The model uses slow CPU Javascript loops to animate vertices, crashing the browser.

#### Gap D: Missing "Annotative Overlays" Guidance
* **The Gap:** No styling instructions requiring overlay text to act purely as telemetry data that frames, rather than blocks, the background simulation.
* **Why it matters:** AI layouts place solid background text cards over WebGL, breaking the spatial depth.

#### Gap E: Lack of a Simulation-First Fallback Strategy
* **The Gap:** Our performance rules lack guidelines for scaling down generative simulations based on client device power (e.g. desktop primary WebGL, tablet 50% particle count, mobile static snapshot).
* **Why it matters:** Heavy fragment shaders freeze mobile screens.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the "Generative Simulation Surface" track** to Cinematic Motion, detailing shader coordinates, procedural noise, and vertex manipulation.
* **Add the "World-State Morphing" pattern** to Cinematic Motion Engineering, providing GLSL vertex math templates.
* **Formulate the "Annotative Overlays" rule** (specifying transparent background settings, edge coordinates, and monospace HUD details).
* **Define the "Simulation-First Fallback Strategy"** for low-power mobile viewports:
  - Detect mobile hardware and bypass heavy fragment shader loops.
  - Scale particle target counts by 50% on tablet.
  - Swap the real-time canvas for a static, stylized image snapshot on mobile screens.
* **Mandate `math-brief.md`** as a required planning file in visual brainstorm workflows.
