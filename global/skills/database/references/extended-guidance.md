# Extended Guidance

## Contents

- [DATABASE HEURISTICS](#database-heuristics)
- [BEHAVIORAL WORKFLOW](#behavioral-workflow)
  - [Phase 1 — Understand](#phase-1-understand)
  - [Phase 2 — Contextualize](#phase-2-contextualize)
  - [Phase 3 — Analyze](#phase-3-analyze)
  - [Phase 4 — Plan](#phase-4-plan)
  - [Phase 5A — Schema Design](#phase-5a-schema-design)
  - [Phase 5B — Relationship Design](#phase-5b-relationship-design)
  - [Phase 5C — Migration Execution (Expand-and-Contract)](#phase-5c-migration-execution-expand-and-contract)
  - [Phase 5D — Query Implementation](#phase-5d-query-implementation)
  - [Phase 5E — Index Creation](#phase-5e-index-creation)
  - [Phase 6 — Verify](#phase-6-verify)
  - [Phase 7 — Critique](#phase-7-critique)
  - [Phase 8 — Communicate](#phase-8-communicate)
- [KEY DIAGNOSTIC QUESTIONS](#key-diagnostic-questions)
  - [Before Designing](#before-designing)
  - [During Design](#during-design)
  - [Before Migration](#before-migration)
  - [During Query Work](#during-query-work)
- [ANTI-PATTERNS](#anti-patterns)
- [OUTPUT SHAPE](#output-shape)
  - [For Schema Design](#for-schema-design)
  - [For Schema Modification](#for-schema-modification)
  - [For Query Optimization](#for-query-optimization)
- [NON-NEGOTIABLE CHECKLIST](#non-negotiable-checklist)
  - [Data Integrity](#data-integrity)
  - [Migration Safety](#migration-safety)
  - [Query Quality](#query-quality)
  - [Indexing](#indexing)
  - [Operational Readiness](#operational-readiness)

## DATABASE HEURISTICS

Prefer:

- Clear ownership over shared mutation
- Normalized models first, denormalized only with workload evidence
- Explicit database constraints over "the application will handle it"
- Schema design driven by actual query and write patterns
- Additive, staged migrations over risky direct destructive changes
- Understanding generated SQL rather than blindly trusting ORM defaults
- Fewer meaningful indexes over many speculative ones
- Boring, well-understood designs over fashionable choices without justified need
- Database changes that can be monitored, rolled back, and recovered safely
- Testing migrations on production-volume clones before execution
- Soft deletes over hard deletes where recovery or audit trail may matter

---

## BEHAVIORAL WORKFLOW

### Phase 1 — Understand

Restate what data needs to be stored, queried, and maintained. Identify domain entities and relationships. Clarify business rules. Determine: new schema design, schema modification, migration, query optimization, or technology evaluation?

### Phase 2 — Contextualize

Map actual access patterns — primary reads and writes, read-to-write ratio, dominant query patterns. Determine current and projected data volumes. Identify the existing schema conventions, naming patterns, and migration tooling. Identify what other systems depend on this data.

### Phase 3 — Analyze

*For Schema Design:*

1. Identify core entities, attributes, and relationships (one-to-one, one-to-many, many-to-many).
2. Normalize to 3NF as the starting point.
3. Map primary access patterns against the normalized schema — identify where joins create performance risk.
4. Evaluate whether targeted denormalization is warranted based on access patterns — not assumptions.
5. Define constraints: NOT NULL, UNIQUE, CHECK, FOREIGN KEY for every applicable invariant.
6. Select appropriate data types — most specific correct type for each column.
7. Design the indexing strategy based on dominant query patterns.

*For Schema Modification:*

1. Identify all consumers of the affected tables (application code, other services, reports, analytics).
2. Assess backward compatibility — will the existing application version still work after this change?
3. Assess locking risk — will this DDL operation lock a high-traffic table?
4. Plan the expand-and-contract sequence if the change is breaking.
5. Define the rollback path.

*For Query Optimization:*

1. Capture the current query and its execution plan (EXPLAIN ANALYZE).
2. Identify the issue: missing indexes, N+1 patterns, full table scans, unnecessary joins, or over-fetching.
3. Evaluate the fix (add index, restructure query, batch fetch, adding a covering index).
4. Test the improvement on production-volume data.

*For Technology Evaluation:*

1. Map the data's characteristics: structured vs unstructured, relational vs document vs graph.
2. Map access patterns: CRUD, complex queries, full-text search, relationship traversal, time series.
3. Map consistency requirements: ACID, eventual, read-your-writes.
4. Evaluate candidates against these concrete requirements — not against trend popularity.

### Phase 4 — Plan

Define the table structure, columns, types, constraints, indexes, and relationships. For modifications: define the migration sequence (expand → dual-write → backfill → switch reads → contract). Define the rollback path. Identify what tests need to exist before and after the change.

### Phase 5A — Schema Design

1. Create tables with explicit column types, constraints, and relationships.
2. Add NOT NULL for all required fields.
3. Add FOREIGN KEY constraints with appropriate ON DELETE behavior.
4. Add UNIQUE constraints for all business uniqueness invariants.
5. Add CHECK constraints for value range restrictions.
6. Create indexes for the primary query patterns — composite indexes ordered by selectivity.
7. Document the reasoning for any denormalization decisions.

### Phase 5B — Relationship Design

1. Define the real cardinality and lifecycle behavior of the relationship.
2. Decide where foreign keys, join tables, nested structures, or references are appropriate.
3. Make CASCADE, SET NULL, and RESTRICT decisions explicitly — the wrong delete behavior can destroy referential integrity silently.
4. Confirm whether child records have independent existence or are strictly owned by the parent.

### Phase 5C — Migration Execution (Expand-and-Contract)

| Step | Action |
| --- | --- |
| **1. Expand** | Add new schema elements (new columns, new tables) as nullable/optional. Existing app continues to work without modification. |
| **2. Dual-Write** | Update app to write to both old and new schema structures simultaneously. Reads still from old. Deploy this code change. |
| **3. Backfill** | Background process to populate new schema elements for all historical rows. Process in small batches to avoid locking. Monitor for errors and replication lag. |
| **4. Switch Reads** | Update app to read from new structure. Deploy. Monitor for errors and data inconsistencies. |
| **5. Contract** | Drop old columns or tables. This is the point of no easy return — verify thoroughly. |

At every step: the system is fully operational. Each step can be individually rolled back. Schema and code deployments are separate.

### Phase 5D — Query Implementation

1. Select specific columns — avoid SELECT *.
2. Use parameterized queries — never string concatenation for values.
3. Examine ORM-generated SQL before trusting it in production.
4. Use EXPLAIN ANALYZE to verify queries use intended indexes.
5. Watch for N+1 patterns in any code that iterates over collections.
6. Use batch fetching or eager loading for known related-data access patterns.

### Phase 5E — Index Creation

1. Identify columns in WHERE, JOIN, and ORDER BY clauses of frequent queries.
2. Create composite indexes with columns ordered by selectivity (most selective first).
3. Consider covering indexes for high-frequency queries where all needed columns can be in the index.
4. Verify index usage with EXPLAIN ANALYZE after creation.
5. Create indexes CONCURRENTLY on production databases to avoid table locks (where supported).

### Phase 6 — Verify

- Attempt to insert invalid data — constraints should reject it.
- EXPLAIN ANALYZE confirms queries use intended indexes.
- Migration tested on production-volume data clone.
- Application functions correctly with the new schema.
- Rollback path tested before executing on production.
- No data was lost or corrupted during backfill.

### Phase 7 — Critique

(Before Finalizing)

1. **Invariants:** Are all business rules that must always hold enforced at the database level?
2. **Access Patterns:** Does the design support the real dominant reads and writes efficiently?
3. **Indexes and Write Costs:** Is every index justified? Is any critical query path missing one? Any speculative overhead?
4. **Ownership:** Is it completely clear which system owns each piece of data and who may mutate it?
5. **Migration Safety:** Has every risky change been assessed for lock risk, backward compatibility, and rollback path?
6. **Simplicity:** Is this design simpler than the problem requires — or more complex than necessary?
7. **Future Change Cost:** What becomes hardest to change later? Is that cost acceptable?
8. **Denormalization Justification:** Is any denormalization justified by measured workload evidence, or does it exist out of convenience?

### Phase 8 — Communicate

Document schema design decisions and the access patterns they serve. Document the migration plan and rollback path. Document denormalization decisions with the performance evidence that justified them. Document the indexing strategy. Define what to monitor after the change is deployed.

---

## KEY DIAGNOSTIC QUESTIONS

### Before Designing

- What are the actual read and write access patterns this schema must serve?
- What are the business rules that constrain this data? (Required fields, uniqueness, valid values, referential integrity)
- What is the projected data volume in 6 months? 12 months?
- Who else reads or writes to this data?

### During Design

- Is this normalized enough to prevent data integrity issues?
- Is this denormalized only where measured access patterns demand it?
- Are constraints enforced at the database level — not just the application level?
- If the application crashes mid-operation, can the data be left inconsistent?

### Before Migration

- Can this migration be applied without locking a high-traffic table?
- Can the current application version continue to work while this migration runs?
- Has this been tested on a production-volume data clone?
- What is the rollback path if the migration fails midway?
- Is the schema deployment separated from the code deployment?

### During Query Work

- What SQL is actually being generated?
- How many queries does this operation trigger (N+1 detection)?
- Is this query using indexes or scanning the full table?
- How will this query perform when the table has 100x more rows?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| --- | --- | --- | --- |
| **The Blocking Migration** | Running `ALTER TABLE` directly on a production table with 50M rows | Table locks for 30 seconds, cascading timeouts, connection pool exhaustion | Use online schema change tools (pt-osc, gh-ost, pg_repack) or non-blocking DDL. Always test on a production-volume clone. |
| **Coupled Schema and Code Deployment** | One deployment that runs a migration, removes old columns, and deploys new code simultaneously | If either fails, the system is in a state neither old nor new code can handle. No independent rollback. | Deploy schema changes separately. Add columns as nullable first (step 1), deploy code (step 2), contract/remove old columns last (step 3). |
| **ORM Blindness** | Trusting the ORM to generate efficient queries without examining the actual SQL. `user.orders.items` triggers 1 + N + N×M queries. | N+1 patterns are invisible at the application layer. Under concurrent load, exhausts connection pools. | Enable query logging in development. Examine generated SQL for every major code path. Use eager loading or batch fetching for collection access. |
| **Schema Mirrors UI** | Database tables structured exactly like UI forms — one table per screen, columns matching form fields | UIs change constantly. Schemas should not. Every UI redesign forces a migration. | Model the domain, not the UI. The application layer transforms domain data into view-specific shapes. |
| **Missing Constraints** | `email` can be NULL even though every user must have one. `status` accepts any string. `user_id` in orders table has no FK to users. | Without DB-level constraints, data integrity depends on application code being perfect forever. Invalid data enters the system and corrupts everything downstream. | Enforce constraints at the DB level: NOT NULL, UNIQUE, FK, CHECK. Make invalid states unrepresentable. |
| **Shared Ownership Ambiguity** | Two services both writing to the same `orders` table with no defined authority | Shared mutation without clear ownership creates inconsistency, race conditions, and silent data corruption | Designate exactly one owner per data boundary. Other systems read. Only the owner writes. |
| **The Speculative Index** | Creating indexes on every column "just in case" — 12 columns, 10 indexes | Every index slows writes and consumes memory. Most will never be used. | Index based on actual query patterns. Remove indexes monitoring shows are never used. |
| **The Big Bang Migration** | One migration that renames 5 columns, changes 3 data types, adds 2 tables, drops 1 table, and backfills 10M rows | If anything fails midway, the database is in a state neither old nor new code can handle | Break migrations into small, independent, backward-compatible steps. Each step deployable and rollbackable on its own. |
| **FLOAT for Money** | `price FLOAT` or `amount DOUBLE` for financial calculations | IEEE 754 rounding errors accumulate across transactions. `0.1 + 0.2 = 0.30000000000000004`. Financial discrepancies impossible to explain to auditors. | Use DECIMAL with explicit precision and scale. Never FLOAT or DOUBLE for money. |
| **Hard Delete Without Audit** | `DELETE FROM orders WHERE id = 123` with no soft-delete flag, no audit trail, no recovery path | Once deleted, the data is irrecoverable unless backups are recent and restore is fast — which is rarely tested. | Prefer soft deletes (`deleted_at TIMESTAMP`). If hard deletes required, log deletion with context (who, when, why) before executing. |
| **Blind Normalization** | Normalizing to 5NF, then requiring 12 joins to render the dashboard that runs on every page load | Integrity without usability is a failed design. Creates the exact performance pressure that leads to premature caching and inconsistency. | Normalize first to protect integrity. Map the dominant access patterns. If specific joins create genuine measured performance problems, consider targeted denormalization for those paths only — with an explicit synchronization strategy. |
| **Cache as Band-Aid** | A slow query is discovered. Rather than fixing it (missing index, N+1), a Redis cache is added in front | The cache masks a fixable problem and adds invalidation complexity, staleness risk, cold-start latency, and memory pressure | Examine the slow operation first. Fix the root cause. Only add caching if the operation is inherently expensive and the root cause cannot be further improved. |

---

## OUTPUT SHAPE

### For Schema Design

```markdown

1. Domain entities, relationships, and access patterns the schema serves
2. Table definitions with columns, types, and constraints
3. Indexing strategy with rationale for each index
4. Denormalization decisions with performance evidence (if any)
5. Scale considerations — projected data volume and growth patterns
6. Migration plan for creating the schema in production
```

### For Schema Modification

```markdown

1. What is changing and why
2. Impact assessment — what consumers, queries, and services are affected
3. Backward compatibility analysis
4. Migration plan — step-by-step expand-and-contract sequence
5. Rollback plan for each step
6. Testing requirements — production-volume data clone validation
7. Deployment sequence — schema deployment separated from code deployment
8. Post-deployment monitoring checklist
```

### For Query Optimization

```markdown

1. The problematic query and its current execution plan
2. Baseline performance metrics (execution time, rows scanned)
3. Root cause (missing index, N+1, full table scan, over-fetching)
4. Proposed fix with rationale
5. Expected improvement
6. Verification plan (EXPLAIN ANALYZE after fix, production-scale testing)
```

---

## NON-NEGOTIABLE CHECKLIST

### Data Integrity

- [ ] All required fields are NOT NULL
- [ ] All uniqueness invariants enforced with UNIQUE constraints or unique indexes
- [ ] All relational references enforced with FOREIGN KEY constraints
- [ ] ON DELETE behavior (CASCADE, SET NULL, RESTRICT) is intentional and correct for the domain
- [ ] Financial data uses DECIMAL — never FLOAT or DOUBLE
- [ ] Timestamps include timezone information (TIMESTAMP WITH TIME ZONE)

### Migration Safety

- [ ] Migration tested on a production-volume data clone
- [ ] Migration does not use blocking DDL on large tables
- [ ] Migration is backward-compatible — current app version works with new schema
- [ ] Schema deployment separated from code deployment
- [ ] Rollback path exists and has been tested
- [ ] Expand-and-contract pattern followed for all breaking schema changes

### Query Quality

- [ ] Queries select specific columns — not SELECT *
- [ ] Queries use parameterized values — not string concatenation
- [ ] ORM-generated SQL examined and verified
- [ ] N+1 patterns checked and eliminated
- [ ] EXPLAIN ANALYZE confirms queries use intended indexes

### Indexing

- [ ] Indexes exist for columns in frequent WHERE, JOIN, and ORDER BY clauses
- [ ] Composite indexes ordered by selectivity (most selective column first)
- [ ] Indexes created CONCURRENTLY on production databases (where supported)
- [ ] No unused indexes accumulating write overhead

### Operational Readiness

- [ ] Slow query logging configured
- [ ] Database backups configured and restore tested
- [ ] PII identified and handled appropriately (encryption, access controls, retention)
- [ ] Database credentials managed securely — not hardcoded

---

**Final Rule:** Good database design protects truth first, supports access second, and evolves safely over time. Data integrity is absolute. Everything else is negotiable. And never, ever use FLOAT for money.
