# BENCHMARK: UI/UX (SKILL: UI/UX & DESIGN THINKING)

**Version:** Gold v1.0
**Layer:** 11 — Verification
**Loading Tier:** 3 — **LOADED ON DEMAND**

***

## PURPOSE

This file contains repeatable test scenarios for evaluating Anti-Gravity's
UI/UX design and implementation capability — user goal clarity, state
completeness, accessibility, interaction quality, and implementation readiness.

### Evaluate With

- [rubric-ux.md](file:///C:/Users/Oviks/.gemini/antigravity/rubric/rubric-ux.md)
- [rubric-communication.md](file:///C:/Users/Oviks/.gemini/antigravity/rubric/rubric-communication.md)

### Tests

- `skill-ui-ux.md`
- `workflow-design-ui.md`
- `design-system.md`

***

## WHAT THIS BENCHMARK TESTS (SKILL: UI/UX & DESIGN THINKING)

This benchmark evaluates whether Anti-Gravity can:

- Identify the real user goal before designing
- Structure flows around the task, not around features
- Design strong information hierarchy and action clarity
- Cover all states — loading, empty, error, success, restricted — not just the happy path
- Reduce cognitive load and abandonment risk
- Handle destructive actions safely
- Consider accessibility and responsiveness as first-class concerns
- Produce practical, implementation-ready UI recommendations

This benchmark should reveal whether Anti-Gravity thinks like a design-aware
builder or a surface-level "make it nicer" assistant.

***

## HOW TO USE THESE BENCHMARKS (SKILL: UI/UX & DESIGN THINKING)

1. Pick a scenario below.
2. Present it to Anti-Gravity as a real task — do not mention it is a benchmark.
3. Let Anti-Gravity process it using its full system — skills, contexts, and workflows active as appropriate.
4. Evaluate the output against the rubrics listed above.
5. Record the score in [benchmark-results.md](file:///C:/Users/Oviks/.gemini/antigravity/memory/benchmark-results.md).
6. Compare scores across runs and versions to track improvement.

***

## EVALUATION DIMENSIONS (SKILL: UI/UX & DESIGN THINKING)

Score benchmark outputs across these dimensions:

1. User goal clarity — was the real task identified before designing?
2. Flow clarity — is the next step obvious at each stage?
3. Information hierarchy — is the most important thing most prominent?
4. State coverage — loading, empty, error, success, restricted?
5. Error prevention and recovery — does the design reduce mistakes?
6. Cognitive load — is the interface scoped to what the user needs?
7. Accessibility awareness — keyboard, labels, contrast, semantics?
8. Responsiveness — does the design work at all target breakpoints?
9. Consistency — does the design fit the product's existing patterns?
10. Implementation readiness — can engineering build without guessing?

***

## SCENARIO 1 — New Page With Multiple States

### Prompt (Scenario 1)

Build the sprint board page. It should show a kanban-style board with columns
for each task status — todo, in progress, in review, done. Users can see task
cards in each column.

### What Excellent Output Looks Like (Scenario 1)

- Asks clarifying questions before designing — is drag and drop required now or Phase 2?
- Maps all states before building:
  - Loading — skeleton that matches board shape with column and card skeletons
  - Empty sprint with no tasks — "No tasks in this sprint. Add tasks from the backlog." with a clear action
  - Empty column — column header visible with an empty area, not hidden
  - Error — "Failed to load sprint board. [Retry]"
  - No active sprint — "No active sprint. [Start a sprint]"
  - Viewer permission — can see but cannot drag or modify
- Designs component hierarchy — board, column, card
- Uses design system components — card, badge, avatar, skeleton
- Responsive — columns stack vertically on mobile with clear priority ordering
- Accessibility — keyboard navigation between columns and cards
- Task card shows the right information at the right density — title, assignee, priority, story points

### Red Flags (Scenario 1)

- Builds only the happy path — data loaded, tasks present
- No loading state — blank page while fetching
- No empty state — blank columns with no guidance
- No mobile consideration
- No accessibility — no keyboard navigation or focus management
- Does not use design system components

***

## SCENARIO 2 — Form With Validation

### Prompt (Scenario 2)

Build the create task form. Fields: title (required), description (optional),
priority (dropdown), assignee (dropdown of project members), story points
(optional number), due date (optional date picker).

### What Excellent Output Looks Like (Scenario 2)

- Uses the project's form library with schema validation — per coding standards
- Field order follows design system convention — most important first
- All fields have visible labels, not placeholder-only labels
- Required fields marked clearly; optional fields marked as optional
- Validation with inline, field-specific error messages:
  - Title: required, maximum character limit — "Task title is required"
  - Story points: valid range, whole numbers only — "Must be between 0 and 100"
  - Description: maximum character count with counter shown near limit
- Submit button right-aligned and shows loading state during submission
- Cancel button adjacent to submit and visually de-emphasized
- Success: toast notification; form resets or modal closes
- Failure: toast error; form retains entered data so the user does not re-enter everything
- Schema shared between client and server validation
- Accessibility: labels associated correctly, errors announced via `aria-describedby`

### Red Flags (Scenario 2)

- No client-side validation — relies entirely on server errors
- Placeholder text used instead of visible labels
- No loading state on the submit button
- Form data lost on error — user must re-enter all fields
- No character limit enforcement or feedback
- Generic error message applied to all validation failures

***

## SCENARIO 3 — Destructive Action UX

### Prompt (Scenario 3)

Add a Delete Project button to the project settings page.

### What Excellent Output Looks Like (Scenario 3)

- Identifies this as a high-severity destructive action before designing
- Uses a destructive visual variant positioned away from primary actions in a clearly separated Danger Zone
- Click opens a confirmation modal with:
  - Clear impact statement — "This will permanently delete [project name] and all associated sprints, tasks, and comments"
  - Scope quantified — "[X] sprints, [Y] tasks, [Z] comments will be deleted"
  - Typed confirmation — "Type [project name] to confirm"
  - Delete button disabled until project name is correctly typed
  - Cancel as the visually dominant action with default focus on cancel
- During deletion, button shows loading state and modal stays open
- On success, redirects to project list with a confirmation message
- On failure, shows error in modal and allows retry without restarting
- Enforces authorization check — only project admins can see this action
- References the design system's destructive action patterns

### Red Flags (Scenario 3)

- Single-click delete with no confirmation
- "Are you sure?" confirmation without explicit impact
- Delete button as the first or most prominent action on the page
- No loading state during deletion
- No mention of who can access this action
- No visual separation from non-destructive settings

***

## SCENARIO 4 — Redesign a Confusing Onboarding Flow

### Prompt (Scenario 4)

Users frequently abandon onboarding during the account setup step. The current
flow asks for too much information up front and does not explain why each step
matters. Redesign the onboarding flow.

### What Excellent Output Looks Like (Scenario 4)

- Starts by identifying why abandonment is happening — too much friction too early, no visible reason to provide information
- Applies progressive disclosure — collect only what is needed now, defer the rest
- Sequences steps logically — must-have information first, optional configuration later
- Explains why each input is needed at the point of asking
- Adds progress indication — user knows how far they are and how much remains
- Handles interruption — if user stops midway, progress is saved and resumable
- Designs success moments — clear feedback when each step is complete
- Defines a success metric for the redesign

### Red Flags (Scenario 4)

- Generic "make it simpler" with no step logic
- No distinction between must-have and deferrable information
- No user psychology or friction analysis
- No progress or feedback design
- No interruption or recovery thinking

***

## SCENARIO 5 — Mobile Adaptation of a Data Table Flow

### Prompt (Scenario 5)

A table-heavy desktop flow works reasonably well but is painful on mobile.
Redesign the experience for small screens without losing core functionality.

### What Excellent Output Looks Like (Scenario 5)

- Identifies what information is essential at mobile scale versus what can be deprioritized or accessed on demand
- Proposes an alternate representation for dense table data — cards, expandable rows, or detail-on-tap, instead of shrinking desktop table
- Preserves critical actions via touch-appropriate interactions
- Eliminates hover-only interactions; all actions accessible via tap
- Uses touch targets at least 44x44px
- Considers column priority explicitly — if only three columns fit, identifies which three matter most
- Discusses responsive tradeoffs clearly — what is gained and what is simplified

### Red Flags (Scenario 5)

- "Make it responsive" with no specifics
- Shrinks the desktop layout onto small screens
- No action reprioritization
- No touch interaction thinking
- Information hidden without an accessible path to reach it

***

## SCENARIO 6 — Fix a Form With High Error Rate

### Prompt (Scenario 6)

A form has a high submission error rate. Users often enter data in the wrong
format, miss required fields, and abandon after seeing validation errors.
Redesign the form experience.

### What Excellent Output Looks Like (Scenario 6)

- Diagnoses likely causes — unclear required fields, confusing format requirements, validation shown only after full submission
- Shifts validation timing — shows inline errors on blur or typing, not only on submit
- Improves field guidance — examples, format hints, inline help text
- Distinguishes required from optional fields visually
- Makes error messages actionable — "Enter a date in MM/DD/YYYY format" not "Invalid date"
- Reduces effort — infers or normalizes format where possible
- Preserves entered data on error
- Considers recovery flow after each error

### Red Flags (Scenario 6)

- "Improve validation messages" with no specifics
- No field-level reasoning
- Validation still only shown on full submission
- No reduction in user effort or format ambiguity
- No distinction between prevention and correction

***

## SCORING GUIDE (SKILL: UI/UX & DESIGN THINKING)

For each scenario, evaluate using `rubric-ux.md` dimensions:

| Dimension | Weight for UI/UX |
| :--- | :--- |
| State Coverage | Critical — all states mapped and designed? |
| Accessibility | High — keyboard, screen reader, contrast, labels? |
| Interaction Feedback | High — loading, success, error states present? |
| User Goal Clarity | High — can the user accomplish their task? |
| Design System Compliance | Medium — uses established patterns and components? |
| Responsive Design | Medium — works at all target breakpoints? |
| Error Experience | Medium — errors are helpful, specific, and recoverable? |
| Cognitive Load | Medium — information appropriately prioritized and scoped? |

Record all scores in [benchmark-results.md](file:///C:/Users/Oviks/.gemini/antigravity/memory/benchmark-results.md).

***

## FINAL RULE (SKILL: UI/UX & DESIGN THINKING)

A strong UI/UX benchmark response makes it easier for the user to:

- Understand the interface on first encounter
- Know what to do next at every stage
- Recover clearly when something goes wrong
- Complete the intended task with less friction

It should make the user's next step clearer, easier, and safer — not just
visually cleaner.
