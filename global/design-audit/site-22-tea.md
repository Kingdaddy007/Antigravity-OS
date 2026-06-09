# Audit Report: Site 22 — Assam Tea (Ritualized Product Film)

### 1. Site Identity & Target Impression
* **Core Vibe:** Meditative Luxury, Sensual Ceremony, Organic Heritage, and CONTEMPLATIVE Craft.
* **Audience:** High-end lifestyle buyers who view tea preparation as a physical ritual rather than a fast transaction.
* **Overall Aesthetic:** Midnight violet/black void (`#0a0812`), warm liquid amber (`#d4af37`), natural green and red botanicals, and vast negative space.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Centered Visual Symmetries:** Symmetrical, single-column focus centering around a single focal object (e.g. teabag, cup, or product tin) in each viewport.
* **Marginalized Copy Layout:** Typography is pushed to the margins of the screen, ensuring it never overlaps or competes with the central 3D sequence.
* **Continuous Handoff Shop Grid:** The e-commerce section ("Choose your ritual") smoothly scroll-reveals as the canvas unpins, inheriting the exact same color palette, typography, and mood of the film.

#### Color & Texture
* **Deep Contemplative Colors:** Midnight Void (`#0a0812`), Liquid Amber (`#d4af37`), botanical green, and rose red.
* **Tactile Material Assets:** Volumetric vapor steam, paper fibers, crystal glass reflection overlays, and organic leaf veins that emphasize physical touch.

#### Motion & Restraint
* **Meditative Causality:** Animation steps emerge logically from the previous state (teabag folds open -> plant grows -> leaves cascade -> water pours -> steam rises -> hands cup glass), mimicking the physical stages of tea preparation.
* **Contemplative Copy Choreography:** Short, sequential text beats ("Pour. Wait. Breathe. Three minutes. That is all it takes.") function as a metronome, slowing down the user's scroll speed and matching their physical breathing rhythm.
* **Bidirectional Scroll Plausibility:** Every stage of the pre-rendered image sequence is designed to look plausible when scrubbed forward and backward (e.g. steam descending back into the cup on reverse scroll).
* **Relaxed Scroll Easing:** Links the canvas to a heavily dampened GSAP scrub factor (`scrub: 1` to `1.5`) to eliminate jittery trackpad movements.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Multi-State 3D Sequence:** Pre-rendered WebP sequence (400-600 frames) covering the folding, growth, cascading, pouring, and steam dynamics.
2. **Tactile Photography Overlay:** Softly lit human hand layers photographed and color-graded to match the 3D void.
3. **State-Chain Board:** A preproduction spec documenting the logical order of material transitions, coordinate milestones, and synchronized copy beats.

#### AI Execution (The "80-60%")
1. **Canvas Frame Player:** Implementing the high-friction, scroll-bound image sequence scrub script.
2. **GSAP ScrollTrigger Metronome:** Writing the timeline that reveals copy cues at exact normalized intervals.
3. **Canvas-to-Commerce CSS Handoff:** Building the smooth unpinning structure and mapping transition styles so the shop grid slides up seamlessly.

---

### 4. Gaps in Current System

Comparing the Assam Tea site to our active skills reveals the following gaps:

#### Gap A: Absence of the "Ritual Transformation Sequence" Pattern
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) covers product showcases but lacks guidelines for **Ritual Transformation Sequences** (illustrating the physical prep/use stages of a product in chronological order).
* **Why it matters:** The model defaults to static product grids rather than building a narrative of use.

#### Gap B: Lack of "Contemplative Copy Choreography" Specs
* **The Gap:** We don't document how to use short, sequenced text prompts to slow down user scroll speed and capture attention.
* **Why it matters:** The model generates long blocks of promotional copy that break the silent atmosphere.

#### Gap C: Missing "Canvas-to-Commerce Handoff" Blueprint
* **The Gap:** No guidelines for transitioning WebGL canvas sequences into HTML shopping grids while maintaining color, tone, and brand terminology (e.g., swapping "Add to Cart" for "Add to Ritual").
* **Why it matters:** The handoff feels like a sudden cut, breaking the premium illusion.

#### Gap D: Lack of a "Bidirectional Scroll suitability" Check
* **The Gap:** Our asset-planning workflows do not check if pre-rendered image frames look realistic when played in reverse.
* **Why it matters:** The user scrolls upward and sees physics simulations (like gravity or liquid splatters) behaving in jarring, impossible ways.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the "Ritual Transformation Sequence" pattern** to Cinematic Motion, detailing causality states and scroll-scrubbed physics.
* **Formulate the "Contemplative Copy Choreography" pattern** (specifying single-word triggers, scroll-based timing blocks, and tracking rules).
* **Establish the "Canvas-to-Commerce Handoff" pattern rules**:
  - Require matching background values between the WebGL viewport and the DOM shop container.
  - Style CTA copy using brand-specific nouns (e.g. "Ritual", "Acquisition") instead of default e-commerce verbs.
* **Add a "Bidirectional Scroll Suitability Check"** to the asset planning workflow, verifying that physics simulations support reverse scrubbing.
* **Mandate `state-chain-board.md`** as a required planning file in visual brainstorm workflows.
