# EXPERT COGNITIVE PATTERNS — THINKING SAFEGUARDS

**Load when:** High-stakes decisions, architectural analysis, debugging persistent issues, anything where confident wrongness would be expensive.
**Companion:** `system-thinking.md` (WHAT to examine). This file: HOW to examine without fooling yourself.

---

## THE 6 META-COGNITIVE SAFEGUARDS

Apply these as automatic checkpoints during any analysis, decision, or conclusion.

### 1. NONLINEARITY

Relationships are almost never one-to-one. "Do X → get Y" is always a simplification.

**Catch:** Your reasoning follows a clean chain: A → B → C → Result.
**Fix:** List all factors that influence the outcome. Map how they interact. Ask: "Under what conditions does my assumed relationship break? What am I holding constant that might actually change?"

### 2. GRAY THINKING

Most decisions are not binary. "Either A or B" is usually a false dichotomy.

**Catch:** You have two options and they feel mutually exclusive.
**Fix:** Generate at least one gray-zone option that gives 70% of A and 80% of B. Common false dichotomies: move fast OR maintain quality; monolith OR microservices; refactor OR rewrite. The gray answer is usually right.

**Key insight:** If your reasoning is very black-and-white and you feel very confident — that confidence is a red flag, not a green light.

### 3. OKAM'S BIAS (Over-Simplification)

Every simplification removes detail. Sometimes that detail matters.

**Catch:** You found the root cause quickly and it feels satisfying. You stopped investigating after the first plausible explanation.
**Fix:** Before committing to a single cause, generate at least one alternative. Ask: "Could there be multiple contributing causes? Am I simplifying because it's noise, or because complexity is uncomfortable?"

### 4. FRAMING BIAS

The way a problem is presented changes how you think about it. The first frame is not necessarily the best frame.

**Catch:** You're thinking about the problem exactly the way it was presented to you.
**Fix:** Restate the problem in at least two fundamentally different ways. Ask: "What if the real problem is one level up? One level down? How would someone from a completely different background frame this?"

### 5. ANTI-COMFORT (Comfort as Warning Sign)

When your analysis feels easy and your confidence is high, you're likely using familiar patterns and missing something.

**Catch:** Solution came quickly. You can't think of a strong counterargument. You're eager to implement.
**Fix:** Actively try to break your own conclusion. Ask: "What could make me wrong? What am I assuming I haven't verified? If a senior engineer disagreed, what would they challenge?" If you can't find any reason you might be wrong — you haven't looked hard enough.

### 6. DELAYED DISCOMFORT (Pay Cognitive Costs Upfront)

The choice is never difficulty vs ease. It's upfront discomfort vs deferred discomfort — and deferred costs compound.

**Catch:** You're tempted to skip edge case review, skip tests, or tell yourself "we can fix it later."
**Fix:** Ask: "Am I saving time now, or creating a problem for my future self? If this shortcut fails, what does that failure cost vs. the time I'm saving?" If you must defer, do it intentionally: document what, why, and when you'll address it.

---

## DECISION CLASSIFICATION

Classify before analyzing. Invest the appropriate depth for the decision type.

| Type | Characteristics | Examples | Required Process |
| :--- | :--- | :--- | :--- |
| **Type 1** — Irreversible | Extremely expensive or impossible to reverse. Consequences persist for years. | Database schema, public API contract, core technology stack, architectural paradigm | All 12 thinking dimensions. All 6 safeguards. Pre-mortem. 3+ options evaluated. Document fully. Days to weeks. |
| **Type 1.5** — Partially reversible | Can be changed but reversal costs meaningful rework or migration. | Frontend framework, auth strategy, 3rd-party integration, caching architecture | Apply most relevant thinking dimensions. Identify riskiest assumption. Design reversibility path. Set review checkpoint. Hours to days. |
| **Type 2** — Reversible | Easily changed if wrong. Cost of reversal is low. | Folder structure, naming conventions, internal library choice, build tool, CSS framework | Time-boxed: 15–60 minutes max. Best decision with available info. 2–3 sentences of reasoning. Move forward. |

### Rules

1. Most engineering decisions are Type 2. Do not treat them as Type 1. Over-analyzing reversible decisions is a major time waste.
2. When uncertain about type, err toward Type 1.5.
3. Delaying a decision is itself a decision — with costs. Do not wait for perfect information.

---

## SECOND-ORDER THINKING

First-order: "What happens if I do X?" Second-order: "What happens after that? And after that?"

Most engineers stop at first-order effects. The most dangerous decisions have positive first-order effects and negative second-order effects.

### Example

- First-order: "Adding a cache reduces database load." ✓
- Second-order: "Now we have cache invalidation complexity and stale data bugs." ✗
- Third-order: "Team builds features assuming cache is always correct — debugging becomes a nightmare." ✗✗

**Rule:** When presenting a recommendation, always describe what it costs, what it changes, and what chain of consequences it sets in motion. If you can't identify any second-order effects, you haven't thought about it deeply enough.

---

## PRE-MORTEM PROTOCOL

Use for Type 1 decisions. Non-optional.

1. Imagine it's 6 months from now. This decision has failed catastrophically.
2. Ask: "What went wrong?" Work backward from the imagined failure.
3. For each identified failure path: How likely? How would we detect it early? Can we prevent it or reduce impact?
4. Does this change the decision, or just the monitoring plan?

**Why it works:** Framing as "explain why this failed" (past) accesses different reasoning patterns than "predict whether this will fail" (future). Optimism hides risks. Imagined failure surfaces them.

---

## SELF-EVALUATION CHECKPOINT

Run before finalizing any significant output (code, architecture, analysis, recommendation):

| Check | Question |
| :--- | :--- |
| **Linearity** | Is my reasoning a clean A→B→C chain? Have I accounted for nonlinear interactions? |
| **Binary** | Am I presenting an either/or? Have I explored the gray zone? |
| **Simplification** | Have I over-simplified? Am I cutting complexity because it's noise, or because it's uncomfortable? |
| **Framing** | Am I thinking about this the way it was presented, or have I tried alternative framings? |
| **Comfort** | Does this feel easy and obvious? If so — what am I missing? |
| **Cost** | Am I paying cognitive cost upfront, or creating delayed discomfort? |
| **Black boxes** | What do I know I don't know? Have I named those uncertainties explicitly? |
| **Second-order** | What happens after the first-order effects? What chain of consequences am I setting in motion? |

- Type 2 decisions: run mentally in 60 seconds.
- Type 1.5 decisions: run and briefly note any flags.
- Type 1 decisions: run thoroughly and document results.
- Any flag raised → pause, investigate, address before proceeding.
