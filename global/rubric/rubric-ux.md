# RUBRIC: UX QUALITY

**Version:** Gold v1.0
**Layer:** 10 — Evaluation
**Tier:** 3 — Loaded on demand
**File:** rubrics/ux-rubric.md
**Purpose:** Self-assessment matrix for evaluating user interface and experience quality before delivery.
**Loaded When:** Phase 7 of any UI/UX task. Evaluating whether a UI implementation meets quality standards.
**References:** skill-ui-ux.md, workflow-design-ui.md, design-system.md

***

## HOW TO USE THIS RUBRIC

After completing a UI or UX design, evaluate your work against
each dimension below. Score each dimension.

- If **Accessibility** scores **Failing** — fix before delivery.
  This is a quality requirement, not optional.

- If **State Coverage** scores **Needs Work** — implement missing
  states before delivery. Users will hit them.

- If **3 or more dimensions** score **Needs Work** — consider
  whether this meets the quality bar for your users.

Use this rubric:

- During UI/UX review before approving a flow or screen design
- Before accepting a redesign proposal
- During benchmark comparison of interface approaches
- During pre-implementation UX evaluation
- When checking consistency against design-system expectations
- When comparing usable versus strong interface quality

***

## WHAT THIS RUBRIC EVALUATES

This rubric evaluates UI/UX across:

- User goal fit and action clarity
- State coverage and completeness
- Accessibility and interaction quality
- Responsive design and context fit
- Interaction feedback
- Visual consistency and design-system alignment
- Error experience and recovery
- Cognitive load and information hierarchy
- Practicality and implementation readiness

This rubric is for judging whether an interface is truly
usable — not just visually acceptable or polished.

***

## EVALUATION MATRIX

### 1. USER GOAL CLARITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | User's goal is clearly served by the interface. The most important action is the most prominent element. User can accomplish their task without trial and error. Flow matches the user's mental model. Design is shaped around a real task rather than a feature list. |
| **Acceptable** | User can accomplish their goal with minimal friction. Primary action is visible. Flow is logical if not perfectly intuitive. Design addresses a real user problem even if not perfectly optimized. |
| **Needs Work** | User has to figure out how to accomplish their goal. Primary action is not obvious. Flow requires learning. Interface centered on system structure rather than user need. Competing CTAs reducing clarity. |
| **Failing** | User goal is not clearly served. Interface organized around technical concepts rather than user tasks. Users would need documentation to use this. Lots of functionality but no clear user task. |

***

### 2. STATE COVERAGE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | All states implemented and polished: loading with skeleton, empty for first use and filtered views, success, error at field and action and page level, partial data, permission denied, and destructive confirmation. No state produces a blank screen or raw error. Experience remains understandable outside the happy path. |
| **Acceptable** | Major states covered: loading, empty, success, error. Minor states such as partial data or specific permission scenarios may be basic but functional. User knows what is happening in all primary flows. |
| **Needs Work** | Happy path polished but other states are afterthoughts. Loading shows a generic spinner. Empty state says only "No data." Error shows a generic message. Some states missing entirely. |
| **Failing** | Only happy path implemented. Loading shows blank page. No empty state. Errors show raw messages or stack traces. Users hit broken states in normal usage. |

***

### 3. ACCESSIBILITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Full keyboard navigation. Visible focus indicators. Screen reader compatible. Color contrast meets WCAG AA — 4.5:1 for body text, 3:1 for large text. Form labels associated correctly. Error messages connected via aria. Reduced motion respected. Meaning not conveyed through color alone. Touch targets adequate. |
| **Acceptable** | Keyboard navigation works for primary flows. Focus indicators present. Basic screen reader support. Color contrast adequate. Form labels present. No click-only assumptions for primary tasks. |
| **Needs Work** | Some interactive elements not keyboard-accessible. Focus indicators inconsistent. Color-only indicators used without alternatives. Some form fields lack labels. Contrast weak in places. |
| **Failing** | Keyboard navigation broken. No focus indicators. Color-only status indicators. Form fields without labels. Not usable by users with disabilities. Controls unlabeled. |

***

### 4. RESPONSIVE DESIGN AND CONTEXT FIT

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Works correctly at all breakpoints — mobile, tablet, desktop. Layout adapts intelligently. Touch targets adequate on mobile at 44x44px minimum. No horizontal scrolling. Content hierarchy maintained across sizes. Degrades gracefully where screen or interaction constraints change. |
| **Acceptable** | Works at primary breakpoints. Minor layout issues at edge sizes. Generally functional on mobile. Core content accessible across devices. |
| **Needs Work** | Desktop-first with mobile as an afterthought. Some elements broken or unusable on mobile. Layout does not adapt well to smaller screens. |
| **Failing** | Not responsive. Broken on mobile. Horizontal scrolling required. Content hidden or inaccessible at smaller sizes. |

***

### 5. INTERACTION FEEDBACK

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Every action has feedback. Buttons show loading state during async operations. Mutations show success and failure clearly. Hover states on all interactive elements. Optimistic updates where appropriate. Destructive actions have confirmation. User never wonders if something happened. |
| **Acceptable** | Primary actions have feedback. Loading states present. Success and failure communicated. Most interactive elements have hover states. Minor gaps in secondary interactions. |
| **Needs Work** | Some actions lack feedback. User sometimes unsure if an action succeeded. Loading states inconsistent. Primary flow mostly works but secondary interactions feel dead. |
| **Failing** | No interaction feedback. User clicks and nothing visibly happens. No loading indicators. No success or failure communication. Interface feels broken. |

***

### 6. VISUAL CONSISTENCY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Uses design system components consistently. Spacing follows the scale. Typography matches the system. Colors match tokens. No one-off styling. Similar interactions behave similarly. Looks like it belongs in the product. Unnecessary novelty avoided. |
| **Acceptable** | Mostly consistent with design system. Minor deviations that do not jar visually. Similar interactions mostly behave similarly. Consistent within itself even if slightly different in places. |
| **Needs Work** | Mix of design system and custom styling. Inconsistent spacing or typography. Some elements look different from the rest of the product. One-off patterns introduced without justification. Visual or interaction drift visible. |
| **Failing** | Ignores design system entirely. Custom styling throughout. Looks like a different product. Inconsistent with existing pages. Unnecessary novelty throughout. |

***

### 7. ERROR EXPERIENCE AND RECOVERY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Errors are user-friendly, specific, and actionable. Never blames the user. Always provides a clear recovery path. Inline validation for forms. Toast or banner for action failures. Full-page error for route failures. No technical jargon. Destructive actions handled safely. Wording is calm and helpful. |
| **Acceptable** | Errors are reasonably clear and provide guidance. Users can understand what went wrong and what to do. Recovery is possible. Most destructive actions are protected. |
| **Needs Work** | Errors are generic — "Something went wrong." Limited recovery guidance. Some technical language exposed. Some irreversible actions without protection. User-blaming wording in places. |
| **Failing** | Raw error messages, stack traces, or error codes shown to users. No recovery path. User-blaming language. Errors that dead-end without an escape. Irreversible actions with no confirmation. |

***

### 8. COGNITIVE LOAD AND INFORMATION HIERARCHY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Information prioritized by importance. Primary action is obvious at each stage. Progressive disclosure for secondary content. User does not need to remember information across steps. Recognition over recall. Minimal learning required. Low-priority information kept from competing with the core task. |
| **Acceptable** | Reasonable information density. Most important elements are prominent. Hierarchy is clear even if not perfectly optimized. Some secondary content could be better organized. |
| **Needs Work** | Too much information on screen. Important and unimportant content compete equally. User has to scan everything to find what they need. Interface asks users to remember, compare, infer, or decode unnecessarily. |
| **Failing** | Overwhelming interface. Every feature visible simultaneously. No visual hierarchy. User paralyzed by options. Form fields require memorizing data from other screens. Multi-step reasoning required for simple tasks. |

***

### 9. PRACTICALITY AND IMPLEMENTATION READINESS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Recommendation is implementable and product-fit. Balances UX quality with system and delivery realities. Design is specific enough that implementation does not have to invent core behaviors. Dependencies and assumptions are visible. Open decisions and fixed decisions are distinguished. |
| **Acceptable** | Mostly implementable with reasonable effort. Key behaviors defined. Some follow-up clarification may be needed for edge cases but core intent is clear. |
| **Needs Work** | Design leaves important behaviors undefined. Implementation would need to guess or invent significant details. Dependencies not surfaced. Aspirational without clear path to build. |
| **Failing** | Not implementable without a major rethink. Core behaviors undefined. Design exists only as a visual concept with no specification. Another engineer could not build from this without starting over. |

***

## SCORING SUMMARY

| Dimension | Score | Notes |
| :--- | :--- | :--- |
| User Goal Clarity |||
| State Coverage |||
| Accessibility |||
| Responsive Design / Context Fit |||
| Interaction Feedback |||
| Visual Consistency |||
| Error Experience / Recovery |||
| Cognitive Load / Information Hierarchy |||
| Practicality / Implementation Readiness |||
***

## DELIVERY DECISION

| Result | Decision |
| :--- | :--- |
| All Excellent / Acceptable | ✅ Ready to deliver |
| State Coverage Needs Work | ⚠️ Implement missing states before delivery — users will hit them |
| Accessibility Failing | ❌ Fix accessibility before delivery — this is a quality requirement, not optional |
| Any 3+ Needs Work | ⚠️ Consider whether this meets the quality bar for your users |

***

## MINIMUM PASS STANDARD

A UI should not be considered strong if it is weak in any
of these high-priority areas:

- User goal fit — design shaped around real user tasks
- Primary action clarity — next step obvious at each stage
- State coverage — experience works outside the happy path
- Accessibility — usable by the full range of users
- Recovery handling — user can recover when things go wrong

Visual polish does not compensate for usability confusion.

***

## COMMON FAILURE PATTERNS

### Layout Before Task

The interface looks arranged but does not clearly support
the user's actual goal. Features displayed without task
context.

### Happy-Path Mockup Thinking

The design ignores empty, error, loading, or restricted
states. These states are not edge cases — users hit them
constantly.

### Novelty Over Consistency

The surface invents new patterns when proven patterns would
reduce cognitive load and match user expectations.

### Pretty But Under-Specified

The interface looks good visually but leaves important
behaviors and dependencies unclear. Implementation has
to invent the hard parts.

### Accessibility as Polish

The design is judged mainly by appearance while usability
fundamentals remain weak. Accessibility is a baseline,
not a finishing touch.

### Feature-Centric Organization

Interface organized around system capabilities rather than
user tasks. Users have to learn the system to accomplish
their goal.

***

## FINAL QUESTIONS

Before delivering this UI, ask:

- Could a first-time user understand what to do?
- What happens when the user fails, hesitates, or has no data?
- Is this actually easier to use, or just visually cleaner?
- Would a user with a disability be able to complete the primary task?
- Does this design reduce future confusion or create it?
- Is the next step obvious at every stage of the flow?

***

## A good interface makes the user's next step clear, safe, and low-friction — even when things go wrong
