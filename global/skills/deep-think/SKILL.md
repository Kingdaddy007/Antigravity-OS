---
name: deep-think
description: 'Use this skill when the user wants to activate full deep-thinking mode before receiving an answer. Forces reading and applying all three core reasoning files: system-thinking.md, expert-cognitive-patterns.md, and first-principles.md. Activated when the user says "deep think", "think deeply about this", "/deep-think", "apply deep thinking", "reason through this carefully", "full cognitive analysis", "think hard about this", "I need you to really think", "first principles analysis", "challenge my assumptions", "don''t give me a quick answer", or any request that demands visible, structured, rigorous reasoning before a response.'
---

# Deep Think — Full Cognitive Protocol Activation

## WHEN TO USE THIS

- User explicitly requests deep, rigorous, or first-principles thinking
- User triggers `/deep-think` slash command
- The problem is ambiguous, high-stakes, or requires challenging assumptions

## PERSISTENCE RULE

Once activated, deep-think stays ON for the remainder of the conversation. Every subsequent response must apply the full protocol until the user explicitly deactivates it by saying "stop deep thinking", "normal mode", "turn off deep think", or similar.

When persistent mode is active:
- Begin every response by confirming: `🧠 Deep Think — Active`
- Apply the full protocol to EVERY question, not just the triggering one
- If a question is trivial, apply the compressed format instead of skipping entirely
- Only deactivate when explicitly told to by the user

## NEVER DO

- Skip reading the core files — the WHOLE POINT is loading the full protocols
- Deliver a "deep think" response that looks like a normal response with extra words
- Silently drop out of deep-think mode without the user explicitly deactivating it
- Show the thinking trace without a clear, actionable answer at the end
- Treat this as decoration — every section of the trace must contain real reasoning, not filler

---

## ACTIVATION SEQUENCE

When this skill triggers, execute these phases in order:

### Phase 1 — Load Core Protocols

Read all three core files in full using the available file-reading capability:

1. `../../core/system-thinking.md`
2. `../../core/expert-cognitive-patterns.md`
3. `../../core/first-principles.md`

Do NOT skip any file. Do NOT rely on the compressed summaries in GEMINI.md. Read the full files.

### Phase 2 — Apply the Full Protocol

With all three files loaded, analyze the user's question or problem through the full cognitive engine:

1. **System Decomposition** (from system-thinking.md)
   - Current State → Desired State → Gap → Constraints → Options → Tradeoffs → Recommended Path → Verification Plan

2. **First-Principles Audit** (from first-principles.md)
   - List all assumptions
   - Classify: verified truth / inherited convention / untested belief / expired truth
   - Strip to bedrock — ask "why?" recursively
   - Detect sacred cows and analogical reasoning traps
   - Rebuild from verified truths upward

3. **Meta-Cognitive Safeguards** (from expert-cognitive-patterns.md)
   - Run all 6 safeguards: Nonlinearity, Gray Thinking, Over-Simplification, Framing Bias, Anti-Comfort, Delayed Discomfort
   - Classify the decision type (Type 1 / 1.5 / 2)
   - Apply second-order thinking
   - Run pre-mortem if Type 1

4. **Self-Evaluation Checkpoint**
   - Run the checkpoint tables from all three files before finalizing

### Phase 3 — Deliver

Present the output in the structured format defined below.

---

## OUTPUT SHAPE

### Full Deep Think (default)

```
## 🧠 Deep Think — [Problem Summary]

### System Decomposition
[Current state, desired state, gap, constraints, 3+ options with tradeoffs]

### Assumption Audit
| # | Assumption | Classification | Bedrock? | Notes |
[Table of all identified assumptions]

### Safeguards Applied
[Which safeguards fired, what they caught, how reasoning was adjusted]

### Second-Order Effects
[First-order → second-order → third-order consequence chain]

### Pre-Mortem (if Type 1)
[Imagined failure scenario and what it reveals]

### Recommendation
[Clear, actionable answer with reasoning trace]

### Verification Plan
[How to confirm this is correct]
```

### Compressed Deep Think (when user asks for "quick but deep")

```
## 🧠 Deep Think — [Problem Summary]

**Assumptions challenged:** [list]
**Safeguards fired:** [which ones, what they caught]
**Recommendation:** [answer]
**Confidence:** [high/medium/low + why]
**Verify by:** [how]
```

---

## NON-NEGOTIABLE CHECKLIST

Before delivering a deep-think response:

1. All three core files were read in full (not from memory, not compressed)
2. System decomposition was applied — not skipped
3. Assumptions were listed AND classified — not hand-waved
4. At least 3 options were generated for the core decision
5. All 6 meta-cognitive safeguards were checked — at least 2 produced insights
6. Second-order effects were mapped — not just first-order
7. The final answer includes a verification plan
8. The response contains real reasoning, not performative thinking
