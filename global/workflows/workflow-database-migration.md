---
id: database-migration
version: 1
status: active
intent: Design and execute compatible, observable, and recoverable database migrations.
use_when: [schema change, data backfill, storage-engine migration, destructive data transition]
do_not_use_when: [query-only analysis, model discussion without migration, unrelated deployment]
inputs: [current schema, target schema, data volume, compatibility window, recovery constraints]
required_resources: [database context, migration tooling, backups policy, dependent service contracts]
mutation_class: external_or_production
approval_gates: [approve implementation plan, explicit target approval before database mutation]
states: [assess, design, rehearse, approve, expand, migrate, validate, contract, monitor, deliver]
outputs: [migration plan, compatibility matrix, rehearsal evidence, validation report, recovery record]
verification: [row and constraint checks, application compatibility, performance comparison, backup or containment proof]
failure_paths: [halt on validation drift, retain compatibility layer, restore or contain according to approved plan]
resume_contract: task-scoped .agents/workflows/database-migration.json using the workflows directory contract
next_workflows: [test-strategy, ship-to-production]
profiles: [general]
---

# WORKFLOW: DATABASE MIGRATION

1. Inventory producers, consumers, constraints, indexes, data volume, and irreversible operations.
2. Prefer expand-and-contract: add compatible shape, dual-read/write only when justified, backfill, validate, switch consumers, then remove old shape later.
3. Define checkpoints, idempotency, batch size, lock/latency budget, observability, and abort criteria.
4. Rehearse against representative volume and verify the recovery or containment path.
5. Obtain explicit approval naming the target database and migration version before mutation.
6. Apply staged changes, recording command output and checkpoint evidence.
7. Validate data invariants and application behavior before contracting old structures.
8. Monitor and deliver evidence, limitations, and deferred cleanup.

