---
name: testing
description: 'Use when the task requires testing guidance. Domain knowledge for TESTING STRATEGY & IMPLEMENTATION'
---

# SKILL: TESTING STRATEGY & IMPLEMENTATION

**Version:** Gold v1.1 (Upgraded — Testing Lenses, Section E Time Pressure, Before-Finalizing Re-check, Final Rule, Core Principles, Test Layer Guidance, Testing Heuristics, Speed Blindness + No Architectural Awareness anti-patterns, Authority Statement added)

**Type:** Specialized Skill Domain

**Tier:** 2 — Loaded by task (when writing tests, or in Builder/Debugger/Reviewer modes)

**File:** skills/skill-testing.md

**Inherits From:** anti-gravity-core.md, system-thinking.md, expert-cognitive-patterns.md

**Primary Mode:** Builder (when implementing tests), Reviewer (when evaluating test quality)

**Secondary Modes:** Architect (when planning test infrastructure)

**Purpose:** Governs how Anti-Gravity approaches software testing, prioritizing developer confidence and deployment velocity over vanity metrics like raw code coverage

***

## MINDSET

The expert's testing mental model calculates ROI strictly based on the economic cost of bugs. They know that a bug caught in production costs exponentially more (up to 100x–1000x) to fix than one caught in a local unit test or CI pipeline.

Therefore, the ultimate, overriding goal of testing is **developer confidence to deploy rapidly** — not the pursuit of arbitrary code coverage percentages. 100% coverage is operationally useless if developers are still terrified to deploy on a Friday.

Experts test *behaviors*, not *implementations*. They understand that if a test breaks when the internal structure of a function changes but the output remains correct, that test is a liability, not an asset. They adapt their strategy based on the context: using the Testing Pyramid (heavy unit, light E2E) for deep backend systems, and the Testing Trophy (heavy integration) for web and UI-heavy applications.

The goal is not to maximize the number of tests. The goal is to maximize **useful confidence per unit of maintenance cost**.

Finally, the expert views flaky tests as a virus. A test that fails randomly destroys trust in the entire suite and is worse than having no test at all.

***

## ACTIVATION TRIGGERS

### When to Load This Skill

- Writing unit, integration, or E2E tests for new features
- Adding regression tests for a bug fix
- Setting up a testing framework (Jest, Cypress, Playwright, JUnit, etc.)
- Evaluating why a CI/CD pipeline is failing
- Reviewing a PR's test coverage
- Designing the test strategy for a new microservice or system
- Deciding between unit, integration, or E2E testing approaches

### Red Flags That This Skill Is Being Neglected

- Writing tests that assert on internal variable states or private methods
- Mocking the database so heavily that the test is essentially testing the mock
- Creating brittle E2E tests that break every time a CSS class changes
- Ignoring flaky tests and just re-running the CI pipeline until it passes
- Writing tests after the entire feature is built, treating them as a chore
- Changes are being merged without any meaningful verification
- The team is chasing coverage numbers without knowing what confidence they actually have

### Usually Pairs With

- `skill-coding.md` — Testing and coding should happen concurrently
- `skill-debugging.md` — Every bug fix requires a regression test to prove it works
- `skill-architecture.md` — To ensure components are designed with testability in mind
- `skill-review-audit.md` — Test quality is a core part of code review
- `skill-security.md` — Security boundaries and auth behavior need integration-level coverage
- `skill-api-design.md` — API contracts deserve explicit boundary tests
- `skill-database.md` — Persistence behavior requires real database integration tests
- `skill-performance.md` — Performance regressions deserve benchmark guardrails

***

## OBJECTIVES

When this skill is active, the goal is to produce tests that:

1. **Provide High Confidence** — Guarantee that the critical paths of the business work
2. **Resist Refactoring** — Do not break when internal implementation details change
3. **Execute Rapidly** — Provide a tight feedback loop for the developer
4. **Act as Documentation** — Explain how the system is supposed to be used
5. **Are Deterministic** — Pass 100% of the time if the code is correct; fail 100% if broken

***

## CORE PRINCIPLES

### 1. Confidence over coverage

Coverage numbers are not the goal. Confidence is the goal.

### 2. Test behavior, not implementation trivia

Tests should survive sensible refactors if external behavior remains correct.

### 3. Use the smallest meaningful test level

Do not jump to E2E if a unit or integration test verifies the behavior better and more cheaply.

### 4. Critical paths deserve stronger protection

High-risk or business-critical behavior should be tested proportionally.

### 5. Bug fixes should create regression defense

A meaningful bug should usually result in a test that prevents recurrence.

### 6. Maintainability matters for tests too

Unreadable or brittle tests degrade trust in the entire suite.

### 7. Integration tests are often the highest ROI

Many failures happen at boundaries; those boundaries deserve explicit verification.

### 8. E2E should be selective

Use E2E for critical journeys, not as a substitute for all other testing.

### 9. Flaky tests are harmful

A test suite that cannot be trusted reduces velocity and encourages bad habits.

### 10. Test strategy should reflect architecture

The system's boundaries, critical paths, and risk profile should shape the test mix.

***

## DECISION FRAMEWORK

Test layers are chosen based on the confidence they provide versus their execution speed and maintenance cost.

| Test Level | Primary Purpose | Cost / Execution Speed | Strategy |
| --- | --- | --- | --- |
| **Static Analysis / Types** | Catching typos, null references, and type mismatches instantly. | Zero maintenance / Instant | Enforce strictly everywhere. |
| **Unit Tests** | Validating complex, isolated business logic, pure functions, and algorithms. | Low maintenance / Very Fast | Use for pure logic and edge-case permutations. Avoid over-mocking. |
| **Integration Tests** | Verifying module boundaries, database interactions, and API contracts. | Medium maintenance / Moderate | Highest ROI for web apps. Use real databases (Testcontainers/Docker) when possible. |
| **E2E Tests** | Validating critical, revenue-generating user flows in a real browser. | High maintenance / Slow | Use sparingly. Only for the absolute most critical paths. |

***

## TESTING LENSES

When designing or evaluating tests, inspect these lenses explicitly:

### 1. Risk Importance

- What failure here would hurt users, data integrity, money, trust, or operations the most?
- Which behavior is business-critical or safety-critical?

### 2. Behavior vs Implementation Detail

- Is the test checking what the system should do, or how the current implementation happens to do it?
- Would a healthy refactor break this test unnecessarily?

### 3. Test Level Fit

- Is this best verified with a unit test, integration test, E2E test, contract check, or static analysis?
- Are we using an expensive level where a cheaper one would work?

### 4. Determinism and Stability

- Is the test stable and repeatable?
- Does it depend on timing, global state, environment drift, or brittle external conditions?

### 5. Coverage Quality

- Are the important paths covered?
- Are edge cases, failure paths, and invariants protected where they matter?
- Is there false confidence because only happy paths are tested?

### 6. Maintenance Cost

- How hard will this test be to keep useful over time?
- Does it create noise, slowness, or constant updates for low value?

### 7. Observability and Diagnosability

- If this test fails, will the team understand why?
- Does it produce a useful, actionable signal or just generic failure noise?

### 8. Regression Protection

- If this exact problem returns later, will the test suite catch it?
- Is the fix protected at the correct level?

### 9. Boundary Realism

- Are we verifying real interactions at the important boundaries?
- Are mocks hiding the very integration risks we care about?

### 10. Confidence Balance

- Does the overall testing strategy create confidence proportionate to the change risk?
- Are we over-investing in low-value checks while under-protecting critical flows?

***

## TESTING HEURISTICS

Anti-Gravity should generally prefer:

- unit tests for pure logic and edge-case permutations
- integration tests for contracts, boundaries, and persistence behavior
- selective E2E for critical user flows only
- deterministic tests over any test that depends on timing or global state
- regression tests for every real bug fixed
- behavior-oriented assertions over implementation-detail assertions
- enough realism to catch likely failures at boundaries
- smaller high-value suites over noisy oversized suites
- real ephemeral databases over mocked database drivers
- confidence per maintenance cost as the primary test ROI measure

***
## REFERENCE LOADING RULES

Load `references/extended-guidance.md` when the task needs detailed implementation rules, examples, edge cases, diagnostics, or verification beyond the core workflow above. Inspect its Contents first and load only the matching sections.

## OUTPUT SHAPE

Deliver the requested artifact or decision, the key rationale and tradeoffs, and a concise verification checklist.

## NON-NEGOTIABLE CHECKLIST

1. Apply the core workflow above.
2. Load matching extended guidance for substantive or high-risk work.
3. Preserve user constraints and verify the result before delivery.
