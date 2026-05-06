# RUBRIC: PERFORMANCE QUALITY

**Version:** Gold v1.0
**Layer:** 10 — Evaluation
**Tier:** 3 — Loaded on demand
**File:** rubrics/performance-rubric.md
**Purpose:** Self-assessment matrix for evaluating performance optimization quality — was the bottleneck real, was the optimization effective, and was the measurement rigorous?
**Loaded When:** Phase 7 of any performance optimization task. Evaluating whether a performance improvement is ready for delivery.
**References:** skill-performance.md, workflow-optimize-performance.md

***

## HOW TO USE THIS RUBRIC

After completing performance optimization work, evaluate your output
against each dimension below. Score each dimension.

- If **Problem Quantification** scores **Failing** — STOP. Measure the problem before optimizing.
- If **Bottleneck Identification** scores **Failing** — STOP. Profile before optimizing.
- If **Regression Safety** scores **Failing** — fix regressions. Never trade correctness for performance.
- If **Measurement Rigor** scores **Needs Work** — verify improvement with a proper before/after comparison before delivery.

Use this rubric:

- During optimization review or after a performance-focused change
- When assessing a performance recommendation
- During benchmark comparison of optimization approaches
- During performance investigation review
- When evaluating query, API, or page-speed improvement proposals
- During throughput and latency tradeoff evaluation
- During before/after validation review

***

## WHAT THIS RUBRIC EVALUATES

This rubric evaluates performance work across:

- Problem quantification and metric clarity
- Bottleneck identification and critical-path accuracy
- Optimization targeting and relevance
- Measurement rigor and evidence quality
- Tradeoff awareness and complexity cost
- Regression safety and correctness preservation
- Stopping discipline and proportionality
- System-level awareness
- Sustainability of the gain

This rubric is for judging whether performance recommendations
improve the right thing for the right reason. Performance advice
without measurement is not strong performance work.

***

## EVALUATION MATRIX

### 1. PROBLEM QUANTIFICATION AND METRIC CLARITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Performance problem quantified with precise measurements: current latency at p50, p95, and p99, throughput, resource cost, or specific conditions under which degradation occurs. Target defined with a specific metric and threshold. Gap between current and target is clear. The relevant metric — latency, throughput, render time, memory, CPU, query time — is explicit and user-important or system-important outcomes are stated. |
| **Acceptable** | Problem measured with reasonable precision. Target defined. Gap understood. Key metric identified even if not fully quantified across all percentiles. |
| **Needs Work** | Problem described qualitatively — "it is slow" — without precise measurement. Target vague — "should be faster." No distinction between latency, throughput, render time, or resource cost. No baseline metric established. |
| **Failing** | No measurement at all. Optimization initiated based on assumption or complaint without data. Optimizing something that may not actually be slow. Speculation driving the recommendation. |

***

### 2. BOTTLENECK IDENTIFICATION AND CRITICAL-PATH ACCURACY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Bottleneck identified through profiling — not assumption. Full request path traced with timing per segment. The dominant time-consuming segment identified with evidence. Profiling done under realistic conditions with production-like data and load. Critical path understood. Optimization aimed at the actual limiting factor rather than visible or convenient code. |
| **Acceptable** | Bottleneck identified with reasonable evidence. Profiling performed. The major time consumer identified. Critical path reasonably understood. |
| **Needs Work** | Bottleneck assumed based on experience or intuition. Limited profiling. May be optimizing a non-bottleneck component. Broad tuning with no narrow constraint identified. No path analysis. |
| **Failing** | No profiling performed. Bottleneck guessed. Random optimization applied. May be optimizing code that accounts for two percent of total latency while ignoring the eighty percent segment. Optimizing visible code rather than the actual bottleneck. |

***

### 3. OPTIMIZATION TARGETING AND RELEVANCE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Optimization targets the identified bottleneck and only the bottleneck. No "while I'm here" optimizations of non-bottleneck code. Optimization directly addresses the root cause of the performance issue. Aimed at the highest-leverage constraint. Improvement is on a meaningful path that matters to users or system throughput. |
| **Acceptable** | Optimization targets the bottleneck. Minor adjacent improvements included but justified. Critical-path relevance is real. |
| **Needs Work** | Optimization spread across multiple areas without clear bottleneck justification. Some changes target non-bottleneck code. Local speedup with limited end-to-end value. Non-critical optimization treated as urgent. |
| **Failing** | Optimization applied to code that is not the bottleneck. Or premature optimization — optimizing before measuring. Effort wasted on the wrong target. Chasing low-impact hotspots. |

***

### 4. MEASUREMENT RIGOR AND EVIDENCE QUALITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Before/after measurements taken with the same methodology, same conditions, and same environment. Results compared at p50, p95, and p99. Improvement quantified as both percentage and absolute values. Statistical significance considered for variable workloads. Evidence is strong enough to localize and confirm the bottleneck. |
| **Acceptable** | Before/after measurements taken. Improvement verified and quantified. Same general conditions maintained. Evidence supports the recommendation without being fully rigorous. |
| **Needs Work** | Before measurement exists but after measurement uses different methodology or conditions. Improvement claimed but not rigorously compared. Assumptions presented as proof. |
| **Failing** | No before/after comparison. Improvement assumed based on code inspection — "this should be faster." No data proving the optimization worked. Speculation driving the conclusion. |

***

### 5. TRADEOFF AWARENESS AND COMPLEXITY COST

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Tradeoffs of the optimization explicitly named: code complexity added, data staleness introduced, memory versus speed exchange, maintainability impact, operational burden, observability implications. Tradeoffs justified against the performance improvement gained. Smallest meaningful optimization taken seriously. Cost of the optimization made visible and accepted explicitly. |
| **Acceptable** | Key tradeoffs acknowledged. Complexity increase noted. Justification present. Main costs of the optimization visible. |
| **Needs Work** | Tradeoffs not explicitly discussed. Optimization treated as pure improvement without acknowledging costs. Readability, maintainability, or operational side effects ignored. |
| **Failing** | No awareness of tradeoffs. Optimization added significant complexity, caching staleness, or maintainability burden without acknowledgment. Future developers will not understand why the complex code exists. Hidden tradeoff denial — presented as pure improvement while new costs are quietly introduced. |

***

### 6. REGRESSION SAFETY AND CORRECTNESS PRESERVATION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | All existing tests pass. No functional regressions introduced. Other operations not degraded by the change. Memory usage verified. Correctness preserved while improving performance. Performance monitoring in place to detect future degradation. Side effects checked. |
| **Acceptable** | Tests pass. Basic regression check performed. No obvious side effects. Correctness maintained for primary paths. |
| **Needs Work** | Tests mostly pass. Regression checking incomplete. Potential side effects not fully evaluated. Some uncertainty about correctness preservation. |
| **Failing** | Tests broken by the optimization. Functional regressions introduced. Other operations degraded. Optimization traded correctness for speed. Correctness and performance treated as a tradeoff rather than a requirement. |

***

### 7. STOPPING DISCIPLINE AND PROPORTIONALITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Optimization stopped when target was met. No over-optimization beyond what was needed. Fast enough recognized as the goal. Remaining improvement opportunities documented but not pursued unless justified. Optimization proportionate to the actual problem. |
| **Acceptable** | Target met or very close. Optimization effort proportional to the problem. Diminishing returns recognized before significant over-investment. |
| **Needs Work** | Over-optimized beyond the target. Significant effort spent on marginal improvements. Diminishing returns not recognized. Or under-optimized — gave up before the target was met without justification. |
| **Failing** | Endless optimization without a clear target. Or optimization of the entirely wrong thing. Effort not proportionate to value. Premature or overbuilt optimization that adds complexity without real gain. |

***

### 8. SYSTEM-LEVEL AWARENESS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Analysis considers the full system context: database, network, cache, queueing, rendering, and infrastructure where relevant. Not narrowly code-focused when the bottleneck is elsewhere. Gain will hold under real workload. System-level constraints understood alongside code-level constraints. |
| **Acceptable** | System context considered for primary components. Major system-level factors identified. Analysis is not purely code-focused where other layers matter. |
| **Needs Work** | Analysis too narrowly code-focused. Adjacent system layers — DB, network, cache, infra — not considered where they likely matter. Local speedup without end-to-end system awareness. |
| **Failing** | Completely code-focused analysis when the bottleneck is infrastructure, DB, or network. System-level context entirely absent. Code optimization delivered while the real bottleneck remains untouched. |

***

### 9. SUSTAINABILITY OF THE GAIN

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Gain will hold under real workload and future growth. Ongoing monitoring or regression detection in place. Optimization is stable under change. Performance improvement observable and maintainable over time. Not dependent on fragile assumptions that will break under scale or change. |
| **Acceptable** | Gain expected to hold under normal workload. Basic monitoring in place or recommended. Optimization reasonably stable. |
| **Needs Work** | One-time speedup with no ongoing observability. Improvement depends on fragile assumptions. No regression detection for future releases. Long-term stability not evaluated. |
| **Failing** | Gain likely to degrade under real conditions or future change. Fragile caching or invalidation logic that will fail at scale. No monitoring. Optimization creates a time bomb rather than a durable improvement. |

***

## SCORING SUMMARY

| Dimension | Score | Notes |
| :--- | :--- | :--- |
| Problem Quantification / Metric Clarity |||
| Bottleneck Identification / Critical Path |||
| Optimization Targeting / Relevance |||
| Measurement Rigor / Evidence Quality |||
| Tradeoff Awareness / Complexity Cost |||
| Regression Safety / Correctness |||
| Stopping Discipline / Proportionality |||
| System-Level Awareness |||
| Sustainability of the Gain |||
***

## DELIVERY DECISION

| Result | Decision |
| :--- | :--- |
| All Excellent / Acceptable | ✅ Optimization is sound and verified |
| Problem Quantification Failing | ❌ STOP — measure the problem before optimizing |
| Bottleneck Identification Failing | ❌ STOP — profile before optimizing |
| Regression Safety Failing | ❌ Fix regressions — never trade correctness for performance |
| Measurement Rigor Needs Work | ⚠️ Verify improvement with proper before/after comparison |

***

## MINIMUM PASS STANDARD

Performance work should not be considered strong if it is
weak in any of these high-priority areas:

- Metric clarity — what is being improved and why it matters
- Bottleneck accuracy — optimization aimed at the real constraint
- Evidence quality — measurement drives recommendation, not intuition
- Post-change verification — improvement confirmed, not assumed

Performance advice without measurement is not strong
performance work.

***

## COMMON FAILURE PATTERNS

### Tune-First, Measure-Later

Code changed before the bottleneck was actually measured.
Effort is wasted and the real constraint often survives
untouched.

### Benchmark Vanity

Synthetic wins celebrated while the real workload remains
weakly improved. The system looks faster on paper but
users or operators do not benefit.

### Complexity for Tiny Gains

The system becomes much harder to maintain for a marginal
performance improvement. Diminishing returns ignored.
Maintenance burden paid forever for a one-time micro-win.

### Hidden Tradeoff Denial

The optimization presented as pure improvement while new
costs are quietly introduced. Future developers inherit
complexity with no explanation of why it exists.

### Wrong Bottleneck, Strong Confidence

A convincing story told about the slow path but the
evidence does not truly support it. Confidence outpaces
measurement.

### Optimizing Non-Critical Paths

Local speedup on code that accounts for a tiny fraction
of total latency. The real bottleneck — DB, network,
infra — remains untouched.

### Correctness Traded for Speed

Functional regressions introduced in the name of
performance. Correctness is never an acceptable tradeoff.

***

## FINAL QUESTIONS

Before delivering this optimization, ask:

- Are we optimizing the real bottleneck?
- What metric should improve if this is truly the right change?
- What complexity are we paying for this optimization, and is it worth it?
- Is the improvement verified with real before/after data?
- Will this gain hold under real workload and future change?
- Are we done, or just stopping — and do we know the difference?

***

## A good optimization improves the measured bottleneck on the path that matters, and proves the gain is worth the added cost
