# Audit Report: Site 09 — Joby Aviation (Aspirational Corporate Narrative)

### 1. Site Identity & Target Impression
* **Core Vibe:** High-Stakes Visionary Optimism, Institutional Trustworthiness, Effortless Flow, and Approachable Authority.
* **Audience:** A broad mix of investors, regulators, B2B ecosystem partners, and future passengers who need to believe a futuristic, speculative category is safe, real, and ready for deployment.
* **Overall Aesthetic:** Bright, sun-drenched photography, airy sky-blue backgrounds, friendly typography, and clean, layered layouts.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Aspirational Credibility Ladder:** The layout progresses through a strict cognitive sequence:
  1. *Experiential Hook:* Cockpit-view passenger videography (emotional alignment).
  2. *Service Convenience:* Parallax card grids outlining app-based door-to-door flight.
  3. *Technical Legitimacy:* Closeups of tilt-rotor mechanics (de-risking technology).
  4. *Ecosystem Validation:* Scroll-linked partner grid (Delta, Uber, ANA).
  5. *Emotional Resolve:* Sky-blue illustrated vision of everyday integration.
* **Alternating Structural Focus:** Full-bleed cinematic video → off-white space with inset cards → structured split-scroll list → full-bleed hero bridge → vector illustrated canvas.
* **Technical Softening:** Aerodynamic curves (rounded border-radius), warm sunset light, and human-centric framing make complex aerospace engineering feel consumer-ready.

#### Color & Texture
* **Optimistic Sky Palette:** Deep sunset orange (`#ff7a00`), sky blue (`#1da1f2`), clean off-whites (`#f8f8f8`), and deep corporate branding blue.
* **Textured Realism to Vector Illustration:** Photographic realism carries the technical proof, while a clean vector city skyline illustration handles the emotional climax.

#### Motion & Restraint
* **Buoyant Scroll-Slide:** Elements slide upward softly, mimicking flight patterns. Snappy, rigid, or chaotic transitions are completely avoided.
* **Scroll-Linked Proof Module:** A pinned section where vertical scrolling on the left shifts through partner categories (e.g., Infrastructure, Airlines) while crossfading matching logo visuals on the right.
* **Graphic Wave Wipes:** Symmetrical colored wave lines (blue and orange) slide up to wipe the screen into the final footer.

#### Typography
* **Approachable sans-serif:** Friendly, rounded geometric sans ( Sofia Pro / Gordita) maintains authority without standard luxury austerity or startup clutter.

---

### 3. The Human/AI Split

#### Human Assets (The "20-30%")
1. **Graded Persuasion Video Sets:** Cockpit interior shots, exterior drone flight videos, and technical asset photos graded under identical warm lighting.
2. **Ecosystem & Partner Assets:** Logos and product shots of global validating brands (Uber, Delta, etc.).
3. **Optimistic City Illustration:** A custom vector landscape showing eVTOL integration in modern cityscapes.

#### AI Execution (The "80-70%")
1. **Multi-State Scroll-Tab System:** Writing the GSAP ScrollTrigger to track list-item offsets and crossfade active visual slides on the right.
2. **Floating Parallax Card Grid:** Scaffolding the CSS absolute overlays and offset Y-axis scroll translations.
3. **SVG Wave Animations:** Animating vector waves during footer reveal sequences.

---

### 4. Gaps in Current System

Comparing the Joby Aviation site to our active skills reveals the following gaps:

#### Gap A: Lack of "Aspirational Credibility Ladder" Pacing
* **The Gap:** We don't document **corporate persuasion sequencing** ( Experience → Service → Tech Proof → Ecosystem Proof → Visionary Resolve).
* **Why it matters:** The model designs sections for decoration rather than building structured validation loops for high-stakes business audiences.

#### Gap B: No Code Pattern for "Scroll-Linked Proof Modules"
* **The Gap:** [cinematic-motion/SKILL.md](../skills/cinematic-motion/SKILL.md) lacks code frameworks for **category lists driving pinned showcases**.
* **Why it matters:** The model struggles to coordinate vertical list offsets with absolute right-aligned image fades, causing timing lag.

#### Gap C: Omission of "Optimistic Technology" / Technical Softening Rules
* **The Gap:** [ui-ux/SKILL.md](../skills/ui-ux/SKILL.md) focuses on either minimalist luxury (monochrome/serifs) or startup tech (dark modes/snappy curves). It lacks instructions for **Optimistic Technology / Technical Softening** (rounded type, sunset warmth, accessibility).
* **Why it matters:** The model defaults to dark-mode SaaS templates, making infrastructure projects look like software widgets.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the "Aspirational Credibility Ladder" layout sequence** to Storytelling.
* **Provide "Scroll-Linked Proof Module" GSAP boilerplate** in Cinematic Motion.
* **Establish an "Optimistic Technology" brand register** in UI/UX (rounded shapes, warm PBR lighting, accessible copy).
* **Incorporate "Credibility Asset Maps"** in project workflows.
