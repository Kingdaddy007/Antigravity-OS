# MEMORY: VERSION NOTES

**Version:** Gold v1.0
**Layer:** 12 — Institutional Learning
**Tier:** 3 — Loaded on demand
**File:** memory/version-notes.md
**Purpose:** Tracks changes to the Anti-Gravity system itself — when core files, skills, workflows, contexts, rubrics, or benchmarks are updated, and WHY. This is the changelog for the cognitive operating system.
**Loaded When:** Updating Anti-Gravity system files. Reviewing system evolution. Diagnosing behavioral changes. Understanding why the system behaves differently than expected. Onboarding to understand how the system evolved.
**Format:** Append-only. Every significant system change gets a timestamped entry.

---

## WHEN TO ADD AN ENTRY

Add an entry when:

- Any file in the Anti-Gravity system is created, updated, or deprecated
- A new skill, workflow, context, rubric, template, or benchmark is added
- An existing file is significantly revised — not just formatting
- The master system prompt is updated
- A behavioral change is deliberately introduced
- A naming or structure shift affects multiple files or layers
- A major layer completion or system milestone is reached

Do NOT log:

- Typo fixes or minor formatting changes
- Context file updates — those are project changes, not system changes
- Memory file entries — the entries themselves are the record
- Every tiny edit — only changes with orientation or behavioral value
- Raw commit-style noise with no milestone significance

---

## HOW TO USE THIS FILE

Anti-Gravity should consult this file when:

- Diagnosing why behavior changed between versions
- Understanding what a system change was intended to improve
- Reviewing the evolution rationale before re-opening a settled change
- Interpreting benchmark results in the context of recent changes

If the system changes in a way that should affect behavior, quality, or load strategy, it belongs in this file. Untracked evolution becomes forgotten drift.

---

## ENTRY FORMAT

[YYYY-MM-DD] — [Change Title]

### Version

[Gold vX.Y]

### What Changed

[Which files were modified and what specifically changed — at a level that helps future readers understand the scope]

### Why

[What motivated this change? Problem observed, improvement identified, benchmark result, user feedback, or structural weakness discovered?]

### Expected Improvement

[What was this change trying to improve in behavior, quality, or system structure?]

- [improvement 1]
- [improvement 2]

### Known Risks or Limitations

[What might have worsened or still needs testing after this change?]

- [risk or open concern 1]
- [risk or open concern 2]

### Impact

[How does this change Anti-Gravity's behavior? What will be different? What should be tested after this change?]

### Files Affected

- [file path 1] — [created / updated / deprecated]
- [file path 2] — [created / updated / deprecated]

### Related Files / Areas

- [benchmark / postmortem / ADR / skill / workflow that motivated this]

### Tags

`#core` `#skill` `#workflow` `#context` `#rubric` `#benchmark` `#master-prompt` `#milestone` `#architecture-decision`

---

## QUALITY BAR FOR ENTRIES

A strong entry:

- Captures a meaningful failure or near-miss with real structural learning
- Uses the 5 Whys to reach structural and systemic causes, not just the surface event
- Extracts a reusable lesson that changes future behavior or design
- Produces specific, owned, deadlined action items
- Is blameless — focuses on what the system allowed, not who failed

A weak entry:

- Is mostly narrative with no extractable lesson
- Stops at the surface cause without asking why the system allowed it
- Focuses on blame instead of structural improvement
- Has no action items, or action items too vague to execute
- Records something too small or trivial to warrant a postmortem

---

## USAGE RULES

1. Record significant system-level changes, not minor drafting edits.
2. Keep rationale visible — this is a changelog for the cognitive operating system, not a file diff.
3. Use this file to support benchmark interpretation across versions.
4. If a change introduced a regression or open concern, note it honestly.
5. Most recent entries appear at the top.

---

## EXAMPLE ENTRIES

### 2024-06-15 — Anti-Gravity Gold v1.0 Initial Build Complete

**Version:** Gold v1.0

**What Changed:** Complete cognitive operating system built from initial design:

- 9 core files — Layers 1 through 4 plus governance
- 14 skill files — Layer 5
- 12 context file templates — Layer 6
- 10 workflow files — Layer 8
- 6 output templates — Layer 9
- 10 rubrics — Layer 10
- 7 benchmark files — Layer 11
- 6 memory file templates — Layer 12
- 8 folder READMEs
- 1 master system prompt

**Why:** Transition from ad-hoc prompting to a structured cognitive operating system. Problems addressed: weak reasoning shape, mode confusion, lack of governing principles, no skill orchestration, no self-evaluation capability.

### Expected Improvement

- Repeatable, principled behavior across task types
- Explicit operating modes that reduce posture confusion
- Systematic execution workflows that prevent premature implementation
- Self-evaluation capability through rubrics
- Improvable behavior through benchmarking

### Known Risks or Limitations

- Initial Gold v1.0 has not been fully benchmarked
- Context file templates require user population before grounding value is realized
- Benchmark files are not yet built — placeholder layer

**Impact:** Anti-Gravity now operates with defined identity, structured thinking, explicit operating modes, systematic execution, and self-evaluation. Behavior is repeatable and measurable for the first time.

### Files Affected

- All files — created

### Related Files / Areas

- benchmarks/ — to be built in a follow-on phase

**Tags:** `#core` `#skill` `#workflow` `#context` `#rubric` `#benchmark` `#master-prompt` `#milestone`

### 2024-07-01 — Layer 3 Redesigned: Mental Models Replaced with Meta-Cognitive Safeguards

**Version:** Gold v1.0 (refinement)

**What Changed:** Renamed `senior-engineer-mental-models.md` to `expert-cognitive-patterns.md`. Replaced ten mental models — which overlapped significantly with Layer 2's twelve thinking dimensions — with six meta-cognitive safeguards: Nonlinearity, Gray Thinking, Occam's Bias, Framing Bias, Anti-Comfort, and Delayed Discomfort. Also added Decision Classification and Probabilistic Thinking.

**Why:** Ten of the original mental models were reformulations of concepts already present in Layer 2. The same ideas appeared twice in the always-loaded tier, consuming context window space for zero additional value. The new structure addresses a genuinely different cognitive level: Layer 2 defines WHAT to think about. Layer 3 now defines HOW to guard the thinking process against reasoning errors.

### Expected Improvement

- Zero overlap between Layer 2 and Layer 3
- Layer 3 now catches thinking errors rather than duplicating thinking dimensions
- Each always-loaded file has a distinct and non-redundant function

### Known Risks or Limitations

- Behavioral change has not been benchmarked yet
- Some engineers may expect "mental models" language and not find it

**Impact:** Layer 3 now functions as a genuine meta-cognitive layer. Redundancy in the always-loaded core is eliminated. Context window efficiency improves for tasks where both layers were previously loaded.

### Files Affected

- core/expert-cognitive-patterns.md — created
- core/senior-engineer-mental-models.md — deprecated

**Tags:** `#core` `#architecture-decision` `#layer-3`

---

## ENTRIES

<!-- Append new entries below this line. Most recent at the top. -->
