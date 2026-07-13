---
status: template
scope: project
project_id: null
updated_at: null
owner: null
confidence: unset
---

# DATABASE CONTEXT

**Version:** Gold v2.0
**Layer:** 6 — Context (Ground Truth)
**Tier:** 2 — Loaded by task
**File:** contexts/database-context.md
**Purpose:** Defines the database posture, data-design discipline, schema patterns, access-pattern expectations, and migration mindset that Anti-Gravity must respect. This keeps data work grounded in real persistence concerns, not generic DB advice.
**Loaded When:** Schema design or changes, query writing, data modeling, migration planning, performance debugging, or any task involving persistent state.
**Maintenance:** Update when database choices are made or changed, schema conventions evolve, access patterns shift, or migration approach changes. Review at least quarterly or after major data-model changes.

---

## HOW ANTI-GRAVITY USES THIS FILE

This file is the **data-layer ground truth** for Anti-Gravity.

**When loaded**, Anti-Gravity will:

- Reason about data using your chosen persistence model (once selected)
- Tie schema and query suggestions to your real access patterns and invariants
- Respect ownership and source-of-truth boundaries when proposing changes
- Follow your migration posture (e.g., expand–contract, additive-first)
- Avoid suggesting patterns that conflict with how your system stores and evolves data

**When missing or incomplete**, Anti-Gravity will:

- Fall back to generic schema and indexing advice that may not fit your architecture
- Suggest migrations without awareness of your deployment or rollback constraints
- Miss domain-specific integrity rules and data-ownership expectations

**When stale**, Anti-Gravity will:

- Refer to tables, fields, or models that no longer exist
- Suggest optimizations based on outdated access patterns
- Reinforce legacy schema patterns you are trying to move away from

**Conflict rule:** If this file conflicts with a more specific stack- or infra-level database file (`stack-context.md`, infra-specific DB docs), the more specific file wins for that area. Anti-Gravity should flag the conflict instead of silently choosing.

**Authoritativeness rule:** When Anti-Gravity’s general database training conflicts with a convention or rule in this file, this file wins. Do not override these constraints for convenience unless this file is explicitly updated.

---

## CURRENT PROJECT POSITION

Anti-Gravity Gold has **not yet** committed to a specific database engine, storage model, or full runtime persistence architecture.

The project does **not** currently assume, by default:

- A particular engine (Postgres, MySQL, Mongo, etc.)
- A single model (purely relational, purely document, purely event sourced)
- ORM-first or raw-SQL-first as already chosen
- A fixed multi-tenant partitioning strategy
- A single-database or database-per-service topology

### Meaning

Database-oriented work at this stage should focus on:

- Data shapes and invariants
- Ownership and source of truth
- Access patterns and workload characteristics
- Migration and change safety
- Avoiding premature engine or tooling lock-in

This file therefore has two layers:

| Layer | Name | Contents | When Active |
| --- | --- | --- | --- |
| **Layer 1** | Philosophy | Engine-agnostic database discipline: ownership, invariants, access-pattern awareness, migration mindset | Active now — independent of concrete DB |
| **Layer 2** | Conventions | Concrete engine choice, schema conventions, access patterns, indexing, migrations, backup/retention, known issues | Filled in once a specific DB/ORM stack is chosen |

> **Maintenance rule:** Choosing or changing a database stack updates
> **Layer 2** (conventions). Changing **Layer 1** (philosophy) requires
> an explicit decision that the project’s persistence posture has
> changed.

---

## CURRENT SAFE DATABASE ASSUMPTIONS

These assumptions are safe to apply now:

### Assumption 1 — Persistent state will matter

Even before picking an engine, some parts of the system will need durable state. Those state shapes should be reasoned about deliberately, not left implicit.

### Assumption 2 — Data ownership must be explicit

There must be clarity about which domain or service owns which truths. “Anyone can change anything” is not acceptable for important data.

### Assumption 3 — Invariants matter before engine choice

Conceptual rules such as uniqueness, valid state transitions, required associations, ordering guarantees, and idempotency should be named early — before schemas exist.

### Assumption 4 — Migration safety will matter later

Future storage choices should be made with changeability and schema evolution in mind, not just initial convenience.

### Assumption 5 — Access patterns must shape design

Persistence design should eventually reflect how data is read, written, and queried — not only entity nouns and relationships.

### Assumption 6 — Storage decisions must be explicit, not accidental

The project should not drift into an engine or model simply because a library or example used it. Once chosen, the persistence stack should be named and justified.

---

## WHAT IS **NOT** SAFE TO ASSUME YET

Until a later file explicitly locks them in, future work must **not** silently assume:

- A specific storage model (pure relational, document, event-sourced, append-only log) as definitive
- A particular engine (e.g., Postgres vs Mongo) as already chosen
- ORM-first design, or raw-SQL-first, as the project default
- A settled denormalization or caching strategy
- A fixed multi-tenant partitioning model

### Meaning (Assumptions)

Any mention of a concrete database, schema style, or persistence pattern must make clear whether it is:

- An example
- A recommendation
- A hypothetical fit
- Or an already-approved decision

---

## CORE DATABASE RULES (PHILOSOPHY LAYER)

These rules apply now, regardless of the eventual engine.

### Rule 1 — Storage-choice language must be explicit

**Rule:** When future files talk about a specific database or model, they must state whether it’s illustrative or actually chosen.

**Meaning:** Avoid accidental pseudo-decisions about persistence that narrow options without agreement.

---

### Rule 2 — Data ownership must not be hand-waved

**Rule:** If an area stores or mutates important truth, the owner of that truth must be explicit.

**Meaning:** Designs where multiple areas casually mutate the same canonical records with no clear authority are suspect.

---

### Rule 3 — Invariants should be named early

**Rule:** Important constraints — uniqueness, valid transitions, required associations, ordering, idempotency — should be identified conceptually before schemas or migrations are written.

**Meaning:** Good data design starts from truth rules, not from table or document syntax.

---

### Rule 4 — Persistence design must be access-pattern aware

**Rule:** Data structures should be designed with workload in mind: expected reads/writes, what must be fast, what must be durable, and what must be easy to evolve.

**Meaning:** Avoid pure noun-and-relationship modeling without thinking about queries, scans, joins, and usage patterns.

---

### Rule 5 — Migration thinking must exist from the start

**Rule:** Even before concrete migrations exist, assume that changing persistent data later will be risky and non-trivial.

**Meaning:** Do not optimize only for “getting it working once” while ignoring the cost of future schema and data evolution.

---

## DATA STACK SUMMARY (TO BE FILLED WHEN CHOSEN)

Once a concrete stack is selected, capture it here.

### Primary Database (when decided)

[Example: PostgreSQL / MySQL / MongoDB / SQLite / managed serverless DB]

### Secondary Datastores (when applicable)

- [datastore 1] — [purpose]
- [datastore 2] — [purpose]
- [datastore 3] — [purpose]

Examples:

- Redis — caching, ephemeral state, jobs
- Search index — full-text or relevance search
- Analytics store — reporting and aggregates
- Object storage — files and large blobs
- Vector database — search/embedding-based retrieval

### Query / Access Layer (when applicable)

[Example: ORM (Prisma/EF/etc.), query builder, raw SQL, mixed]

### Migration System (when applicable)

[Example: Prisma Migrate, Flyway, Alembic, hand-written SQL scripts]

### Database Role In The System

[Short explanation of what the primary database is responsible for once chosen: system of record, transactional core, etc.]

---

## DATA DOMAINS AND OWNERSHIP (CONCEPTUAL)

Even before selecting an engine, define conceptual domains and ownership.

### Main Data Domains

- **[Domain 1]** — [what data it owns]
- **[Domain 2]** — [what data it owns]
- **[Domain 3]** — [what data it owns]

Examples:

- **Users / Identity** — accounts, profiles, credentials, roles
- **Billing** — subscriptions, invoices, payment events
- **Operational Data** — tasks/orders/tickets and their lifecycle
- **Audit / Events** — change history and event logs
- **Reporting** — derived aggregates, metrics, summaries

### Ownership / Source of Truth Rules

- [rule 1: which domain/service owns which truths]
- [rule 2: which tables/collections are projections only]
- [rule 3: what must not be updated casually]

Examples:

- User account truth lives in Users/Identity, not in analytics tables
- Billing truth lives in Billing domain and external PSP, not in arbitrary caches
- Analytics/BI tables are **not** operational source of truth

### Guidance for Anti-Gravity (Data Ownership)

- Be explicit about where truth lives vs what is derived, cached, or replicated
- Treat designs where multiple areas co-own the same truth as a risk and call them out

---

## ACCESS PATTERNS (WORKLOAD-ORIENTED THINKING)

Access patterns should drive schema, indexing, and optimization advice.

### Primary Read Patterns

- [read pattern 1 — what is queried and how often]
- [read pattern 2]
- [read pattern 3]

Examples:

- “Get user by email / external ID”
- “List items by owner + created_at with pagination”
- “Fetch dashboard summary for a tenant (aggregated counts)”
- “Fetch current session/token validity”

### Primary Write Patterns

- [write pattern 1 — what is written and how often]
- [write pattern 2]
- [write pattern 3]

Examples:

- “Status transitions in a workflow (e.g., order/task status updates)”
- “High-frequency append-only event writes”
- “Background job status updates”

### Known or Expected Hot Paths

- [hot path 1]
- [hot path 2]
- [hot path 3]

Examples:

- Frequently viewed dashboards or boards
- Authorization checks (membership lookups, permission checks)
- Event ingestion pipelines

### Guidance for Anti-Gravity (Access Patterns)

- Tie schema and index suggestions to these patterns, not generic “best practices”
- Treat high-frequency paths as first-class when suggesting changes

---

## INTEGRITY / CONSTRAINT EXPECTATIONS

Key invariants should be named independent of the engine.

### Critical Invariants

- [invariant 1]
- [invariant 2]
- [invariant 3]
- [invariant 4]

Examples:

- No duplicate active subscription per user/tenant
- A payment must map to a valid order and amount
- Tenant data must remain isolated from other tenants
- Certain state transitions are forbidden (e.g., completed → draft)

### Constraint Expectations

- [constraint 1]
- [constraint 2]
- [constraint 3]

Examples:

- Referential integrity enforced between core entities (conceptually via FKs or equivalent)
- Unique constraints on key business identifiers (email, slug, external reference IDs)
- Soft-delete semantics in some domains vs hard deletes in others

### Dangerous Invalid States

- [invalid state 1]
- [invalid state 2]
- [invalid state 3]

Examples:

- Orphaned records (child without parent)
- Overlapping subscriptions or duplicate active records
- Financial or audit records silently mutated after initial write

### Guidance for Anti-Gravity (Integrity)

- Preserve these invariants in schema and query suggestions
- Make tradeoffs explicit if a change weakens a constraint

---

## MIGRATION MINDSET AND RULES

Even pre-engine, migration approach should be principled.

### Migration Safety Expectations

- Favor additive-first changes where possible
- Avoid single-step destructive schema changes in live systems
- Plan for backward-compatible deploy sequences when evolving schemas
- Treat large data backfills as separate, carefully managed operations

Examples (once concrete):

- Use expand–contract pattern for renames or type changes
- Separate schema rollout from app code rollout when possible

### Migration Risks to Watch

- Treating migrations as trivial “one-time SQL scripts”
- Running heavy migrations on production without testing on realistic data
- Ignoring rollback strategies for high-risk changes
- Assuming migrations are instantaneous and lock-free at all scales

### Tables / Areas Requiring Extra Caution (when defined)

- [area 1]
- [area 2]
- [area 3]

Examples:

- Billing/payment records
- High-volume event or audit tables
- Multi-tenant shared tables

### Guidance for Anti-Gravity (Migrations)

- Treat migrations as operationally significant changes, not plumbing
- Recommend expand–contract or similar phased patterns for breaking changes
- Explicitly call out migration risk/cost when suggesting data model changes

---

## INDEXING / SCALING NOTES (ONCE DATA EXISTS)

Indexing and scaling advice should reflect real workloads.

### Important Existing or Planned Indexing Assumptions

- [assumption 1]
- [assumption 2]
- [assumption 3]

Examples:

- Frequent filter columns (tenant_id, status, created_at) must be indexed
- Composite indexes aligned to multi-column filters
- Avoid redundant or low-cardinality-only indexes

### Scaling Concerns

- [concern 1]
- [concern 2]
- [concern 3]

Examples:

- Single large table expected to grow quickly
- Expensive reporting queries running on transactional data
- Cross-tenant queries that may become slow or expensive

### Current or Expected Growth Pressure

[Describe which domains or tables will likely grow fastest and how that should influence design.]

### Guidance for Anti-Gravity (Indexing)

- Do not recommend “index everything”; weigh write cost vs read benefit
- Propose indexing or denormalization based on actual or expected hot paths

---

## SECURITY / PRIVACY CONSIDERATIONS AT THE DB LAYER

Some data is inherently higher risk.

### Sensitive Data Areas (when known)

- [area 1]
- [area 2]
- [area 3]

Examples:

- Credentials/secrets
- PII and contact info
- Billing and payment-related data
- Audit logs with detailed behavior

### Data Access Rules

- [rule 1]
- [rule 2]
- [rule 3]

Examples:

- Sensitive fields should not be casually exposed in ad-hoc queries
- Tenant filtering must be applied to all multi-tenant reads
- Soft-deleted data must not leak into normal “active” queries

### Logging / Exposure Concerns

- [concern 1]
- [concern 2]
- [concern 3]

Examples:

- Avoid logging full query result payloads containing PII
- Ensure query logs are scrubbed of secrets or tokens

### Guidance for Anti-Gravity (Security)

- Align database-related suggestions with overall security baselines
- Treat schema and query changes that touch sensitive data as high-risk

---

## ANTI-GRAVITY GUIDANCE (DATABASE WORK)

When dealing with database-related tasks, Anti-Gravity should:

- Reason from this context rather than generic DB patterns
- Tie schema and query recommendations to real or expected access patterns
- Preserve clear ownership and source-of-truth boundaries
- Treat migrations and data changes as operationally important
- Respect different consistency/freshness needs across flows
- Avoid reinforcing known or documented pain points

Anti-Gravity should be especially careful about:

- Changes touching high-risk data (identity, billing, permissions, audit)
- Suggestions that imply engine-specific behavior before it is chosen
- Schema and indexing advice for hot paths or high-volume tables

Anti-Gravity should avoid:

- Assuming the ORM or driver hides all database complexity safely
- Recommending destructive schema changes casually
- Ignoring source-of-truth and tenant-isolation boundaries
- Suggesting denormalization or indexing changes without workload awareness

---

## WHAT IS **NOT** DECIDE YET

This file does **not** currently decide:

- Exact schemas, table/collection structures, or indexing
- Concrete engine or hosting (e.g., RDS Postgres vs managed serverless)
- ORM vs query builder vs raw SQL as the final access layer
- Specific migration tools or pipelines
- Concrete backup/retention configurations

Those belong to stack- and infra-specific layers once chosen.

This file should be read as:

```text
project-level database discipline
not final engine-specific schema documentation
```

---

## KNOWN DATABASE PAIN POINTS (WHEN DISCOVERED)

Document specific persistence-layer issues or hotspots here:

- [pain point 1]
- [pain point 2]
- [pain point 3]

Examples:

- N+1 query patterns in older modules
- Long-running analytical queries on the primary transactional DB
- Inconsistent use of transactions for multi-step updates
- Tables that have grown beyond original assumptions
- Legacy denormalized fields causing confusion
- Weak or missing audit/event history

### Guidance for Anti-Gravity (Pain Points)

- Treat these as caution zones, not “probably fine”
- Prefer recommendations that reduce or work around these issues instead of reinforcing them

---

## WHAT “GOOD DATABASE WORK” LOOKS LIKE HERE

“Good” data work in this project:

- Ties schema and query designs to real or expected access patterns
- Keeps ownership and source-of-truth boundaries clear
- Preserves key invariants and integrity constraints
- Designs migrations as safe, staged operations, not one-shot blasts
- Uses indexing and denormalization deliberately, with justification
- Separates transactional and analytical concerns where needed
- Makes consistency/freshness tradeoffs explicit per domain
- Avoids speculative complexity that the current scale does not need

### Guidance for Anti-Gravity (Quality Standards)

- Use these qualities as a self-check before proposing database changes
- Call out when a requested change would clearly fall short on these criteria

---

## EXCEPTIONS / PRACTICAL NOTES

Reality may not perfectly match the ideal patterns yet.

Examples:

- Some legacy tables may not fully align with current ownership boundaries
- Raw SQL may be acceptable in reporting or known hot paths where the ORM is limiting
- Some denormalized fields exist for historical reasons and require careful migration
- Older migrations may not reflect current best practices
- Analytics or search indexes may intentionally duplicate primary data

### Guidance for Anti-Gravity (Practicality)

- Distinguish between tolerated legacy reality and desired future pattern
- When touching legacy areas, avoid sweeping refactors unless explicitly scoped — keep changes safe and reviewable
- If recommending change, make migration cost and operational risk explicit

---

## INSTRUCTIONS FOR ANTI-GRAVITY (SUMMARY)

When using this file for database-related work:

1. Reason from the actual persistence context, not generic database habits
2. Tie schema and query suggestions to access patterns and invariants
3. Preserve source-of-truth and ownership clarity across domains
4. Treat migrations as high-impact operations that need safe patterns
5. Follow the existing query layer conventions unless intentionally proposing change
6. Respect differences in consistency and freshness requirements between domains
7. Avoid reinforcing known pain points (N+1, unsafe migrations, unclear ownership)
8. Make tradeoffs explicit when suggesting denormalization, indexing, or engine-specific features
9. State assumptions clearly if database context is incomplete
10. Use this file as the minimum floor for data-layer reasoning in this project

---

## WHAT FUTURE FILES SHOULD ASSUME

Future stack- or infra-specific files should assume:

- The database stack may be refined or swapped, but ownership, invariants, access-pattern thinking, and migration safety remain required
- Engine-specific context (e.g., Postgres + Prisma) will extend this file with concrete schemas, indexes, and tools without weakening the philosophy layer
- Database-related decisions should remain explicit and documented, not implicit in scattered examples

---

## CROSS-REFERENCES

| Related Context File | Relationship |
| --- | --- |
| `stack-context.md` | Defines concrete DB engine, ORM/query tooling, and any caching layers |
| `architecture-context.md` | Describes how data flows between services/modules and how repositories are structured |
| `coding-standards.md` | Influences how models, repositories, and query helpers are named and organized |
| `security-baselines.md` | Governs handling of sensitive data, encryption, and access control at the DB layer |
| `infra-context.md` | Covers DB hosting, backups, monitoring, and operational limits |
| `testing-standards.md` | Describes test DB strategy, fixtures/factories, and migration use in tests |

---
