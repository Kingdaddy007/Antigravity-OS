# Audit Report: Site 25 — INDIGO+ (Playful Agency Portfolio)

### 1. Site Identity & Target Impression
* **Core Vibe:** Snappy Playfulness, Thematic Gamification, Bold Growth Strategy, and High-Contrast Energy.
* **Audience:** Brands and creators looking for social media strategy and visual impact without corporate dullness.
* **Overall Aesthetic:** Vibrant Kelly Green (`#1b8b39`), orange/red highlights, stark black-and-white page resets, thick display type, and a recurring "Playing Card" visual structure.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Structural Motif (Playing Card Frame):** Replaces standard grid blocks and cards with a unified "deck of cards" metaphor. Fronts, backs, and frames package all case studies and testimonial sections.
* **Semicircular Hero Fan:** An asymmetrical hero layout where a stacked deck of cards fans out into a readable semicircle on scroll.
* **360-Degree Radial Bloom:** An act composed around a central title element, with cards blooming outward into a perfect circular sunburst shape.
* **Horizontal Carousel Showroom:** A pinned vertical viewport that slides massive card blocks horizontally along the X-axis.

#### Color & Texture
* **Color-Reset Pacing:** Aggressive color whiplash (Green -> White -> Black -> Green) used to segment acts and reset the user's attention.
* **Playful 3D Assets:** Glossy, real-time 3D models (boosting boxes, glowing test tubes) embedded via Spline to add physical depth.
* **Saturated Color Blocks:** Solid, flat color fields without gradients, supporting the high-contrast graphical theme.

#### Motion & Restraint
* **Snappy Physical Play:** Rejects slow, floating eases in favor of bouncy, momentum-driven easing (`back.out(1.5)` or `elastic.out`).
* **Semicircular Card Fan Math:** Sets card transform origins to the bottom center (`transformOrigin: "50% 100%"`), fanning them out with calculated offset rotations:
  * Rotation angle increment: `totalSpread / (cards.length - 1)`
  * Arc compensation Y-translation: `Math.abs(rotation) * 0.5`
* **SVG Liquid Drip Transition:** Uses a custom SVG path drip shape inside a `<clipPath>` mask to wipe section backgrounds organically on scroll.

#### Typography
* **Ultra-Heavy Display Type:** Loud, thick display headers (e.g. Shrimp) representing volume and market impact.
* **Predictable Utility Sans:** Clean geometric sans-serif layouts for numerical tables and UI headers.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Bespoke Card Design System:** Front/back designs, statistics card styles, and illustrations mapped as a unified visual family.
2. **Playful 3D Spline Models:** Interactive software boxes and test tubes pre-modeled with matching materials and lighting.
3. **SVG Liquid Transition Paths:** Custom drip shapes designed and mapped to coordinate vectors.
4. **Motif Grid Storyboard:** A plan detailing spacing, margins, and card variants per chapter.

#### AI Execution (The "80-60%")
1. **Fan & Bloom Trigonometric Math:** Writing the GSAP loop scripts that calculate angles, Y-axis offsets, and rotations for circular spreads.
2. **SVG Mask Morphing Timeline:** Animating path control coordinates in GSAP ScrollTrigger to execute the drip transitions.
3. **Spline Viewer Embeds:** Setting up the `@splinetool/react-spline` canvas element.
4. **Horizontal Scroll Calculator:** Pinning the horizontal showroom section and translating cards relative to scroll progress.

---

### 4. Gaps in Current System

Comparing the INDIGO+ site to our active skills reveals the following gaps:

#### Gap A: Absence of the "Structural Motif" Concept
* **The Gap:** We document design system consistency but lack guidelines on choosing a single physical metaphor (like playing cards, stamps, files) to reshape layouts and animations.
* **Why it matters:** The model generates generic dashboard grids and SaaS boxes, losing unique brand identities.

#### Gap B: Lack of Playful Group Choreography Patterns
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) covers generic scroll moves but lacks code templates for **circular spreads, cascades, radial blooms, and card fans**.
* **Why it matters:** The model struggles to write the mathematical rotations and offsets needed for grouped asset layouts.

#### Gap C: Missing "Playful Proof Presentation" Rules
* **The Gap:** No guidelines for converting tables, checklists, and reviews into gamified, custom visual formats.
* **Why it matters:** Testimonials fallback to standard sliders.

#### Gap D: No Exception Rule for Motif-Driven Cards
* **The Gap:** Our design bans forbid cards, failing to distinguish generic SaaS feature boxes from bespoke, motif-driven structural cards.

#### Gap E: Absence of "Color-Reset Pacing" Guidelines
* **The Gap:** We don't document hard visual whiplash resets as intentional pacing devices.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Introduce the Structural Motif concept** in Cinematic Motion (requiring a physical theme for packaging and layout continuity).
* **Create a Creative-Agency Motion Submodule** detailing group layouts (Fan Spreads, Radial Blooms, Cascades, Shuffle Stacks) with math templates.
* **Establish Playful Proof rules** (transforming statistics and lists into gamified card blocks).
* **Define Color-Reset Pacing** (specifying contrast rules for section colors, keeping the motif consistent across changes).
* **Update the card ban rule** to allow bespoke motif-driven structural cards.
* **Mandate `motif-spec.md`** as a required asset-planning checklist (card types, front/back states, shadow rules, content hierarchy).
