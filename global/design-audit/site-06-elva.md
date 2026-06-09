# Audit Report: Site 06 — Elva (Anchor Object State-Morph)

### 1. Site Identity & Target Impression
* **Core Vibe:** High-Velocity SaaS Launch, Creator-Focused Utility, Kinetic Physics, and Visually Punchy.
* **Audience:** Creators, video editors, and mobile-native users who respond to high-energy motion, instant visual payoff, and immediate capability demonstrations over slow luxury pacing.
* **Overall Aesthetic:** Pure pitch-black voids (`#000000`), bold white typography, stark borders, and high-contrast glowing elements.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Fixed Center Stage:** Sibling layout divs are bypassed. Almost all visual action is pinned in the exact center of the screen, acting as a volumetric stage.
* **Single Transformable Anchor:** Instead of switching assets, a single central media container changes physical topologies continuously:
  * Flat 2D iPhone screen (default)
  * Floating 3D circular video bubbles (fragmented clips)
  * Iridescent glowing energy orb (AI core / processing)
  * Flat phone UI workflow (app process)
  * Rotating 3D vertical video cylinder (choice space)
  * Flat iPhone screen (resolution loop)

#### Color & Texture
* **Void Contrasts:** Solid black background erases screen borders. Colors are entirely sourced from the user's video content and the shifting iridescent blue-orange-pink AI glow.
* **Rounded Affordances:** Heavy border radii on cards, phone bezels, and circular video spheres, matching creator-app design languages.

#### Motion & Restraint
* **Physics-Coded Easing:** Animations communicate gravity, containment, release, attraction, collision, elasticity, and spin.
* **Scrubbed State Chain:** Timelines are scroll-bound. Scrolling acts as a playhead scrubbing forward and backward through the shape-shifting states.
* **Billboard Typography:** Copy is treated as massive display lines layered in the background, crossfading behind the central WebGL stage.

---

### 3. The Human/AI Split

#### Human Assets (The "20%")
1. **Curated Video Clip Pack:** High-contrast, vertically-shot lifestyle videos selected for color richness to serve as textures inside the spheres and cylinders.
2. **State Transformation Map:** A visual storyboard defining the sequence of forms, transition triggers, and copy synchronization beats.
3. **Orb Shader Parameters:** Mathematical rules (glow density, speed, colors) for the GLSL noise shader core.

#### AI Execution (The "80%")
1. **Three.js Geometry Scaffolding:** Generating the phone plate meshes, particle systems, and positioning planes in a cylindrical ring.
2. **GSAP Timeline State morphing:** Writing the ScrollTrigger logic to interpolate positions, scales, and rotation states.
3. **Multi-Video Texture Optimization:** Implementing performance safeguards (pausing off-screen video elements, culling back-facing video meshes).

---

### 4. Gaps in Current System

Comparing the Elva site to our active skills reveals the following gaps:

#### Gap A: Lack of "Anchor Object State-Morph" Concept
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) covers standard slide-ins, scatters, and fades. It lacks rules for **state-morphing a single persistent visual element** across the entire scroll narrative.
* **Why it matters:** The model treats sections as independent visuals instead of maintaining a single transformable canvas spine, breaking identity continuity.

#### Gap B: No Physics Language in Motion Planning
* **The Gap:** We document basic easing (expo, ease-out), but do not require defining the **physical laws/verbs of the scene** (containment, release, gravity, merge, collapse, recoil).
* **Why it matters:** Motion path timing looks like standard slide tweens instead of organic, momentum-carrying events.

#### Gap C: Missing Multi-Video Performance Budgets
* **The Gap:** We don't define limits or code patterns for **multiple active video textures**.
* **Why it matters:** The assistant will attempt to load and autoplay 10-15 WebGL video textures simultaneously, instantly causing frame-drops and tab crashes on mobile/tablet devices.

#### Gap D: No Conversion Structure Safeguards
* **The Gap:** [ui-ux/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/ui-ux/SKILL.md) does not remind the model to keep the standard conversion funnel visible (headline, proof, process, CTA) when building fully-hijacked pinned canvas layouts.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add "State-Morph WebGL TIMELINE" instructions** to Cinematic Motion.
* **Incorporate "Physics Verbs" mapping** into motion planning workflows.
* **Draft a "Multi-Video Texture Performance Budget"** (defining culling, cashing, and off-axis pauses).
* **Write rules for "SaaS Pinned Funnels"** (keeping conversion frameworks readable during scrolljacking).
