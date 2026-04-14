# MEMORY: DECISIONS LOG

**Version:** Gold v1.0
**Layer:** 12 — Institutional Learning
**Tier:** 3 — Loaded on demand
**File:** memory/decisions-log.md
**Purpose:** Records significant technical decisions and their reasoning so they are not re-litigated and future work can reference WHY choices were made.
**Loaded When:** Making a decision similar to one already made. Onboarding new contributors. Reviewing past architectural choices. Evaluating whether a past decision should be reconsidered.
**Format:** Append-only. Never edit past entries — add corrections as new entries.

---

## WHEN TO ADD AN ENTRY

Add an entry when:

- A Type 1 or Type 1.5 decision is made — architectural, technology, data model, API contract, deployment strategy, security posture
- The team debates an approach and reaches consensus
- A significant tradeoff is consciously accepted
- A decision is made that someone might question or re-litigate later
- A previous decision is reversed, updated, or superseded

Do NOT log:

- Routine implementation choices — variable naming, local refactoring
- Type 2 decisions that are easily and cheaply reversible
- Decisions already documented in Architecture Decision Records — reference the ADR instead
- Temporary task choices with no long-term impact
- Raw brainstorming or transient notes

---

## HOW TO USE THIS FILE

Anti-Gravity should consult this file when:

- A recurring decision topic or architecture question reappears
- The team is tempted to re-open a resolved issue without new evidence
- Historical rationale matters for current work
- Onboarding a new contributor or reviewing past choices

If the team keeps having the same argument repeatedly, the decision probably belongs in this file.

---

## ENTRY FORMAT

[YYYY-MM-DD] — [Decision Title]

Context
[What situation prompted this decision? What problem were we solving? What need led to this choice?]

Options Considered

[Option A] — [brief description and why it was considered]
[Option B] — [brief description and why it was considered]
[Option C] — [brief description and why it was considered]

Decision
[What we chose and WHY — one sentence summary, then reasoning]

Why This Path Was Chosen

[reason 1]
[reason 2]
[reason 3]

Tradeoffs Accepted
[What we sacrificed and why it is acceptable given the context]

Assumptions
[What must remain true for this decision to hold]

Review Trigger
[Under what condition should this decision be reconsidered? What new evidence or changed constraint would make it worth revisiting?]

Related Files / Areas

[ADR / context file / workflow / feature area / postmortem]
[related item 2]

Tags
[#architecture #database #auth #performance #tooling #process etc.]

---

## QUALITY BAR FOR ENTRIES

A strong entry:

- Captures something future work may genuinely need to reference
- Explains why the decision mattered at the time
- Records reasoning, not just outcomes
- Makes future reversal conditions explicit
- Is specific enough to reduce repeated debates

A weak entry:

- Stores trivial choices with no long-term consequence
- Lacks rationale — records what but not why
- Becomes a noisy history dump instead of useful decision memory
- Overwrites or silently edits past decisions instead of adding a new entry

---

## USAGE RULES

1. Record decisions that materially affect:
   - Architecture and system structure
   - Stack and tooling choices
   - API contracts and compatibility posture
   - Deployment and release strategy
   - Security posture and trust-boundary decisions
   - Product and engineering tradeoff patterns
   - Naming conventions and standards with long-term impact
2. Do not overwrite history silently — if a decision is revisited, add a new entry and mark the old one as superseded.
3. Most recent entries appear at the top.
4. Use this file to reduce repeated debates, not to freeze the system permanently against legitimate reconsideration.

---

## EXAMPLE ENTRY

2024-03-15 — Chose Zustand and React Query Over Redux

Context
Needed a state management approach for the frontend. Team debated the options during sprint planning. Multiple engineers had different prior experience and preferences.

Options Considered

Redux Toolkit — full-featured, some team experience, significant boilerplate
Zustand plus React Query — minimal client state plus server state separation with caching built in
Jotai — atomic state model, very lightweight, less ecosystem

Decision
Chose Zustand plus React Query. Zustand handles minimal client-only state such as UI toggles, modals, and sidebar state. React Query handles all server state — caching, refetching, and optimistic updates. This keeps client state trivially simple while giving robust server state management without building a caching layer ourselves.

Why This Path Was Chosen

Clear separation of concerns — server state and client state are fundamentally different problems
Less boilerplate than Redux for our actual usage pattern
React Query handles caching that we would have built manually anyway
Zustand is trivial to learn and leaves no footprint when not needed

Tradeoffs Accepted

Two tools instead of one unified state solution
Team needs to learn React Query patterns — upfront investment
Acceptable because the separation of concerns reduces total complexity over time

Assumptions

Server state remains dominant over complex client-only state
React Query continues to be actively maintained
Our client state needs remain simple — UI toggles, not complex local state machines

Review Trigger
If client-only state becomes complex beyond UI toggles, reconsider whether Zustand is sufficient or a different atomic model is better.

Related Files / Areas

contexts/stack-context.md
contexts/architecture-context.md

Tags: #architecture #frontend #state-management

---

## ENTRIES

<!-- Append new entries below this line. Most recent at the top. -->
<!-- Append new entries below this line. Most recent at the top. -->
