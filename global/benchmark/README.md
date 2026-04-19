# README - BENCHMARKS FOLDER

**Location:** `.antigravity/benchmark/`
**Layer:** Advanced evaluation infrastructure
**Loading Tier:** Evaluation only

---

## PURPOSE

Benchmarks exist to measure whether Anti-Gravity is improving over time.

They are useful, but they are **not** normal task context and should not sit in the ordinary execution path. This layer is for evaluating the OS itself, not for everyday project work.

---

## WHEN TO USE BENCHMARKS

Use benchmarks when:

- comparing system versions
- checking whether a file change improved behavior
- diagnosing capability gaps in the OS
- collecting evidence before changing important system guidance

Do not load benchmarks for normal user tasks.

---

## HOW BENCHMARKS FIT

1. choose a benchmark scenario
2. run Anti-Gravity against it as a normal task
3. evaluate the result with the matching rubric
4. store the result in `memory/benchmark-results.md`
5. compare results over time

Benchmarks depend on rubrics and feed memory, but they remain outside the normal runtime bundle.

---

## STATUS

This folder is advanced infrastructure. It can grow over time, but the OS should remain fully usable without it in day-to-day execution.

---

## FINAL RULE

`benchmark/` should answer whether the OS is actually improving, without pretending benchmark files belong in normal project startup.
