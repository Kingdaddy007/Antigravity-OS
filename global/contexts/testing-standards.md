# TESTING STANDARDS

**Version:** Gold v2.0
**Layer:** 6 — Context (Ground Truth)
**Tier:** 2 — Loaded by task
**File:** contexts/testing-standards.md

**Purpose:** Defines how testing is done in this project — what to test, how to test, what patterns to follow, and what standards apply. Anti-Gravity uses this to generate tests that match your team's approach and integrate with your CI pipeline.

**Loaded When:** Writing or modifying tests, reviewing code (checking verification and regression protection), building features (writing tests alongside), debugging failures (understanding test infrastructure), or refactoring (ensuring behavior preservation).

**Maintenance:** Update when testing tools change, test conventions evolve, or CI pipeline requirements change. Review quarterly. Changes must be agreed by the team before updating this file — not made unilaterally.

---

## HOW ANTI-GRAVITY USES THIS FILE

This file governs every test Anti-Gravity generates. It ensures tests
match **your** testing philosophy, use **your** testing tools, follow
**your** naming conventions, and integrate with **your** CI pipeline.

**When loaded**, Anti-Gravity will:

- Name and organize tests following your file structure conventions
- Generate test data using your factories and patterns
- Respect what your CI pipeline requires before a PR can merge

**When missing or incomplete**, Anti-Gravity will:

- Generate tests using generic patterns that may not run in your environment
- Write tests at the wrong level (over-mocking with unit tests when integration tests are preferred)
- Use test organization patterns inconsistent with your codebase

**When stale**, Anti-Gravity will:

- Use deprecated test utilities or assertion patterns
- Miss new testing conventions the team has adopted
- Generate tests incompatible with updated CI requirements

**Conflict rule:** If this file conflicts with a more specific
stack-level testing file (`stack-context.md`, `infra-context.md`,
framework-specific testing guidelines), the more specific file takes
precedence for that area. Flag the conflict rather than silently
choosing.

**Authoritativeness rule:** When Anti-Gravity’s general training
disagrees with a convention in this file, this file wins. Do not
override these standards with generic testing habits. If a convention
seems wrong, surface the concern — do not quietly substitute a
different pattern.

---

## CURRENT PROJECT POSITION

Anti-Gravity Gold is still primarily a **markdown-native structured
intelligence system**, not a fully locked runtime application stack.

This file therefore has two layers:

| Layer | Name | Contents | When Active |
| :--- | :--- | :--- | :--- |
| **Layer 1** | Philosophy | Testing posture, safe assumptions, project-level standards, change-type expectations, risks, anti-patterns | Active now — applies regardless of stack |
| **Layer 2** | Conventions | Testing stack tools, layer breakdown, mocking rules, test file conventions, CI pipeline details, examples | Filled in and adjusted when the concrete stack is confirmed or changed |

> **Maintenance rule:** When the stack changes, only **Layer 2**
> (conventions) should be updated. Layer 1 (philosophy) stays, unless
> the team explicitly decides to change the project’s testing posture.

This file does **not** yet prescribe:

- Framework-specific test libraries and runners
- Language-specific test directory layout
- CI configuration per tool
- Fixed coverage percentages
- Exact mocking or snapshot policy by framework

Those belong in stack-specific files. This file defines the
**project-level verification standards** that should remain true even
as tools evolve.

---

## TESTING PHILOSOPHY

Anti-Gravity Gold treats testing as a **confidence system**, not a
compliance ritual.

The project is not trying to maximize the number of tests. It is trying
to:

- Protect important behavior
- Reduce fear of change
- Detect regressions early
- Support safe refactoring
- Calibrate confidence honestly
- Make future change cheaper and safer

### Meaning

A weak but passing test suite is not automatically “good.”
One carefully chosen test may be more valuable than many shallow ones.

---

## CURRENT SAFE TESTING ASSUMPTIONS

These assumptions are safe regardless of stack choice:

### Assumption 1 — Important behavior should have a credible verification path

If a behavior matters to users, correctness, safety, or project
integrity, there should be an intentional way to verify it.

### Assumption 2 — Different risks deserve different verification depth

Not all changes need the same amount of testing, but important or risky
behavior should not rely on hope.

### Assumption 3 — Regression protection is valuable project memory

When the team has already paid to understand a bug or fragile behavior,
that learning should usually be preserved as a guardrail.

### Assumption 4 — Manual checking is useful but limited

Manual verification can provide quick confidence, but critical or
repeated behavior should not depend on “we checked it once” as the only
defense.

### Assumption 5 — Test quality matters more than test volume

The project should prefer meaningful, trustworthy tests over broad but
shallow testing theater.

---

## PROJECT-LEVEL TESTING STANDARDS

These standards express the project’s testing posture in concrete form.
Each has a Rule and a Meaning, so Anti-Gravity can self-check before
suggesting tests.

### Standard 1 — Verification should match behavioral importance

**Rule:** Verification effort should be proportional to the importance
and risk of the behavior being changed.

**Meaning:** Trivial low-risk changes may need lighter verification;
critical logic, security-sensitive behavior, data integrity paths, and
known failure-prone surfaces need stronger protection.

---

### Standard 2 — The chosen test level should match the real risk surface

**Rule:** Prefer the **lowest-cost test level that gives credible
confidence** for the behavior in question.

**Meaning:** Local logic does not automatically require expensive
end-to-end validation, and cross-boundary behavior cannot claim safety
just because a unit test passed. Verification should fit the actual
risk, not the most fashionable test style.

---

### Standard 3 — Bug fixes should usually leave behind regression defense

**Rule:** When a bug is diagnosed and fixed, the project should normally
preserve that learning as:

- A regression test, or
- Stronger validation, or
- Improved instrumentation, or
- Alerting / structured failure detection

**Meaning:** A fix that leaves no guardrail behind is weaker than one
that does.

---

### Standard 4 — Happy-path-only confidence is weak confidence

**Rule:** Where the risk justifies it, verification must include more
than just the best-case scenario.

**Meaning:** Important edge cases, key failure paths, invariants,
invalid input behavior, and state transitions (including retry and
idempotency when relevant) should be covered. If the project only proves
the nicest case, it is often not proving enough.

---

### Standard 5 — Brittle tests are a real maintenance cost

**Rule:** A passing but unreliable suite weakens trust in the whole
system.

**Meaning:** The project should avoid tests that fail because of
irrelevant implementation details, unstable timing, unrealistic mocks,
or frequent false alarms. Flaky tests are defects, not background noise.

---

### Standard 6 — Verification should be explicit when incomplete

**Rule:** If a change cannot be fully verified yet, that fact should be
stated explicitly.

**Meaning:** The system should prefer explicit confidence limits,
stated gaps, and follow-up verification plans over fake certainty.

---

### Standard 7 — Testability is part of design quality

**Rule:** Code or structure that is extremely hard to verify should be
treated as a design smell.

**Meaning:** Future implementation and refactoring work should preserve
boundaries and shapes that make verification practical. If something is
hard to test, that is a signal to improve the design, not to skip
verification.

---

## DEFAULT EXPECTATIONS BY CHANGE TYPE

Different kinds of work carry different verification expectations.

### Feature Work

Expected:

- Verification of core intended behavior
- At least one credible path for validating the new capability
- Explicit statement of what is and is not covered

### Bug Fix Work

Expected:

- Reproduction of the symptom where practical
- Verification that the fix removes the symptom
- Regression guardrail (test, validation, or other) where practical

### Refactoring Work

Expected:

- Checks that behavior is preserved (regression tests, golden paths)
- Focus on structural improvement without changing externally observed
  outcomes

### High-Risk Work

Expected:

- Stronger verification depth (multiple layers when needed)
- Broader regression awareness (neighboring behavior, not just the
  touched line)

- Explicit confidence and rollback thinking, especially around
  migrations, security, or data integrity

---

## TESTING STRATEGY

<!-- WHY THIS MATTERS: This is the philosophical foundation of your testing
     approach. It determines where Anti-Gravity invests testing effort
     and what kind of tests it writes by default. Without this, Anti-Gravity
     defaults to writing unit tests for everything — which is usually
     the wrong choice. -->

### Our Approach: Testing Trophy

We prioritize test types by their confidence-to-cost ratio:

```text
              ┌─────────┐
              │   E2E   │  Fewer — critical paths only
             ─┤         ├─
            / └─────────┘ \
           /               \
          ┌─────────────────┐
          │   Integration   │  MOST tests live here
         ─┤                 ├─
        / └─────────────────┘ \
       /                       \
      ┌───────────────────────┐
      │       Unit Tests      │  Complex logic only
     ─┤                       ├─
    / └───────────────────────┘ \
   /                             \
  ┌─────────────────────────────┐
  │  Static Analysis (TS/Lint)  │  Foundation — always on
  └─────────────────────────────┘
```

### What This Means in Practice

- **Static analysis** — TypeScript strict mode and linting catch the most
  bugs at zero runtime cost; treat these as required baseline, not optional
  polish

- **Integration tests** — highest ROI; test real module interactions without
  the brittleness of E2E

- **Unit tests** — reserved for complex, algorithmic, or math-heavy logic
  where isolation provides genuine clarity

- **E2E tests** — reserved for critical revenue-path or user-journey flows
  only

### The Guiding Principle

> We optimize for **deployment confidence**, not coverage percentage.
> A 60% coverage rate where every test verifies meaningful behavior is
> better than 95% coverage where tests are coupled to implementation
> details.

---

## TEST LAYER BREAKDOWN

<!-- WHY THIS MATTERS: Without a layer breakdown, Anti-Gravity defaults
     to the test type it sees most in its training data — usually unit
     tests. Each layer has a distinct job. Using the wrong layer for
     a given situation creates tests that either miss the real risk or
     cost far more than the confidence they produce. -->

### Static Analysis / Type Checks

### Use for

- TypeScript strict mode checking
- Linter and formatter baseline
- Schema validation generation
- Anything that catches bugs at zero runtime cost

### Guidance for Anti-Gravity (Static Analysis)

- Treat these as required baseline verification — not optional polish
- Passing static analysis is not a substitute for behavior tests
- Always assume `"strict": true` and `"noUncheckedIndexedAccess": true`
  are active unless this file or a stack file explicitly says otherwise

---

### Unit Tests

### Use for

- Isolated business logic
- Pure functions with meaningful calculations
- Rules engines and state machine logic
- Transformation and formatting utilities
- Edge-case-heavy logic where isolation adds genuine clarity

### Avoid using for

- Behavior that only makes sense when modules interact together
- Code so simple that TypeScript already protects it
- Anything where the main risk lives at a boundary

### Guidance for Anti-Gravity (Unit Tests)

- Prefer unit tests where logic is isolated and complexity is real
- Keep them fast and deterministic — no network, no disk, no time
- Do not mirror implementation details; test observable behavior
- Parameterized tests (`it.each`) are preferred when the same logic
  needs to be verified across many input/output cases

---

### Integration Tests

### Use for

- Database interactions (queries, state transitions, retrieval)
- Module boundary verification
- API handlers (request → response)
- Server actions / mutations (validate → auth → persist)
- Auth and permission behavior
- Cross-boundary state transitions
- Any risk that lives where two systems meet

### Avoid using for

- Logic that is already verified by a fast unit test at lower cost
- Flows so simple that the integration adds no new confidence

### Guidance for Anti-Gravity (Integration Tests)

- These often provide the highest ROI in real applications
- Prefer integration tests where the main risk is boundary correctness,
  not isolated logic

- Use realistic dependencies where possible — avoid mocking the world
- If a test requires extensive mocking to work, question whether it is
  testing the right thing

---

### End-to-End Tests

### Use for

- Critical business or user journeys that cross multiple layers
- High-value, high-risk flows (login, primary feature, payment, checkout)
- Smoke tests for deployment confidence
- Scenarios where only a full-stack run proves the behavior is correct

### Avoid using for

- Every UI detail or visual state
- Low-risk helper behavior
- Duplication of coverage that already exists at a lower layer

### Guidance for Anti-Gravity (E2E Tests)

- Keep E2E tests selective and high-value — a small strong suite beats
  a large brittle one

- E2E tests are expensive to write, run, and maintain — justify each one
- Never recommend E2E coverage as a substitute for missing integration
  or unit tests

---

## WHAT TO TEST

<!-- WHY THIS MATTERS: This prevents Anti-Gravity from over-testing trivial
     code or under-testing critical code. Testing effort should be
     proportional to risk and complexity — not distributed uniformly. -->

### Always Test — Non-Negotiable

| What | Test Type | Why |
| :--- | :--- | :--- |
| Mutations and server actions | Integration | Input validation, auth checks, and data writes — the highest-risk code path |
| Business logic functions | Unit | Calculations, transformations, and rules need isolated verification |
| Complex hooks with state logic | Unit / Integration | Stateful logic is where UI bugs hide |
| Data query functions | Integration | Verify correct retrieval, filtering, and transformation |
| Critical user flows | E2E | Login, primary feature workflow, revenue paths |
| Edge cases for user input | Unit | Empty, null, malformed, boundary values, special characters |
| State transitions | Unit / Integration | State machines must enforce valid transitions and reject invalid ones |
| Error handling paths | Integration | Verify failures are caught, logged, and surfaced correctly |
| Authorization checks | Integration | Verify users can only access what their role permits |

### Do Not Test — Waste of Effort

| What | Why Not |
| :--- | :--- |
| Simple presentational components with no logic | TypeScript catches structural issues; rendering JSX is not a behavior test |
| Third-party library behavior | Test your integration with the library, not whether the library works |
| Implementation details (internal state, private methods) | Tests coupled to implementation break during refactoring without catching bugs |
| CSS and styling | Unless it affects accessibility or functionality (visibility, focus states) |
| Auto-generated code | Trust the generator; test your queries, not generated client code |
| Getter/setter functions with no logic | If a function just returns a value, TypeScript is sufficient |
| Configuration files | Unless configuration logic is dynamic and could fail |

---

## WHAT WE CONSIDER OVER-TESTING

- Writing unit tests for every function regardless of complexity or risk
- Testing the same behavior at three layers when one layer gives full confidence
- Snapshot-testing every component render output
- Asserting internal implementation state instead of observable behavior
- Writing tests to inflate coverage numbers rather than improve confidence

> **Standard:** We optimize for **deployment confidence**, not coverage percentage.
> A 60% coverage rate where every test verifies meaningful behavior is
> better than 95% coverage where tests are coupled to implementation
> details.

---

## WHAT MATTERS MORE THAN RAW COVERAGE

1. **Confidence on critical paths** — important behavior is protected
2. **Stable tests** — the suite produces trustworthy signals
3. **Useful regression defense** — known bug classes cannot silently return
4. **Realistic boundary verification** — tests reflect real system behavior,
   not mock fantasies

---

## MOCKING STANDARDS

<!-- WHY THIS MATTERS: Over-mocking creates tests that validate fantasies.
     Under-mocking creates tests that are slow and flaky. Anti-Gravity
     needs clear mock boundaries to generate tests at the right level
     of isolation — not tests that pass while the real system is broken. -->

### What to Mock

| Dependency | Mock Strategy | Why |
| :--- | :--- | :--- |
| External third-party APIs | Network-level interception (e.g., MSW) | Intercepts at the real fetch boundary so code uses real request logic |
| Database client | Mock per-method for unit tests; test DB for integration | Unit tests should not require a running database |
| Auth session | Mock the auth helper return value | Tests must control authentication state precisely |
| Time / Date | Fake timers | Tests involving time must be deterministic |
| Environment variables | Stub via test utilities | Tests should not depend on a developer's local environment |
| File system | Mock the storage abstraction | Tests should not create or read real files |

### What NOT to Mock

| Dependency | Why Not |
| :--- | :--- |
| Your own utility functions | If you mock your own code, you are testing the mock, not the code |
| Validation schemas | Validation is core logic — test it for real |
| State management stores | Test with real stores — they are fast and deterministic |
| Internal contracts central to correctness | Mocking these hides the most important failures |

### The Mock Boundary Principle

> **Avoid mocking the world.** Prefer reality where confidence depends
> on real interaction behavior. Use mocks to control external and
> non-deterministic boundaries — not to avoid all integration.

### Guidance for Anti-Gravity — Mocking

- Default to the lowest-mock test that still runs fast and deterministically
- If a test requires mocking most of its dependencies, treat that as a
  signal that the wrong test layer is being used

- Mock external boundaries; keep internal behavior real
- Never use empty mock implementations that return nothing — they
  produce tests that always pass

---

## DATABASE TESTING EXPECTATIONS

- Integration tests should use a separate test database — never the development database
- The test database should be reset between test suites (transaction rollback or equivalent)
- No shared mutable state between tests — each test owns its data
- Test data generated using factory functions, not SQL dumps or hardcoded fixtures
- If the project values true integration confidence, do not mock the database layer in integration tests

---

## API TESTING EXPECTATIONS

API tests should cover:

- Request validation (invalid input → correct error shape)
- HTTP status codes (correct code per outcome)
- Error response format (matches the project's standard error shape)
- Authentication and authorization (unauthenticated → 401, unauthorized → 403)
- Response contract (shape and field presence, not just truthy)
- Pagination behavior where relevant
- Edge-case payloads (empty, null, oversized, special characters)

### Guidance for Anti-Gravity (API Testing)

- API tests should verify consumer-visible contract behavior — not just
  that internal functions are called

- Test the full request → handler → response cycle where possible, not
  only the handler function in isolation

---

## FRONTEND / UI TESTING EXPECTATIONS

Frontend tests should cover:

- Component behavior under different prop states
- Form validation feedback (correct error shown for invalid input)
- Critical interaction states (click, submit, keyboard)
- Loading, empty, and error states
- Accessibility basics where relevant (labels, roles, focus management)
- Critical user journeys at E2E level

### Guidance for Anti-Gravity (UI Testing)

- Test what the user sees and can interact with — not internal state
- Avoid brittle tests tightly coupled to CSS class names or DOM structure
- Prefer user-event interactions over direct event firing for realistic
  behavior simulation

- Never test that a component renders — test that it behaves correctly

---

## MANUAL VERIFICATION EXPECTATIONS

Not all critical behavior can or should be fully automated at every stage.

If manual checks are still required in some areas, they must be named
explicitly — not left as silent assumptions:

- Critical UI changes should be manually checked in staging before release
- Migration-related changes may require manual rollout validation
- Permission model changes may require manual scenario testing
- Analytics instrumentation may require post-deploy verification

### Guidance for Anti-Gravity (Manual Verification)

- Do not assume automation is complete in areas this project still relies on manual checks
- Where manual verification is required, make it explicit — name the check, the owner, and the trigger condition
- Never recommend "verified" for a change that still has outstanding manual checks

---

## REGRESSION TESTING EXPECTATIONS

### Standard

Bug fixes should normally include regression protection.

### Alternative Guardrails

When a regression test is not practical, one of these alternatives
should be present:

| Alternative | When to Use |
| :--- | :--- |
| Assertion | When the invariant can be checked at runtime |
| Validation boundary | When the input class causing the bug can be blocked early |
| Monitoring / alerting | When the failure mode is observable in production metrics |
| Contract test | When the failure lives at a system boundary |
| Manual deployment gate | When no automated option is practical |

### Guidance for Anti-Gravity (Regressions)

- If a bug was important enough to fix, it is usually important enough
  to protect against recurrence

- Prefer reproducing the failure in a test first when practical
- If no regression test is practical, state explicitly which alternative
  guardrail is in place and why

- Never leave a bug fix with no guardrail of any kind

---

## CI / MERGE / RELEASE EXPECTATIONS

### What Must Pass Before Merge

- Static analysis (type checks, linting)
- Unit and integration tests for changed areas
- Any required snapshot updates (when snapshots are allowed by policy)

### What Should Block Release

- Failing tests on main or release branches
- Failing E2E smoke tests for critical user journeys
- Known critical bugs without mitigation plan

---

## FLAKY TEST POLICY

Flaky tests are treated as **defects**, not tolerated noise.

- A test that fails intermittently without code changes is flaky
- Flaky tests destroy trust in the suite and must not be normalized

### Policy

1. Quarantine quickly — mark flaky tests with `it.skip()` or equivalent,
   including a `// FLAKY:` comment explaining the symptoms

2. Create a fix ticket with appropriate priority
3. Fix, replace, or remove flaky tests as soon as practical
4. Do not leave known flaky tests running in CI

### Guidance for Anti-Gravity (Flaky Tests)

- Never introduce timing-sensitive patterns that depend on arbitrary delays (`setTimeout` sleeps)
- Favor `waitFor`, `findBy`, and fake timers over fixed sleeps
- If a proposed test looks fragile, prefer a different test strategy over adding more waiting

---

## COVERAGE POLICY

Coverage is a **diagnostic signal**, not the primary success metric.

### Policy

- No hard minimum coverage percentage is enforced as a gate by default
- Coverage reports are generated to identify untested critical paths
- Coverage is used to guide investment, not to judge individual PRs

### How to Read Coverage

- High coverage + confident deploys → healthy suite
- High coverage + still afraid to deploy → tests are low-signal or over-coupled to implementation
- Low coverage + confident deploys → likely under-testing, getting lucky
- Low coverage + afraid to deploy → serious testing investment needed

### Focus Areas

- Mutations and server actions
- Business logic functions
- State transition logic
- Authorization checks

### Guidance for Anti-Gravity (Coverage)

- Use coverage as a weak signal — never as the only measure of trust
- Prefer adding a few high-value tests in critical areas over many low-value tests in safe areas

---

## TEST QUALITY STANDARDS

Good tests in this project should be:

- Deterministic — same input, same output, no random failures
- Behavior-oriented — test what the system does, not how it does it
- Easy to understand — readable enough to serve as documentation
- Appropriately isolated — not over-coupled to global state
- Maintainable — small enough and clear enough to evolve with the code
- Meaningful when they fail — failures indicate real issues, not noise

### Avoid tests that

- Fail randomly or depend on timing
- Assert only that mocks were called, not that behavior is correct
- Break during harmless refactors because they are tied to implementation
- Assert so little that they can never truly fail
- Are too hard to read for a reviewer to understand quickly

---

## GOOD VS BAD TEST EXAMPLES

### Testing Behavior vs Implementation Details

❌ **Bad — tests internal state:**

```typescript
it('should set isLoading to true when fetching', () => {
  const { result } = renderHook(() => useTaskList('project-1'));

  // Implementation detail — breaks if we change how loading is tracked
  expect(result.current.isLoading).toBe(true);
});
```

✅ **Good — tests user-visible behavior:**

```typescript
it('should show loading skeleton while fetching tasks', () => {
  render(<TaskList projectId="project-1" />);

  expect(screen.getByTestId('task-list-skeleton')).toBeInTheDocument();
});
```

---

### Over-Mocking vs Real Behavior

❌ **Bad — tests the mock, not the code:**

```typescript
it('should call formatDate', () => {
  vi.mock('./formatDate', () => ({
    formatDate: vi.fn(() => 'Jan 1'),
  }));

  render(<TaskCard task={testTask} />);

  expect(formatDate).toHaveBeenCalledWith(testTask.createdAt);
});
```

✅ **Good — tests real output:**

```typescript
it('should display the formatted creation date', () => {
  const task = createTestTask({ createdAt: new Date('2024-01-15') });

  render(<TaskCard task={task} onSelect={vi.fn()} />);

  expect(screen.getByText('Jan 15, 2024')).toBeInTheDocument();
});
```

---

### Assertion Clarity

❌ **Bad — vague assertion:**

```typescript
it('works', () => {
  const result = calculateVelocity();
  expect(result).toBeTruthy();
});
```

✅ **Good — specific assertion:**

```typescript
it('should return the average of completed points across sprints', () => {
  expect(calculateVelocity()).toBe(10);
});
```

---

### Test Independence

❌ **Bad — depends on test order:**

```typescript
let sharedTask: Task;

it('should create a task', async () => {
  sharedTask = await createTask({ title: 'Test' });
  expect(sharedTask.id).toBeDefined();
});

it('should update the task', async () => {
  await updateTask(sharedTask.id, { status: 'done' });
});
```

✅ **Good — each test owns its own data:**

```typescript
it('should update a task status', async () => {
  const task = createTestTask({ status: 'todo' });
  prismaMock.task.update.mockResolvedValue({ ...task, status: 'done' });

  const result = await updateTaskStatus(task.id, 'done');

  expect(result.success).toBe(true);
  expect(result.data.status).toBe('done');
});
```

---

## TESTING RISKS TO WATCH

- **Confidence theater** — mistaking visible testing activity for real confidence
- **Bug learning loss** — merging fixes without preserving what was learned as guardrails
- **Brittle suite decay** — tests that break often and are ignored
- **Manual-check dependency** — critical behavior quietly relying on ad hoc manual testing
- **Verification vagueness** — calling a change “tested” without naming what was actually verified

---

## KNOWN TESTING GAPS / WEAK AREAS

Document known weak spots so Anti-Gravity can be more cautious:

- [Fill in] — limited integration coverage around background jobs
- [Fill in] — older modules with inconsistent tests
- [Fill in] — auth edge cases under-tested
- [Fill in] — E2E suite slow and brittle
- [Fill in] — analytics instrumentation poorly verified

### Guidance for Anti-Gravity (Known Gaps)

- Treat these as caution zones — do not assume they are adequately protected
- Prefer stronger verification recommendations in these areas

---

## EXCEPTIONS / PRAGMATIC RULES

Not every area gets the same testing investment.

Examples where lighter testing may be acceptable:

- Legacy modules where full retrofit is too expensive for now
- Migration scripts that are run once and reviewed carefully
- Generated code that is already covered by generator tests
- Low-risk glue code that is exercised indirectly by integration tests

### Guidance for Anti-Gravity (Exceptions)

- Apply testing standards intelligently, not mechanically
- If a lower level of testing is acceptable, explain why in context
- Do not use “legacy” or “low risk” as blanket excuses — be specific

---

## INSTRUCTIONS FOR ANTI-GRAVITY

When working in this project, Anti-Gravity should:

1. Match test recommendations to the project’s testing philosophy and risk profile
2. Prioritize coverage where failure matters most
3. Distinguish baseline verification (static analysis) from meaningful behavior tests
4. Prefer behavior-focused tests over implementation-detail tests
5. Align recommendations with actual CI gates and runtime expectations
6. Avoid introducing brittle, low-value tests
7. Recommend regression protection for important bug fixes where appropriate
8. Be explicit about when manual verification is still required
9. If a testing recommendation conflicts with current project standards, explain why and surface the conflict
10. Use this file to ground testing strategy in real project expectations, not generic testing dogma

---

## WHAT FUTURE FILES SHOULD ASSUME

Future stack-specific files should assume that:

- Verification is part of completion, not optional cleanup
- Testing in this project means confidence-building, not box-ticking
- Stack-specific testing details may refine but must not weaken these project-level standards
- Bug fixes, features, and refactors all carry appropriate verification expectations

---

## CROSS-REFERENCES

| Related Context File | Relationship |
| :--- | :--- |
| `stack-context.md` | Defines testing tools and versions this file assumes |
| `coding-standards.md` | Test code follows the same coding conventions |
| `architecture-context.md` | Feature organization determines test file location |
| `infra-context.md` | CI/CD pipeline runs the test suite and enforces gates |
| `security-baselines.md` | Auth and security tests must match security posture |
| `performance-baselines.md` | Performance-sensitive tests align with perf budgets |
