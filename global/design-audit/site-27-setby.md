# Audit Report: Site 27 — Setby (Industrial Logistics Showcase)

### 1. Site Identity & Target Impression
* **Core Vibe:** Industrial Physicality, Heavy Mass and Inertia, Engineered Reliability, and Creative Boldness.
* **Audience:** B2B enterprise logistics buyers and fleet operators who seek industrial coordination and security rather than generic SaaS utilities.
* **Overall Aesthetic:** Industrial warning red (`#ff3b30`), clean stark white (`#ffffff`), solid black (`#000000`), oversized structural sans-serifs, and raw metal container details.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Center-Weighted Core Motif:** Built entirely around a central, suspended 3D cargo container that acts as the page's spatial anchor and transition engine.
* **Asymmetric Flanking Text:** Large headlines are pushed to the left and right margins, leaving the center open for the 3D model.
* **Vertical Sticky Card Stack:** Staggers case details using a card stack accordion that slides up vertically and stacks behind/below the previous cards.
* **Horizontal Service Tables:** Utilitarian service grids featuring custom hover states that trigger image reveals following the cursor path.

#### Color & Texture
* **Industrial High Contrast:** Red, White, and Black palette. Sharp, flat colors mimicking warning signs and cargo stencil markings.
* **Hardware Geometry:** Hard edges, rectangular divisions, and wide polygonal frames. Rounded borders are completely rejected to preserve the industrial tone.

#### Motion & Restraint
* **Industrial Physicality:** All motions—pendulum swinging, card drops, and sliding panels—convey weight, gravity, and momentum.
* **Technical Annotation Scene:** As the 3D container rotates on scroll, thin vector lines draw outward from named vertices on the mesh to frame HTML text labels.
* **Shape Inheritance Masking:** The 3D container zooms in and its outer outline morphs directly into a geometric clip-path mask, wiping the canvas to reveal 2D photography.
* **Dampened Pendulum Idle:** The idle container uses a low-frequency, high-amplitude sine swing to simulate massive suspended steel mass.

#### Typography
* **Engineered Sans-Serif:** Blocky, geometric sans-serif (e.g. Monument Extended) reminiscent of warehouse labeling.
* **Massive Scale Contrast:** Enormous background letters overlapping the cargo and container meshes.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Texture-Mapped Cargo Container:** An optimized `.glb` shipping container with separate, named mesh parts for dynamic material/color swapping in code.
2. **Anchor Coordinate Map:** Specific 3D coordinate paths on the model mesh representing anchor points for tooltips.
3. **Polygonal Mask Coordinates:** Svg outline parameters matching the container mesh face.
4. **Object Role Inventory:** Storyboard mapping the container's structural role per scroll milestone.

#### AI Execution (The "80-60%")
1. **WebGL Vector Projector:** Writing the Three.js vector projection script (`vector.project(camera)`) that translates 3D coordinates to CSS pixel positions for tooltips.
2. **GSAP Sticky Card Timeline:** Pinning the card-stack container and animating `y` translations with scale offsets (`scale: 0.95` -> `1.0`).
3. **Cursor Reveal Image Tracker:** Writing the hover events that position image thumbnails dynamically at the mouse cursor.

---

### 4. Gaps in Current System

Comparing the Setby site to our active skills reveals the following gaps:

#### Gap A: Absence of the "Technical Annotation Scene" Pattern
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) covers standard 3D viewers but lacks the projection scripts and collision constraints required to anchor HTML cards to rotating WebGL vertices.
* **Why it matters:** The model cannot link DOM text to 3D models, causing coordinate drifting.

#### Gap B: No "Object Role Inventory" Requirement
* **The Gap:** We don't verify if an anchor 3D asset plays multiple functional roles (symbol, inspection, transition mask, footer anchor) across scroll depths.
* **Why it matters:** The 3D asset is repeated as a decorative background, losing utility.

#### Gap C: Lack of GLTF Specification for Annotation Readiness
* **The Gap:** Asset briefly sheets only request file formats, omitting named vertices, bounding boxes, and coordinate anchors.
* **Why it matters:** The developer receives models with un-addressable vertices, breaking tooltip trackers.

#### Gap D: Absence of the "Shape Inheritance" Transition Pattern
* **The Gap:** No code templates for morphing 3D mesh boundaries into 2D clip-path masks.

#### Gap E: Lack of "Industrial Physicality" Motion Rules
* **The Gap:** Our motion guidelines lack rules for gravity, swing, drop, and slide easing suited for physical industries (construction, logistics).

#### Gap F: Missing Category Artifact Strategy
* **The Gap:** Workflows don't instruct teams to identify the sector's most iconic physical object (e.g. pallet, spool, container) and design the site around it.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the "Technical Annotation Scene" pattern** to Cinematic Motion, detailing Three.js coordinate projection math.
* **Add the "Shape Inheritance Transition" pattern** to Cinematic Motion Engineering (handling outline masks).
* **Establish "Industrial Physicality" motion rules** (specifying heavy sine swings, drop and slide timelines, and high-contrast warning colors).
* **Add the "Category Artifact Strategy"** to visual brainstorm workflows (requiring teams to identify one physical object to organize layouts).
* **Mandate two new planning files** in workflows:
  - `object-role-inventory.md` (defining the container's structural role per scroll block).
  - `3d-annotation-brief.md` (mapping target vertex names, 3D coordinate offsets, and mobile occlusion rules).
