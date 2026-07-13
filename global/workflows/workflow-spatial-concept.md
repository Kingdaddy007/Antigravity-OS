---
name: workflow-spatial-concept
description: Compare visible spatial concept territories, record selection, and hand the chosen premise into experience architecture
id: spatial-concept
version: 2
status: active
intent: Select a brand-specific whole-page concept through explicit criteria rather than taste, novelty, or effect preference.
use_when: [three spatial concept territories and rough tests are ready for comparison]
do_not_use_when: [evidence or creative brief is unresolved, territories have not been externally tested, general product UI, or implementation]
inputs: [evidence dossier, creative brief, concept directions, visible rough tests, constraints]
required_resources: [applicable AGENTS.md files, spatial-experience-design, storytelling, master-design-director]
mutation_class: local_edit
approval_gates: [territory completeness, Director selection review, explicit user selection or hybrid approval]
states: [validate, compare, challenge, recommend, approve, record, handoff]
outputs: [selection record inside concept-directions.md, experience-architecture questions, evidence, residual risks]
verification: [selection traces to brief criteria, hybrid conflicts are resolved, rejected options retain rationale]
failure_paths: [return to visual-brainstorm for missing divergence or tests, return to brief for invalid criteria]
resume_contract: task-scoped .agents/workflows/spatial-concept.json using the workflows directory contract
next_workflows: [storytelling, spatial-design-ui]
profiles: [spatial]
---

# WORKFLOW: SPATIAL CONCEPT SELECTION

## PURPOSE

Choose the governing whole-page concept after evidence, briefing, divergence, references, and visible rough tests. Selection is a strategic decision with downstream costs; it is not a vote for the prettiest hero.

## ENTRY GATE

Confirm `concept-directions.md` or an equivalent contains for all three territories:

- governing premise and first-known priority;
- whole-page narrative and chapter logic;
- opening form and proof strategy;
- visual and stillness/motion posture;
- reference provenance;
- visible rough test;
- assets, constraints, risks, and failure conditions.

If any territory lacks a visible test or full-page logic, return to `workflow-visual-brainstorm.md`.

## COMPARISON

Score and discuss—not mechanically average—each territory against:

1. Brand truth and perception-gap repair.
2. Desired first impression and first-known priority.
3. Controlling argument and full-page potential.
4. Proof strength, timing, and visitor comprehension.
5. Distinctiveness without reference imitation.
6. Asset feasibility and content reality.
7. Motion necessity versus stillness.
8. Accessibility and responsive integrity.
9. Performance and maintenance burden.
10. Inquiry readiness and wrong-fit filtering.

Name the riskiest assumption, strongest reason to choose, strongest reason to reject, and second-order consequences of each.

## COGNITIVE ENGINE CHECKPOINT

Concept selection is a Type 1.5 decision. Load `core/system-thinking.md`, `core/expert-cognitive-patterns.md`, and `core/first-principles.md`, then test the comparison before recommending a winner:

- Re-check which criteria are supported by evidence and which are preference or inference.
- Reframe the decision as both “Which page is most compelling?” and “Which page can this studio truthfully sustain?”
- Challenge the polished favorite: would it still win if all three tests had equal visual finish?
- Run a short pre-mortem: six months after launch, how could the chosen direction have failed through assets, proof, accessibility, performance, maintenance, or weak inquiry readiness?
- Record the reversal condition that would return the project to territory exploration.

## DIRECTOR CHALLENGE

Use `master-design-director` Concept Selection Gate. Actively test whether:

- the obvious favorite is benefiting from polish rather than logic;
- a restrained option was undervalued because it looks less spectacular;
- assets can actually sustain the promised experience;
- motion is compensating for weak composition;
- the concept remains compelling beyond the opening;
- the page can communicate on mobile and with reduced motion.

## SELECTION RECORD

Recommend one territory with explicit tradeoffs, then wait for user selection. The user may approve a hybrid only when the record states:

- which governing premise remains primary;
- which exact element is borrowed and why;
- what conflict the combination creates;
- how that conflict is resolved;
- which rejected mechanics stay rejected.

Write the decision, rationale, rejected alternatives, assumptions, risks, and return conditions into `concept-directions.md`.

## HANDOFF

Do not immediately convert the selected territory into implementation. Prepare questions for `experience-blueprint.md`: narrative form, chapter jobs, hierarchy, proof timing, copy-image relationship, inquiry, responsive intent, visual system, motion posture, and asset contract.

## QUALITY GATE

- [ ] All territories have comparable visible evidence.
- [ ] Selection traces to approved brief criteria.
- [ ] Full-page value outweighs hero novelty.
- [ ] Motion and stillness were compared explicitly.
- [ ] Asset, accessibility, performance, and maintenance costs are visible.
- [ ] User explicitly selected a territory or resolved hybrid.
- [ ] Rejected options and return conditions remain documented.
