# BENCHMARK: CODE REVIEW AND AUDIT

**Version:** Gold v1.0
**Layer:** 11 — Verification
**Loading Tier:** 3 — **LOADED ON DEMAND**

***

## PURPOSE

This file contains repeatable test scenarios for evaluating Anti-Gravity's
code review quality — finding real issues, prioritizing correctly, and
providing actionable feedback.

### Evaluate With

- [rubric-communication.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-communication.md)
- [rubric-code-quality.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-code-quality.md)
- [rubric-security.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-security.md)
- [rubric-testing.md](file:///c:/Users/Oviks/antigravitygold/rubric/rubric-testing.md)

### Tests

- `skill-review-audit.md`
- `workflow-review-code.md`

***

## WHAT THIS BENCHMARK TESTS

This benchmark evaluates whether Anti-Gravity can:

- Understand the intent of a change before critiquing it
- Identify high-signal issues rather than low-value style noise
- Distinguish correctness risk from preference
- Prioritize findings by severity — critical before advisory
- Recognize security, authorization, and trust-boundary risks
- Catch logic errors, data consistency problems, and API contract risks
- Identify over-engineering and complexity that does not serve the product
- Produce actionable, collaborative review output
- Make a clear merge recommendation with explicit reasoning

This benchmark should reveal whether Anti-Gravity reviews like a
senior engineer with judgment or a noisy nitpicker.

***

## HOW TO USE THESE BENCHMARKS

1. Pick a scenario below
2. Present it to Anti-Gravity as a real task — do not mention it is a benchmark
3. Let Anti-Gravity process it using its full system — skills, contexts, and workflows active as appropriate
4. Evaluate the output against the rubrics listed above
5. Record the score in `memory/benchmark-results.md`
6. Compare scores across runs and versions to track improvement

***

## EVALUATION DIMENSIONS

Score benchmark outputs across these dimensions:

1. Intent understanding — was the change purpose understood first?
2. Finding quality — were the real issues found, not just the visible ones?
3. Severity prioritization — critical, major, advisory correctly separated?
4. Correctness awareness — logic errors, race conditions, null paths?
5. Security awareness — auth, authz, trust boundary, data exposure?
6. Maintainability awareness — coupling, responsibility mixing, fragility?
7. Testing awareness — regression gaps, missing coverage, flaky risks?
8. Actionability — can the author act on this without guesswork?
9. Tone quality — collaborative and constructive, not accusatory?
10. Signal-to-noise ratio — useful guidance rather than style noise?

***

## SCENARIO 1 — Review With Security Vulnerability

### Prompt [SCENARIO 1]

Review this server action:

```typescript
export async function updateUserProfile(formData: FormData) {
  const session = await auth();
  const userId = formData.get('userId') as string;
  const name = formData.get('name') as string;
  const email = formData.get('email') as string;
  const role = formData.get('role') as string;

  await prisma.user.update({
    where: { id: userId },
    data: { name, email, role },
  });

  return { success: true };
}
```

### What Excellent Output Looks Like [SCENARIO 1]

- 🔴 **CRITICAL** — IDOR vulnerability: userId comes from form data, not the session. Any authenticated user can update ANY user's profile by changing the userId field.
- 🔴 **CRITICAL** — Privilege escalation: role comes from form data. Any user can make themselves an admin by submitting the form with a different role value.
- 🟠 **HIGH** — No input validation. Raw form data is passed directly to the database with no schema or type checking.
- 🟠 **HIGH** — No authorization check. Even if userId came from the session, there is no check that the caller has permission to update profiles.
- 🟡 **MEDIUM** — "as string" type assertion instead of proper validation — could be null and will silently produce incorrect data.
- 🟡 **MEDIUM** — No error handling. Prisma errors will throw unhandled and surface raw errors to the caller.
- 🟡 **MEDIUM** — Should return a Result type, not throw, per project standards.
- 🟢 **LOW** — Email change should trigger re-verification to prevent account takeover via email change.
- Provides specific fix for each finding.
- Tone is collaborative and specific, not accusatory.

### Red Flags [SCENARIO 1]

- Misses the IDOR vulnerability — userId from form data
- Misses the privilege escalation — role from form data
- Focuses on style issues while missing the security issues
- Does not classify findings by severity
- Says "LGTM" or gives only minor stylistic feedback

***

## SCENARIO 2 — Review With Subtle Logic Error

### Prompt [SCENARIO 2]

Review this sprint completion function:

```typescript
export async function completeSprint(sprintId: string) {
  const session = await auth();
  if (!session) return { success: false, error: 'Not authenticated' };

  const sprint = await prisma.sprint.findUnique({
    where: { id: sprintId },
    include: { tasks: true },
  });

  if (!sprint) return { success: false, error: 'Sprint not found' };

  const incompleteTasks = sprint.tasks.filter(t => t.status !== 'done');
  for (const task of incompleteTasks) {
    await prisma.task.update({
      where: { id: task.id },
      data: { sprintId: null, status: 'backlog' },
    });
  }

  const completedPoints = sprint.tasks
    .filter(t => t.status === 'done')
    .reduce((sum, t) => sum + t.storyPoints, 0);

  await prisma.sprint.update({
    where: { id: sprintId },
    data: { status: 'completed', velocity: completedPoints },
  });

  return { success: true };
}
```

### What Excellent Output Looks Like [SCENARIO 2]

- 🟠 **HIGH** — No transaction. If the sprint update fails after tasks are already moved to backlog, data is in an inconsistent state — tasks moved but sprint still active.
- 🟠 **HIGH** — N+1 query pattern. Updating tasks one by one in a loop. Use updateMany for a batch update.
- 🟠 **HIGH** — No authorization check. Any authenticated user can complete any sprint regardless of project membership or role.
- 🟡 **MEDIUM** — storyPoints could be null or undefined. The reduce would produce NaN. Needs null coalescing: (t.storyPoints ?? 0).
- 🟡 **MEDIUM** — No check that the sprint is currently active. Could complete a sprint already in planning or completed state, violating the state machine.
- 🟡 **MEDIUM** — No soft-delete filter on tasks. Tasks with deletedAt set may be included.
- 🟢 **LOW** — No audit logging of the completion event.
- Acknowledges what is done well — auth check present, clear function name, logical overall structure.

### Red Flags [SCENARIO 2]

- Misses the missing transaction — data consistency risk
- Misses the N+1 query pattern
- Misses the null storyPoints issue
- Misses the authorization gap
- Comments only on style and naming without checking the logic

***

## SCENARIO 3 — Review With Over-Engineering

### Prompt [SCENARIO 3]

Review this utility for formatting dates — a Singleton Factory pattern with a nine-option config interface, a class-based DateFormatter, and approximately 200 lines of implementation.

### What Excellent Output Looks Like [SCENARIO 3]

- 🟠 **HIGH** — Massive over-engineering. The project uses an existing date library. A simple formatDate(date) utility function would suffice for all current uses.
- 🟠 **HIGH** — The config interface has nine options, most of which the project does not need. YAGNI violation — building for imagined future requirements.
- 🟡 **MEDIUM** — Classes and Singletons violate project conventions which prefer a functional approach throughout.
- 🟡 **MEDIUM** — This would be the only Singleton in the codebase, introducing a pattern inconsistency with no justification.
- Shows the simpler alternative — approximately ten lines versus two hundred lines — wrapping the existing date library with the two or three formats actually used.
- Tone acknowledges the careful thinking while redirecting to the project's simplicity standard.

### Red Flags [SCENARIO 3]

- Approves the over-engineering with praise for thorough implementation
- Suggests only minor improvements within the complex structure
- Does not question whether the complexity is justified
- Misses the YAGNI violation and convention inconsistency
- Does not compare against project patterns

***

## SCENARIO 4 — Review a Mixed-Scope PR

### Prompt [SCENARIO 4]

Review a PR that includes a feature addition, some refactoring, renamed fields, updated tests, and an API response shape change.

### What Excellent Output Looks Like [SCENARIO 4]

- Understands the PR intent before critiquing.
- Raises concern about mixed-scope changes — harder to review, harder to roll back if one part causes a problem.
- Flags the API response shape change as the highest-risk item — existing consumers may depend on the current shape.
- Prioritizes compatibility and correctness concerns over the refactoring and naming changes.
- Distinguishes blockers from non-blockers clearly.
- Does not rewrite the PR — focuses on review, not replacement.
- Makes a clear recommendation — approve, approve with conditions, or request changes — with explicit reasoning.

### Red Flags [SCENARIO 4]

- Comments mostly on formatting and naming
- Misses the API response shape change as a compatibility risk
- Treats all findings as equal weight
- No merge recommendation or explicit reasoning
- Rewrites sections of the PR rather than reviewing them

***

## SCENARIO 5 — Review a Bug Fix That Works But Is Fragile

### Prompt [SCENARIO 5]

A bug fix resolves the visible issue but the change introduces hidden coupling, lacks regression protection, and mixes unrelated responsibilities into one function.

### What Excellent Output Looks Like [SCENARIO 5]

- Acknowledges that the symptom is fixed.
- Raises concern that the fix may create future problems through the coupling and mixed responsibilities it introduces.
- Specifically flags the absence of a regression test — this bug can return without detection.
- Explains the future cost of the structural issues, not just that they exist.
- Provides targeted improvement suggestions rather than vague "clean this up" comments.
- Distinguishes what must change before merge from what can be addressed as follow-up.

### Red Flags [SCENARIO 5]

- "Looks good since the bug is fixed"
- No mention of coupling, responsibility mixing, or regression risk
- Only style comments
- Does not distinguish the symptom fix from the structural cost

***

## SCENARIO 6 — Review Security-Sensitive Code

### Prompt [SCENARIO 6]

Review code that handles role changes, token refresh, and audit logging. The code appears clean but may have hidden authorization and logging gaps.

### What Excellent Output Looks Like [SCENARIO 6]

- Distinguishes authentication from authorization explicitly.
- Checks that role change operations verify not just that the caller is authenticated but that they have permission to change roles.
- Checks that token refresh does not introduce session fixation or reuse vulnerabilities.
- Checks that audit logging captures who did what and when — not just that something happened.
- Does not let clean formatting or tidy code override security scrutiny.
- Notes what IS done correctly alongside what needs attention.

### Red Flags [SCENARIO 6]

- "Clean code" review with no security depth
- No trust-boundary or privilege-level analysis
- No authz scrutiny — assumes auth is sufficient
- No audit-logging quality assessment
- Commenting on naming rather than the security posture

***

## SCORING GUIDE

For each scenario, evaluate using `communication-rubric.md` and `code-quality-rubric.md` dimensions:

| Dimension | Weight for Review and Audit |
| :--- | :--- |
| Security findings | Critical — missed security issues are the worst review failure |
| Logic correctness | High — did the review catch logical and data errors? |
| Severity classification | High — are findings prioritized correctly? |
| Actionability | High — can the author fix issues based on the feedback? |
| Tone | Medium — is feedback collaborative and constructive? |
| Over-engineering detection | Medium — does the review flag unnecessary complexity? |
| Strengths acknowledged | Medium — are positive aspects recognized? |
| Merge recommendation clarity | Medium — is the final judgment explicit? |

Record all scores in `memory/benchmark-results.md`.

***

## FINAL RULE

A strong review benchmark response protects quality by making the
most important risks visible, prioritized, and actionable.

It finds:

- The right things — not just the visible things
- In the right order — critical before advisory
- For the right reasons — correctness and safety before preference
- And communicates them in a way that improves the work instead of creating noise
