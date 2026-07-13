# Audit Report: Site 05 — Cartier Watches & Wonders (Canvas-First Exhibition)

### 1. Site Identity & Target Impression
* **Core Vibe:** Maison-Level Rarity, Exclusive Digital Exhibition, Material Sophistication, and Sculptural Ceremony.
* **Audience:** High-net-worth collectors, watch enthusiasts, and luxury consumers who expect aesthetic perfection, aura, and prestige over functional information delivery.
* **Overall Aesthetic:** Pristine real-time 3D gallery architecture, monochromatic cream/beige tones, high-fidelity physical textures, and dramatic spotlights.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Canvas-First Exhibition Environment:** The standard HTML/CSS DOM layout is completely abandoned. The entire viewport is a real-time WebGL `<canvas>` container representing a continuous 3D gallery.
* **Lighting as Page Structure:** Spatial divisions are created by color temperature and spot-lighting (ambient beige → dark bronze spotlight → icy platinum → pitch-black shadows → high-key white liquid mercury pool).
* **Volumetric Layered Typography:** Branding and text are rendered as glass-refracted, 3D meshes floating in coordinates inside the scene, interacting with light and depth.

#### Color & Texture
* **PBR-Driven Palette:** Raw gold, polished platinum, rich leather grains, diamond refractions, and liquid mercury metal. Hex codes are replaced by physical material properties (metalness, roughness, normal maps).
* **Studio HDRI Reflection Maps:** Warm, highly diffused light panels reflecting realistic gradients off metallic and glass watch surfaces.

#### Motion & Restraint
* **Robotic Macro-Lens Camera:** The scroll bar translates to a robotic camera arm panning, orbiting, and pushing through the 3D gallery.
* **The "Mesh-Breach" Wipe:** A Z-axis transition where the camera pushes *directly into and through* the physical mesh of the watch (e.g., gold watch band links, or a volumetric portal of white light) to seamlessly hide the loading and swapping of the next product scene.
* **Exploded Assembly Sequences:** Products explode smoothly along their axes on scroll (separating casing, gears, hands, straps) to show internal depth, then snap back together.

---

### 3. The Human/AI Split

#### Human Assets (The "20%")
1. **Watch Mesh Models & PBR Maps:** Highly detailed, topologically optimized CAD models of the watches baked with high-end roughness, normal, and displacement maps.
2. **Camera Path & Lens Storyboard:** Explicitly defined coordinate track, field-of-view (FOV), and camera targets mapped to scroll intervals.
3. **Custom Shader Briefs:** Specific GLSL scripts or matcap maps to render liquid metal ribbons, glass refraction, and particle dust.

#### AI Execution (The "80%")
1. **R3F Scene Integration:** Rendering the 3D meshes and integrating custom material shaders.
2. **GSAP ScrollTrigger Bindings:** Binding the scroll progression to the camera position vector, target coordinates, and mesh explode/slide offsets.
3. **Orientation Chrome & Loading States:** Designing the minimal overlay UI (menu buttons, persistent logo) and managing React Suspense logic.

---

### 4. Gaps in Current System

#### Gap A: Lack of "Canvas-First Exhibition" Category
* **The Gap:** [cinematic-motion/SKILL.md](../skills/cinematic-motion/SKILL.md) assumes a traditional web page containing a 3D canvas block. It has no design rules for **Canvas-First environments** where HTML is reduced to a minimal static overlay and the page architecture exists solely inside WebGL.
* **Why it matters:** The model tries to write standard vertical sections containing absolute canvases, leading to scroll gaps and layering bugs.

#### Gap B: No "Mesh-Breach" or Geometry-Driven Wipes
* **The Gap:** We don't document **mesh-breaches** (flying through geometry as cover wipes) or **volumetric light portals** to transition between scenes.
* **Why it matters:** The model defaults to CSS page wipes or alpha crossfades, which break the continuity of the 3D world.

#### Gap C: Missing Material Drama & Custom Shader Specifications
* **The Gap:** Our current 3D instructions assume standard Three.js materials. We lack a designated category for **Material Drama**—defining where custom shaders (liquid metals, glass refractions) must carry the luxury aesthetic.

#### Gap D: No Camera-Path Briefing (Spatial IA)
* **The Gap:** We do not instruct the AI to construct a **Camera-Path Storyboard** (coordinates, focal lens, targets, and occlusion meshes per scroll block) which acts as the Information Architecture (IA) of the site.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Introduce "Canvas-First Exhibition" track** to Cinematic Motion.
* **Add "Mesh-Breach Geometry Wipes" code patterns** using scale-interpolation and clipping limits.
* **Create a "Camera-Path Brief" format** (replacing traditional layout sitemaps).
* **Write guidelines for "Material Drama"** (defining shader priorities).
