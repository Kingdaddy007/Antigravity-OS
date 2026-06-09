# Audit Report: Site 03 — MAIN (Abstract WebGL Sequence)

### 1. Site Identity & Target Impression
* **Core Vibe:** Ethereal Technology, Philosophical Manifesto, Intimate/ Felt Intelligence.
* **Audience:** Founders, investors, early adopters, and design-literate users who connect with vision, storytelling, and high aesthetic ambition over typical product features.
* **Overall Aesthetic:** Ultra-minimalist, high-key silver-white studio seamless backgrounds, thin typography, and glowing transitions.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Continuous WebGL Scene:** Rather than distinct vertical divs, the page is rendered inside a single continuous WebGL `<canvas>` container.
* **Abstract 3D Progression:** A sequential chain of symbolic 3D models represents the narrative:
  * Zero-gravity floating UI icons (abstract/scattered intent)
  * Humanoid bust with swirling particles (felt intelligence/consciousness)
  * Frosted-glass cube with metallic core (processing/engine)
  * Gyroscopic network rings (system/connection)
  * Paired android figures (hyper-personalization)
  * Massive collective field of androids (social scale)
* **Orientation Scaffolding:** A persistent vertical progress rail on the left with a glowing orange dot maps the scroll journey.

#### Color & Texture
* **High-Key Palette:** Clean off-white and pale silver-grey (`#f5f5f7` to `#eaeaec`).
* **Material Contrasts:** Frosted glass (high transmission/roughness), metallic iridescence, and glowing particle systems.
* **Chroma Shifts:** Transition from warm golden amber (human intent) to a clinical cybernetic cyan-blue (the network).

#### Motion & Restraint
* **Scroll-Bound Camera Path:** Scroll progress translates directly to the camera’s position, zoom, and target rotation along a predefined path in 3D space.
* **Lighting as the Editor:** Sudden, blinding light blooms (particle sparks) are used to wash out the screen. This hides the loading, swapping, and rendering of different 3D meshes behind the glow.
* **Frictionless Easing:** Long, slow decelerations (ease-outs) on camera moves, with a single bouncy spring ease specifically used for UI cards.

#### Typography
* **Ethereal Pinned Text:** Ultra-thin text blocks that fade in and out in static screen coordinates rather than scrolling vertically, keeping the focal weight on the 3D canvas.

---

### 3. The Human/AI Split

#### Human Assets (The "20%")
1. **Abstract 3D assets:** Custom GLB/gltf assets (icons, humanoid models, cubes, gyros) with matching materials.
2. **Material Shader Specs:** Defining frosted glass, iridescence, and particle systems beforehand.
3. **Shot List / Camera Storyboard:** Specifying camera coordinates, zoom levels, and object configurations at scroll intervals (0%, 25%, 50%, 75%, 100%).

#### AI Execution (The "80%")
1. **R3F Scene Setup:** Implementing the Canvas, custom shaders, and Drei helper rigs.
2. **GSAP Camera Interpolation:** Mapping the scroll timeline to camera coordinates and tweening mesh properties.
3. **HTML overlay sync:** Coordinating text crossfades and progress line indicators to the scroll position.

---

### 4. Gaps in Current System

Comparing the MAIN site to our active skills reveals the following gaps:

#### Gap A: "Product Viewer" vs. "Narrative Scene" Logic
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) deals with 3D as an interactive inspection tool ( OrbitControls, Swatches, PresentationControls). It lacks guidance for **camera-path choreography** and **directed storytelling** where the user controls a timeline, not the camera directly.
* **Why it matters:** The model defaults to static canvas zones rather than continuous scroll-films.

#### Gap B: No Scene Graph / Scroll-Board Template
* **The Gap:** We do not instruct the AI to plan or output a **Scene Graph Brief** (coordinate maps, light transitions, active models, active text overlays per scroll percentage) before writing code.
* **Why it matters:** Setting up complex camera paths without a structured timeline spreadsheet results in messy, uncoordinated GSAP code.

#### Gap C: Luminous / Shading Transition Gaps
* **The Gap:** Our current transitions rely on HTML fog overlays (like Montfort) or canvas opacity. We do not document **luminous transitions** (using HDR blooms, density fog, or glowing particle bursts to mask model swaps).

#### Gap D: Missing Rules for Scroll Orientation Aids
* **The Gap:** We have no guidelines recommending custom scrolling UI indicators (progress rails, chapter markers, etc.) to orient users in heavily scroll-jacked layouts.

---

### 5. Upgrade Specifications

We will compile these specs:
* **Add "Narrative WebGL Sequence" track** to Cinematic Motion.
* **Require a WebGL Scene-Graph Brief** mapping scroll ranges to camera, lights, meshes, and text layers.
* **Provide Canvas material templates** (frosted glass, metallic iridescence) inside the engineering skill.
* **Introduce "Luminous Transition Wipes" code patterns** utilizing Three.js fog and bloom values.
