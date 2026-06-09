# Audit Report: Site 08 — Art Here (Portal-Based 3D Exhibition)

### 1. Site Identity & Target Impression
* **Core Vibe:** Museum-Grade Digital Installation, Curated Curation, Multiverse Exploration, and Prestigious Quiet.
* **Audience:** Art collectors, design-literate visitors, and museum stakeholders who expect digital installations to respect the aura and legibility of the physical artworks.
* **Overall Aesthetic:** Stark, neutral outer frames (beige, cream, parchment) housing highly colorful, thematic, and independent 3D worlds.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **The Multiverse Cadence:** The layout alternates between high-intensity 3D worlds and flat, full-bleed 2D typography cards (3D World → 2D Card → 3D World).
* **Frame-Within-a-Frame:** Rectangular portal doorways act as physical windows, showing a glimpse of the next 3D scene before the camera passes through.
* **Typographic Decompression Chambers:** Solid-color HTML cards slide over the WebGL canvas, giving the user’s eyes a rest while separating the different artists.

#### Color & Texture
* **Neutral Frame/Vibrant Core:** Beige/white surfaces hold the UI, while the 3D worlds supply independent color personalities (neon purple, golden cavern, pitch-black void).
* **Pre-Baked Lighting:** Light and shadow maps are computed in 3D editing software (baked) rather than calculated live by the browser, maintaining high frame rates.

#### Motion & Restraint
* **Frictionless Z-Axis Tunnel:** Scrolling pushes the camera strictly forward through doorways. There is no Y-axis page sliding.
* **Render-Target / Stencil Portals:** Moving the camera through a specific plane swaps the rendered scene.
* **Rest States as Pacing:** The scroll timeline holds the camera static during 2D card displays, forcing reading pacing before advancing the camera.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Scene Curation Registry:** 3D model files, environment settings, and lighting setups for 7 entirely separate worlds.
2. **Baked Light and Material Maps:** Optimized, baked textures for the environments (preventing runtime lighting calculations).
3. **The Spatial Pacing Map:** Map spreadsheet containing scroll ranges, camera Z positions, portal crossing points, and unmount offsets.

#### AI Execution (The "80-60%")
1. **Multi-Scene R3F Lifecycle Manager:** Scaffolding the React Three Fiber container to mount, unmount, and load the active world.
2. **Active Memory Disposal System:** Writing disposal scripts to clear textures, materials, and geometries from the GPU during 2D card interludes.
3. **GSAP Scroll-Coord Mapper:** Synchronizing camera positions and HTML slide-ins to the scroll timeline.

---

### 4. Gaps in Current System

Comparing the Art Here site to our active skills reveals the following gaps:

#### Gap A: Lack of "Portal Exhibition Architecture" subtype
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) lacks patterns for **threshold transitions** and **multi-world sequences**. 3D is treated as a single product viewer or single camera track.
* **Why it matters:** The model cannot build multi-scene exhibitions because it does not know how to link separate 3D scenes.

#### Gap B: No Active 3D Lifecycle Management (GPU Disposal)
* **The Gap:** We do not provide instructions on **unmounting and garbage-collecting (disposing of) unused 3D meshes**.
* **Why it matters:** Loading multiple high-fidelity GLTF scenes sequentially without calling `.dispose()` on geometries/materials leads to instant GPU memory overflow and browser tab crashes.

#### Gap C: Missing "Spatial Pacing Map" Guideline
* **The Gap:** We lack a workspace artifact detailing camera Z coordinates, portal crossings, and card dwell intervals.
* **Why it matters:** The model attempts to write arbitrary ScrollTrigger scrub ranges, resulting in erratic camera speeds and text overlays that desynchronize.

#### Gap D: No "Creative-Dev / Senior-Only" Warning Tier
* **The Gap:** Our workflows treat WebGL portals and stencil render targets as standard tasks.
* **Why it matters:** The model will attempt complex GLSL or WebGL pipeline modifications that exceed standard autocomplete capabilities, resulting in code errors.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add "Portal Exhibition Architecture" subtype** to Cinematic Motion.
* **Write a "WebGL Asset Disposal & Memory Management" guide** inside the engineering skill.
* **Require a "Spatial Pacing Map"** for multi-scene 3D experiences.
* **Incorporate "2D Performance Masking" rules** (using text cards to hide scene unloads).
* **Insert a "Creative-Dev Task Guard"** to flag complex stencil buffer tasks for manual human art direction.
