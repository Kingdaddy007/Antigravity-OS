---
name: VISUAL BRAINSTORMING & DESIGN PREVIEW
description: Domain knowledge for VISUAL BRAINSTORMING & DESIGN PREVIEW — generating live visual mockups and design briefs during brainstorming and project inception.
---

# SKILL: VISUAL BRAINSTORMING & DESIGN PREVIEW

**Version:** Gold v1.0

**Type:** Specialized Skill Domain

**Tier:** 2 — Loaded by task (when Designer Mode is active during brainstorming/inception)

**File:** skills/visual-brainstorming/SKILL.md

**Inherits From:** anti-gravity-core.md, system-thinking.md

**Primary Mode:** Designer

**Secondary Modes:** Architect (structural decisions), Builder (HTML preview generation)

**Purpose:** Governs how Anti-Gravity produces visual design artifacts during the brainstorming and inception phases — before any production code is written. Offers two execution paths: direct HTML preview generation and Google Stitch design brief preparation.

---

## MINDSET

Design decisions made in text are abstract. Abstract decisions lead to misaligned expectations — the user imagines one thing, the AI builds another, and the gap is discovered only after hours of implementation.

The expert visual brainstormer solves this by making design direction **visible** as early as possible. The cheapest time to change a design is before a single line of production code exists. A 5-minute HTML preview or a well-crafted Stitch prompt can save hours of rework.

This skill is NOT about building production UI. It is about generating disposable visual artifacts that accelerate decision-making: "Do you want THIS or THAT?" — shown, not described.

---

## ACTIVATION TRIGGERS

### When to Load This Skill

- Starting a new project with a user interface (workflow-project-inception Phase 3A)
- Designing the visual identity of a product (colors, typography, layout direction)
- The user asks to "see" a layout, design, or component before building it
- Deciding between visual approaches (dark vs light, sidebar vs top-nav, etc.)
- Before committing to a design system or visual direction
- The user mentions Google Stitch, mockups, wireframes, or design previews

### Red Flags That This Skill Is Being Neglected

- Production frontend code is being written without any visual preview or design direction
- Color palettes and typography are being chosen in text without visual comparison
- Layout decisions are described in prose but never rendered
- The user says "that's not what I imagined" after seeing the built UI
- Complex UI is being designed purely from component descriptions

### Usually Pairs With

- `skill-ui-ux.md` — For the design principles that inform the visual direction
- `skill-product-thinking.md` — For understanding the user and the Job-to-be-Done
- `skill-coding.md` — When transitioning from preview to production implementation

---

## OBJECTIVES

When this skill is active, the goal is to:

1. **Make the invisible visible** — Render design decisions as viewable artifacts before implementation
2. **Accelerate alignment** — Reduce "that's not what I meant" moments to near zero
3. **Enable comparison** — Show options side-by-side so the user can choose with confidence
4. **Create reusable direction** — Output design tokens, color values, and patterns that feed directly into implementation
5. **Bridge to tools** — Generate design briefs that work with external tools like Google Stitch

---

## THE TWO PATHS

This skill offers two execution paths based on the situation. Anti-Gravity should recommend the appropriate path, but the user decides.

### Path A: Direct HTML Preview (Quick & Built-In)

### When to use

- Quick visual comparisons (color palettes, typography, spacing)
- Simple layout decisions (sidebar vs top-nav, grid arrangements)
- Design token previews (seeing CSS custom properties rendered live)
- The user wants to iterate fast without leaving the IDE

### What it produces

- A single self-contained HTML file with inline CSS
- Saved to the conversation artifacts directory
- Opened in the browser for immediate viewing
- Disposable — not production code, not kept after the session

### Quality bar

- The preview must look polished enough to evaluate design direction — not pixel-perfect, but not ugly
- Must render correctly in a modern browser
- Must be a single file (no external dependencies, no CDN links)
- All fonts loaded from Google Fonts via `@import` or embedded
- Must include a title describing what's being previewed
- Dark background if the product direction is dark mode

### Path B: Google Stitch Design Brief (High-Fidelity Mockups)

### When to use

- Full page layouts with multiple components
- Complex UI patterns (dashboards, data tables, multi-step forms)
- The user wants production-quality visual fidelity before building
- Exploring multiple design directions simultaneously
- The user's visual identity context file already exists and should be referenced

### What it produces

- A structured design brief document that the user takes to Google Stitch (stitch.google.com)
- The brief includes: visual direction, component requirements, layout structure, color tokens, typography choices, mood references, and anti-references
- Optionally, a copy of the relevant design context files formatted for Stitch input

### Design Brief Structure

```markdown

# Design Brief: [Screen/Component Name]

## Visual Direction

- **Mood:** [e.g., "Premium, dark, data-dense like Bloomberg terminal"]
- **References:** [2-3 products/sites to draw from, with WHAT to borrow]
- **Anti-references:** [What it should NOT look like]

## Layout Structure

- [Description of layout: sidebar + main, full-width, split-panel, etc.]
- [Primary content area purpose]
- [Secondary/navigation area purpose]

## Components Needed

1. [Component] — [purpose, states, key interactions]
2. [Component] — [purpose, states, key interactions]
3. [Component] — [purpose, states, key interactions]

## Color Palette

- Background: [hex values]
- Text: [hex values]
- Accent: [hex values]
- Feedback: [success/warning/error hex values]

## Typography

- Headlines: [font family, weight]
- Body: [font family, weight]
- Data/Mono: [font family, weight]

## Specific Requirements

- [Any constraints, responsive needs, accessibility notes]

## Context Files to Attach

- visual-identity.md (if exists)
- design-system.md (if exists)

```

---

## DECISION FRAMEWORK

### Choosing Between Path A and Path B

| Signal | Path A (HTML Preview) | Path B (Stitch Brief) |
| :--- | :--- | :--- |
| Need to see color options | ✅ Best choice | Overkill |
| Need to see typography | ✅ Best choice | Overkill |
| Need to see a full page layout | ⚠️ Acceptable but limited | ✅ Best choice |
| Need to compare 2-3 design directions | ✅ Quick and effective | ✅ Also good, but slower |
| Need production-quality mockup | ❌ Not the right tool | ✅ Best choice |
| Time pressure (need to decide NOW) | ✅ Fastest option | ❌ Requires external tool |
| Complex dashboard or data-heavy UI | ⚠️ Will look rough | ✅ Stitch excels here |

### When to Suggest BOTH

If the user is at Phase 3A of project inception (Visual Identity), suggest:

1. **Path A first** — Generate a quick HTML preview of color palette + typography + basic component patterns
2. **Path B second** — Once the visual direction is locked, generate a Stitch brief for the first major screen layout

---

## BEHAVIORAL WORKFLOW

### Step 1: Clarify What Needs Visualization

Before generating anything, ask:

- What are we trying to decide? (color direction, layout, component patterns, full page?)
- Is there an existing visual-identity.md or design-system.md to build from?
- Are there reference products or sites that capture the desired aesthetic?

### Step 2: Choose the Path

Based on the answers, recommend Path A or Path B. Explain the tradeoff in one sentence. Let the user decide.

### Step 3A: Execute Path A (HTML Preview)

1. **Design the preview** — Plan what sections the HTML file will contain
2. **Generate the HTML** — Single self-contained file with inline CSS, Google Fonts, and no external dependencies
3. **Save to artifacts** — Save to the conversation artifacts directory
4. **Open in browser** — Use the browser tool to render and display
5. **Iterate** — Ask for specific feedback: "What do you want to change? Colors? Typography? Layout? Spacing?"
6. **Lock decisions** — When the user approves, extract the design tokens (colors, fonts, spacing) and write them to `contexts/visual-identity.md`

### Step 3B: Execute Path B (Stitch Brief)

1. **Gather inputs** — Collect visual direction, layout requirements, component needs
2. **Generate the brief** — Using the Design Brief Structure defined above
3. **Include context files** — Attach visual-identity.md, design-system.md, or any relevant context
4. **Present to user** — "Here's your Stitch brief. Copy this into Google Stitch and iterate there. When you're happy with the result, come back and we'll extract the design tokens."
5. **Post-Stitch** — When the user returns with the approved direction, help extract design tokens and update `contexts/visual-identity.md`

### Step 4: Export Design Decisions

Regardless of which path was used, the final output should include:

- Updated `contexts/visual-identity.md` with concrete CSS custom properties
- A clear design direction statement (1-2 sentences)
- Any component patterns that were decided during the preview

---

## HTML PREVIEW TEMPLATES

### Color Palette Preview

When generating a color palette preview, include:

- Background swatches (large blocks showing surface colors)
- Text on background (readability check)
- Accent color applications (buttons, links, hover states)
- Feedback colors (success, warning, error — small badges)
- Dark/light mode comparison if applicable

### Typography Preview

When generating a typography preview, include:

- Headline hierarchy (H1 through H3 at minimum)
- Body text paragraph with real content (not lorem ipsum — use product-relevant text)
- Label and caption sizes
- Monospace/code font (if relevant to the product)
- Line height and letter spacing visible

### Layout Preview

When generating a layout preview, include:

- A simple wireframe showing content zones (header, sidebar, main, footer)
- Labeled regions ("Navigation", "Primary Content", "Data Panel")
- Approximate proportions (use CSS grid or flexbox)
- Responsive behavior indication (optional)

### Component Pattern Preview

When generating component previews, include:

- Primary button + hover state
- Secondary/ghost button
- Card component with title, content, and action
- Input field with label and focus indication
- A small data table or list (if relevant)

---

## ANTI-PATTERNS

### Designing in Text When Visuals Would Settle It Faster

**What it looks like:** Writing three paragraphs describing a color palette instead of showing it.
**Why it is harmful:** Text descriptions of visual properties are inherently ambiguous. "Warm dark gray" means different things to different people.
**What to do instead:** Generate an HTML preview. 30 seconds to render beats 5 minutes of description.

### Over-Engineering the Preview

**What it looks like:** Building a multi-page interactive prototype during the brainstorming phase.
**Why it is harmful:** The preview is a decision tool, not a deliverable. Over-investing in it wastes time that should go to implementation.
**What to do instead:** Keep previews minimal. One HTML file. Inline styles. No JavaScript unless needed for interaction.

### Skipping the Visual Step Entirely

**What it looks like:** Going straight from text-based visual identity (Phase 3A) to building production components.
**Why it is harmful:** The first time the user sees the actual visual direction is in the real app. If they don't like it, hours of work are wasted.
**What to do instead:** Always offer a preview. Even a 2-minute Path A preview is better than zero visual validation.

### Generating Stitch Briefs Without Context

**What it looks like:** Writing vague briefs like "Make a dark dashboard with charts."
**Why it is harmful:** Stitch will produce generic output. The brief should be specific enough that the mockup comes back usable.
**What to do instead:** Include color hex values, font names, layout structure, component list, and at least 2 reference products.

---

## NON-NEGOTIABLE CHECKLIST

- [ ] The user's visual direction has been clarified before any preview is generated
- [ ] Path A or Path B has been explicitly chosen (not assumed)
- [ ] HTML previews are self-contained with no external dependencies (except Google Fonts)
- [ ] Stitch briefs include specific color values, font names, and layout structure — not vague descriptions
- [ ] Design decisions are exported to `contexts/visual-identity.md` after approval
- [ ] The preview is treated as disposable — it is NOT production code

---

## FILE RELATIONSHIPS

| Related File | Relationship |
| :--- | :--- |
| `skill-ui-ux.md` | Provides the design principles (cognitive load, state coverage, accessibility) that inform the visual direction |
| `skill-product-thinking.md` | Provides the Job-to-be-Done and user context that should influence the visual approach |
| `workflow-project-inception.md` | Phase 3A (Visual Identity) is the primary integration point for this skill |
| `workflow-design-ui.md` | This skill feeds into the UI design workflow — visual direction is decided here, implemented there |
| `contexts/visual-identity.md` | This is the output target — design tokens and visual direction are written here |
| `contexts/design-system.md` | If an existing design system exists, this skill reads it to ensure preview consistency |

---

## AUTHORITY

If any other file in this system appears to contradict this file on **how visual brainstorming and design previews should be produced**, this file is authoritative unless a project-level override is explicitly documented.
