# Audit Report: Site 20 — Cartier (Heritage Diorama Exhibition)

### 1. Site Identity & Target Impression
* **Core Vibe:** Heritage Legacy, Museum Reverence, Theatrical Ceremony, and Timeless Crafts.
* **Audience:** High-end art patrons, watch collectors, and prestige luxury buyers who value craftsmanship and legacy over direct retail convenience.
* **Overall Aesthetic:** Warm gold-and-amber illuminated display chambers (`#cba36b` to `#e6d4ba`), black silhouette figures acting as scale devices, and high-contrast centered typography.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Continuous Chamber Viewport:** The entire page is a single, pinned exhibition viewport. Individual modules or stacked sections are replaced by a guided camera tour.
* **Peripheral UI Restraint:** Logo, navigation, and options are kept tiny, transparent, and pushed to the absolute margins.
* **Pullback Grid Climax:** Resolves the narrative by pulling the camera back from a close-up watch vignette to reveal a large gallery wall of multi-frame screens.

#### Color & Texture
* **Warm Amber Dioramas:** Volumetric light streams through grid windows, illuminating gold watch details and casting deep, soft shadow gradients.
* **Silhouette Contrasts:** High-contrast solid black human figures staged inside the warm amber light fields, defining the spatial boundaries of each chamber.

#### Motion & Restraint
* **Diorama Procession:** An unbroken, pre-rendered 3D camera path that glides, orbits, and pans through 5 staged value chambers (Craftsmen -> Jeweler's Eye -> Tourbillon -> Manufacture -> Masterpiece) on scroll.
* **Heavy Momentum Scrub:** Linear GSAP scroll scrubbing with a dampening index (`scrub: 0.5`), giving the camera movements a sense of physical weight and mass.
* **Focus-Pull Handoffs:** Focus shifts (baked depth of field) draw attention to watch gears while background silhouettes blur out, directing the user's eye without UI pointers.
* **Absolute Interactive Silence:** Zero hover-states, bouncing elements, or scroll-hijacked jumps. The page moves only when the user scrolls.

#### Typography
* **Timeless Serif Authority:** Refined, high-contrast transitional serif font (perfectly kerned and centered) carrying all narrative headlines.
* **Peripheral Utility Labels:** Small sans-serif uppercase tags for minor details.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Curatorial Chamber Map:** A plan detailing 5–7 narrative chambers, mapping each to a specific craft value (e.g. tourbillon, manufacture).
2. **Pre-Rendered Cinematic Frames:** A sequence of 400-600 WebP frames of the camera journey, rendered with volumetric shadows and reflections.
3. **Silhouette Staging Layouts:** Graphic outline assets of watchmakers and observers scaled to match the watch components.
4. **Camera-Path Brief:** A sheet defining coordinates, lens zooms, silhouette layers, and copy cues per frame range.

#### AI Execution (The "80-60%")
1. **Canvas Frame Player:** Implementing the progressive loading and frame drawing loop inside an HTML5 canvas.
2. **GSAP ScrollTrigger Frame Matcher:** Writing the timeline that maps scroll depth to normalized frame indexes.
3. **Normalized Typography Cue Triggers:** Syncing serif text overlays to fade in and out at exact frame intervals (e.g., fading "THE EYE OF THE JEWELER" between frames 150 and 200).
4. **Responsive Grid Layout:** Managing the CSS grid calculations for the final gallery wall pullback.

---

### 4. Gaps in Current System

Comparing the Cartier site to our active skills reveals the following gaps:

#### Gap A: Absence of the "Diorama Procession" Pattern
* **The Gap:** [cinematic-motion/SKILL.md](../skills/cinematic-motion/SKILL.md) covers 3D displays but lacks guidelines for **Diorama Processions** (using a continuous camera path to travel through staged symbolic value rooms).
* **Why it matters:** The model defaults to building separate sections, destroying the museum ceremony.

#### Gap B: Lack of "Monumentalization" Guidelines
* **The Gap:** We lack design rules on using scale cues (pedestals, human silhouettes, volumetric light shafts) to make small physical items appear monumental and historic.
* **Why it matters:** Renders look like standard, flat e-commerce product photos.

#### Gap C: Missing "Heritage Luxury Restraint" Checklist
* **The Gap:** We do not instruct the developer to suppress UI chrome, buttons, search bars, and card boxes during the first acts.
* **Why it matters:** AI models place typical e-commerce controls above the fold, immediately cheapening the prestige.

#### Gap D: Absence of the "Gallery Pullback Ending" Spec
* **The Gap:** We don't document the pullback pattern to transition from close-up inspection to a broad visual catalog grid.
* **Why it matters:** The page ends abruptly without a structured grid resolution.

#### Gap E: No Camera-Path Brief Specification
* **The Gap:** Workflows don't require storyboarding camera vectors, depth planes, and light directions per frame window.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the "Diorama Procession" pattern** to Cinematic Motion, enforcing continuous camera paths, baked depth-of-field, and staged rooms.
* **Establish a "Monumentalization" design rule** (specifying scale figures, volumetric lighting, pedestal placement, and massive negative spacing around single objects).
* **Formulate the "Heritage Luxury Restraint Checklist"** (completely hiding navigation, button borders, and search grids in the intro sections).
* **Write the "Gallery Pullback Ending" code pattern** (detailing rapid camera zoom-out and scaling frame grids in GSAP).
* **Mandate `camera-path-brief.md`** as a required planning file in visual brainstorm workflows.
