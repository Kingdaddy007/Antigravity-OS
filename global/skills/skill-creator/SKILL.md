---
name: skill-creator
description: >
  Use this skill when you need to CREATE or REFACTOR a skill file for the
  Anti-Gravity OS. Activated when the user asks to "build a new skill",
  "reformat a skill", "compress a skill", "apply the skill creator", or
  "update [skill name] to the new format". Also activated at the start of
  Phase 6 (skill refactoring) of the OS optimization plan. Produces lean,
  token-efficient SKILL.md files using the high-density truth-document format.
---

# Skill Creator — Anti-Gravity OS

Build every Anti-Gravity skill as a **truth document**: dense, imperative, activation-first.
Never write a manual. Never explain the skill to a human reader. Write instructions for an AI.

---

## THE FORMAT CONTRACT

Every skill must follow this exact structure:

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

## [DOMAIN SECTION 2]

...

## OUTPUT SHAPE

[What a response looks like when this skill is active. Mode-specific template.]

## NON-NEGOTIABLE CHECKLIST

[Short numbered list. Verify before delivery.]
```text

---

## THE RULES

### Rule 1 — The description field IS the activation trigger

This is the most important field. It determines when the skill loads.

### Bad (current pattern)

```yaml
description: Domain knowledge for IMPLEMENTATION & CODING
```text

### Good (Anthropic pattern)

```yaml
description: >
  Use this skill when writing, modifying, or generating code. Activated when
  the user asks to build features, implement functions, create components,
  write endpoints, refactor code, or produce any working implementation.
  Examples: "build this", "write the code", "create a function that...",
  "implement the endpoint", "wire this together", "update this code to...".
  Do NOT use for architecture decisions (use architecture skill) or
  pure debugging (use debugging skill).
```text

The description must:

- State explicitly WHEN to load (trigger words + example phrases)
- State explicitly WHEN NOT to load (neighboring domains)
- Be specific enough that a routing system can activate it correctly without reading the whole file

### Rule 2 — Instructions only. No meta-commentary

Cut everything that exists to explain the skill's purpose, history, version, or relationship to other files.
An AI does not need to be told why a file exists. It needs to be told what to do.

### Cut

- `## ROLE OF THIS FILE` sections
- `## FILE RELATIONSHIPS` tables
- `## VERSION HISTORY` tables
- `**Inherits From:**` header fields
- `**Status:** ALWAYS LOADED` declarations
- Any section that starts with "Without this file, Anti-Gravity would..."

### Keep

- Everything that tells the AI what to DO
- Checklists
- Priority orders
- Decision frameworks
- Output templates
- Hard boundaries ("never do X")

### Rule 3 — Imperative, not declarative

**Declarative (wrong):** "The expert coder treats readability as the highest implementation virtue."
**Imperative (right):** "Prioritize readability. If the code requires a comment explaining WHAT it does, rename until the name makes it obvious."

Every sentence should be an instruction, not a description of the desired identity.

### Rule 4 — Cut verbose examples. Keep the rule

Examples in skills are the biggest token sink. They have almost zero behavioral delta.

### Before (6 lines, minimal value)

```typescript
// ❌ Bad
const d = getD();
if (d > 30) handleExp();

// ✅ Good
const daysSinceLastLogin = getDaysSinceLastLogin(user);
```text

### After (1 line, same behavioral signal)

`Use names that state business intent: \`daysSinceLastLogin\` not \`d\`, \`handleAccountExpiration\` not \`handleExp\``

Keep examples ONLY when the concept is genuinely hard to express in a rule. Maximum 1 example per concept.

### Rule 5 — Compress anti-patterns into a table

### Before (10-line anti-pattern block)

```text

### The Cleverness Trap

What it looks like: One-liner chains...
Why it is harmful: Every future reader pays the cognitive tax...
What to do instead: Write the obvious, explicit version...
```text

### After (1 table row)

| Anti-Pattern | What It Is | Fix |
| --- | --- | --- |
| Cleverness Trap | Nested ternaries, bitwise tricks, compressed chains | Write the obvious version. Lines are free. |

### Rule 6 — Size target

| Skill Type | Target Size | Max |
| --- | --- | --- |
| Narrow domain (context-hygiene, context-formatting) | < 3KB | 4KB |
| Standard domain (debugging, review, research) | 3–6KB | 8KB |
| Broad domain (coding, architecture, security) | 6–10KB | 12KB |
| Complex domain (api-design, database, product-thinking) | 8–12KB | 15KB |

If the skill exceeds the max: cut examples first, cut anti-pattern prose second, compress output templates third.

### Rule 7 — The output shape section is mandatory

Every skill must define what a response looks like when it's active.
This replaces the verbose mode-output-templates that lived in `communication-standards.md`.

Example for a coding skill:

```text

## OUTPUT SHAPE

**Simple implementation:** Approach (1-2 sentences) → Code → What to verify
**Moderate implementation:** Objective restatement → Approach + rationale → Code → Assumptions → Edge cases → What to verify
**Complex implementation:** All of the above + Key decisions explained + Testing recommendations + Next steps
```text

---

## THE REFACTORING PROCESS

When refactoring an EXISTING skill:

1. **Read the whole file first.** Identify the 20% that contains behavioral signal. Mark it.
2. **Write the new description field.** Long, specific, with trigger phrases and exclusions.
3. **Extract the behavioral core.** Keep: priority orders, checklists, decision frameworks, hard boundaries. Cut: narrative prose, verbose examples, meta-commentary, file relationship tables, version history.
4. **Rewrite in imperative voice.** Every section = instructions. Not descriptions.
5. **Compress anti-patterns into a table.** One row per anti-pattern.
6. **Add output shape section.** Define what responses look like when this skill is active.
7. **Check size.** Must be within target for the skill type.
8. **Overwrite the file.** Save to the same path. This is not a draft.

---

## NON-NEGOTIABLE CHECKLIST

Before declaring a skill complete:

- [ ] `description` field contains trigger phrases and explicit exclusions
- [ ] No `## ROLE OF THIS FILE`, `## FILE RELATIONSHIPS`, or `## VERSION HISTORY` sections
- [ ] All instructions are imperative (DO this, NOT "the expert does this")
- [ ] Anti-patterns are in a table, not individual prose blocks
- [ ] At most 1 example per concept — zero examples if the rule is self-evident
- [ ] `## OUTPUT SHAPE` section is present
- [ ] `## NON-NEGOTIABLE CHECKLIST` is present
- [ ] File size is within the target range for this skill type
- [ ] The file reads like instructions to an AI, not a document for a human
