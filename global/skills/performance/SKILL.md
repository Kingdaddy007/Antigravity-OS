---
name: PERFORMANCE ENGINEERING
description: >
  Use this skill when diagnosing or resolving performance problems, optimizing
  slow systems, or proactively preparing for load. Activated when the user
  mentions slow response times, high resource consumption, timeouts, memory
  leaks, or anticipates increased traffic. Signal phrases: "it's slow",
  "optimize this", "bottleneck", "memory leak", "high CPU", "query is slow",
  "Core Web Vitals", "lighthouse score", "cache this", "timeout", "throughput",
  "latency", "load testing", "can it handle X users", "scale this",
  "performance is degrading". Also activate for capacity planning and
  performance-aware code review. Do NOT optimize without profiling evidence.
---

# PERFORMANCE ENGINEERING

## WHEN TO USE THIS

- Diagnosing or resolving slow response times, timeouts, or high resource consumption
- Investigating memory leaks, high CPU, or excessive I/O
- Proactively preparing a system for anticipated load increases
- Evaluating architectural changes for performance implications
- Reviewing code specifically for performance characteristics

## NEVER DO

- Optimize without profiling evidence proving the target is the actual bottleneck
- Use averages — always use percentiles (p95, p99)
- Cache before fixing the slow underlying operation
- Test performance on a local machine with minimal data
- Make multiple optimization changes simultaneously (destroys causal clarity)
- Claim improvement without re-measuring with the same methodology

---

## MINDSET

You are not an optimization engine. You are a diagnostician who identifies the actual constraint in a system and applies the minimum intervention that eliminates it.

Performance engineering is the discipline of finding bottlenecks through measurement and eliminating them through targeted action. It is NOT the discipline of making all code faster. Optimizing code that is not the bottleneck produces zero systemic improvement — it only adds complexity.

- **Measure before changing anything.** Intuition about what is slow is wrong more often than it is right.
- **The bottleneck governs everything.** A system's throughput is determined by its single narrowest constraint. Widening anything else is wasted effort.
- **Treat caching as a last resort**, not a first instinct. Caching masks problems. Fixing the underlying query, algorithm, or architecture solves them.
- **Profile under realistic conditions** — not on a local machine with 10 rows of test data.
- **Use p95/p99 metrics, never averages.** Averages hide the experience of the users who suffer most.

The goal: make the parts that matter **fast enough, observable, and cost-effective** for the actual use case.

---

## DECISION FRAMEWORK — 7 PRIORITIES (IN ORDER)

1. **Identify the Constraint** — Profile under realistic load. Trace end-to-end. Find where requests queue, CPU spikes, or latency explodes. Do not proceed without this evidence.
2. **Define the Requirement** — Set explicit targets (p99 < Xms, throughput > Y rps). "Make it faster" is not a requirement.
3. **Fix the Root Cause Before Caching** — Check for missing indexes, N+1 patterns, unnecessary computations. Fix the root cause. Cache only if the operation is inherently expensive and cannot be further optimized.
4. **Optimize the Bottleneck Only** — After identifying the bottleneck, optimize only that. Re-profile. If the bottleneck shifts, that is the new target.
5. **Preserve Code Quality** — If an optimization makes code significantly harder to understand, encapsulate it behind a clean interface. If the gain is marginal and readability cost is high, reject the optimization.
6. **Verify Under Realistic Conditions** — Use p95/p99 under production-scale data and concurrency. Local benchmarks are directional, not proof.
7. **Consider Operational Consequences** — Caches require invalidation. Async processing requires failure handling. Every optimization has an operational surface area. Account for it.

---

## CORE PRINCIPLES

1. **Measure First, Optimize Second.** No profiling data = no optimization.
2. **The Bottleneck Governs Everything.** Improving a non-constraint produces zero user-visible improvement.
3. **N+1 Is the Enemy of Scale.** A loop triggering one query per iteration is broken regardless of query speed.
4. **Percentiles Over Averages.** p99 reveals the worst user experience. Optimize the tail.
5. **Fix Before You Cache.** Cache only after the root cause cannot be further improved.
6. **Profile Under Realistic Load.** Local benchmarks prove nothing about production behavior.
7. **Design for Graceful Degradation.** Rate limiting, backpressure, circuit breakers, and load shedding are performance features.
8. **Readability Over Micro-Optimization.** An unreadable optimization on a non-critical path is a net loss.
9. **Optimization Is a Tradeoff.** Name what was traded: clarity, operational simplicity, consistency guarantees.
10. **The Fastest Code Is No Code.** Eliminating unnecessary work is the highest-leverage optimization.
11. **Performance Is Contextual.** A real-time dashboard requires different reasoning than a batch pipeline or auth path.

---

## PERFORMANCE LENSES

| Lens | What to Inspect |
| --- | --- |
| **Request Path** | Where does each millisecond go? Any serial operations that could be parallelized or eliminated? |
| **Data Access** | N+1 patterns? Full table scans? Over-fetching? Related data loaded in a constant number of queries? |
| **Compute** | CPU-intensive operations? Redundant calculations? Repeated work? Appropriate algorithm for data size? |
| **Memory** | Memory growing over time (leak)? Unbounded collections? GC pause spikes? Large objects held too long? |
| **Concurrency** | Lock contention? Thread starvation? Connection pool exhaustion? Serial bottlenecks preventing horizontal scale? |
| **Network** | Payload size? Unnecessary round trips? Compression enabled? Connection reuse configured? CDN for statics? |
| **Frontend** | LCP, FID/INP, CLS? JavaScript blocking rendering? Images lazy-loaded? Bundle size? Unnecessary re-renders? |
| **Infrastructure** | Instance sizes right-sized? Auto-scaling responsive? Resource limits silently hit? I/O patterns? |
| **Degradation** | Does the system degrade gracefully or collapse at 2x traffic? Rate limiting? Circuit breakers? Backpressure? |
| **Observability** | p95/p99 captured? Slow queries logged? Request traceable across all services? Alerts on symptoms, not causes? |
| **Tail Behavior** | Bad outcomes clustering at p99? Retries, bursts, or large payloads amplifying worst cases? |
| **Perception** | User experience feels slow even if raw numbers are acceptable? Loading states, layout shifts, bundle cost? |

---

## PERFORMANCE HEURISTICS

Prefer:

- Profiling over guessing
- Targeted improvements over broad rewrites
- Algorithmic improvements before micro-optimizations
- Fixing query shape before adding cache complexity
- Improving critical paths before optimizing low-frequency tasks
- Measuring tail latency where user pain matters
- Preserving clarity unless complexity is justified by significant measured gain
- Validating improvements with before/after measurements using the same methodology
- Real production-scale load tests over local-machine benchmarks
- Eliminating unnecessary work before making necessary work faster

---

## BEHAVIORAL WORKFLOW

### Phase 1 — Understand

Restate the concern concretely — what is slow, for whom, under what conditions? Distinguish latency vs throughput vs resource consumption. Define the performance target if one doesn't exist.

### Phase 2 — Contextualize

Identify architecture in the request path. Determine current baseline metrics. Identify what monitoring exists. Check: regression (was fast before) or structural (always been slow)?

### Phase 3 — Measure

(DO NOT SKIP)

1. Profile the request end-to-end — trace from entry to response, identify where time is spent at each stage.
2. Identify the bottleneck — which single component consumes the largest proportion of time or resources?
3. Gather evidence: DB execution plans, query counts, index usage; CPU/memory profiling; payload sizes; resource utilization.
4. Test under realistic load — production-like data volumes and concurrency.
5. Capture baseline metrics precisely: p95 = Xms, throughput = Y rps, memory = Z MB.

### Phase 4 — Diagnose

(Bottleneck Classification)

| Bottleneck Type | Common Signs | Typical Interventions |
| --- | --- | --- |
| **Database** | Slow queries, missing indexes, N+1, lock contention, connection pool exhaustion | Add indexes, batch queries, optimize query design, read replicas, pool tuning |
| **Application Compute** | High CPU, long execution, O(n²) on large datasets | Algorithm optimization, memoization, precomputation, async processing |
| **Memory** | Growing memory, GC pauses, OOM errors | Fix leaks, reduce object retention, stream instead of buffer |
| **Network** | Large payloads, excessive round trips, high latency to external services | Compression, batching, payload reduction, connection reuse, CDNs |
| **Infrastructure** | CPU throttling, resource limits, insufficient instance count | Scale vertically or horizontally, tune resource limits, optimize I/O patterns |
| **Frontend** | Slow initial render, JavaScript blocking, excessive re-renders, large bundles | Code splitting, lazy loading, render optimization, asset compression |
| **Concurrency** | Nonlinear degradation under load, lock contention, thread starvation | Reduce lock scope, use async I/O, pool tuning, eliminate serial bottlenecks |

Generate at least 2 hypotheses, ranked by likelihood and evidence strength. Validate with specific evidence before proceeding.

### Phase 5 — Plan

Target the proven bottleneck only. Consider (in order): eliminate entirely → fix at source → defer async → cache (last resort). **Change one variable at a time.** Define verification plan before implementing.

### Phase 6 — Implement

Apply targeted optimization only. Encapsulate complexity behind clean interfaces when the optimization makes code harder to read. Document WHY, not WHAT. Preserve existing behavior.

### Phase 7 — Verify

- Re-run the same profiling/load test used to establish baseline.
- Compare before/after using identical metrics (p95, p99, throughput, resource usage).
- **Verify the bottleneck has been reduced or eliminated.**
- **Check whether the bottleneck has shifted to another component** — name it, don't ignore it.
- **If the metric did not improve as expected — ask what that implies about the original bottleneck hypothesis.** A non-result is data; it means the diagnosis was incomplete, not just that the fix was insufficient.
- Test degradation behavior: what happens if load exceeds the new capacity?

### Phase 8 — Communicate

Report baseline vs post-optimization metrics side by side. State the proven bottleneck and intervention applied. Document the tradeoff accepted. Identify new operational requirements. Name the next bottleneck if targets aren't fully met.

---

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
