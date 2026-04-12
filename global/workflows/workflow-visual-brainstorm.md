# WORKFLOW: VISUAL BRAINSTORMING

**Version:** Gold v1.0
**Layer:** 8 — Execution Workflow
**Tier:** 2 — Loaded by task
**File:** workflows/workflow-visual-brainstorm.md
**Purpose:** The systematic sequence for generating visual design previews
          and design briefs during brainstorming and project inception —
          making design direction visible before implementation begins.
**Loaded When:** Starting a new UI project, defining visual identity,
              choosing between design directions, or preparing mockups.
**Inherits From:** execution-workflow.md (8-phase universal process)
**Note:** This workflow bridges the gap between text-based design decisions
       and actual visual output. It uses two paths: direct HTML previews
       (fast, built-in) and Google Stitch briefs (high-fidelity, external).

---

## WHAT THIS WORKFLOW DOES

This workflow produces visual artifacts that help the user SEE design
decisions before committing to implementation. It prevents the most
expensive mistake in UI development: building something that looks
different from what the user imagined.

The output of this workflow is:
1. A visual preview of the design direction (HTML file or Stitch mockup)
2. Confirmed design tokens (colors, fonts, spacing) written to context files
3. A clear "this is what we're building" visual reference

---

## ACTIVATION

### Use When

- "I want to see what this will look like before we build it"
- "Let's figure out the visual direction"
- Phase 3A of workflow-project-inception (Visual Identity)
- "Show me some color options / layout options / typography options"
- "I want to mockup this in Stitch"
- "Prepare a design brief for me"
- Designing the first screen of a new application

### Do NOT Use When

- The visual identity is already locked and you're building production UI → use `workflow-design-ui.md`
- You're debugging or fixing an existing UI → use `workflow-debug-issue.md`
- The product has no user interface (CLI tools, pure backends)

---

## REQUIRED FILES

### Skills to Load

| Priority | Skill | Why |
| :--- | :--- | :--- |
| Primary | `visual-brainstorming` | Core skill — preview generation and Stitch brief format |
| Secondary | `skill-ui-ux` | Design principles that inform visual direction |
| Conditional | `skill-product-thinking` | If visual direction needs to align with user/business goals |

### Context Files to Load

| Context | When |
| :--- | :--- |
| `visual-identity.md` | If it exists (read existing direction before generating previews) |
| `design-system.md` | If it exists (ensure consistency with established patterns) |
| `stack-context.md` | If generating Path A previews (know what CSS framework is in use) |

---

### MANDATORY STOP-AND-VERIFY GATE
> **[CONTEXT AMNESIA FAILSAFE]**
> Do NOT proceed to Step 1 until you have verified in your `<thought_process>` that all required context files and skill files have been read using tool calls. You must state: "I have read X, Y, Z files and I am ready to begin."

## EXECUTION SEQUENCE

### PHASE 1: UNDERSTAND THE VISUAL NEED (5 minutes)

#### Mode: Designer (Discovery)

Before generating anything, clarify:

1. **What needs visualization?**
   - Color palette only → Path A (quick HTML)
   - Typography comparison → Path A (quick HTML)
   - Full page layout → Path B (Stitch brief) or Path A (wireframe)
   - Complete design direction → Both paths sequentially

2. **Is there existing visual context?**
   - Check for `contexts/visual-identity.md`
   - Check for `contexts/design-system.md`
   - Ask: "Are there reference products that capture your desired look?"

3. **What's the decision to make?**
   - "Light or dark?" — Show both
   - "This layout or that layout?" — Show both
   - "What colors?" — Show 2-3 palette options

**Gate:** Do NOT generate a preview until the question being answered is clear.

---

### PHASE 2: CHOOSE THE PATH (2 minutes)

Present the two options:

**Path A — HTML Preview (I generate it now, you see it in 60 seconds):**
Best for: quick color/typography/spacing decisions, simple layout wireframes.

**Path B — Google Stitch Brief (I prepare the brief, you run it in Stitch):**
Best for: full page mockups, complex layouts, production-quality visual fidelity.

Recommend one. Let the user decide.

**Gate:** Path is explicitly chosen before generation begins.

---

### PHASE 3A: EXECUTE — HTML PREVIEW PATH (10-15 minutes)

#### Mode: Builder (Preview Generation)

1. **Plan the preview sections** — List what the HTML file will contain
2. **Generate the HTML** — Single self-contained file:
   - Inline CSS (no external stylesheets)
   - Google Fonts via `@import` in `<style>` block
   - No JavaScript unless needed for interactive comparison
   - Dark background by default (most products target dark mode)
   - Responsive layout
   - Clear section labels explaining what each area shows
3. **Save the file** — Save to conversation artifacts directory
4. **Open in browser** — Use browser subagent to navigate to the file
5. **Capture and present** — Take a screenshot for discussion

#### Iteration Loop

After presenting:
- Ask: "What would you change? Colors, typography, layout, spacing?"
- Apply the requested changes
- Regenerate and re-present
- Repeat until the user says "looks good"

**Gate:** User explicitly approves the visual direction.

---

### PHASE 3B: EXECUTE — STITCH BRIEF PATH (10-15 minutes)

#### Mode: Designer (Brief Preparation)

1. **Gather all inputs**:
   - Visual mood (3-5 adjectives)
   - Reference products (2-3 with specific things to borrow)
   - Anti-references (what it should NOT look like)
   - Layout structure
   - Components needed
   - Color direction (even approximate)
   - Typography preferences

2. **Generate the design brief** using the template from the SKILL.md

3. **Include context files**:
   - If `visual-identity.md` exists, include relevant sections
   - If `design-system.md` exists, include component patterns

4. **Present to user**:
   "Here's your Stitch brief. Steps:
   1. Go to stitch.google.com
   2. Paste this brief as your prompt
   3. Optionally attach the visual-identity.md file for more context
   4. Iterate in Stitch until you're happy
   5. Come back here and tell me 'I'm done with Stitch' — I'll extract the design tokens"

5. **Wait for return** — When the user comes back with approved Stitch output, proceed to Phase 4

**Gate:** User returns from Stitch with an approved direction.

---

### PHASE 4: LOCK THE DESIGN DIRECTION (5 minutes)

#### Mode: Architect (Decision Capture)

Regardless of which path was used:

1. **Extract design tokens**:
   - Background colors (CSS custom properties)
   - Text colors (primary, secondary, muted)
   - Accent/brand color
   - Feedback colors (success, warning, error)
   - Font families (headline, body, mono)
   - Type scale (sizes for headings, body, caption)
   - Spacing base unit
   - Border radius tokens
   - Shadow/elevation tokens

2. **Write to context**:
   - Create or update `contexts/visual-identity.md` with all design tokens
   - If a design system exists, verify consistency

3. **State the decision clearly**:
   "Visual direction locked: [1-2 sentence summary]. All tokens written to visual-identity.md."

---

### PHASE 5: HAND OFF (2 minutes)

#### Mode: Communicate

Transition to the next phase:
- If during project inception → return to Phase 3 (Architecture) of workflow-project-inception
- If standalone design session → summarize decisions and suggest next workflow (workflow-design-ui or workflow-build-feature)

---

## QUALITY GATES

- **G1 (Clarity):** No preview generated without a clear question to answer
- **G2 (Path):** Path A or B explicitly chosen — not assumed
- **G3 (Approval):** User explicitly approves the visual direction before tokens are exported
- **G4 (Export):** Design tokens written to `contexts/visual-identity.md` — not left only in the preview

---

## ANTI-PATTERNS THIS WORKFLOW PREVENTS

| Anti-Pattern | How This Workflow Prevents It |
| :--- | :--- |
| "Build it and I'll tell you if I like it" | Visual preview shown before any production code |
| Describing colors in text | Path A renders actual color swatches |
| Generic Stitch prompts producing generic mockups | Path B generates detailed, specific design briefs |
| Design decisions lost after brainstorming | Phase 4 exports everything to context files |
| Spending 2 hours on a mockup that should take 5 minutes | Path A is designed for 60-second previews |
