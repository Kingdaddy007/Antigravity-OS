# Audit Report: Site 19 — NomadaToast (Creative Agency Bait-and-Switch)

### 1. Site Identity & Target Impression
* **Core Vibe:** Surreal Disruption, Technical Boldness, Confrontational Hook, and Structured Credibility.
* **Audience:** Clients, brands, and agencies seeking high-impact 3D design, motion authority, and experimental visual taste.
* **Overall Aesthetic:** Stark monochromatic black-and-white UI, high-fidelity photorealistic human head render, mutating particle explosion with an amber core, and sharp, boxy card structures.

---

### 2. Design & Animation DNA

#### Composition & Layout
* **Surreal-to-Commercial Transition:** Splitting the page into a high-intensity pinned canvas entry (manifesto/hook), a clean middle section (straightforward partner grids and case logos), and a closing composite layout where DOM panels slide over the 3D canvas background.
* **Asymmetrical Hero Split:** Tightly leaded typography blocks on the left, with the interactive 3D canvas occupying the right.
* **3D-over-DOM Compositing:** Overlapping scrolling testimonial and social UI cards slide vertically over the desaturated, pinned 3D particle background, adding deep layering without creating layout noise.

#### Color & Texture
* **Monochrome UI Framing:** Pure white (`#ffffff`), light gray (`#f5f5f5`), and solid black (`#000000`).
* **Luminous Ember Core:** A bright orange/amber core inside the exploding particle mesh, providing a single chromatic highlight.
* **Material Disruption:** Contrast between the smooth organic texture of human skin and the sharp, granular particles of the exploded swarm.

#### Motion & Restraint
* **Recognition-to-Rupture Hook:** The page begins with an organic, cursor-tracking human head. Scrolling triggers a sudden, violent morph where the face shatters into a swirling particle field.
* **Shock-to-Proof Narrative Pacing:**
  1. High-Intensity: Surreal 3D morph hook.
  2. Quiet/Grounded: Flat partner marquee and grid.
  3. Controlled Return: Pinned 3D scene playing behind scrollable overlay cards.
* **Snappy Hard-Cut Text Swaps:** Rejects smooth opacity fades for instant, digital typographic state changes (`duration: 0.1`) that snap in sync with scroll thresholds, giving the interface a mechanical, high-velocity feel.

---

### 3. The Human/AI Split

#### Human Assets (The "20-40%")
1. **Semantic Shock Assets:** A photorealistic human head model and the corresponding face-to-particle morph simulation frames (pre-rendered in Houdini or Cinema4D).
2. **Coherent Branding UI Kit:** Utilitarian vector partner logos, typography system assets, and testimonial card content.
3. **Frame-to-Text Storyboard:** A mapping document matching specific frame indexes of the 3D sequence to instant text hard-cuts.

#### AI Execution (The "80-60%")
1. **Canvas Transition Player:** Implementing the canvas rendering loop, managing frame changes and cursor-tracking coordinates.
2. **GSAP ScrollTrigger Sequence Timeline:** Mapping the morph sequence to scroll progress, triggering hard-cuts on typography blocks.
3. **Overlapping DOM Card Stacks:** Building the CSS stacking context and scrolling offsets that allow white cards to slide cleanly over the background WebGL canvas.

---

### 4. Gaps in Current System

Comparing the NomadaToast site to our active skills reveals the following gaps:

#### Gap A: Absence of the "Surreal Mutation Hook" Pattern
* **The Gap:** [cinematic-motion/SKILL.md](../skills/cinematic-motion/SKILL.md) covers standard 3D displays but lacks guidelines for **Surreal Mutation Hooks** (using a recognizable object that shatters into abstraction as a psychological bait-and-switch).
* **Why it matters:** The model defaults to decorative 3D scenes that lack narrative force and surprise.

#### Gap B: No "Shock-to-Proof" Narrative Layout Spec
* **The Gap:** We lack a sequence standard that guides the developer on how to transition from high-intensity canvas entries, to flat credibility blocks, and back to background-layered canvas cards.
* **Why it matters:** The model carries complex WebGL performance drag through standard portfolio grids, causing mobile lag.

#### Gap C: Missing "Hard-Cut Copy States" Rules
* **The Gap:** Our typography and motion guidelines always recommend smooth, eased fades.
* **Why it matters:** Fades look sluggish and outdated on tech-creative agency sites that require razor-sharp, instant text swaps.

#### Gap D: Lack of "3D Background + DOM Card Overlay" Compositing Guidelines
* **The Gap:** No specific rules for value reduction, card width constraints, desaturating background canvases, and maintaining contrast behind scrolling DOM text panels.
* **Why it matters:** Foreground typography collapses into the chaotic background 3D colors, rendering text unreadable.

#### Gap E: Missing "WebGL vs. Canvas Sequence" Decision Gate
* **The Gap:** Workflows do not force deciding between real-time R3F rendering and pre-rendered canvas sequences at inception.

---

### 5. Upgrade Specifications

We will compile these specifications:
* **Add the "Surreal Mutation Hook" pattern** to Cinematic Motion, detailing the contrast between recognizable assets and abstract mutations.
* **Create the "Shock-to-Proof" narrative template** (High-intensity entry -> flat grid proof -> composite return with 3D background).
* **Formulate "Hard-Cut Copy States" rules** in Cinematic Motion Engineering (using instant `duration: 0.1` text swaps linked to scroll percentages).
* **Write "3D Background + DOM Card Overlay" compositing rules**:
  - Require background desaturation or 50% opacity value reduction when cards overlap.
  - Limit scrolling card width to 30% of the viewport to keep the 3D scene visible on the side.
  - Force backdrop-blur filters (`backdrop-filter: blur(12px)`) on card backgrounds to preserve text contrast.
* **Introduce a "Sequence vs. WebGL" decision gate** in workflows, outlining asset pipeline, performance budgets, and fallback paths for both.
* **Mandate semantic hook object details** (starting state, ending state, brand narrative role) inside the project inception plans.
