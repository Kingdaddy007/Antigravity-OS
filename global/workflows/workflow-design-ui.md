# WORKFLOW: DESIGN UI (FULL SOURCE)

**Version:** Gold v1.1 (Master Merge)
**Layer:** 8 — Execution Workflow
**Tier:** 2 — Loaded by task
**File:** workflows/workflow-design-ui-SOURCE.md
**Primary Mode:** Designer
**Secondary Modes:** Builder, Product Thinking, Architect, Performance, Reviewer, Security
**Purpose:** The systematic sequence for designing and implementing user interfaces — from user goal identification through component implementation with full state coverage and accessibility. Ensures UI work starts with the USER, not with the component.
**Loaded When:** Building frontend components, designing user flows, creating new pages or views, improving existing UI, improving usability, or designing interaction states.
**Inherits From:** execution-workflow.md (universal process)

---

## WHAT THIS WORKFLOW DOES

This workflow ensures UI work starts with the user, not with the component. It forces state coverage — loading, empty, error, success — accessibility compliance, and responsive behavior. These are the things that get skipped when developers jump straight to the happy-path UI.

Without this workflow, UI development produces components that work in the demo but break in production because empty states, error states, loading states, mobile views, and keyboard navigation were never considered.

---

## ACTIVATION

### Use When

- "Build this page / screen / view"
- "Create this component"
- "Design the user flow for [feature]"
- "Improve the UX of [feature]"
- "Make this responsive"
- "Fix the accessibility of [component]"
- "Design this form / onboarding / dashboard / navigation"
- "Make this more intuitive"
- Any task that produces user-facing interface elements

### Do NOT Use When

- Building API endpoints with no UI → use `workflow-build-feature.md`
- Reviewing existing UI code → use `workflow-review-code.md`
- Optimizing UI performance → use `workflow-optimize-performance.md`
- Planning overall system architecture → use `workflow-plan-architecture.md`
- Debugging a broken system → use `workflow-debug-issue.md`

If the task includes both design and implementation, complete design steps first, then transition to Builder Mode.

---

## REQUIRED FILES

### Skills — Always Load

| Priority | Skill | Why |
| :--- | :--- | :--- |
| Primary | `skill-ui-ux` | Design thinking, state coverage, accessibility |
| Primary | `skill-coding` | Component implementation quality |
| Secondary | `skill-product-thinking` | User goal and friction framing |

### Skills — Load When Relevant

| Condition | Skill |
| :--- | :--- |
| Building a new module or page structure | `skill-architecture` |
| UI requires new API endpoints | `skill-api-design` |
| UI handles auth flows or sensitive data | `skill-security` |
| Responsiveness or rendering cost matters | `skill-performance` |

### Contexts — Always Load

- `design-system.md`
- `stack-context.md`
- `coding-standards.md`
- `architecture-context.md`
- `project-context.md`
- `business-priorities.md`
- `domain-rules.md`

### Contexts — Load When Relevant

| Condition | Context |
| :--- | :--- |
| UI enforces business rules | `domain-rules.md` |
| Auth or permission UI | `security-baselines.md` |
| Consuming API data | `api-conventions.md` |

---

## REQUIRED INPUTS

At minimum, Anti-Gravity should have or establish before proceeding:

- the user goal
- the relevant screen, flow, or problem area
- who the user is
- what constraints matter
- whether the task is new design, redesign, UX improvement, component design, or UI critique

### If inputs are incomplete

Clarify the user goal before designing. Do NOT start designing components against an unclear user task.

---

### MANDATORY STOP-AND-VERIFY GATE
> **[CONTEXT AMNESIA FAILSAFE]**
> Do NOT proceed to Step 1 until you have verified in your `<thought_process>` that all required context files and skill files have been read using tool calls. You must state: "I have read X, Y, Z files and I am ready to begin."

## EXECUTION SEQUENCE

---

### STEP 1 — UNDERSTAND THE USER GOAL

**Mode:** Designer
**Goal:** Define what the user needs to accomplish — not what the screen looks like.

**Gate:** Do NOT start designing components until the user goal and flow are clear.

#### Actions (Step 1)

1. **Identify the user:**
   - Which user type is this for? Check `project-context.md` user types
   - What is their skill level and tolerance for complexity?
   - What device and context are they in — desktop focus session, mobile quick check, or something else?

1. **Identify the job:**
   - What is the user trying to accomplish?
   - Frame as Job-to-be-Done:
     > "When [situation], the user wants to [motivation] so that [outcome]"
   - What does the user have BEFORE this interaction?
   - What do they have AFTER?
   - Distinguish the feature request from the actual user need

1. **Identify the flow:**
   - What triggered the user to arrive at this screen?
   - What are the possible exits: success, cancel, error, navigation?
   - Is this a single interaction or a multi-step process?
   - Where does friction or confusion likely occur?
   - Where are the likely drop-off points?

1. **Identify constraints:**
   - What data is available to show?
   - What actions can this user take? Check role permissions
   - What are the responsive requirements? Check `design-system.md`
   - What are the accessibility requirements?
   - What platform or device assumptions matter?
   - Does this fit an existing screen pattern or is it more open?

#### Output (Step 1)

```text
User: [who]
Job: When [situation], they want to [motivation] so that [outcome]
Arrives from: [trigger]
Leaves via: [success path] or [alternative paths]
Constraints: [list]
Friction points: [where confusion likely occurs]
```

---

### STEP 2 — MAP ALL STATES

**Mode:** Designer
**Goal:** Identify every possible state the UI must handle BEFORE building anything.

**This is the most commonly skipped step and the number one cause of UI bugs in production.**

**Gate:** Do NOT start building until every state has a defined design approach.

#### State Map (Step 2)

For every view, screen, or component, define all of these:

| State | Questions to Answer | Design Decision |
| :--- | :--- | :--- |
| **Loading — initial** | What does the user see while data fetches for the first time? | Skeleton placeholder matching content shape, or full-page spinner? Check `design-system.md` loading patterns |
| **Loading — refresh** | What during background data refresh? | Show stale data with subtle indicator, or skeleton again? |
| **Empty — first use** | No data yet because user has not created any? | Illustration + friendly message + CTA to create first item |
| **Empty — filtered** | Filters or search return no results? | Lighter message + suggestion to adjust filters |
| **Success** | Normal, data-present state | The primary design |
| **Partial** | Some data present but incomplete? | Graceful fallbacks: initials for avatar, placeholder for missing description |
| **Error — field** | Form validation error? | Inline error below field, red border, aria-describedby |
| **Error — action** | Failed mutation: save failed, delete failed? | Toast notification with retry option |
| **Error — page** | Full page data fetch failure? | Error card with retry button replacing content area |
| **Permission denied** | User lacks access? | Message with redirect or limited view |
| **Destructive confirmation** | Before irreversible actions? | Modal with typed confirmation for high-severity, simple confirm for low |
| **Optimistic update** | Immediate UI change before server confirms? | Immediate visual change, revert on failure |
| **Disabled or pending** | Awaiting condition or permission? | Disabled state with clear visual treatment |

#### Output (Step 2)

A state map table listing every state with the design decision for each.

---

### STEP 3 — MAP THE FLOW AND INFORMATION PRIORITIES

**Mode:** Designer
**Goal:** Understand the full journey and clarify what each screen or state must communicate before touching component or layout decisions.

#### Flow Mapping Actions (Step 3)

- Outline the flow from start to finish
- Identify entry point, main steps, user decisions, system responses, and completion point
- Identify what the user must know at each step
- Identify what decision should be obvious next
- Identify where confusion could happen

#### Information Priority Actions (Step 3)

- Identify what must be visible immediately
- Identify the primary action — there should be one
- Identify secondary actions
- Define what information can be deferred or hidden
- Determine whether the screen is action-heavy, information-heavy, confirmation-heavy, or error-recovery-heavy

#### Output (Step 3)

```text
Flow outline: [steps and transitions]
Friction map: [where confusion likely occurs]
Information hierarchy: [what must be immediate vs deferred]
Action hierarchy: [primary, secondary, tertiary]
```

---

### STEP 4 — DESIGN THE LAYOUT AND COMPONENTS

**Mode:** Designer
**Goal:** Plan the component structure, visual hierarchy, and responsive behavior before writing any code.

#### Visual Hierarchy (Step 4)

- What is the PRIMARY action on this screen? Make it most prominent
- What is the SECONDARY information? Supporting, less prominent
- What is TERTIARY content? Metadata, least important
- Apply `design-system.md` typography scale: largest equals most important

#### Component Selection (Step 4)

- What components from `design-system.md` will be used?
- Are any new components needed? Prefer existing over new
- What variants and sizes are appropriate?
- Avoid inventing new patterns unless existing ones are insufficient

#### Layout Structure (Step 4)

- What is the page layout: single column, sidebar plus content, grid?
- How does it change at each responsive breakpoint?
- Reference `design-system.md` responsive breakpoints

#### Interaction Design (Step 4)

- What are the clickable and interactive elements?
- What feedback does each interaction provide: hover, active, loading?
- What keyboard shortcuts apply if any?
- Is tab order logical?

#### Information Density (Step 4)

- Is there too much on the screen creating cognitive load?
- Can anything be hidden behind progressive disclosure: accordion, show more, tabs?
- Is the most important information visible without scrolling?

#### Output (Step 4)

Component structure description covering which components, how they are arranged, responsive behavior, and interaction patterns.

#### Gate (Step 4)

If the primary action is not obvious, or hierarchy is weak, redesign before building. Visual neatness does not compensate for weak UX structure.

---

### STEP 5 — IMPLEMENT

**Mode:** Builder
**Goal:** Build the UI with full state coverage and accessibility.

Load `skill-coding` and follow its behavioral workflow.

#### 5a — Component Structure (Step 5)

1. Create component files following `architecture-context.md` placement rules
1. Define component props with TypeScript
1. Decide Server Component versus Client Component using `coding-standards.md` decision table
1. Set up data fetching via React Query hook or Server Component

#### 5b — Happy Path First (Step 5)

1. Build the success state — the primary, data-present view
1. Use design system components from `design-system.md`
1. Apply Tailwind classes following spacing, typography, and color tokens
1. Ensure correct responsive behavior at each breakpoint

#### 5c — All Other States — Do NOT Skip (Step 5)

1. **Loading state:** Implement skeleton or spinner per `design-system.md` patterns
1. **Empty — first use:** Implement with appropriate messaging and CTA
1. **Empty — filtered:** Implement with filter adjustment suggestion
1. **Error — action:** Implement toast or inline with retry
1. **Error — page:** Implement error card with retry button
1. **Partial state:** Implement graceful fallbacks for missing data
1. **Permission state:** Implement role-based visibility if applicable

#### 5d — Interaction States (Step 5)

1. Hover, focus, active states on all interactive elements
1. Loading and disabled states on buttons during async operations
1. Destructive action confirmation per `design-system.md` patterns
1. Optimistic updates where appropriate — revert on failure

#### 5e — Accessibility — Non-Negotiable (Step 5)

1. All interactive elements keyboard-accessible
1. Focus indicators visible — check `design-system.md` focus styles
1. All images have alt text — decorative images use `alt=""`
1. Form fields have associated labels — visible or screen-reader-only
1. Error messages connected via `aria-describedby`
1. Dynamic content changes announced via `aria-live`
1. Modal focus trap and Escape to close
1. Color contrast ratios met — 4.5:1 body text, 3:1 large text
1. `prefers-reduced-motion` respected

#### 5f — Responsive Behavior (Step 5)

1. Test at each breakpoint from `design-system.md`
1. Mobile touch targets minimum 44 by 44 pixels
1. Content reflows appropriately — no horizontal scrolling on mobile
1. Navigation adapts appropriately at small breakpoints

---

### STEP 6 — VERIFY

**Mode:** Reviewer
**Goal:** Confirm every state works correctly, responsively, and accessibly.

#### State Coverage Verification (Step 6)

- [ ] Loading state — initial — displays correctly
- [ ] Loading state — refresh — displays correctly
- [ ] Empty state — first use — displays correctly with CTA
- [ ] Empty state — filtered — displays correctly with suggestion
- [ ] Success state — displays correctly with real-looking data
- [ ] Partial state — handles missing fields gracefully
- [ ] Error state — field validation — displays correctly
- [ ] Error state — action failure — displays correctly
- [ ] Error state — page-level — displays correctly with retry
- [ ] Permission denied state — displays correctly

#### Responsive Verification (Step 6)

- [ ] Desktop layout correct
- [ ] Tablet layout correct
- [ ] Mobile layout correct
- [ ] No horizontal scrolling at any breakpoint
- [ ] Touch targets adequate on mobile

#### Accessibility Verification (Step 6)

- [ ] Full keyboard navigation works — Tab, Shift+Tab, Enter, Escape
- [ ] Focus indicators visible on all interactive elements
- [ ] Screen reader announces content correctly
- [ ] Color contrast passes — verified in browser DevTools
- [ ] Form labels associated with inputs
- [ ] Error messages connected to fields via aria-describedby
- [ ] Modal focus trap and Escape behavior correct

#### Interaction Verification (Step 6)

- [ ] Hover states work on all interactive elements
- [ ] Loading states show during async operations
- [ ] Destructive confirmations fire before destructive actions
- [ ] Optimistic updates show and revert correctly on failure
- [ ] No state results in a blank screen or raw error output

#### UX Quality Check (Step 6)

- Is the user goal obvious?
- Is the next action obvious?
- Is this too crowded?
- Are error and recovery paths clear?
- Could a first-time user succeed without explanation?
- Is visual neatness hiding real UX weakness?

---

### STEP 7 — CRITIQUE

**Mode:** Reviewer
**Goal:** Challenge whether the design is truly good, not just neat.

#### Ask (Step 7)

- Is this feature-first instead of user-goal-first?
- Is the hierarchy weak?
- Are states underdesigned?
- Is visual neatness hiding real UX weakness?
- Is the flow too complicated?
- Am I optimizing for visual tidiness or user success?
- Is anything hidden that users should not have to hunt for?
- Is there too much competing for attention?
- Are we over-designing without regard for implementation reality?

#### Output (Step 7)

Final UX quality check, caveats, and refinement suggestions if needed.

---

### STEP 8 — DELIVER

**Mode:** Communicator
**Goal:** Present the UI work clearly with context, rationale, and verification guidance.

#### Delivery Structure (Step 8)

```markdown
## What Was Built
[1-2 sentence summary of the UI feature]

## User Goal
[Job-to-be-Done statement]

## Flow Structure
[Sequence of steps, entry, exits, friction points addressed]

## States Implemented
- Loading: [approach]
- Empty (first use): [approach]
- Empty (filtered): [approach]
- Success: [approach]
- Partial: [approach]
- Error (field): [approach]
- Error (action): [approach]
- Error (page): [approach]
- Permission denied: [approach if applicable]

## Components Used
[List of design system components used]

## Responsive Behavior
[How the layout changes at each breakpoint]

## Accessibility
[Summary of accessibility measures implemented]

## Key Decisions
[Non-obvious design or implementation decisions and rationale]

## Tradeoffs and Constraints
[Where simplicity competed with flexibility, density with readability]

## What to Test
[How to manually verify each state]

## Next Steps
[Deferred scope, Phase 2 items, follow-up work]
```

---

## CHECKPOINTS AND QUALITY GATES

| Gate | Condition | Action |
| :--- | :--- | :--- |
| Gate 1 — User goal unclear | Cannot state what the user is trying to accomplish | Clarify before designing anything |
| Gate 2 — States not mapped | Any state left undefined before building | Complete state map before coding |
| Gate 3 — Hierarchy weak | Primary action not obvious | Redesign before building |
| Gate 4 — Design system ignored | New patterns invented where existing ones exist | Align with design system before continuing |
| Gate 5 — Accessibility skipped | Any accessibility checklist item unaddressed | Accessibility is non-negotiable — address before delivery |
| Gate 6 — Responsive untested | Layout not verified at all breakpoints | Test at all breakpoints before marking complete |

---

## QUALITY GATE CHECKLIST

Before marking UI work complete:

- [ ] User goal clearly defined before design began
- [ ] Job-to-be-Done statement written
- [ ] Flow mapped with entry, exits, and friction points identified
- [ ] ALL states mapped and designed — loading, empty, partial, success, error, permission, destructive
- [ ] Information and action hierarchy defined
- [ ] Design system components used consistently
- [ ] No new patterns invented where existing ones serve the need
- [ ] Happy path implemented correctly
- [ ] All non-happy states implemented — do not skip
- [ ] Interaction states complete — hover, focus, active, loading, disabled
- [ ] Responsive behavior verified at all breakpoints
- [ ] Touch targets adequate on mobile
- [ ] Accessibility requirements met — keyboard, screen reader, contrast, labels, aria attributes
- [ ] Form patterns follow `design-system.md` conventions
- [ ] Destructive actions have appropriate confirmation
- [ ] Error messages are user-friendly and actionable
- [ ] No state results in a blank screen or raw error
- [ ] Delivery summary written with states, decisions, and test steps

---

## WORKFLOW ANTI-PATTERNS

| Anti-Pattern | Why It Is Harmful | How This Workflow Prevents It |
| :--- | :--- | :--- |
| Component-First Design | Interface gets built for what is easy to build, not what helps the user succeed | Define the user goal and job before touching any component or layout decision |
| Happy-Path-Only UI | Loading, empty, and error states exist in production every day | Map all states at Step 2 before writing code |
| Visual Neatness Over UX Clarity | Users fail to accomplish their goal even though UI looks polished | Prioritize user task completion over visual tidiness |
| Ignoring Accessibility | A meaningful portion of users cannot use product effectively | Treat accessibility as non-negotiable at Step 5e |
| Feature-Centric Design | Cognitive load increases and most important action gets lost | Design around the user's next meaningful action |

---

## FAILURE MODES AND ESCALATION PATHS

| Failure Mode | What It Looks Like | Escalation |
| :--- | :--- | :--- |
| Missing API | Cannot build the UI without a contract | Switch to `workflow-design-api.md` first |
| Architecture Gap | Component placement or data flow unclear | Load `skill-architecture.md`, resolve before building |
| Auth Boundary | Access rules affect what is shown | Load `skill-security.md` and `security-baselines.md` |
| Design Gap | No existing component serves the need | Document gap, propose new pattern with justification |
| Product Mismatch | Confusion caused by unclear product decisions | Switch to product thinking before designing |

---

## FINAL RULE

Design the interface around the user's next meaningful action — not around everything the system could possibly show, and not around what is easiest to build.

---

## VERSION HISTORY

| Version | Date | Changes |
| :--- | :--- | :--- |
| Gold v1.1 | Initial | Established the systematic sequence for designing and implementing UI |
