# MEMORY: COMMON PATTERNS

**Version:** Gold v1.0
**Layer:** 12 — Institutional Learning
**Tier:** 3 — Loaded on demand
**File:** memory/common-patterns.md
**Purpose:** Captures reusable patterns that work well in YOUR project — proven solutions to recurring problems that should be applied consistently rather than reinvented each time.
**Loaded When:** Implementing something that has a known pattern. Building a feature similar to a previous one. Looking for the standard way to do something in this project.
**Format:** Append-only. Mark patterns as deprecated rather than deleting.

---

## WHEN TO ADD AN ENTRY

Add an entry when:

- You solve a problem and realize the same pattern will apply elsewhere
- A pattern has proven valuable across three or more uses — the Rule of Three
- The team standardizes an approach that should become the default
- A code review reveals a better way that should replace prior practice

Do NOT log:

- Patterns already documented in `coding-standards.md` — that is the conventions file
- Generic programming patterns that are not project-specific
- One-off solutions that are unlikely to recur
- Patterns that are still too speculative to validate
- Vague observations with no practical implementation guidance

---

## HOW TO USE THIS FILE

Anti-Gravity should consult this file when:

- Implementing something that may have a known solution shape
- Building a feature similar to a previous one
- Looking for the standard way to solve a recurring problem in this project
- A code review or postmortem suggests a pattern should be standardized

This file helps Anti-Gravity become faster and more accurate by reusing known-good approaches instead of rediscovering them every time. If the same good solution shape appears repeatedly and predictably, it belongs here as reusable knowledge rather than accidental repetition.

---

## ENTRY FORMAT

[YYYY-MM-DD] — [Pattern Name]

Category
[Architecture / Coding / Testing / API / UI-UX / Security / Infra / Workflow / Product / Auth]

Problem It Solves
[What recurring problem does this pattern address?]

The Pattern
[Concise description of the approach — with code example if applicable]

When to Apply
[What signals indicate this pattern should be used?]

- [condition 1]
- [condition 2]
- [condition 3]

When NOT to Apply
[What situations look similar but require a different approach?]

- [condition 1]
- [condition 2]

Why It Works Here
[Why this pattern fits this project specifically — not just in general]

Tradeoffs and Limits
[What cost comes with it? When does it break down?]

- [tradeoff or limit 1]
- [tradeoff or limit 2]

Where It Is Used
[List of existing places this pattern is already applied]

Related Files / Areas

- [skill / workflow / context / ADR / code area]
- [related item 2]

Tags: #architecture #coding #auth #api #error-handling #validation

---

## QUALITY BAR FOR ENTRIES

A strong pattern entry:

- Has reuse value across more than one task or module
- Is validated in this project — not just a general best practice
- Explains why the pattern fits this project specifically
- Includes clear "when NOT to use" limits so it is not over-applied
- Reduces ambiguity, repeated mistakes, inconsistency, or implementation time

A weak pattern entry:

- Is too generic to guide actual work
- Describes taste or preference rather than an operational solution
- Records something seen only once with no evidence of recurrence
- Lacks limits — treating the pattern as universally applicable
- Becomes a random snippet dump rather than reusable knowledge

---

## USAGE RULES

1. Store patterns that have been validated in this project, not generic best practices imported from elsewhere.
2. Prefer patterns that reduce:
   - Ambiguity about the right approach
   - Repeated mistakes and inconsistency
   - Implementation time on recurring problems
3. Mark deprecated patterns clearly rather than deleting them — the history of why something was retired is itself useful.
4. Update patterns as the system evolves and better approaches emerge.
5. Most recent entries appear at the top.

---

## EXAMPLE ENTRY

2024-04-10 — Server Action Result Pattern

Category
Coding / Error Handling

Problem It Solves
Server Actions need a consistent way to return success or failure without throwing exceptions, which are hard for the client to handle gracefully and produce inconsistent error experiences.

The Pattern
Every Server Action returns a discriminated union:

```typescript
type ActionResult<T> =

| { success: true; data: T } |
| { success: false; error: string; code?: string }; |

```

Pattern in action:

```typescript
export async function createTask(
  input: unknown
): Promise<ActionResult<Task>> {
  const parsed = taskSchema.safeParse(input);
  if (!parsed.success) {
    return {
      success: false,
      error: 'Invalid input',
      code: 'VALIDATION_ERROR'
    };
  }

  const session = await auth();
  if (!session) {
    return {
      success: false,
      error: 'Not authenticated',
      code: 'AUTH_ERROR'
    };
  }

  try {
    const task = await insertTask(parsed.data);
    return { success: true, data: task };
  } catch (error) {
    logger.error('Failed to create task', { error });
    return {
      success: false,
      error: 'Failed to create task',
      code: 'INTERNAL_ERROR'
    };
  }
}
```

When to Apply

- Any Server Action called directly from the UI
- Any mutation that can fail in multiple distinct ways
- Any operation where the client needs to distinguish error types

When NOT to Apply

- API routes for external consumers — use HTTP status codes instead
- Webhook handlers — use standard HTTP responses
- Read-only data fetching that throws on error is acceptable

Why It Works Here
The project uses Server Actions as the primary mutation mechanism. A consistent result shape means all UI components handle errors the same way — no inconsistent try/catch patterns scattered across feature files.

Tradeoffs and Limits

- Adds a small wrapper layer to every action
- Requires discipline to not mix this pattern with raw throws
- Does not replace proper logging — errors should still be logged before returning a failure result

Where It Is Used

- features/tasks/actions/
- features/sprints/actions/
- features/projects/actions/

Related Files / Areas

- contexts/coding-standards.md
- skill-coding.md

Tags: #server-action #error-handling #coding #pattern

---

## ENTRIES

<!-- Append new entries below this line. Most recent at the top. -->
<!-- Append new entries below this line. Most recent at the top. -->
