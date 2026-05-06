---
name: UI/UX & DESIGN THINKING
description: >
  Use this skill when designing or evaluating user interfaces, user flows,
  or frontend experiences. Activated when designing a new screen, component,
  or user flow; writing frontend implementation code (React, Vue, HTML/CSS);
  defining how an application handles loading, error, or empty states;
  restructuring navigation or information architecture; evaluating
  accessibility; or deciding how a backend error should be communicated to
  the user. Also activated when writing or reviewing any CSS, choosing fonts,
  picking colors, defining motion, or building responsive layouts. Examples:
  "design this flow", "how should this form work?", "what should the empty
  state look like?", "the UI is confusing", "make this more user-friendly",
  "write the frontend for X", "build this page", "make this look better".
  Do NOT use for pure backend implementation (use coding skill) or
  architecture decisions (use architecture skill).
---

# UI/UX & DESIGN THINKING

Unified design intelligence. Covers UX foundations, visual craft, motion, accessibility, and execution standards. This skill activates automatically on every frontend task — you do not need to invoke it explicitly.

For structured deep-dives (formal audits, critiques, polish passes), use the `/workflow-impeccable-*` workflows. This skill provides the passive intelligence that runs underneath.

---

## LAYER 1: UX FOUNDATIONS

### Mindset

UX is the systematic reduction of cognitive load. The interface is a deterministic state machine that guides the user safely from point A to point B. Users scan, not read. Users make mistakes; the system prevents them when possible and forgives them when they happen.

Think in:
- **Flows**, not isolated screens
- **States**, not just the default state
- **Behavior**, not just layout
- **User goals**, not only stakeholder requests
- **Clarity** over cleverness

### The 10 UX Lenses

Apply all ten before and during design or review:

1. **User Goal Clarity** — What is the user trying to accomplish? Is the primary task obvious?
2. **Information Hierarchy** — What should users notice first? Are the most important actions visually clear?
3. **Flow Logic** — Is the path obvious? Are there unnecessary steps or dead ends?
4. **Cognitive Load** — How much must the user remember or decide at once? Can choices be simplified?
5. **State Visibility** — Does the user know what the system is doing? Are loading/error/empty states explicit?
6. **Interaction Safety** — Can the user undo mistakes? Are destructive actions protected?
7. **Consistency** — Does the screen follow established patterns? Is a new pattern introduced without reason?
8. **Accessibility** — Keyboard reachable? Contrast adequate? Labels present? Touch targets 44px+?
9. **Performance Perception** — Does it feel responsive? Are delays acknowledged?
10. **Implementation Realism** — Are UX gains proportional to implementation cost?

### The 6 UI States

Do not design only the Happy Path. Every screen must define:

1. **Ideal** — Data present, looks perfect
2. **Empty** — First-time use, no data (provide CTA)
3. **Loading** — Fetching or processing (skeleton screens > spinners)
4. **Error** — Action failed (empathetic message + recovery path)
5. **Partial** — Some data available, or extreme text lengths
6. **Disabled** — No permission, or prerequisites unmet

### Forms

- Group related fields logically
- Ask only for information needed at that stage
- Use labels, help text, defaults, and validation feedback
- Make errors specific and recoverable
- Never wipe the whole form on one field's validation failure

### Destructive Actions

- Prefer undo over confirmation dialogs (users click through confirmations mindlessly)
- Use confirmation only for truly irreversible or high-cost actions
- Make consequences clear before the action is taken

### Decision Framework

| Design Choice | Resolution |
|---|---|
| Free-form vs Dropdown | Constrained choices for standard data; free-form for unique text |
| Pagination vs Infinite Scroll | Pagination for finding specific items; infinite scroll for discovery |
| Explicit Save vs Auto-save | Auto-save for long-form content; explicit save for configuration |
| Modals vs New Pages | Modals for quick supplementary actions; new pages for complex tasks |

---

## LAYER 2: VISUAL CRAFT LAWS

These rules apply to every CSS file, every component, every design decision. They are not optional.

### Color

- **Use OKLCH.** Not HSL, not hex for design decisions. OKLCH is perceptually uniform.
- **Never use `#000` or `#fff`.** Tint every neutral toward the brand hue (chroma 0.005-0.01).
- **Pick a color strategy before picking colors:**
  - **Restrained** — tinted neutrals + one accent ≤10%. Product default; brand minimalism.
  - **Committed** — one saturated color carries 30-60% of the surface. Brand default.
  - **Full palette** — 3-4 named roles, each used deliberately. Brand campaigns; data viz.
  - **Drenched** — the surface IS the color. Brand heroes, campaign pages.
- **60-30-10 is about visual weight**, not pixel count. Accent works because it's rare.
- **Alpha is a design smell.** Heavy `rgba()`/`hsla()` use means an incomplete palette. Define explicit overlay colors.
- **Gray text on colored backgrounds is always wrong.** Use a darker shade of the background color, or transparency.
- See [reference/color-and-contrast.md](reference/color-and-contrast.md) for full guidance.

### Typography

- **Body text minimum 16px (1rem).** Below this fails WCAG on mobile.
- **Cap body line length at 65-75ch** using `max-width: 65ch`.
- **Hierarchy through scale + weight contrast.** Minimum 1.25 ratio between type steps. Flat scales (1.1x) read as uncommitted.
- **Fluid `clamp()` for headings only.** Body text stays at fixed rem. Keep `max ≤ 2.5x min`.
- **Light text on dark: compensate on three axes.** Bump line-height +0.05-0.1, add letter-spacing 0.01-0.02em, optionally step weight up one notch.
- **ALL-CAPS needs tracking.** Add 0.05em-0.12em letter-spacing to all-caps labels and headings.
- **`text-wrap: balance` on headings, `text-wrap: pretty` on prose.**
- **Web font loading:** Use `font-display: swap`. Preload the critical weight only. Match fallback metrics to minimize CLS.
- See [reference/typography.md](reference/typography.md) for full guidance.

### Layout & Spacing

- **4pt base grid** (4, 8, 12, 16, 24, 32, 48, 64, 96px). Name tokens semantically (`--space-sm`), not by value.
- **Vary spacing for rhythm.** Same padding everywhere is monotony.
- **Cards are the lazy answer.** Use them only when truly the best affordance. **Never nest cards inside cards.**
- **Don't wrap everything in a container.** Most things don't need one.
- **Use `gap` instead of margins** for sibling spacing.
- **Touch targets minimum 44x44px.** Use padding or pseudo-elements to expand without changing visual size.
- See [reference/spatial-design.md](reference/spatial-design.md) for full guidance.

### Motion

- **Ease out with exponential curves:** `cubic-bezier(0.16, 1, 0.3, 1)` (expo out) is the recommended default.
- **No bounce. No elastic.** They feel tacky and amateurish.
- **Don't animate CSS layout properties** (`width`, `height`, `top`, `left`, margins).
- **Exit animations are faster than entrances** (~75% of enter duration).
- **Duration guide:** 100-150ms (instant feedback), 200-300ms (state changes), 300-500ms (layout), 500-800ms (entrances).
- **`prefers-reduced-motion` is mandatory.** Provide crossfade alternatives, not just `animation: none`.
- See [reference/motion-design.md](reference/motion-design.md) for full guidance.

### Interaction Design

- **Every interactive element needs 8 states:** default, hover, focus, active, disabled, loading, error, success.
- **Never `outline: none` without replacement.** Use `:focus-visible` for keyboard-only focus rings.
- **Placeholders aren't labels.** They disappear on input. Always use visible `<label>` elements.
- See [reference/interaction-design.md](reference/interaction-design.md) for full guidance.

### Responsive Design

- **Mobile-first.** Base styles for mobile, `min-width` queries to layer complexity.
- **Content-driven breakpoints.** Let content tell you where to break, not device sizes.
- **Detect input method, not just screen size.** Use `@media (pointer: coarse)` and `@media (hover: none)`.
- **Handle the notch.** Use `env(safe-area-inset-*)` and `viewport-fit=cover`.
- See [reference/responsive-design.md](reference/responsive-design.md) for full guidance.

### UX Writing

- **Button labels: verb + object.** "Save changes" not "OK". "Delete project" not "Yes".
- **Error messages: What happened + Why + How to fix.** Never blame the user.
- **Empty states are onboarding moments.** Acknowledge, explain value, provide CTA.
- **Consistency: pick one term and enforce it.** Delete/Remove/Trash → pick one.
- See [reference/ux-writing.md](reference/ux-writing.md) for full guidance.

### Absolute Bans

Match-and-refuse. If you're about to write any of these, rewrite the element with different structure:

- **Side-stripe borders.** `border-left` or `border-right` > 1px as colored accent. Rewrite with full borders, background tints, icons, or nothing.
- **Gradient text.** `background-clip: text` with gradient. Use a single solid color. Emphasis via weight or size.
- **Glassmorphism as default.** Blurs and glass cards used decoratively. Rare and purposeful, or nothing.
- **The hero-metric template.** Big number, small label, supporting stats, gradient accent. SaaS cliche.
- **Identical card grids.** Same-sized cards with icon + heading + text, repeated endlessly.
- **Modal as first thought.** Exhaust inline and progressive alternatives first.
- **Em dashes in copy.** Use commas, colons, semicolons, periods, or parentheses.

### The AI Slop Test

If someone could look at this interface and say "AI made that" without doubt, it has failed. Check:
- Are you using Inter, DM Sans, or Outfit by reflex?
- Is the palette purple-to-blue or teal-to-green?
- Are there rounded-square icon tiles above every heading?
- Is every section a centered stack with identical card grids?
- Could someone guess the palette from the category name alone? ("fintech = navy + gold", "healthcare = white + teal")

If yes to any: rework until the answer is no.

---

## LAYER 3: REGISTER SYSTEM

Every design task is either **brand** or **product**. Identify before designing.

### Brand Register

When design IS the product: brand sites, landing pages, marketing surfaces, portfolios, editorial.

- **Typography:** Distinctive + refined. Display serif + sans body, or rule-breaking mono-only. Two families minimum only when voice needs it. Modular scale, fluid `clamp()`, ≥1.25 ratio.
- **Color:** Committed, Full Palette, and Drenched strategies are encouraged. Palette IS voice. Don't hedge with neutrals.
- **Layout:** Asymmetric compositions or rigorously-gridded. The failure is splitting the difference into a generic centered stack. Don't default to centering everything.
- **Motion:** Ambitious first-load motion permitted. Scroll-triggered transitions, typographic choreography.
- **Imagery:** Brand surfaces that imply imagery (fashion, food, travel, hotels) MUST ship imagery. Zero images is a bug.
- **Permissions:** Single-purpose viewports, typographic risk, unexpected color strategies, art direction per section.
- **Font selection:** Follow the 4-step procedure in [reference/brand.md](reference/brand.md). Check against the reflex-reject list.
- **Reflex-reject font list:** Fraunces, Newsreader, Lora, Crimson (all variants), Playfair Display, Cormorant, Cormorant Garamond, Syne, IBM Plex families, Space Mono, Space Grotesk, Inter, DM Sans, DM Serif families, Outfit, Plus Jakarta Sans, Instrument Sans, Instrument Serif. When the existing brand has already committed to a font, identity-preservation wins; the reject list applies to new greenfield choices only.
- See [reference/brand.md](reference/brand.md) for full guidance.

### Product Register

When design SERVES the product: app UIs, dashboards, settings, data tables, tools.

- **Typography:** System fonts are legitimate. One family is often right. Fixed rem scale, not fluid. Tighter scale ratio (1.125-1.2).
- **Color:** Restrained by default. Accent for primary actions only, not decoration.
- **Layout:** Predictable grids. Familiar patterns are features. Standard navigation.
- **Components:** Every interactive component has all 8 states. Skeleton states for loading.
- **Motion:** 150-250ms. Motion conveys state, not decoration. No orchestrated page-load sequences.
- See [reference/product.md](reference/product.md) for full guidance.

### Register Detection

Priority order: (1) Cue in the task ("landing page" = brand, "dashboard" = product), (2) the surface in focus, (3) PRODUCT.md if it exists. First match wins.

---

## LAYER 4: EXECUTION STANDARDS

### Framer Motion Performance

- **Never run infinite intervals off-screen.** Pause `setInterval` crossfaders when element is out of view using Intersection Observer or `useMotionValueEvent`.
- **Explicit variant typing.** Always type variants using `const variants: Variants = {...}` to catch invalid CSS at compile time.

### Layout & Clipping Integrity

- **Beware `overflow: hidden` on complex hero sections.** For portal/zoom effects, the section container can use `overflow: clip`, but the sticky wrapper inside MUST use `overflow: visible`.
- **SVG animations:** Don't mix absolute SVGs with CSS Grid children. Put SVGs in a wrapper absolutely positioned outside the grid container.

### 3D CSS Perspectives

- For premium horizontal galleries, use 3D Coverflow: parent `perspective: 1200px`, track `transform-style: preserve-3d`, cards calculate `rotateY` and `z` from center distance.

### Architectural Polish

- **Global reduced motion:** ALWAYS include `@media (prefers-reduced-motion: reduce)` that forces `animation-duration: 0.01ms !important` and `scroll-behavior: auto`.
- **Film grain overlays:** For premium dark aesthetics, implement as SVG `<feTurbulence>` filter via Base64 data URI in `::after`, `opacity: 0.03`, `pointer-events: none`.
- **Typographic contrast:** Never use display (serif) fonts for long-form paragraph text. Body (sans-serif) for paragraphs.

---

## BEHAVIORAL WORKFLOW

### For New Screens/Flows

1. Write the user goal in plain language
2. Determine register (brand or product)
3. Map the flow as a sequence of states
4. Define content hierarchy (primary, secondary, deferrable)
5. Design all 6 UI states explicitly
6. Apply visual craft laws (color, type, spacing, motion)
7. Run the AI slop test
8. Check accessibility and responsive behavior
9. Verify against anti-patterns and absolute bans

### For Improving Existing UI

1. Identify where users hesitate, misclick, or become confused
2. Determine whether the issue is hierarchy, wording, states, flow, or craft
3. Fix the most important friction first
4. Re-check state coverage, accessibility, and anti-patterns

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Fix |
|---|---|---|
| Exposing the Machine | Raw stack traces, HTTP codes in UI | Catch at boundary, translate to human-readable copy |
| Mystery Meat Navigation | Icons without text labels | Pair icons with text labels for primary navigation |
| Dead End Empty State | "No documents found" with no actions | Explanation + primary CTA to create first item |
| Unforgiving Interface | Form clears all fields on one error | Preserve valid state, warn before destruction |
| Component-Centric Thinking | Starting from widgets, not user journey | Design components to serve the flow |

---

## NON-NEGOTIABLE CHECKLIST

Before delivering any frontend work:

- [ ] Primary CTA is obvious and singular per view
- [ ] All async actions have loading indicators and success/failure states
- [ ] Error messages are empathetic and state next steps
- [ ] All 6 UI states accounted for
- [ ] Destructive actions protected
- [ ] No technical jargon in user-facing copy
- [ ] Body text ≥ 16px
- [ ] No pure black or pure white — all neutrals tinted
- [ ] Motion uses exponential ease-out, no bounce
- [ ] `prefers-reduced-motion` respected with alternatives
- [ ] Touch targets ≥ 44px
- [ ] Focus rings visible for keyboard navigation
- [ ] Line length capped at 65-75ch
- [ ] No items from the absolute bans list
- [ ] Passes the AI slop test

---

**Final Rule:** A good interface helps users succeed without making them think harder than necessary. If the user still feels lost, the design is not good enough. If someone could say "AI made that" without hesitation, the craft is not good enough.
