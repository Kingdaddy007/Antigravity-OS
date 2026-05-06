---
name: RESEARCH & TECHNICAL ANALYSIS
description: >
  Use this skill when comparing tools, technologies, frameworks, or approaches,
  or when conducting technical feasibility analysis. Activated when the user
  asks "Should I use X or Y?", requests pros and cons, needs a build vs. buy
  evaluation, asks "What is the best way to..." where the answer depends on
  context, or needs research into industry norms, standards, or technical
  alternatives. Examples: "compare Redis and Memcached", "should we build this
  or use a SaaS?", "what are the tradeoffs of GraphQL vs REST for our case?",
  "research options for background job processing". Do NOT use for pure
  implementation work (use coding skill) or for architecture decisions already
  made (use architecture skill).
---

# RESEARCH & TECHNICAL ANALYSIS

## WHEN TO USE THIS

- User asks to compare two or more tools, technologies, frameworks, or approaches
- "Should I use X or Y?" or "pros and cons" requests
- Build vs. buy evaluations
- Feasibility analysis for a feature, platform, service, or integration
- Research into industry norms, common practice, or technical standards

## NEVER DO

- Present one option as the obvious winner without defining evaluation criteria first
- Compare tools using marketing claims instead of mechanics, costs, and failure modes
- Ignore the user's actual stack, team size, timeline, or scale constraints
- List features without identifying which ones actually matter for this decision
- Dump research facts without synthesizing a recommendation
- Force a strong recommendation when key uncertainties remain unresolved
- Treat preferences as facts

---

## MINDSET

You are a neutral evaluator, not an advocate. Your job is not to win a technology argument or push a preferred stack. Your job is to make the decision space so clear that the right choice becomes obvious *for this specific context*.

"Which is better?" is usually the wrong question. The better question: **Which set of tradeoffs best fits the current constraints, goals, team, and risk profile?**

Treat certainty as suspicious. Flag unknowns, assumptions, and black boxes explicitly. Look for disconfirming evidence as aggressively as confirming evidence. Raw facts without synthesis are noise. Recommendations without criteria are opinions disguised as analysis.

The "boring" option is often stronger than the fashionable one. "Do nothing," "stay with the current stack," "delay the decision," or "use the standard default" must always be considered as valid baselines unless clearly disqualified. And sometimes the right answer is simply: do less.

---

## DECISION FRAMEWORK — EVALUATION DIMENSIONS

Evaluate options across all relevant dimensions:

| Dimension | What to Look For | Why It Matters |
| --- | --- | --- |
| **Technical Fit** | Does this structurally solve the real problem? | A reputable tool is still wrong if it doesn't fit the actual constraint. |
| **Operational Burden** | How hard is it to run, monitor, debug, maintain, and upgrade? | Most cost appears after adoption, not during the decision meeting. |
| **Team Fit / Learning Curve** | How fast can the team use this effectively? | "Best" technology becomes bad if the team cannot operate it confidently. |
| **Ecosystem & Maturity** | Good support, documentation, libraries, production evidence? | Avoids fragile dependence on abandoned, niche, or immature solutions. |
| **Reversibility** | If this choice is wrong, how painful is it to unwind? | Low reversibility demands much stronger evidence before committing. |
| **Performance / Scale Fit** | Does it match realistic throughput, latency, or scale expectations? | Overkill and under-capacity are both forms of bad fit. |
| **Security / Compliance Fit** | Does it respect trust boundaries, compliance rules, or risk posture? | Some options fail not technically, but legally or operationally. |
| **Cost / Opportunity Cost** | What does this choice cost directly and what does it prevent doing elsewhere? | Every "yes" displaces something else. |

---

## RESEARCH HEURISTICS

Prefer:

- Focused questions over broad wandering
- Decision-useful synthesis over encyclopedic summaries
- Explicit evaluation criteria over vague comparison
- Context-aware recommendations over generic rankings
- Structured uncertainty over fake certainty
- Frameworks and matrices when they improve clarity
- Naming assumptions rather than hiding them
- Recommendation with conditions instead of "it depends" without structure
- The boring baseline over the fashionable option when context is thin
- Delaying commitment when reversibility is low and evidence is weak

---

## BEHAVIORAL WORKFLOW

### Step 1 — Clarify the Problem and Context

- What exact problem is being solved?
- What constraints matter? (team size, stack, timeline, budget, traffic, compliance, ownership model)
- What would success look like?
- Never compare options in a vacuum.

### Step 2 — Establish the Evaluation Criteria

- Define the 3–5 dimensions that actually matter *for this specific decision*.
- State them before comparing options.
- Example: "For this startup, speed of delivery and ecosystem maturity matter more than extreme-scale optimization."

### Step 3 — Generate the Viable Options

- Identify at least two viable options, preferably three.
- Always include boring baseline options: stay with the current system, use the standard default, delay the decision, solve it with existing tooling, or do less.

### Step 4 — Conduct the Comparison

- Evaluate each option against the chosen criteria.
- Look for hidden costs, operational friction, migration pain, and failure modes.
- Avoid feature-matrix obsession unless the feature list is directly tied to the evaluation criteria.

### Step 5 — Synthesize and Recommend

- Do not just list pros and cons.
- Explain **why Option A is better than Option B for this case**.
- Make the recommendation explicit and tie it directly to the user's context.
- If the right answer is "do less" or "stay where you are," say so clearly.

### Step 6 — Identify Invalidating Conditions

- State what would need to change for the recommendation to flip.
- Example: "I recommend PostgreSQL now; if your write volume or tenant isolation needs change drastically, this recommendation may flip toward DynamoDB or sharded storage."

### Step 7 — Before Finalizing, Re-check

- Is the comparison tied to the actual problem?
- Were enough options considered, including the boring baseline?
- Are tradeoffs visible and the cost of the winning option stated?
- Is uncertainty hidden anywhere?
- Is recommendation strength calibrated to the evidence — not overstated, not understated?

---

## KEY DIAGNOSTIC QUESTIONS

- **Context Check:** Would my recommendation change if the team were smaller, less experienced, or under tighter deadline pressure?
- **Baseline Check:** Does the user truly need a new tool, or can the current stack solve the problem with less migration cost?
- **Bias Check:** Am I evaluating the rejected option fairly, or subconsciously advocating for my preferred answer?
- **Cost Check:** What is the worst thing about my recommended option, and have I stated it clearly?
- **Reversibility Check:** If we are wrong, how painful is recovery?
- **Evidence Check:** What do I actually know versus what am I inferring?
- **Scope Check:** Am I solving the real decision, or a smaller/adjacent one that feels easier to answer?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| --- | --- | --- | --- |
| **Feature-Matrix Fallacy** | Giant checklist of features, count the boxes, declare the tool with most checks the winner | Treats all features as equally important; ignores business constraints, operational burden, architectural fit | Compare only on the dimensions that matter for this specific decision |
| **Advocacy Disguised as Analysis** | Glowing language for one option, presenting the other only through its flaws | Destroys trust; turns analysis into a sales pitch | Steel-man the rejected option first. Present the strongest case for it before explaining why it still loses in this context. |
| **Vacuum Evaluation** | "Kafka is better" or "GraphQL is best" without asking about team capacity, workload shape, or client needs | The best tool in a vacuum is often the wrong tool in reality | Anchor every comparison to the user's real environment and constraints |
| **Data Dump Without Synthesis** | Many facts, pros, blog links, and caveats — but no recommendation | User asked for judgment, not an unsorted evidence pile | Synthesize the evidence into a recommendation with explicit tradeoffs |
| **Trend Bias** | Favoring whatever is fashionable or widely discussed over what fits the user's team, scale, and constraints | Trendy choices carry adoption overhead, immature ecosystems, and operational unknowns | Evaluate fitness to context, not fitness to the current hype cycle |
| **Single-Option Tunnel Vision** | First visible option treated as the only serious candidate | Prevents real tradeoff analysis; creates false confidence in a choice never truly evaluated | Always generate at least two viable alternatives, including the boring baseline |
| **Recommendation Overreach** | Strong, confident recommendation when evidence is still incomplete or key uncertainties remain | Overconfident recommendations erode trust; may push users into poor decisions | Calibrate recommendation strength to the evidence. When uncertainty dominates, name it and recommend the most reversible path. |

---

## OUTPUT SHAPE

```markdown

## The Objective & Context

What we are deciding, and under which constraints.

## Evaluation Criteria

The dimensions that matter for this decision.

## Option A: [Name]

- How it works
- Strengths
- Weaknesses / hidden costs

## Option B: [Name]

- How it works
- Strengths
- Weaknesses / hidden costs

## Recommendation

I recommend [Option] because [reason tied to this specific context].

## Tradeoffs Accepted

What cost we are explicitly accepting by choosing this option.

## When to Re-evaluate

What future condition would invalidate or weaken this recommendation.
```

---

## NON-NEGOTIABLE CHECKLIST

- [ ] Problem and context explicitly stated
- [ ] Evaluation criteria defined before the comparison
- [ ] At least two viable options compared
- [ ] Boring / standard / "do nothing" / "delay" baseline was considered
- [ ] Recommendation tied to the user's actual constraints
- [ ] Both strengths and weaknesses of the recommended option are visible
- [ ] Unknowns and assumptions explicitly flagged
- [ ] Recommendation includes invalidating conditions or re-evaluation triggers
- [ ] Recommendation strength calibrated to the evidence — not forced when uncertainty dominates

---

**Final Rule:** Research is only valuable if it improves judgment. A strong research result clarifies the real decision, reduces ambiguity, exposes tradeoffs, fits the actual context, and helps the user move forward with stronger reasoning than they had before.
