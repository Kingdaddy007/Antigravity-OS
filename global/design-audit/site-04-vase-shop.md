# Audit Report: Site 04 — Chinese Porcelain Vase Shop (Narrative E-commerce)

### 1. Site Identity & Target Impression
* **Core Vibe:** Interactive Museum Exhibit, Opulent Historical Craft, Tactile/Story-First E-commerce.
* **Audience:** Design-literate consumers and collectors who value premium craftsmanship, cultural storytelling, and headless e-commerce over generic Shopify grids.
* **Overall Aesthetic:** Symmetrical, clean parchment backgrounds, high-contrast serif typography, traditional ink/watercolor textures, and photorealistic product showcases.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Symmetrical "Curtain" Entry:** The page opens with two massive, ornate vase-painted pillars framing the left and right edges. Scrolling slides them horizontally out of the viewport, "opening the gates" to the shop.
* **Museum-Grade Negative Space:** Vases are presented in isolation with massive negative space, elevating them from "retail items" to "historical artifacts."
* **Z-Pattern to Horizontal Track:** The layout flows from a vertical Z-pattern (alternating text and spinning vases) into a pinned horizontal gallery track displaying different dynasties.

#### Color & Texture
* **Imperial Palette:** Stark white and parchment (`#fcfcfc`), ink charcoal (`#1a1a1a`), imperial yellow (`#ffd700`), cinnabar red, and cobalt blue.
* **Organic Textures:** Torn rice paper, thick dry ink brush strokes, and porcelain glazes.

#### Motion & Restraint
* **Organic Brush-Stroke Mask:** A transition into a landscape scene uses a custom, jagged ink-brush stroke mask (CSS `mask-image` or WebGL alpha matte) that expands from the center outward.
* **360-Degree Vase Spin:** Products rotate on their Y-axis linked directly to scroll progress (scrubbed canvas image sequence).
* **Extreme Glaze Zoom & Crossfade:** The camera zooms aggressively *into* the texture of the vase, which crossfades into a flowing video of ocean ripples (glaze morphs to water).

#### Typography
* **Expressive Serifs:** Elegant, high-contrast serifs (similar to *Playfair Display* or *Cormorant Garamond*) are used for narrative headings, while small, neutral sans-serifs handle e-commerce details and micro-captions.

---

### 3. The Human/AI Split

#### Human Assets (The "20%")
1. **360 Product Sequence Render Sets:** ~100 high-resolution transparent WebP/PNG frames of each vase rotating 360 degrees.
2. **Textured Alpha Mattes:** Custom SVG paths or black-and-white alpha-matte images (torn paper edge, jagged ink brush stroke) for the organic masks.
3. **Looping Environment Video:** Highly compressed water/ripple footage.
4. **Compositions / Illustrative Art:** Culturally aligned landscape art (misty mountains, pagodas).

#### AI Execution (The "80%")
1. **Curtain Reveal & Pinning Logic:** Writing the GSAP ScrollTrigger to split elements along the X-axis and handle pinned sections.
2. **Horizontal Track Math:** Translating vertical scroll depth to horizontal X-axis translation for the product catalog.
3. **Canvas Image Sequence Renderer:** Drawing the correct rotation frame to the canvas based on scroll percentage.
4. **Headless E-commerce Hooks:** Scaffolding the connection to a headless Shopify Storefront API to fetch prices, cart state, and product titles.

---

### 4. Gaps in Current System

#### Gap A: No Horizontal Scroll-Catalog Template
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) documents infinite sliders with modulo, but does **not provide a layout or GSAP blueprint for vertical-to-horizontal pinning tracks**.
* **Why it matters:** The model struggles to calculate the width/scroll-bounds of horizontal tracks, leading to broken responsive grids or scroll-jacking bugs.

#### Gap B: Lack of Organic/Textured Masking Patterns
* **The Gap:** We document standard geometric scale-up masks (like circles or boxes), but lack guidelines for **organic/textured alpha-masking** (torn paper, brush strokes, paint splatters) using CSS `mask-image`.
* **Why it matters:** The assistant defaults to clean, vector-perfect geometric masks, which look "digital/AI-made" instead of hand-crafted or thematic.

#### Gap C: No Curtain-Reveal Layout Blueprint
* **The Gap:** We lack a structural styling guide for a symmetrical "curtain pull" intro (elements sliding horizontally to reveal centered background visual anchors on scroll).

#### Gap D: Missing Headless Storytelling E-commerce Architecture
* **The Gap:** [ui-ux/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/ui-ux/SKILL.md) treats e-commerce as standard UI (grids, listings). It lacks rules on how to blend product data with narrative acts, resulting in typical retail templates instead of museum-like portfolios.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add "Vertical-to-Horizontal Pinned Track" GSAP boilerplate** to Cinematic Motion.
* **Incorporate CSS `mask-image` alpha-matte code patterns** for organic masks.
* **Provide structural layout patterns for Symmetrical X-Axis Splits** (curtains).
* **Write guidelines on Headless Narrative E-commerce integration**, blending story flows with API storefront bounds.
