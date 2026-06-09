# Hero Layout Blueprints & Composition Reference

This document serves as a structured reference library of premium composition formulas, typography systems, color theories, and asset behaviors. 

> [!IMPORTANT]
> **GUIDING LAW: INSPIRATION, NOT CONSTRAINT**
> These layouts represent visual and structural benchmarks. They are NOT a static template menu. 
> - **Custom-Tailored Strategy:** Every design must be derived from the brand's unique story (e.g., Presence Engineering).
> - **Hybridization:** You are encouraged to blend layouts (e.g., using the typography contrast of the "Editorial Presence" layout with the interactive metadata pinning of the "Annotated" layout).
> - **Apply the Principles:** Study *why* these formulas work (whitespace ratios, lighting coherence, motion tracks, type hierarchies) and apply these principles to create bespoke layouts.

---

## Global Header Rules (Consistent Foundation)

Every premium UI layout utilizes a fixed top navigation bar. Keep these properties static to ground the design:

* **Layout:** Full-width container, clear horizontal padding, flexbox layout, `justify-content: space-between`, `align-items: center`.
* **Left Element:** Minimalist, geometric brand logo (e.g., `ISGY & KOS` or `IN YENE` in all-caps, sans-serif).
* **Center Navigation:** Clean, sentence-case or lowercase links with wide letter spacing (e.g., `Products`, `Security`, `Pricing`, `About us`, `Log in`, `Eng` with a small dropdown chevron).
* **Right Element:** Pill-shaped or sharp rectangular high-contrast CTA button (e.g., `GET IN TOUCH`, `SHOP NOW`, `ORDER NOW`).

---

## Set 1: Aesthetic & Atmospheric Archetypes

### 1. The "Visual Power" Hero Section (Red Aesthetic)
* **Layout Style:** Split-screen overlay with a heavy center focus.
* **Color Palette:** Monochromatic dark mode crimson. Deep burgundy/black background (`#0A0000` to `#150000`), vibrant candy-red accents.
* **Typography:**
  * *Hero Text:* Elegantly oversized "Visual power" in a high-fashion serif font. Pure white, large scale (~96px), left-aligned but physically overlapping the central asset to create depth.
  * *Body/Meta Text:* Crisp, tiny sans-serif descriptor text tucked into the bottom-right corner.
* **Asset Treatment:** High-fashion studio portrait of a model with vibrant red hair and matching glossy red lipstick. The image has a dark, moody vignette that blends seamlessly into the black background.
* **Motion & Animation Potential:**
  * *Arrival:* Crimson wash over the background.
  * *Ambient:* A subtle candlelight flicker behavior reflecting off the model's red tones.
  * *Scroll-bound:* As the page scrubs, the main image scales down slightly (focusing depth) while the overlapping serif text translates slightly to the left.

### 2. The "Quietly Icon" Hero Section (Blue Aesthetic)
* **Layout Style:** Classic left-heavy split layout with asymmetric floating typography.
* **Color Palette:** Deep midnight blue, royal blue lighting, and crisp white text.
* **Typography:**
  * *Hero Text:* "Quietly icon" broken into two lines, stacked vertically on the right side of the screen. Display serif, stark white.
  * *Body Text:* Left-aligned narrative block in a clean, ultra-light sans-serif font.
  * *Social Links/Meta:* `BEHANCE`, `INSTAGRAM`, and `LINKEDIN` in small, tracked-out sans-serif caps, acting as floating anchor elements on the upper-left of the hero area.
* **Asset Treatment:** A side-profile artistic portrait of a model bathed in intense neon blue light, positioned slightly off-center left, creating an artistic contrast with the text on the right.
* **Motion & Animation Potential:**
  * *Arrival:* The model fades in from a deep shadow, and the blue neon highlight spills across the profile.
  * *Interaction:* Hovering over the social links generates a soft, blue glow trail beneath the cursor.

### 3. The "High Contrast Beauty" Hero Section (Teal Aesthetic)
* **Layout Style:** Ultra-minimalist modern editorial focusing heavily on negative space (whitespace).
* **Color Palette:** Soft, pale cyan/teal background mixed with stark black elements. High brightness, low saturation.
* **Typography:**
  * *Hero Text:* "High Contrast Beauty" stacked on the left. High-fashion serif with high contrast between thick and thin stroke weights.
  * *Body Text:* Positioned right next to the title in the center-right column. Clean, medium-weight sans-serif prose.
* **Asset Treatment:** A stark, graphic 3D render or vector illustration of a dark, stylized silhouette of an open hand. Acts as a minimalist stamp on the right side of the layout.
* **Motion & Animation Potential:**
  * *Scroll-bound:* The vector silhouette rotates slowly or translates on scroll, weaving behind the title but in front of the background.
  * *Arrival:* Elements reveal using a clean, sharp line mask wipe, mimicking a drawing being sketched out.

### 4. The "Editorial Presence" Hero Section (Stark White/Abstract)
* **Layout Style:** Asymmetric grid / Museum gallery style.
* **Color Palette:** Clean studio white background (`#FFFFFF`) paired with charcoal black typography (`#111111`).
* **Typography:**
  * *Hero Text:* "Editorial presence" written in a wide, luxury serif font on the left.
  * *Secondary Elements:* Small, scattered text blocks and navigation tags (`BEHANCE`, `INSTAGRAM`) placed on the bottom right to anchor the floating visuals.
* **Asset Treatment:** A central, vertical rectangular image container showcasing a metallic, chrome, or iridescent abstract 3D bust portrait. To its right, a smaller secondary circular or rectangular floating graphic container acts as a visual accent.
* **Motion & Animation Potential:**
  * *Ambient:* The chrome bust has a slow reflection loop (like studio light panning across metallic surfaces).
  * *Scroll-bound:* As the page scrolls, the secondary circular graphic floats up faster than the main bust (parallax depth shift).

---

## Set 2: Structural Layout Formulas

### 1. The "Split" Hero Section (E-Commerce / Product Focused)
* **Best Used For:** Physical products, apparel, or goods where seeing the item clearly is as important as the emotional messaging.
* **Layout Structure:** 50/50 vertical division. The left side handles the typography and CTA; the right side is reserved for a clean, high-contrast vertical product image container.
* **Color Palette:** Warm, organic earth tones (e.g., warm oatmeal/cream background `#EFEBE4` with dark charcoal text and a deep brown product asset).
* **Typography:**
  * *Hero Text:* Ultra-bold, high-contrast, distressed vintage serif font that dominates the upper left.
  * *Subtext:* Medium-weight sans-serif for description and small pill button below.
* **Motion Strategy:**
  * *Arrival:* The vertical image container reveals with a slide-up and scale-down wipe (e.g., from `scaleY: 1.2` to `1`).
  * *Scroll-bound:* Slow vertical translation (parallax) of the product image inside its cropped container.

### 2. The "Annotated" Hero Section (Technical / Experimental)
* **Best Used For:** High-performance gear, tech-wear, architectural products, or software where structural features need highlighting.
* **Layout Structure:** Massive, abstract background typography wrapped around a center grid. Features "annotations" (small, independent text cards or info-blocks) pinned to different coordinates of the layout like blueprints.
* **Color Palette:** Stark, modern industrial light-mode. Minimal cool grays, pure blacks, and neon accent highlights.
* **Typography:**
  * *Hero Text:* Massive, custom block-geometric typeface filling the upper layer.
  * *Annotation Blocks:* Small, hard-bordered square boxes containing technical specifications, acting like physical labels pinned to the layout.
* **Motion Strategy:**
  * *Arrival:* Letters of the massive backdrop text slide in horizontally.
  * *Interaction:* Hovering over annotation nodes displays micro-detail specs; lines connect nodes to the central object via dynamic SVG paths.

### 3. The "Editorial" Hero Section (Content / Storytelling Heavy)
* **Best Used For:** Agencies, premium services, online journals, or design-forward brands where philosophy and copy take priority over a single image.
* **Layout Structure:** Asymmetric 3-column newspaper grid setup. Two distinct paragraphs blocks sit side-by-side on top, while a massive, experimental typography layout anchors the bottom of the screen.
* **Color Palette:** Vibrant, bold editorial block colors (e.g., striking burnt orange/terracotta background `#D94B2B` with high-contrast bone-white typography).
* **Typography:**
  * *Hero Title:* Spread horizontally across the base in a mix of elegant script and clean sans-serif typefaces.
  * *Body Text:* Left-aligned, tightly tracked sans-serif blocks that read like a physical book or magazine spread.
* **Motion Strategy:**
  * *Arrival:* Text shifts upwards line-by-line with a staggered, low-friction ease.
  * *Ambient:* A subtle grain/noise filter overlay running across the background.

### 4. The "Illustrative" Hero Section (Creative / Dynamic Action)
* **Best Used For:** Sports, interactive platforms, dynamic applications, or experiential brands that rely on fluid movement or art assets.
* **Layout Structure:** Fluid composition where elements cross over grids. The background contains abstract geometric lines, wireframe circles, and vector artwork that weaves behind and between the text.
* **Color Palette:** Light, neutral gray/off-white backdrop mixed with high-contrast black vector art lines and a single bright pop of color (e.g., a neon green button).
* **Typography:** Left-heavy, all-caps sans-serif block tightly stacked vertically.
* **Asset Treatment:** Dynamic, fine-line vector drawings (like a court layout or planetary orbits) flowing freely through the background to guide the user's eye.
* **Motion Strategy:**
  * *Scroll-bound:* The background vector lines grow or animate along their paths on scroll using SVG stroke dashoffset.
  * *Ambient:* Subtle floating movement of the geometric shapes.

### 5. The "Magazine" Hero Section (High-Fashion / Editorial Portrait)
* **Best Used For:** Luxury items, celebrity/influencer features, high-end portfolios, or creative lookbooks where a human model or artistic focal point anchors the screen.
* **Layout Structure:** The background contains a massive, screen-filling word. A vertical portrait image cut-out sits dead-center, *overlapping* the giant text, creating an illusion of depth (3D layering).
* **Color Palette:** Muted, sophisticated dark tones. Earthy olive green or dark sepia palette with crisp white lettering.
* **Typography:**
  * *Hero Text:* Hyper-expanded, extra-black sans-serif font filling the top half.
  * *Subtext:* Centered beneath the main portrait image, leading directly to a single stark CTA button.
* **Asset Treatment:** Studio portrait photography with a model looking directly at the camera, cropped as a vertical rectangle sitting right over the giant background text.
* **Motion Strategy:**
  * *Arrival:* The model image splits/curtains open, revealing the massive text layer behind.
  * *Scroll-bound:* The background text translates horizontally while the model moves slightly vertically (asymmetric parallax).

### 6. The "Centered" Hero Section (Minimal / Impactful)
* **Best Used For:** Restaurants, premium dining, single-product drops, or boutique brands seeking instant, bold clarity with minimal clutter.
* **Layout Structure:** Absolute symmetry. Every single element—from the central visual mark to the copy and call-to-action button—is aligned directly down the center axis of the screen.
* **Color Palette:** Ultra-clean minimalist cream or parchment background with jet-black typographic elements.
* **Typography/Assets:**
  * *Hero Centerpiece:* Large, bold cultural logography (e.g., Japanese Kanji text or custom geometric symbol) acting as the main visual weight.
  * *Subtext:* Perfectly centered 2-line headline explaining the core value proposition directly underneath, followed immediately by a single centered button.
* **Motion Strategy:**
  * *Arrival:* The centerpiece ink reveals or morphs into place.
  * *Ambient:* Subtle light wash sliding from left-to-right across the centerpiece.

---

## Dynamic Layout Decider Guide

Use this table to match the brand identity and storytelling goal to the correct structural setup:

| Brand Type | Core Sensation | Recommended Formula | Recommended Aesthetic | Key Motion Archetype |
| :--- | :--- | :--- | :--- | :--- |
| **Physical Product / E-Commerce** | Tactile quality, direct purchase | **Split Layout** | Oatmeal/Cream or Crimson | Vertical image mask scrub |
| **Premium Services / Agency** | Thought leadership, design philosophy | **Editorial Layout** | Terracotta/Burnt Orange | Line-by-line staggered text drift |
| **Luxury / Creative Portfolio** | High fashion, deep immersion | **Magazine Layout** | Muted Dark Olive or Sepia | Depth layer shift (3D overlapping) |
| **Interactive Tech / Engineering** | Advanced precision, features | **Annotated Layout** | Industrial Cool Gray/Black | SVG path connector lines |
| **Active / Experimental Studio** | Fluid movement, culture | **Illustrative Layout** | Light Gray + Neon Pop | SVG stroke path scroll morphing |
| **Culinary / Boutiques** | Absolute focus, craft | **Centered Layout** | Parchment / Clean White | Centered reveal or ink drop morph |

---

## Prompting Strategy for AI Layout Engine

When prompting an AI model (image or web layout generator) based on these blueprints, use this structure to guarantee high-fidelity matching:

```text
Generate a modern, high-fashion editorial UI hero section. 
Use the [Insert Layout Formula, e.g., Magazine Layout] structure paired with the [Insert Aesthetic Name, e.g., Blue Aesthetic] color guidelines. 
The layout must feature a top navigation bar matching the Static Header Rules (all-caps logo, sentence-case menu, pill CTA). 
Incorporate [Insert Typography Rule, e.g., a hyper-expanded sans-serif title overlapping a vertical model cutout portrait]. 
Ensure the studio-lit asset matches the [Color Palette, e.g., deep midnight blue with royal blue lighting] and use generous asymmetric negative space.
```
