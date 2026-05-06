# BENCHMARK: ARCHITECTURE

**Version:** Gold v1.0
**Layer:** 11 — Verification
**Loading Tier:** 3 — **LOADED ON DEMAND**

***

## PURPOSE

This file contains repeatable test scenarios for evaluating Anti-Gravity's
architectural decision-making — problem framing, boundary design, option
comparison, tradeoff reasoning, and recommendation quality.

### Evaluate With

- [rubric-architecture.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-architecture.md)
- [rubric-communication.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-communication.md)

### Tests

- `skill-architecture.md`
- `workflow-plan-architecture.md`

***

## WHAT THIS BENCHMARK TESTS

This benchmark evaluates whether Anti-Gravity can:

- Define the real architectural problem before proposing solutions
- Choose appropriate system and module boundaries
- Generate and compare multiple viable structural options
- Reason about scale, failure, changeability, and operational cost
- Avoid overbuilding and trend-driven pattern selection
- Make tradeoffs visible — both what is gained and what is sacrificed
- Recommend practical architecture grounded in real context and team maturity
- Align structure with product stage, not just engineering preference

This benchmark should reveal whether Anti-Gravity thinks like a
systems-minded architect or a pattern-name generator.

***

## HOW TO USE THESE BENCHMARKS

1. Pick a scenario below
2. Present it to Anti-Gravity as a real task — do not mention it is a benchmark
3. Let Anti-Gravity process it using its full system — skills, contexts, and workflows active as appropriate
4. Evaluate the output against the rubrics listed above
5. Record the score in `memory/benchmark-results.md`
6. Compare scores across runs and versions to track improvement

***

## EVALUATION DIMENSIONS

Score benchmark outputs across these dimensions:

1. Problem framing — was the real architectural question identified?
2. System boundary clarity — are responsibilities explicit?
3. Option quality — were multiple viable structures compared?
4. Tradeoff reasoning — were costs and benefits named honestly?
5. Simplicity discipline — was the simplest sufficient structure favored?
6. Data and ownership thinking — where does truth live?
7. Failure awareness — how does this fail? What is the blast radius?
8. Time-horizon reasoning — what is hard to reverse? What can evolve?
9. Team and operational realism — can this team build and run this?
10. Communication clarity — can a teammate act on this recommendation?

***

## SCENARIO 1 — New Feature Module Decision

### Prompt [SCENARIO 1]

We need to add a notification system to the product. Users should
receive in-app notifications and email notifications for events like
task assignment, sprint start, and comments on their tasks. How
should we architect this?

### What Excellent Output Looks Like [SCENARIO 1]

- Asks clarifying questions about scale, delivery requirements — real-time versus batched — and user preference controls
- Defines requirements before designing — what events trigger notifications, what channels, what user control is needed
- Generates three or more genuine options:
  1. Simple — direct notification creation in existing server actions, synchronous
  2. Medium — event-driven with async queue for background processing
  3. Complex — full event bus with separate notification service
- Recommends the medium option for current scale with an explicit path to the complex option if needed
- Applies boring technology bias — uses existing infrastructure before introducing new systems
- Applies the 2 AM test — can a mid-level engineer debug notification failures without heroic effort?
- Considers preference and delivery edge cases — per-user muting, email batching, deduplication
- Addresses failure modes — what happens if email delivery fails? Retry, dead letter queue, observability
- Proposes data model for the notifications table
- Documents the decision as an ADR

### Red Flags [SCENARIO 1]

- Jumps to complex event-driven architecture without justifying the added complexity
- Considers only one option
- No consideration of failure modes or delivery guarantees
- Ignores existing infrastructure already in place
- No data model proposed
- Over-engineers for scale the product does not yet have

***

## SCENARIO 2 — Technology Choice

### Prompt [SCENARIO 2]

We need to add full-text search across tasks, comments, and project
names. Our existing database text search queries are too slow with
50K or more records. What should we use?

### What Excellent Output Looks Like [SCENARIO 2]

- Defines requirements first — what fields, what query patterns, expected data volume, acceptable latency
- Generates three or more options with honest evaluation:
  1. Database trigram index plus GIN index — no new infrastructure
  2. Lightweight self-hosted search — simple, minimal ops
  3. Managed search service — powerful, more expensive
  4. Elasticsearch — powerful, operationally complex, likely overkill
- Evaluates each against team capability, operational burden, cost, performance, and integration effort
- Applies boring technology bias — start with database-native option if it meets requirements
- Explains clearly why the most complex option is not recommended at current scale
- Considers the synchronization problem — how does the search index stay consistent with the database?
- Considers degradation — what happens when search is unavailable? Degrade to basic filtering rather than hard failure
- Classifies the decision by reversibility — can we switch search engines later if needed?

### Red Flags [SCENARIO 2]

- Recommends the most complex option without considering simpler ones
- No evaluation against team capability or operational burden
- Ignores the database-native option entirely
- Does not address index synchronization with the source of truth
- No consideration of failure or degradation behavior

***

## SCENARIO 3 — Scaling Architecture Decision

### Prompt [SCENARIO 3]

We are hitting our database connection limit during peak hours.
Our serverless functions each open their own connection pool. What
should we do?

### What Excellent Output Looks Like [SCENARIO 3]

- Identifies the structural problem — serverless plus per-function connection pools equals connection exhaustion under concurrency
- Defines the problem quantitatively — how many concurrent functions? What is the peak connection count? What is the limit?
- Generates three or more options:
  1. Add a connection pooler between application and database
  2. Use a managed connection pooling service
  3. Upgrade database instance for more connections — band-aid
  4. Reduce connections per function immediately — quick win
- Evaluates tradeoffs for each:
  - Connection pooler — effective but adds infrastructure to operate
  - Managed service — simplest operationally but vendor dependency
  - Instance upgrade — treats the symptom, not the cause
  - Reduce per-function connections — quick win, limits per-function concurrency
- Recommends a sequenced approach — immediate quick win plus structural fix in parallel
- Explains clearly why the instance upgrade is a band-aid and not the right answer
- Classifies the decision by reversibility — some choices here are harder to undo than others

### Red Flags [SCENARIO 3]

- Recommends upgrading the database instance as the primary solution
- Only one option considered
- Does not understand the serverless connection pool problem
- No quantitative analysis of current connection usage
- Ignores the cheapest and fastest immediate win

***

## SCENARIO 4 — Monolith Versus Service Split

### Prompt [SCENARIO 4]

A growing product currently runs as one backend. The team is debating
whether to split out services. How should we evaluate this decision?

### What Excellent Output Looks Like [SCENARIO 4]

- Asks what the actual pain is — is this driven by deployment coupling, team ownership friction, or performance?
- Distinguishes between modular monolith improvements and a full service split
- Evaluates the real decision criteria — not ideology:
  - Current coupling and ownership pain
  - Team size and maturity
  - Deployment and operational burden of each option
  - The cost of distributed systems — observability, latency, partial failure, data consistency
- Recommends staying modular monolith unless a specific and concrete pain makes the service split worthwhile
- Names what would need to be true to justify the split
- Addresses reversibility — splitting is expensive to undo
- Grounds recommendation in current product and team reality, not trend or future aspiration

### Red Flags [SCENARIO 4]

- Recommends microservices by reflex because the product is "growing"
- No team or operational realism
- No concrete current-pain framing
- No boundary or ownership analysis
- No reversibility thinking
- Recommendation not tied to any specific problem being solved

***

## SCENARIO 5 — Multi-Tenant Data Boundary

### Prompt [SCENARIO 5]

Design a multi-tenant boundary for an application where users from
different organizations must never see each other's data.

### What Excellent Output Looks Like [SCENARIO 5]

- Treats this as a security and correctness problem, not just a design preference
- Identifies tenant isolation as the primary constraint driving every other decision
- Evaluates structural options:
  1. Row-level filtering with organization ID on every query
  2. Schema-per-tenant isolation
  3. Database-per-tenant isolation
- Evaluates each on isolation strength, operational cost, migration complexity, and team capability
- Recommends row-level filtering for most products with explicit enforcement at the query layer — not reliance on calling code
- Addresses the blast radius — what does a data leakage incident look like at this boundary?
- Considers audit and compliance implications
- Notes that trust-boundary enforcement must be centralized — not scattered across individual endpoints

### Red Flags [SCENARIO 5]

- "Just filter by organization ID" with no enforcement strategy
- No trust-boundary seriousness
- No consideration of what happens if a query omits the filter
- No source-of-truth or enforcement-layer clarity
- No blast radius or incident consequence reasoning

***

## SCENARIO 6 — API Evolution Without Breaking Consumers

### Prompt [SCENARIO 6]

A core API is used by multiple internal teams and some external
clients. The team needs to evolve it to support richer filtering
and new fields without breaking existing consumers. How should this
be approached?

### What Excellent Output Looks Like [SCENARIO 6]

- Distinguishes between internal consumers (can be updated simultaneously) and external consumers (cannot)
- Defines additive evolution strategy — add new optional fields and parameters rather than changing or removing existing ones
- Addresses the boundary cases — what constitutes a breaking change? Field removal, type change, semantic change, status code change
- Generates options:
  1. Purely additive evolution in current version — simplest
  2. New version for significant structural changes
  3. Feature flags or API negotiation for gradual transition
- Recommends additive evolution as the default, versioning only when a breaking change cannot be avoided
- Discusses contract documentation and consumer communication
- Addresses the deprecation lifecycle — how do old patterns get retired safely?

### Red Flags [SCENARIO 6]

- Reflexively recommends "just make v2" without exploring additive evolution first
- No distinction between internal and external consumer impact
- No definition of what constitutes a breaking change
- No deprecation lifecycle
- No consideration of the cost of maintaining multiple versions

***

## SCENARIO 7 — Modernize a Legacy Module

### Prompt [SCENARIO 7]

A core legacy module is hard to change, poorly documented, and feared
by the team. Plan the architectural path forward.

### What Excellent Output Looks Like [SCENARIO 7]

- Does NOT recommend a big-bang rewrite
- Evaluates the debt-interest question — is the pain worth the migration cost?
- Identifies the strategy — strangler pattern or seam extraction rather than replacement
- Emphasizes behavior preservation as the primary constraint — hidden business rules must be discovered, not assumed away
- Proposes a realistic migration path — identify seams, add tests before changing structure, extract incrementally
- Considers the risk of rewriting something that carries undocumented business logic
- Addresses the team concern — how do you make this module safer to touch without a full rewrite?
- Defines success criteria — what does "modernized" actually mean in measurable terms?

### Red Flags [SCENARIO 7]

- Immediate rewrite recommendation
- No migration safety thinking
- No awareness of hidden business rules in legacy code
- No seam or strangler pattern thinking
- No incremental path — only big-bang options

***

## SCORING GUIDE

For each scenario, evaluate using `rubric-architecture.md` dimensions:

| Dimension | Weight for Architecture |
| :--- | :--- |
| Requirements Clarity | High — were requirements defined before designing? |
| Options Evaluation | Critical — were three or more genuine options considered? |
| Tradeoff Transparency | High — were gains AND sacrifices named explicitly? |
| Simplicity Discipline | High — was the simplest sufficient option favored? |
| Failure Mode Analysis | High — how does each option fail? What is the blast radius? |
| Team Fit | Medium — can the team build and maintain this? |
| Reversibility | Medium — how hard is it to change if the decision is wrong? |
| Boundary Clarity | Medium — are responsibilities and ownership clearly defined? |

Record all scores in `memory/benchmark-results.md`.

***

## FINAL RULE

A strong architecture benchmark response makes the system easier
to understand, change, and operate — not merely more sophisticated
on paper.

It shows:

- Why this structure exists and what problem it solves
- What it protects and what it costs
- How it fails and what the blast radius is
- How it evolves as the product grows
- Why it is the right fit for this team and system right now —
  not just a fashionable pattern
