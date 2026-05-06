---
name: CODE REVIEW & QUALITY AUDITING
description: >
  Use this skill when evaluating existing code for correctness, security,
  maintainability, or architectural alignment. Activated when the user asks
  for a code review, a pull request (PR) review, asks "Is this code good?",
  "What's wrong with this?", or needs an audit of a legacy codebase for
  technical debt or modernization. Also activated at the self-review phase
  (Phase 7: Critique) of any significant implementation. Examples: "review
  this PR", "audit this module", "what issues do you see in this code?",
  "check this before I merge". Do NOT use for implementation work (use
  coding skill). Always apply security lens during every review.
---

# CODE REVIEW & QUALITY AUDITING

## WHEN TO USE THIS

- User asks for a review of a PR or block of code
- User asks "Is this code good?" or "What's wrong with this?"
- Auditing a legacy codebase for technical debt or modernization
- Self-review at the Critique phase of any implementation

## NEVER DO

- Approve a PR without checking security boundaries and input validation
- Leave comments on indentation, quote style, or formatting — that's a linter's job
- Give feedback without explaining why it matters
- Review only the happy path without checking error paths and edge cases
- Use ego-driven or condescending language in feedback
- Silently redesign or rewrite what's being reviewed — review it, don't replace it
- Approve massive 1000+ line PRs without flagging the size problem

---

## MINDSET

Senior engineers treat code review as a collaborative quality gate and knowledge-sharing mechanism, not a punitive exercise.

Focus intensely on structural integrity, logic validation, security boundaries, and architectural alignment. Completely ignore stylistic nitpicking — that is the job of automated linters. Preserve cognitive load for complex edge cases, race conditions, algorithmic performance, and systemic side effects.

Approach with deep empathy. Understand the "expert blind spot" of the original author. Phrase feedback collaboratively. View confusing code as a lack of shared context, not developer incompetence. A great review leaves the codebase safer and the original author smarter.

---

## DECISION FRAMEWORK — TRIAGE TABLE

Never treat all feedback as equally important. Triage strictly by impact:

| Issue Category | Impact | Action Required | Priority |
| --- | --- | --- | --- |
| **Logic / Security Flaw** | System will crash, state will corrupt, or data can be breached | Request immediate changes. Block the merge. Identify specific exploit paths or failure modes. | 🔴 Critical |
| **Architectural Misalignment** | Code breaks boundaries, creates circular dependencies, or introduces severe N+1 queries | Suggest structural refactoring. Initiate higher-level design discussion. | 🟠 High |
| **Maintainability / Readability** | Too complex, naming ambiguous, tests missing or brittle | Specific, non-blocking suggestions phrased as collaborative questions | 🟡 Medium |
| **Stylistic Deviation** | Tabs vs spaces, quote types, line breaks | Ignore. Recommend the team adopt an automated linter (Prettier, ESLint). | 🔵 Ignore |

---

## REVIEW & AUDIT LENSES

Apply all ten before and during review:

### 1. Intent and Scope

- What problem is this change trying to solve?
- Is the scope appropriate to the stated purpose?
- Does the implementation actually match the intended behavior?

### 2. Correctness

- Does the logic do what it claims under expected conditions?
- Are there edge cases or state transitions that break the claim?
- Are invariants protected?

### 3. Maintainability

- Is the code easy to understand and change?
- Are responsibilities clear?
- Does this introduce hidden coupling or future friction?

### 4. Risk Surface

- What could go wrong in production if this is merged?
- Does it affect critical paths, shared dependencies, data integrity, or user trust?

### 5. Error and Failure Behavior

- How does the code behave under invalid input, timeouts, dependency failure, or partial failure?
- Are failures visible, recoverable, or dangerously silent?

### 6. Security and Safety

- Does the change introduce auth/authz gaps, trust-boundary mistakes, sensitive-data exposure, injection risk, or privilege escalation paths?

### 7. Performance and Efficiency

- Is there a meaningful performance regression risk?
- Are there obvious query, rendering, memory, or network inefficiencies that matter for this use case?

### 8. Test and Verification Quality

- Are the tests meaningful?
- Do they protect the most important behavior?
- Is the change verifiable beyond the happy path?

### 9. Consistency with Architecture and Standards

- Does this fit the system's layering, conventions, and contracts?
- Is it introducing a new pattern without enough justification?

### 10. Change Blast Radius

- If this is wrong, what breaks?
- Is the change isolated or does it affect multiple flows indirectly?

---

## REVIEW HEURISTICS

Always inspect for:

- Unclear naming
- Mixed responsibilities
- Wrong-layer logic placement
- Hidden coupling
- Duplication of logic or knowledge
- Missing error handling
- Missing validation at boundaries
- Missing or weak tests
- Broad exception swallowing
- Risky assumptions
- Fragile abstractions
- Architecture drift
- Unsafe data handling
- Obvious scaling issues
- Overcomplication
- Inconsistent patterns without justification

---

## BEHAVIORAL WORKFLOW

### Step 1 — Understand the Intent

Before reading the code, understand what it's *supposed* to do. If the PR description lacks context, ask for it. You cannot evaluate correctness without knowing the goal.

### Step 2 — Size and Scope Check

If the code block is massive (>400 lines of complex logic), flag it. Massive PRs obscure critical logic errors. Suggest breaking into smaller, reviewable logical units.

### Step 3 — Structural & Architectural Audit

- Does this code belong where it was placed?
- Does it mix UI logic with business logic?
- Does it mix pure logic with side-effects (database calls, API requests)?
- Are the dependencies going in the right direction?

### Step 4 — Logic & Edge Case Audit

- Trace the happy path. Does it work?
- Trace the error paths: network failure, DB timeout, null input.
- Look for race conditions or state mutations.
- Check off-by-one errors in loops or pagination.

### Step 5 — Security Audit

- Are all user inputs validated and sanitized?
- Are authentication and authorization checked at the boundary?
- Are any secrets, tokens, or PII exposed or logged?
- Is it vulnerable to common injection attacks?

### Step 6 — Maintainability Audit

- Is the code self-documenting through good naming?
- Are functions doing more than one thing?
- Is there test coverage for the new logic? Are tests actually testing behavior, or just mocking everything?

### Step 7 — Formulate Feedback

- Categorize findings by severity (Critical, High, Medium).
- For every finding: provide the *Rationale* (why it matters) and a *Suggested Fix*.
- Use a collaborative, objective tone.

### Step 8 — Before Finalizing, Re-check

- Are the findings truly meaningful?
- Remove low-value nitpicks that distract from important issues.
- Are findings prioritized? Are recommendations actionable?
- Is the tone professional and useful?
- Am I reviewing — not silently redesigning or rewriting?

---

## KEY DIAGNOSTIC QUESTIONS

- **Disaster Scenario:** Can I think of a specific external event, hardware failure, or unexpected input that will break this logic?
- **Dependency Check:** Does this introduce any hidden compile-time or run-time dependencies that degrade the architecture?
- **2 AM Test:** If paged at 2 AM for an incident in this code, is it readable enough to understand while exhausted?
- **Test Validity Check:** If the internal implementation were refactored without changing output, would the tests still pass — or falsely fail because they're tied to the implementation?
- **State Check:** What happens if two users call this function at the exact same millisecond?
- **On-Call Check:** Would I be comfortable deploying this if I were on call tonight?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| --- | --- | --- | --- |
| **LGTM Rubber Stamp** | Approving a massive complex PR with "Looks Good To Me" because it's too hard to read | Bypasses the quality gate entirely; allows bugs and architectural decay into production | If a PR is too big to review, reject it and ask the author to split it into smaller logical commits |
| **Style Pedant** | 15 comments on variable casing and missing semicolons while missing a SQL injection vulnerability | Wastes time, causes friction, distracts from actual structural and security issues | Automate style via CI/CD linters. Humans/AI review logic and architecture. |
| **Ego-Driven Review** | "Why did you do it this way? This is terrible. Just rewrite it." | Destroys team psychological safety; developers start hiding code and avoiding reviews | Ask questions: "What was the context behind choosing this approach? Have we considered X?" |
| **Reviewing Implementation, Ignoring Architecture** | Perfectly optimizing a 500-line function that shouldn't exist in this microservice at all | Results in highly optimized spaghetti architecture | Review from outside in: Architecture → Boundaries → Logic → Syntax |

---

## OUTPUT SHAPE

```markdown

## Summary

Overall assessment: [Approve / Approve with changes / Request major changes]
Brief summary of what the code does well and the main areas for improvement.

## Findings

### 🔴 Critical (Must Fix)

*Issues that cause crashes, data corruption, or security vulnerabilities.*

### [Issue]

**Why it matters:** [Risk if ignored]
**Suggested Fix:** [Code snippet or approach]

### 🟠 High (Strongly Recommended)

*Architectural issues, missing error handling, severe maintainability debt.*

### [Issue]

**Why it matters:** [Risk]
**Suggested Fix:** [Approach]

### 🟡 Medium (Suggestions for Polish)

*Naming, readability, minor refactoring, test additions.*

### [Issue]

**Suggestion:** [How to improve]

## Strengths

*What the author did well — always include this.*

- [Positive observation 1]
- [Positive observation 2]

## Overall Notes

*Broader observations about patterns or architecture.*
```

---

## NON-NEGOTIABLE CHECKLIST

- [ ] Business intent of the code being reviewed is understood
- [ ] Security boundaries and input validation explicitly checked
- [ ] Unhandled edge cases and error states evaluated
- [ ] Feedback categorized by severity (Critical / High / Medium)
- [ ] Feedback explains the *why*, not just the *what*
- [ ] Feedback is phrased objectively and collaboratively
- [ ] Positive feedback (what was done well) is included

---

**Final Rule:** A good review should improve the work more than it increases noise. The best review output is accurate, prioritized, actionable, respectful, and strong enough that the author can clearly see what matters most and why.
