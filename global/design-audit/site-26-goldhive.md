# Audit Report: Site 26 — Goldhive (Object-Led Scrollytelling)

### 1. Site Identity & Target Impression
* **Core Vibe:** Artisanal Honey Craft, Material Reality, High-End Digital Specimen, and Rustic Heritage.
* **Audience:** High-end farm-to-table consumers, honey connoisseurs, and B2B buyers who value slow craftsmanship but expect premium digital taste.
* **Overall Aesthetic:** Warm honeyed amber (`#e5a93d`), natural deep browns (`#2c1e16`), pure white spaces, photorealistic bees, and translucent honey droplets.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Narrative Object Overlay Canvas:** A transparent WebGL canvas fixed to the viewport (`z-index` highest, `pointer-events: none`). A single 3D character (the bee) floats continuously across DOM layout boundaries.
* **Asymmetrical Text Flanking:** Typography is split into left-and-right aligned blocks, framing a central 3D honeycomb container.
* **Whitespace Breathing Rooms:** Enormous vertical padding inside the middle acts, giving the 3D bee room to navigate without colliding with text.
* **Contrast Section Pacing:** Alternates visually dense, textured photography (hero and metrics sections) with minimalist white fields (diorama sections).

#### Color & Texture
* **Sensory Color Codes:** Honey golden-amber, farm white, and deep soil brown.
* **Subsurface Scattering (Translucency):** The WebGL honeycomb and honey drop use translucent, light-reactive materials (Three.js `MeshPhysicalMaterial` with transmission and thickness variables) to look sticky and glossy.

#### Motion & Restraint
* **Character-Led Guidance:** Text and UI remain static. The 3D bee and honey drip absorb the entire animation budget, guiding the user's eye down the document.
* **2D-to-3D Breakout Illusion:** The 3D bee begins its path positioned exactly over a 2D bee in the hero background photo. On scroll, it detaches, scales up, and flies toward the camera.
* **Hybrid Motion Integration:** Combines two animation registers:
  1. *Time-Bound Ambient Loop:* The bee's wings flap continuously via a skeletal `AnimationMixer` clock.
  2. *Scroll-Bound Spatial Path:* The bee's spatial coordinates (`position.x/y/z`, `rotation.x/y/z`) are scrubbed by GSAP ScrollTrigger.
* **Scroll-Stretched Honey Drip:** A 3D honey droplet scale-stretches (`scale.y`) on the Y-axis linked directly to vertical scroll progress.

#### Typography
* **Artisanal Serif Headings:** Classic display serif headers representing heritage, farm-to-table quality, and slow pacing.
* **Grounded Sans-Serif:** Clean sans-serif utility labels and navigation.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Rigged 3D Bee Model:** A `.glb` bee model with realistic anatomy, translucent wing textures, and an embedded skeletal wing-flap animation.
2. **Material-Optimized Honeycomb Mesh:** Honeycomb and honey drop models with subsurface transmission shaders.
3. **Alignment Hero Photo:** Background photography shot/framed to align perfectly with the starting scale and position of the 3D model.
4. **Object Blocking Map:** A storyboard sheet listing the coordinate targets, scale indices, and mesh states of the 3D bee per scroll milestone.

#### AI Execution (The "80-60%")
1. **Layered Canvas Setup:** Configuring the viewport-fixed, click-through canvas layer over the HTML document.
2. **GSAP ScrollTrigger Linkage:** Writing the timeline that maps scroll progress to the 3D bee's spatial translations and the honey drop's vertical scaling.
3. **Three.js Clock Loop:** Running the render clock to update the skeletal animation mixers independent of scroll scrubbing.
4. **Responsive Media Swapping:** Handling window resizing math to keep the 3D bee centered relative to fluid HTML typography.

---

### 4. Gaps in Current System

Comparing the Goldhive site to our active skills reveals the following gaps:

#### Gap A: Absence of the "Narrative Object Overlay" Pattern
* **The Gap:** [cinematic-motion/SKILL.md](../skills/cinematic-motion/SKILL.md) covers section-confined 3D viewers but lacks instructions for **viewport-fixed 3D overlays** that swim across vertical boundaries to carry continuity.
* **Why it matters:** The model isolates 3D objects inside standalone cards, missing the seamless overlay flow.

#### Gap B: No Requirement for an "Object Blocking Map"
* **The Gap:** We lack a planning step mapping the coordinates, scales, and states of a 3D overlay across scroll milestones (0%, 25%, 50%, 75%, 100%).
* **Why it matters:** The 3D model drifts randomly and overlaps text awkwardly.

#### Gap C: Incomplete 3D Asset Planning Specifications
* **The Gap:** Our guidelines request a generic "GLB asset" without specifying rigging status, skeletal animation loops, and transmission/translucency limits.
* **Why it matters:** The model receives static meshes that cannot perform ambient animations (like wing flapping).

#### Gap D: No Guidelines for "2D-to-3D Breakout Illusions"
* **The Gap:** We don't document the alignment math and coordinates mapping required to transition from flat image pixels to live WebGL scenes.
* **Why it matters:** The transition jump looks jarring and unaligned.

#### Gap E: Incorrect 3D Restrictions for Warm/Artisanal Brands
* **The Gap:** Our brand matrix asserts that warm/organic brands should skip WebGL, missing the rule that 3D is highly effective if the model represents a true craft specimen.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the "Narrative Object Overlay" pattern** to Cinematic Motion, detailing viewport-fixed canvases and click-through overlays.
* **Create the "2D-to-3D Breakout Illusion" pattern** in Cinematic Motion Engineering (handling coordinate matching and camera handoffs).
* **Refine the Brand Matrix rules for warm brands**:
  - Acceptable: When 3D models act as authentic craft specimens (e.g. animals, honey, raw materials) with realistic textures.
  - Banned: When 3D represents imported abstract tech spectacle.
* **Establish DOM Restraint rules** for object-led pages (forcing text and layouts to remain static when an overlay character is active).
* **Mandate two new planning files** in workflows:
  - `object-blocking-map.md` (detailing positions, scale, rotation, and animation states per scroll percentage).
  - `3d-spec-sheet.md` (detailing rigging bones, blend shapes, material transmission, and rendering budgets).
