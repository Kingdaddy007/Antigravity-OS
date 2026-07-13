# Audit Report: Site 30 — Nauta (Enterprise Supply Chain OS)

### 1. Site Identity & Target Impression
* **Core Vibe:** Authoritative, High-Tech Systems, Enterprise-Chic, and Structured Credibility.
* **Audience:** Global supply chain operators and logistics enterprises who require system trust, structured info architecture, and functional logic rather than lifestyle marketing.
* **Overall Aesthetic:** Clean white background layouts, deep maritime navy infrastructure bands (`#0A1128`), vibrant primary blue conversion sections (`#1D4ED8`), and sharp tech-focused typography.
* **The "Premium SaaS" Shift:** Unlike generic SaaS templates, Nauta gains its premium feel through high-end custom illustrations, a "living" product simulation, and structural confidence, rather than performative scroll movies or decorative cartoon shapes.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Premium Product-Register Split Layout:** High contrast division between narrative text (left column, 35% width) and responsive HTML mockups (right column, 65% width) within a pinned viewport wrapper.
* **Hard-Cut Narrative Segmentation:** Rejects gradient transitions between sections. Instead, it utilizes sharp, flat cuts (White -> Navy -> White -> Blue) to clearly compartmentalize distinct chapters of the brand story (Hero -> Network -> Features -> Stats -> Call-to-Action).
* **Wide Clean Containers:** Generous whitespace framing central 3D imagery and data grids, preventing visual crowding.

#### Color & Texture
* **Systems Palette:** Slate black typography, light grey borders, system navy backgrounds, and a saturated cobalt blue for conversion points and gradient accents.
* **Material Precision:** Cards and dashboards rendered in native CSS/HTML with precise borders and subtle drop shadows (`box-shadow: 0 10px 30px rgba(0,0,0,0.05)`) instead of flat screenshots.

#### Motion & Restraint
* **Trust-Preserving Motion:** Focuses entirely on explanation rather than ornament. The motion vocabulary is limited to sticky sequencing, progressive text highlights, and clean content swaps.
* **The Living Mockup (setInterval Ticker):** The HTML-rendered product mockups on the right contain data fields (e.g. ETA timers, Bill of Lading codes) that dynamically randomize and update every 2 seconds via simple client-side JavaScript (`setInterval`). This simulates real-time activity and software vitality at zero performance cost.
* **CSS Scroll-Bound Parallax:** The bottom blue CTA section reveals itself using a zero-JS vertical parallax slide, driven natively via CSS `animation-timeline: scroll()` and `translateY` translations.

#### Typography
* **Disciplined Neo-Grotesque Display:** Neutral, highly technical sans-serif (Inter, SF Pro, or Roobert) with medium/bold contrasts, tight tracking, and gradient text fills (`-webkit-background-clip: text`) for high-tech statements.

---

### 3. The Human/AI Split

#### Human Assets (The "Credibility Layer" — 20-40%)
1. **Custom System Illustrations:** A futuristic 3D maritime port hero render, a vector route-network diagram, and an isometric port terminal footer graphic.
2. **HTML-Ready UI Mockups:** Polished, modular dashboard designs built as layout components so numbers and data states can be edited natively in code.
3. **Structured Content Grid:** A mapping document outlining the 4-6 feature cards, navigation labels, and specific ticker values for the sticky section.

#### AI Execution (The "Code Assembly" — 80-60%)
1. **Sticky Feature Orchestrator:** Coding the scroll-bound pin trigger that anchors the left menu while swapping the right-side cards based on viewport intersect.
2. **Active State Toggles:** Swapping class states (`text-black font-bold` vs `text-gray`) on navigation links dynamically.
3. **Mockup Ticker Scripting:** Writing the client-side JavaScript interval hooks to update numbers and indicators inside the mockups.
4. **CSS Parallax Reveal:** Implementing native scroll-timeline transform offsets for the final CTA block.

---

### 4. Gaps in Current System

Comparing the Nauta site to our active skills reveals the following gaps:

#### Gap A: Absence of the "Premium Product-Register Storytelling" Lane
* **The Gap:** [cinematic-motion/SKILL.md](../skills/cinematic-motion/SKILL.md) and [ui-ux/SKILL.md](../skills/ui-ux/SKILL.md) focus heavily on visual brand films, lacking a specific design guide for premium B2B SaaS.
* **Why it matters:** SaaS pages get over-designed with dramatic mask wipes and long scroll pins that damage professional trust.

#### Gap B: No "Living Mockup" Pattern
* **The Gap:** We do not instruct the developer to build interactive HTML/CSS cards containing local JavaScript update loops (`setInterval`) to simulate software vitality.
* **Why it matters:** Mockups remain static, making the product demo feel like a dead image.

#### Gap C: Missing "Hard-Cut Narrative Segmentation" Rules
* **The Gap:** No styling instructions for compartmentalizing layout stories via alternating solid background blocks (White -> Dark Navy -> White -> Accent) with zero gradient blends.
* **Why it matters:** Sections bleed into one another, diluting the narrative progression.

#### Gap D: No "Trust-Preserving Motion" Boundaries
* **The Gap:** Workflows do not restrict motion complexity on SaaS pages, allowing excessive parallax or layout displacement.
* **Why it matters:** Heavy animations slow down business users and feel gimmicky.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the "Enterprise Product Storytelling" pattern lane** to the UI/UX and Cinematic Motion skills, outlining rules for clean whitespace, hard-cut section transitions, and restrained typography.
* **Create the "Living Mockup" code blueprint** in Cinematic Motion Engineering (detailing targetable HTML numbers, loading pulse CSS, and setInterval state changes).
* **Define a "B2B SaaS Asset Pack" Checklist** during project inception:
  - Hero World Render.
  - Dark Network/Infrastructure Vector.
  - Interactive-ready HTML/CSS UI layouts.
  - Isometric CTA graphics.
* **Incorporate "Trust-Preserving Motion Rules"** (restricting animations to sticky tracks, fades, active swaps, and scroll-timeline parallax, banning decorative clip-path mask reveals on SaaS pages).
* **Add a preflight checklist question** to visual brainstorm workflows: *"What makes this product page feel alive without pretending to be a cinematic showcase?"*
* **Mandate the "Section Rhythm Plan"** mapping the narrative: Hero -> Network Scale -> Interactive Product Sticky -> Utility Statistics Grid -> Parallax CTA Reveal.
