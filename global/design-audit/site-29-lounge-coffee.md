# Audit Report: Site 29 — Lounge Coffee (Immersive Coffee Experience)

### 1. Site Identity & Target Impression
* **Core Vibe:** Playful, Premium Sensory World, Physical Web Theater, and Appetite-Driven Storytelling.
* **Audience:** Coffee enthusiasts and premium hospitality customers seeking sensory indulgence and product charm rather than dry transactional grids.
* **Overall Aesthetic:** Burnt Orange (`#D54215`), Cream (`#F6F4F0`), Stark Black (`#111111`), Mustard Yellow (`#EBB040`), and oversized floating 3D product sculptures.
* **The "Before" vs "After" Redesign Upgrade:**
  * *Before (The Stale AI Baseline):* A generic Shopify template. Dark muddy brown/black, centered text, flat mustard yellow buttons, background video of floating coffee beans, standard block-by-block left-image right-text grids, and repeated 3-column product list. Lifeless structure without storytelling.
  * *After (The Alive Human Redesign):* A dramatic brand entrance. Burnt orange gradient backdrop containing a single central 3D coffee bean. Bean splits to pour white liquid (milk mask wipe), revealing a soft cream page with three massive 3D cups layered on the Z-axis. Scroll-scrubbed cup translations, text reveal behind objects, staggered overlapping cards, and a quiet, clean, highly structured shopping grid.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Experience-then-Store Layout:** The site organizes itself as a narrative procession rather than a commercial layout. It prioritizes sensory mood first, and only transitions into shopping grids once appetite is established.
* **Oversized Product Sculpture:** Product renders are treated as massive 3D sculptures that dominate layout boundaries, floating in front of text layers rather than sitting inside boxed grid containers.
* **Whitespace Palette Cleanser:** The high-intensity, visually dramatic product features are followed by a quiet, minimal menu section on a pure white background with generous whitespace to prevent cognitive fatigue.
* **Overlapping Card Stack:** Product cards stack on top of each other dynamically on scroll (resembling a deck of cards or polaroids), scaling down and fading inactive cards behind the main focused card.

#### Color & Texture
* **Warm Contrast Palette:** Rich burnt orange and mustard yellow accents contrasting with premium warm cream background tones.
* **Silhouetted Material Quality:** Clean, high-resolution product drink images with uniform lighting and soft drop shadows, making objects pop off the white screen.

#### Motion & Restraint
* **The Hook (The "Milk Split"):** A signature preloader reveal. A single centered coffee bean splits in half, pouring a white fluid stream that expands horizontally to wipe the canvas and reveal the website.
* **The Climax (Scroll-Scrubbed Assembly):** GSAP ScrollTrigger timeline pins the hero and controls spatial cup translations:
  - Red (left) and Yellow (right) cups slide and rotate off-screen.
  - Black (center) cup scales up, rotates 15 degrees for kinetic posture, and anchors the viewport.
  - Large background typography scales and fades in *behind* the black cup.
* **Restraint & Pacing:** The menu grid remains completely static, utilizing clean CSS transitions for hover actions only, providing visual breathing room.

#### Typography
* **Extreme Scale Contrast:** Enormous display serifs (120px+) for brand headlines layered behind the product meshes, contrasted with small, tight, clean sans-serifs (14px) for transactional prices and details.

---

### 3. The Human/AI Split

#### Human Assets (The "Scene Kit" — 20-40%)
1. **Coherent Render Family:** High-resolution transparent PNG renders of coffee cups (Red, Yellow, Black) and coffee beans sharing identical top-down studio lighting, reflections, and camera perspectives.
2. **Liquid Mask Transition:** Custom SVG paths or Lottie files representing the fluid "milk split" masking effect.
3. **Appetite Imagery:** Silhouetted menu photography with consistent soft drop shadows.
4. **Section Rhythm Map:** Planning outline showing where visual intensity peaks and where it drops into quiet commerce.

#### AI Execution (The "Code Assembly" — 80-60%)
1. **Z-Index Sandwich Stacking:** Absolute positioning layers stacking background text, cups, and floating badges.
2. **Horizontal Curtain Wipe:** Coding the GSAP timeline mapping the SVG milk-mask wipe on load.
3. **Scroll-Scrubbed Layout Morph:** Orchestrating the GSAP timeline translates and scales the cups relative to the scrollbar.
4. **Stacked Card Controller:** Writing ScrollTrigger calculations that stack, scale, and fade the polaroid cards.

---

### 4. Gaps in Current System

Comparing the Lounge Coffee site to our active skills reveals the following gaps:

#### Gap A: Absence of the "Hero Event" Concept
* **The Gap:** [cinematic-motion/SKILL.md](../skills/cinematic-motion/SKILL.md) describes entrance animations but does not require defining a **Hero Event**—a single physical reveal, split, spill, peel, cut, burst, pour, or transformation that anchors the site's identity.
* **Why it matters:** Entry sequences default to generic fade-ups or slide-ins, losing brand theater.

#### Gap B: No "Experience-then-Store" Pattern
* **.The Gap:** [ui-ux/SKILL.md](../skills/ui-ux/SKILL.md) does not specify that food, beverage, and luxury product sites must establish sensory appetite and brand mood before presenting commerce modules.
* **Why it matters:** The model immediately builds functional Shopify-like storefront grids, bypassing the appetite hook.

#### Gap C: Lack of "Palette Cleanser" Spacing Guidelines
* **The Gap:** We do not mandate a rhythmic layout structure that alternates high-intensity visual sequences with quiet, high-whitespace grids, leading to visual clutter.
* **Why it matters:** Pinned animations run back-to-back, exhausting the viewer.

#### Gap D: Missing "Anti-Template/Anti-Slop" Preflight Step
* **The Gap:** Workflows don't force the developer to analyze the obvious semantic layout a "lazy AI" would generate from the prompt, and actively ban those defaults.
* **Why it matters:** The assistant falls back to centered heroes, three-column grids, and flat image-left text-right blocks.

#### Gap E: Incomplete Hospitality/Appetite Visual Rules
* **The Gap:** We lack rules for utilizing surreal scale (oversized product sculptures) and silhouetted appetite assets for food and beverage sites.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the "Hero Event" mandate** to Cinematic Motion guidelines (requiring a single physical action like split, peel, spill, or pour to open the site).
* **Create the "Experience-then-Store" layout recipe** in UI/UX and Storytelling skills (prioritizing sensory branding before showing grids).
* **Establish "Palette Cleanser" pacing rules** (requiring highly structured, static sections with massive whitespace after scroll-scrubbed visual sequences).
* **Integrate the "Anti-Template Preflight Question"** into Visual Brainstorm workflows: *"If a basic layout tool generated this, what would it look like? Ban that layout immediately."*
* **Add "Surreal Scale" rules** for appetite-led brands (beverage, food, luxury) allowing product sculptures to take up 80%+ of the viewport.
* **Mandate two new planning files** in workflows:
  - `hero-event-blueprint.md` (defining the start, transformation vector, mask parameters, and final state of the page-load reveal).
  - `section-rhythm-flow.md` (mapping the user's cognitive wave: Brand Hook -> Visual Climax -> Palette Cleanser Commerce -> Footer Anchor).
