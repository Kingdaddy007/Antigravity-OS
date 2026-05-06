# RUBRIC: CODE QUALITY

**Version:** Gold v1.0
**Layer:** 10 — Evaluation
**Tier:** 3 — Loaded on demand
**File:** rubrics/code-quality-rubric.md
**Purpose:** Self-assessment matrix for evaluating code quality before delivery. Used during Phase 7 (Critique) of the execution workflow
**Loaded When:** Phase 7 of any coding task. Self-review before delivery. Evaluating whether code meets production quality standards
**References:** skill-coding.md, coding-standards.md, quality-bar.md

***

## HOW TO USE THIS RUBRIC

After completing implementation, evaluate your output against each
dimension below. Score each dimension.

- If any dimension scores **Failing** — the code is not ready for delivery.
- If multiple dimensions scores **Needs Work** — consider whether the
  overall output meets the quality bar before delivering.

Use this rubric:

- Before finalizing implementation
- During pull request or peer review
- During refactor assessment
- When comparing acceptable versus strong implementation quality
- During benchmark comparison or coaching feedback

***

## WHAT THIS RUBRIC EVALUATES

This rubric evaluates code across these dimensions:

- Correctness and behavioral integrity
- Readability and clarity
- Maintainability and change safety
- Responsibility separation
- Scope discipline
- Architectural fit and convention compliance
- Error handling and defensive behavior
- Testability and verification support
- Simplicity
- Security awareness
- Performance appropriateness

This rubric is for judging whether implementation is not just
functional, but professionally responsible.

***

## EVALUATION MATRIX

### 1. CORRECTNESS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Solves the actual problem — not a surface interpretation. Handles happy path, error paths, and edge cases. All boundary conditions considered. Assumptions stated explicitly. Output shape and behavior match the real requirement. |
| **Acceptable** | Solves the stated problem correctly. Happy path and common error paths handled. Most edge cases considered. Minor gaps documented. |
| **Needs Work** | Solves the happy path but error handling is incomplete. Some edge cases missed. Logic depends on unstated assumptions. Assumptions not stated. |
| **Failing** | Logic errors present. Core functionality broken for some inputs. Error paths not handled. Output shape or behavior does not match the requirement. Would cause bugs in production. |

***

### 2. READABILITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | A developer unfamiliar with this code understands intent immediately. Names are precise and domain-appropriate. Structure reveals purpose. No comments needed for WHAT — only WHY for non-obvious decisions. Control flow is easy to scan. |
| **Acceptable** | Generally readable. Most names are clear. Structure is logical. Minor areas could be clearer but do not impede understanding. |
| **Needs Work** | Requires significant mental effort to understand. Vague or misleading names. Logic flow is hard to follow. Compressed or tricky logic. Too much hidden behavior. Needs comments to explain WHAT the code does. |
| **Failing** | Unreadable without the author's explanation. Clever tricks, deep nesting, unclear abbreviations. Another engineer would need to rewrite it to understand it. |

***

### 3. MAINTAINABILITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Can be modified by another engineer without assistance. Clear separation of concerns. Changes are localized — modifying one behavior does not require touching unrelated code. Abstraction level is appropriate. Dependencies are explicit. |
| **Acceptable** | Generally maintainable. Most responsibilities are clear. Changes might touch one or two adjacent areas but impact is predictable. Complexity is proportionate to the problem. |
| **Needs Work** | Responsibilities are mixed. Changes risk unintended side effects. Some implicit dependencies that are not obvious. Unnecessary abstraction added. Structural drift from the surrounding codebase. |
| **Failing** | Functions handling multiple unrelated concerns. Changes anywhere risk breaking something elsewhere. Implicit coupling throughout. Future maintainers will struggle with this code. |

***

### 4. RESPONSIBILITY SEPARATION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Concerns are well-separated. Each module, function, or class has a clear single job. Business logic is distinct from transport, persistence, formatting, and integration concerns. Mixed-layer logic is minimized. |
| **Acceptable** | Responsibilities are mostly clear. Minor blending of concerns that does not meaningfully harm the structure. |
| **Needs Work** | Business logic leaks into transport or UI layers. Database concerns leak upward unnecessarily. Unrelated responsibilities blended without justification. |
| **Failing** | Logic in the wrong layer entirely. No meaningful separation of concerns. Would require major restructuring to separate responsibilities. |

***

### 5. SCOPE DISCIPLINE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Solves the requested problem without unnecessary expansion. Unrelated changes kept under control. Solution is proportional to the requirement. Every line earns its place. |
| **Acceptable** | Mostly on-scope. Minor over-engineering that does not significantly harm readability or structure. |
| **Needs Work** | Hidden redesign inside a small task. Broad refactor with no justification. Overbuilt implementation for a narrow problem. Code solving imagined future problems. |
| **Failing** | Massively over-engineered. Complex abstractions for simple use cases. Speculative generalization that serves the developer's interest, not the product's need. |

***

### 6. ERROR HANDLING AND DEFENSIVE BEHAVIOR

| Score | Criteria |
| :--- | :--- |
| **Excellent** | All foreseeable failure paths handled. Errors are specific and actionable. Fails fast on invalid state. External dependency failures handled gracefully. No silent failures. User-facing errors are clear and helpful. |
| **Acceptable** | Major failure paths handled. Errors are reasonably specific. Most external failures handled. Minor edge-case failures may not have dedicated handling. |
| **Needs Work** | Happy-path-only implementation. Some catch-all error handling. Silent failures possible. Swallowed exceptions. Error messages are generic. Unsafe assumptions at boundaries. |
| **Failing** | Error handling absent or broken. Empty catch blocks. Errors swallowed silently. Application crashes on bad input. Stack traces exposed to users. |

***

### 7. TESTABILITY AND VERIFICATION SUPPORT

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Important behaviors easily testable without heroic setup. Pure logic separated from side effects. Dependencies injectable. Clear seams for meaningful verification. Tests written alongside code where expected. |
| **Acceptable** | Core behaviors testable. Some setup complexity for integration points. Tests present for main scenarios. Verification expectations met for the risk level. |
| **Needs Work** | Difficult to test in isolation. Business logic entangled with side effects. Tests missing for important behaviors. No clean seam for verification. |
| **Failing** | Untestable without mocking everything. No separation of concerns. No tests provided where expected. Would require major restructuring to add tests. |

***

### 8. ARCHITECTURAL FIT AND CONVENTION COMPLIANCE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Follows all project conventions. Matches surrounding codebase patterns. Logic is in the right layer. Boundaries and responsibilities are respected. Feels like the same developer wrote it as the rest of the codebase. |
| **Acceptable** | Follows most conventions. Minor deviations that do not cause confusion. Consistent within itself even if slightly different from the wider codebase. |
| **Needs Work** | Multiple convention violations. Inconsistent naming, file placement, or patterns. New patterns introduced without architectural fit or justification. |
| **Failing** | Ignores project conventions entirely. Different naming style, error handling pattern, file organization. Logic placed in the wrong layer. Creates confusion about how things are done. |

***

### 9. SECURITY AWARENESS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | All user input validated server-side. Auth and authz checked on every protected path. No sensitive data leaked in responses or logs. Trust boundaries, validation, and sensitive operations handled appropriately. |
| **Acceptable** | Input validation present. Auth checked. No obvious vulnerabilities. Minor gaps in defense-in-depth that do not create exploitable paths. |
| **Needs Work** | Some input validation missing. Auth present but authz incomplete. Potential data exposure in error messages. Client data trusted without validation. |
| **Failing** | Injection vulnerabilities possible. Auth bypass paths exist. Secrets hardcoded. Sensitive data in client bundle or logs. Missing permission checks. Would fail a security audit. |

***

### 10. PERFORMANCE APPROPRIATENESS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Implementation is free from obvious wasteful patterns. Performance complexity is proportional to actual need. No avoidable N+1, repeated work, or unnecessary round-trip issues. |
| **Acceptable** | Generally efficient. Minor inefficiencies that are not likely to matter at expected scale. |
| **Needs Work** | Visible avoidable inefficiencies. Repeated work that could be eliminated. Patterns that will degrade under realistic load. |
| **Failing** | Serious performance anti-patterns present. N+1 queries in loops. Synchronous blocking work that should be async. Would degrade meaningfully under expected usage. |

***

## SCORING SUMMARY

| Dimension | Score | Notes |
| :--- | :--- | :--- |
| Correctness |||
| Readability |||
| Maintainability |||
| Responsibility Separation |||
| Scope Discipline |||
| Error Handling |||
| Testability |||
| Architectural Fit / Convention |||
| Security Awareness |||
| Performance Appropriateness |||
***

## DELIVERY DECISION

| Result | Decision |
| :--- | :--- |
| All Excellent / Acceptable | ✅ Ready to deliver |
| 1–2 Needs Work on non-critical dimensions | ⚠️ Deliver with noted improvements |
| Any Failing | ❌ Fix before delivery |
| Security Failing | ❌ BLOCK — fix immediately regardless of other scores |

***

## MINIMUM PASS STANDARD

Code should not be treated as production-ready or merge-ready
if it is Failing or persistently Weak in any of these
high-priority areas:

- Correctness
- Maintainability
- Architectural fit
- Security awareness where relevant
- Error handling where relevant

Strong styling alone does not compensate for weakness in
these areas.

***

## COMMON FAILURE PATTERNS

### Style-Looks-Good-But-Logic-Is-Weak

The code is neat on the surface but contains correctness
or state-flow risk.

### Mixed-Responsibility Implementation

Transport, domain logic, persistence, and side effects
are tangled together.

### Cleverness Over Clarity

The code is dense, indirect, or over-abstracted in ways
that make future change harder.

### Verification-Hostile Structure

Important behavior is difficult to test or reason about
because the design is tightly coupled or under-bounded.

### Cosmetic Cleanup Mistaken for Quality

The code may be formatted nicely but still carries high
structural friction.

### Scope Creep Inside a Small Task

Hidden redesign or broad refactor disguised as a
targeted fix.

***

## FINAL QUESTIONS

Before closing this review, ask:

- Would another engineer trust this code enough to inherit it?
- Does this code solve the problem without introducing
  avoidable long-term cost?

- If this is merged, what is most likely to hurt us later?
- Is this code correct, clear, safe, and maintainable enough
  to build on?

***

## Good code is not merely code that runs

## Good code solves the problem clearly, safely, and in a form future engineers can trust
