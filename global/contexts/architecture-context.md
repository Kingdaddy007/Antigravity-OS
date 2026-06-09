# CONTEXT: ARCHITECTURE

**Version:** Gold v2.1

**Type:** Context File

**Layer:** Context — Ground Truth

**Tier:** 2 — Loaded by task

**File:** contexts/architecture-context.md

**Loaded When:** Architecture discussions, feature planning, code that touches multiple modules, debugging cross-cutting concerns, onboarding new contributors, or any task requiring understanding of system structure

**Purpose:** Defines how the system is structured — folder organization layer responsibilities, module boundaries, data flow, patterns and architectural decisions already made. Anti-Gravity uses this to place code correctly, respect ownership rules, and reason about the real shape of the system

**Maintenance:** Update when folder structure changes, new patterns are adopted, modules are added/split/merged, or significant architectural decisions are made. Review quarterly

---

## HOW ANTI-GRAVITY USES THIS FILE

This file is the structural map of the system. It tells Anti-Gravity
where things live, how they connect, and what rules govern the boundaries.

**When loaded**, Anti-Gravity will:

- Place new code in the correct location following the organizational
  pattern — not guess based on generic conventions

- Respect module boundaries — not suggest changes that violate ownership
  rules or create cross-module coupling

- Follow established architectural patterns instead of inventing new ones
- Understand data flow when debugging cross-cutting issues
- Reference previous architectural decisions instead of re-litigating them
- Identify and respect known technical debt instead of rediscovering it
- Treat critical boundaries as constraints, not suggestions

**When missing or incomplete**, Anti-Gravity will:

- Place new code in locations that may not match existing conventions
- Suggest architectural patterns that conflict with the current structure
- Create cross-module dependencies that violate boundary rules
- Re-debate decisions that have already been made and documented
- Miss known technical debt and potentially make it worse

**When stale**, Anti-Gravity will:

- Reference folders or modules that have been renamed or reorganized
- Follow deprecated patterns instead of current ones
- Miss new modules or boundaries that have been added since the last update

**Conflict rule:** If architectural details here conflict with another
context file, Anti-Gravity will flag the conflict explicitly rather than
silently choosing one. Both files may need to be updated.

---

## CURRENT ARCHITECTURAL REALITY

<!-- WHY THIS MATTERS: For projects that are not yet deployed as conventional
     applications — or that are in a spec/build/design phase — this section
     defines the actual current architectural model. Anti-Gravity uses this
     to avoid assuming a runtime architecture that does not yet exist, and
     to understand the structural environment it is actually operating in. -->

### What This Architecture Currently Is

<!-- Describe the current architectural model honestly.
     If this is a deployed application, summarize the architectural style.
     If this is still in a spec/design/build phase, describe that reality.

     Example (deployed application):
     "Modular monolith. Single Next.js application serving both frontend
     and API. Organized by feature domain (features/), not by technical
     layer. No microservices — all code lives in one repository, one
     deployment unit."

     Example (spec/build phase — like Anti-Gravity Gold):
     "Anti-Gravity Gold is a layered AI operating system being assembled
     as a file-based architecture. The 'architecture' is the layer model
     itself: core/, skills/, contexts/, workflows/, templates/, rubrics/,
     benchmarks/, and memory/. The system is in active build-out.
     The context layer is the current frontier." -->
[Fill in]

### Architecture Summary

<!-- WHY THIS MATTERS: Anti-Gravity uses this as the quick orientation
     anchor before diving into section-level detail. -->

<!-- Template:
     "The system is currently structured as [monolith / modular monolith /
     service-oriented / mixed / file-based layered architecture].
     Major domains include [key domains/components].
     Core interactions happen through [HTTP APIs / events / direct module
     calls / queues / database access / layer references].
     The architecture is optimized primarily for [delivery speed /
     maintainability / reliability / scale / team autonomy]." -->
[Fill in]

### What This Architecture Is NOT

<!-- WHY THIS MATTERS: Naming what the architecture is NOT prevents
     Anti-Gravity from suggesting patterns appropriate for a different
     architectural style. -->
<!-- Be explicit. What has been deliberately ruled out?
     Examples:

     - "This is NOT a microservices architecture. Do not suggest
       splitting into separate services."

     - "This is NOT a traditional MVC application."
     - "This is NOT a runtime application yet — do not assume a
       deployed server, database, or client." -->

- [Fill in]
- [Fill in]

---

## LAYER MODEL AND RESPONSIBILITIES

<!-- WHY THIS MATTERS: Every system has layers — whether code layers,
     module layers, or file-system layers. Knowing what belongs in each
     layer prevents misplaced logic, layer leakage, and ownership
     confusion. Anti-Gravity uses this to place code and recommendations
     in the correct layer every time. -->

### Layer Structure

| Layer | Responsibility | What Belongs Here | What Does NOT Belong Here |
| --- | --- | --- | --- |
| [Layer] | [What it does] | [What goes here] | [What is excluded] |
| [Layer] | [What it does] | [What goes here] | [What is excluded] |
| [Layer] | [What it does] | [What goes here] | [What is excluded] |

### Authoritative Boundaries

<!-- Which layer is authoritative for what?
     Anti-Gravity uses this to resolve placement disputes — when two
     layers could plausibly own something, the authoritative boundary
     decides. -->

| Layer | Is Authoritative For |
| --- | --- |
| [Layer] | [What this layer owns absolutely] |
| [Layer] | [What this layer owns absolutely] |
| [Layer] | [What this layer owns absolutely] |

### Structural Relationships Between Layers

<!-- How do the layers depend on and constrain each other? -->

- [Layer A] → [how it shapes or constrains Layer B]
- [Layer B] → [how it uses or is constrained by layers above]
- [Layer C] → [its relationship to the rest of the stack]

### Decision Rule: Where Does New Work Belong?

<!-- A routing test for placing any new file, module, or piece of logic.
     Anti-Gravity uses this when placement is unclear. -->

| If it is... | It belongs in... |
| --- | --- |
| Universal and always active | [Layer] |
| Domain-specific but reusable across projects | [Layer] |
| Specific to this project's reality | [Layer] |
| A repeatable execution procedure | [Layer] |
| A reusable output/document shape | [Layer] |
| An evaluation or scoring framework | [Layer] |
| A comparison or calibration reference | [Layer] |
| Durable retained project knowledge | [Layer] |

---

## FOLDER STRUCTURE

<!-- WHY THIS MATTERS: This is the map Anti-Gravity uses to determine where
     new code should go. Without this, new files may end up in wrong
     locations, violating the organizational pattern and creating confusion.
     Anti-Gravity will use this structure to:

     - Determine where to create new feature files
     - Know where to find existing code when debugging
     - Maintain consistency in file placement across the project -->

<!-- Document the ACTUAL folder organization with annotations explaining
     the purpose of each directory.

     Example:
     src/
     ├── app/               # Next.js App Router — pages and layouts ONLY
     │   ├── (auth)/        # Auth pages (login, register)
     │   └── (dashboard)/   # Authenticated pages
     ├── features/          # Feature-based modules — PRIMARY CODE LOCATION
     │   ├── projects/      # Everything related to projects
     │   │   ├── components/
     │   │   ├── hooks/
     │   │   ├── actions/
     │   │   ├── queries/
     │   │   ├── schemas/
     │   │   └── types.ts
     │   └── [other features follow same structure]
     ├── shared/            # Code used by 3+ features
     └── infrastructure/    # Technical plumbing — NOT business logic -->

```text
[Fill in actual folder structure with annotations]
Placement Rules
<!-- Numbered rules for where new code goes. Unambiguous enough to answer placement questions without consulting the team. -->
[Placement rule 1]

[Placement rule 2]

[Placement rule 3]

[Placement rule 4]

Never [critical exclusion 1]

Never [critical exclusion 2]

MAJOR DOMAINS AND COMPONENTS
<!-- WHY THIS MATTERS: Naming the major domains helps Anti-Gravity respect ownership when designing, reviewing, or implementing. Each domain owns specific data, behavior, and workflows. Crossing domain boundaries should be explicit and deliberate — never accidental. -->
Domain / Component Map
Domain Owns Does NOT Own Can Import From
[Domain] [Data / behavior / workflows it owns] [What is explicitly excluded] [Allowed dependencies]
[Domain] [What it owns] [What it excludes] [Allowed imports]
[Domain] [What it owns] [What it excludes] [Allowed imports]
Shared Components and Utilities
<!-- What shared layers or packages exist across domains? Examples: UI component library, shared utility package, internal SDK, validation library, logging package, API client layer, auth middleware -->
[Shared area] — [what it is for, what it must NOT become]

[Shared area] — [purpose and limits]

### Guidance for Anti-Gravity (Folder Structure)

Respect domain boundaries when designing, reviewing, or implementing

Do not recommend moving responsibility across domains casually

If a task crosses domain boundaries, make that explicit

Do not push domain logic into shared layers unless that is truly intended

If a shared area is acting as an architecture dumping ground, flag it

OWNERSHIP MODEL
<!-- WHY THIS MATTERS: Ambiguous ownership is an architectural smell. When two areas appear to co-own the same concept, bugs hide in the seam between them. Anti-Gravity uses this to avoid recommendations that blur ownership and to flag situations where ownership is unclear. -->
Data Ownership
<!-- Which domain or service owns which source of truth? Who is the authoritative writer for each important data entity? -->
[Data entity] — owned by [domain]

[Data entity] — owned by [domain]

Behavioral Ownership
<!-- Which domain owns which decisions, state transitions, or workflows? Who is responsible for enforcing each important business rule? -->
[Behavior / workflow] — owned by [domain]

[Behavior / workflow] — owned by [domain]

Team Ownership
<!-- If relevant, which team or person owns which area? -->
[Area] — owned by [team/person]

### Guidance for Anti-Gravity (Ownership)

Avoid recommendations that blur ownership

Treat ambiguous ownership as an architectural smell worth naming

If multiple areas appear to co-own the same concept, flag it explicitly

COMMUNICATION PATTERNS
<!-- WHY THIS MATTERS: How components talk to each other determines failure modes, latency characteristics, and coupling risk. Recommending a new interaction pattern without understanding the existing ones creates inconsistency and unexpected behavior. Anti-Gravity uses this to match design guidance to the actual communication model in use. -->
Current Interaction Patterns
Pattern Used For Notes
[Pattern] [What it handles] [Key constraints or conventions]
[Pattern] [What it handles] [Notes]
[Pattern] [What it handles] [Notes]

### Guidance for Anti-Gravity (Communication Patterns)

Do not recommend introducing new interaction patterns casually

If the current pattern is problematic, state why explicitly rather
than silently switching models

Match design guidance to the actual communication model already in use

DATA FLOW
<!-- WHY THIS MATTERS: Anti-Gravity uses data flow to trace how data moves through the system. When debugging, it follows this flow to locate where data might be corrupted, lost, or delayed. When building features, it follows this flow to ensure new code integrates correctly at the right points — not at layers it bypasses or skips. -->
Primary Read Flow
[Trace from user action to data return]

Example:
User action (click / navigate)
  │
  ▼
UI Component
  │
  ▼
Data-fetching hook / React Query
  │  Manages caching, loading states, refetch
  ▼
Server Action or API route
  │  Auth check + input validation
  ▼
Query / service function
  │  Encapsulates all DB access
  ▼
Database
  │
  ▼
Response flows back up the same chain
  │
  ▼
Cache updated → Component re-renders with data
Primary Write / Mutation Flow
[Trace from user action to confirmed state change]

Example:
User action (form submit / button click)
  │
  ▼
UI Component calls mutation handler
  │  Optionally: optimistic update applied immediately
  ▼
Server Action
  │  1. Validates input (Zod schema)
  │  2. Checks authorization
  │  3. Calls mutation function
  │  Returns: { success: true, data } | { success: false, error }
  ▼
Mutation / query function
  │  Encapsulated DB write
  ▼
Database write confirmed
  │
  ▼
Cache invalidated → Component re-renders with updated data
  │  On failure: optimistic update reverted
Async / Background Flow
[Trace from trigger to completion]

Example:
Trigger (user action / scheduled job / webhook)
  │
  ▼
Server Action enqueues job
  │  Job type, payload, priority, retry config
  ▼
Queue (Redis-backed / message queue)
  │
  ▼
Worker process picks up job
  │  Processes async work (email, report, export, etc.)
  ▼
Writes result to database
  │  On failure: retries per config → dead letter queue
  ▼
Client discovers result via polling / push / refetch
Critical Flows
Flow Name Path Summary Failure Impact
[Flow] [Brief path] [What breaks when this fails]
[Flow] [Brief path] [Impact]
[Flow] [Brief path] [Impact]
Key Data Flow Rules
<!-- The rules that govern how data is allowed to move. These prevent shortcuts that create hidden coupling. -->
Data always flows through defined layers — no shortcuts

[Rule — e.g., components never call the database directly]

[Rule — e.g., Server Actions never bypass input validation]

[Rule — e.g., all cross-feature data access goes through the
owning feature's query functions]

Background jobs write results to the database — never directly
to the client

## KEY ARCHITECTURAL PATTERNS

<!-- WHY THIS MATTERS: Anti-Gravity must follow these patterns when
     generating code or making recommendations. Introducing new patterns
     for problems already solved by existing ones creates inconsistency
     and increases cognitive load. Every pattern here represents a
     deliberate team decision — not a suggestion to revisit casually. -->

### Patterns We Use

| Pattern | Where Applied | How It Works | When NOT to Use |
| --- | --- | --- | --- |
| [Pattern] | [Location] | [How it works] | [When to skip it] |
| [Pattern] | [Location] | [How it works] | [When to skip it] |
| [Pattern] | [Location] | [How it works] | [When to skip it] |

### Patterns We Avoid

<!-- Explicitly name patterns that have been ruled out — and why.
     This prevents Anti-Gravity from re-suggesting them. -->

- **[Pattern]** — [why it is avoided in this project]
- **[Pattern]** — [why it is avoided]
- **[Pattern]** — [why it is avoided]

### Pattern Adoption Rules

<!-- The threshold for introducing new patterns.
     These rules prevent one-off improvisation from fragmenting the
     codebase. -->

- Before introducing a new pattern, verify no existing pattern solves
  the problem

- If a new pattern is genuinely needed, document it in this file
  before using it

- Do not create one-off patterns — if it is worth doing once, it is
  worth standardizing

- If an existing pattern is insufficient, make the gap explicit before
  diverging

### Guidance for Anti-Gravity (Patterns)

- Use these patterns as the first answer to any structural
  implementation question

- Only deviate with explicit justification
- When proposing a deviation, explain what the existing pattern
  cannot do

- Do not suggest patterns from the avoided list without acknowledging
  they were deliberately excluded

---

## ARCHITECTURAL DEFAULTS

<!-- WHY THIS MATTERS: Every system develops preferred approaches for
     common concerns. Anti-Gravity uses these defaults to stay consistent
     with existing code rather than introducing new primitives that
     fragment the codebase. The default answer to most implementation
     questions should come from this table — not from generic best
     practices. -->

| Concern | Default Approach | Notes |
| --- | --- | --- |
| Business logic placement | [Fill in] | [Notes] |
| Integration / external service logic | [Fill in] | [Notes] |
| Input validation | [Fill in] | [Notes] |
| Cross-domain coordination | [Fill in] | [Notes] |
| New feature placement | [Fill in] | [Notes] |
| Async / background work | [Fill in] | [Notes] |
| Error handling | [Fill in] | [Notes] |
| Shared utility placement | [Fill in] | [Notes] |

### Guidance for Anti-Gravity (Architectural Defaults)

- Use these defaults as the first answer to any placement or
  structural question in the relevant concern area

- Only deviate from a default with explicit justification
- When proposing a deviation, explain the gap the default cannot fill

---

## ARCHITECTURAL DECISIONS RECORD

<!-- WHY THIS MATTERS: Anti-Gravity should not re-debate decisions that
     have already been made with full analysis. This table captures the
     key decisions and their rationale so Anti-Gravity can reference them
     instead of proposing alternatives that were already considered and
     rejected. The "Revisit When" column prevents these decisions from
     becoming permanent by default — they have defined conditions for
     reconsideration. -->

| # | Decision | Choice Made | Alternatives Considered | Why This Choice | Date | Revisit When |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [Decision topic] | [What was chosen] | [What was considered] | [Why this won] | [Date] | [Condition to reconsider] |
| 2 | [Decision topic] | [Choice] | [Alternatives] | [Rationale] | [Date] | [Revisit trigger] |
| 3 | [Decision topic] | [Choice] | [Alternatives] | [Rationale] | [Date] | [Revisit trigger] |

### Architectural Decisions Already Locked

<!-- Decisions that are stable and should not be casually challenged.
     These represent the foundational commitments the entire system is
     built on. Changing them requires deliberate architectural review,
     explicit documentation, and updates to all affected context files. -->

1. **[Decision 1]** — [Why it is locked and what it protects]
2. **[Decision 2]** — [Why it is locked]
3. **[Decision 3]** — [Why it is locked]
4. **[Decision 4]** — [Why it is locked]
5. **[Decision 5]** — [Why it is locked]

### Guidance for Future Architectural Changes

<!-- If the architecture genuinely needs to change, use this process.
     Architectural drift without documentation is more dangerous than
     the problem being solved. -->

1. Identify exactly which boundary or decision is failing and why
2. Explain why the current model is genuinely insufficient
3. Document the new decision explicitly in this file and the ADR table
4. Update all affected context files to reflect the change
5. Avoid silent drift — architectural changes must be explicit
   decisions, not casual local edits

---

## MODULE BOUNDARIES

<!-- WHY THIS MATTERS: Module boundaries determine where new code lives,
     which modules a change should not touch, when a feature is trying
     to do too much, and whether a proposed change requires cross-module
     coordination. Violating boundaries creates hidden coupling, makes
     code harder to change, and increases the blast radius of bugs.
     Anti-Gravity uses this table to catch boundary violations before
     they are written. -->

### Module Boundary Map

| Module | Owns | Does NOT Own | Can Import From |
| --- | --- | --- | --- |
| [Module] | [What it owns] | [What is excluded] | [Allowed dependencies] |
| [Module] | [What it owns] | [What is excluded] | [Allowed imports] |
| [Module] | [What it owns] | [What is excluded] | [Allowed imports] |

### Cross-Module Import Rules

<!-- The rules that govern dependencies between modules.
     These prevent circular dependencies and hidden coupling. -->

1. Modules **never** import directly from another module's internal
   code (components, hooks, actions, queries, handlers)

2. Modules **may** import type definitions from other modules
   (`import type { X } from '@/features/x/types'`)

3. If two modules need to share runtime code, it must be extracted
   to the shared layer

4. The shared layer never imports from feature modules (no upward
   dependencies)

5. The infrastructure layer never imports from feature or shared
   layers (leaf node — no app imports)

6. If a rule must be violated, it is a signal that boundaries need
   redesigning — not that the rule is wrong

### Boundary Rules

<!-- Important architectural boundaries that must be preserved.
     Anti-Gravity uses these to catch drift. If current code violates
     them, flag the mismatch explicitly rather than assuming the rule
     no longer applies. -->

- [Boundary rule 1 — e.g., frontend must not call the database directly]
- [Boundary rule 2 — e.g., external provider logic stays behind adaptor]
- [Boundary rule 3 — e.g., domain logic must not depend on UI concerns]
- [Boundary rule 4 — e.g., shared utilities must not contain domain logic]

### Guidance for Anti-Gravity (Module Boundaries)

- Use these boundaries to catch architectural drift before it is written
- If current code violates a boundary, flag the mismatch explicitly
  rather than assuming the rule is obsolete

- If a boundary needs to change, that is an architectural decision —
  document it

---

## ARCHITECTURAL ANTI-PATTERNS

<!-- WHY THIS MATTERS: Named anti-patterns give Anti-Gravity specific,
     actionable guidance about what NOT to do in this architecture.
     Generic warnings are easy to ignore. Named patterns with "what it
     looks like / why harmful / what to do instead" are harder to miss
     and easier to catch during review. -->

### Layer Leakage

**What it looks like:** Project-specific facts placed in universal
layers; domain behavior placed in context or utility layers; workflow
steps embedded inside skill or domain files.
**Why it is harmful:** Makes the system harder to reason about, causes
duplication across layers, and creates contradiction risk when one
layer is updated but the other is not.
**What to do instead:** Respect the role boundaries of each layer.
If placement is unclear, use the Decision Rule routing test.

### Ownership Blurring

**What it looks like:** Two modules co-owning the same concept.
Data written by one module, read authoritatively by another. State
transitions for the same entity spread across multiple services or
layers with no single owner.
**Why it is harmful:** Creates hidden coupling, produces inconsistent
state, and makes debugging dramatically harder — the bug lives in the
seam between two owners, where neither side feels responsible.
**What to do instead:** Assign explicit ownership to every concept.
If a concept is shared, one module owns it and others consume it.
If ownership is genuinely unclear, flag it as an architectural smell
before building on top of it.

### Shared Layer as Dumping Ground

**What it looks like:** Business logic, domain rules, or feature-
specific code accumulating in shared utilities or common packages
because it was "easier to put it there."
**Why it is harmful:** Shared layers become tightly coupled to domain
concerns, making them impossible to change without ripple effects
across every consumer.
**What to do instead:** Shared layers reduce duplication of genuinely
generic code. Domain logic belongs in its owning module. If a shared
area is growing domain-specific concerns, flag it.

### Silent Architectural Drift

**What it looks like:** Boundaries or patterns quietly changing in
code without being documented. New files placed in incorrect
locations. Old patterns coexisting with new ones without explanation.
**Why it is harmful:** Future work is built on inconsistent
assumptions. Onboarding becomes confusing. The architecture document
diverges from reality and loses its value.
**What to do instead:** Architectural changes are explicit decisions.
Update this file and the ADR when patterns or boundaries change.

### Re-Litigating Locked Decisions

**What it looks like:** Suggesting architectural alternatives that
were already evaluated and deliberately rejected — without
acknowledging that the decision was already made.
**Why it is harmful:** Wastes time, creates confusion about whether
the architecture is settled, and may lead to inconsistent
implementations if the suggestion is partially adopted.
**What to do instead:** Check the ADR before proposing major
structural changes. If the trigger condition for reconsideration has
been met, name it explicitly rather than re-opening the debate
without context.

### Debt Compounding

**What it looks like:** New code added to known debt areas that
follows the debt pattern rather than the intended pattern. Debt
normalized into the architecture by repetition until it is
indistinguishable from intentional design.
**Why it is harmful:** Debt becomes exponentially more expensive
to pay down as more code depends on the broken pattern. What starts
as a known temporary compromise becomes a permanent structural
constraint.
**What to do instead:** When working near a known debt area, follow
the intended pattern — not the existing debt pattern. If the debt
makes the correct approach impractical, flag it explicitly rather
than silently reinforcing it.

## KNOWN ARCHITECTURAL DEBT

<!-- WHY THIS MATTERS: Anti-Gravity should be aware of existing debt so
     it does not accidentally make it worse. When working in debt areas,
     recommendations should acknowledge the debt rather than build on top
     of it as if the foundation were clean. The "Risk if Ignored" column
     makes debt visible and accountable — not just documented and
     forgotten. -->

| # | Debt Item | Location | Impact | Why It Exists | Risk if Ignored | Plan |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [Debt description] | [File / module] | [User or system impact] | [Why it was built this way] | [What gets worse] | [Fix plan or accepted risk] |
| 2 | [Debt description] | [Location] | [Impact] | [Why] | [Risk] | [Plan] |
| 3 | [Debt description] | [Location] | [Impact] | [Why] | [Risk] | [Plan] |

### Guidance for Anti-Gravity

- When working in a debt area, acknowledge the debt rather than
  building on it as if it is clean

- Do not recommend solutions that depend on debt being resolved
  unless the resolution is part of the same task

- If a recommendation would make debt worse, flag it explicitly
- If a debt item has a plan, prefer solutions that align with
  that direction

---

## KNOWN WEAK SPOTS AND HOTSPOTS

<!-- WHY THIS MATTERS: Not all problem areas are the same. Fragile areas
     break easily under change. Confusing areas cause misunderstanding
     and incorrect assumptions. High-change areas accumulate drift
     through churn. Extra-caution areas carry disproportionate cost
     when mistakes happen. Each category requires a different kind of
     care — naming them separately tells Anti-Gravity not just WHERE
     to be careful but WHY and WHAT KIND of careful to be. -->

### Fragile Areas

<!-- Where breakage is likely under change — handle with extra care,
     test thoroughly, avoid casual edits. -->

- [Area] — [why it is fragile and what tends to break]
- [Area] — [why it is fragile]
- [Area] — [why it is fragile]

### Confusing Areas

<!-- Where understanding is low, intent is unclear, or the code
     diverges from what the surrounding architecture would suggest.
     High risk of incorrect assumptions during implementation. -->

- [Area] — [what is confusing and what assumptions are dangerous here]
- [Area] — [what is confusing]
- [Area] — [what is confusing]

### High Change Frequency Areas

<!-- Where churn is constant, creating ongoing risk of drift,
     regression, and boundary erosion. Extra care needed to preserve
     pattern consistency despite frequent edits. -->

- [Area] — [why it changes often and what risk that creates]
- [Area] — [why it changes often]
- [Area] — [why it changes often]

### Areas Requiring Extra Caution

<!-- Where mistakes are especially costly — to users, to the business,
     to data integrity, or to system stability. Anti-Gravity should
     escalate rigor, test depth, and review care proportionally here. -->

- [Area] — [why mistakes here are especially costly]
- [Area] — [why mistakes here are especially costly]
- [Area] — [why mistakes here are especially costly]

### Guidance for Anti-Gravity (Weak Spots)

- Treat fragile areas as high-breakage risk — test before and after
- Treat confusing areas as assumption traps — verify intent before
  building on them

- Treat high-change areas as drift-risk zones — check pattern
  consistency before adding to them

- Treat extra-caution areas as elevated-rigor surfaces — slow down,
  review more carefully, prefer smaller changes

---

## INTEGRATION POINTS

<!-- WHY THIS MATTERS: Anti-Gravity needs to understand what external
     systems the application depends on to properly handle failures,
     understand data flow, and respect integration constraints. External
     systems impose their own rate limits, retry requirements, idempotency
     expectations, and failure modes. Ignoring these leads to integration
     code that works in development but fails in production. -->

| System | Purpose | Integration Method | Auth | Failure Impact | Failure Handling |
| --- | --- | --- | --- | --- | --- |
| [System] | [What it is used for] | [SDK / REST / webhook] | [Auth method] | [What breaks when it fails] | [Retry / fallback / alert] |
| [System] | [Purpose] | [Method] | [Auth] | [Impact] | [Handling] |
| [System] | [Purpose] | [Method] | [Auth] | [Impact] | [Handling] |

### External Integration Boundaries

<!-- Every external provider should be accessed through a deliberate
     abstraction boundary — not scattered across unrelated modules.
     This section defines where each integration is abstracted and
     what the boundary looks like. -->

- **[Provider]** — abstracted at [location]; failure mode: [what happens]
- **[Provider]** — abstracted at [location]; failure mode: [what happens]

### Guidance for Anti-Gravity (Integration Points)

- External providers should always be accessed through their defined
  integration boundary — not called directly from business logic

- Do not spread third-party coupling across unrelated modules
- Factor provider failure into architecture, debugging, and design
  guidance

- Consider rate limits, retry requirements, and idempotency when
  working near any external integration

---

## SCALING NOTES

<!-- WHY THIS MATTERS: Anti-Gravity should understand current capacity
     limits to avoid suggesting solutions that work at scale but are
     unnecessary at current volume — or solutions that work now but will
     break soon. Knowing the thresholds prevents both over-engineering
     and under-engineering. -->

| Component | Current Capacity | Current Usage | Bottleneck Threshold | Scaling Plan |
| --- | --- | --- | --- | --- |
| [Component] | [Estimated capacity] | [Current peak usage] | [When it becomes a problem] | [Plan or accepted risk] |
| [Component] | [Capacity] | [Usage] | [Threshold] | [Plan] |
| [Component] | [Capacity] | [Usage] | [Threshold] | [Plan] |

### Guidance for Anti-Gravity (Scaling)

- Do not recommend solutions that work at scale if they are premature
  for current volume — complexity has a real cost

- Do not recommend solutions that work now but will clearly break at
  the next order of magnitude

- When a scaling threshold is close, name it rather than ignoring it

---

## CURRENT ARCHITECTURAL STATE

<!-- WHY THIS MATTERS: Knowing the build status of each layer prevents
     Anti-Gravity from assuming maturity that does not yet exist, or from
     treating planned layers as if they are already active. This section
     is the honest status report — not a wishlist. -->

### Layer Build Status

| Layer | Status | Notes |
| --- | --- | --- |
| [Layer] | [Complete / Active / In progress / Planned / Not yet built] | [Relevant context] |
| [Layer] | [Status] | [Notes] |
| [Layer] | [Status] | [Notes] |

### Current Architectural Frontier

<!-- What is the active edge of the build right now? -->

- **Active now:** [What is currently being built or stabilized]
- **Next:** [What follows after the current frontier is complete]
- **Deferred:** [What is intentionally not being built yet]

---

## ARCHITECTURAL STRENGTHS

<!-- WHY THIS MATTERS: Anti-Gravity should preserve what is working well
     rather than "fixing" things that are actually good. Knowing the
     strengths of the current architecture prevents well-intentioned
     recommendations from eroding them. -->

- [Strength 1] — [why it matters and what it enables]
- [Strength 2] — [why it matters]
- [Strength 3] — [why it matters]

### Guidance for Anti-Gravity (Strengths)

- Preserve these strengths when making recommendations
- Do not recommend changes that would erode a known strength without
  a compelling reason

- When a recommendation touches a strength area, acknowledge it
  explicitly

---

## CURRENT ARCHITECTURAL WEAKNESSES AND PAIN POINTS

<!-- WHY THIS MATTERS: Known weaknesses are areas to treat cautiously.
     Architecture, review, and refactor recommendations should account
     for existing pain rather than assuming a clean foundation.
     Naming weaknesses also prevents Anti-Gravity from accidentally
     making them worse. -->

- [Weakness 1] — [what it causes and where it hurts]
- [Weakness 2] — [what it causes]
- [Weakness 3] — [what it causes]

### Guidance for Anti-Gravity (CURRENT ARCHITECTURAL WEAKNESSES)

- Treat these as known uncertainty zones — not settled, clean design
- Do not build on top of a weakness as if it were solid
- When working near a weak area, acknowledge the risk explicitly
- If a recommendation would make a weakness worse, flag it

---

## ARCHITECTURAL CONSTRAINTS

<!-- WHY THIS MATTERS: Real constraints shape what is architecturally
     possible. Anti-Gravity must not recommend structurally clean changes
     that ignore real-world limitations. If a recommendation depends on
     relaxing a constraint, that dependency must be stated explicitly. -->

### Hard Constraints

<!-- Fixed constraints that cannot be changed without significant
     external action — budget, team size, compliance, contract,
     legacy system coupling. -->

- [Hard constraint 1] — [why it exists and what it rules out]
- [Hard constraint 2] — [why it exists]
- [Hard constraint 3] — [why it exists]

### Soft Constraints and Preferences

<!-- Semi-fixed constraints or strong preferences that guide decisions
     but can be revisited with good reason. -->

- [Soft constraint 1]
- [Soft constraint 2]
- [Soft constraint 3]

### Current Debt and Transitional Structure

<!-- Areas where the architecture is in transition — old patterns
     coexisting with new ones, migrations in progress, debt that is
     known but not yet addressed. -->

- [Transitional area 1] — [old state → intended new state]
- [Transitional area 2] — [transition description]
- [Transitional area 3] — [transition description]

### Guidance for Anti-Gravity (ARCHITECTURAL CONSTRAINTS)

- Do not recommend changes that ignore hard constraints
- If a recommendation depends on relaxing a constraint, name that
  dependency explicitly

- In transitional areas, prefer solutions that move toward the
  intended new state rather than reinforcing the old one

---

## ARCHITECTURAL EVOLUTION DIRECTION

<!-- WHY THIS MATTERS: Architecture is not static. Knowing where the
     system is intended to go helps Anti-Gravity make recommendations
     that move in the right direction — rather than optimizing for the
     current state in ways that make future evolution harder. -->

### Intended Direction

- [Evolution direction 1] — [why this matters and what it enables]
- [Evolution direction 2] — [direction and motivation]
- [Evolution direction 3] — [direction and motivation]

### What Should NOT Change

<!-- What architectural commitments should stay stable even as the
     system evolves? -->

- [Stable commitment 1]
- [Stable commitment 2]

### Guidance for Anti-Gravity (ARCHITECTURAL EVOLUTION DIRECTION)

- Recommendations should align with the intended evolution direction
  where appropriate

- Avoid optimizing for current state in ways that make future
  evolution significantly harder

- If current architecture and intended direction conflict, flag it
  explicitly rather than picking one silently

---

## WHAT GOOD TECHNICAL WORK LOOKS LIKE IN THIS ARCHITECTURE

<!-- WHY THIS MATTERS: Generic engineering quality standards exist. But
     "good" has an architecture-specific meaning that depends on the
     current structure, team, and evolution direction. This section
     defines what quality means HERE — so Anti-Gravity applies the right
     standard for this context. -->

- New behavior is placed in the correct layer or domain — not wherever
  is most convenient

- Business logic stays in its appropriate layer — never in transport,
  UI, or infrastructure layers

- Ownership remains explicit — every new module or function has a
  clear home

- Interfaces remain simpler than internal complexity — consumers should
  not need to understand internal implementation to use a boundary

- Changes strengthen the current architectural direction rather than
  eroding it

- New integrations are isolated behind clear abstraction boundaries
- Structural recommendations are proportionate to actual system needs —
  not aspirationally over-engineered

- [Project-specific definition of good — fill in]
- [Project-specific definition — fill in]

---

## OPEN ARCHITECTURE QUESTIONS

<!-- WHY THIS MATTERS: Not all architectural questions are settled.
     Anti-Gravity should not treat unresolved areas as if they have
     clear answers. When reasoning about open questions, it should
     surface the uncertainty rather than silently picking a direction. -->

- [Open question 1 — what is still undecided or contested]
- [Open question 2 — what may change soon]
- [Open question 3 — what depends on future information]

---

## ASSUMPTIONS AND UNKNOWNS

<!-- WHY THIS MATTERS: Some architectural assumptions are currently
     stable but not fully confirmed. Anti-Gravity should treat these as
     uncertainty zones — not settled design. When these areas come up
     in a task, surface the uncertainty rather than assuming the
     assumption is solid.

     Rule: if the real architecture differs from this documentation,
     trust observed reality and note the mismatch — do not defend
     stale documentation against live code. -->

- [Assumption 1 — assumed but not fully confirmed]
- [Assumption 2 — true now but may evolve]
- [Assumption 3 — depends on a future decision]

---

## INSTRUCTIONS FOR ANTI-GRAVITY

When working inside this architecture, Anti-Gravity must:

1. **Reason from the actual architecture** — not from generic best
   practices alone. The current structure is the starting point for
   every recommendation.

2. **Preserve clear ownership boundaries** unless there is a strong,
   explicit reason to change them. Blurring ownership is an
   architectural cost, not a convenience.

3. **Match recommendations to the current layering and communication
   patterns.** Do not introduce new structural primitives casually.

4. **Make cross-boundary impacts explicit.** If a change touches more
   than one module or layer, name that explicitly.

5. **Prefer the project's architectural defaults** before inventing
   new structural patterns. The defaults table is the first answer
   to most placement questions.

6. **Flag architectural drift, ambiguity, or ownership mismatch
   clearly** rather than working around them silently.

7. **Respect known constraints and evolution direction.** Do not
   recommend changes that ignore hard constraints, and do not
   reinforce patterns being actively migrated away from.

8. **If the real architecture differs from this documentation, trust
   observed reality and note the mismatch** — do not defend stale
   documentation against live code.

9. **Do not assume "shared" means "free to put anything here."**
   Shared layers have rules. Violations should be flagged.

10. **Use this file to keep implementation, review, and design work
    aligned with system structure** — not just technically correct
    in isolation.

---

## CROSS-REFERENCES

<!-- WHY THIS MATTERS: This file is the structural map, but it does not
     stand alone. Related context files extend and specialize the
     grounding it provides. Anti-Gravity should load cross-referenced
     files when their domain is relevant to the task. -->

| Related Context File | Relationship |
| --- | --- |
| `project-context.md` | What this architecture is building and for whom |
| `stack-context.md` | The technology implementing this architecture |
| `build-status.md` | Current state of each architectural layer |
| `decision-log.md` | Full record of settled architectural decisions |
| `naming-conventions.md` | File, folder, and variable naming standards |
| `domain-rules.md` | Business logic rules this architecture enforces |
| `coding-standards.md` | Conventions applied within this architecture |
| `database-context.md` | Deep dive on the data layer |
| `infra-context.md` | Deep dive on operational infrastructure |

---

## TEMPLATE FILL-IN SUMMARY

### Required

*(Anti-Gravity is significantly degraded without these)*

- [ ] Current Architectural Reality — with IS NOT declarations
- [ ] Layer Model table — What Belongs / What Does NOT Belong
- [ ] Folder Structure — annotated tree with Placement Rules
- [ ] Major Domains / Component Map — Owns / Does NOT Own / Can Import
- [ ] Ownership Model — data + behavioral
- [ ] Module Boundary Map + Cross-Module Import Rules
- [ ] Boundary Rules
- [ ] Data Flows — read + write + async with ASCII diagrams
- [ ] Architectural Defaults table

### High Value

*(Strongly recommended)*

- [ ] Architectural Patterns table — with When NOT to Use column
- [ ] Patterns We Avoid
- [ ] Architectural Decisions Record — with Revisit When column
- [ ] Locked Architectural Decisions
- [ ] Known Architectural Debt table — with Risk if Ignored + Plan
- [ ] Known Weak Spots — all 4 categories
- [ ] Integration Points table — with Failure Impact + Failure Handling
- [ ] Architectural Constraints — Hard / Soft / Transitional

### Useful When Relevant

- [ ] Communication Patterns table
- [ ] Scaling Notes table
- [ ] Current Architectural State + Frontier
- [ ] Architectural Strengths
- [ ] Architectural Evolution Direction — with What Should NOT Change
- [ ] Weaknesses and Pain Points
- [ ] Open Architecture Questions
- [ ] Assumptions and Unknowns

---

## FINAL RULE

All implementation, debugging, review, and design suggestions should
respect the current architecture unless a deliberate architectural
change is explicitly being considered.

When placement is unclear: use the Decision Rule routing test.
When a boundary would be crossed: name it and justify it.
When a decision was already made: reference it, do not re-litigate it.
When the architecture needs to change: document it, do not drift silently.
When this file is stale: update it — stale architecture context is
actively harmful.

---

## AUTHORITATIVENESS

If another file appears to contradict this one on system structure,
layer responsibilities, module boundaries, or architectural decisions,
this file is authoritative unless an explicit project-level override
is documented in `decision-log.md` or a more specialized context file
such as `database-context.md`, `infra-context.md`, or `domain-rules.md`.
