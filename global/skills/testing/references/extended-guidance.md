# Extended Guidance

## Contents

- [BEHAVIORAL WORKFLOW](#behavioral-workflow)
  - [Step 1: Define the Critical Behaviors](#step-1-define-the-critical-behaviors)
  - [Step 2: Choose the Test Level](#step-2-choose-the-test-level)
  - [Step 3: Setup the State (Arrange)](#step-3-setup-the-state-arrange)
  - [Step 4: Execute the Action (Act)](#step-4-execute-the-action-act)
  - [Step 5: Verify the Outcome (Assert)](#step-5-verify-the-outcome-assert)
  - [Step 6: Verify Test Failure](#step-6-verify-test-failure)
  - [Step 7: Clean Up (Teardown)](#step-7-clean-up-teardown)
  - [Step 8: Before Finalizing — Re-check](#step-8-before-finalizing-re-check)
- [THE TDD MICRO-LOOP (EXECUTION CONSTRAINT)](#the-tdd-micro-loop-execution-constraint)
- [BEHAVIORAL SECTIONS](#behavioral-sections)
  - [A. When adding tests for new behavior](#a-when-adding-tests-for-new-behavior)
  - [B. When fixing a bug](#b-when-fixing-a-bug)
  - [C. When deciding test level](#c-when-deciding-test-level)
  - [D. When cleaning up or reviewing existing tests](#d-when-cleaning-up-or-reviewing-existing-tests)
  - [E. When working under time pressure](#e-when-working-under-time-pressure)
- [TEST LAYER GUIDANCE](#test-layer-guidance)
  - [Unit Tests](#unit-tests)
  - [Integration Tests](#integration-tests)
  - [End-to-End Tests](#end-to-end-tests)
  - [Static Analysis / Types](#static-analysis-types)
  - [Manual / Exploratory Checks](#manual-exploratory-checks)
- [KEY DIAGNOSTIC QUESTIONS](#key-diagnostic-questions)
- [NON-NEGOTIABLE CHECKLIST](#non-negotiable-checklist)
- [ANTI-PATTERNS](#anti-patterns)
  - [Mocking the World](#mocking-the-world)
  - [Testing Implementation Details](#testing-implementation-details)
  - [The E2E Ice Cream Cone](#the-e2e-ice-cream-cone)
  - [Ignoring the Sad Path](#ignoring-the-sad-path)
  - [Speed Blindness](#speed-blindness)
  - [No Architectural Awareness](#no-architectural-awareness)
- [OUTPUT CONTRACT](#output-contract)
- [Testing Strategy](#testing-strategy)
- [Assumptions & Mocks](#assumptions-mocks)
- [Test Implementation](#test-implementation)
- [Covered Scenarios](#covered-scenarios)
- [Gaps / Follow-Up](#gaps-follow-up)
- [Instructions to Run / Verify](#instructions-to-run-verify)
- [EXAMPLES OF GOOD BEHAVIOR](#examples-of-good-behavior)
  - [Good: AAA Pattern — Behavioral, Isolated Test](#good-aaa-pattern-behavioral-isolated-test)
  - [Good: Addressing a Flaky Test](#good-addressing-a-flaky-test)
  - [Good: Idempotency Regression Test](#good-idempotency-regression-test)
  - [Good: Pushing Back on Over-Mocking](#good-pushing-back-on-over-mocking)
- [FILE RELATIONSHIPS](#file-relationships)
- [AUTHORITY](#authority)
- [FINAL RULE](#final-rule)
- [VERSION HISTORY](#version-history)

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

- be few but valuable — cover the 3–5 flows that keep the business running
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
**What to do instead:** Push logic tests down the pyramid. Use E2E tests only for the 3–5 critical paths that keep the business running.

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
| Gold v1.1 | Upgrade | Added Testing Lenses (10) from C including Observability/Diagnosability, Boundary Realism, and Confidence Balance; added Behavioral Sections A–E from C including Section E (Time Pressure); added Before-Finalizing Re-check as Step 8 from A; added Final Rule from A; added 'Evaluating existing tests + deletion instruction' as Section D from A; added 10 Core Principles from B; added Dedicated Test Layer Guidance section from B including Static Analysis and Manual/Exploratory; added Testing Heuristics from B; added Speed Blindness anti-pattern from B; added No Architectural Awareness anti-pattern from B; added Authority statement |
