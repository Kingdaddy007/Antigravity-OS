# RUBRIC: SECURITY QUALITY

**Version:** Gold v1.0
**Layer:** 10 — Evaluation
**Tier:** 3 — Loaded on demand
**File:** rubrics/security-rubric.md
**Purpose:** Self-assessment matrix for evaluating security posture of code, features, or systems.
**Loaded When:** Phase 7 of any security-sensitive task. Security review. Evaluating whether code meets security baselines.
**References:** skill-security.md, workflow-security-audit.md, security-baselines.md

***

## HOW TO USE THIS RUBRIC

After completing a security-sensitive feature, design, or review,
evaluate your work against each dimension below. Score each dimension.

- If **any dimension** scores **Failing** — BLOCK delivery.
  Security failures are never acceptable for delivery.

- If **Authorization or Input Validation** scores **Needs Work** —
  fix before delivery. These are the most common exploit vectors.

- If **Secret Management** scores **Failing** — take IMMEDIATE action.
  Secrets may already be compromised.

Use this rubric:

- During security review before approving security-sensitive changes
- During pre-release high-risk review
- When evaluating threat or hardening recommendations
- During auth and authz design evaluation
- During sensitive-data handling review
- When prioritizing remediation severity
- During benchmark comparison of security approaches

***

## WHAT THIS RUBRIC EVALUATES

This rubric evaluates security quality across:

- Trust-boundary awareness and asset identification
- Authentication correctness
- Authorization and privilege discipline
- Input validation and output safety
- Data protection and sensitive data handling
- Secret and credential management
- Blast radius and failure safety
- Security headers and configuration
- Dependency security
- Auditability and observability
- Abuse and misuse thinking
- Mitigation quality and proportionality

This rubric is for judging whether security thinking is real —
not cosmetic. Security is not present because someone mentioned
auth or OWASP. Security is present when trust is enforced,
exposure is reduced, and misuse is hard.

***

## EVALUATION MATRIX

### 1. TRUST BOUNDARY CLARITY AND ASSET IDENTIFICATION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Important assets, capabilities, and sensitive surfaces are identified clearly. Trust boundaries are explicit rather than implied. Untrusted input is treated as untrusted. Boundary crossings are enforced rather than assumed. It is obvious what needs to be protected and from whom. Trusted and untrusted actors and systems are distinguished correctly. |
| **Acceptable** | Trust boundaries identified and reasonably clear. Primary assets and sensitive surfaces identified. Most boundary crossings enforced. Minor implicit trust assumptions that do not create serious risk. |
| **Needs Work** | Trust boundaries vague or partially identified. Some "internal" systems assumed safe without verification. Boundary transitions not clearly identified. Hidden trust assumptions present. |
| **Failing** | No trust boundaries identified. Untrusted input treated as trusted. Internal assumed safe without reason. No analysis of what needs protection or from whom. |

***

### 2. AUTHENTICATION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Auth implemented correctly per security baselines. Session management secure. Rate limiting on auth endpoints. Account lockout policy enforced. Password handling follows policy. Token and session assumptions are explicit. All auth paths tested. Authentication required where appropriate. |
| **Acceptable** | Auth correctly implemented. Sessions managed securely. Basic rate limiting present. Standard password handling. Auth required on all appropriate paths. |
| **Needs Work** | Auth present but with gaps. Missing rate limiting. Session handling has minor weaknesses. Authentication assumed but not fully enforced in some paths. Weak or unclear session and token handling. |
| **Failing** | Auth bypass possible. Session tokens predictable or exposed. No rate limiting on login. Passwords stored improperly. Auth missing where required. |

***

### 3. AUTHORIZATION AND PRIVILEGE DISCIPLINE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Every protected action checks both authentication AND authorization server-side. Role-based permissions match the defined matrix exactly. Resource-level access enforced — users cannot access other users' data. No IDOR vulnerabilities. Authorization logic centralized and consistent. Least privilege preserved throughout. Privileged actions protected appropriately. |
| **Acceptable** | Authorization checked on all critical paths. Role permissions generally correct. Resource-level access enforced for primary entities. Least privilege mostly respected. |
| **Needs Work** | Some endpoints missing authorization checks. Partially relying on client-side authorization. Resource-level access inconsistent. Role assumptions too broad in places. Access control not checked per resource or action consistently. |
| **Failing** | Authorization missing or bypassable. Privilege escalation possible. Users can access other users' data. Client-side-only authorization checks. Authentication treated as sufficient without authorization enforcement. |

***

### 4. INPUT VALIDATION AND OUTPUT SAFETY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | All user input validated server-side with strict schemas. Validation at every trust boundary crossing. SQL injection impossible via parameterized queries. XSS prevented via output escaping and CSP. File uploads validated for type, size, and content. Dangerous outputs constrained, encoded, or filtered appropriately. Output does not leak sensitive or internal details. Misuse paths considered. |
| **Acceptable** | Server-side validation present on all primary inputs. Parameterized queries used. Basic XSS prevention. File upload limits enforced. Most dangerous outputs constrained. |
| **Needs Work** | Some inputs not validated server-side. Relying on client-side validation for security. Some raw queries without parameterization. Unsafe rendering or serialization in places. Unbounded input assumptions present. |
| **Failing** | No server-side validation. SQL injection possible. XSS possible. Unvalidated file uploads accepted. Client-side validation treated as sufficient. Output leaking sensitive or internal details. |

***

### 5. SENSITIVE DATA AND DATA PROTECTION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Sensitive data classified and handled per classification rules. PII encrypted at rest. All data encrypted in transit via TLS. No sensitive data in logs. No sensitive data in client-side code or bundles. API responses expose minimum necessary data. Sensitive field exposure limited deliberately. |
| **Acceptable** | Sensitive data generally protected. TLS enforced. Most PII handled correctly. Logs mostly clean of sensitive data. API responses reasonably scoped. |
| **Needs Work** | Some sensitive data handling gaps. Overly broad API responses. Some PII in logs. Sensitive field exposure not fully minimized. |
| **Failing** | Sensitive data exposed in logs, error messages, or client-side code. No encryption at rest. API returns internal data structures including sensitive fields. PII or tokens visible in operational surfaces. |

***

### 6. SECRET AND CREDENTIAL MANAGEMENT

| Score | Criteria |
| :--- | :--- |
| **Excellent** | No secrets in code or git history. All secrets in environment variables with proper scoping. Rotation policy followed. Development secrets separated from production. Secret access logged. Secret sprawl avoided. |
| **Acceptable** | Secrets properly externalized. Not in code or git. Rotation policy exists. Development and production secrets separated. |
| **Needs Work** | Secrets externalized but management is informal. No rotation policy. Development and production secrets may share values. Secret handling not fully auditable. |
| **Failing** | Secrets hardcoded in source code. Secrets committed to git history. Same secrets in development and production. No rotation ever. Credentials or tokens leaking into logs or payloads. |

***

### 7. BLAST RADIUS AND FAILURE SAFETY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | If a control fails, the blast radius is explicitly understood and minimized. Least-privilege and compartmentalization principles applied. Failure defaults to safe behavior — fail-closed rather than fail-open on sensitive paths. One compromise does not expose too much of the system. Boundary isolation strong. |
| **Acceptable** | Blast radius considered for primary failure scenarios. Least privilege generally respected. Failure behavior mostly safe. Boundaries provide reasonable isolation. |
| **Needs Work** | Blast radius not explicitly evaluated. Some broad privilege scopes without justification. Failure behavior for sensitive paths not fully specified. Boundary isolation weaker than it should be. |
| **Failing** | No blast-radius thinking. Fail-open behavior on sensitive paths. Broad privilege scopes throughout. One compromise exposes large portions of the system. Weak boundary isolation. |

***

### 8. SECURITY HEADERS AND CONFIGURATION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, and Permissions-Policy all set correctly. CORS configured with specific origins — no wildcard. HSTS enabled. Security headers tested and verified. |
| **Acceptable** | Key security headers present — CSP, X-Frame-Options, HSTS. CORS configured with reasonable restrictions. |
| **Needs Work** | Some security headers missing. CORS overly permissive. CSP not configured or too loose. |
| **Failing** | No security headers. CORS allows all origins. No HSTS. Browser security features not leveraged. |

***

### 9. DEPENDENCY SECURITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | No known vulnerabilities in dependencies. Lock file committed and reviewed. Regular automated vulnerability scanning. License compliance verified. New dependencies reviewed before adoption. |
| **Acceptable** | No critical vulnerabilities. Lock file committed. Periodic vulnerability scanning. |
| **Needs Work** | Some known non-critical vulnerabilities. Scanning not regular. Lock file not consistently reviewed. New dependencies adopted without formal review. |
| **Failing** | Critical vulnerabilities in dependencies. No vulnerability scanning. Unknown dependency licenses. No review process for new dependencies. |

***

### 10. AUDITABILITY AND OBSERVABILITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Suspicious behavior would be detectable through meaningful security telemetry. Auth failures, privilege misuse, and abuse patterns are visible and traceable. Operational investigation is realistic. Security-relevant events logged without becoming a leakage vector. Incidents traceable after the fact. |
| **Acceptable** | Major auth and access events logged. Basic security telemetry present. Most incidents traceable with reasonable effort. Logs useful without exposing sensitive data. |
| **Needs Work** | Limited security telemetry. Some auth and misuse events not logged. Incidents difficult to trace without significant manual effort. Misuse partially invisible. |
| **Failing** | No meaningful security telemetry. Auth failures not logged. Incidents invisible unless discovered manually. No audit trail for privileged operations. |

***

### 11. ABUSE AND MISUSE THINKING

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Analysis goes beyond happy-path behavior. Replay, tampering, brute force, overreach, and abuse scenarios considered where relevant. Real exploit paths identified and addressed. Security thinking grounded in concrete abuse paths, not generic fear. |
| **Acceptable** | Main abuse scenarios considered. Key misuse paths identified. Findings connected to real risk rather than theoretical concern. |
| **Needs Work** | Analysis mostly happy-path. Some misuse scenarios mentioned but not analyzed deeply. Findings sound serious but lack concrete exploit path connection. |
| **Failing** | No misuse thinking. Only the intended use case considered. Generic risk language with no concrete abuse paths. Security theater with no actual enforcement thinking. |

***

### 12. MITIGATION QUALITY AND PROPORTIONALITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Mitigations are concrete, proportionate to real risk, and placed at the correct layer. Recommendations are enforceable, not vague. Security and usability tradeoffs made visible where relevant. Convenience is not silently overriding protection. High-risk issues identified and prioritized correctly. Blocking conditions and remediation direction are clear. |
| **Acceptable** | Key mitigations concrete and actionable. Proportionate to identified risk. Most recommendations enforceable. Blocking conditions clear. |
| **Needs Work** | Some mitigations vague — "add security" without specifics. Convenience shortcuts normalized without explicit acknowledgment. Prioritization uneven. Some recommendations not clearly enforceable. |
| **Failing** | Vague mitigations throughout. Overconfident claims of safety. Security theater with no actual enforcement. All risk labeled maximum priority making true prioritization impossible. No clear blocking conditions or remediation direction. |

***

## SCORING SUMMARY

| Dimension | Score | Notes |
| :--- | :--- | :--- |
| Trust Boundary Clarity / Asset ID |||
| Authentication |||
| Authorization / Privilege Discipline |||
| Input Validation / Output Safety |||
| Sensitive Data / Data Protection |||
| Secret / Credential Management |||
| Blast Radius / Failure Safety |||
| Security Headers / Configuration |||
| Dependency Security |||
| Auditability / Observability |||
| Abuse / Misuse Thinking |||
| Mitigation Quality / Proportionality |||
***

## DELIVERY DECISION

| Result | Decision |
| :--- | :--- |
| All Excellent / Acceptable | ✅ Security posture is adequate for delivery |
| Any dimension Failing | ❌ BLOCK — security failures are never acceptable for delivery |
| Authorization or Input Validation Needs Work | ⚠️ Fix before delivery — these are the most common exploit vectors |
| Secret Management Failing | ❌ IMMEDIATE action — secrets may already be compromised |

***

## MINIMUM PASS STANDARD

Security work should not be considered strong if it is weak
in any of these high-priority areas:

- Authorization — enforced at the right level, per resource
- Trust-boundary handling — boundaries explicit and enforced
- Input and output safety — server-side, at every boundary
- Secret and sensitive data handling — no leakage, no sprawl

Weakness in these areas often creates serious downstream risk.
Visual or procedural security does not compensate for
enforcement gaps.

***

## COMMON FAILURE PATTERNS

### Client-Side Trust Illusion

Surface-level UI restriction mistaken for real access control.
Authorization must be enforced server-side — always.

### Secret Sprawl

Sensitive credentials or tokens leak into code, logs, or
weak operational handling. Git history is permanent.

### Generic Fear Without Concrete Path

Review language sounds serious but does not connect findings
to real exploit paths. Risk without specificity is not
actionable.

### All-Risk-Is-Max-Risk Thinking

Everything labeled critical, making true prioritization
weaker. Proportionality is a security discipline too.

### Approval Ambiguity

The review identifies problems but never says whether the
target is actually acceptable or blocked. Unclear outcome
is not a safe outcome.

### Happy-Path-Only Security Design

Security reasoning only applied to the intended use case.
Misuse, abuse, and edge cases left unanalyzed.

### Convenience Silently Overriding Protection

Security shortcuts normalized without explicit
acknowledgment of the tradeoff being accepted.

***

## FINAL QUESTIONS

Before approving this security review or feature, ask:

- If this were abused, did we meaningfully think about how?
- Are we protecting the real capability and asset, or just the UI around it?
- What is the most dangerous thing a bad actor could still do after this?
- Are trust boundaries enforced or merely assumed?
- Is misuse hard, or just not the intended path?
- Would suspicious behavior be detectable and traceable?

***

## Security is not present because someone mentioned auth or OWASP. Security is present when trust is enforced, exposure is reduced, and misuse is hard
