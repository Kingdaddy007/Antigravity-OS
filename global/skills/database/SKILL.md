---
name: database
description: 'Use this skill when designing schemas, writing queries, planning migrations, or evaluating data model decisions. Activated when the user mentions creating or modifying database tables, writing SQL, data integrity issues, slow queries, indexing, data migrations, ORM behavior, or choosing a database technology. Signal phrases: "design the schema", "create the tables", "add a column", "migration", "database is slow", "query optimization", "indexing", "normalize / denormalize", "data model", "foreign key", "relationship between", "N+1 queries", "data integrity", "ORM", "access pattern". Also activate for any work involving data that crosses service boundaries or any data integrity concern.'
---

# DATABASE DESIGN & DATA MODELING

## WHEN TO USE THIS

- Creating, modifying, or evaluating database schemas
- Writing or optimizing database queries
- Planning or executing schema migrations
- Evaluating database technology choices
- Investigating data integrity issues, inconsistencies, or corruption
- Designing data models for new features or services
- Evaluating indexing strategies

## NEVER DO

- Design a schema before understanding the actual access patterns
- Run blocking ALTER TABLE on large production tables
- Deploy schema changes and application code changes in the same operation
- Trust ORM-generated queries without examining the actual SQL executed
- Use FLOAT or DOUBLE for financial data — always use DECIMAL
- Apply hard deletes to sensitive or audit-relevant data without a recovery path
- Denormalize before profiling proves the join overhead is the actual bottleneck

---

## MINDSET

You are not a schema generator. You are a guardian of the most rigid, critical, and hardest-to-change foundation in the entire system.

Data fundamentally outlives application code. Data often outlives features, services, frameworks, and teams. Frameworks will be replaced, APIs will be versioned, frontends will be rewritten — but the data and the schema it lives in will persist through all of it. A schema mistake that reaches production is orders of magnitude more expensive to fix than an application bug, because schema changes affect every consumer, every query, every integration, and every row of existing data.

The expert database engineer:

- **Treats the schema as the most consequential architectural decision in the system** — harder to reverse than any technology choice, any API contract, or any frontend framework
- **Models data based on how the application will actually read and write it** — not based on how the domain looks in an ER diagram on a whiteboard
- **Views migrations as operations on a live, explosive environment** where a single locking ALTER TABLE on a high-traffic table can cause a system-wide outage
- **Never couples schema migrations to application code deployments** — they are separate operations with separate rollback paths
- **Indexes deliberately** — every index speeds reads but slows writes and consumes memory
- **Treats ORMs as tools, not oracles** — they can generate disastrous N+1 patterns that are invisible at the application layer but catastrophic at the database layer
- **Treats data integrity as absolute** — application bugs can be hotfixed, but corrupted or lost data is permanent and often irrecoverable
- **Designs for a billion rows, not a thousand rows** — the schema that works today must still work when data volume has grown by three orders of magnitude
- **Prefers boring, well-understood designs** unless complexity is clearly justified by the actual workload

The goal: create a model that preserves important truths, supports the most important reads and writes efficiently, can evolve safely, and makes ownership and integrity explicit.

---

## DECISION FRAMEWORK — 7 PRIORITIES (IN ORDER)

### Priority 1 — Data

Integrity

Enforce integrity at the database level — not only at the application level. Use foreign key constraints, NOT NULL, CHECK constraints, and unique constraints. The application layer can crash, have bugs, or be bypassed — the database constraints are the last line of defense.

### Priority 2 — Access

Pattern Alignment

Map the primary read and write patterns before designing the schema. A schema optimized for writes (highly normalized) may perform terribly for complex reads. Design for the dominant access pattern first, then mitigate the secondary pattern's weaknesses.

### Priority 3 — Migration

Safety

Never execute blocking DDL on large production tables. Use the expand-and-contract pattern for breaking changes. Test migrations on production-volume data clones. Separate schema deployment from application deployment. Have a rollback plan for every migration.

### Priority 4 — Scale

Awareness

Full table scans that are invisible at 10,000 rows become catastrophic at 10 million rows. Consider query performance at scale. Consider index selectivity degradation. Consider partition strategies for tables that grow unboundedly.

### Priority 5 — Query

Predictability

Examine ORM-generated queries. Log and review slow queries. Tag queries with comments identifying their source. Every query path should be understood — not abstracted away and hoped for the best.

### Priority 6 — Normalization

vs Denormalization

Start at 3NF for data integrity. Denormalize only when empirical profiling proves that read performance is unacceptable AND the root cause is join overhead — not a missing index or N+1 pattern. When denormalizing, document the update anomaly risk and define the consistency maintenance strategy.

### Priority 7 — Technology

Fit

Relational databases (PostgreSQL, MySQL) are the default for structured data with relationships and ACID requirements. Choose a different technology only when the data's access patterns demand its specific strengths — not because it is trendy.

**Rule:** Design from user and system behaviors, reads and writes, invariants and ownership, migration and scale constraints — not from nouns alone.

---

## CORE PRINCIPLES

1. **Data Integrity Is Absolute.** Application bugs can be hotfixed. Corrupted, inconsistent, or lost data may be permanent and irrecoverable. Enforce integrity at the database level with constraints, foreign keys, and transactions.
2. **Access Patterns Dictate Design.** A beautiful normalized schema that requires 12 joins for the most common read operation is a failed design.
3. **Never Couple Schema and Code Deployment.** Deploy schema changes first (backward-compatible). Then deploy the code that uses them. Each has its own rollback path.
4. **Normalize First, Denormalize With Evidence.** Start at 3NF. Denormalize only when profiling proves join overhead is the bottleneck — not when someone assumes it might be slow.
5. **Index Deliberately.** Every index speeds reads but slows writes and consumes memory. Create indexes based on actual query patterns — not speculatively.
6. **Migrate Without Downtime.** Use the expand-and-contract pattern. Test every migration on a production-volume data clone before execution.
7. **ORMs Are Tools, Not Oracles.** Examine the SQL your ORM generates. Watch for N+1 patterns and full table scans. The ORM serves you — you do not serve the ORM.
8. **Design for a Billion Rows.** The schema must work not just with today's data but with data volume anticipated in 12–24 months.
9. **Types and Constraints Are Documentation.** Use the most specific correct type. NOT NULL for required fields. ENUM or CHECK for restricted values. DECIMAL for financial data — never FLOAT.
10. **Deletions Are Dangerous.** Prefer soft deletes (`deleted_at` timestamp) for any data that might need recovery or audit trails.
11. **Make Source of Truth Explicit.** Every piece of data has exactly one authoritative owner. Multiple systems reading the same data is fine. Multiple systems mutating the same truth without clear authority is a consistency disaster.
12. **Database Design Is Part of Architecture.** A schema decision is not a local implementation detail — it is a system-wide architectural commitment with long-lasting consequences.

---

## DATABASE LENSES

| Lens | What to Inspect |
| --- | --- |
| **Access Pattern** | What are the primary reads and writes? Frequencies? Columns filtered/sorted/joined? Read-to-write ratio? Aggregation queries? |
| **Integrity** | Where can data become inconsistent? All required fields NOT NULL? Uniqueness invariants enforced? Relational references enforced with FK? Value ranges enforced? |
| **Scale** | How many rows in 6/12/36 months? At projected scale, will current queries still perform? Full table scans at 100x? Archival/partition strategy for unbounded tables? |
| **Index** | Columns in WHERE, JOIN, ORDER BY? Composite indexes ordered correctly? Covering indexes needed? Any unused indexes that waste write overhead? Index selectivity at scale? |
| **Migration** | Can this change be applied without locking? Backward compatible with current app version? Rollback path if it fails midway? Tested on production-volume clone? Schema deployment separated from code deployment? |
| **Query** | What SQL is actually being executed? How many queries does this operation trigger (N+1)? Using indexes or full table scan (EXPLAIN ANALYZE)? Over-fetching? Unnecessary subqueries? |
| **Relationship** | One-to-one, one-to-many, or many-to-many? Enforced with FK at DB level? ON DELETE behavior intentional (CASCADE, SET NULL, RESTRICT)? Child records — independent existence or strictly owned by parent? |
| **Consistency & Transactions** | Does this operation need to be atomic? Partial success possible? Denormalized copies — what keeps them in sync? Concurrent modifications — optimistic vs pessimistic locking? |
| **Type Safety** | Most specific correct type? DECIMAL (not FLOAT) for financial data? TIMESTAMP WITH TIME ZONE? VARCHAR with limits vs TEXT? UUIDs where globally unique IDs needed? |
| **Operational & Security** | Slow query logging configured? Backup + restore tested? PII identified, minimized, encrypted? Credentials managed securely? Data retention requirements? |

---
## REFERENCE LOADING RULES

Load `references/extended-guidance.md` when the task needs detailed implementation rules, examples, edge cases, diagnostics, or verification beyond the core workflow above. Inspect its Contents first and load only the matching sections.

## OUTPUT SHAPE

Deliver the requested artifact or decision, the key rationale and tradeoffs, and a concise verification checklist.

## NON-NEGOTIABLE CHECKLIST

1. Apply the core workflow above.
2. Load matching extended guidance for substantive or high-risk work.
3. Preserve user constraints and verify the result before delivery.