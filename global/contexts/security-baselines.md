# SECURITY BASELINES

**Version:** Gold v2.0
**Layer:** 6 — Context (Ground Truth)
**Tier:** 2 — Loaded by task
**File:** contexts/security-baselines.md
**Purpose:** Defines the minimum security posture, baseline protections, trust-boundary assumptions, and non-negotiable security rules that apply across this project. Anti-Gravity uses this to enforce YOUR security standards — not generic checklists.
**Loaded When:** Auth or permissions work, input handling, API design, data modeling, infrastructure changes, code review, dependency updates, or any work touching sensitive data or trust boundaries.
**Maintenance:** Review at least quarterly. Update immediately when auth changes, new compliance duties appear, or incidents reveal gaps. Stale security context is actively dangerous.

---

## HOW ANTI-GRAVITY USES THIS FILE

This file defines the security rules Anti-Gravity must respect in all generated, modified, or reviewed work.

**When loaded**, Anti-Gravity will:

- Apply your authentication and session patterns when generating protected endpoints or flows
- Enforce your authorization model at the correct boundaries
- Treat secrets according to your secret management policy
- Recommend validation and sanitization at the right input/output boundaries
- Avoid logging or exposing sensitive data beyond what this file allows
- Flag security concerns that violate this baseline posture, even when not asked explicitly

**When missing or incomplete**, Anti-Gravity will:

- Fall back to generic security habits that may not match your system
- Generate auth code that conflicts with your real session handling
- Miss project-specific security constraints (e.g., tenant isolation, data classification rules)
- Underestimate risks on flows this project considers high-sensitivity

**When stale**, Anti-Gravity will:

- Enforce outdated auth, authz, or secret-handling patterns
- Miss new trust boundaries introduced by architectural changes
- Apply wrong assumptions about data sensitivity or compliance scope

**Conflict rule:** If this file conflicts with a more specific stack-level or infra-level security file (`stack-context.md`, `infra-context.md`, framework-specific auth docs), the more specific file wins for that area. Flag the conflict rather than silently picking one.

**Authoritativeness rule:** When Anti-Gravity’s general training disagrees with a convention in this file, this file wins. Do not override these baselines for convenience. If a baseline seems wrong, surface it as a concern — do not silently ignore it.

---

## CURRENT PROJECT POSITION

Anti-Gravity Gold is currently a **structured intelligence architecture**, not yet a fully finalized runtime stack.

This file therefore has two layers:

| Layer | Name | Contents | When Active |
| --- | --- | --- | --- |
| **Layer 1** | Philosophy | Minimum security posture, safe assumptions, project-level baselines, risks, anti-patterns | Active now — independent of concrete stack |
| **Layer 2** | Conventions | Auth model, permission model, data classification, headers, CORS, secret handling, dependency policy, compliance specifics | Filled in and updated as the concrete stack and infra evolve |

> **Maintenance rule:** Stack changes update **Layer 2** (conventions).
> Changing **Layer 1** (philosophy) requires an explicit team decision
> that the project’s minimum security posture has changed.

This file does **not** lock down:

- Specific auth/identity products or IAM vendors
- Exact secret manager product or encryption library
- Exact network segmentation, WAF, or zero-trust tooling
- Exact CSP/CORS/header configurations for a specific framework

Those belong in stack/infra-specific files. This file defines the **minimum security posture** that should remain true regardless of tools.

---

## BASELINE SECURITY PHILOSOPHY

Security in this project is not an optional hardening pass.
It is a **baseline design responsibility**.

The project should default to:

- Explicit trust boundaries
- Least privilege access
- Careful handling of secrets and sensitive data
- Server-side or authoritative-boundary enforcement where authority matters
- Explicit treatment of high-risk flows
- Avoiding fail-open decisions on security-sensitive logic

### Meaning

Future work must not treat security as something to “add later” after architecture, APIs, and code are already fixed.

---

## CURRENT SAFE SECURITY ASSUMPTIONS

These assumptions are safe to apply now across the project:

### Assumption 1 — Secrets should never be handled casually

Credentials, API keys, tokens, and privileged secrets must not be casually embedded in code, docs intended for implementation, logs, or temporary debugging artifacts.

### Assumption 2 — Real authorization must happen at the authoritative boundary

UI restrictions, client-side logic, or convenience checks are not sufficient where real access control is required.

### Assumption 3 — Untrusted input is untrusted by default

External inputs, user-controlled data, and boundary-crossing payloads must not be assumed benign.

### Assumption 4 — High-risk changes deserve higher scrutiny

Changes affecting auth, authorization, trust boundaries, payments, sensitive data, secrets, or integrity-critical flows are not ordinary edits and require stronger review and verification.

### Assumption 5 — Security posture cuts across layers

Security will intersect implementation, API, infra, logging, and operational choices. It is not confined to one file or team.

### Assumption 6 — “Internal” does not automatically mean “safe”

Internal services, admin paths, or non-public surfaces are not exempt from security thinking by default.

---

## PROJECT-LEVEL SECURITY BASELINES

These baselines are the minimum rules Anti-Gravity must preserve.
Each has a Rule and a Meaning.

### Baseline 1 — Do not hardcode secrets

**Rule:** Secrets, credentials, tokens, and keys must not be embedded in code or long-lived implementation docs.

**Meaning:** Even in early-stage implementation planning, secret handling must be deliberate and externalized to proper mechanisms.

---

### Baseline 2 — Enforce authorization at the authoritative boundary

**Rule:** If an action requires permission, enforce it where authority actually lives — server, control plane, or equivalent — not only in the UI.

**Meaning:** Future designs must not rely on client-side restraint or hidden buttons as real protection.

---

### Baseline 3 — Prefer least privilege by default

**Rule:** Broad roles, broad data access, and broad infra permissions require explicit justification.

**Meaning:** “Give it wide access because it is easier” is suspicious by default and should not be the quiet default.

---

### Baseline 4 — Avoid unsafe leakage via logs, errors, and diagnostics

**Rule:** Sensitive data, tokens, credentials, and attacker-useful internals must not leak casually through logs, error messages, or observability tooling.

**Meaning:** Observability is important, but it must not become an accidental data-exposure channel.

---

### Baseline 5 — High-risk trust boundaries require explicit reasoning

**Rule:** Work that touches authentication, authorization, cross-tenant boundaries, privileged actions, sensitive data, destructive actions, or integrity-sensitive behavior must include explicit security reasoning.

**Meaning:** These areas are not “just another ticket” — they require deliberate thought about threats and controls.

---

### Baseline 6 — Security decisions should not fail open casually

**Rule:** If the system cannot determine whether an action is allowed, trusted, or valid, the default must not casually become broad access or silent success.

**Meaning:** The project should bias toward safe failure at security-sensitive decision points unless a documented exception exists.

---

### Baseline 7 — Security-relevant changes get intensified review

**Rule:** Security-sensitive changes require stronger review, testing, and rollout caution than cosmetic or low-risk changes.

**Meaning:** A passing happy-path test is not enough to treat a trust-boundary change as routine work.

---

## WHAT THIS FILE DOES **NOT** DECIDE YET

This file does **not** currently decide:

- Exact auth flow design or libraries
- Provider-specific IAM and policy structures
- Concrete secret manager product or vault configuration
- Exact encryption scheme parameters
- Precise network segmentation, WAF, or IDS tooling choices
- Detailed compliance implementation for each regulation

Those are set in stack, infra, and compliance context files.

This file should be read as:

```text
project-level minimum security posture
not full stack-specific security design
```

---

## SENSITIVE ASSETS

These are assets that require stronger protection by default:

- User accounts and identity data
- Authentication credentials and recovery flows
- API tokens, access tokens, refresh tokens, and signing keys
- PII / personal information (as defined for this project)
- Billing and payment-related data (even if delegated to a processor)
- Role/permission assignments and tenant relationships
- Admin / operator capabilities
- Customer data exports and bulk access paths
- Internal system secrets and configuration keys
- Logs that may contain operational or user context

### Guidance for Anti-Gravity (Assets)

- Treat work that touches these assets as high-rigor by default
- Do not assume equal sensitivity across all data — these require more care
- Prefer designs that minimize how often these assets are handled or exposed

---

## TRUST BOUNDARIES

Trust boundaries separate parts of the system that operate under different trust assumptions.

Examples include:

- Browser/client → backend
- Public internet → internal services
- Application → database
- Application → third-party integrations (payment, email, auth)
- Admin interface → privileged operations
- Internal tools → customer data stores
- Background jobs → production data

### Guidance for Anti-Gravity (Boundaries)

- Validate inputs at trust boundaries — not deep inside the system
- Enforce authorization where capability is granted, not only where UI is shown
- If a trust boundary is unclear, treat that as a risk and surface it

---

## AUTHENTICATION BASELINE

Authentication establishes identity; it does not grant rights by itself.

### Baseline Expectations

- Sensitive endpoints must require authenticated identity
- Session or token validity must be checked server-side or at the authoritative boundary
- Unauthenticated access must be explicit, not accidental
- Account recovery and login flows are high-sensitivity surfaces

### Guidance for Anti-Gravity (Authentication)

- Distinguish authentication (who you are) from authorization (what you can do)
- Never rely solely on client-side checks to enforce auth
- Treat identity establishment and recovery flows as high-risk, not routine forms

---

## AUTHORIZATION / ACCESS CONTROL BASELINE

Authorization governs **what** an authenticated identity may do.

### Baseline Expectations (AUTHORIZATION / ACCESS)

- Authorization checks must occur server-side or at authoritative boundaries — never UI-only
- Role/tenant/ownership rules must be enforced for read, update, delete, and export operations
- Admin/privileged actions require stronger checks and, where relevant, auditing
- Cross-tenant access must be explicitly prevented unless intentionally allowed

### Sensitive Actions Requiring Extra Caution

- Permission or role changes
- Data export, bulk access, or impersonation
- Destructive admin actions (delete, reset, override)
- Cross-tenant or cross-account operations

### Guidance for Anti-Gravity (Authorization)

- Any action that touches sensitive or user-specific data must be examined for **authorization**, not just authentication
- Prefer explicit, centralized authorization checks over scattered, ad-hoc checks
- When in doubt, recommend adding an authz check, not removing one

---

## INPUT VALIDATION BASELINE

Untrusted input must be validated and constrained.

### Baseline Expectations (INPUT VALIDATION BASELINE)

- Validate external inputs at the boundary (API, server action, message consumer, webhook)
- Do not rely on client-side validation for security — it is for UX only
- Constrain payload size, shape, and allowed values where meaningful
- Sanitize or escape outputs for the target rendering context (HTML, SQL, logs, etc.)

### Guidance for Anti-Gravity (Validation)

- Treat query params, headers, body payloads, file uploads, webhooks, and third-party callbacks as untrusted
- Recommend validation as the first step in processing untrusted input
- Prefer allowlists and structured schemas over ad-hoc checks

---

## OUTPUT / EXPOSURE BASELINE

Outputs can leak information just as inputs can introduce risk.

### Baseline Expectations (OUTPUT / EXPOSURE)

- Do not expose sensitive fields by default in responses or logs
- Avoid including internal error details, stack traces, or implementation secrets in public responses
- Apply encoding/sanitization appropriate to the output context
- Be cautious when reflecting user-supplied content back to clients

### Guidance for Anti-Gravity (Exposure)

- Prefer minimal, purpose-specific response shapes over “dump the whole object”
- When suggesting error handling, separate user-facing messages from internal diagnostics
- Treat logs, exports, and debug endpoints as potential exposure paths

---

## SENSITIVE DATA HANDLING BASELINE

Not all data is equal; some requires stricter handling.

### Baseline Expectations (SENSITIVE DATA HANDLING)

- Collect only what is needed; avoid storing unnecessary sensitive data
- Store sensitive data only where justified and with appropriate safeguards
- Transmit sensitive data over secure channels only
- Avoid logging or exposing sensitive user data unless explicitly required and justified
- Treat exports, reports, and admin views as exposure surfaces

### Guidance for Anti-Gravity (Data)

- Prefer designs that **minimize** exposure of sensitive fields
- If a suggestion increases data exposure (e.g., adding fields to an API), flag that impact explicitly
- Consider retention, backup, and archival when suggesting storage patterns for sensitive data

---

## SECRET HANDLING BASELINE

Secrets are always high-risk assets.

### Baseline Expectations (SECRET HANDLING BASELINE)

- No hardcoded secrets in code or committed files
- Secrets must come from approved secret/config systems, not ad-hoc mechanisms
- Secrets must not appear in logs, stack traces, screenshots, or client payloads
- Secret rotation must be possible without code changes

### Guidance for Anti-Gravity (Secrets)

- Never recommend hardcoding secrets, even in examples
- If secret handling is unclear, surface it as a risk rather than assuming a safe default
- Treat access to secrets as a privileged capability that should be narrowly scoped

---

## LOGGING AND OBSERVABILITY BASELINE

Logs are both a diagnostic tool and a potential leak.

### Baseline Expectations (LOGGING AND OBSERVABILITY)

- Log important auth/security events and failures at appropriate levels
- Do **not** log passwords, tokens, secrets, full payment details, or unnecessary PII
- Prefer structured logs where possible for better analysis
- Retain enough signal for incident investigation without turning logs into a data lake of sensitive information

### Guidance for Anti-Gravity (Logging)

- When recommending logging, focus on security-relevant context (what, who, where, when) without including secrets
- Avoid suggesting overly verbose logs in sensitive paths without redaction/filtering
- Treat audit logging for high-risk actions as desirable where feasible

---

## TRANSPORT / DATA-IN-TRANSIT BASELINE

How data moves matters as much as where it rests.

### Baseline Expectations (TRANSPORT / DATA-IN-TRANSIT)

- Use HTTPS/TLS for all production traffic
- Avoid placing sensitive data in URLs where it may end up in logs or browser history
- Validate webhook signatures or equivalent for incoming third-party callbacks
- Apply appropriate controls for internal service-to-service traffic, depending on environment

### Guidance for Anti-Gravity (Transport)

- Treat transport security as a baseline assumption, not an optional enhancement
- Call out when a suggested design would send sensitive data through a weaker channel

---

## DATA-AT-REST BASELINE

Stored data must respect sensitivity and retention needs.

### Baseline Expectations (DATA-AT-REST BASELINE)

- Sensitive data should be encrypted at rest where required
- Backups and exports should follow the same sensitivity rules as primary storage
- Data retention and deletion should align with project and compliance expectations

### Guidance for Anti-Gravity (At-Rest)

- When suggesting new storage of sensitive data, consider exposure, retention, and access boundaries
- Flag long-lived storage of highly sensitive fields as a risk unless clearly justified

---

## ABUSE AND MISUSE BASELINE

Security must consider misuse, not just intended use.

### Baseline Expectations (ABUSE AND MISUSE)

- Sensitive endpoints should have appropriate rate limiting or abuse controls
- Auth surfaces should defend against obvious brute-force and replay attempts
- Critical actions should consider idempotency or duplicate protection
- Suspicious patterns (e.g., repeated failures, access from unusual contexts) should be observable where important

### Guidance for Anti-Gravity (Abuse)

- For externally exposed or sensitive flows, do not reason only from the happy path
- Ask what misuse looks like and whether the suggested design would resist it

---

## HIGH-SENSITIVITY FLOWS

The following flows should receive stronger-than-normal scrutiny:

- Login, signup, and account recovery
- Password or credential reset flows
- Role/permission changes and membership management
- Billing and payment flows
- Data export and bulk access operations
- Destructive admin actions (delete, purge, impersonate)
- Account deletion and deactivation
- Secret rotation and key management
- Third-party webhook ingestion that impacts critical state

### Guidance for Anti-Gravity (Flows)

- Automatically escalate rigor when recommendations touch these flows
- Avoid silent convenience-over-security tradeoffs here
- Prefer explicit threat and control consideration instead of treating these as routine changes

---

## SECURITY SHORTCUTS THAT ARE NOT ACCEPTABLE

Anti-Gravity must never normalize these shortcuts in this project:

- Relying on frontend-only checks for access control
- Hardcoding secrets or tokens “temporarily” for convenience or demos
- Removing or bypassing authorization checks to make a flow work
- Returning internal stack traces or detailed internals in public errors
- Granting broad admin access “for speed” without explicit justification
- Treating “internal” surfaces as if they require no real security
- Skipping validation on external input because “it’s just internal use”

If a recommendation is fast, elegant, or convenient but violates these baselines, it is still the wrong recommendation.

---

## SECURITY RISKS TO WATCH

- **Convenience over trust boundary** — choosing the easier design that weakens real access controls
- **Client-trust illusion** — assuming UI/UX restrictions equate to real authorization
- **Secret sprawl** — credentials and tokens leaking into code, config, logs, or docs
- **Internal-equals-safe thinking** — assuming internal paths deserve less scrutiny
- **Security minimization under pressure** — calling risky shortcuts “temporary” without clear ownership

---

## SECURITY ANTI-PATTERNS (NARRATIVES)

### 1. Convenience Over Trust Boundary

### What it looks like

Weakening access control, skipping validation, or broadening privileges because the correct design feels slower or more annoying.

### Why it is harmful

It creates security debt exactly where trust should be strongest and often becomes permanent, not temporary.

### What to do instead

Preserve real boundary enforcement and, if an exception is truly needed, document scope, duration, and owner explicitly.

---

### 2. Client-Trust Illusion

### What it looks like

Assuming disabled buttons, hidden routes, or UI-only checks enforce authorization.

### Why it is harmful

A malicious or buggy client can bypass surface-level restrictions entirely.

### What to do instead

Enforce permissions at the authoritative server or control boundary and treat UI checks as UX, not security.

---

### 3. Secret Sprawl

### What it looks like

Credentials appearing in source, logs, screenshots, tickets, or local scripts.

### Why it is harmful

Every copy increases the attack surface and complicates incident response and rotation.

### What to do instead

Centralize secret storage, prohibit secrets in code and logs, and treat secret handling as a first-class operational concern.

---

### 4. Internal-Equals-Safe Assumption

### What it looks like

Treating internal APIs, admin tools, or back-office systems as exempt from rigorous security because they are “not public.”

### Why it is harmful

Many serious incidents target exactly those internal paths via lateral movement or insider misuse.

### What to do instead

Apply explicit trust reasoning and appropriate controls even on non-public surfaces.

---

### 5. Security-Sensitive Changes Reviewed Like Routine Edits

### What it looks like

Auth, authz, or sensitive-data changes going through the same level of review as minor UI tweaks.

### Why it is harmful

Underestimates the blast radius of mistakes in those areas.

### What to do instead

Increase scrutiny, verification depth, and rollout caution for any change that affects trust boundaries, sensitive data, or privileged actions.

---

## COMPLIANCE / POLICY CONSTRAINTS

If this project is subject to regulatory or contractual constraints, they shape what is acceptable.

Examples may include:

- GDPR or other privacy regulations
- HIPAA or health-data protections
- PCI-related payment data handling constraints
- Data residency or localization requirements
- Audit logging and retention policies
- Enterprise access-control obligations

### Guidance for Anti-Gravity (Compliance)

- When recommendations touch regulated data or flows, call out compliance impact explicitly
- Do not assume a “policy-neutral” environment on regulated surfaces
- Prefer designs that make compliance easier, not harder

---

## KNOWN SECURITY-SENSITIVE AREAS / WEAK SPOTS

Document known weak or high-caution areas so Anti-Gravity can be more conservative:

- [Fill in] Legacy auth flows with inconsistent checks
- [Fill in] Older admin endpoints relying on weak role assumptions
- [Fill in] Webhook validation uneven across providers
- [Fill in] Incomplete audit logging in some sensitive flows
- [Fill in] Divergent frontend vs backend validation in old modules
- [Fill in] Internal tools with broader privileges than strictly needed

### Guidance for Anti-Gravity (Gaps)

- Treat these as caution zones, not “probably fine”
- Prefer stronger verification and defense recommendations when working in or near these areas

---

## EXCEPTIONS / PRACTICAL NOTES

Not every surface gets identical controls, but exceptions must be conscious and scoped.

Examples:

- Some internal-only tools may trade a bit of UX friction for practicality, while still enforcing auth/authz
- Local development may use simplified auth, but production guidance must not inherit those shortcuts
- Low-risk internal glue code may not justify full hardening, but must not undermine higher-level protections

### Guidance for Anti-Gravity (Pragmatism)

- Apply baselines proportionately, but do not let “internal” become an excuse for sloppy reasoning
- When suggesting an exception, name its scope, rationale, and limits
- Do not silently normalize existing violations; call them out

---

## INSTRUCTIONS FOR ANTI-GRAVITY

When using this file:

1. Treat these baselines as the **minimum**, not optional enhancements
2. Escalate rigor when work touches sensitive assets or high-sensitivity flows
3. Keep authentication, authorization, validation, and exposure distinct in your reasoning
4. Make security tradeoffs explicit when convenience or speed competes with safety
5. Respect trust boundaries when suggesting design or implementation changes
6. Do not recommend patterns that undercut this project’s baseline posture
7. If a requested change violates a baseline, say so clearly and suggest safer alternatives
8. When context is incomplete, state what security assumptions you are making
9. If the current system violates a baseline, do not normalize it — treat it as known debt
10. Use this file as the **floor** for secure reasoning in this project

---

## WHAT FUTURE FILES SHOULD ASSUME

Future stack/infra files should assume that:

- Security is a baseline design concern, not post-hoc hardening
- Auth, authz, trust boundaries, and sensitive data flows require explicit treatment
- Stack-specific security details may refine but must not weaken these baselines
- High-risk changes carry stronger review and verification expectations than routine edits

---

## CROSS-REFERENCES

| Related Context File | Relationship |
| --- | --- |
| `stack-context.md` | Auth libraries, crypto choices, and session implementation details |
| `architecture-context.md` | Trust boundaries and service/module boundaries |
| `coding-standards.md` | Error handling and logging conventions affect security surfaces |
| `api-conventions.md` | API auth, rate limiting, error response, and validation patterns |
| `infra-context.md` | Infrastructure security, networking, monitoring, and incident response |
| `testing-standards.md` | How auth and security behavior are tested and mocked |

---
