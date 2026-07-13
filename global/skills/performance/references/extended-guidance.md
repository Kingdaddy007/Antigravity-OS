# Extended Guidance

## Contents

- [PERFORMANCE STRATEGY GUIDANCE](#performance-strategy-guidance)
- [KEY DIAGNOSTIC QUESTIONS](#key-diagnostic-questions)
  - [Before Starting](#before-starting)
  - [During Investigation](#during-investigation)
  - [Before Optimizing](#before-optimizing)
  - [After Optimizing](#after-optimizing)
- [ANTI-PATTERNS](#anti-patterns)
- [OUTPUT SHAPE](#output-shape)
  - [For Performance Diagnosis](#for-performance-diagnosis)
  - [For Performance Optimization](#for-performance-optimization)
- [NON-NEGOTIABLE CHECKLIST](#non-negotiable-checklist)
  - [Evidence](#evidence)
  - [Targeting](#targeting)
  - [Quality Preservation](#quality-preservation)
  - [Verification](#verification)

## PERFORMANCE STRATEGY GUIDANCE

**Frontend:** Bundle size, code splitting, critical rendering path, blocking scripts, render frequency, image/asset optimization, network waterfalls, Core Web Vitals (LCP, FID/INP, CLS), perceived responsiveness, hydration cost for SSR/SSG.

**Backend / Service:** Endpoint critical path end-to-end, query efficiency and N+1 patterns, I/O latency and unnecessary blocking, connection pooling and reuse, batch vs per-item work, serialization cost, external dependency latency and timeout behavior.

**Database:** Query plan quality and index usage, indexing strategy for hot access patterns, N+1 behavior and eager loading, cardinality and data volume growth, locking and contention, transaction scope, hot rows under concurrent write load.

**Distributed / Infrastructure:** Queue depth growth and drain rate, retry amplification and thundering herd behavior, backpressure mechanisms between services, saturation points and autoscaling thresholds, cross-service latency chains, noisy-neighbor contention, circuit breaker behavior under partial failure.

---

## KEY DIAGNOSTIC QUESTIONS

### Before Starting

- What is the specific performance target?
- Is this latency, throughput, or resource consumption?
- Where is the evidence that this is actually slow?
- Has this degraded recently, or has it always been slow?

### During Investigation

- Where does each millisecond go in the request lifecycle?
- Which single component is consuming the most time or resources?
- How many database queries does this operation trigger? Are they indexed?
- Is the application doing work it does not need to do?
- At exactly what load does response time begin to degrade nonlinearly?

### Before Optimizing

- Am I targeting the proven bottleneck, or optimizing something that feels slow?
- Can I eliminate this work entirely instead of making it faster?
- Can I fix the root cause instead of caching the symptom?
- Am I about to change multiple variables at once, losing causal clarity?
- How will I verify that the optimization actually improved performance?

### After Optimizing

- Did the metrics improve by the expected amount?
- **If the metric did not change — what does that imply about the original bottleneck hypothesis?**
- Has the bottleneck shifted to another component?
- Did the optimization introduce any correctness regressions?
- Does the system still degrade gracefully under extreme load?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| --- | --- | --- | --- |
| **Premature Optimization** | Rewriting with bit-shifting tricks before any profiling | Adds complexity with no proven benefit; actual bottleneck is almost always elsewhere | Write the simple version. Profile under realistic load. Optimize surgically only if this is the bottleneck. |
| **Optimizing the Non-Bottleneck** | Week spent optimizing a 2% function while the 85% DB query goes unexamined | The system's performance is governed by its single narrowest constraint | Profile the full request path. Identify the bottleneck. Optimize only that. |
| **Average-Based Reasoning** | "Average response time is 150ms, fine" while p99 is 4,200ms | Averages are dominated by fast requests and conceal tail latency | Always use percentile metrics. |
| **Cache-First Thinking** | First response to "query is slow" is "let's cache it" | Caching adds invalidation complexity, staleness risk, memory pressure on top of a fixable problem | Fix the root cause first. Cache only if inherently expensive and cannot be further optimized. |
| **N+1 Blindness** | List page loading 50 items, each triggering a separate query (51 queries total) | Destroys throughput. Under concurrent load, exhausts connection pools. | Examine every list operation for N+1. Use eager loading, batch fetching, or joined queries. |
| **Local-Machine Benchmarking** | "It returns in 5ms on my laptop with 100 rows. Fine." | 5ms with 100 rows may be 30 seconds with 10 million. Local benchmarks prove nothing about production behavior. | Test with production-scale data and realistic concurrent load. |
| **Multi-Change Chaos** | Adding cache, rewriting a query, upgrading a library, adding CDN simultaneously | Cannot isolate what caused improvement or regression | Change one variable per optimization cycle. Measure after each change. |
| **Optimization Theater** | Replacing `for` loops with streams for endpoints running once per hour | Optimized-looking code that doesn't materially improve any user-facing metric | Ask: if this change succeeds completely, what metric improves by how much? If not much, don't make the change. |
| **Degradation Ignorance** | System works at normal load but crashes completely at 2x traffic with no rate limiting | Traffic spikes are inevitable. Systems that crash cause cascading failures. | Design degradation: rate limiting, load shedding, circuit breakers, backpressure. |
| **Scale Fantasy** | Sharding a database for an application with 200 active users | Adds architectural complexity for performance scenarios that will never occur at current scale | Optimize for the scale that exists today with a clear, low-cost upgrade path. |
| **One-Shot Tuning** | Single investigation, apply a fix, close the ticket, never monitor again | Performance regressions recur. Data volumes grow. Traffic patterns shift. | After every optimization, confirm monitoring exists to detect recurrence. |

---

## OUTPUT SHAPE

### For Performance Diagnosis

```markdown

1. Problem statement — what is slow, for whom, under what conditions
2. Baseline metrics — current p95/p99 latency, throughput, resource usage
3. Methodology — how the bottleneck was identified
4. Identified bottleneck — the specific component, query, or operation
5. Evidence — the data that proves this is the bottleneck
6. Recommended interventions — ranked by impact-to-complexity ratio
7. Expected improvement — quantified estimate for each intervention
8. Tradeoffs — what each intervention costs
```

### For Performance Optimization

```markdown

1. Bottleneck targeted — what was the constraint and what evidence proved it
2. Baseline metrics — pre-optimization measurements
3. Intervention applied — what was changed and why
4. Post-optimization metrics — same measurement methodology as baseline
5. Improvement achieved — e.g., "p99 reduced from 1,200ms to 180ms"
6. Tradeoff accepted — what was sacrificed
7. Operational requirements — any new monitoring, cache management, or config needs
8. Next bottleneck — if target not fully met, where the constraint has shifted
```

---

## NON-NEGOTIABLE CHECKLIST

### Evidence

- [ ] Bottleneck identified through measurement — not assumption or intuition
- [ ] Baseline metrics captured before any optimization was applied
- [ ] Metrics use percentiles (p95, p99) — not averages
- [ ] Testing performed under realistic conditions (production-like data volume and concurrency)

### Targeting

- [ ] Optimization targets the proven bottleneck — not unrelated code
- [ ] Root cause examined before caching was considered
- [ ] N+1 query patterns checked and eliminated where found
- [ ] Only one variable changed per optimization cycle to preserve causal clarity

### Quality Preservation

- [ ] Code readability preserved or complexity encapsulated behind clean interfaces
- [ ] Optimization logic documented with WHY comments where non-obvious
- [ ] No correctness regressions introduced

### Verification

- [ ] Post-optimization metrics captured using the same methodology as baseline
- [ ] Improvement quantified and compared against the performance target
- [ ] Whether the bottleneck moved was checked and documented
- [ ] Degradation behavior under extreme load considered

---

**Final Rule:** Never optimize without evidence. Never assume without measuring. Never cache without first fixing. Never claim improvement without re-measuring. The fastest operation is the one you eliminate entirely. A strong performance result makes clear what was actually slow, why it was slow, what change had the best payoff, what the optimization costs, and how we will know if the improvement is real.
