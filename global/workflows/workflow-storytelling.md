---
id: storytelling
version: 2
status: active
intent: Turn an approved spatial concept into a controlling argument, brand-specific narrative form, chapter jobs, proof choreography, and inquiry posture.
use_when: [a spatial territory is selected and experience architecture must be defined]
do_not_use_when: [concept territories are still open, final copywriting, general product UI, or implementation]
inputs: [evidence dossier, creative brief, selected concept, approved rough test]
required_resources: [applicable AGENTS.md files, storytelling skill, matching guide, master-design-director]
mutation_class: local_edit
approval_gates: [selected concept confirmed, narrative alternatives compared, experience gate approved]
states: [context, argument, alternatives, chapters, proof, integration, approve, write]
outputs: [narrative and content architecture inside experience-blueprint.md or approved equivalent, evidence, residual risks]
verification: [chapter jobs prove the controlling argument, proof timing matches trust burden, selected form traces to brand evidence]
failure_paths: [return to concept selection when narrative exposes a weak premise, return to creative brief when priorities conflict]
resume_contract: task-scoped .agents/workflows/storytelling.json using the workflows directory contract
next_workflows: [spatial-design-ui]
profiles: [spatial]
---

# WORKFLOW: SPATIAL STORYTELLING

## PURPOSE

Define what the selected concept argues and how the visitor moves from first impression to proof and selective inquiry. Storytelling shapes experience architecture; it does not independently lock a hero, animation system, or fixed section sequence.

## ENTRY GATE

Read `evidence-dossier.md`, `creative-brief.md`, and the selection record in `concept-directions.md` or approved equivalents. Do not proceed if the territory is unselected or if its first-known priority contradicts the brief.

Load:

- `skills/storytelling/SKILL.md`;
- `skills/storytelling/references/resource-index.md` for task-specific resources;
- `skills/storytelling/library/matching-guide.md` when comparing mechanics or archetype fit;
- `skills/master-design-director/SKILL.md` for the experience gate.

References provide vocabulary and tests. They do not dictate the page order.

## COGNITIVE ENGINE CHECKPOINT

Experience architecture is a Type 1.5 creative decision. Load `core/system-thinking.md`, `core/expert-cognitive-patterns.md`, and `core/first-principles.md` before locking chapter order. Separate evidence from inherited category convention, compare at least two narrative forms, and challenge whether the proposed first chapter earns its priority from the brief. Map second-order effects on proof timing, comprehension, mobile behavior, motion need, and inquiry readiness. If the controlling argument cannot survive a quiet still-image version, do not use cinematic treatment to conceal the gap.

## EXECUTION

### 1. Name the Controlling Argument

State the single proposition the experience must make believable. Identify the visitor's starting belief, desired ending belief, evidence required for the shift, and what would falsify the argument.

### 2. Compare Narrative Forms

Test at least two forms compatible with the selected territory: atmosphere-led, transformation-led, point-of-view-led, material/process-led, project-led editorial, proof-first, founder-led, or another justified form.

Do not treat `Atmosphere -> Taste -> Transformation -> Proof -> Method -> Inquiry` as default law; it remains one useful candidate. Choose based on what this studio must establish first and its proof burden.

### 3. Define Chapter Jobs

For every chapter define:

- claim or question;
- visitor emotion and comprehension goal;
- primary evidence;
- copy posture;
- visual responsibility;
- interaction or motion job, including `none`;
- transition relationship to adjacent chapters;
- responsive intent;
- contribution to inquiry readiness.

Chapter names may be spatial, editorial, project-based, or direct. Avoid generic service-page structure unless the evidence and user task genuinely require it.

### 4. Choreograph Proof and Inquiry

Decide when to reveal projects, transformations, material/process intelligence, credentials, press, client evidence, founder authority, method, fit, and exclusions. Use detailed `portfolio-proof-chapters.md` only when individual project decisions need their own narrative contract.

### 5. Integrate Copy, Visuals, and Stillness/Motion

For each chapter record what copy says, what visuals prove, and what interaction or motion adds. Motion is not required. Do not ask animation to communicate missing copy or ask atmospheric imagery to carry unsupported proof.

### 6. Director Experience Gate

Present the controlling argument, compared forms, selected narrative, chapter jobs, proof timing, inquiry posture, and unresolved risks. Use `master-design-director` to approve, revise, simplify, or return to concept.

### 7. Write the Blueprint Contribution

Add the approved narrative architecture to `experience-blueprint.md`. Legacy `story.md` or `spatial-story.md` files remain valid equivalents when they contain the same approved decisions.

Create `scroll-storyboard.md` only if the selected experience depends on authored scroll timing, pinning, persistent continuity, or media choreography.

## QUALITY GATE

- [ ] Controlling argument traces to evidence and brief.
- [ ] At least two compatible narrative forms were compared.
- [ ] Selected order follows first-known priority, not a universal sequence.
- [ ] Every chapter has a communication and evidence job.
- [ ] Proof timing matches trust burden.
- [ ] Copy, visual, interaction, and motion responsibilities do not duplicate or contradict one another.
- [ ] Motion and scroll storyboarding remain conditional.
- [ ] Director approved the experience architecture.
