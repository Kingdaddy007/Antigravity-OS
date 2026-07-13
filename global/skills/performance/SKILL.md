---
name: performance
description: 'Use this skill when diagnosing or resolving performance problems, optimizing slow systems, or proactively preparing for load. Activated when the user mentions slow response times, high resource consumption, timeouts, memory leaks, or anticipates increased traffic. Signal phrases: "it''s slow", "optimize this", "bottleneck", "memory leak", "high CPU", "query is slow", "Core Web Vitals", "lighthouse score", "cache this", "timeout", "throughput", "latency", "load testing", "can it handle X users", "scale this", "performance is degrading". Also activate for capacity planning and performance-aware code review. Do NOT optimize without profiling evidence.'
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
## REFERENCE LOADING RULES

Load `references/extended-guidance.md` when the task needs detailed implementation rules, examples, edge cases, diagnostics, or verification beyond the core workflow above. Inspect its Contents first and load only the matching sections.

## OUTPUT SHAPE

Deliver the requested artifact or decision, the key rationale and tradeoffs, and a concise verification checklist.

## NON-NEGOTIABLE CHECKLIST

1. Apply the core workflow above.
2. Load matching extended guidance for substantive or high-risk work.
3. Preserve user constraints and verify the result before delivery.