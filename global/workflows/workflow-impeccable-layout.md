---
name: workflow-impeccable-layout
description: Impeccable UI/UX layout workflow
---

Assess and improve layout and spacing that feels monotonous, crowded, or structurally weak — turning generic arrangements into intentional, rhythmic compositions driven by psychology, time, and the LIFT system.

---

## Register

Brand: asymmetric compositions, fluid spacing with `clamp()`, intentional grid-breaking for emphasis. Rhythm through contrast — tight groupings paired with generous separations. Layout is eye choreography.

Product: predictable grids, consistent densities, familiar navigation patterns. Responsive behavior is structural (collapse sidebar, responsive table), not fluid typography. Consistency IS an affordance.

---

## Assess Current Layout (The LIFT System)

Evaluate the spatial design not just structurally, but psychologically:

1. **Leverage Points (Focal Anchors)**:
   - What is the *single most important thing*? Is it dominating via scale, contrast, positioning, or isolation?
   - Are there competing elements fighting for leverage? (If everything is bold, nothing is).

2. **Internal Rhythm (Eye Choreography)**:
   - Does the eye flow naturally from the leverage point to secondary information?
   - Is spacing predictable enough to build trust and relax the brain?

3. **Friction & Flow**:
   - *Bad Friction*: Clutter, unwanted noise, tight spaces where they shouldn't be, competing focal points.
   - *Good Friction*: Intentional disruptions (asymmetry, rotated elements, grid-breaking overlaps) that force the eye to pause and re-engage.
   - *Flow*: Smooth, scannable reading paths with clear boundaries.

4. **Temporal Flow (Time-Based Journey)**:
   - Does the layout control *how long* the eye lingers?
   - **Punch (Impact)**: Fast hit, bold headline, full-bleed visual.
   - **Slow (Linger)**: Layered details, finer typography, secondary paths to explore.
   - **Release (Pool)**: Vast open whitespace for the eye to rest and process.

5. **Density & Grids**:
   - Is the layout too cramped or too sparse?
   - Is it a monotonous 12-column or identical card grid everywhere?
   - Does it use grids dynamically (e.g., asymmetric grids, elements spanning multiple columns)?

**CRITICAL**: Space is a design material. Layout is not just where things sit; it is *when* the user sees them.

## Plan & Improve Systematically

### 1. Establish the LIFT Foundation

- **Isolate the Leverage Point**: Push back anything that competes with the primary focal point.
- **Map the Eye Journey**: Define the path the eye should take. Guide it using consistent margins and gutters.

### 2. Choreograph Temporal Flow

- **Pacing**: Alternate between fast beats (bold, large imagery) and slow beats (detailed text, specs, exploration paths).
- **Pools of Space**: Add generous vertical padding (`96px-160px`) between major sections to act as "release" pools for the brain.

### 3. Master Grids & Break Them

- **Versatility**: Grids aren't just for rows of cards. Use them for typography alignment, hero layouts, and overlapping elements.
- **Asymmetric Grids**: Let hero elements take up more space to naturally draw attention, leaving smaller columns for secondary flow.
- **Break the Rules**: Have 90% of your design adhere to the grid, but intentionally break one element out of it (e.g., an overlapping image or floating CTA) to create contrast and "Good Friction."

### 4. Create Structural Rhythm

- **Tight grouping**: 8-12px between related siblings.
- **Generous separation**: 48-96px between distinct sections.
- **Fluid spacing**: Apply `clamp()` for spacing that breathes naturally across screen sizes without hard breakpoints.

### 5. Choose the Right Structural Tool

- **Use Flexbox for 1D layouts**: Rows, nav bars, button groups.
- **Use Grid for 2D layouts**: Page-level structure, asymmetric compositions.
- **Don't default to Grid** when Flexbox with `flex-wrap` is simpler.

### 6. Break Card Monotony

- Don't default to identical card grids for everything.
- Mix module sizes (e.g., span a featured card across two columns) to create visual interest.
- Never nest cards inside cards — use spacing and dividers for internal hierarchy.

### 7. Manage Depth & Elevation

- Build a consistent shadow scale (sm → md → lg → xl) — shadows should be subtle.
- Use elevation to reinforce hierarchy, not as mere decoration.

**NEVER**:
- Make all spacing equal — variety creates hierarchy and tempo.
- Use arbitrary spacing values outside your scale.
- Wrap everything in cards — not everything needs a container.
- Center everything blindly — left-aligned with asymmetry often feels far more premium and intentional.
- Ignore transferability — if it only looks good at exactly 1440px width, it's broken.

## Verify Layout Improvements

- **The Squint Test**: With blurred vision, is the Leverage Point still obvious?
- **The Rhythm Check**: Does the page have a satisfying beat of tight groupings and generous release pools?
- **The Friction Check**: Is the eye pausing at the right moments, or just getting confused by clutter?
- **Responsiveness (Transferability)**: Does the hierarchy survive when shrunk to a mobile screen?

Remember: Space is the most underused design tool. A layout with the right rhythm, friction, and temporal flow transforms a generic page into an unforgettable experience.

## Live-mode signature params

Each variant MUST declare a `density` param. Drive all spacing tokens in the variant's scoped CSS through `calc(var(--p-density, 1) * <base>)` — paddings, gaps, column widths. Users slide from airy to packed and see layout re-breathe with no regeneration.

```json
{"id":"density","kind":"range","min":0.6,"max":1.4,"step":0.05,"default":1,"label":"Density"}
```

For variants whose topology genuinely changes (stacked vs. side-by-side, grid vs. bento), use a `steps` param whose scoped CSS branches via `:scope[data-p-structure="X"]`. One structure param + one density param is a powerful combo; resist adding a third.

```json
{"id":"structure","kind":"steps","default":"grid","label":"Structure","options":[
  {"value":"stacked","label":"Stacked"},
  {"value":"grid","label":"Grid"},
  {"value":"bento","label":"Bento"}
]}
```

See `reference/live.md` for the full params contract.
