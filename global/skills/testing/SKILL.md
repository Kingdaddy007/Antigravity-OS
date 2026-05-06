---
name: TESTING STRATEGY & IMPLEMENTATION
description: Domain knowledge for TESTING STRATEGY & IMPLEMENTATION
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

The expert's testing mental model calculates ROI strictly based on the economic cost of bugs. They know that a bug caught in production costs exponentially more (up to 100xâ€“1000x) to fix than one caught in a local unit test or CI pipeline.

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

## BEHAVIORAL WORKFLOW

When tasked with testing a feature or system, follow this sequence:

### Step 1: Define the Critical Behaviors

- What are the most important things this code must do?
- Write the scenarios in plain English: "It should reject passwords under 8 characters."

### Step 2: Choose the Test Level

- Pure algorithmic calculation? → Unit Test
- Reads/writes to a database or calls another module? → Integration Test
- Multi-page user journey or revenue-critical flow? → E2E Test

### Step 3: Setup the State (Arrange)

- Create the exact state needed for the test.
- Use factories or builders to generate test data, not massive hardcoded JSON blobs.
- Avoid shared global state between tests. Ensure test isolation.

### Step 4: Execute the Action (Act)

- Trigger the specific behavior being tested.

### Step 5: Verify the Outcome (Assert)

- Assert on the observable output or state change, not internal mechanics.
- Check both the Happy Path and the Sad Path (error handling, failure behavior).

### Step 6: Verify Test Failure

- Temporarily break the application code to ensure the test actually fails.
- If the test still passes when the code is broken, the test is useless.

### Step 7: Clean Up (Teardown)

- Ensure the test cleans up after itself (truncating database tables, resetting state) so it does not pollute subsequent tests.

### Step 8: Before Finalizing — Re-check

- Re-check whether the proposed tests map to important behavior.
- Re-check whether the chosen test level is justified.
- Re-check whether the tests would survive reasonable refactors.
- Re-check whether any critical path is still weakly covered.
- Re-check whether the verification plan actually increases confidence or just adds test count.

***

## THE TDD MICRO-LOOP (EXECUTION CONSTRAINT)

When writing new features or fixing bugs, execution **must** follow this strict micro-loop sequence. Do not combine these steps into a single action.

1. **Write failing test:** Implement the test code.
2. **Verify it fails:** Run the test. Confirm it fails exactly as expected.
3. **Write minimal code:** Implement only the exact code needed to pass the test.
4. **Verify it passes:** Run the test again.
5. **Commit:** Save the working state.

***

## BEHAVIORAL SECTIONS

### A. When adding tests for new behavior

1. State the behavior or invariant that must hold.
2. Identify the most appropriate test level.
3. Cover the primary success path.
4. Add edge-case or failure-path checks where risk justifies it.
5. Keep the test focused on observable behavior.
6. Ensure test failure will be interpretable — a failing test should tell you exactly what broke.

### B. When fixing a bug

1. Reproduce the bug in a failing test before fixing where practical.
2. Ensure the test fails for the right reason.
3. Apply the minimal fix.
4. Verify the regression test passes after the fix.
5. Check whether adjacent edge cases also deserve coverage.

### C. When deciding test level

1. Use a unit test for pure logic and local invariants.
2. Use an integration test when the risk lies in component, DB, API, or boundary interaction.
3. Use E2E tests sparingly for critical user flows and system-spanning regressions.
4. Use contract-like checks when external or inter-service compatibility matters.
5. Use static analysis as the zeroth layer — it is the cheapest and fastest check of all.

### D. When cleaning up or reviewing existing tests

1. Identify brittle tests that fail for non-behavioral reasons.
2. Identify duplicate or low-value tests adding noise without confidence.
3. Identify slow, flaky, or redundant tests.
4. Check whether boundaries and contracts are actually protected.
5. Preserve the important behavioral coverage while simplifying the suite.
6. Recommend deletion or refactoring of low-value tests where justified — more tests is not always better.

### E. When working under time pressure

1. Protect the highest-risk behavior first.
2. Reduce feature scope before dropping essential verification.
3. If a temporary gap must remain, state it explicitly and create follow-up ownership.
4. A quick manual check may be enough for low-risk changes, but critical changes still need durable regression protection.

***

## TEST LAYER GUIDANCE

### Unit Tests

Best for:

- pure logic, calculations, transformations
- validation rules and branching behavior
- edge-case-heavy functions
- deterministic domain behavior

Good unit tests should:

- run fast
- be deterministic
- be easy to understand
- test meaningful logic, not framework defaults
- avoid excessive mocking

Avoid when: the actual risk lives in external interaction or boundary behavior.

### Integration Tests

Best for:

- module boundaries and service interactions
- database reads/writes and persistence rules
- API contracts and auth flows
- state coordination and event/queue transitions
- repository behavior with real storage

Good integration tests should:

- use real ephemeral databases (Testcontainers/Docker) rather than mocked drivers
- verify realistic collaboration between components
- catch the boundary failures that unit tests cannot see
- reflect actual contracts and state transitions

Avoid when: a pure logic unit test would provide the same confidence far more cheaply.

### End-to-End Tests

Best for:

- critical user journeys: login, checkout, onboarding, payment
- major business-critical cross-system behavior
- high-value flows where lower-level tests miss the real risk

Good E2E tests should:

- be few but valuable — cover the 3â€“5 flows that keep the business running
- not try to replace all other testing
- avoid becoming an unmaintainable pile (the E2E Ice Cream Cone)

Avoid when: the behavior can be verified faster and more reliably at the integration layer.

### Static Analysis / Types

Best for:

- null reference prevention
- type contract enforcement
- catching typos and invalid calls at zero cost
- compiler-level guarantees before a single test runs

This layer should always be active. It is the cheapest test form that exists.

### Manual / Exploratory Checks

Best for:

- fast local confidence on low-risk changes
- visual and experiential validation
- discovering issues not obvious from predefined tests

Avoid when: treating manual checks as durable regression protection for critical behavior.

***

## KEY DIAGNOSTIC QUESTIONS

Ask these when writing or reviewing tests:

- **The Refactor Check:** If I completely rewrite the internal logic without changing inputs or outputs, will this test still pass?
- **The Reality Check:** Am I mocking so many dependencies that I am testing a fantasy environment instead of the real system?
- **The Flake Check:** Does this test rely on `setTimeout`, system clocks, or network speeds? If yes, it will eventually flake.
- **The ROI Check:** Does the cost of maintaining this slow E2E test outweigh the cost of the bug it is trying to prevent?

***

## NON-NEGOTIABLE CHECKLIST

- [ ] Tests verify behavior and public interfaces, not internal implementation
- [ ] Tests fail when the code is broken (verified by Step 6)
- [ ] Mocks are used only for boundaries that are too slow or expensive to hit (external APIs, payment gateways)
- [ ] Database operations are tested against a real database instance, not mocked
- [ ] Flaky tests are immediately quarantined, repaired, or deleted
- [ ] Bug fixes gain regression protection where practical
- [ ] Critical paths are not left under-verified
- [ ] The test suite is not being made more brittle than the confidence gain justifies

***

## ANTI-PATTERNS

### Mocking the World

**What it looks like:** Writing a test for a database repository where the connection, query builder, and result set are all mocked.
**Why it is harmful:** The test validates a fantasy environment. It passes in CI but fails immediately in production when it hits a real SQL syntax error or constraint.
**What to do instead:** Use a real ephemeral database (SQLite in-memory or PostgreSQL via Docker/Testcontainers) for integration tests. Only mock external 3rd-party boundaries like Stripe or Twilio.

### Testing Implementation Details

**What it looks like:** Asserting that `methodA` was called exactly twice, or checking the value of a private variable.
**Why it is harmful:** It ties the test to code structure. When a developer refactors cleanly without changing output, the test breaks and discourages future refactoring.
**What to do instead:** Black-box testing. Give it an input, assert on the output or the final observable state change.

### The E2E Ice Cream Cone

**What it looks like:** 500 slow, brittle UI tests and only 10 unit tests.
**Why it is harmful:** The CI pipeline takes 2 hours to run. Tests fail randomly due to network blips or UI redesigns. Developers stop trusting the suite.
**What to do instead:** Push logic tests down the pyramid. Use E2E tests only for the 3â€“5 critical paths that keep the business running.

### Ignoring the Sad Path

**What it looks like:** Five tests that prove a form submits successfully and zero tests for what happens when the API returns a 500.
**Why it is harmful:** The happy path is rarely where catastrophic system failures occur.
**What to do instead:** Specifically write tests that force errors, timeouts, and boundary conditions to ensure the system degrades gracefully.

### Speed Blindness

**What it looks like:** Creating test suites so slow that developers stop running them locally or stop trusting CI feedback.
**Why it is harmful:** Tests that are not run or not trusted provide no value. A slow suite degrades the entire feedback loop and encourages shortcuts.
**What to do instead:** Optimize for fast feedback. Push heavy tests to a separate CI stage. Keep the primary local loop under 30 seconds.

### No Architectural Awareness

**What it looks like:** Testing without considering boundaries, contracts, and system structure — every test is either a micro-unit test or a full E2E test with nothing in between.
**Why it is harmful:** The most important failures happen at architectural boundaries. Ignoring those boundaries means the suite protects code that works in isolation but fails in composition.
**What to do instead:** Map the system's real boundaries and design the test mix to cover them explicitly at the integration level.

***

## OUTPUT CONTRACT

When generating test code or strategy, follow this structure:

```markdown

## Testing Strategy

Brief explanation of what level (Unit/Integration/E2E) is being used and why.

## Assumptions & Mocks

Explicitly state what is being mocked and what is real.

## Test Implementation

[The code, cleanly separated into Arrange / Act / Assert blocks]

## Covered Scenarios

- [x] Happy Path: [Description]
- [x] Sad Path: [Description]
- [x] Edge Case: [Description]

## Gaps / Follow-Up

What still remains untested or should be monitored.

## Instructions to Run / Verify

How a developer should execute this test locally.
```

***

## EXAMPLES OF GOOD BEHAVIOR

### Good: AAA Pattern — Behavioral, Isolated Test

```javascript
// âœ… Good: Clear, behavioral, isolated
test('rejects orders with negative quantities', () => {

  // Arrange
  const inventory = new InventorySystem();
  const order = { itemId: 'sku-123', quantity: -5 };

  // Act & Assert
  expect(() => {
    inventory.processOrder(order);
  }).toThrow(InvalidOrderError);

});
```

### Good: Addressing a Flaky Test

**User:** "This UI test fails about 10% of the time in CI, but passes locally."
**Anti-Gravity:** "This is a classic flaky test. The code uses `setTimeout(1000)` to wait for the modal to appear. In a busy CI environment, rendering might take 1.2 seconds, causing a failure. *Fix:* Replace the explicit timeout with a deterministic wait: `await screen.findByText('Success')`. This polls the DOM and resolves the exact millisecond the text appears — no timing dependency."

### Good: Idempotency Regression Test

"The bug was that retries created duplicate invoices. Add a regression test that simulates a retry on the same idempotency key and proves only one invoice record is persisted. That is the guardrail that protects the fix — not just a re-run of the happy path."

### Good: Pushing Back on Over-Mocking

"I recommend against mocking the PostgreSQL driver to test the UserRegistration service. If we mock the driver, we will not catch foreign key violations or unique constraint errors. Let's write this as an integration test using an ephemeral test database instead. It will be slightly slower, but the confidence ROI is vastly higher."

***

## FILE RELATIONSHIPS

| Related File | Relationship |
| --- | --- |
| `anti-gravity-core.md` | Core principle: "Verify before concluding." Testing is the automated manifestation of this principle. |
| `system-thinking.md` | Used to inspect verification points, boundaries, and failure modes worth protecting. |
| `skill-coding.md` | Testing dictates how code should be structured — code must be modular and injectable to be testable. |
| `skill-debugging.md` | Every root cause found in debugging must result in a new regression test written via this skill. |
| `expert-cognitive-patterns.md` | Prevents confidence illusions, over-simplification, and weak expected-value thinking in test strategy. |
| `quality-bar.md` | Defines what level of test coverage is required for Tier 1 (production) vs Tier 3 (exploration) code. |

***

## AUTHORITY

If any other file in this system appears to contradict this file on **how testing should be reasoned through as a domain skill**, this file is authoritative unless a project-level override is explicitly documented.

***

## FINAL RULE

Tests are there to buy confidence.

A strong testing result should make it clearer what behavior is protected, what failures are now less likely to escape, what still remains uncertain, and how safely the system can now change.

***

## VERSION HISTORY

| Version | Date | Changes |
| --- | --- | --- |
| Gold v1.0 | Initial | Complete testing skill — economic confidence mindset, Pyramid vs Trophy framework, static analysis layer, 7-step AAA workflow with Step 6 verify-failure, diagnostic questions, 4 anti-patterns with What/Why/Fix, output contract |
| Gold v1.1 | Upgrade | Added Testing Lenses (10) from C including Observability/Diagnosability, Boundary Realism, and Confidence Balance; added Behavioral Sections Aâ€“E from C including Section E (Time Pressure); added Before-Finalizing Re-check as Step 8 from A; added Final Rule from A; added 'Evaluating existing tests + deletion instruction' as Section D from A; added 10 Core Principles from B; added Dedicated Test Layer Guidance section from B including Static Analysis and Manual/Exploratory; added Testing Heuristics from B; added Speed Blindness anti-pattern from B; added No Architectural Awareness anti-pattern from B; added Authority statement |
