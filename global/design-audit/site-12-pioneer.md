# Audit Report: Site 12 — Pioneer (Continuous Morph Narrative)

### 1. Site Identity & Target Impression
* **Core Vibe:** High-Precision Biological Engineering, Scientific Authority, Cinematic Process, and Organic Evolution.
* **Audience:** Agricultural partners, investors, and industry stakeholders who need to perceive seed genetics as cutting-edge technology rather than rustic tradition.
* **Overall Aesthetic:** Dark, cosmic-black fields (`#0a0a0a`), luminous glowing point clouds, biological color shifts, and clean negative space.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Material Continuity:** Rather than swapping out image or video assets section by section, the site commits to a single visual substance—particles—as the universal metaphor of growth and science.
* **Unobtrusive Typography:** Text is clean, neutral, and kept secondary, fading in and out of the black space surrounding the glowing particle shapes.
* **Integrated UI Scaffold:** A persistent circular progress index tracks the progression of the genetic story.

#### Color & Texture
* **Biological Color Shifts:** Chronological color changes representing stages of life:
  * Fiery red/orange: Raw energy and genetic code (DNA).
  * Vibrant neon green: Organic growth, data vitality, and leaf structures.
  * Muted earth tones: Soil and root networks.
* **Luminous Contrast:** Deep black background makes the glowing points readable.

#### Motion & Restraint
* **Continuous Point-Cloud Morphing:** Scrolling interpolates the X, Y, Z coordinates of thousands of vertices from one 3D shape directly into the next (Helix → Seed → Data Network → Roots Sprout → Corn Ear).
* **Narrative Camera Paths:** The camera flies through the shapes (e.g., zooming directly inside the leaf to transition into the data grid) rather than watching from a static distance.
* **1:1 Scrubbing:** Particle position and camera vectors are scrubbed directly via custom shader uniforms linked to the scroll playhead.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Compatible Point-Cloud Datasets:** 3D subject models (DNA helix, seed, seedling, leaf, corn) exported with the exact same vertex counts so they can map 1:1 during morphing.
2. **Morph Choreography Map:** A document mapping state sequences, color regime thresholds, camera milestones, and the semantic reason for each morph.
3. **GLSL Vertex Shader Scripts:** Custom GPU code to handle the linear interpolation (`lerp`) of thousands of points smoothly.

#### AI Execution (The "80-60%")
1. **R3F Scene Boilerplate:** Setting up the WebGL Canvas, camera clipping parameters, and Orbit/Drei controllers.
2. **GSAP ScrollTrigger Uniform Mapping:** Animating the custom progress uniforms in the shader material based on scroll depth.
3. **Responsive HTML Text Sync:** Coordinating typography fades and progress UI updates with ScrollTrigger markers.

---

### 4. Gaps in Current System

Comparing the Pioneer site to our active skills reveals the following gaps:

#### Gap A: Omission of "Continuous Morph Narrative" Subtype
* **The Gap:** [cinematic-motion/SKILL.md](../skills/cinematic-motion/SKILL.md) assumes mixed media sections (scatters, parallax, video scrub). It has no guidelines for **single-material continuous morphing** where the entire page is one evolving canvas.
* **Why it matters:** The model defaults to switching assets rather than maintaining material continuity.

#### Gap B: No Shader-Territory Detection Gate
* **The Gap:** Our workflows don't flag when a concept crosses from standard R3F scene work into **custom shader pipeline territory** (requiring GLSL vertex shader morphs).
* **Why it matters:** The model attempts to animate thousands of vertices using JavaScript loop iterations, instantly freezing the browser.

#### Gap C: Missing Point-Cloud Asset Preprocessing Rules
* **The Gap:** We don't document **vertex matching, origin alignment, or sampling requirements** in 3D modeling tools for point-cloud systems.
* **Why it matters:** The user provides assets with different vertex counts, causing the model's shader interpolation to break and crash the WebGL context.

#### Gap D: Missing Low-Power Fallback Rules (Sanitized)
* **The Gap:** We lack rules for replacing heavy real-time particle morphing with pre-rendered WebM video clips, flat images, or simple CSS reveal cascades on mobile and low-power devices.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add "Continuous Morph Narrative" track** to Cinematic Motion.
* **Incorporate a "Shader Territory Guard"** in workflows to detect GPU-heavy coordinate morphs early.
* **Write a "Point-Cloud Preprocessing Guide"** for 3D modeling pipelines.
* **Draft "Low-Power Fallback Rules"** (de-activating WebGL point morphs on mobile in favor of lightweight pre-rendered loops).
