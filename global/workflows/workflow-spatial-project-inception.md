---
name: workflow-spatial-project-inception
description: Discover, select, prototype, and produce a brand-specific interior or spatial website experience
id: spatial-project-inception
version: 2
status: active
intent: Execute the ten-phase BEVAMPED spatial project workflow with evidence discipline, visible concept divergence, approval gates, and conditional complexity.
use_when: [starting or substantially redesigning an interior, spatial, decor, showroom, gallery, furniture, staging, luxury-home, or architecture-adjacent brand website]
do_not_use_when: [general product or SaaS UI, a small implementation task with approved context, backend-only work, or Project 003 before separate authorization]
inputs: [user objective, available brand evidence, workspace context, constraints, requested authority mode]
required_resources: [applicable AGENTS.md files, brand-strategy, storytelling, spatial-experience-design, master-design-director]
mutation_class: local_edit
approval_gates: [evidence coverage, diagnosis, creative brief, territory divergence, concept selection, experience architecture, production contract, risk prototype, final approval]
states: [evidence, diagnose, brief, diverge, externalize, select, architect, systemize, prototype, produce, verify, deliver]
outputs: [five core artifact contracts or approved equivalents, conditional artifacts when justified, implementation when separately authorized, verification evidence, residual risks]
verification: [trace evidence to decisions and downstream consumers, run spatial consistency checks, record raw evidence, label anything unverified]
failure_paths: [return to the earliest invalidated gate, stop on authority or contract conflict, preserve state, report blocker and safe next action]
resume_contract: task-scoped .agents/workflows/spatial-project-inception.json using the workflows directory contract
next_workflows: [visual-brainstorm, spatial-concept, spatial-design-ui, impeccable-craft, impeccable-animate]
profiles: [spatial]
---

# WORKFLOW: BEVAMPED SPATIAL PROJECT INCEPTION

## PURPOSE

Turn evidence about one interior or spatial brand into a distinct, testable website concept and then into controlled production. The workflow discovers the concept; it does not assume a cinematic hero, fixed story sequence, video, motion, anchor object, or effect library choice.

## ARTIFACT CONTRACT

Maintain five logical contracts in `.agents/contexts/` or an approved equivalent location:

1. `evidence-dossier.md`
2. `creative-brief.md`
3. `concept-directions.md`
4. `experience-blueprint.md`
5. `production-plan.md`

They are contracts, not a file-count ritual. Existing approved documents may satisfy them. Legacy spatial projects may retain fourteen-file context sets; map their content, identify genuine gaps, and consolidate only with user approval.

Conditional outputs:

- `scroll-storyboard.md` for authored scroll timing, pinning, continuity, or media choreography;
- `cinematic-prompt-pack.md` for approved generated imagery/video;
- `portfolio-proof-chapters.md` for detailed project decision narratives;
- `DESIGN.md` / `DESIGN.json` for implementation tokens and component rules.

## TEN PHASES

### 1. Evidence Intake

Use `brand-strategy`. Catalog website, social, projects, assets, communications, proof, constraints, dates, and unknowns. Separate facts, reported claims, inferences, and unknowns. Write `evidence-dossier.md`.

**Gate:** User confirms coverage and unresolved gaps. Missing evidence may remain, but it must be visible.

### 2. Brand Diagnosis

Inside the dossier, diagnose perception gap, desired authority, audience, taste patterns, founder authority, proof burden, premium leaks, category conventions, wrong-fit audience, and inquiry posture. Do not prescribe visuals.

**Cognitive Engine checkpoint — Type 1.5 creative decision:** Load `core/system-thinking.md`, `core/expert-cognitive-patterns.md`, and `core/first-principles.md`. Decompose current perception, desired authority, evidence gap, real constraints, and unknowns. Reframe the diagnosis from the visitor's likely misunderstanding as well as the studio's self-description. Challenge any conclusion that relies on an attractive inference rather than observed proof, and record second-order implications for asset reality, proof burden, and inquiry posture.

**Gate:** User approves or revises diagnosis.

### 3. Creative Brief

Write `creative-brief.md`: what visitors should feel, understand, believe, and do; what must be known first; controlling problem; proof requirements; constraints; anti-goals; and territory-selection criteria.

**Gate:** `master-design-director` runs the Creative Brief Gate.

### 4. Concept Territories

Run `workflow-visual-brainstorm.md`. Generate three structurally different directions for the whole page, not hero, palette, or animation variations. Include one restrained or still-led option unless the evidence rules it out.

### 5. References and Rough Externalization

Gather references only for named design questions. For every territory, produce a mini reference board and a visible rough styleframe, sequence sketch, or prototype with realistic-enough assets. Record rationale and provenance in `concept-directions.md`.

**Gate:** The Director confirms genuine divergence. No territory advances without a visible rough test.

### 6. Concept Selection

Run `workflow-spatial-concept.md`. Compare territories on brand truth, first impression, proof, full-page potential, asset feasibility, motion necessity, accessibility, performance, responsiveness, and maintenance. Record the decision.

**Gate:** User selects one territory or an explicitly reasoned hybrid.

### 7. Experience Architecture

Use `storytelling` and `spatial-experience-design`. Decide controlling argument, narrative form, chapter jobs, hierarchy, proof timing, copy-visual relationship, inquiry, navigation, and responsive intent. Write `experience-blueprint.md`.

**Gate:** Director runs the Experience Gate.

### 8. Visual, Motion, and Asset Systems

Complete the blueprint and `production-plan.md`: type, color, composition, crop, material, density, stillness, motion grammar when justified, asset boundary, generated-media needs, performance, accessibility, fallbacks, and build slices. Activate `cinematic-showroom-strategy`, `cinematic-motion`, `scroll-storyboard`, and conditional artifacts only when their activation tests pass.

**Gate:** User and Director approve the production contract.

### 9. Risk Prototype and Vertical Slice

Prototype the most dangerous assumption first. Then create one representative sequence using real-enough imagery, typography, mobile behavior, and signature motion only when applicable. Store evidence and findings in `production-plan.md`.

**Gate:** Director verdict is `expand`, `revise`, `simplify`, or `return to concept`.

### 10. Full Production and Verification

After implementation authority, run `workflow-spatial-design-ui.md` and `workflow-impeccable-craft.md`; use `workflow-impeccable-animate.md` only when motion is approved. Build coherent slices and critique each slice. Verify accessibility, performance, responsive composition, reduced-motion/fallback behavior, proof, inquiry, and concept continuity.

**Gate:** Final Director and user approval.

## STABLE NICHE JOBS, VARIABLE DESIGN

Interior brands commonly need atmosphere/point of view, curated work/taste, transformation or design intelligence, authority/proof, process/fit, and selective inquiry. These are reusable communication jobs, not required sections or a fixed order.

Every project independently decides what is known first, emotional register, controlling argument, narrative form, opening form, typography, color, crop, material, density, motion amount, proof strategy, and inquiry posture.

## QUALITY GATE

- [ ] Evidence and inference are visibly separated.
- [ ] Diagnosis precedes visual prescription.
- [ ] Three whole-page territories diverge structurally and have visible rough tests.
- [ ] References answer named questions and are not copied as architecture.
- [ ] Selection rationale traces to brief criteria.
- [ ] Five contracts or approved equivalents cover the work.
- [ ] Optional complexity is explicitly accepted or rejected.
- [ ] A risk prototype and vertical slice precede broad production.
- [ ] The general project/UI workflow remains untouched.
