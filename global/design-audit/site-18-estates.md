# Audit Report: Site 18 — Estates (Billionaire Minimal Real Estate)

### 1. Site Identity & Target Impression
* **Core Vibe:** Quiet Power, Billionaire Minimalism, Discretion and Exclusivity, and Calm Architectural Authority.
* **Audience:** Ultra-high-net-worth individuals, elite real-estate investors, and off-market advisory clients who value taste and curation over transaction speed.
* **Overall Aesthetic:** Full-bleed cinematic panoramas, "invisible" edge-only UI controls, high-contrast typography, and a strict light-to-dark emotional rhythm.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Full-Bleed Viewport Sections:** Each page act completely consumes the screen, removing standard headers, footers, and margins to let the imagery dominate.
* **Invisible UI Framing:** Eliminates all border strokes, buttons, and traditional listing grids. Links are reduced to plain, tracked-out text elements.
* **Bento Decompression Grid:** Closes the sequence with a warm, asymmetric bento layout (using soft `border-radius: 12px` corners), acting as an inviting, resting landing zone after intense full-screen chapters.

#### Color & Texture
* **Atmospheric Scene Delimiters:** The color script relies on the light grading of the property films:
  * Bright Sunset: Golden-hour warmth, luxury vista.
  * Wooden Interior: Warm dining lighting, intimacy.
  * Night City: Nocturnal shadow, urban scale.
  * Black & White: Technical/advisory interstitial (typographic reset).
  * Warm Beige (`#f7f5f0`): Grounded, human grid.
* **Textured Architecture:** Exposed brutalist concrete, warm oak grain, and soft ambient shadow gradients inside the media clips.

#### Motion & Restraint
* **Stacked Media Panels:** Pinned full-screen layout cards slide vertically upward over one another, applying a soft drop-shadow (`box-shadow: 0px -20px 50px rgba(0,0,0,0.5)`) on the entering panel to sell the physical overlapping sheet depth.
* **Contrast Pacing:** Alternates high-intensity cinematic camera pans with flat, static typographic resets (pure black and white) to prevent visual exhaustion.
* **Heavy Scroll Hijacking:** Integrates smooth scrolling (e.g. Lenis) with high friction parameters to translate quick trackpad gestures into slow, museum-grade pans (0.8s - 1.2s).

#### Typography
* **Editorial Contrast pairing:** Refined high-contrast serif for narrative section headers, paired with a commanding modern sans-serif (Neue Haas Grotesk) for manifesto statements.
* **Utilitarian Micro-Labels:** Small uppercase copy, tracked widely, used for labels and concierge details.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Graded Property Films:** 4–6 high-resolution cinematic video loops edited as a cohesive family sharing the same lighting and tone.
2. **Concise Copy System:** Short, high-impact copy lines written to fit negative spaces.
3. **Property Media Edit Sheet:** A document mapping clip order, targeted lighting quality, text overlay coordinates, and transition types.

#### AI Execution (The "80-60%")
1. **Lenis Scroll Controller:** Initializing and configuring the smooth scroll script with heavy dampening.
2. **GSAP ScrollTrigger Stacking Timeline:** Writing the pinning and translation logic that slides panels up from `yPercent: 100` to `0` with a linear scrub.
3. **Responsive Image Grid Reveal:** Implementing container reveals (`overflow: hidden`) that scale background images from `1.1` to `1.0` upon scrolling into view.

---

### 4. Gaps in Current System

Comparing the Estates site to our active skills reveals the following gaps:

#### Gap A: Absence of "Billionaire Minimal / Private Estates" Brand Archetype
* **The Gap:** [cinematic-motion/SKILL.md](../skills/cinematic-motion/SKILL.md) groups luxury under general guidelines. It has no specific rules for billionaire minimal brands, which require the absolute removal of listing grids, button borders, and search filters.
* **Why it matters:** The model defaults to adding standard listing-site cards and search inputs, cheapening the brand.

#### Gap B: Lack of the "Stacked Media Panels" Pattern
* **The Gap:** No specific code template in our motion files for vertical section overlays with drop shadows.
* **Why it matters:** The model uses standard scroll sections, losing the "glass slab" sliding effect.

#### Gap C: Missing "Invisible UI" Design Rules
* **The Gap:** No specifications on when and how to conceal navigation and style CTAs purely as quiet, un-bordered concierge contact links.
* **Why it matters:** The model places prominent call-to-action buttons that break the cinematic immersion.

#### Gap D: Missing Bandwidth-Aware Cinematic Media Optimization Guide
* **The Gap:** Our performance rules lack specific guides for high-latency mobile networks, including FFmpeg target compression rates (under 3MB), WebM containers, progressive poster frame swapping, and mobile video-to-still swaps.
* **Why it matters:** Heavy video files lag and stall on mobile screens, ruining the luxury experience.

#### Gap E: No Property Media Edit Sheet Spec
* **The Gap:** Workflows don't require the user to storyboard the emotional lighting contrast and shot order of background clips.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the "Private Estates / Billionaire Minimal" archetype** to the brand-to-motion matrix, enforcing invisible UI, slow pacing, and zero listing grids.
* **Create the "Stacked Media Panels" code template** in Cinematic Motion Engineering, detailing vertical overlay pinning and shadow offsets.
* **Establish an "Invisible UI" guideline** (eliminating borders, converting buttons to plain text, and styling navigation as a quiet, borderless utility).
* **Write the "Cinematic Media Optimization Guide"** for low-power mobile viewports:
  - Compress background videos to WebM containers under 3MB using FFmpeg.
  - Require a static poster image frame matching the first frame of each video.
  - Implement mobile media queries that swap autoplay videos for high-res static images on narrow screens.
* **Mandate `property-media-edit.md`** as a required planning file in visual brainstorm workflows.
