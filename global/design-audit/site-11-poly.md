# Audit Report: Site 11 — Poly (Spatial Skeuomorphism)

### 1. Site Identity & Target Impression
* **Core Vibe:** Spatial Skeuomorphism, Tactile File Management, Nostalgic Warmth, and Organic Software Demos.
* **Audience:** Creative, visually oriented users who prefer tactile, physics-based interactions that make digital file structures feel as natural as organizing papers on a desk.
* **Overall Aesthetic:** Warm wood grain desks, soft incandescent lamp light, pink cutting mats, and highly detailed physical props.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Environment-Led Product Storytelling:** The product UI is embedded directly inside a physical workspace mockup rather than isolated on a generic digital stage.
* **Canvas/DOM Role Separation:** Crisp text explanations and search overlays live exclusively in the DOM to maintain readability and SEO, while the tactile desk elements, materials, and depth maps run inside WebGL.
* **Dimensional Hopping:** The layout transitions back and forth between a 3D physical workspace and a clean, flat 2D dark UI layout.

#### Color & Texture
* **Tactile Material Textures:** Warm wood grain, glossy photo paper finishes, celluloid filmstrips, translucent red acrylic (with realistic reflections), and textured cutting mats.
* **Cinematic Lighting & Depth of Field (DoF):** Diffused desk-lamp light with baked shadows. Camera lens blur is dynamically applied to the WebGL background when 2D HTML overlays appear.

#### Motion & Restraint
* **Tactile Physics:** Objects behave with gravity, momentum, and friction (falling photos settle onto the desk, the filmstrip unrolls with tension).
* **The "Shatter-to-Tabletop" Transition:** The flat digital grid on the 3D laptop screen explodes, transforming into physical 3D photo meshes that scatter onto the wood.
* **Nested Object Scrolling:** The tilted iPad-like tablet in Section 3 pins in the viewport, while the content *inside* the tablet screen scrolls on the Y-axis.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Fully Modeled & Pre-Baked 3D Environment:** The desk, laptop, and accessory models with baked-in shadow and lightmaps ( Blender workflows).
2. **Material Shader maps:** High-resolution roughness, normal, and displacement maps for physical textures.
3. **Scene-Choreography Map:** A blueprint defining coordinate transitions, camera lens targets, and DOM-vs-Canvas bounds for each section.

#### AI Execution (The "80-60%")
1. **R3F Scene Integration:** Rendering the pre-baked Blender scenes, lighting, and cameras.
2. **GSAP ScrollTrigger Interpolation:** Mapping scroll progress to the Z-axis camera movement, photo scatter vectors, and tablet scroll states.
3. **Dynamic Depth of Field (DoF) Blurs:** Coordinating canvas post-processing filters with DOM element enter/exit events.

---

### 4. Gaps in Current System

Comparing the Poly site to our active skills reveals the following gaps:

#### Gap A: Omission of "Spatial Skeuomorphism" Subtype
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) focuses on product viewers or scrolling panels. It lacks rules for **embedding product UI inside physical, skeuomorphic environments**.
* **Why it matters:** The model isolates models on simple screens rather than creating interactive workspace ecologies.

#### Gap B: No "Dimensional Translation" Motion Formula
* **The Gap:** We don't document **dimensional transitions** (translating a flat digital interface element into a physical 3D prop).
* **Why it matters:** Animations are limited to basic scaling and slide fades, losing the tactile software-to-object illusion.

#### Gap C: Pre-Baked Realism vs. Live WebGL Shadows
* **The Gap:** Our 3D instructions do not explicitly require **baking lighting maps** in 3D modeling tools prior to WebGL import.
* **Why it matters:** The model attempts to calculate real-time dynamic shadows for multiple complex meshes, causing major frame rate drops in-browser.

#### Gap D: Missing Hardware-Aware Fallback Doctrine
* **The Gap:** We lack rules for de-activating heavy real-time WebGL scenes on mobile/tablet devices and substituting them with pre-rendered video loops, flat images, or simplified reveal cascades.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add "Spatial Skeuomorphism" track** to Cinematic Motion.
* **Establish "Dimensional Translation" code patterns** (Z-axis scale and coordinate handoffs).
* **Require pre-baked lightmaps** for multi-mesh WebGL layouts.
* **Implement a "Hardware-Aware Mobile Fallback Doctrine"** (switching heavy R3F canvases to static poster frames or lightweight loop sequences on mobile).
