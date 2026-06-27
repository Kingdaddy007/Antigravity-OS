# FIRST PRINCIPLES — ASSUMPTION DESTRUCTION PROTOCOL

**Load when:** Evaluating "the way we always do it," choosing between inherited approaches, challenging foundational assumptions, designing from scratch, or when the user explicitly asks for first-principles reasoning.
**Companion:** `system-thinking.md` (WHAT to examine), `expert-cognitive-patterns.md` (HOW to guard thinking). This file: WHERE truth begins — strip everything back to provable bedrock and rebuild upward.

---

## THE ASSUMPTION AUDIT

Every decision rests on assumptions. Most assumptions are inherited, not verified. The audit makes them visible.

### The Protocol

1. **LIST** every assumption — not just constraints, ALL assumptions. Include assumptions about the user, the environment, the technology, the timeline, and the problem definition itself.
2. **CLASSIFY** each assumption:
   - **Verified Truth** — provably true, empirically confirmed, or mathematically certain
   - **Inherited Convention** — "everyone does it this way" but no one can explain why from bedrock
   - **Untested Belief** — assumed true because it feels right, was told once, or was never questioned
3. **STRIP** away inherited conventions and untested beliefs. What remains that is provably true?
4. **ASK "WHY?"** recursively for each remaining element until you hit bedrock — a truth that cannot be decomposed further.
5. **REBUILD** solutions upward from verified truths only — not sideways from analogies, not downward from conclusions.

### Bedrock Recognition

You have reached bedrock when:

- The statement is provably true without depending on another unverified assumption
- It cannot be decomposed into smaller claims that might independently be false
- Removing it would make the problem undefined or physically impossible
- It holds regardless of implementation choice, framework, or convention

You have NOT reached bedrock when:

- The statement relies on "industry best practice" without explaining why the practice exists
- The justification is "that's how [respected source] does it"
- The truth depends on a specific technology, vendor, or paradigm that could be swapped
- You stopped asking "why?" because the answer felt obvious — obviousness is the enemy

---

## CONVENTION vs TRUTH SEPARATION

Most engineering "truths" are conventions. Conventions are useful — but they are not load-bearing. Building on a convention as if it were truth creates invisible fragility.

| Category | Signal | Example |
| :--- | :--- | :--- |
| **Verified Truth** | Provable, testable, holds across contexts | "This data must be consistent because concurrent writes will corrupt it" |
| **Inherited Convention** | Widely practiced but origin unknown | "We always put auth in middleware" |
| **Untested Belief** | Assumed true, never challenged | "Users won't need more than 100 items" |
| **Expired Truth** | Was true once, conditions changed | "We can't do that — the old API didn't support it" |

### The Expired Truth Trap

The most dangerous category. It was once verified, so it carries authority. But the conditions that made it true have changed. Ask: "Is this still true TODAY, or is this a fossil from a past constraint?"

---

## THE ANALOGICAL REASONING TRAP

First-principles thinking exists because analogical reasoning fails silently.

**Analogical reasoning:** "X worked for Company A, so it will work for us."
**First-principles reasoning:** "What specific conditions made X work for A? Do those conditions exist here? What conditions exist here that did NOT exist for A?"

### When Analogies Break

| Analogy Pattern | Why It Breaks | First-Principles Fix |
| :--- | :--- | :--- |
| "Netflix does X" | Different scale, constraints, team, budget | Identify YOUR constraints and design for them |
| "It worked on Project Y" | Different users, data shape, access patterns | Verify the shared assumptions actually hold |
| "The docs recommend X" | Docs assume the common case — you may be the edge case | Check whether your use case matches the doc's assumptions |
| "Everyone uses X library" | Popularity ≠ fit. Survivorship bias. | Ask what X solves, whether you have that problem, what X costs |

### The Borrowing Rule

Borrowing a solution is not forbidden. But every borrowed solution carries hidden assumptions from its origin. Before importing a solution, explicitly list what it assumes about your problem. If any assumption is wrong, the solution is wrong — even if it "works" superficially.

---

## THE RECONSTRUCTION PROTOCOL

After stripping to bedrock, rebuild deliberately:

1. **State the bedrock truths.** What is provably, irreducibly true about this problem?
2. **Derive the constraints.** From the truths, what limits exist? What MUST be true for any solution?
3. **Generate options from constraints.** What solutions are possible given ONLY the bedrock truths and derived constraints — ignoring all conventions?
4. **Evaluate against reality.** Now reintroduce practical constraints (time, team, budget). Which first-principles solutions are feasible?
5. **Compare with convention.** Does the conventional approach match your first-principles answer? If yes — use it (convention has ecosystem benefits). If no — you've found a structural advantage. The unconventional path may be correct.

### The Convention Reconciliation Rule

When your first-principles answer AGREES with convention → use convention (you get ecosystem, documentation, community for free).

When your first-principles answer DISAGREES with convention → you've found either a genuine insight or a gap in your analysis. Double-check your bedrock. If it holds, trust it over convention. Document why you diverged.

---

## THE SACRED COW DETECTOR

Sacred cows are decisions that persist because no one questions them. They accumulate in every codebase, team, and architecture.

### Detection Signals

- "We've always done it this way"
- "That's just how [framework/language] works" (often false — it's how the TUTORIAL did it)
- Nobody can name the original decision-maker or the context of the decision
- The decision predates the current team
- Questioning it triggers emotional resistance rather than technical arguments
- The justification is authority-based ("the architect decided") rather than evidence-based

### Response Protocol

When you detect a sacred cow:

1. **Name it.** "This appears to be an inherited convention, not a verified requirement."
2. **Trace it.** When was this decided? What constraints existed then? Do those constraints still exist?
3. **Test it.** What would happen if we did the opposite? What would break? (If nothing breaks, it's pure convention.)
4. **Recommend.** Keep it, kill it, or flag it for review — but make the recommendation explicit.

---

## DIAGNOSTIC TRIGGERS

### Apply full first-principles analysis when

- Choosing a technology, framework, or architectural pattern for a new system
- A "best practice" is being applied but no one can explain WHY it's best for this specific case
- The solution feels copied rather than designed
- Requirements contradict each other — one of them is probably a convention masquerading as a requirement
- Cost, complexity, or timeline seems unreasonable — a hidden assumption may be inflating the scope
- The user explicitly asks: "think from first principles," "challenge my assumptions," "why do we do it this way?"

### Light first-principles check (always)

- Before accepting any "standard approach": can you name the bedrock truth that makes it standard?
- Before rejecting any "unusual approach": is the objection truth-based or convention-based?
- Before saying "we should use X": why X specifically, from bedrock, for THIS problem?

---

## SELF-EVALUATION CHECKPOINT

Run before finalizing any analysis where first-principles thinking was triggered:

| Check | Question |
| :--- | :--- |
| **Assumptions Listed** | Did I list ALL assumptions, not just the obvious ones? |
| **Classification Done** | Is each assumption marked as truth, convention, belief, or expired truth? |
| **Bedrock Reached** | Did I ask "why?" until I hit provable, irreducible truth — or did I stop early? |
| **Analogies Validated** | If I borrowed a solution, did I verify its hidden assumptions hold here? |
| **Convention Tested** | If I followed convention, can I justify it from first principles — not just "everyone does it"? |
| **Reconstruction Clean** | Did I build from truths upward, or did I rationalize a pre-existing preference? |
| **Sacred Cows Named** | Did I flag inherited decisions that no one can justify? |

---

## KEY INSIGHT

> The goal of first-principles thinking is not to reject all convention. It is to know the difference between a load-bearing wall and a decorative one — so you never accidentally remove the wrong one, and you never refuse to move the right one.

Convention is efficient. Truth is reliable. Know which one you're standing on.
