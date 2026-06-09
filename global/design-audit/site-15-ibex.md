# Audit Report: Site 15 — IBEX (Editorial Gallery / Digital Exhibition)

### 1. Site Identity & Target Impression
* **Core Vibe:** Editorial Luxury Gallery, Private Cultural Patronage, Ethereal Atmosphere, and Artistic Ceremony.
* **Audience:** Art patrons, collectors, and prestige-oriented cultural buyers who seek an exclusive, curated presentation rather than an e-commerce catalog.
* **Overall Aesthetic:** Jewel-toned room transitions (Gold, Deep Navy, Burgundy, Pure White), massive negative space, and world-class fine-art photography.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Room-by-Room Color Chapters:** Color blocking mimics walking through distinct gallery rooms (Amber entry -> Navy gallery -> White certification hall -> Dark technical overlay -> Burgundy patronage -> Gold exit), each with its own lighting and emotional weight.
* **One Focal Point Rule:** Composition is strictly limited to one primary focal element per viewport (e.g., a single artwork or one centered video block), allowing the media to breathe.
* **Symmetrical Margin Spacing:** Generous, luxurious whitespace borders framing typography and artwork containers.

#### Color & Texture
* **Jewel-Toned Palette:** Amber/Gold (`#d4a359`), Deep Navy (`#111525`), Burgundy/Blood Red (`#4a0e17`), and stark Gallery White (`#ffffff`).
* **Tactile Dust Atmosphere:** A very slow, low-opacity ambient particle field (representing dust motes in sunbeams) overlays solid backgrounds to create depth and texture.

#### Motion & Restraint
* **Printed Plate Transition Grammar:** Media enters by scaling down slightly and settling into place (e.g., `scale: 1.05` to `scale: 1.0`) while fading in, simulating heavy printed plates being framed or museum walls revealing themselves.
* **Curatorial Gallery Pinning:** Pinned (sticky) ScrollTrigger sections where scrolling scrubs a slow crossfade slideshow of images, changing the art piece while the layout remains anchored.
* **Atmosphere, Not Spectacle:** Motion is slow, heavy, and ceremonial. Easing is locked to smooth, non-elastic curves (e.g., `power2.out` or `power3.out`).

#### Typography
* **Luxury Editorial Tension:** Classic high-fashion pairing—a refined, high-contrast display Serif for the cultural voice, and tiny, tracked-out geometric Sans-Serif labels for metadata and CTAs.
* **Quiet Captioning Posture:** Text is formatted like gallery labels rather than marketing copy, with strict line-length controls.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Color-Graded Asset Family:** World-class digital art photography and process videos color-graded to match the amber/navy/burgundy palette.
2. **Line-Art Brand Emblem:** A transparent vector line-art face/hands mark for the hero.
3. **Curation Sequence Map:** A document ordering the assets by narrative weight and defining the room color transitions.

#### AI Execution (The "80-60%")
1. **Pinned Slide Crossfades:** GSAP ScrollTrigger timeline to handle the scale-down/fade-in transitions of the masterpieces.
2. **Ambient Particle Canvas:** A lightweight HTML Canvas or CSS texture loop that draws the floating dust particles.
3. **Responsive Grid Layout:** Generating the masonry grid for the footer gallery and staggered loading reveals.

---

### 4. Gaps in Current System

Comparing the IBEX site to our active skills reveals the following gaps:

#### Gap A: Absence of "Editorial Gallery / Digital Exhibition" Subtype
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) groups luxury under general rules, but does not define the unique rules of **Editorial Galleries** (room color blocking, single-focus viewports, and zero-elasticity pacing).
* **Why it matters:** The model defaults to adding standard scroll animations or layout scatters that ruin the solemn museum atmosphere.

#### Gap B: No Asset Priority Matrix or Curation Spec
* **The Gap:** We lack rules requiring the user to rank imagery and map out a curation sequence before writing code.
* **Why it matters:** The model treats all media files equally, sometimes placing low-resolution placeholders in high-impact hero positions.

#### Gap C: Missing Luxury Typography Spec Rules
* **The Gap:** We don't define the precise boundaries for display serifs, tracked micro-labels, line lengths, and caption layouts.
* **Why it matters:** The typography defaults to generic blog styles rather than lookbook-grade editorial layouts.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the "Editorial Gallery" subtype** to Cinematic Motion, enforcing the "One Focal Point" rule, zero-elasticity curves, and slow scale-down focus reveals.
* **Mandate three planning documents** for gallery-grade builds:
  - `curation-map.md` (defining section colors, dominant asset, transition type, and emotional progression).
  - `asset-priority-matrix.md` (ranking media assets to prevent low-quality substitutions).
  - `luxury-typography-spec.md` (specifying font pairings, tracking, and line length).
* **Define "Room-by-Room Transitions"** as a valid pattern where sudden color-blocking changes represent architectural thresholds.
* **Establish mobile fallback patterns** where pinned galleries translate to simple, reveal-based vertical stacks while retaining room color blocks.
