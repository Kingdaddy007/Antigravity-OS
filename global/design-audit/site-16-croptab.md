# Audit Report: Site 16 — CropTab (Physics-First Product Reveal)

### 1. Site Identity & Target Impression
* **Core Vibe:** Precise AgTech, Ecological Authenticity, Physics-First Storytelling, and Engineering Credibility.
* **Audience:** Farmers, agronomists, and B2B sustainability buyers who expect high-precision tech-grade solutions framed within natural credibility.
* **Overall Aesthetic:** Vibrant natural tones (lime green `#c7d92d`, dusty pink `#f2e8e3`, white, and charcoal `#2a2a2a`), heavy textures, bold engineered sans-serifs, and physical physics-based simulation.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Symmetrical Focus:** Center-aligned hero layout with a floating 3D anchor object positioned directly over a massive background logo.
* **Vertical-to-Horizontal Conveyor:** A section where vertical scroll progress is transferred to slide a horizontal carousel row of cards sideways (X-axis translation).
* **3D Diorama Showcase:** A closing full-screen interactive 3D landscape layout featuring floating callout tooltips pinned to specific coordinates.

#### Color & Texture
* **Section-as-Color-World:** Uses colors as distinct scene barriers with high-contrast cuts:
  * Lime Green: Alive, vital, and energized.
  * Dusty Pink: Problem area, loss, and deficit.
  * Murky Yellow/Green: Submersion and zero-runoff dissolution.
  * Pure White: Clinical data proof.
* **Tactile Materiality:** Luminous, high-fidelity textures (charcoal tablet metal, liquid splash mechanics, and organic corn vector lines) that convey weight and physical reality.

#### Motion & Restraint
* **Physics-as-Argument:** The central 3D CropTab tablet drops and splashes into water, acting as a visual explainer of the product's actual release mechanism.
* **Object-Wipe Transition:** The 3D tab scales up massive (scale: 60+) until its dark texture completely fills the screen, forming a camera wipe that reveals the next scene without a fade.
* **Multi-Register Motion Sync:** Orchestrates three distinct motion engines concurrently:
  1. Real-time R3F 3D floating logic (ambient, pre-scroll).
  2. Canvas Image Sequence scrubbing (water impact and underwater panning).
  3. SVG path stroke-draw animation (scrolled plant growth).
* **Progressive Outline-to-Solid Marquee:** Outlined marquee text that gradually fills with solid color as the scroll position updates, acting as a reading progress bar.

#### Typography
* **Extended Engineered Sans:** Wide, structural sans-serif display typography (e.g., Monument Extended) representing industrial precision.
* **Extreme Scale Contrast:** Giant display headings combined with tiny tracked spec labels, with zero middle-ground sizing.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Three-State 3D Assets:** The product model prepared in beauty, submerged, and exploded-schematic mesh views.
2. **Fluid Dynamics Sequence:** A folder of 150-300 pre-rendered WebP frames of the water-drop impact simulation (rendered in Houdini or Blender).
3. **Growth-Optimized SVG:** A 2D plant vector illustration with sequential, connected stroke paths organized for logical botanical expansion.
4. **Color-Graded B-Roll:** Golden-hour agricultural drone/field video, graded as a rich texture for background marquee layers.

#### AI Execution (The "80-60%")
1. **Multi-Canvas Coordinator:** Structuring the page to run a real-time WebGL canvas in the hero and an HTML5 canvas image sequence scrubber further down.
2. **Axis Transfer Scroll Calculator:** Writing the GSAP ScrollTrigger logic that translates vertical Y-axis scrolling to X-axis horizontal card movement.
3. **SVG Growth Draw Trigger:** Animating the SVG plant stroke draw (`drawSVG`) based on viewport entry, syncing branch reveals at staggered intervals.

---

### 4. Gaps in Current System

Comparing the CropTab site to our active skills reveals the following gaps:

#### Gap A: Omission of the "AgTech/EcoTech" Brand Archetype
* **The Gap:** [cinematic-motion/SKILL.md](../skills/cinematic-motion/SKILL.md)'s brand-to-motion matrix misses this hybrid category. AgTech combines industrial precision with organic warmth, demanding natural tones, linear physics, and heavy tactile surfaces.
* **Why it matters:** The model defaults to cold "tech blue" layouts and bouncy startup eases.

#### Gap B: No "Object-Wipe" Transition Pattern
* **The Gap:** We lack a code template or design guide for scaling a 3D element past the camera clipping plane to serve as a camera wipe.
* **Why it matters:** The model defaults to standard opacity fades, losing the cinematic object continuity.

#### Gap C: Missing "Physics-as-Argument" and "SVG Draw Explainer" Patterns
* **The Gap:** We document image sequences and drawSVG technically, but we don't define them as narrative devices where the scroll-drawn event *is* the marketing proof.
* **Why it matters:** The model treats growth drawings as static page decorations rather than scroll-bound stories.

#### Gap D: Absence of "Vertical-to-Horizontal Scroll Transfer"
* **The Gap:** No instructions for mapping horizontal translation to vertical scroll windows.
* **Why it matters:** The model attempts to use default browser overflows, causing layout breaks.

#### Gap E: No Multi-Register Performance Budget
* **The Gap:** We don't define the safety limits of combining real-time 3D, canvas frame sequences, and video assets on a single page.
* **Why it matters:** Models load multiple WebGL viewports and image scrubs together, crashing mobile browsers.

#### Gap F: Color-Scripting is Not Mandatory
* **The Gap:** Workflows don't enforce color-scripting (section colors, transitions, and emotional intent) in the pre-dev phase.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the AgTech/EcoTech Archetype** to the Cinematic Motion matrix (specifying `power2.inOut` easing, tactile materials, and organic palettes).
* **Write the "Object-Wipe" code pattern** into Cinematic Motion Engineering (handling scale and clipping).
* **Create the "SVG Scroll-Draw Explainer" pattern** (linking botanical path offsets to scroll).
* **Create the "Vertical-to-Horizontal Scroll Transfer" pattern** (mapping horizontal `x` translation to GSAP scroll height).
* **Establish a Multi-Register performance budget** (max 1 R3F scene + 1 Canvas Sequence per page).
* **Make "Color-Scripting" and "Sequence-Map Storyboards"** mandatory artifacts in Visual Brainstorm and Project Inception workflows.
