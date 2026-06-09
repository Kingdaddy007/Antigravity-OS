# Audit Report: Site 02 — Montfort (Corporate Atmospheric Fly-Through)

### 1. Site Identity & Target Impression
* **Core Vibe:** Institutional Gravitas, Global Scale, Environmental Authority, and Structural Discipline.
* **Audience:** Investors, enterprise partners, regulators, and high-value stakeholders who require trust, reach, and capability before reading granular details.
* **Overall Aesthetic:** Cool, desaturated tones, vast outdoor landscapes, layered weather/fog effects, and restrained typographic styling.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Z-Axis Camera Move:** The layout mimics a camera pushing forward into space along the Z-axis, moving through clouds into maritime ocean views, then high altitude, before landing in a structured layout.
* **Myth-to-Governance Shift:** It starts center-aligned and highly cinematic (visual myth-making), then shifts to asymmetrical grids for compliance data and a clean white corporate footer.
* **Typography Hierarchy:** Extremely sparse. Short copy blocks and large display headings are subordinated to the massive backdrops.

#### Color & Texture
* **Elemental Palette:** Ice whites, cool greys, deep sea navy (`#0a1118`), and strategic organic greens reserved solely for ESG (Environmental, Social, and Governance) sections.
* **Atmospheric Texturing:** Cloud, mist, fog, and light-ray overlays are used as structural textures, avoiding plain CSS backgrounds.

#### Motion & Restraint
* **Diegetic Transitions:** The site uses the physical elements of its world (drifting fog, cloud layers, water glare) to wipe the screen. Scaling a transparent cloud image past the camera acts as a natural cover to swap the background footage behind it.
* **Pacing & Weight:** Animations are slow, heavy, and drift naturally without snapping, bouncing, or sudden spring movements.
* **Typographic Restraint:** Copy only fades in once the background environment is fully established, preventing visual competition between text and motion.

---

### 3. The Human/AI Split

#### Human Assets (The "20%")
1. **Curated & Graded Video Plate Set:** High-resolution looping background videos (mountain peak, tracking shot of cargo ship, stratosphere, ESG underwater rays) that share a consistent visual grading (contrast, noise, color temperature).
2. **Diegetic Overlay Plates:** Transparent high-resolution cloud/fog PNG or WebP images large enough to scale 10x without pixelation.
3. **World Progression Script:** A conceptual storyboard mapping thematic progression (Descent → Emergence → Expansion → Governance → Stewardship).

#### AI Execution (The "80%")
1. **Z-Axis Timeline Orchestration:** Setting up the GSAP ScrollTrigger timeline to scale and fade layered transparent cloud assets synchronously.
2. **Video Loader & Crossfader:** Scripting the crossfades between background `<video>` elements and implementing proximity/lazy-loading to protect page load performance.
3. **Structured Responsive Fallbacks:** Creating alternative CSS reveal cascades for mobile/low-bandwidth clients when pinned sequences are deactivated.

---

### 4. Gaps in Current System

Comparing the Montfort system to our active skills reveals the following gaps:

#### Gap A: Lack of an "Atmospheric Fly-Through" Subtype
* **The Gap:** [cinematic-motion/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/cinematic-motion/SKILL.md) lacks layout/motion instructions for **Z-axis progression**. It defaults to standard scroll reveals (parallax, sticky, masks, or bento grids) rather than camera-depth staging.
* **Why it matters:** The assistant cannot build immersive spatial depth (Z-axis scale/opacity overlapping) because it treats scroll strictly as a Y-axis movement.

#### Gap B: Absence of Diegetic Wipes
* **The Gap:** We don't define **diegetic transition wipes** (using transparent elements native to the brand's world like cloud, smoke, glare, shadow, or water) to mask background shifts.
* **Why it matters:** The model uses generic CSS page wipes or simple opacity fades, which makes transitions look digital and generic rather than authored and cinematic.

#### Gap C: Missing Media Grading & Visual Progression Requirements
* **The Gap:** Our workflows don't instruct the model to verify visual grading consistency across stock assets.
* **Why it matters:** If the user provides a warm-toned sunny video and a cool-toned mountain peak, the assistant will implement them side-by-side, breaking the immersive illusion.

#### Gap D: Missing Restraint Rules for Moving Footage
* **The Gap:** [ui-ux/SKILL.md](file:///C:/Users/godsw/.gemini/config/skills/ui-ux/SKILL.md) doesn't warn that copy must stay sparse and delay its entry when overlaid on heavy background videos, leading to cluttered, unreadable screens.

---

### 5. Upgrade Specifications

We will compile these for our final upgrade plan. Key specifications:
* **Add "Z-Axis Fly-Through" boilerplate** to Cinematic Motion.
* **Incorporate "Diegetic Transition" guidelines** (cloud/fog scale-outs).
* **Require a "World Progression Map"** in visual brainstorming.
* **Establish typographic timing rules** on moving footage (delay copy fades relative to background stabilization).
