# Audit Report: Site 17 — Igloo/Penguin (Single-Canvas Cinematic Film)

### 1. Site Identity & Target Impression
* **Core Vibe:** Clinical Futurism, Intimidating Tech Authority, Elite Cinematic Showcase, and Structural Rarity.
* **Audience:** Clients purchasing high-end digital design, cinematic systems orchestration, and prestige visual execution.
* **Overall Aesthetic:** Monochrome ice-world colors (pure white `#ffffff`, icy silver `#e2e6eb`, deep black `#000000`), edge-only Heads-Up Display (HUD) instrumentation, and photorealistic ice physics.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Single-Canvas Viewport:** The entire page is a single, pinned `<canvas>` element. Traditional vertical stacked HTML sections are completely rejected.
* **HUD Frame Overlay:** UI elements (logo, CTAs, coordinates, crosshairs) are pushed to the absolute margins of the screen, acting as camera viewfinder markings.
* **Dossier Slide-In Panel:** Semi-transparent panels with backdrop-blur filters (`backdrop-filter: blur(12px)`) slide in from the screen edge, showing text without blocking the underlying 3D scene.

#### Color & Texture
* **Monochrome Icy Palette:** Pristine silver, snow white, and cold grays. Dark panels provide high-contrast focal points.
* **High-Fidelity Ice Refraction:** Realistic light refraction, reflection mapping, and scattering within the ice blocks, emphasizing material weight and physical reality.

#### Motion & Restraint
* **Unbroken Camera Continuity:** The user does not scroll through separate layout blocks; instead, the virtual camera travels continuously through a single environment, panning and zooming through 6 distinct states (Wireframe -> Disassembly -> Specimen block -> Shatter -> Freefall -> Chamber -> Loop return).
* **Infinite Looped Sequence:** The bottom of the scroll sequence seamlessly connects back to the first frame, closing the camera path in an infinite circle.
* **Heavy Easing & Lerp:** Smooth inertial scroll dampening maps the scroll wheel to the animation playhead, maintaining a heavy, cinematic momentum.
* **Static Edge Restraint:** The HUD UI remains entirely static on the screen margins, creating a stable "viewfinder window" contrast to the moving 3D environment.

#### Typography
* **Clinical Micro-Typography:** Space Grotesk/Monospace fonts, styled with tiny font sizes, wide tracking, and technical formatting (e.g. brackets `[ ]`, coordinate parameters, and `+` crosshairs).
* **Instrumental HUD Voice:** Text acts as telemetry data and system labels rather than marketing headlines.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Master Camera Path & Timeline:** The directed, pre-authored 3D camera sweep, detailing lens settings, focal points, and loop parity coordinates.
2. **Procedural Shatter & Fracture Sequence:** A folder of 300-500 WebP frames of the ice block exploding and the character model freefalling, pre-rendered in Houdini or Blender.
3. **HUD Identity Kit:** Custom vector UI icons, technical brackets, coordinates, and styling specs.
4. **Sequence Bible:** A master sheet mapping safe frame windows where text overlays can enter without colliding with the camera's path.

#### AI Execution (The "80-60%")
1. **Canvas Frame Player:** Implementing the high-performance drawing loop, swapping image frames based on scroll depth.
2. **Background Thread Web Worker Loader:** Writing a worker script to load and cache frame slices in chunks without blocking the main rendering thread.
3. **GSAP ScrollTrigger Timeline:** Mapping the 0-500 frame index sequence to a 5000px scroll window and orchestrating the dossier panel reveal transitions.
4. **Loop Boundary Handoff:** Writing the wrapping logic that redirects the scroll playhead back to index 0 at the end of the scroll container.

---

### 4. Gaps in Current System

Comparing the Igloo/Penguin site to our active skills reveals the following gaps:

#### Gap A: Absence of "Single-Canvas Narrative World" Pattern
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) assumes pages are built of stacked sections. It has no branch for pages where the entire interface is a single canvas and the DOM serves purely as instrumentation.
* **Why it matters:** The model defaults to building standard layouts with sections, breaking the continuous cinematic illusion.

#### Gap B: No HUD Overlay Grammar Rules
* **The Gap:** We lack rules for edge-only UI styling (brackets, crosshairs, micro-labels, coordinate logs) and backdrop-blur panels.
* **Why it matters:** The model defaults to adding generic sci-fi styling that looks cheap and unrefined.

#### Gap C: Missing "Looped Sequence Architecture" Guidelines
* **The Gap:** No instructions for planning frame parity (matching start/end coordinates) or managing loop seams in scroll playheads.
* **Why it matters:** The model builds scroll animations that abruptly stop or reset with a jarring snap.

#### Gap D: Missing Memory & Image-Sequence Preloading specs
* **The Gap:** We don't document **Web Worker frame streaming, resolution tiering, or frame disposal policies** for heavy image sequences.
* **Why it matters:** High-resolution frame folders crash mobile devices due to browser RAM saturation.

#### Gap E: Omission of "Clinical Futurist" Brand Archetype
* **The Gap:** The brand-to-motion matrix lacks a cold, high-authority, monospace-driven scientific style guide.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add "Single-Canvas Narrative World" track** to Cinematic Motion, detailing canvas context execution, edge HUD styling, and continuous camera transitions.
* **Add the "Clinical Futurist / Lab-Cinematic" Archetype** to the motion matrix (specifying monospace typography, monochrome tones, and zero-bounce camera eases).
* **Establish a HUD Overlay Grammar spec** (brackets, crosshairs, tiny tracking, blur filters, and micro-labels).
* **Write Looped Sequence guidelines** (ensuring frame parity and managing wrap-around scroll triggers).
* **Create an Image-Sequence Performance Guide** (detailing chunked lazy-loading via Web Workers, memory cleanup, and mobile resolution downgrades).
* **Mandate `sequence-bible.md`** as a required planning file for single-canvas cinematic builds.
