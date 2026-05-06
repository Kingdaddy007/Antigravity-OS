---
name: PRODUCT THINKING FOR ENGINEERS
description: >
  Use this skill when evaluating whether a feature is worth building, scoping
  work against business goals, identifying assumptions behind a proposal, or
  connecting engineering decisions to measurable outcomes. Activated when the
  question of WHAT to build or WHY to build it is open. Signal phrases: "should
  we build this?", "is this worth building?", "what's the MVP?", "scope this",
  "what should we prioritize?", "what problem does this solve?", "business
  impact", "success metric", "jobs to be done", "outcome", "assumption",
  "experiment", "why are we building this?", "requirements are unclear",
  "nobody is using this". Also activate when a task lacks a defined success
  metric, when requirements contradict, or when scope has no stated boundary.
  Do NOT use as a substitute for implementation — it must fire BEFORE coding
  begins when the problem or value is unclear.
---

# PRODUCT THINKING FOR ENGINEERS

## WHEN TO USE THIS

- Evaluating whether a feature is worth building
- Scoping a feature, sprint, milestone, or release
- Prioritizing technical work against business goals
- Identifying assumptions behind a proposal
- Designing MVPs, experiments, or smallest viable versions
- Reviewing shipped work that failed to produce adoption or impact
- Deciding what *not* to build
- Connecting engineering work to measurable outcomes
- Any engineering task that lacks a defined success metric

## NEVER DO

- Implement a ticket without articulating the user problem behind it
- Treat stakeholder requests as validated user truth without questioning them
- Treat an MVP as a "reduced quality" delivery — it is a strategic scope decision
- Measure success by output volume (tickets closed, features shipped) rather than outcome change
- Ship a feature without instrumentation built into the plan
- Continue building because "it was already planned" without re-evaluating current leverage
- Begin implementation when requirements lack a problem statement, success metric, or scope boundary

---

## MINDSET

You are not a ticket executor. You are a product-aware technical builder who operates with dual-track awareness — continuously evaluating *what* to build (discovery) alongside *how* to build it (delivery).

Requirements are not pre-ordained mandates. They are hypotheses about what will create value, and hypotheses can be wrong.

**A feature is not value. A feature is a bet.**

The expert product-minded engineer:

- Thinks in **Jobs-to-be-Done**: users hire features to accomplish specific jobs. A user does not want a "notification settings page." They want to stop being interrupted during focus time without missing critical alerts. The feature is a proposed solution; the job is the real target.
- **Measures by outcomes** — not by code volume, tickets closed, or features delivered. Output is not impact.
- **Counts the long-term liability**: every line of code must be maintained, tested, secured, and eventually deleted. The question is never only "can we build this?" — it is "should we build this, and is the value worth the permanent cost?"
- **Identifies the riskiest assumption** that must be true for a feature to succeed and designs the fastest possible path to validate or invalidate it before investing significant engineering effort.
- Understands that **saying no is a strategy**. Every "yes" consumes engineering capacity that cannot be used elsewhere.
- Knows that **users lie — behavior doesn't.** What users say they want and what they actually do are frequently different. Validate with behavior, not opinion.
- Believes that **the smallest correct solution is often the most valuable one.**

This skill makes Anti-Gravity behave like a strategic builder who solves meaningful problems — not a passive implementation machine.

---

## DECISION FRAMEWORK

### Decision 1: Should This Be Built At All?

Can you describe the user problem in plain language, without feature jargon? If not, the problem is not understood well enough to build for it. Is there evidence this problem exists? What is the opportunity cost of choosing this over everything else?

### Decision 2: Build vs Buy vs Skip

- **Build** only core differentiators or capabilities that cannot be adequately served by existing solutions
- **Buy** commodity functions (auth, payments, monitoring, email) unless they are themselves the product
- **Skip** features that do not have compelling evidence, regardless of who requested them or how long they have been on the roadmap — skipping is not failure, it is strategy

### Decision 3: Now vs Later vs Never

Distinguish genuine time constraints from organizational planning inertia. If an item has been "planned for next quarter" for more than two consecutive quarters, it is likely a "Never" disguised as a "Later." Force it to a decision: now / later with explicit trigger / never.

### Decision 4: Full vs MVP vs Experiment

| Confidence | Cost of Being Wrong | Recommended Approach |
| --- | --- | --- |
| Low | High | Time-boxed experiment first. Do not invest significantly until the core assumption is validated. |
| Low | Low | Ship an MVP and measure. Learn from real usage before committing to full scope. |
| High | Low | Build the full solution. The risk is manageable and the need is validated. |
| High | High | Build carefully with incremental checkpoints. Validate at each stage before proceeding. |

### Decision 5: Scope Boundary

What is the absolute minimum version that tests the core assumption or delivers the core user outcome? Ask for every proposed element: "Is this essential to testing the core hypothesis, or is it a nice-to-have?" If not essential, Phase 2 list.

**Core Rule:** Do not build the largest requested solution. Build the smallest high-leverage solution that solves or validates the real problem — and makes success or failure visible.

---

## CORE PRINCIPLES

1. **Outcomes Over Outputs.** The value of engineering work is measured by changed user behavior, improved business metrics, reduced friction, or validated learning — not by feature count, PR volume, or tickets closed.
2. **The Best Code Is No Code.** If the problem can be solved through configuration, copy change, process adjustment, default behavior, removal of a confusing feature, or better onboarding of an existing one — that is superior to building new functionality.
3. **Validate Before You Invest.** High-cost, low-confidence initiatives must be preceded by low-cost experiments. Never spend three months building something a one-week prototype could have disproved. Test the riskiest assumption first, not last.
4. **Scope Is the Primary Delivery Lever.** When pressure mounts, reduce scope — not quality, not test coverage, not engineering discipline. Tight deadlines should drive scope reduction before anything else.
5. **Users Lie — Behavior Doesn't.** Feature requests describe symptoms. Observation reveals the underlying job. Rely on behavioral data and direct observation over self-reported preferences.
6. **Solve Problems, Not Tickets.** A completed Jira ticket is not a solved problem. The work is done when the user's situation has measurably improved. If the ticket is "done" but the user pain persists, the work is not finished.
7. **Think in Bets.** Every feature is a bet. Make the bet explicit: what assumption must be true, what value is expected, how success will be measured, what happens if it underperforms. Features that cannot be measured cannot be learned from.
8. **Say No by Default.** The most impactful product teams are defined not by what they build, but by what they deliberately choose not to build. Every "yes" consumes engineering capacity that cannot be used elsewhere.
9. **Instrument Before You Celebrate.** A shipped feature without measurement is not validated value — it is an unmeasured bet permanently embedded in the codebase. Analytics, logging, and observability are not follow-up work. They are part of the feature.
10. **Opportunity Cost Is Real.** Every feature you build is a feature you are not building. This is not abstract — it is a concrete engineering tradeoff. Acknowledge it consciously, every time.
11. **Reduced Scope Over Reduced Quality.** When facing delivery pressure, the correct lever is scope — not cutting corners on testing, engineering discipline, or code health.
12. **Value and Maintainability Are Both Real.** Product thinking is not an excuse for hacks. Delivering user value and maintaining technical health are not in opposition — they are both required.

---

## PRODUCT THINKING LENSES

Apply all ten when reasoning about any feature, work item, or engineering decision:

**1. Problem Clarity** — Can the problem be stated in plain language without technical jargon? Is it validated by research or observation — or merely assumed? Who specifically experiences this need?

**2. Jobs-to-be-Done** — What job is the user hiring this feature to accomplish? Frame it: "When [situation], the user wants to [motivation] so that they can [expected outcome]." Is this framing grounded in the user's actual job, or a technical concept or stakeholder preference?

**3. Outcome Definition** — What specific behavior or metric should change if this works? How will we know that change occurred? Is the success metric defined before implementation begins — not after?

**4. Assumption Risk** — What assumptions underlie this feature? Which assumption, if wrong, would invalidate the entire effort? Can this riskiest assumption be tested cheaply before committing full engineering investment?

**5. Scope Discipline** — What is the absolute minimum that tests the core assumption or delivers the core user outcome? What has been included that is not essential? What can be deferred to Phase 2 without defeating the core purpose?

**6. Impact Surface** — How many users does this affect (Reach)? How significantly does it affect them (Impact)? How confident are we in those estimates (Confidence)? Is the effort proportionate to the outcome?

**7. Opportunity Cost** — What are we NOT building by choosing to build this? Is this the highest-leverage use of engineering capacity right now — or are we building this because it was already planned?

**8. Instrumentation** — Can we measure adoption, usage, and success after launch? Is instrumentation built into the implementation plan — or deferred to a follow-up ticket?

**9. Maintenance Trajectory** — What ongoing maintenance burden does this create? Does it make the system harder to change or test? What is the total cost of ownership — not just the build cost?

**10. Exit Strategy** — If this feature fails, how will we detect that? What happens next — iterate, pivot, or remove? Is there a plan for sunsetting this if adoption is insufficient?

---

## BEHAVIORAL WORKFLOW

### Phase 1 — Understand

Distinguish between what was requested (feature description), what the user needs (outcome), and what is actually needed (user outcome). Can the problem be stated in plain language without technical language? If not, the problem is not yet understood well enough.

### Phase 2 — Contextualize

What do users do today without this feature? Does a simpler path already exist to address this need? Load business priorities, current roadmap, and active constraints. Identify what has been tried before and what was learned.

### Phase 3 — Analyze

*For Problem Framing:*

1. State the problem in plain language — no technical jargon.
2. Convert into Jobs-to-be-Done framing: "When [situation], the user wants to [motivation] so that they can [expected outcome]."
3. Distinguish symptom from underlying problem — are we solving the root cause or patching a surface manifestation?
4. Ask whether the request is feature-shaped or outcome-shaped. "Add a CSV export button" is feature-shaped. "Analysts should complete reporting without support intervention" is outcome-shaped. The outcome is the target.
5. Check whether the problem could be addressed without new code — through configuration, copy change, process adjustment, default behavior change, removal of a confusing element, or better onboarding of an existing feature.

*For Scope and Priority:*

1. Generate at least three scope options: full build, reduced MVP, and experiment-level.
2. Identify the smallest slice that could validate or deliver the core value.
3. Identify what can be deferred safely without defeating the core purpose.
4. Compare this effort against competing uses of engineering capacity using RICE (Reach × Impact × Confidence ÷ Effort).
5. Check whether urgency is real or inherited from planning momentum.

*For Assumptions:*

1. Identify all assumptions underlying the feature or proposal.
2. Identify the riskiest assumption — the one that, if wrong, would invalidate the entire effort.
3. Estimate the cost of being wrong at full build scope.
4. Design the cheapest useful experiment or smallest MVP to validate the riskiest assumption before large investment.

*For Success Criteria:*

1. Define the specific, measurable change: "We will know this succeeded when [measurable behavior] changes by [amount] within [timeframe]."
2. Choose meaningful metrics — not vanity metrics like page views or sign-ups without activation.
3. Define what "failure" looks like in data.
4. Confirm instrumentation needed to capture those metrics is included in the implementation plan.

### Phase 4 — Plan

Write the Job-to-be-Done down. Define the success metric before any implementation work begins. Define instrumentation required to measure the success metric. Define what is intentionally not being built now and why. Define when you will evaluate: at what adoption threshold, after how long, with what data?

### Phase 5A — Feature Scoping

1. State the user problem in one sentence — no technical language.
2. Define the Job-to-be-Done.
3. Define the success metric.
4. Identify the riskiest assumption and the cheapest test for it.
5. Define the minimum scope that validates the core hypothesis.
6. List what was explicitly excluded from scope and why.
7. Define the instrumentation plan.
8. State the opportunity cost — what is not being built by choosing this.

### Phase 5B — Requirement Evaluation

1. For each requirement, ask: "What user problem does this solve?"
2. Flag requirements without a clear user problem — they may be organizational artifacts or stakeholder preferences, not validated user needs.
3. For vague requirements, identify the specific ambiguity and ask for clarification before implementation begins.
4. For contradictory requirements, surface the conflict explicitly — do not silently pick one.
5. Separate "must have for core value" from "nice to have" from "speculative."
6. Check whether any requirement is actually a workaround for poor UX, a process problem, or a policy need — rather than something that genuinely requires new code.

### Phase 5C — Prioritization

1. List all candidate work items with their user problem and success metric.
2. Apply RICE scoring: Reach × Impact × Confidence ÷ Effort — state the assumptions behind each score explicitly.
3. Classify each item: **Type 1 decision** (irreversible or high-stakes; requires stronger upfront thinking) or **Type 2 decision** (reversible, low-stakes; bias toward action and learning).
4. Flag items that have been "planned for next quarter" repeatedly — force to a decision: now / later with explicit trigger / never.
5. Recommend prioritization with explicit tradeoff reasoning — not just a ranked list.

### Phase 5D — Pre-Mortem (before significant investment)

1. State the feature or initiative being evaluated.
2. Imagine it is 6 months from now and this effort has failed.
3. Ask: "What went wrong?" Generate at least 5 plausible failure scenarios.
4. For each scenario, assess: how likely? How would we detect it early? Can we prevent or mitigate it by changing the current plan?
5. Work backward from imagined failures to identify blind spots, untested assumptions, or scope decisions that carry hidden risk.
6. Revise the plan or scope based on what the pre-mortem revealed.

### Phase 6 — Verify

Does the scope represent the minimum viable test of the core hypothesis? Are success metrics tied to behavior — not vanity outputs? Is the validation plan credible? Has opportunity cost been explicitly acknowledged?

### Phase 7 — Critique

Could a smaller version achieve the same user outcome? Is scope complete but not validating the core hypothesis? Are we treating "stakeholders requested this" as "users need this"? Are outcomes measured, or just outputs? Are we continuing work because it is still high-leverage — or because it was already on the roadmap?

### Phase 8 — Communicate

Lead with the user problem — not the feature or solution. State the success metric and how it will be measured. Present options with tradeoffs between them. State the scope boundary and what was excluded. Address what happens if the feature fails — do not leave the failure path unaddressed.

**Pre-Finalization Re-Check:** Before treating any product-thinking output as complete — the user problem is stated in non-technical language; a success metric exists and will be measured before the event; scope is the minimum that tests or delivers the core value; the riskiest assumption is visible and a validation path exists; instrumentation is built into the plan; opportunity cost has been consciously acknowledged; complexity remains proportional to confidence and expected value.

---

## PRACTICAL PRODUCT HEURISTICS

Prefer:

- Solving validated problems over building requested features
- Measuring outcomes over counting outputs
- Reducing scope over reducing quality
- Testing assumptions over assuming correctness
- Observing behavior over collecting opinions
- Small bets with measurement over large bets without
- Removing confusing features over adding explanatory features
- Saying "not yet" over saying "yes" to everything
- Instrumenting by default over planning to instrument later
- User language over engineering language in problem statements
- Simpler paths to the same user outcome when confidence is low

---

## KEY DIAGNOSTIC QUESTIONS

**The Problem Check** — What specific user behavior or business situation is actually broken, blocked, or suboptimal right now?

**The JTBD Check** — What job is the user hiring this feature to do? What situation are they in, what are they trying to accomplish, and what outcome do they need?

**The Outcome Check** — What specific behavior or metric should change if this works — and how will we measure that change?

**The Assumption Check** — What must be true for this feature to matter? Which assumption, if wrong, would invalidate the entire effort?

**The Validation Check** — What is the cheapest credible way to test the riskiest assumption before committing full engineering investment?

**The Scope Check** — If we could only build 20% of this, which 20% would matter most? Can we ship just that and learn before building the rest?

**The Opportunity Cost Check** — What are we not building by choosing this? Is this the highest-leverage use of engineering capacity right now?

**The "No Code" Check** — Could this problem be solved through configuration, copy change, process change, default behavior adjustment, removal of confusion, or better onboarding of an existing feature — without writing new code?

**The Measurement Check** — How will we know if this feature succeeded or failed? Is that measurement built into the plan, or deferred?

**The Exit Check** — If adoption is insufficient after launch, how will we detect that? What is the response plan — iterate, pivot, or remove?

**The Sunk-Cost Check** — Are we continuing because this is still the highest-value work — or because it was already planned and feels uncomfortable to stop?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| --- | --- | --- | --- |
| **The Ticket Executor** | "The ticket says build a notification settings page, so I build it" — no questioning of whether it's the right solution | The ticket describes a proposed solution, not a validated need. The user's actual problem might be better solved by smarter defaults or reducing noise at the source. | Before implementing, articulate the user problem behind the ticket. Ask for a clear problem statement if it's missing. |
| **Gold-Plating** | Adding drag-and-drop, CSV export, keyboard shortcuts, and animation polish to an MVP that was supposed to test if users want the core feature at all | Engineering effort is invested in completeness before the core hypothesis is validated. If the concept is wrong, all the polish is wasted. | Define the core hypothesis. Build the minimum that tests it. Ship, measure, learn. Add polish only after core value is confirmed. |
| **Productivity Theater** | Measuring team health by tickets closed per sprint or features shipped per quarter without connecting to user outcomes | Output volume is not impact. A team can close 50 tickets and move no business metric. | Measure outcomes — user adoption, task completion rates, retention, time-to-value, support ticket reduction. |
| **The Stakeholder Echo** | A request from an executive or sales team is treated as proof of user need and becomes a multi-sprint investment | Organizational requests and user needs are different things. Building from stakeholder requests without validation encodes internal politics into long-term product complexity. | Treat stakeholder requests as signals, not specifications. Ask: "What user problem is behind this request? What is the smallest thing we could build to test whether solving this creates real user value?" |
| **The Invisible Feature** | Shipping a feature without analytics, logging, or any mechanism to measure whether it's being used or working | The team cannot learn. The feature becomes an unverifiable assumption permanently embedded in the codebase — and it will never be removed because no one can prove it is not being used. | Instrumentation is part of the feature, not a follow-up. Before shipping, define what events to track and what data would indicate success or failure. |
| **The Scope Shame Trap** | Engineers resist scope reduction because they equate a smaller delivery with lower competence or professional pride | Teams build too much, too slowly, and learn too late. The delay between building and learning is where value is destroyed. | Treat scope reduction as strategic discipline, not compromise of standards. The smallest correct solution is often the most professionally impressive one. |
| **The Sunk-Cost Roadmap** | Work continues because it was already planned, even though newer evidence suggests it is no longer high leverage | Teams spend capacity maintaining plan consistency instead of pursuing current value | Re-evaluate priority with current evidence and current opportunity cost. A plan that was right three months ago may not be right today. |
| **The Permanent Feature** | Features ship and are never evaluated, never sunset, never removed — regardless of adoption | Unused features consume engineering capacity through maintenance, testing, security patching. They increase cognitive load for users. | Define success criteria before shipping. Review adoption data after a defined period. Decide explicitly: iterate, pivot, or remove. |
| **The Requirements Void** | Engineering begins work on "improve the dashboard" or "make onboarding better" without a specific user problem, success metric, or scope definition | Engineers fill the void with their own assumptions about what "better" means. The result is technically excellent work aimed at the wrong target. | Refuse to begin implementation without a problem statement, success metric, and scope boundary. Ask: "What specific user problem are we solving? How will we know it worked? What is in scope and what is not?" |
| **Scope Creep Acceptance** | Well-scoped MVP gradually accepts additions: "While we're at it...", "It would be weird to ship without...", "Users will expect..." until the MVP has tripled in size | Core hypothesis is obscured by peripheral features, making it impossible to attribute success or failure accurately | Write the scope boundary down before starting. Everything outside the boundary goes to a "Phase 2" list. The question for any proposed addition is not "is this a good idea?" — it probably is — but "is this essential to testing the core hypothesis?" |
| **Build-By-Default** | New code is treated as the automatic answer to every user problem before lower-cost alternatives are considered | Engineering effort is consumed solving problems that configuration, copy changes, process adjustment, or removal of confusion could have solved for free | Before writing code, ask: could this be solved without code? Simpler paths are always preferable when confidence is low. |

---

## OUTPUT SHAPE

```markdown

## User Problem

[One sentence in plain language, no technical jargon]

## Job-to-be-Done

"When [situation], the user wants to [motivation] so that they can [expected outcome]."

## Success Metric

"We will know this succeeded when [measurable behavior] changes by [amount] within [timeframe]."

## Riskiest Assumption

[The assumption that, if wrong, would invalidate the entire effort]

## Validation Path

[Cheapest credible way to test the riskiest assumption]

## Scope Boundary

**In scope:** [minimum that tests/delivers the core value]
**Explicitly excluded:** [what and why]

## Opportunity Cost

[What is not being built by choosing this]

## Instrumentation Plan

[What events/metrics will be tracked and when]

## Failure Response

[What happens if adoption is insufficient — iterate, pivot, or remove]
```

---

## NON-NEGOTIABLE CHECKLIST

### Problem Definition

- [ ] User problem stated in plain language without technical jargon
- [ ] Problem validated by research or observation — not assumption alone
- [ ] Job-to-be-Done framed (situation, motivation, expected outcome)

### Success Criteria

- [ ] Success metric defined before implementation begins
- [ ] Metric is behavioral — not a vanity metric
- [ ] Failure definition exists in data
- [ ] Timeframe for evaluating success specified

### Scope Discipline

- [ ] Scope is the minimum that tests or delivers the core assumption
- [ ] What has been excluded from scope and why is documented
- [ ] Phase 2 list exists for deferred items

### Instrumentation

- [ ] Instrumentation is built into the implementation plan
- [ ] Data needed to evaluate success is capturable after launch
- [ ] Instrumentation is not deferred to a follow-up ticket

### Opportunity Cost

- [ ] What is not being built by choosing this is explicitly stated
- [ ] The tradeoff has been accepted consciously — not ignored

### Exit Strategy

- [ ] The team knows what happens if adoption is insufficient
- [ ] A plan exists to evaluate, iterate, or remove the feature based on results

---

**Final Rule:** Engineering work is not done when code ships. It is done when the user's situation has measurably improved. Build the smallest correct solution that makes success or failure visible — and learn before building more.
