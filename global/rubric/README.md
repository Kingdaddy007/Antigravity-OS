# README - RUBRICS FOLDER

**Location:** `.antigravity/rubric/`
**Layer:** Support-layer evaluation
**Loading Tier:** Tier 3 - on demand

---

## PURPOSE

Rubrics help Anti-Gravity judge output quality during critique, review, and explicit evaluation.

They are important, but they are **not part of the normal startup bundle**. They belong near the end of work, not the beginning.

If templates help Anti-Gravity shape output, rubrics help it judge whether that output is actually strong enough.

---

## WHEN TO LOAD RUBRICS

Load rubrics when:

- the task reaches critique or self-review
- the user explicitly asks for a review or assessment
- the work is high-stakes and needs a structured quality pass
- benchmark scenarios are being scored

Do not preload rubrics for ordinary execution.

---

## INVENTORY ROLE

Rubrics currently cover:

- code quality
- debugging quality
- architecture quality
- UX quality
- security quality
- communication quality
- testing quality
- performance quality
- API quality
- release readiness
- project planning quality

This folder remains in the OS, but as a support layer rather than a core day-one dependency.

---

## INTERACTION WITH OTHER FOLDERS

| Folder | Relationship |
| :--- | :--- |
| `workflows/` | workflows may invoke rubrics during critique |
| `skills/` | rubrics evaluate the output of skill-driven work |
| `global_templates/` | structured artifacts may be judged with a rubric |
| `benchmark/` | benchmarks use rubrics for scoring |
| `memory/` | repeated rubric failures may create useful memory entries |

---

## FINAL RULE

`rubric/` should make weak work harder to mistake for strong work, without turning every task into ceremonial box-checking.
