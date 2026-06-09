# Audit Report: Site 23 — Hool Labs (Zero-Gravity Cosmetics)

### 1. Site Identity & Target Impression
* **Core Vibe:** Zero-Gravity Skincare, Ethereal Cosmos, Gen-Z/Millennial Luxury, and High-Fidelity Glassmorphism.
* **Audience:** Beauty and cosmetics consumers seeking trendy, high-performance, and visually bold skincare presentation.
* **Overall Aesthetic:** Saturated neon magenta, purple, and soft peach gradients (`#d53a9d` to `#ffb6b9`), iridescent product materials, soft volumetric cloud layers, and rounded frosted glass overlays.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Visual Layering (Behind-Text Object):** The floating 3D skincare bottle sits in front of the main display typography, creating immediate depth inside a single viewport.
* **Interactive Constellation Grid:** A testimonial map structured as scattered node elements (customer avatars) connected by curving lines, replacing standard card sliders.
* **Staggered Overlapping Showroom:** A showroom section featuring a series of rounded, glassmorphic panels that overlap and cascade vertically.
* **macOS Window Stacking:** UI blocks styled as Apple macOS desktop windows, sliding vertically and stacking behind each other on scroll.

#### Color & Texture
* **Saturated Celestial Gradients:** Saturated magenta and soft pastel peach tones that merge continuously across sections.
* **Glassmorphic Materiality:** High-density frosted glass textures (`backdrop-filter: blur(16px)`) with semi-transparent white borders.
* **Anti-Gravity Textures:** Iridescent metallic product finishes and translucent floating bubble assets.

#### Motion & Restraint
* **Governing Physics Sentence:** Every motion—floating bubbles, Y-axis bottle drift, and cloud panning—is bound to one world law: *"Skincare suspended in a soft cosmic vacuum."*
* **Low-Amplitude Ambient Drift:** Idle elements use randomized, desynchronized `sine.inOut` loops (3s to 6s durations, 15px-30px offsets) to create weightlessness. This acts as subtle environment motion, preventing the site from looking static without seeking direct attention.
* **Deep Parallax Card Stack:** Glass cards translate vertically at different speeds relative to the scroll playhead, creating a 3D parallax corridor.
* **Magnetic Node Testimonials:** Moving the cursor attracts nearby avatar nodes in the constellation map, and clicking a node reveals glass reviews.

#### Typography
* **Delicate high-contrast Serif:** Elegant display serif headlines (e.g. Voyage) representing beauty authority.
* **Micro tracked Sans-Serif:** Clean, tracked utility labels for UI navigation.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Iridescent 3D Product Renders:** Highly detailed skincare bottle meshes with metallic, translucent, and iridescent texture maps.
2. **Volumetric Cloud Shaders:** Custom GLSL shaders or high-res visual assets representing drifting space clouds.
3. **Glass UI Styling Specifications:** Define exact blur parameters, border alphas, and shadow offsets to guarantee text readability over colorful backgrounds.
4. **Constellation Map Wireframe:** Coordinate nodes list and connectors path design.

#### AI Execution (The "80-60%")
1. **WebGL Canvas Setup:** Scaffolding the React Three Fiber container, adding ambient lights and mesh rotation scripts.
2. **GSAP Float Loops:** Writing the desynchronized sine loops for bubbles and product bobs.
3. **Interactive Cursor Attractor:** Math scripts mapping mouse position to SVG node offsets (magnetic hook).
4. **Parallax Scroll Controller:** Implementing the vertical stacking offsets for the glassmorphic showroom cards.

---

### 4. Gaps in Current System

Comparing the Hool Labs site to our active skills reveals the following gaps:

#### Gap A: Absence of the "Governing Physics System" Concept
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) describes motion styles, but does not enforce declaring a single physical world law (e.g. zero-gravity, drag, magnetism) to unify animations.
* **Why it matters:** The model mixes unrelated CSS transitions, creating visual chaos.

#### Gap B: No Category Split for Motion Types
* **The Gap:** We treat all movement as a single category, lacking a split between **ambient drift** (low-impact environment), **narrative scroll** (scrubbed sections), and **interactive mouse tracking**.
* **Why it matters:** The model uses high-intensity attention-seeking animations where quiet environmental motion is needed.

#### Gap C: Missing "Interactive Constellation / Node Field" Pattern
* **The Gap:** No guidelines or code patterns for managing coordinate-based node maps, connecting SVG lines, and magnetic hover responses.
* **Why it matters:** The model defaults to standard, boring testimonial sliders.

#### Gap D: Lack of Warnings Against "Trend Props"
* **The Gap:** We do not warn against the overuse of Dribbble-centric trend elements (macOS window frames, heavy glass loops) that dilute timeless brand messaging.
* **Why it matters:** AI-designed sites look dated very quickly.

#### Gap E: Omission of the "Beauty/Cosmetics" Brand Archetype
* **The Gap:** The brand-to-motion matrix lacks a beauty profile (demanding soft materials, slow buoyant pacing, and luminous surfaces).

#### Gap F: Weakness in the AI Slop Test
* **The Gap:** Our quality checks don't ask if the layout remains compositionally distinct once colorful gradients and blur filters are removed.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the Governing Physics Sentence requirement** to Cinematic Motion planning (requiring a single physics rule before coding).
* **Introduce a Motion Classification Split** (defining Ambient, Narrative, and Interactive motion guidelines).
* **Create the "Interactive Constellation / Node Field" code pattern** in Cinematic Motion Engineering (handling coordinate paths and magnetic cursor attractors).
* **Add the "Beauty/Cosmetics" Archetype** to the motion matrix (specifying soft materials, slow buoyant pacing, and luminous surfaces).
* **Incorporate a Trend Prop Warning** inside UI/UX guidelines (limiting macOS windows and floating bubbles to direct brand alignments).
* **Upgrade the AI Slop Test** in Code Review & Quality Auditing:
  - Ask: *"If I strip all gradients and blur filters, does the layout still stand on a unique compositional grid?"*
