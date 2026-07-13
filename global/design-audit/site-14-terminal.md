# Audit Report: Site 14 — Terminal (Sequence-Scrub Brand Film)

### 1. Site Identity & Target Impression
* **Core Vibe:** Industrial Authority, High-Fidelity Logistics, AI-Native Operations, and Cinematic Restraint.
* **Audience:** Enterprise buyers, fleet operators, and logistics investors who view yard operations as high-tech strategic infrastructure rather than manual trucking.
* **Overall Aesthetic:** Dark, moody dawn/dusk photorealism (`#0a0a0c`), sharp off-white pages (`#f4f4f0`), with highly disciplined Amber (physical) and Neon Green (data) accent lighting.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Full-Screen Pinned Canvas:** The primary container pins to the viewport, acting as a dynamic "projection screen" while text blocks scroll vertically over it.
* **Asymmetric Explanatory Grids:** Transitioning from centered headline overlays (manifesto mode) to a left-aligned typography grid paired with right-aligned blueprint diagrams (explanation mode).
* **Sharp Industrial Geometry:** Zero rounded corners, heavy use of layout grids, and strict box structures, reinforcing operational precision.

#### Color & Texture
* **Isolated Visual Registers:** Segregates assets into distinct categories—photorealistic 3D, flat/isometric vectors, blueprint wireframes, and digital lidar scans. Visual styles are never blended, preventing visual noise.
* **Amber & Green Accents:** Restricts light accents to Amber (physical light source) and Neon Green (system telemetry and movement paths).
* **Refined Gradients & Meshes:** Subtle digital grids overlaying dark canvases, representing scanning and tracking operations.

#### Motion & Restraint
* **Sequence-Scrub Playhead:** The scroll wheel operates as a linear playhead mapping directly to the frames of a pre-rendered 3D sequence drawn to a canvas.
* **Heavy Inertia (Lerping):** Uses a slight GSAP scroll lag (`scrub: 0.5`) to give the animations weight, simulating the physics of massive logistics machinery.
* **Narrative Hard Cuts:** Uses abrupt background and color flips (Dark 3D -> Light Vector -> Dark Blueprint) as clean chapter markers, giving the user structured pauses to process technical data.

#### Typography
* **3-Tier Typography Scale:** Massive geometric display headers (wide tracking for titles like "Y O S"), medium informational subtitles, and small utilitarian label copy.
* **Functional Alignment Swapping:** Centering typography for high-impact emotional statements and left-aligning it for complex system specs.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Pre-Rendered 3D Sequence Frames:** Folder of 300-500 high-res compressed `.webp` frames of the truck camera movement, rendered for both desktop (16:9) and mobile (9:16).
2. **Technical Wireframe & LiDAR Passes:** Alternate render sequences showing the chassis wireframe and dot-matrix radar scan overlays.
3. **Sequence-Map Storyboard:** A spreadsheet specifying scroll boundaries, target frame numbers, and active typographic text layers per scroll trigger.

#### AI Execution (The "80-60%")
1. **Canvas Sequence Renderer:** Writing the high-performance canvas loop that clears and draws images frame-by-frame based on a GSAP-animated frame index.
2. **Progressive Preloader Script:** Building a task-runner to preload the WebP frames sequentially, implementing an automatic "closest-loaded-frame" fallback during high-speed scrolling.
3. **Responsive Sequence Swapping:** Listening to screen resize events and swapping the active image array between desktop and mobile sequence sets.

---

### 4. Gaps in Current System

Comparing the Terminal site to our active skills reveals the following gaps:

#### Gap A: Absence of "Sequence-Scrub Brand Film" Subtype
* **The Gap:** [cinematic-motion/SKILL.md](../skills/cinematic-motion/SKILL.md) describes real-time 3D, video scrubs, and parallax, but completely lacks instructions for **Canvas Image Sequence Scrubbing** (managing frame preloading, memory disposal, and canvas redraw throttling).
* **Why it matters:** The model attempts to load large, un-scrubable raw `.mp4` video files directly, causing buffering stutters on scroll.

#### Gap B: Missing Frame-Range Storyboard Spec
* **The Gap:** We don't require an explicit sequence storyboard linking scroll depth to exact frame numbers, camera states, and text layers.
* **Why it matters:** The model attempts to scrub the entire folder in one giant timeline, losing control over narrative pacing and layout cuts.

#### Gap C: Lack of "Enterprise Restraint" Guidelines
* **The Gap:** Our motion guidelines don't define a strict style guide for industrial/enterprise brands (demanding linear/near-linear scrub paths, minimal accents, sharp geometry, and zero bounce easing).
* **Why it matters:** The model defaults to adding generic elastic transitions, which dilutes the serious, high-end authority of the brand.

#### Gap D: Missing "Data Over Reality" Pattern Family
* **The Gap:** We have no guidelines for overlaying wireframe blueprints or point clouds directly onto realistic visual layers on scroll.
* **Why it matters:** The system defaults to swapping sections entirely rather than transitioning visual states on the same object.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add "Sequence-Scrub Brand Film" track** to Cinematic Motion, detailing canvas context-drawing, progressive frame preloading, and active frame cleanup.
* **Mandate two new planning files** for image-sequence projects:
  - `sequence-map.md` (specifying scroll range, active file range, camera behavior, and typography overlays).
  - `asset-state-matrix.md` (listing photoreal, vector, wireframe, and scan variants).
* **Establish an "Enterprise Restraint" doctrine** (restricting easing to linear scrub, capping UI borders to 0px border-radius, and limiting accent colors to two).
* **Define a "Data Over Reality" pattern guide** to handle transitions between photoreal views and technical scan overlays.
* **Incorporate global mobile-hardware fallbacks** (such as swapping dynamic canvas sequences for lightweight, timed CSS grids or optimized looping pre-rendered videos on mobile viewports).
