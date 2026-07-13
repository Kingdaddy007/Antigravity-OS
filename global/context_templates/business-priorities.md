---
status: template
scope: project
project_id: null
updated_at: null
owner: null
confidence: unset
---

# BUSINESS PRIORITIES

**Version:** Gold v1.2 (Master Merge)
**Layer:** 6 — Context (Ground Truth)
**Tier:** 2 — Loaded by task
**File:** contexts/business-priorities.md
**Purpose:** Defines current strategic priorities, acceptable tradeoffs, priority hierarchy overrides, and what the team has explicitly decided NOT to build. Anti-Gravity uses this to align every engineering and product recommendation with business reality.
**Loaded When:** Feature prioritization, scope decisions, architectural tradeoffs, resource allocation discussions, or any decision where business context should influence the technical choice.
**Maintenance:** Review and update MONTHLY. This is the most time-sensitive context file — stale priorities lead to misaligned engineering effort. Update immediately after strategic planning meetings, pivots, or significant business changes.

---

## HOW ANTI-GRAVITY USES THIS FILE

This file directly shapes Anti-Gravity's tradeoff recommendations. When two valid approaches exist and the technical merits are comparable, this file determines which direction Anti-Gravity leans.

Priorities are contextual, not permanent. A recommendation that is right for an MVP may be wrong for an enterprise rollout. Anti-Gravity should not optimize in the abstract — it should optimize in alignment with current business priorities.

If business priorities are unclear or this file is stale, recommendations should be more conditional and that uncertainty should be stated explicitly.

**When loaded**, Anti-Gravity will:

- Align feature scope suggestions with your current strategic priorities
- Recommend tradeoff resolutions that favor what matters most right now
- Discourage engineering investment in areas explicitly deprioritized
- Flag when a proposed approach conflicts with a stated business priority
- Suggest scope reductions that preserve the highest-priority value
- Acknowledge opportunity cost in every significant recommendation
- Be skeptical of strategically deprioritized work unless a strong case is made
- Name priority conflicts explicitly rather than hide them

**When missing or incomplete**, Anti-Gravity will:

- Make tradeoff recommendations based on generic engineering best practices, which may not align with your business needs
- Give equal weight to all engineering concerns even when your business context demands bias toward specific ones
- Not know what you have decided NOT to build and may suggest features in those areas

**When stale**, Anti-Gravity will:

- Optimize for yesterday's priorities instead of today's
- Recommend investment in areas that are no longer strategic
- Miss new constraints or opportunities that have emerged
- Conflict with decisions your team has already made

---

## BUSINESS PRIORITIES SUMMARY

<!-- Fill in a short summary of what matters most right now.

Template:
The current business focus is on [primary priorities].
This means the team is intentionally optimizing for [delivery speed /
reliability / retention / enterprise readiness / cost control / activation].
Technical work should support these priorities by [how engineering
should respond].

Example:
The business is currently focused on improving activation and reducing
onboarding friction while maintaining enough reliability for customer
trust. Engineering should favor changes that improve user clarity and
speed of iteration, while avoiding debt in critical flows like auth
and billing.
-->

[Fill in]

---

## CURRENT PRIORITIES (Ranked)

### Priority 1: [Name] (Ranked)

- **Context:** [why this matters now]
- **Target Metric:** [measurable goal]
- **Timeline:** [when]
- **Success Looks Like:** [concrete outcome]
- **Engineering Implications:**
  - [implication 1]
  - [implication 2]
  - [implication 3]

### Priority 2: [Name] (Ranked)

- **Context:** [why this matters now]
- **Target Metric:** [measurable goal]
- **Timeline:** [when]
- **Success Looks Like:** [concrete outcome]
- **Engineering Implications:**
  - [implication 1]
  - [implication 2]

### Priority 3: [Name] (Ranked)

- **Context:** [why this matters now]
- **Target Metric:** [measurable goal]
- **Timeline:** [when]
- **Success Looks Like:** [concrete outcome]
- **Engineering Implications:**
  - [implication 1]
  - [implication 2]

---

## PRIORITY DEFINITIONS

### [Priority 1 Name] (Definition)

- **What it means:** [practical definition]
- **Why it matters now:** [reason]
- **Work that supports it:** [examples]
- **Work deprioritized because of it:** [examples]

### [Priority 2 Name] (Definition)

- **What it means:** [practical definition]
- **Why it matters now:** [reason]
- **Work that supports it:** [examples]
- **Work deprioritized because of it:** [examples]

---

## CONFLICT RESOLUTION OVERRIDES

| Default Position | Concern | Override Position | Reason | Duration | Scope |
| --- | --- | --- | --- | --- | --- |
| [position] | [concern] | [new position] | [reason] | [duration] | [scope] |

---

## WHAT WE ARE NOT DOING

### Explicitly Excluded — Do Not Suggest or Build

| Area | Decision | Rationale | Revisit When |
| --- | --- | --- | --- |
| [area] | Not building | [reason] | [condition] |
| [area] | Not building yet | [reason] | [condition] |
| [area] | Not planned | [reason] | [condition] |

### What This Means for Anti-Gravity

- Do NOT suggest [excluded area 1]
- Do NOT suggest [excluded area 2]
- If a feature request touches these areas, flag it explicitly: "This conflicts with the current Not Doing list in business-priorities.md. Has this decision been reconsidered?"

---

## ACCEPTABLE TRADEOFFS

### What We Will Accept

| Tradeoff | Why Acceptable | Boundary |
| --- | --- | --- |
| [tradeoff] | [reason] | [when it becomes unacceptable] |
| [tradeoff] | [reason] | [when it becomes unacceptable] |
| [tradeoff] | [reason] | [when it becomes unacceptable] |

### What We Will NOT Accept — Non-Negotiable Quality

| Line | Why Non-Negotiable |
| --- | --- |
| [hard line 1] | [reason] |
| [hard line 2] | [reason] |
| [hard line 3] | [reason] |

Examples of what belongs in non-negotiable lines:

- shipping without tests for critical paths such as auth, data mutations, and state transitions
- skipping security review on auth-related changes
- accumulating database migration debt
- deploying without error monitoring functional
- bypassing code review for changes described as small

---

## WHAT MUST BE PROTECTED EVEN UNDER PRESSURE

- [protected area 1]
- [protected area 2]
- [protected area 3]

Examples of what belongs here:

- auth and permission correctness
- payment and billing integrity
- tenant data isolation
- critical user trust flows
- legal and compliance obligations
- operator visibility into failures

---

## HIGH-LEVERAGE BUSINESS SURFACES

- [surface 1]
- [surface 2]
- [surface 3]

Examples of what belongs here:

- onboarding flow
- checkout and billing reliability
- admin workflows for enterprise setup
- reporting correctness
- notification trust
- self-serve configuration

---

## CURRENT CONSTRAINTS SHAPING PRIORITIES

| Constraint | Impact on Decisions |
| --- | --- |
| [constraint 1] | [how it affects recommendations] |
| [constraint 2] | [how it affects recommendations] |
| [constraint 3] | [how it affects recommendations] |

Examples of what belongs here:

- small engineering team
- urgent customer commitments
- limited runway
- high support load
- enterprise deals pending
- compliance pressure increasing
- roadmap compression

---

## TIME HORIZON BIAS

Current operating horizon: [immediate MVP / this quarter / next 6-12 months / long-term platform stability / near-term enterprise readiness]

### Meaning for Anti-Gravity (Horizon)

[Describe how this horizon should shape recommendation style]

---

## PRODUCT VS ENGINEERING BIAS

Current balance: [product speed dominates / engineering quality prioritized in critical flows / actively paying down debt / reliability recovery mode / enterprise readiness forcing more rigor]

### Meaning for Anti-Gravity (Bias)

[Describe how this balance should shape recommendations]

---

## CURRENT SUCCESS METRICS

| Metric | What It Actually Means | What It Does NOT Mean |
| --- | --- | --- |
| [metric] | [real meaning] | [common wrong assumption] |
| [metric] | [real meaning] | [common wrong assumption] |

---

## INVESTMENT ALLOCATION

| Category | Target % of Engineering Time | Priority Alignment |
| --- | --- | --- |
| [category 1] | [%] | [priority] |
| [category 2] | [%] | [priority] |
| [category 3] | [%] | [priority] |
| Bug fixes and maintenance | [%] | Ongoing |
| Infrastructure and tooling | [%] | As needed |

### Allocation Rules

- These are guidelines, not rigid quotas
- If a critical bug emerges it takes priority over everything
- Anti-Gravity should flag when a proposed investment significantly exceeds its category allocation

---

## STRATEGIC NO RULES

| Pattern | Why to Challenge It |
| --- | --- |
| Broad rewrites with no immediate leverage | [reason] |
| Speculative platform work | [reason] |
| Features without measurable user problem | [reason] |
| Scaling work without actual scale pain | [reason] |
| Dependency churn without real need | [reason] |
| [custom pattern] | [reason] |

---

## KNOWN PRIORITY TENSIONS

| Tension | How to Navigate It |
| --- | --- |
| Speed vs maintainability | [current bias] |
| Feature breadth vs reliability | [current bias] |
| Product urgency vs engineering investment | [current bias] |
| Sales commitments vs engineering reality | [current bias] |
| [custom tension] | [current bias] |

---

## PRIORITY OVERRIDE CONDITIONS

The following conditions justify immediate reprioritization:

- Security issue or vulnerability
- Data integrity risk
- Revenue-impacting outage
- Major customer trust issue
- Compliance concern
- Repeated failure in a critical workflow
- High blast-radius operational weakness
- [project-specific condition]

---

## UPCOMING DECISIONS

| # | Decision | Deadline | Type | Options | Current Leaning |
| --- | --- | --- | --- | --- | --- |
| 1 | [decision] | [when] | [type] | [options] | [leaning] |
| 2 | [decision] | [when] | [type] | [options] | [leaning] |

### How Anti-Gravity Should Handle Upcoming Decisions

- If a task touches a pending decision area, flag it: "Note: this area has a pending decision about [X]. The approach here should be compatible with both likely outcomes, or explicitly noted as depending on that decision."
- Do not pre-empt the decision by strongly recommending one option
- If asked directly, present options with tradeoffs and let the user decide

---

## WHAT GOOD TECHNICAL PRIORITIZATION LOOKS LIKE RIGHT NOW

Work is well-prioritized when:

- it is chosen based on user or business leverage, not engineering novelty
- scope is reduced before quality is reduced
- critical flows receive disproportionate care
- product and engineering tradeoffs are made consciously
- technical debt work is tied to delivery, reliability, or support impact
- features are scoped so they can be measured after release
- architecture investment is proportional to current product stage
- the team is not solving low-priority problems beautifully while ignoring high-priority ones

Work is poorly prioritized when:

- it is technically elegant but strategically mistimed
- it adds complexity that the current stage cannot justify
- it invests in areas the team has explicitly deprioritized
- it treats all engineering improvements as equally valuable right now

---

## BUSINESS PRIORITY ANTI-PATTERNS

### File-count vanity

**What it looks like:** Treating the number of generated artifacts as evidence of meaningful progress.
**Why it is harmful:** Rewards visible volume instead of durable quality.
**What to do instead:** Ask whether the work increased coherence, reuse, clarity, or future leverage.

### Priority thrash

**What it looks like:** Changing what matters most every few steps without preserving a stable value hierarchy.
**Why it is harmful:** Sequencing becomes chaotic and the system grows unevenly.
**What to do instead:** Keep the current priority stack stable unless there is an explicit reason to revise it.

### Local optimization over system value

**What it looks like:** Choosing the fastest next move for one feature even when it weakens the larger architecture.
**Why it is harmful:** Short-term convenience becomes long-term structural cost.
**What to do instead:** Optimize for whole-system integrity, not just local speed.

### Foundation skipping

**What it looks like:** Jumping into later layers or polish-heavy work before the current foundational layer is stable.
**Why it is harmful:** Downstream work gets built on unstable assumptions.
**What to do instead:** Finish the right layer deeply enough before accelerating outward.

### Sophistication theater

**What it looks like:** Adding complexity or extra structure because it sounds advanced.
**Why it is harmful:** The project looks more sophisticated while becoming harder to maintain and trust.
**What to do instead:** Prefer the simplest structure that strengthens the system honestly.

---

## PRIORITY QUESTIONS

When making tradeoff-sensitive decisions, Anti-Gravity should ask:

- Does this help the current top priorities?
- Is this improving the part of the product that matters most right now?
- Is this worth the opportunity cost at this stage?
- Is this increasing complexity in a way that fights the current business direction?
- If the team only had time for one thing, would this be it?
- Is this solving a low-priority problem beautifully while a high-priority problem waits?
- Does this conflict with anything on the Not Doing list?

---

## OPEN PRIORITY QUESTIONS

- [question 1]
- [question 2]
- [question 3]

---

## REVIEW CADENCE

| Review Type | Frequency | Trigger | Who |
| --- | --- | --- | --- |
| Full priority review | Monthly | First Monday of each month | Product + tech lead |
| Override review | Monthly | Same as priority review | Tech lead |
| Not Doing review | Quarterly | Strategic planning meeting | Full team |
| Upcoming decisions review | Biweekly | Sprint planning | Tech lead |
| Emergency update | As needed | Pivot or major business change | Product manager |

---

## CROSS-REFERENCES

| Related Context File | Relationship |
| --- | --- |
| `project-context.md` | Product overview and business stage inform priorities |
| `conflict-resolution.md` | Default priority hierarchy that overrides modify |
| `architecture-context.md` | Architectural decisions shaped by business priorities |
| `domain-rules.md` | Business rules that implement product behavior |
| `api-conventions.md` | API investment decisions guided by priorities |
| `infra-context.md` | Infrastructure investment guided by priorities |
| `stack-context.md` | Technology choices influenced by strategic direction |
| `security-baselines.md` | Security is never deprioritized regardless of overrides |

---

## FINAL RULE

The best technical answer is not always the best project answer.

Recommendations should follow the current business priority frame of this project — not generic engineering ideals, not what was true last quarter, and not what would be right for a different product at a different stage.

When in doubt about current priorities, ask. Do not assume.

---
