---
id: ui-animate
version: 1
status: active
intent: Add purposeful motion to a general product interface without weakening usability, accessibility, or performance.
use_when: [a product interface needs feedback, continuity, hierarchy, state transition, or orientation through motion]
do_not_use_when: [motion is purely decorative, reduced-motion behavior is undefined, the request is spatial cinematic motion]
inputs: [implemented interface, interaction states, DESIGN.md or motion tokens, active performance constraints]
required_resources: [applicable AGENTS.md files, skills/ui-ux/SKILL.md, skills/ui-ux/reference/motion-design.md]
mutation_class: local_edit
approval_gates: [confirm new dependencies, scope expansion, or external assets before proceeding]
states: [intake, identify-purpose, define-motion-contract, implement, verify-reduced-motion, verify-performance, deliver]
outputs: [motion implementation, purpose-to-motion mapping, reduced-motion behavior, performance evidence, residual risks]
verification: [verify state transitions, keyboard and pointer parity, prefers-reduced-motion behavior, layout stability, and applicable performance budgets]
failure_paths: [remove or simplify motion that harms comprehension, accessibility, responsiveness, or performance]
resume_contract: task-scoped .agents/workflows/ui-animate.json using the workflows directory contract
next_workflows: [verify-project]
profiles: [general]
---

# Workflow: UI Animate

## Sequence

1. Name the user-facing purpose of every proposed motion: feedback, continuity, hierarchy, progress, or orientation.
2. Define trigger, affected property, duration, easing, interruption behavior, and reduced-motion alternative.
3. Prefer transform and opacity where they preserve layout and meaning; do not animate inaccessible hidden state or delay required actions.
4. Implement motion through existing project primitives before adding a dependency.
5. Verify pointer, keyboard, touch, interrupted transitions, narrow viewports, reduced motion, and layout stability.
6. Remove motion that has no observable purpose or misses its performance budget.
7. Deliver the motion contract, changed artifacts, evidence, and remaining risks.

