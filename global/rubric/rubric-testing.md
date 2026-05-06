# RUBRIC: TESTING QUALITY

**Version:** Gold v1.0
**Layer:** 10 — Evaluation
**Tier:** 3 — Loaded on demand
**File:** rubrics/testing-rubric.md
**Purpose:** Self-assessment matrix for evaluating the quality of tests — are they testing the right things, at the right level, in the right way?
**Loaded When:** Phase 7 of any task that includes tests. Evaluating test quality during code review.
**References:** skill-testing.md, testing-standards.md

***

## HOW TO USE THIS RUBRIC

After completing testing work, evaluate your output against each
dimension below. Score each dimension.

- If **Coverage Strategy** scores **Failing** — add tests before
  delivery. Critical behaviors are untested.

- If **Test Reliability** scores **Needs Work** — fix flaky tests
  before delivery. Unreliable tests are worse than no tests.

- If **Behavior vs Implementation** scores **Failing** — rewrite
  to test behavior. Tests that break on every refactor
  destroy confidence rather than building it.

Use this rubric:

- When reviewing tests or evaluating test strategy
- After bug-fix verification work
- During Phase 7 of any task that includes tests
- During benchmark comparison of testing approaches
- When reviewing whether a testing strategy provides real confidence or just coverage numbers

***

## WHAT THIS RUBRIC EVALUATES

This rubric evaluates testing quality across:

- Test coverage strategy and risk alignment
- Behavior orientation versus implementation coupling
- Test clarity and structure
- Edge case and failure path coverage
- Test independence and isolation
- Mock appropriateness and reality fit
- Test reliability and determinism
- Regression protection
- Feedback speed and CI fit
- Maintainability of the test suite

This rubric is for judging whether testing is useful —
not just present. A large suite that is fragile and
low-signal is not strong testing.

***

## EVALUATION MATRIX

### 1. TEST COVERAGE STRATEGY AND RISK ALIGNMENT

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Tests target the right code at the right level. Business logic unit tested. Integration points integration tested. Critical flows E2E tested. No over-testing of trivial code. No under-testing of complex code. Coverage reflects risk, not percentage targets. Effort concentrated where failure matters most. Important behaviors and critical paths protected. |
| **Acceptable** | Key behaviors tested. Reasonable balance of test levels. Some gaps in edge case coverage but core paths covered. Critical paths reasonably protected. |
| **Needs Work** | Testing focused on easy-to-test code rather than important-to-test code. Missing coverage on complex logic. Over-testing simple cases while critical paths remain underprotected. Coverage distributed evenly without risk judgment. |
| **Failing** | Critical behaviors untested. No tests for business logic. Tests only cover trivial cases. Or no tests at all. Important behaviors or failure paths receiving no meaningful test attention. |

***

### 2. BEHAVIOR VERSUS IMPLEMENTATION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Tests verify observable behavior and outcomes. Refactoring the internal implementation would NOT break these tests. Tests answer "does it do the right thing?" not "does it do it this specific way?" Tests would still be useful after a harmless refactor. |
| **Acceptable** | Most tests focus on behavior. Minor coupling to implementation in a few tests. Sensible refactoring would preserve most tests. |
| **Needs Work** | Tests coupled to implementation details — specific function calls, internal state. Refactoring would break tests even if behavior is unchanged. Implementation-detail assertions visible. |
| **Failing** | Tests verify HOW code works, not WHAT it does. Every internal change breaks tests. Tests provide false confidence — they pass but do not verify correct behavior. Tests fail for harmless design changes. |

***

### 3. TEST CLARITY AND STRUCTURE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Test names describe the expected behavior clearly. Arrange-Act-Assert structure visible. Each test verifies one logical behavior. A failing test name immediately tells you what is broken. Test code is readable and understandable without decoding. |
| **Acceptable** | Most test names are descriptive. Structure is generally clear. Some tests verify closely related assertions together without creating confusion. |
| **Needs Work** | Vague test names. Tests verify multiple unrelated things. Hard to understand what a failing test means. Test code requires significant effort to interpret. Giant setup boilerplate reducing readability. |
| **Failing** | No descriptive names. No clear structure. Tests are copy-pasted blocks with minor variations. Failing test gives no indication of what is actually broken. Test code is harder to maintain than production code. |

***

### 4. EDGE CASE AND FAILURE PATH COVERAGE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Edge cases systematically identified and tested: null, empty, malformed, boundary values, concurrent, extreme size. Parameterized tests for multiple input variations. Error cases tested as thoroughly as the happy path. Important unhappy-path and invalid-input conditions covered where relevant. |
| **Acceptable** | Major edge cases covered. Null and empty handling tested. Primary error scenarios covered. Most important failure paths represented. |
| **Needs Work** | Only happy path thoroughly tested. A few error cases covered. Boundary values not tested. Failure paths treated as lower priority. |
| **Failing** | No edge case testing. Only the ideal input scenario tested. Bugs will surface immediately with real-world data. Error and invalid-input paths entirely absent. |

***

### 5. TEST INDEPENDENCE AND ISOLATION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Each test runs independently in any order. No shared mutable state. Each test creates its own data. Tests can run in parallel. Failure of one test does not cascade to others. |
| **Acceptable** | Tests are mostly independent. Shared setup via beforeEach that resets correctly. No order dependencies. |
| **Needs Work** | Some tests depend on execution order. Shared state between tests. Failure sometimes cascades. Highly coupled setup in places. |
| **Failing** | Tests depend on each other. Must run in specific order. Shared mutable state causes intermittent failures. Test suite is fragile and untrustworthy. |

***

### 6. MOCK APPROPRIATENESS AND REALITY FIT

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Mocks used at correct boundaries — external services, time, environment. Internal code not mocked — tested for real. Network-level mocking for API boundaries where appropriate. Mock boundaries are principled and consistent. Tests verify real behavior, not mock behavior. Important integrations tested against enough reality to build confidence. |
| **Acceptable** | Mocking generally appropriate. External dependencies mocked. Most internal code tested directly. Realism sufficient for the risk level. |
| **Needs Work** | Over-mocking — internal functions mocked when they could be tested directly. Tests validate that mocks were called, not that behavior is correct. Strategy detached from actual behavior. Mock-heavy fantasy environments. |
| **Failing** | Everything mocked — tests validate a fantasy, pass perfectly but code fails with real dependencies. Or nothing mocked — tests require full infrastructure to run, making them slow and fragile. Neither extreme builds real confidence. |

***

### 7. TEST RELIABILITY AND DETERMINISM

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Tests pass deterministically — every run, every environment. No flaky tests. Async operations properly awaited. Time-dependent tests use fake timers. No environment-specific assumptions. Flaky or timing-sensitive patterns avoided or called out explicitly. |
| **Acceptable** | Tests consistently pass. Rare flakiness quickly identified and fixed. Suite is trusted by the team. |
| **Needs Work** | Some flaky tests. Intermittent failures treated as normal. Tests sometimes fail in CI but pass locally. Suite confidence is degraded. |
| **Failing** | Frequent flaky tests. Team ignores failures because "it is just flaky." Tests undermine confidence instead of building it. CI pipeline is not trusted. Flaky conditions not minimized or acknowledged. |

***

### 8. REGRESSION PROTECTION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Important bug fixes gain regression tests that fail before the fix and pass after. Known failure classes are protected from returning. Repeated issues are turned into tests or guardrails. Recurrence risk meaningfully reduced. |
| **Acceptable** | Major bug fixes gain regression protection. Primary failure classes covered. Recurrence less likely due to test additions. |
| **Needs Work** | Bug fixes added without regression defense. Same class of issue could return without detection. No meaningful test added after serious failures. |
| **Failing** | No regression protection added after bug fixes. Same class of issue has returned or could easily return. Serious failures closed with no durable guardrail. |

***

### 9. FEEDBACK SPEED AND CI FIT

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Suite is fast enough to support healthy development flow. Right tests fast enough to run often. Testing strategy fits the project's CI and delivery workflow. Suite practical to run and trust. Expensive test stages used only where genuinely needed. |
| **Acceptable** | Feedback speed is reasonable. CI integration works. Suite can be run regularly without significant friction. |
| **Needs Work** | Slow feedback loop reducing how often tests are run. Too much pushed into expensive test stages unnecessarily. Friction starting to discourage running the suite. |
| **Failing** | Suite too slow to run regularly. Everything pushed into expensive stages. Friction so high the suite is effectively bypassed. Confidence claimed but not earned through regular execution. |

***

### 10. TEST MAINTAINABILITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Tests are readable, understandable, and modifiable as the system evolves. No excessive setup boilerplate. No duplicated assertion logic. Tests are worth their maintenance cost. Test code held to the same quality bar as production code. |
| **Acceptable** | Tests are generally maintainable. Some boilerplate but manageable. Can be modified when the system evolves without excessive pain. |
| **Needs Work** | Unreadable test code. Giant setup boilerplate. Duplicated assertion logic throughout. Tests starting to become harder to maintain than the production code they cover. |
| **Failing** | Tests are effectively unmaintainable. Boilerplate so complex that modifying tests requires as much effort as rewriting them. Test debt actively discouraging test improvement. |

***

## SCORING SUMMARY

| Dimension | Score | Notes |
| :--- | :--- | :--- |
| Coverage Strategy / Risk Alignment |||
| Behavior vs Implementation |||
| Test Clarity / Structure |||
| Edge Case / Failure Path Coverage |||
| Test Independence / Isolation |||
| Mock Appropriateness / Reality Fit |||
| Test Reliability / Determinism |||
| Regression Protection |||
| Feedback Speed / CI Fit |||
| Test Maintainability |||
***

## DELIVERY DECISION

| Result | Decision |
| :--- | :--- |
| All Excellent / Acceptable | ✅ Tests are trustworthy and valuable |
| Coverage Strategy Failing | ❌ Critical behaviors untested — add tests before delivery |
| Test Reliability Needs Work | ⚠️ Fix flaky tests — unreliable tests are worse than no tests |
| Behavior vs Implementation Failing | ⚠️ Rewrite to test behavior — tests will break on every refactor |

***

## MINIMUM PASS STANDARD

Testing should not be considered strong if it is weak in
any of these high-priority areas:

- Confidence value — tests protect behavior that matters
- Critical-path coverage — important paths are not underprotected
- Test-layer fit — chosen levels match risk and realism needed
- Brittleness control — suite fails for meaningful reasons only

A large suite that is fragile and low-signal is not strong
testing. Testing is not useful just because it is present.

***

## COMMON FAILURE PATTERNS

### Ceremonial Testing

Tests exist to satisfy a coverage number rather than to
protect meaningful behavior. The suite looks healthy but
provides little real confidence.

### Over-Mocking Fantasy

Everything is mocked so thoroughly that tests validate
an imagined system rather than the real one.
Suite passes perfectly while the code fails in production.

### Implementation Coupling

Tests are so tied to internal structure that every
refactor breaks the suite — even when behavior is
unchanged. Creates fear of improvement.

### Happy-Path-Only Testing

Only the ideal input scenario is covered.
Real-world data immediately surfaces bugs that tests
never caught because failure paths were ignored.

### Flaky Test Normalization

Intermittent failures become "normal." Team stops
trusting the suite. CI becomes a formality rather than
a signal. Unreliable tests are worse than no tests.

### Regression Amnesia

Bugs are fixed but no regression test is added.
The same class of issue returns. No institutional memory
is built through the test suite.

### Brittle Cascade

Tests share mutable state and depend on execution order.
One failure causes a cascade. The suite cannot be
trusted or parallelized.

***

## FINAL QUESTIONS

Before delivering this testing work, ask:

- What behavior can we now trust that we could not confidently trust before?
- If the implementation is refactored, will these tests still help?
- Are we gaining real confidence, or just more test files?
- Would a serious bug in the critical path be caught by this suite?
- Is the suite trusted enough that a passing run means something?

***

## A good test strategy protects what matters most, fails for the right reasons, and makes the system safer to change
