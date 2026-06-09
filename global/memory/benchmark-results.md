# MEMORY: BENCHMARK RESULTS

**Version:** Gold v1.0
**Layer:** 12 — Institutional Learning
**Tier:** 3 — Loaded on demand
**File:** memory/benchmark-results.md
**Purpose:** Tracks Anti-Gravity's performance scores over time. Proves or disproves that the system is improving. Identifies areas of persistent weakness. Connects benchmark tasks to versioned, comparable evidence.
**Loaded When:** Running benchmark tests. Evaluating system effectiveness. Deciding which skills or workflows need improvement. Comparing before and after a system change.
**Format:** Append-only. Each benchmark run is a timestamped entry.

---

## WHEN TO ADD AN ENTRY

Add an entry when:

- Running any benchmark scenario from the `benchmarks/` folder
- Comparing Anti-Gravity's performance before and after a system change
- Completing a monthly or quarterly evaluation run
- A capability area shows persistent weakness that should be tracked
- An upgrade or change to core, skills, or workflows is being validated

---

## WHAT THIS FILE ANSWERS

- Is Anti-Gravity actually improving over time?
- Which capabilities are getting stronger?
- Which capabilities remain persistently weak?
- Did a specific change to core, skills, or workflows produce a measurable improvement?
- What regressions appeared after a system change?
- Which benchmark areas show the most consistent gaps?

Benchmark results should create a history of evidence, not a history of vague impressions.

---

## ENTRY FORMAT

[YYYY-MM-DD] — Benchmark Run: [Category]

### System State

- **Anti-Gravity version:** [Gold v1.X]
- **Skills loaded:** [which skills were active]
- **Contexts loaded:** [which contexts were populated]
- **Recent system changes:** [any recent updates to skills, workflows, core files, or contexts]
- **Scenario:** [Scenario Name from benchmarks/ file]

| Dimension | Score | Notes |
| --- | --- | --- |
| [Dimension 1] | [Excellent / Acceptable / Needs Work / Failing] | [Observation] |
| [Dimension 2] | [Score] | [Notes] |
| [Dimension 3] | [Score] | [Notes] |

### Overall Assessment

[Summary — what went well, what needs improvement, whether overall quality is trending up or down relative to previous runs]

### Comparison to Previous Run

[Better / Same / Worse than last time? In which specific dimensions? First run if no prior comparison is available.]

### Improvement Actions

- [Specific changes to make based on this result — which files to update, which behaviors to strengthen]

Tags: #feature-build #debugging #architecture #review #ui-ux #api #devops

---

## QUALITY BAR FOR ENTRIES

A strong entry:

- Records results with enough detail that future comparisons stay meaningful
- Explains why a result matters — not just what the score was
- Identifies the likely cause of improvement or weakness
- Produces specific improvement actions, not vague observations
- Preserves results with future decision value
- Links back to the benchmark file and scenario used

A weak entry:

- Stores isolated scores with no context or trend
- Duplicates benchmark definitions instead of recording results
- Produces no comparison to prior runs
- Has no improvement actions — "good job" with no follow-through
- Records a synthetic win later found to be meaningless

---

## USAGE RULES

1. Log benchmark results after meaningful version or system changes.
2. Compare against previous runs when prior runs exist.
3. Be specific about what improved or regressed and in which dimensions.
4. Tie observations back to changes in:
   - Core files
   - Skills
   - Workflows
   - Contexts
5. Use this file to guide refinement, not just to celebrate improvement.
6. Most recent entries appear at the top.

---

## EXAMPLE ENTRY

2024-06-01 — Benchmark Run: Feature Building

### System State (Example)

- **Anti-Gravity version:** Gold v1.0
- **Skills loaded:** skill-coding, skill-product-thinking, skill-architecture
- **Contexts loaded:** stack-context, architecture-context, coding-standards
- **Recent system changes:** Initial Gold v1.0 deployment
- **Scenario:** Simple CRUD Feature — tags on tasks

| Dimension | Score | Notes |
| --- | --- | --- |
| Correctness | Excellent | Proper relational model, validation, edge cases handled |
| Readability | Excellent | Clear naming, focused functions |
| Error Handling | Acceptable | Happy path and main errors covered, minor edge gaps |
| Convention Compliance | Excellent | Matched existing patterns throughout |
| Security | Acceptable | Input validated, auth checked |
| Simplicity | Excellent | No over-engineering |
| Testability | Acceptable | Tests suggested but not fully specified |

### Overall Assessment (Example)

Strong performance on the CRUD feature. Product thinking — asking clarifying questions before building — was excellent. Slight gap in test specification depth: suggested what to test but did not provide specific test structure or examples.

### Comparison to Previous Run (Example)

First benchmark — no comparison available. Establishing baseline.

### Improvement Actions (Example)

- Strengthen skill-coding workflow to produce more specific test recommendations — not just what to test but how to structure the tests
- Consider adding a test-writing step explicitly to the build-feature workflow checklist

Tags: #feature-build #benchmark-baseline

---

## TRACKING DASHBOARD

Use this table to track scores across runs at a glance:

| Date | Category | Scenario | Overall | Weakest Dimension | Trend |
| --- | --- | --- | --- | --- | --- |
|||||||
> Fill this in as benchmark results accumulate. Use it to spot persistent weaknesses and verify improvement trends.

---

## ENTRIES

<!-- Append new entries below this line. Most recent at the top. -->
