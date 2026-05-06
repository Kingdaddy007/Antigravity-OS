# README - MEMORY FOLDER

**Location:** `.antigravity/memory/`
**Layer:** Institutional learning
**Loading Tier:** Tier 3 - on demand

---

## PURPOSE

Memory is Anti-Gravity's retained learning layer. It keeps the system from restarting every hard lesson from zero.

This folder preserves:

- important decisions
- proven patterns
- repeated mistakes
- incidents and postmortems
- benchmark history
- system-version changes

Memory is first-class, but selective. It should be consulted when history changes the quality of the current decision.

---

## RUNTIME RECALL BEHAVIOR

Load memory only when it materially helps:

| Situation | File |
| :--- | :--- |
| A similar decision was made before | `decisions-log.md` |
| A reusable pattern may already exist | `common-patterns.md` |
| The area has known traps | `mistakes-to-avoid.md` |
| A similar incident happened before | `postmortems.md` |
| Evaluating OS changes | `benchmark-results.md` |
| Updating Anti-Gravity itself | `version-notes.md` |

Default rule:

- use workspace memory first for project work
- use global memory only for cross-project or system-level lessons

---

## AUTHORING AND ENTRY CONVENTIONS

Memory files are append-only logs. Add new entries; do not silently rewrite history.

A strong memory entry should include:

- date
- context
- conclusion or lesson
- why it mattered
- what to do differently next time

Memory should preserve judgment, not copy-paste project context.

---

## DIFFERENCE FROM CONTEXTS

| `contexts/` | `memory/` |
| :--- | :--- |
| current truth | accumulated learning |
| what is true now | what was learned over time |
| updated when reality changes | updated when lessons are earned |

---

## INTERACTION WITH OTHER FOLDERS

| Folder | Relationship |
| :--- | :--- |
| `contexts/` | contexts hold current truth; memory holds historical rationale and lessons |
| `workflows/` | workflows should trigger memory writes after meaningful decisions and incidents |
| `skills/` | recurring patterns or mistakes may suggest skill improvements |
| `benchmark/` | benchmark results are stored here for trend tracking |
| `rubric/` | rubric gaps discovered in practice can create new memory entries |

---

## MAINTENANCE

Review memory periodically for usefulness, but do not treat it like disposable scratch notes.

Good maintenance means:

- keeping entries specific
- avoiding duplicate noise
- moving stable current truth into contexts when appropriate
- preserving history instead of overwriting it

---

## FINAL RULE

Memory should make Anti-Gravity more experienced, not just more verbose.
