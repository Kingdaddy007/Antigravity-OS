# Audit Report: Site 01 — Oryzo Coaster Reveal (Apple-Style Parody)

### 1. Site Identity & Target Impression
* **Core Vibe:** Cinematic Satire, Ultra-Premium Tech Product Reveal (Apple flagship parity).
* **Audience:** Tech-fluent builders, design enthusiasts, and creators who appreciate high-end interaction design and spatial humor.
* **Overall Aesthetic:** Dark-mode luxury contrasting with sudden neon feature sections, sharp layout grids, ultra-precise typography, and seamless transitions centered on a single floating 3D object.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **The "Anchor Object" Pin:** The central visual focus is a floating 3D coaster that remains pinned (`position: sticky` or GSAP pin) in the center/right of the viewport. As the user scrolls, the page content slides up, fades, and restructures *behind* and *around* this single object.
* **Asymmetrical Split to Grid:** Section layouts shift dynamically from an asymmetric split (heavy left-aligned type, right-aligned floating object) to a three-column vertical lifestyle card grid, and then back to technical split-screens.
* **Whitespace & Scale:** Massive display typography ("SUSTAINABILITY" bleeding off the edges) contrasted with tiny, widely-tracked technical specs (10-12px). Generous margin and padding budgets prevent visual crowding.

#### Color & Texture
* **Dopamine Color Reset:** The site does not stick to a single monochromatic palette. It uses color to force psychological resets between features:
  * *Hero:* Deep, near-black (`#0a0a0a`) with warm, diffused radial ambient glow.
  * *AI Integration:* Warm amber/orange gradient sweep (`#ff7a00`).
  * *Thermodynamic:* Electric neon purple/magenta (`#8a2be2` to `#ff1493`).
  * *Grip Lock:* Kelly green cutting mat (`#00a86b`).
  * *Sustainability:* Warm off-white/beige.
* **High Contrast Sweeps:** Transitions between background colors are either scrubbed color tweens (gradual transitions) or rapid flash-cuts triggered at section thresholds to surprise the user.

#### Motion & Restraint
* **Timeline Scrubbing (80% of Motion):** The scrollbar is treated as a timeline playhead. If scrolling stops, the animation freezes. This applies to:
  * The rotation of the coaster (isometric tilt to flat top-down).
  * The "exploded wireframe" assembly sequence.
  * The deep zoom into the cork texture.
* **Triggered Animation (20% of Motion):** UI cards, text reveals, and reviews use trigger-once entrances (`toggleActions: "play none none reverse"`) to animate smoothly when their containers reach the viewport.
* **Restraint:** The navigation bar remains static and minimal, acting as a structural anchor. Paragraph body text does not move erratically; only display headings and primary assets participate in the timeline scrub.

#### Typography
* **Scale Contrast:** High contrast between massive display type (80px–150px) and micro-spec labels (10px).
* **Typography Animation:** Headings slide up through reveal masks (CSS `clip-path: inset()` or translation behind an overflow-hidden wrapper) rather than basic fades.

---

### 3. The Human/AI Split

#### Human Assets (The "20%")
1. **3D Render Image Sequence:** ~150 to 300 transparent PNG/WebP frames of the 3D coaster rotating, flattening, and expanding into an exploded wireframe view under identical lighting.
2. **Editorial/Lifestyle Mockups:** High-resolution photography of the coaster edited into absurd, high-fashion lifestyle mockups (e.g., styled on model's eyes or pockets), clipped cleanly from their backgrounds.
3. **Macro/Micro Assets:** A high-resolution transition video or image sequence zooming from a top-down coaster view into a microscopic fiber texture.
4. **Storyboard/Depth Map:** A chronological list of scroll coordinates mapping what the coaster is doing at each scroll position (e.g., 0-1000px = rotate, 1000-2000px = scale and overlay crop box).

#### AI Execution (The "80%")
1. **HTML5 Canvas Drawing Engine:** A GSAP-linked canvas renderer that maps the scroll position to the image sequence array index and draws the frame.
2. **GSAP ScrollTrigger Pinned Timelines:** Setting up the multi-layered master timeline, pinning the wrapper, and choreographing text reveals, background color sweeps, and grid slides.
3. **Responsive Grid Layouts & Fallbacks:** Managing CSS grid containers, absolute layers, and rendering CSS fallbacks for mobile layouts when pins are disabled.

---

### 4. Gaps in Current System

Comparing this premium execution to our active skills reveals critical systemic blind spots:

#### Gap A: Missing Canvas Image Sequence Scrubbing
* **The Gap:** [cinematic-motion/SKILL.md](../skills/cinematic-motion/SKILL.md) explains 3D rendering with R3F (React Three Fiber) and video scrubbing (`ffmpeg -g 1`). However, it has **zero guidelines or code templates for Canvas Image Sequence scrubbing**.
* **Why it matters:** Real-time WebGL/3D on the web is CPU/GPU heavy and prone to loading stutters. Canvas image sequences (drawing pre-rendered transparent WebPs on scroll) are the industry standard for Apple-style reveals. Our assistant has no template to write this performantly.

#### Gap B: No "Anchor Object Pinning" Choreography Template
* **The Gap:** The skills mention pinning/sticky layouts, but they lack a structural layout blueprint for keeping a single visual asset pinned in the viewport while section backgrounds wipe behind it and text elements slide past it.
* **Why it matters:** Without a clear layout structure (e.g., a `.pin-wrapper` holding a `.canvas-container` set to `position: absolute` or `sticky`, and sibling `.scroll-section` triggers), the assistant tries to write ad-hoc CSS positioning, leading to scroll gaps and overlapping layers.

#### Gap C: Lack of Dynamic Color Reset Guidelines
* **The Gap:** [ui-ux/SKILL.md](../skills/ui-ux/SKILL.md) and [color-and-contrast.md](../skills/ui-ux/reference/color-and-contrast.md) focus on choosing a singular, cohesive color strategy (Restrained, Committed, etc.). They lack rules for scroll-driven color shifts or sudden high-contrast resets to create visual pacing.
* **Why it matters:** The assistant defaults to a single background color throughout the page, resulting in a monotonous scroll experience.

#### Gap D: Missing Text-Reveal Mask Patterns
* **The Gap:** Current text reveals in `cinematic-motion/SKILL.md` rely on basic SplitText fade-ups. The clean, sharp "appearing behind an invisible wall" mask-reveal (using CSS `clip-path` or nested container translations) is not explicitly detailed with a code pattern.
