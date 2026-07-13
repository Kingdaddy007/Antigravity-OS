---
name: workflow-visual-brainstorm
description: Generate and visibly test three brand-grounded whole-page concept territories for a spatial website
id: visual-brainstorm
version: 2
status: active
intent: Create genuine early divergence before concept selection, using purposeful references and rough externalization.
use_when: [an approved spatial creative brief needs distinct concept territories]
do_not_use_when: [diagnosis or creative brief is unresolved, a concept is already selected, general product UI, or implementation]
inputs: [evidence dossier, approved creative brief, available assets, constraints]
required_resources: [applicable AGENTS.md files, storytelling, spatial-experience-design, master-design-director]
mutation_class: local_edit
approval_gates: [creative brief approved, territory divergence confirmed, visible rough tests complete]
states: [brief-check, diverge, question-map, reference, externalize, compare, deliver]
outputs: [concept-directions.md or approved equivalent, reference provenance, three visible rough tests, risks]
verification: [territories differ structurally, every reference answers a named question, every territory has a visible test]
failure_paths: [return to creative brief when territories cannot be distinguished, preserve uncertainty, report missing assets]
resume_contract: task-scoped .agents/workflows/visual-brainstorm.json using the workflows directory contract
next_workflows: [spatial-concept]
profiles: [spatial]
---

# WORKFLOW: VISUAL BRAINSTORM

## PURPOSE

Discover possible whole-page concepts before committing to one. This workflow exists to make thinking visible and comparable, not to decorate an already selected direction.

## REQUIRED INPUT GATE

Read `evidence-dossier.md` and the approved `creative-brief.md` or equivalents. Confirm:

- first-known priority;
- desired visitor response;
- proof burden;
- asset reality;
- anti-goals;
- selection criteria.

If these are unresolved, return to the relevant inception phase.

## COGNITIVE ENGINE CHECKPOINT

This is a Type 1.5 creative decision because the selected territory shapes every later asset, narrative, motion, and implementation choice. Load `core/system-thinking.md`, `core/expert-cognitive-patterns.md`, and `core/first-principles.md` before generating directions.

- Separate verified evidence, reported claims, inferences, and unknowns; do not let an attractive inference become the premise.
- Restate the problem from the visitor's first impression and from the studio's business problem; compare both frames.
- Apply gray thinking: create three structurally different whole-page answers, including a restrained/still-led answer unless evidence rules it out.
- Apply anti-comfort: challenge the most obvious territory and identify the strongest reason it could fail.
- Map second-order effects for each territory: asset burden, proof clarity, accessibility, responsive behavior, performance, maintenance, and inquiry posture.
- Record the riskiest assumption each visible rough test must try to disprove.

## EXECUTION

### 1. Generate Three Structural Territories

Use different governing arguments and page logics. Differences may include transformation-led, project-led editorial, material/process-led, point-of-view-led, proof-first, atmosphere-led, founder-led, or another evidence-grounded form.

At least one territory must test restraint or a still-led approach unless the brief explicitly rules it out. Do not submit three hero treatments, palettes, typography styles, animation systems, or versions of the same chapter order.

For each territory define:

- premise and controlling argument;
- what the visitor knows first;
- narrative form and chapter jobs;
- opening form;
- proof strategy;
- visual posture and stillness/motion posture;
- asset requirements and missing evidence;
- responsive, accessibility, performance, and maintenance implications;
- reason it belongs to this brand;
- failure condition.

### 2. Name Design Questions Before References

Examples: How can the project proof lead without feeling technical? What crop behavior makes material intelligence legible? Can a still opening create enough tension? How might a transformation compare without a generic slider?

Search or browse only after questions exist. Record source, observed mechanic, adapted lesson, rejected imitation, and where the reference does **not** fit. A reference can influence one decision without donating its site architecture.

### 3. Externalize Every Territory

Produce a mini reference board plus at least one visible rough test per territory:

- styleframe;
- low-fidelity page sequence;
- motion study;
- asset/crop test;
- coded micro-prototype;
- or another proportionate representation.

Use real or realistic-enough imagery and type. The test must expose the territory's most important assumption, not merely make it attractive.

### 4. Run the Divergence Gate

Use `master-design-director` to ask:

- Would choosing a different territory materially change the page architecture?
- Is each territory a complete page idea rather than a hero idea?
- Is one option merely the safest styling of another?
- Are references supporting questions rather than leading taste?
- Does every visible test reveal both potential and cost?

If divergence fails, revise before selection.

### 5. Write the Comparison Contract

Create or update `concept-directions.md` with the brief criteria, all three territories, reference provenance, rough-test evidence, unresolved risks, and a neutral comparison. Do not select the winner inside this workflow.

## QUALITY GATE

- [ ] Creative brief is approved.
- [ ] Exactly three territories are structurally distinct.
- [ ] A restrained/still-led option exists or its evidence-based exclusion is recorded.
- [ ] References answer named questions.
- [ ] Each territory has a visible rough test.
- [ ] Full-page logic, proof, assets, motion necessity, and constraints are comparable.
- [ ] No winner is chosen before the selection gate.
