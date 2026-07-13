---
name: workflow-impeccable-animate
description: Plan, prototype, implement, and verify only the motion justified by an approved spatial concept
id: impeccable-animate
version: 2
status: active
intent: Add purposeful spatial motion without turning cinematic technique into a universal requirement.
use_when: [approved non-trivial motion is part of a spatial production contract]
do_not_use_when: [still-led concepts, decorative motion requests, missing motion job or fallback, general product UI, or backend work]
inputs: [experience blueprint, production plan, approved prototype evidence, implementation authority]
required_resources: [applicable AGENTS.md files, cinematic-motion, exact implementation references selected by motion job]
mutation_class: local_edit
approval_gates: [motion necessity, risk prototype, dependency changes, per-slice verification]
states: [validate, classify, prototype, implement, integrate, verify, deliver]
outputs: [motion implementation, fallback behavior, performance/accessibility evidence, changed-artifact list, residual risks]
verification: [semantic job, track ownership, scroll behavior, mobile, reduced motion, navigation and inquiry reachability, performance]
failure_paths: [use stillness or simpler behavior, return to production contract when assumptions change, preserve functional content]
resume_contract: task-scoped .agents/workflows/impeccable-animate.json using the workflows directory contract
next_workflows: [verify-project]
profiles: [spatial]
---

# WORKFLOW: SPATIAL ANIMATE

## ACTIVATION GATE

Before code, confirm:

- the communication job;
- evidence that the motion belongs to the selected concept;
- why stillness or a simple transition is insufficient;
- approved assets and interaction model;
- mobile, reduced-motion, loading, and failure behavior;
- performance and maintenance budget;
- prototype evidence for the riskiest mechanic.

If the gate fails, use stillness or a simpler behavior. That is a successful design decision, not a missing feature.

## LOAD PURPOSEFULLY

Load `skills/cinematic-motion/SKILL.md`. Use `motion-library` and its semantic index only to find candidates for a named job. Load GSAP, canvas, WebGL, video choreography, mobile fallback, or performance references only for the selected implementation.

Activate `cinematic-showroom-strategy` only for genuinely media-heavy choreography. Create `scroll-storyboard.md` only when authored scroll depth, pinning, persistence, or synchronized media requires it.

## EXECUTION

### 1. Classify Applicable Tracks

Separate only the tracks in use:

- arrival;
- ambient;
- scroll-bound;
- interaction.

Unused tracks are explicitly `none`. Keep ownership separate to prevent timeline collisions.

### 2. Prototype Risk

Test the hardest motion assumption with the real-enough asset, typography, viewport behavior, and fallback. Do not learn feasibility after the whole page depends on it.

### 3. Implement the Simplest Sufficient Technique

- CSS for simple hover, focus, state, and transition behavior.
- GSAP/ScrollTrigger for justified timeline, pin, or scrub choreography.
- Canvas sequences for frame-accurate pre-rendered media with preload and poster plans.
- CSS 3D or WebGL only when depth, camera, inspection, or material behavior cannot be communicated more simply.
- Video only for a section-specific atmosphere, threshold, transformation, material, proof, or inquiry job.

Do not add a dependency merely because a reference uses it.

### 4. Integrate Without Hiding Content

Semantic content, navigation, proof, and inquiry must remain reachable before, during, and after motion. Scroll-bound motion stops with scroll unless intentionally ambient. Keyboard and touch interactions receive equivalents.

### 5. Verify

Check normal, fast, reverse, interrupted, resized, mobile, touch, reduced-motion, slow-loading, and failure paths. Verify offscreen pause, media controls where applicable, no scroll traps, no timeline collisions, stable layout, and acceptable performance.

Record whether each motion was retained, simplified, or removed and why.

## QUALITY GATE

- [ ] Motion passed the activation test.
- [ ] Stillness was explicitly considered.
- [ ] Applicable tracks have separate ownership.
- [ ] The riskiest mechanic was prototyped.
- [ ] Technique and dependency are proportionate.
- [ ] Mobile and reduced-motion equivalents work.
- [ ] Navigation, proof, and inquiry stay reachable.
- [ ] Performance and failure behavior are verified.
- [ ] Motion still strengthens the selected concept after integration.
