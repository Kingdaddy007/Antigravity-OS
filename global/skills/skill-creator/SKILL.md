---
name: skill-creator
description: >
  Use this skill when you need to CREATE or REFACTOR a skill file for the
  Anti-Gravity OS. Activated when the user asks to "build a new skill",
  "reformat a skill", "compress a skill", "apply the skill creator", or
  "update [skill name] to the new format". Also activated at the start of
  Phase 6 (skill refactoring) of the OS optimization plan. Produces lean,
  token-efficient SKILL.md files and multi-file skill packages using the 
  high-density truth-document format.
  Do NOT use for general file editing, writing documentation, or formatting arbitrary markdown.
---

# Skill Creator — Anti-Gravity OS

Build every Anti-Gravity skill as a **truth document**: dense, imperative, activation-first.
Never write a manual. Never explain the skill to a human reader. Write instructions for an AI.

---

## WHEN TO USE THIS

- Creating a new SKILL.md or multi-file skill package for Anti-Gravity OS
- Refactoring an existing skill to match the truth-document format
- Compressing an oversized skill to reduce token waste

## NEVER DO

- Write meta-commentary about why a skill exists or who it's for
- Include version history, file relationships, or inheritance headers
- Use declarative voice ("the expert does X") — use imperative only
- Leave anti-patterns as prose blocks when they can be tables
- Write descriptions without trigger phrases AND exclusions
- Force a complex skill into one file if it damages behavior; use references instead
- Create decorative references without explicit loading rules

---

## SINGLE-FILE VS MULTI-FILE PACKAGES

The skill-creator must decide whether to create:

### Option A: Single-File Skill
Use a single `SKILL.md` when the skill is:
- Narrow, procedural, low-context, or utility-focused.
- Easy to express as rules and short workflows.
- Not dependent on large examples, taxonomies, research, or critique banks.
*Examples: context hygiene, simple formatting, code review checklist, debugging assistant.*

### Option B: Multi-File Skill Package
Create a multi-file skill package when a skill requires deep knowledge, extended examples, taxonomies, critique language, research-derived frameworks, or specialist references that should not load every time.

Use this structure:
```text
[skill-name]/
  SKILL.md
  references/
    [agent-chosen-reference].md
```
Keep `SKILL.md` lean, imperative, and activation-first. Move deep supporting knowledge into `references/`. Do not force all intelligence into the main skill file. Do not compress away material that materially improves behavior. Use references to preserve depth while controlling context.

*Examples: master design director, brand strategist, architecture reviewer, legal reasoning assistant.*

---

## THE FORMAT CONTRACT

Every main `SKILL.md` must follow this exact structure:

```text
---
name: [skill-name]
description: > [LONG, specific activation trigger — see Rule 1 below]
---

# [Skill Name]

## WHEN TO USE THIS
[2-3 bullet conditions for loading. Concrete, not abstract.]

## NEVER DO
[3-8 hard behavioral boundaries. Short. Direct. No explanation.]

## [DOMAIN SECTION 1]
[Imperative instructions. What to DO.]

## REFERENCE LOADING RULES
[MANDATORY for multi-file packages. Optional for single-file. Defines when to load references.]

## OUTPUT SHAPE
[What a response looks like when this skill is active. Mode-specific template.]

## NON-NEGOTIABLE CHECKLIST
[Short numbered list. Verify before delivery.]
```

---

## THE RULES

### Rule 1 — The description field IS the activation trigger
The description must:
- State explicitly WHEN to load (trigger words + example phrases)
- State explicitly WHEN NOT to load (neighboring domains)
- Be specific enough that a routing system can activate it correctly without reading the whole file

### Rule 2 — Instructions only. No meta-commentary
Cut everything that exists to explain the skill's purpose, history, version, or relationship to other files. An AI does not need to be told why a file exists. It needs to be told what to do.

### Rule 3 — Imperative, not declarative
**Declarative (wrong):** "The expert coder treats readability as the highest implementation virtue."
**Imperative (right):** "Prioritize readability. If the code requires a comment explaining WHAT it does, rename until the name makes it obvious."

### Rule 4 — Reference Design & Loading Rules
When creating references for a multi-file package:
1. Create references only when they have a clear loading purpose. Do not create decorative references.
2. Write references as operational AI guidance (diagnostics, decision rules, examples). Do not create vague academic essays.
3. Keep each reference focused on a distinct task, domain, or knowledge cluster.
4. Merge references if they overlap; split if they become too broad.
5. Name reference files clearly and practically.

For every reference file created, the main `SKILL.md` MUST include a `REFERENCE LOADING RULES` section explicitly stating the filename, contents, and exact conditions for loading.
*Example:* `Load references/[filename].md when diagnosing [failure type] or producing [output type].`

### Rule 5 — Compress anti-patterns into a table
Use a 3-column table: `| Anti-Pattern | What It Is | Fix |`

### Rule 6 — Size Target & Philosophy
- For normal single-file skills, keep the existing target size rules (Narrow: <4KB, Standard: <8KB, Broad: <12KB, Complex: <15KB).
- For multi-file skill packages, keep `SKILL.md` lean and activation-focused.
- Allow `references/` files to be longer when depth is behaviorally necessary. Do not cut examples, audit frameworks, taxonomies, or response examples that teach the AI how to push back or speak.
- The goal is not maximum compression. The goal is controlled loading: lean command file, rich references.

### Rule 7 — The output shape section is mandatory
Every skill must define what a response looks like when it's active.

### Rule 8 — The Leading-Words Technique
Model reasoning is heavily influenced by the first few tokens of its prompt.
- **Commanding Imperatives:** Start sentences with verbs: `Run`, `Verify`, `Compare`, `Assert` (not `You should write...`).
- **Trigger Alignment:** Place signal keywords at the very top of descriptions and files to anchor model context early.

### Rule 9 — Eliminate Double Negatives
Models struggle with double negatives (e.g. "Do not avoid checking if tests are not failing"). Rephrase as positive commands: "Ensure tests pass before committing."

### Rule 10 — Model-Invoked vs User-Invoked Load
Distinguish between skills that are called explicitly by the user (high visibility) and skills that are loaded silently by the model based on trigger keywords. For model-invoked skills, keep the description tightly bound to specific triggers to prevent context pollution.

---

## OUTPUT FORMAT CONTRACT

The skill-creator must output the complete files. Do not output only a plan. Do not merely describe the folder. Produce the actual file contents using this format:

### For Single-File Skills
```markdown
# FILE: [skill-name]/SKILL.md

[full contents]
```

### For Multi-File Skill Packages
```markdown
# FILE: [skill-name]/SKILL.md

[full contents]

# FILE: [skill-name]/references/[reference-name].md

[full contents]

# FILE: [skill-name]/references/[reference-name].md

[full contents]
```

---

## THE REFACTORING PROCESS

When refactoring or creating a skill:
1. Read the full user request and any provided source material.
2. Decide whether the skill should be single-file or multi-file.
3. If single-file, use the existing lean `SKILL.md` structure. If multi-file, design the package architecture first (what lives in `SKILL.md` vs `references/`).
4. Write the activation description with triggers and exclusions.
5. Write imperative behavior instructions. Add reference loading rules if references exist.
6. Compress anti-patterns into a table.
7. Add output shapes and non-negotiable checklist.
8. Verify every reference has a loading rule, no reference is decorative, and the package preserves behavioral depth without bloating the main skill.

---

## ANTI-PATTERNS

| Anti-Pattern | What It Is | Fix |
| --- | --- | --- |
| Giant Skill File | Forcing a broad, complex skill into one huge `SKILL.md` | Move deep material into `references/`; keep `SKILL.md` as the command file |
| Decorative References | Creating reference files that do not serve a clear loading purpose | Create only references with specific triggers and use cases |
| Lost Depth Compression | Cutting examples, critique language, or frameworks that define behavior | Preserve behaviorally essential depth in references |
| Reference Without Routing | Creating references but not telling the main skill when to load them | Add explicit `REFERENCE LOADING RULES` |
| Manualized Reference | Writing references as human essays instead of AI-operational guidance | Use imperatives, diagnostics, frameworks, and decision rules |
| Over-Splitting | Creating too many tiny references with overlapping content | Merge related material into focused reference files |
| Under-Splitting | Creating one massive reference that hides multiple unrelated domains | Split by task, domain, or retrieval need |
| Token Bloat | Including full 100-line code templates directly in the skill text | Move templates to separate files and reference their paths |
| Double Negatives | "Do not avoid checking if tests are not failing" | Use positive commands: "Ensure tests pass before committing" |

---

## NON-NEGOTIABLE CHECKLIST

Before declaring a skill complete:
- [ ] Single-file vs multi-file decision was made intentionally.
- [ ] Multi-file package used when compression would damage behavior.
- [ ] Main `SKILL.md` stays activation-first and operational.
- [ ] Reference files contain deep supporting guidance, not duplicated main-skill content.
- [ ] Every reference has a clear loading rule in `SKILL.md`.
- [ ] No reference exists without a purpose.
- [ ] Behaviorally essential examples were preserved when needed.
- [ ] Size discipline did not destroy judgment, critique, or domain expertise.
- [ ] `description` field contains trigger phrases and explicit exclusions.
- [ ] All instructions are imperative (DO this, NOT "the expert does this").
- [ ] Anti-patterns are in a table, not individual prose blocks.
- [ ] `## OUTPUT SHAPE` section is present.
