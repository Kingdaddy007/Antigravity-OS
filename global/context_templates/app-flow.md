---
status: template
scope: project
project_id: null
updated_at: null
owner: null
confidence: unset
---

# APP FLOW

**Version:** Gold v1.0

**Type:** Context File

**Layer:** Context — Ground Truth

**Tier:** 2 — Loaded by task

**File:** contexts/app-flow.md

**Loaded When:** Feature development, UI implementation, architecture design, debugging user journeys, onboarding design, or any task where understanding how users move through the product matters. Created during `workflow-project-inception` Phase 2A.

**Purpose:** Maps how every user type moves through this product — from first touch to completed job. Anti-Gravity uses this to understand the connected journey, not just isolated screens. Without this file, the AI builds disconnected features that technically work but do not flow together.

**Maintenance:** Update whenever a new flow is added, an existing flow changes, or user feedback reveals that users are not following the expected path. A stale app flow causes Anti-Gravity to build transitions and navigation for journeys that no longer exist.

---

## HOW ANTI-GRAVITY USES THIS FILE

This file is the journey map. It tells Anti-Gravity not just WHAT screens exist, but HOW users arrive at them, WHAT they do there, and WHERE they go next.

**When loaded**, Anti-Gravity will:

- Understand the full user journey before building any single screen — no screen is designed in isolation
- Ensure every new feature connects correctly to the screens before and after it in the flow
- Identify missing transitions, dead ends, or disconnected screens before they become bugs
- Build navigation, routing, and state management that matches how users actually move through the product
- Validate that error states, edge cases, and permission boundaries are handled at every transition point
- Use the flow to inform data requirements — what data must be available at each step, and where it comes from

**When missing or incomplete**, Anti-Gravity will:

- Build features as isolated screens without understanding how users reach them or leave them
- Produce navigation and routing that feels disconnected or requires the user to figure out the next step
- Miss critical transition states (e.g., what happens between "user submits form" and "user sees confirmation")
- Create screens with data dependencies that cannot be satisfied because the previous step does not provide the required data
- Generate UI that works in isolation during development but breaks when assembled into a real user journey

**When stale**, Anti-Gravity will:

- Build transitions to screens that have been removed or restructured
- Miss new entry points or shortcuts that have been added
- Assume users follow paths that no longer represent actual usage
- Produce navigation structures that conflict with the current product reality

**Conflict rule:** If this file describes a flow that conflicts with `project-context.md` (critical flows section) or `architecture-context.md` (routing structure), flag the conflict explicitly. Both files may need updating.

**Authoritativeness rule:** This file defines the intended user journey. If Anti-Gravity's general product training suggests a different flow pattern (e.g., "most apps do onboarding this way"), this file wins. Do not override the documented flow for convention unless the file is explicitly updated.

---

## APP FLOW DESIGN PRINCIPLES

These principles guide how flows are defined and maintained in this file.

### Principle 1 — Every screen has a reason to exist

**Rule:** A screen should not appear in a flow unless it serves a clear purpose in the user's journey toward completing their job.

**Meaning:** If a screen exists only because "we needed something there" or "other apps have this step," it is a candidate for removal or merging. Every screen should either collect input, display necessary information, confirm an action, or resolve an error.

### Principle 2 — Flows are defined by user intent, not by implementation

**Rule:** Flows are written from the user's perspective — what they are trying to accomplish — not from the developer's perspective of how the system processes the request.

**Meaning:** "User reviews order summary and confirms payment" is a flow step. "System calls the Stripe API and writes to the payments table" is an implementation detail. Implementation belongs in `architecture-context.md`. This file describes what the human experiences.

### Principle 3 — Every decision point has defined paths

**Rule:** When a user can take more than one action at a step, ALL possible paths must be documented — not just the happy path.

**Meaning:** If a user can approve OR reject, both paths must be mapped. If a user can skip a step, that skip must be shown. Unmapped decision points become bugs — the developer will guess, and they will guess wrong.

### Principle 4 — Entry and exit points must be explicit

**Rule:** Every flow must define where the user comes from (entry points) and where they go when finished (exit points).

**Meaning:** A flow that starts with "User is on the dashboard" without explaining how they got there creates assumptions. A flow that ends with "User sees success message" without explaining what happens next creates dead ends.

### Principle 5 — Transitions are as important as screens

**Rule:** The space between screens — loading states, redirects, confirmation dialogs, error recoveries — must be documented as steps in the flow, not assumed.

**Meaning:** "User submits → User sees dashboard" is incomplete. "User submits → System processes (loading state) → Success: redirect to dashboard / Error: show inline error with retry option" is complete.

---

## FLOW NOTATION GUIDE

Use this notation consistently when documenting flows in this file.

### Step Format

Each step in a flow should follow this format:

```text
[Step Number]. [Screen/State Name]

   - **What the user sees:** [describe the screen or state]
   - **What the user does:** [the primary action available]
   - **What happens next:** [where they go on success]
   - **On error:** [what happens if something fails]
   - **Alternative paths:** [other actions available, if any]

```

### Flow Symbols

When writing flows as compact sequences (useful for overviews), use:

- `→` for normal forward progression (user completes step and moves on)
- `↓` for a decision point that branches
- `⟲` for a loop back (user returns to a previous step, e.g., retry)
- `✕` for a terminal/dead-end (user exits the product or abandons the flow)
- `⊕` for a merge point (multiple paths converge into one step)
- `[Condition]` in brackets for conditional branching

### Example Compact Flow

```text
Landing Page → Sign Up Form → Email Verification → [Verified?]
  ↓ Yes → Onboarding Wizard → Dashboard
  ↓ No → Resend Email Screen ⟲ Email Verification
```

---

## USER TYPES AND THEIR PRIMARY JOURNEYS

<!-- WHY THIS MATTERS: Different user types take different paths through the
     same product. A buyer and a seller see different screens, take different
     actions, and have different definitions of "done." Anti-Gravity needs
     to know which flows belong to which user type to avoid building features
     that serve no actual user journey. -->

<!-- For each user type, list their primary journey through the product.
     This is the "golden path" — the most common, most important sequence
     of steps they follow when using the product for its intended purpose. -->

### User Type 1: [Name]

**Role:** [What this user does in the product]
**Primary job:** [What they are trying to accomplish]
**Entry point:** [How they first arrive — direct URL, referral, marketing page, app store, etc.]

#### Primary Journey (User Type 1)

<!-- Document the step-by-step journey this user takes to complete their
     primary job. Use the Step Format above. Be specific about every screen
     they see and every action they take. -->

1. [Step 1]
   - **What the user sees:** [Fill in]
   - **What the user does:** [Fill in]
   - **What happens next:** [Fill in]

2. [Step 2]
   - **What the user sees:** [Fill in]
   - **What the user does:** [Fill in]
   - **What happens next:** [Fill in]

3. [Step 3]
   - **What the user sees:** [Fill in]
   - **What the user does:** [Fill in]
   - **What happens next:** [Fill in]
   - **On error:** [Fill in]

<!-- Add as many steps as needed to complete the full journey. -->

#### Compact Flow

```text
[Write the compact flow using the notation guide above]
```

---

### User Type 2: [Name]

**Role:** [Fill in]
**Primary job:** [Fill in]
**Entry point:** [Fill in]

#### Primary Journey (User Type 2)

1. [Step 1]
   - **What the user sees:** [Fill in]
   - **What the user does:** [Fill in]
   - **What happens next:** [Fill in]

2. [Step 2]
   - **What the user sees:** [Fill in]
   - **What the user does:** [Fill in]
   - **What happens next:** [Fill in]

<!-- Continue for all steps. -->

#### Compact Flow

```text
[Write the compact flow using the notation guide above]
```

---

## SECONDARY FLOWS

<!-- WHY THIS MATTERS: Beyond the primary journey, users perform secondary
     tasks that are less frequent but still important to the product's value.
     These flows are where bugs often hide — because they are tested less
     frequently during development but used regularly in production. -->

<!-- Document each secondary flow in the same format as primary flows.
     Common secondary flows include: profile management, settings changes,
     notification handling, search/filter workflows, admin actions, etc. -->

### [Secondary Flow Name]

**User type:** [Who performs this]
**Trigger:** [What causes the user to enter this flow]
**Frequency:** [How often — daily, weekly, occasionally, one-time]

#### Steps (Secondary Flow 1)

1. [Step 1]
   - **What the user sees:** [Fill in]
   - **What the user does:** [Fill in]
   - **What happens next:** [Fill in]

<!-- Continue for all steps. -->

---

### [Secondary Flow Name 2]

**User type:** [Fill in]
**Trigger:** [Fill in]
**Frequency:** [Fill in]

#### Steps (Secondary Flow 2)

1. [Fill in]

---

## AUTHENTICATION AND ONBOARDING FLOW

<!-- WHY THIS MATTERS: Authentication and onboarding are the front door of
     the product. If this flow is broken, confusing, or incomplete, users
     never reach the core value. Anti-Gravity treats this flow as high-
     sensitivity — changes to auth/onboarding flows require elevated rigor
     and explicit error-state coverage. -->

### Registration

<!-- Map every step from "user decides to sign up" through "user is fully
     set up and ready to use the product." Include email verification,
     profile completion, and any required onboarding. -->

1. [Fill in — first screen the user sees when they start registration]
2. [Fill in — what information is collected]
3. [Fill in — verification step if applicable]
4. [Fill in — onboarding/setup if applicable]
5. [Fill in — first screen after onboarding is complete]

### Login

<!-- Map the login flow including password recovery, MFA if applicable,
     and where the user lands after successful login. -->

1. [Fill in]
2. [Fill in]
3. [Fill in — where does the user land after login?]

### Password Recovery

1. [Fill in]
2. [Fill in]
3. [Fill in]

---

## ERROR AND RECOVERY FLOWS

<!-- WHY THIS MATTERS: How a product handles failure defines its quality more
     than how it handles success. Anti-Gravity uses this section to ensure
     that error states are not afterthoughts but designed, documented
     transitions. Without this, developers implement generic "something went
     wrong" messages instead of actionable recovery paths. -->

### Global Error Patterns

<!-- Define how the product handles common failure scenarios across all flows.
     These patterns should be consistent everywhere unless a specific flow
     documents an override. -->

| Error Type | What the User Sees | Recovery Action | Where They Go |
| --- | --- | --- | --- |
| Network failure | [Fill in] | [Fill in] | [Fill in] |
| Authentication expired | [Fill in] | [Fill in] | [Fill in] |
| Permission denied | [Fill in] | [Fill in] | [Fill in] |
| Validation error | [Fill in] | [Fill in] | [Fill in] |
| Server error (500) | [Fill in] | [Fill in] | [Fill in] |
| Not found (404) | [Fill in] | [Fill in] | [Fill in] |
| Rate limited | [Fill in] | [Fill in] | [Fill in] |

### Flow-Specific Error Handling

<!-- Document any flow-specific error patterns that override the global
     patterns above. For example, a payment flow might have a different
     error recovery pattern than a profile update flow. -->

| Flow | Error Scenario | Specific Handling |
| --- | --- | --- |
| [Flow name] | [What can fail] | [How it is handled differently] |
| [Flow name] | [What can fail] | [How it is handled differently] |

---

## NAVIGATION STRUCTURE

<!-- WHY THIS MATTERS: Anti-Gravity uses this to understand how the product
     is organized at the highest level. This prevents building features that
     are unreachable from the product's actual navigation, or placing screens
     in the wrong section of the product. -->

### Global Navigation

<!-- Describe the persistent navigation elements — what is always visible
     and accessible from any screen in the product. -->

| Navigation Item | Destination | Visible To |
| --- | --- | --- |
| [Item 1] | [Where it goes] | [All users / specific roles] |
| [Item 2] | [Where it goes] | [All users / specific roles] |
| [Item 3] | [Where it goes] | [All users / specific roles] |

### Conditional Navigation

<!-- Navigation items that appear only under certain conditions
     (user role, subscription tier, feature flags, etc.) -->

| Navigation Item | Condition | Destination |
| --- | --- | --- |
| [Item] | [When it appears] | [Where it goes] |

---

## SCREEN INVENTORY

<!-- WHY THIS MATTERS: This is the complete list of screens in the product.
     Anti-Gravity uses this as a checklist — every screen should appear in
     at least one flow above. A screen that appears in no flow is either
     dead code or an undocumented feature. -->

<!-- For each screen, note: its name, what flow(s) it belongs to, and
     whether it has been implemented. -->

| Screen Name | Flow(s) | Status | Notes |
| --- | --- | --- | --- |
| [Screen 1] | [Which flows use it] | [Planned / Built / Needs Update] | [Any notes] |
| [Screen 2] | [Which flows use it] | [Status] | [Notes] |
| [Screen 3] | [Which flows use it] | [Status] | [Notes] |

---

## APP FLOW RISKS TO WATCH

- **Happy-path-only flows** — documenting only the success path and leaving error recovery to developer guesswork
- **Orphan screens** — screens that exist in the codebase but appear in no documented flow
- **Missing transitions** — flows that jump from step A to step C without defining what happens at step B
- **Assumed context** — flows that start mid-journey without explaining how the user arrived there
- **Role-blind flows** — flows documented for "the user" without specifying which user type, causing permissions and visibility confusion
- **Stale flows** — documented flows that no longer match the actual product behavior, causing Anti-Gravity to build against a phantom product

---

## APP FLOW ANTI-PATTERNS (NARRATIVES)

### The Disconnected Feature

### What it looks like

A new feature is built as a standalone screen with no clear entry point from existing navigation and no defined exit path back to the user's previous context.

### Why it is harmful

Users cannot discover the feature organically. When they do find it (via direct link or help docs), they cannot return to their previous task without using the browser back button. The feature feels bolted on rather than integrated.

### What to do instead

Before implementing any feature, define: Where does the user come from? Where do they go when done? How do they discover this feature in the first place? Add these connections to the app flow before writing code.

---

### The Happy-Path-Only Flow

### What it looks like

A flow is documented (or built) showing only the ideal sequence: user enters data → system processes → user sees result. No error states, no edge cases, no "what if the user goes back" scenarios.

### Why it is harmful

In production, the happy path is the minority case. Network failures, validation errors, expired sessions, permission issues, and user mistakes happen constantly. Without documented recovery paths, each developer invents their own, producing inconsistent and often broken error handling.

### What to do instead

For every step in a flow, answer: "What happens when this step fails?" Document the error state, the user's recovery options, and where they go next. This is especially critical for flows involving payments, data submission, or authentication.

---

### The Phantom Navigation

### What it looks like

The documented flow shows users navigating between screens by steps that do not correspond to any actual button, link, or menu item in the product. The flow makes logical sense on paper but has no physical implementation path.

### Why it is harmful

Developers build the screens but not the connections between them. Users are stranded — the next step exists, but there is no way to reach it without knowing a URL or clicking through unrelated navigation.

### What to do instead

For every transition in a flow, identify the specific UI element that triggers it. If no such element exists, add it to the design requirements before the flow is considered complete.

---

### The Infinite Loop

### What it looks like

An error recovery flow that sends the user back to the same step that caused the error, without changing anything about the step. The user retries, hits the same error, and is trapped in a frustrating cycle.

### Why it is harmful

Destroys user trust and creates support tickets. The user perceives the product as broken even if the error is on their end (e.g., invalid input, expired payment method).

### What to do instead

Error recovery flows must either: (a) change something about the step the user returns to (pre-fill corrected data, show a more specific error message, offer an alternative path), or (b) offer an escape route (contact support, skip this step, try a different method).

---

## KNOWN FLOW PROBLEMS / GAPS

Document concrete issues here so Anti-Gravity can be more careful in affected areas:

- [Fill in] Flows that are partially documented or have known gaps
- [Fill in] Screens that exist but are not yet connected to any documented flow
- [Fill in] Error states that are known to be poorly handled
- [Fill in] User journeys where feedback suggests users are getting lost or confused
- [Fill in] Flows that work differently on mobile vs desktop but are only documented for one

### Guidance for Anti-Gravity (Flow Problems)

- Do not treat undocumented flows as intentional — treat them as gaps
- When building a feature that touches a known-problematic flow, flag the issue and suggest improvements alongside the feature work
- If a user journey has no documented flow, ask for clarification before assuming the path

---

## INSTRUCTIONS FOR ANTI-GRAVITY

When using this file:

1. Read the relevant flow BEFORE implementing any screen — understand where the user comes from, what they do, and where they go next
2. Verify that every screen you build connects to the screens before and after it in the flow
3. Implement error and recovery paths documented in the flow, not just the happy path
4. If a feature request does not appear in any documented flow, ask: "Where does this fit in the user's journey?"
5. When modifying a screen, check whether the change affects any flow that passes through that screen
6. Do not create screens that are unreachable from the product's documented navigation
7. Treat transition states (loading, redirecting, confirming) as real steps that need implementation, not invisible gaps
8. When building a multi-step flow, ensure the user can always understand: where they are, where they came from, and how many steps remain
9. If the flow document and the actual codebase disagree, flag the discrepancy — do not silently follow either one
10. Use the compact flow notation when proposing changes to user journeys, so the full path is visible at a glance

---

## WHAT FUTURE FILES SHOULD ASSUME

Future context, architecture, and design files should assume:

- Every feature connects to a documented user journey — there are no orphan features
- Flow documentation includes error and recovery paths, not just the happy path
- Screen-level design decisions reference the flow context — what comes before and after
- Navigation changes are reflected in this file, not just in the codebase
- New user types receive their own documented primary journey before features are built for them
- This file is the bridge between `project-context.md` (what the product does) and `architecture-context.md` (how it is built) — it answers "how does the user experience it?"

---

## CROSS-REFERENCES

| Related Context File | Relationship |
| --- | --- |
| `project-context.md` | Defines the product identity, user types, and critical flows that this file maps in detail |
| `architecture-context.md` | Defines the routing, state management, and API structure that implements these flows |
| `DESIGN.md` | Defines the visual tokens and design language used within these flows |
| `domain-rules.md` | Business rules that constrain flow logic (e.g., "a booking cannot be confirmed without payment") |
| `security-baselines.md` | Authentication and authorization rules that gate access to specific flows |

---
