# Audit Report: Site 28 — CALMM (Organic Gut Health Diorama)

### 1. Site Identity & Target Impression
* **Core Vibe:** Living Product World, Organic Elegance, Reassuring Trust, and Cinematic Depth.
* **Audience:** Health-conscious wellness consumers seeking high-end scientific credibility blended with emotional, organic warmth.
* **Overall Aesthetic:** Soft sky-blue-to-white radial backdrop, lush forest and grass greens, and a centered floating diorama balanced by orbiting proof and conversion layers.
* **The "Before" vs "After" Redesign Upgrade:**
  * *Before (The Stale State):* Flat white/light grey background (`#F5F5F5`), invisible CTA (low-contrast outline ghost button), competing static 3D capsule renders on the margins, and zero faces or trust signals. Clinical, flat, and sterile.
  * *After (The Alive State):* Immersive 2.5D diorama (floating grass island holding the product bottle), distinct foreground/background layers, high-contrast CTA pill, vertical curtain opening veil, and continuous ambient leaf drift.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Diorama Hero Composition (The "Depth Sandwich"):** Unlike flat modular layouts, CALMM builds its scene using layered transparent assets positioned absolutely on the Z-axis:
  * *Layer 1 (Deepest):* Radial sky gradient (`#B4D4EA` to white).
  * *Layer 2:* Massive, centered display headline.
  * *Layer 3:* Floating organic dirt/grass island.
  * *Layer 4:* Green glass product bottle (resting on the island, partially masking Layer 2 text).
  * *Layer 5:* Translucent UI proof cards (reviews, photos) and floating leaves.
  * *Layer 6 (Closest):* Blurred foreground foliage creating a faux camera depth-of-field effect.
* **Assets as Layout:** Assets do not sit "inside components"; the assets *are* the composition, behaving like physical scenic objects in a set while UI elements orbit them as functional overlays.

#### Color & Texture
* **Organic High Contrast:** Sky blue (`#B4D4EA`) fading to white, contrasting with bottle green (`#2A4B3A`) and grass green (`#6B9E3A`).
* **Pre-Rendered Realism:** Shadows, specular lighting, and materials are pre-baked into transparent PNG assets rather than rendered in WebGL, maintaining 60fps mobile execution while preserving realistic textures.

#### Motion & Restraint
* **Curtain Veil Reveal:** A vertical liquid/fabric split transition. On page load, left and right curtain masks slide horizontally (`xPercent: -100` and `xPercent: 100`) to reveal the assembled scene.
* **Physical Arrival Sequence:** Staggered entrance timeline:
  1. *Island:* Slides up slightly (`translateY(30px)` to `0`) and scales up (`scale(0.9)` to `1.0`), fading in.
  2. *Headline:* Drops down slightly from behind the bottle.
  3. *Bottle:* Scales up onto the island surface.
  4. *UI Cards:* Slide in from left/right margins.
  5. *CTA:* Pops up from the bottom with a slight spring overshoot.
* **Dual-Track Animation Separation:**
  * *Interactive Track:* 2.5D mouse-parallax shifting layers at offset speeds (foreground leaf translates faster than the background gradient).
  * *Ambient Track:* Continuous, slow, infinite floating loops on the leaves (`translate3d` and `rotate` over 10-15s) to simulate gentle drift without conflicting with scroll triggers.

#### Typography
* **Oversized Sans-Serif Title:** Ultra-bold sans-serif (800/900 weight, Clash Display / Pangram Sans) with tight line-height (`0.9` to `1.0`) and negative letter-spacing (`-0.02em`).
* **Utility Cleanliness:** Clean, highly readable body copy (Inter/Roboto) on proof cards to contrast with the display headline.

---

### 3. The Human/AI Split

#### Human Assets (The "Scene Kit" — 20-40%)
1. **Coherent Asset Pack:** High-res transparent PNGs of the grass island, bottle, leaf layers, and pre-blurred foreground leaves sharing the same perspective and lighting direction (top-left highlight).
2. **Curtain Reveal Texture:** SVG/DIV mask vectors for the vertical split preloader.
3. **Lighting & Perspective Brief:** Reference sheet locking the highlight behavior, camera angle, and material finishes.
4. **Before-State Staleness Diagnosis:** A checklist of structural failures in the baseline site.

#### AI Execution (The "Code Assembly" — 80-60%)
1. **Z-Index Layer Sandwich:** Styling absolute wrappers, overflow controls, and aspect-ratio sizing.
2. **Page-Load Preloader Masking:** Animating the curtain reveal using horizontal translations.
3. **Staggered Arrival Timeline:** Writing GSAP entrance animations with precise eases (`expo.out` and `back.out`).
4. **Mouse-Track Parallax Engine:** Listening to cursor position and interpolating translation offset formulas.
5. **Continuous Drift Loop:** Handling the infinite leaf sway separately from interactive controls.

---

### 4. Gaps in Current System

Comparing the CALMM site to our active skills reveals the following gaps:

#### Gap A: Absence of the "Diorama Hero" Pattern
* **The Gap:** [ui-ux/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/ui-ux/SKILL.md) and [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) lack instructions for building layered Z-axis scenes where scale, foreground obstruction, and relative depth replace grid sections.
* **Why it matters:** The model defaults to standard modular layouts and box grids, failing to achieve cinematic diorama depth.

#### Gap B: No Requirement for "Asset Family Coherence"
* **The Gap:** We do not mandate rules ensuring that transparent assets share identical lighting angles, shadows, camera perspective, and crop logic.
* **Why it matters:** The model generates or accepts mismatched images, causing the 2.5D illusion to collapse into a messy collage.

#### Gap C: Missing Pre-Build "Staleness Audit"
* **The Gap:** Workflows do not instruct the assistant to critique the "Before" state of a page before starting the redesign.
* **Why it matters:** The assistant adds cosmetic polish without fixing root user-experience failures (like low-contrast buttons or lack of social proof).

#### Gap D: No Concept of "Dual-Track Animation" (Arrival vs. Ambient)
* **The Gap:** No guidelines separating one-time physical arrival animations from continuous ambient loops (like foliage sway), causing timeline collisions and stutters.
* **Why it matters:** The assistant overrides infinite loops with scroll triggers, freezing ambient elements.

#### Gap E: Absence of a "Depth Map Planning" Phase
* **The Gap:** We do not require creating a structural depth map mapping the roles and overlap limits of elements across Z-planes (Layer 1 to Layer 6).

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the "Diorama Hero" pattern** to UI/UX and Cinematic Motion skills (defining Z-axis sandwiches, absolute centering, and foreground depth-of-field blurs).
* **Create an "Asset Family Coherence Checklist"** in Impeccable Craft workflows (mandating camera angle, light direction, crop boundaries, and blur roles).
* **Integrate the "Staleness Audit" step** into Visual Brainstorm workflows (requiring developers to list low-contrast elements, competing anchors, and trust gaps in the baseline site before writing code).
* **Establish "Dual-Track Animation Rules"** in Cinematic Motion Engineering (separating keyframe arrival timelines from timeline-independent loops).
* **Mandate the creation of two new planning files** in workflows:
  - `depth-map.md` (defining layout roles across Layers 1 to 6).
  - `asset-lighting-brief.md` (specifying specular highlight direction, shadow intensity, and surface finishes).
* **Banish CSS-only placeholders for diorama scenes:** Mandate that if a concept depends on organic scenery or environmental depth, shipping CSS shapes instead of real cutout assets is a system failure.
