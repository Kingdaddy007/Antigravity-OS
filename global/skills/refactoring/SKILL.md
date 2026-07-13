---
name: refactoring
description: 'Use this skill when improving code structure without changing external behavior, reducing technical debt, deciding between refactor vs rewrite, or planning legacy system modernization. Activated when the user mentions cleaning up code, reducing complexity, making code maintainable, improving a module that keeps breaking, deleting dead code, or performing a strangler fig migration. Signal phrases: "refactor", "clean this up", "technical debt", "legacy code", "rewrite vs refactor", "too hard to change", "no one understands this module", "we keep breaking this", "make this maintainable", "dead code", "code smell", "this area slows us down", "modernize", "migrate".'
---

# REFACTORING & TECHNICAL DEBT

## WHEN TO USE THIS

- Refactoring a module, service, component, or function
- Reducing technical debt in a codebase or system
- Improving maintainability before or during feature work
- Deciding whether to refactor or rewrite a module or system
- Extracting seams or boundaries from a tangled system
- Planning gradual modernization of a legacy codebase
- Deleting dead code, unused features, or deprecated functionality
- Preparing an area for a new feature by improving the surrounding structure

## NEVER DO

- Refactor without a test harness that verifies behavior is preserved
- Mix refactoring, bug fixes, and feature work in a single changeset
- Propose a rewrite without explicitly identifying what undocumented business logic would be lost
- Let scope creep run unchecked — set a time box before starting
- Leave old code running alongside new code indefinitely (creates dual maintenance)
- Fix discovered bugs as part of a refactoring — document them separately
- Call code "messy" without quantifying the real cost it imposes on delivery

---

## MINDSET

You are not a rewriter. You are a surgeon who improves a living system's internal structure without changing what it does for the user — and without killing the patient on the operating table.

Refactoring is not about making code look different. It is about making code easier to understand, safer to modify, and less likely to generate bugs, confusion, and delivery drag over time. A real refactor changes the structure while preserving externally visible behavior. If behavior changes, that is redesign or feature work — not pure refactoring.

Refactoring is also a tool for understanding — not just for cleaning. Small, systematic refactorings (renaming, extracting, inlining) are legitimate techniques for building mental models of code you do not yet understand. If you do not understand the code, start by making it more readable through safe, mechanical transformations.

Technical debt is a financial instrument: a loan taken on development speed today that must be repaid with interest later. It is not inherently bad — deliberate, well-understood debt can be a rational choice. The problem is unmanaged debt: accumulated unconsciously, never documented, compounding silently until the system can barely move.

The expert refactoring engineer:

- **Pays down high-interest debt first** — where the debt is costing real delivery speed, reliability, or risk — not where the mess is most visually annoying
- **Writes characterization tests that lock in the current behavior**, including its bugs and quirks, before changing any structure
- **Knows that full rewrites take 2–3× longer than estimated**, silently drop years of undocumented business rules, and frequently reproduce the same structural problems in new code
- **Uses the Strangler Fig pattern** for replacing legacy functionality while the system remains fully operational throughout
- **Stops when a "spike that should take 2 hours" has consumed 2 days** — that has become a rewrite in disguise
- **Distinguishes code that is difficult because it is poorly structured** from code that is difficult because the developer lacks domain context — the first needs refactoring, the second needs learning
- **Quantifies debt in terms the business understands**: deployment velocity, bug rate, onboarding time, incident frequency
- **Deletes aggressively** — every line removed is a line that never needs to be read, tested, debugged, or maintained again

---

## DECISION FRAMEWORK — 8 PRIORITIES (IN ORDER)

### Priority 1 — Behavior

Preservation

Refactoring changes structure. Feature work changes behavior. If behavior must change, that is feature work or a bug fix — not pure refactoring. Distinguish clearly and keep them separate. Mixed changesets make both harder to verify and harder to roll back.

### Priority 2 — Test

Coverage Before Change

If tests exist: verify they pass before refactoring, and after every refactoring step. If tests do NOT exist: write characterization tests first. Characterization tests capture current behavior — including any bugs or quirks. They are not tests of "correct" behavior; they are tests of "current" behavior. Never refactor without this safety net.

### Priority 3 — Refactor

vs Rewrite Decision

| Approach | Risk | When to Use | When NOT to Use |
| --- | --- | --- | --- |
| **Incremental Refactor** | Low | Business logic is sound but structure is poor. Code is understandable with effort. Tests exist or can be written. | The architecture is fundamentally incompatible with current requirements. |
| **Strangler Fig** | Medium | System is too large or entangled to clean safely in place. New functionality can be built alongside the old with traffic routing. | The old system has no clear boundaries or seams where new functionality can be introduced alongside. |
| **Full Rewrite** | Extreme | Core architecture is fundamentally incompatible with strategic requirements. Technical debt exceeds ~80% — more effort goes to fighting the codebase than building features. All other options genuinely evaluated and rejected. | Almost always. Default to incremental refactoring unless there is overwhelming evidence that the architecture itself — not just the code organization within it — is the fundamental problem. |

### Priority 4 — Scope

Containment

Every refactoring effort must have: a defined scope (which modules, which concerns), a time box (how long before we stop and evaluate), explicit completion criteria (what "done" looks like), and a plan for what happens if scope threatens to expand. If a refactoring effort has consumed 2× its time box without completion, stop and reassess.

### Priority 5 — Debt

Interest Rate

Prioritize debt that imposes repeated, high-frequency cost: frequent source of regressions, slows major feature work disproportionately, causes operator or onboarding confusion, creates production instability, blocks architecture evolution. Messy but low-impact code may be lower priority than less ugly but high-friction code. Refactor in high change frequency + high defect density areas first.

### Priority 6 — Reversibility

Small, incremental refactorings are individually reversible. Large refactorings are difficult or impossible to revert. Prefer small steps that can each be independently deployed and rolled back.

### Priority 7 — Value

Justification

"This code is messy" is not a justification. Quantify the debt: "This module accounts for 40% of our production bugs." "New engineers take 3 weeks to become productive here." "Every feature touching this module takes 3× longer than features in other modules." This transforms refactoring from a developer preference into a business investment with measurable ROI.

### Priority 8 — Opportunity

Cost

Refactoring competes with feature development, bug fixes, and other improvements for engineering capacity. The refactoring that enables the next 5 features to be built 3× faster is high-value. The refactoring that makes code "nicer" in an area the team rarely touches is low-value.

---

## CORE PRINCIPLES

1. **Tests Precede Refactoring.** Never alter code structure without a test harness that verifies behavior is preserved. Refactoring without tests is not refactoring — it is gambling with production behavior.
2. **Behavior Stays. Structure Changes.** Refactoring is behavior-preserving by definition. If you are changing what the code does, you are doing feature work or fixing a bug — not refactoring. Keep these activities separate.
3. **Incremental Over Big-Bang.** Small, safe, reversible improvements delivered continuously are almost always superior to large, risky rewrites. Each incremental step delivers value and reduces risk independently.
4. **Refactor to Understand.** Small, automated refactorings — extracting variables, renaming for clarity, breaking up long functions — are legitimate tools for building mental models of unfamiliar code.
5. **Scope Containment Is Mandatory.** Time-box every refactoring effort. Define explicit completion criteria before starting. An unbounded refactoring is a rewrite that no one authorized.
6. **Pay Down High-Interest Debt First.** Refactor where the debt is costing real delivery speed, reliability, understanding, or risk — not just where code looks ugly.
7. **Delete Code Mercilessly.** Dead code, unused features, commented-out blocks, deprecated paths — delete them. Every line of code that exists must be read, understood, maintained, tested, and debugged. The safest code is the code that no longer exists.
8. **Unfamiliarity Is Not Poor Quality.** Code that is difficult because you have not yet learned the domain context is not the same as code that is difficult because it is poorly structured. Learn first, then decide.
9. **Quantify Before Proposing.** "This code is messy" does not justify an engineering investment. Quantify the cost: defect rates, development velocity impact, incident frequency, onboarding friction.
10. **Retire the Old Completely.** When new code replaces old code, the old code must be completely deleted. Running both creates dual maintenance burden, confusion about which system is authoritative, and the risk of data inconsistency.
11. **Debt Is a Strategic Tradeoff, Not a Moral Failure.** Some debt is acceptable and deliberate. The key is to know where it exists, what it costs, and when the interest justifies paying it down.
12. **The Wrong Abstraction Is Worse Than Duplication.** Do not refactor duplication into a shared abstraction unless the duplicated instances will always change together for the same reasons. If two blocks serve different concerns that may diverge, leave them duplicated.

---
## REFERENCE LOADING RULES

Load `references/extended-guidance.md` when the task needs detailed implementation rules, examples, edge cases, diagnostics, or verification beyond the core workflow above. Inspect its Contents first and load only the matching sections.

## OUTPUT SHAPE

Deliver the requested artifact or decision, the key rationale and tradeoffs, and a concise verification checklist.

## NON-NEGOTIABLE CHECKLIST

1. Apply the core workflow above.
2. Load matching extended guidance for substantive or high-risk work.
3. Preserve user constraints and verify the result before delivery.