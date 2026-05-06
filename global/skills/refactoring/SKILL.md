---
name: REFACTORING & TECHNICAL DEBT
description: >
  Use this skill when improving code structure without changing external behavior,
  reducing technical debt, deciding between refactor vs rewrite, or planning legacy
  system modernization. Activated when the user mentions cleaning up code, reducing
  complexity, making code maintainable, improving a module that keeps breaking,
  deleting dead code, or performing a strangler fig migration. Signal phrases:
  "refactor", "clean this up", "technical debt", "legacy code", "rewrite vs
  refactor", "too hard to change", "no one understands this module", "we keep
  breaking this", "make this maintainable", "dead code", "code smell", "this area
  slows us down", "modernize", "migrate". Also activate when repeated bugs originate
  from the same structural confusion. Do NOT mix refactoring (structure changes) with
  feature work or bug fixes in the same changeset — they must stay separate.
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

## REFACTORING LENSES

| Lens | What to Inspect |
| --- | --- |
| **Seam** | Where are the natural boundaries where new interfaces can be drawn? Can a subsystem be isolated behind a clean interface without modifying its internals? |
| **Change Frequency** | Which modules change most frequently? Which have the highest defect density? Where do developers spend the most time when building new features? Which areas generate the most merge conflicts? |
| **Friction** | Where does this code slow down future changes? What repeated complaints, regressions, or incidents point at hidden debt? What specific cost is this structure imposing, and how often does that cost recur? |
| **Boundary** | Are responsibilities mixed that should be separated? Is logic in the wrong layer? Are seams for extraction or modularization visible? |
| **Duplication** | Is knowledge duplicated, or just syntax duplicated? Are there multiple places that must change together for the same reason? Will the duplicated instances always change for the same reasons — or may they diverge? |
| **Behavior Safety** | What behavior must remain unchanged? What tests or checks prove that behavior is preserved? Are tests verifying behavior or implementation? (Implementation-coupled tests break on refactoring even when behavior is preserved.) |
| **Reversibility** | Can this be done in small, independently reversible steps? Can we pause or revert midway if a problem is discovered? What is the blast radius if a step introduces a bug? |
| **Debt Classification** | Is this deliberate debt or accidental (accumulated through neglect)? Is it prudent or reckless (shortcuts taken without understanding the cost)? Is it localized (one module) or systemic (spread across the codebase)? |
| **Deletion** | Can complexity be removed entirely, rather than rearranged? Is any code, configuration, or path still serving a real purpose? |
| **Business Value** | How does this refactoring enable future work? What features become possible or faster? Is the timing right — or would this block higher-priority work? |
| **Pattern** | Are there code smells (long parameter lists, primitive obsession, inappropriate intimacy, god functions)? Is a new pattern solving a concrete problem or being introduced for its own sake? |
| **Migration** | Can the Strangler Fig be applied? Are there seams where new functionality can be introduced alongside the old? Can traffic be gradually routed from old to new? Is there a clear decommissioning plan? |
| **ROI** | What will become cheaper, faster, or safer after this refactoring? What is the ongoing monthly cost of the debt vs the one-time cost to pay it down? |
| **Legacy** | Is this legacy area actually bad, or just unfamiliar to the current team? What undocumented business rules might be hiding inside it? What would be lost in a rewrite that would not be obvious until months later? |
| **Dependency** | What depends on this code? What does this code depend on? Are dependencies explicit and injectable, or implicit and global? Can the code be refactored in isolation, or must changes propagate to dependent systems? |

---

## BEHAVIORAL WORKFLOW

### Phase 1 — Understand

Identify what is being refactored and why. Distinguish: pure refactoring (structure only), feature work, or defect correction — do not mix them. Is this driven by measurable pain (production bugs, delivery velocity, difficult onboarding) or by aesthetic preference? Define explicit completion criteria and time box before starting.

### Phase 2 — Contextualize

Map the code: what does it do, what depends on it, what does it depend on? Assess current test coverage. Identify the seams — where can changes be introduced with minimal blast radius? Identify change frequency and defect density to confirm this area is worth refactoring.

### Phase 3 — Analyze

*For Debt Assessment:*

1. Identify the specific code smells and structural problems.
2. Classify the debt: deliberate vs accidental, prudent vs reckless, localized vs systemic, accruing vs stable.
3. Quantify the cost: defect rate attributable to this module, velocity impact, onboarding time, incident frequency.
4. Estimate the compound cost if the debt is not addressed in 6 months.
5. Estimate refactoring effort and compare to the ongoing cost of the debt.
6. Determine whether the debt should be: paid now / scheduled soon / consciously tolerated.

*For Refactor vs Rewrite Decision:*

1. Evaluate whether the business logic is sound but the structure is poor (→ incremental refactor).
2. Evaluate whether the system has identifiable seams and is too large to clean in place (→ Strangler Fig).
3. Evaluate whether the architecture is fundamentally incompatible with current requirements (→ consider rewrite as last resort).
4. For rewrite proposals: explicitly identify what undocumented business rules exist in the legacy code that would be lost.
5. For rewrite proposals: estimate the true duration (multiply the initial estimate by 2–3×).
6. Ask: "Am I advocating for a rewrite because the architecture is truly incompatible — or because I do not understand the code and want to start fresh?"

*For Scope Definition:*

1. Identify the minimum refactoring scope that addresses the core pain point.
2. Define clear boundaries: what is in scope and what is explicitly out of scope.
3. Plan the sequence: which refactorings should happen first to enable later ones?
4. Define checkpoints: at what points will we stop and verify before continuing?

### Phase 4 — Plan

Define the refactoring strategy (incremental, Strangler Fig, or rarely rewrite). Sequence the work into small, independently deployable steps. Define what characterization tests are needed before starting. Define the rollback path for each step. Set the time box and reassessment trigger.

### Phase 5A — Write Characterization Tests (first)

1. Write tests that capture the current behavior of the code being refactored.
2. Include happy path, error paths, edge cases, and any known quirks.
3. These tests verify CURRENT behavior — not CORRECT behavior. If the code has a bug users depend on, the characterization test should verify the bug exists.
4. Run all characterization tests — they must pass before any refactoring begins.
5. These tests are the safety net. Without them, refactoring is blind modification.

### Phase 5B — Incremental Refactoring (one safe transformation at a time)

1. **Rename** — Change names to accurately describe purpose. Safest refactoring — low risk, high readability gain.
2. **Extract** — Extract methods, functions, or classes to separate concerns. Reduces function size, improves testability.
3. **Inline** — Inline unnecessary abstractions that add indirection without value. Simplifies control flow.
4. **Move** — Move code to the module or layer where it belongs based on responsibility. Improves cohesion.
5. **Replace** — Replace complex conditional logic with simpler patterns (strategy, lookup tables, guard clauses).
6. **Delete** — Remove dead code, unused variables, commented-out blocks, deprecated paths.

After each transformation: run all tests → verify behavior is preserved → commit as an independent, revertable unit → do NOT combine multiple refactorings in a single commit.

**Preparatory Refactoring:** When a new feature is needed in an area with structural problems, the right sequence is: refactor first to make the area easy to modify, then add the feature in a separate commit. "Make the change easy (that may be hard), then make the easy change."

### Phase 5C — Strangler Fig Migration

1. **Identify the seam** — Find a boundary where new functionality can be introduced alongside the old.
2. **Build the replacement** — Implement the new component with its own tests, alongside the old system.
3. **Route a small percentage of traffic** — Monitor intensely. Compare outputs.
4. **Gradually increase traffic** — As confidence builds, route more traffic to the new component.
5. **Switch completely** — Route all traffic to the new component.
6. **Delete the old** — Remove the legacy code entirely. Do not leave it running "just in case."
7. **Repeat** — Identify the next seam and repeat for the next module.

At every stage: the system is fully operational. Each stage can be individually rolled back. The old system remains available until the new is fully validated.

### Phase 5D — Handling Scope Creep

When scope threatens to expand: stop and document what was discovered, complete the current scoped refactoring first, log the discovered debt for future prioritization, and define whether it is blocking the current scope or independent. If blocking, redefine scope explicitly with stakeholder awareness — do not silently expand.

### Phase 5E — Handling Discovered Bugs

Do NOT fix the bug as part of the refactoring. Document it separately with reproduction steps. Complete the refactoring with the bug still present. Fix the bug as a separate, subsequent change with its own tests. Mixing bug fixes with refactoring makes both harder to verify and harder to roll back.

### Phase 6 — Verify

Run all characterization tests, all unit and integration tests — they must all pass. Verify no external behavior has changed (API responses, UI behavior, data outputs). For Strangler Fig: compare old and new system outputs for the same inputs. Verify scope was maintained — no unplanned changes introduced. Check for regressions in adjacent code.

### Phase 7 — Critique

Is the refactored code easier for a new developer to understand than the original? Did we stay in scope? Was all old code deleted — or is dual maintenance now silently running? Was the refactor worth the cost — did it reduce the debt that justified starting it?

### Phase 8 — Communicate

Document what was refactored and why — the structural goal, not just the mechanics. Document what behavior was preserved and how it was verified. Document any discovered bugs or additional debt that was found but not addressed. Document what code was deleted and why.

### Pre-Finalization Re-Check

- The structural goal was clear and the debt being paid down was real, not cosmetic
- Behavior was preserved or any behavior change was explicitly separated and scoped
- The result is genuinely easier to change, understand, or support than before
- The work did not quietly become an uncontrolled rewrite
- Old code has been deleted — no dual maintenance has been created

---

## KEY DIAGNOSTIC QUESTIONS

**The Pain Check** — What specific cost is this code imposing today, and how often do we pay that cost?

**The Quantification Check** — Can I express the cost of this debt in terms the business understands — bug rates, delivery velocity, incident frequency, onboarding time — or am I only expressing aesthetic irritation?

**The Familiarity Check** — Is this code difficult because it is poorly structured, or because I do not yet understand the domain? Am I trying to improve the code — or to escape having to understand it?

**The Safety Check** — What protects existing behavior while this change is made? If the answer is "nothing," the first step is writing characterization tests, not starting the refactor.

**The Rewrite Check** — Am I improving structure, or am I secretly trying to rewrite because the old code frustrates me? What undocumented business rules exist in the legacy code that would be lost in a rewrite? How long do I estimate this will take — and what is that estimate multiplied by 2–3×?

**The Leverage Check** — Which single structural improvement would remove the most future friction? What is the smallest refactoring scope that materially helps?

**The Scope Check** — Is this the smallest refactor that materially helps, or am I widening the work because "while we're here…" feels tempting? What is the time box — and am I still within it?

**The Coupling Check** — Did this refactor actually reduce dependency entanglement, or only rename the problem?

**The Clarity Check** — Would another engineer understand this system faster after the change? Is the refactored code genuinely clearer, or just different?

**The Debt Residue Check** — What important debt still remains after this refactor? Has the partial cleanup been honestly acknowledged, or is it being treated as full resolution?

**The Retirement Check** — Has all old code been deleted — or is dual maintenance now silently running? Is there a clear decommissioning plan?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| --- | --- | --- | --- |
| **The Big Bang Rewrite** | "This codebase is too messy to fix. Let's rewrite from scratch." Team spends 6 months. Rewrite takes 3× longer. Silently drops 30% of undocumented business rules. Users report dozens of missing behaviors on launch. | Rewrites carry catastrophic business risk. The old codebase contains years of accumulated bug fixes, edge case handling, and business rule implementations — much of it undocumented. Delivers zero user value during development. Frequently reproduces the same structural problems. | Use the Strangler Fig pattern. Incrementally replace functionality. Keep the old system running. Migrate gradually. Delete the old code only after the new is fully proven. |
| **Refactoring Without Tests** | "I'll just clean up this module quickly." Discovers days later that a subtle behavior change broke a downstream consumer. No tests to catch it. | Without tests, there is no way to verify behavior was preserved. Subtle changes slip through undetected. | Write characterization tests before refactoring. Run them after every transformation. |
| **Scope Creep Refactor** | Cleaning up the auth module, noticed the user service could use improvement, then the notification system, now restructuring the data access layer. 2 hours → 2 weeks, 47 files touched. | Unbounded refactoring is a rewrite in disguise. Each expansion increases blast radius. The changeset becomes too large to meaningfully review or roll back. | Define scope before starting. Set a time box. Document discovered debt for future prioritization — do not address it mid-flight. |
| **The Cosmetic Refactor** | Large formatting, renaming, and file-layout changes presented as debt reduction — without improving coupling, duplication, complexity, or change friction. The diff is large. The structural improvement is zero. | Consumes review time and risk budget without meaningful leverage. Creates the feeling of progress without the substance of it. | Tie refactor work to actual structural or maintenance improvement. Refactor only when the structure becomes meaningfully easier to understand or change. |
| **The Wrong Abstraction** | Removing duplication by introducing a generalized abstraction harder to understand than the original — or forcing two concerns that will later diverge into the same place. | The system becomes more rigid and more cognitively expensive. The wrong abstraction creates coupling that is harder to undo than the duplication it replaced. | Favor clarity over DRY. Abstract only when the pattern is real, stable, and represents the same thing changing for the same reason. |
| **Rewrite as Avoidance** | Team calls for a rewrite because understanding the current code feels hard and writing new code feels easier. Real problem is lack of domain context — not poor architecture. | The rewrite destroys years of embedded knowledge — bug fixes, edge cases, real-world accommodations — while the team rebuilds them more slowly and less completely from memory. | Before any rewrite proposal, explicitly ask: "Am I advocating for a rewrite because the architecture is fundamentally incompatible — or because I do not understand the existing code?" If the latter, learn first. |
| **Mixed Purpose Commits** | A single changeset combines refactoring, bug fixes, and new feature additions. Reviewer cannot determine what is structure-only and what is behavior-changing. | Makes both the refactoring and the feature work harder to review, verify, and roll back independently. | Use Preparatory Refactoring — refactor first, then add the feature in a separate commit. |
| **Debt Without Economics** | Technical debt discussed in terms of code quality, aesthetics, or engineering frustration — but never in concrete, recurring cost terms. | Without economic framing, debt cannot be prioritized against feature work. It remains an emotional discussion rather than a business decision. | Name the debt in terms the business understands. Quantify it. How often does it hurt, how badly, and what does it block? |
| **The Zombie Legacy** | New code has replaced the old system. Migration is complete. But the old system is still running "just in case" — alongside the new one, indefinitely. Both being maintained. | Dual maintenance burden grows over time. Data may diverge. Teams stop knowing which path is canonical. The "just in case" justification never expires on its own. | Once the new system is validated, decommission the old one completely. A Strangler Fig migration is not complete until the old system is dead. |
| **Confusing Unfamiliarity With Poor Quality** | Developer joins a new codebase, finds it hard to understand, and concludes it needs to be refactored or rewritten. Code is not poorly structured — developer simply lacks domain context. | Refactoring legitimately complex domain code can remove essential complexity and introduce bugs. The refactorer destroys embedded knowledge they did not know existed. | Invest time in understanding the domain before proposing structural change. Use small mechanical refactorings as a learning tool first. |
| **The Debt Denial Loop** | Teams repeatedly work around the same pain point — writing workarounds, patching symptoms, avoiding the area — but never treating it as debt worth paying down. The pain compounds silently. | The interest rate on the debt keeps accruing. The team normalizes the pain and stops questioning it. | Name recurring pain as debt and evaluate whether the interest now justifies targeted payoff. Make the cost explicit so it can be prioritized. |

---

## OUTPUT SHAPE

```markdown

## Debt Assessment

- Specific structural problem and where it lives
- Debt classification: deliberate/accidental, localized/systemic, accruing/stable
- Quantified cost: defect rate, velocity impact, onboarding friction, incident frequency
- Compound cost in 6 months if not addressed
- Recommended action: pay now / schedule / tolerate consciously

## Refactoring Plan

- Strategy: incremental refactor / Strangler Fig / (rarely) rewrite with justification
- Scope boundary: what is in scope, what is explicitly out
- Sequence: ordered steps, each independently deployable
- Time box and reassessment trigger
- Characterization test plan
- Rollback path

## Post-Refactor Summary

- What was refactored and the structural goal
- Behavior preserved and how it was verified
- What was deleted
- Discovered debt not addressed (for future prioritization)
- Structural improvement delivered

```

---

## NON-NEGOTIABLE CHECKLIST

### Before Starting

- [ ] The debt cost is quantified in measurable terms — not just "it's messy"
- [ ] The scope is defined with explicit boundaries (what is in scope, what is out)
- [ ] The time box is set with a reassessment trigger
- [ ] Completion criteria are defined (what "done" looks like)
- [ ] The refactor-vs-rewrite decision has been explicitly evaluated
- [ ] The code's difficulty has been assessed: poor structure vs missing domain understanding

### Test Coverage

- [ ] Characterization tests exist that verify the current behavior of the code being refactored
- [ ] All tests pass before refactoring begins
- [ ] Tests are run after every individual transformation — not just at the end

### During Execution

- [ ] Each transformation is committed independently and is individually revertable
- [ ] Refactoring, bug fixes, and feature work are kept in separate changesets
- [ ] Discovered bugs are documented separately and fixed in separate changesets
- [ ] Discovered scope creep is documented for future prioritization — not addressed mid-flight

### After Completion

- [ ] All tests pass — characterization tests, unit tests, integration tests
- [ ] External behavior is verified unchanged
- [ ] All old code has been deleted — no dual maintenance
- [ ] The code is genuinely easier to understand or change than the original
- [ ] Discovered debt and follow-up work have been documented

### For Strangler Fig Migrations

- [ ] The old system remains fully operational throughout the migration
- [ ] Traffic routing between old and new is controllable and reversible at every stage
- [ ] The old system is completely decommissioned after migration is validated

---

**Final Rule:** Refactoring changes structure. Never behavior. The surgeon's goal is to leave the patient healthier — not to perform surgery for its own sake. Before cutting, know what you are preserving. After cutting, verify it is still there.
