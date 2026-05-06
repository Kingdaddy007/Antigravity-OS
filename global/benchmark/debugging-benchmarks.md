# BENCHMARK: DEBUGGING

**Version:** Gold v1.0
**Layer:** 11 — Verification
**Loading Tier:** 3 — **LOADED ON DEMAND**

***

## PURPOSE

This file contains repeatable test scenarios for evaluating Anti-Gravity's
debugging capability — evidence gathering, hypothesis formation, root cause
analysis, fix quality, and regression prevention.

### Evaluate With

- [rubric-debugging.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-debugging.md)
- [rubric-communication.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-communication.md)
- [rubric-testing.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-testing.md)

### Tests

- `skill-debugging.md`
- `workflow-debug-issue.md`

***

## WHAT THIS BENCHMARK TESTS

This benchmark evaluates whether Anti-Gravity can:

- Define symptoms clearly and precisely
- Distinguish expected versus actual behavior
- Gather and use evidence before proposing fixes
- Generate and rank multiple hypotheses
- Identify root causes rather than suppressing symptoms
- Avoid guess-driven fixes and first-story bias
- Propose precise, targeted mitigations
- Verify the fix and defend against regression
- Recognize security-adjacent bugs and treat them appropriately

This benchmark should reveal whether Anti-Gravity debugs like a
disciplined investigator or a random patch generator.

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

1. Symptom clarity — was expected versus actual behavior made explicit?
2. Evidence use — was investigation grounded in data before guessing?
3. Hypothesis quality — were multiple plausible causes considered?
4. Root-cause depth — was the actual mechanism identified?
5. Fix precision — does the fix address the cause, not just the symptom?
6. Verification strength — was the fix confirmed against the original issue?
7. Regression awareness — was protection against recurrence added?
8. Structural awareness — was a pattern recognized, not just an instance?
9. Communication clarity — can a teammate act on this?
10. Uncertainty honesty — was confidence calibrated to the evidence?

***

## SCENARIO 1 — Straightforward Bug With Clear Symptoms

### Prompt [SCENARIO 1]

Users are reporting that when they create a new task and immediately
try to view it on the sprint board, it does not appear. But if they
refresh the page, it shows up. This started happening after last
Thursday's deployment.

### What Excellent Output Looks Like [SCENARIO 1]

- Restates the symptom precisely — create then immediate view equals missing, refresh equals visible
- Identifies this as likely a cache or state invalidation issue
- Forms multiple hypotheses:
  1. Cache not invalidated after mutation — most likely given the pattern
  2. Optimistic update not configured, waiting for background refetch
  3. Sprint board query has different filters than the creation endpoint
- Asks what changed in Thursday's deployment
- Investigates the mutation flow and cache invalidation code path first
- Identifies the fix — ensure cache invalidation is called after task creation with the correct query key
- Suggests regression test — create task, assert it appears in list without refresh
- Checks for similar issues in other mutation flows

### Red Flags [SCENARIO 1]

- Jumps straight to "try adding a setTimeout" — symptom masking
- Does not ask about Thursday's deployment
- Considers only one hypothesis
- Suggests full page reload as a fix
- No regression test suggested

***

## SCENARIO 2 — Intermittent Bug With Ambiguous Evidence

### Prompt [SCENARIO 2]

About ten percent of the time, saving a comment on a task returns a
500 error. No pattern in which users it affects. The error does not
appear in local testing. The error message is a database transaction
already closed error.

### What Excellent Output Looks Like [SCENARIO 2]

- Recognizes this as a concurrency or connection issue under load
- Reads the actual error message carefully before hypothesizing
- Forms multiple hypotheses:
  1. Transaction timeout — operation takes too long under production load, connection returns to pool before commit
  2. Connection pool exhaustion — too many concurrent requests exhaust the pool
  3. Nested transaction — code accidentally nests transactions
- Asks about database connection pool size and current utilization
- Investigates the comment creation code path for transaction usage
- Checks connection pool metrics in production telemetry
- Identifies likely root cause — default transaction timeout too short under production concurrency
- Addresses the structural question — why does comment creation need a transaction at all?
- Fix — increase transaction timeout OR refactor to avoid unnecessary transaction, whichever fits the actual structure

### Red Flags [SCENARIO 2]

- Dismisses with "just retry the request"
- Ignores the intermittent ten percent signal — a concurrency indicator
- Does not read the actual error message carefully
- Suggests a client-side fix for a server-side concurrency problem
- No investigation of connection pool or transaction structure

***

## SCENARIO 3 — Bug Requiring Business Logic Understanding

### Prompt [SCENARIO 3]

The sprint velocity calculation is showing wrong numbers. A sprint
completed with eight tasks worth 42 total story points, but the
velocity chart shows 38 for that sprint.

### What Excellent Output Looks Like [SCENARIO 3]

- Asks for the exact data — which eight tasks, what were their point values?
- Checks the velocity calculation formula in domain rules
- Forms multiple hypotheses:
  1. A task was completed after sprint end — points counted but timing is off
  2. A task was re-opened and completed again — count may be wrong
  3. A task's story points were modified after sprint completion
  4. The calculation query has a filter excluding some tasks
- Investigates the query that calculates velocity
- Identifies the structural problem — calculation uses live point values rather than snapshotting points at sprint completion time
- Suggests the real fix — snapshot story points at sprint completion, do not rely on values that can be edited after the fact
- Writes a regression test with specific point values and expectations

### Red Flags [SCENARIO 3]

- Assumes the calculation is correct and the user is wrong
- Does not check the actual data behind the discrepancy
- Does not reference the business rules for velocity calculation
- Fixes the displayed number manually without fixing the underlying cause
- No consideration of the snapshot versus live value problem

***

## SCENARIO 4 — Performance-Related Bug

### Prompt [SCENARIO 4]

A project dashboard takes 12 seconds to load for the largest customer,
who has 47 sprints and 2,300 tasks. Other customers with fewer tasks
load in under one second.

### What Excellent Output Looks Like [SCENARIO 4]

- Recognizes this as a performance-scaling bug, not a functional bug
- Does NOT jump to "add caching" — measures first
- Asks what data is fetched on dashboard load
- Forms multiple hypotheses:
  1. N+1 query — loading each sprint's tasks individually
  2. Unindexed query — full table scan on large task table
  3. Aggregation query without proper indexing
  4. Loading all historical data instead of paginating
- Suggests profiling — enable query logging and check query plans on dashboard queries
- Identifies the likely root cause — dashboard loads all sprint data for all time with no pagination on historical sprints
- Fix — paginate or limit to recent sprints, lazy-load historical data
- Also checks whether aggregate queries are indexed appropriately
- Suggests adding a performance baseline as a regression guard

### Red Flags [SCENARIO 4]

- Immediately suggests adding a caching layer without measuring first
- No profiling or measurement step
- Adds pagination on the frontend but still fetches all data from the database
- Ignores the scaling dimension — works for small customers, fails for large
- No investigation of query patterns or data access paths

***

## SCENARIO 5 — Security-Adjacent Bug

### Prompt [SCENARIO 5]

A user reported that they can see tasks from a project they were
removed from last week. They can view tasks on the board but cannot
edit them. They receive a 403 when trying to update.

### What Excellent Output Looks Like [SCENARIO 5]

- Recognizes this as a SECURITY issue — data leakage across authorization boundaries
- Treats with high urgency — this is not a regular bug
- Forms multiple hypotheses:
  1. Read queries do not check project membership — only write queries do
  2. Client cache is serving stale data from before the user was removed
  3. The membership removal did not propagate correctly
  4. The board page uses a different auth check than the API write path
- Checks whether the board query filters by project membership
- Identifies the likely root cause — read queries check project existence but not user membership, while writes check both
- Recognizes this as a PATTERN — not just one endpoint
- Fix — add membership check to ALL read queries, not only the reported one
- Audits other read paths for the same class of vulnerability
- Treats this as a potential incident — assesses who else may have been affected
- Regression test — remove user from project, verify all read endpoints return 403

### Red Flags [SCENARIO 5]

- Treats this as a regular bug instead of a security issue
- Fixes only the reported endpoint without checking the pattern in other read paths
- Attributes to caching without investigating the authorization logic
- No security audit of other read paths
- No consideration of who else might have been affected or for how long

***

## SCENARIO 6 — Distributed System Data Mismatch

### Prompt [SCENARIO 6]

A user updates their profile information, but another part of the
application still shows old information for several minutes after
the update is saved successfully.

### What Excellent Output Looks Like [SCENARIO 6]

- Identifies this as a distributed consistency or caching problem, not a simple bug
- Forms multiple hypotheses:
  1. Read path serves from a cache that is not invalidated on write
  2. Eventual consistency — a secondary store or service is updated asynchronously
  3. CDN or edge caching serving stale data
  4. Different reads hitting different database replicas with replication lag
- Asks which part of the application shows stale data — same service or different?
- Investigates the read path for the stale data — does it query primary or replica?
- Identifies the source of truth and whether the write path confirms propagation
- Does not propose a client-side fix for a system-level propagation issue
- Fix depends on root cause — cache TTL adjustment, explicit invalidation, or read-after-write consistency strategy
- Defines verification — confirm propagation timing across the system

### Red Flags [SCENARIO 6]

- Immediately suggests increasing a cache TTL without investigating
- No source-of-truth analysis
- No distributed timing or propagation awareness
- Treats this as a local frontend state issue
- Proposes a workaround without understanding the actual propagation path

***

## SCENARIO 7 — Background Job Duplicates Work

### Prompt [SCENARIO 7]

A background worker sometimes processes the same job twice, causing
duplicate emails and duplicate downstream side effects. The issue is
not constant and is difficult to reproduce consistently.

### What Excellent Output Looks Like [SCENARIO 7]

- Identifies this as an idempotency and queue delivery semantics problem
- Forms multiple hypotheses:
  1. Queue retry without idempotency — job fails partway through, retries from scratch, and side effects repeat
  2. Visibility timeout too short — job appears available again before the first worker finishes
  3. Multiple workers racing on the same job
  4. Missing deduplication key or idempotency guard
- Asks about queue delivery semantics — at-least-once delivery expected?
- Investigates whether the job handler is idempotent
- Identifies the structural fix — make the job idempotent so reprocessing the same input produces the same outcome
- Adds deduplication logic or checks at the job entry point
- Improves observability — log job ID, worker ID, and attempt count to make future duplicate processing visible
- Regression test — trigger the same job twice, verify side effects occur only once

### Red Flags [SCENARIO 7]

- Suggests adding a boolean "processed" flag without addressing the race condition in checking it
- No queue semantics analysis
- No idempotency thinking
- No discussion of delivery guarantees, retry behavior, or worker timing
- Treats intermittent nature as unexplainable rather than a signal

***

## SCORING GUIDE

For each scenario, evaluate using `rubric-debugging.md` dimensions:

| Dimension | Weight for Debugging |
| :--- | :--- |
| Evidence Gathering | High — was data collected before guessing? |
| Symptom vs Cause Separation | High — was the root cause found, not just the trigger? |
| Hypothesis Quality | High — were multiple hypotheses considered and ranked? |
| Root Cause Identification | Critical — was the real cause found? |
| Fix Quality | High — does the fix address the root cause? |
| Regression Prevention | High — was a test or guard added? |
| Verification Strength | Medium — was the fix confirmed against the original issue? |
| Structural Awareness | Medium — was a class of bug recognized, not just an instance? |

Record all scores in `memory/benchmark-results.md`.

***

## FINAL RULE

A strong debugging benchmark response reduces uncertainty before
changing behavior. It makes clear:

- What failed and under what conditions
- What likely caused it and how that was determined
- How the fix addresses the root cause — not just the symptom
- Why recurrence should now be less likely

A system that diagnoses before patching, considers multiple causes,
and protects against recurrence is behaving like a disciplined
investigator — not a random patch generator.
