# Audit Report: Site 07 — Springs (Editorial Real Estate)

### 1. Site Identity & Target Impression
* **Core Vibe:** Premium Architectural Digest, Editorial Real Estate, Organic Luxury, and Curated Pacing.
* **Audience:** Affluent, design-conscious buyers, investors, and high-end consumers who expect taste, prestige, and quiet authority over traditional real-estate listings.
* **Overall Aesthetic:** Magazine-style grids, overlapping absolute elements, earthy colors, and expansive negative space.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Editorial Grid-Breaking:** Content layout bypasses standard linear grids. Cards, images, and text boxes overlap, breaking bounds to emulate a printed magazine.
* **The Parallax Card Stack:** Multiple layers (background container, main architectural render, floating inset cards, and staggered text) scroll on the Y-axis at slightly offset speeds, creating deep DOM-based parallax without WebGL.
* **Structured Chaptering:** The scroll journey is organized into distinct, focused narrative acts (Descent → Wellness → Nature → Interiors → Location).

#### Color & Texture
* **Earthy Chapter Palettes:** Deep forest greens (`#1a332d`), warm sand/beige (`#e8e3d8`), and natural leaf teals. The background colors transition between sections to signal a change in narrative topic.
* **Organic Media Textures:** High-resolution slow-motion videos (rippling sun-dappled water, rustling leaves) are used as structural backdrops.

#### Motion & Restraint
* **Sustained Editorial Momentum:** The site rejects theatrical visual climaxes. Instead, it maintains a silken, continuous scrolling velocity.
* **Inertial Smooth-Scroll Physics:** A smooth-scroll overlay (like Lenis) adds drag and follow-through to the scrollbar, eliminating browser scroll jitter on absolute elements.
* **Exponential Decelerations:** Elements enter quickly and settle slowly (`ease-out`), giving weight and physical presence to the transitions.

#### Typography
* **Serif-Sans Tension:** Elegant display serifs (similar to *PP Editorial New* or *Ogg*) carry the storytelling emotion, while geometric sans-serifs handle lists, statistics, and UI labels.

---

### 3. The Human/AI Split

#### Human Assets (The "20%")
1. **Multi-Crop Render Packages:** Renders and photographs cropped at multiple aspect ratios (full-bleed backgrounds, portrait inset cards, landscape cards, mobile fits).
2. **The Layer Map:** A blueprint defining the layout stack (which elements overlap, their z-index values, and their parallax speed ratios).
3. **Editorial Typography Guide:** Font rules setting where serifs handle narrative and where sans handles information.

#### AI Execution (The "80%")
1. **DOM Layering & CSS Grid:** Writing the absolute layouts and responsive container styling.
2. **GSAP ScrollTrigger Parallax:** Coding the timeline offsets and animating element translations based on scroll progress.
3. **Lenis Integration:** Configuring smooth-scroll scripts to ensure frame rates remain high during layered scrolls.

---

### 4. Gaps in Current System

Comparing the Springs site to our active skills reveals the following gaps:

#### Gap A: Lack of "Editorial Card Overlap" Styling Guide
* **The Gap:** [ui-ux/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/ui-ux/SKILL.md) lacks guidelines for **asymmetric overlapping layouts**. It defaults to standard columns, flexboxes, or grids, which makes layouts look templated.
* **Why it matters:** The model struggles to write overlapping cards that scale responsively without clipping text or breaking alignment.

#### Gap B: No "Layer Map" Workflow Step
* **The Gap:** Our project visual workflow does not require the creation of a **Layer Map** (defining overlapping z-indexes and scroll speed offsets) before writing CSS.
* **Why it matters:** The AI writes trial-and-error parallax code that often miscalculates layer priority, causing background cards to block click actions or float in front of text.

#### Gap C: "Peak Climax" vs. "Sustained Momentum" Pacing
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) teaches a 4-act structure culminating in a single visual climax. It lacks a pacing model for **Sustained Editorial Momentum** where sections are balanced equally as magazine chapters.

#### Gap D: Missing Practical Data Styling Rules
* **The Gap:** We don't define how to integrate practical database specs (amenity lists, location maps, distance tables) into an editorial aesthetic, causing these sections to drop back into standard, boring corporate layouts.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add "Editorial Parallax Card Stack" CSS/GSAP boilerplate** to Cinematic Motion.
* **Require a "Layer Map"** in visual layouts.
* **Draft "Sustained Momentum Pacing" rules** (equal weight scene-chaptering).
* **Write guidelines for "Practical Data Integration"** (styling specs, maps, and list details for editorial layouts).
