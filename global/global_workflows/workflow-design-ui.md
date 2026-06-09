---
name: workflow-design-ui
description: Route frontend design work for high-end interior storytelling websites
---

# WORKFLOW: DESIGN UI

## WHAT THIS WORKFLOW DOES

Route frontend design work for high-end interior storytelling websites. Use the spatial system for brand/portfolio/showroom pages and use UI/UX rules to keep navigation, galleries, proof, inquiry, accessibility, and responsive behavior usable.

## ACTIVATION

Use when:

- Designing or implementing pages, components, galleries, inquiry forms, navigation, project indexes, material swatches, or responsive UI for interior/spatial websites.
- Improving a decorator or spatial design site that feels generic, unclear, inaccessible, or template-like.

Do NOT use when:

- The task is backend/API/security/database/DevOps-only.
- The task is pure copywriting without layout or UX impact.

## REQUIRED FILES

For spatial brand pages, load:

- `skills/spatial-experience-design/SKILL.md`
- `skills/ui-ux/SKILL.md`
- `skills/cinematic-motion/SKILL.md` when motion is present
- `workflows/workflow-spatial-concept.md`
- `workflows/workflow-impeccable-craft.md`
- `skills/spatial-experience-design/reference/audit-mechanics-map.md`
- `skills/spatial-experience-design/reference/scene-kit-and-asset-directive.md`
- `contexts/spatial/` artifacts

## ROUTING

### Spatial Brand Surface

Interior decorator portfolio, spatial studio, gallery, showroom, furniture/decor brand, architecture-adjacent website, luxury home brand.

Route:

1. `workflow-spatial-concept.md` if artifacts are missing.
2. `workflow-visual-brainstorm.md` if exploring direction.
3. `workflow-impeccable-craft.md` for implementation.
4. `workflow-impeccable-animate.md` for non-trivial motion.

### Product-Like UI Inside Spatial Site

Project filter, material selector, inquiry form, private portfolio gate, booking/request flow.

Route:

1. Use `skills/ui-ux/SKILL.md`.
2. Preserve spatial tone.
3. Design all states.
4. Verify accessibility and mobile behavior.

## EXECUTION SEQUENCE

### STEP 1: Confirm Context

Identify:

- site type
- visitor goal
- inquiry goal
- active spatial artifacts
- current stage in Atmosphere -> Taste -> Transformation -> Proof -> Method -> Inquiry

Gate: If spatial artifacts are missing for a brand page, run `workflow-spatial-concept.md`.

### STEP 2: Map UI Responsibilities

Define:

- navigation model
- project/gallery browsing
- proof presentation
- method/process section
- inquiry path
- states and errors
- mobile behavior

### STEP 3: Build Or Refine

Use `workflow-impeccable-craft.md`.

Preserve:

- visual thesis
- scene kit
- depth map
- material script
- motion board
- asset boundary

### STEP 4: Verify

Check:

- primary action clarity
- quiet inquiry visibility
- gallery/project usability
- responsive crops
- keyboard/focus behavior
- reduced-motion behavior
- anti-template smell tests

## QUALITY GATE CHECKLIST

- [ ] Spatial brand pages route through spatial concept first.
- [ ] UI follows the spatial journey.
- [ ] All forms and interactive elements include states and accessibility.
- [ ] Project/gallery UI supports curation before scanning.
- [ ] No SaaS hero/card-grid/default CTA pattern appears by accident.
