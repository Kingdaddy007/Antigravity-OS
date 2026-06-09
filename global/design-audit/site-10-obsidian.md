# Audit Report: Site 10 — The Obsidian Assembly (Curated Archive Luxury)

### 1. Site Identity & Target Impression
* **Core Vibe:** Esoteric Luxury, Dark Academia, Curated Curation, Historical Secrecy, and Museum of the Future.
* **Audience:** High-end members, collectors, and design-literate users who seek belonging, mystery, and deep cultural positioning over typical consumer efficiency.
* **Overall Aesthetic:** Earthy dark browns and obsidian black, parchment bone hues, architectural catalog photography, and historical artifacts.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Curated Disorder:** Scattered, asymmetrical masonry grids where images drift and overlap slightly, creating a sense of natural discovery rather than structured template design.
* **Typographic Labels:** Text blocks behave like museum tags (accession numbers, coordinates, provenance notes) rather than sales copy.
* **The "Obsidian to Parchment" Cycle:** The site alternates color worlds between deep darks (Obsidian `#0a0a0a`/`#241b18`) and bright textures (Parchment `#e8e1d5`) to segment the chapters.

#### Color & Texture
* **Tactile Materials:** Physical paper grains, vintage map coordinates, gold accents, and stone/porcelain textures.
* **High Contrast Values:** Restrained dark umber and warm bone, prioritizing PBR material properties.

#### Motion & Restraint
* **GSAP FLIP Layout-Morphing:** Sibling list cards do not disappear during detail views. The selected card detaches from the grid and morphs its scale, borders, and viewport coordinates to become a full-screen hero slider (First, Last, Invert, Play).
* **Ink-Bleed SVG Masks:** Transitioning to the map section utilizes an organic, fluid ink-splat SVG mask that bleeds across the screen.
* **Scholarly Artifact Inspection:** Suspending 3D objects on a horizontal track that rotates 360-degrees on Y-axis focus, surrounded by fading technical metadata paragraphs.

#### Typography
* **Serif Dominance:** A highly expressive display serif (Ogg / PP Editorial New) carries status, contrasted with microscopic, widely tracked sans-serif UI tags.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Graded Archival Photography Catalog:** Cohesive, low-contrast architectural and interior stills matching the dark umber lighting.
2. **Textured Asset Package:** Vintage map scans and high-resolution black-and-white ink bleeds for masking.
3. **Artifact Render Sequences:** 3D assets of artifacts baked with matching stone/gold material lighting.
4. **Continuity & Flow Map:** Storyboard documenting which elements transform into which detail frames (shared element transitions).

#### AI Execution (The "80-60%")
1. **GSAP FLIP Integration:** Writing the DOM state calculations and layout interpolations.
2. **Dynamic Theme Switching:** Transitioning background and text CSS custom variables on ScrollTrigger markers.
3. **Masonry Grid Layouts:** Coding the CSS grid structures and viewport containment.

---

### 4. Gaps in Current System

Comparing the Obsidian Assembly to our active skills reveals the following gaps:

#### Gap A: Absence of Shared-Element / FLIP Transitions
* **The Gap:** We don't document **shared-element expansions** or **grid-to-hero Promotions**.
* **Why it matters:** The model hides the list and mounts a new component, causing a visual flash instead of a continuous layout morph.

#### Gap B: No "Curated Archive Luxury" Design Mode
* **The Gap:** [ui-ux/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/ui-ux/SKILL.md) lacks an "Archive Mode" (evidence catalogs, metadata tables, museum labels, parchment-obsidian resets).
* **Why it matters:** The model defaults to clean corporate luxury, losing the academic, mysterious tone.

#### Gap C: Missing "Material Script" in Planning
* **The Gap:** We don't ask **"what material is this section pretending to be (paper, glass, stone)?"** during visual planning.
* **Why it matters:** Animations focus on CSS transforms instead of transitioning tactile textures.

#### Gap D: No "Artifact Inspection" Code Pattern
* **The Gap:** We don't have a template for product rotations paired with fading peripheral annotations/metadata.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add "GSAP FLIP Layout-Morphing" templates** to Cinematic Motion.
* **Establish a "Curated Archive / Esoteric Luxury" sub-register** in UI/UX.
* **Require a "Material Script"** in visual layouts.
* **Draft "Artifact Curation Layout" patterns** (rotating objects with metadata tags).
