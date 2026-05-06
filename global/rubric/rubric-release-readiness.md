# RUBRIC: RELEASE READINESS

**Version:** Gold v1.0
**Layer:** 10 — Evaluation
**Tier:** 3 — Loaded on demand
**File:** rubrics/release-readiness-rubric.md
**Purpose:** Meta-rubric for evaluating whether a feature, release, or deployment is ready to ship to production. Aggregates quality signals across ALL dimensions — code, tests, security, performance, UX, documentation, and operations.
**Loaded When:** Before any production deployment. Final "should we ship?" evaluation. Referenced by workflow-ship-to-production.md.
**References:** All other rubrics, quality-bar.md, workflow-ship-to-production.md

***

## HOW TO USE THIS RUBRIC

This is the FINAL checkpoint before shipping. It evaluates readiness
across every dimension that matters. Unlike the deployment workflow
(which is a process to follow), this rubric is an evaluation
(which is a quality judgment to make).

Use this when asking: "Is this READY?" — not "What are the STEPS?"

For the steps, use `workflow-ship-to-production.md`.
For the judgment, use this rubric.

Use this rubric:

- Before production release and go/no-go decisions
- When reviewing release plans and rollout strategies
- After release workflow preparation
- During pre-release go/no-go review
- During rollout plan assessment and release readiness signoff
- During production delivery quality critique

***

## WHAT THIS RUBRIC EVALUATES

This rubric evaluates release readiness across:

- Functional completeness and scope clarity
- Code quality
- Test coverage and verification confidence
- Security posture and sensitivity awareness
- Performance acceptability
- User experience readiness
- Data integrity and migration safety
- Operational readiness and rollback readiness
- Documentation and communication
- Risk assessment and blast radius understanding

This rubric is for judging whether "done" is actually "safe enough
to release." A release is ready not when the work is finished,
but when the risk is understood, the behavior is verified,
the rollout is controlled, and failure is survivable.

***

## EVALUATION MATRIX

### 1. FUNCTIONAL COMPLETENESS AND SCOPE CLARITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | All scoped functionality implemented and verified. Acceptance criteria met for every user story. Edge cases handled. No partial implementations or stubs in production code. It is clear exactly what is being shipped. Affected components, flows, and contracts are understood. Success metric instrumentation in place. |
| **Acceptable** | Core functionality complete and working. Minor nice-to-have items deferred and documented. No broken or half-implemented features. Release scope reasonably clear and bounded. |
| **Needs Work** | Most functionality works but some gaps remain. Some acceptance criteria not fully met. Scope boundaries somewhat unclear. Workarounds needed for edge cases. |
| **Failing** | Core functionality incomplete or broken. Features partially implemented. Release scope vague or poorly understood. Would ship a broken experience to users. |

***

### 2. CODE QUALITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Code passes all dimensions of the code-quality rubric at **Acceptable** or above. Clean, readable, maintainable, and convention-compliant. No debug artifacts or commented-out code. Self-review completed. Scope is controlled and solution is proportionate to the requirement. |
| **Acceptable** | Code is clean and functional. Minor quality improvements possible but nothing that affects reliability or maintainability. Follows project conventions well enough. |
| **Needs Work** | Code has quality issues — messy logic, unclear naming, inconsistent patterns — but is functionally correct. Technical debt being deliberately shipped. |
| **Failing** | Code quality significantly below standards. Missing error handling, convention violations throughout. Would fail code review. Should not reach production in current state. |

***

### 3. TEST COVERAGE AND VERIFICATION CONFIDENCE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | All critical paths tested. Tests verify behavior, not implementation. Edge cases and regression risks covered. All tests pass reliably. No flaky tests. CI pipeline fully green. Verification confidence is proportionate to the release risk level. |
| **Acceptable** | Critical paths tested. Tests pass reliably. Main error scenarios covered. Minor edge case gaps documented as known limitations. Verification sufficient for the risk level. |
| **Needs Work** | Some critical paths untested. Tests pass but coverage is thin. Key edge cases unconsidered. Confidence to deploy is only moderate. |
| **Failing** | Critical functionality untested. Tests failing or flaky. CI pipeline not fully green. Would be deploying without a meaningful safety net. |

***

### 4. SECURITY POSTURE AND SENSITIVITY AWARENESS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | All dimensions of the security rubric at **Acceptable** or above. Auth and authz verified. Input validation complete. No secrets exposed. Security headers configured. Dependency audit clean. Security-sensitive and data-integrity-sensitive implications reviewed with appropriate rigor. Protected flows treated proportionately. |
| **Acceptable** | No known security vulnerabilities. Auth correctly implemented. Input validated. Secrets managed properly. Sensitive changes reviewed proportionately. |
| **Needs Work** | Minor security gaps that do not create exploitable vulnerabilities. Auth or permission behavior changed without stronger scrutiny. Defense-in-depth could be stronger. |
| **Failing** | Security vulnerabilities present. Auth bypass possible. Input validation missing. Secrets exposed. Trust-boundary impact unreviewed. **MUST NOT SHIP.** |

***

### 5. PERFORMANCE ACCEPTABILITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Performance measured and within targets. No obvious bottlenecks. No operations that would degrade under realistic load. Database queries indexed. Page load and response times within acceptable targets. Performance proportionate to the actual system needs. |
| **Acceptable** | Performance is acceptable for current scale. No obvious bottlenecks. Meets baseline performance expectations. Minor inefficiencies that are not likely to matter at expected scale. |
| **Needs Work** | Some operations are slower than ideal but not critically impacting user experience. Known slow path that should be addressed soon. |
| **Failing** | Significant performance issues. Operations that would noticeably degrade user experience. Unindexed queries on large tables. Features that would break under moderate load. |

***

### 6. USER EXPERIENCE READINESS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | All dimensions of the UX rubric at **Acceptable** or above. All states implemented — loading, empty, error, success. Accessible for keyboard, screen reader, and contrast. Responsive across target devices. Error messages user-friendly. Interaction feedback complete. Consistent with design system. |
| **Acceptable** | Primary user flows work well. Major states covered. Accessible for primary flows. Works on primary devices and browsers. Minor UX gaps that do not block core usage. |
| **Needs Work** | Happy path works but some states are missing or rough. Accessibility gaps. Responsive issues on some devices. UX risk visible but not critical. |
| **Failing** | UX is broken or confusing. Missing loading states producing blank pages. Raw error messages shown to users. Not responsive. Accessibility failures. Would damage user trust or experience. |

***

### 7. DATA INTEGRITY AND MIGRATION SAFETY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Database migrations tested and safe. Breaking changes use an expand-contract or equivalent safe sequencing pattern. Rollback path verified. No data corruption risk. Transactions used where atomicity matters. Schema and API consumer transitions understood and managed deliberately. Old and new states compatible with a clear plan. |
| **Acceptable** | Migrations are safe — additive only or properly sequenced. Data integrity maintained. Basic rollback path exists. Migration and compatibility impact understood. |
| **Needs Work** | Migrations not tested against production-volume data. Rollback path exists but not verified. Minor data consistency risks. Migration sequencing somewhat unclear. |
| **Failing** | Migration could corrupt data or cause downtime. No rollback path. Data integrity at risk. Breaking schema or contract change without safe sequencing. Downstream systems or users would break. |

***

### 8. OPERATIONAL READINESS AND ROLLBACK READINESS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Rollout strategy is appropriate to the risk — feature flags, canary, staged rollout, or migration sequencing used where needed. Rollback procedure is realistic, documented, feasible, and fast enough if needed. Error monitoring covers new code paths. Relevant logs added for debugging. Health metrics available. On-call engineer aware of the deployment. Post-deployment monitoring plan defined. Team understands what changed. |
| **Acceptable** | Rollout approach is reasonable for the risk level. Rollback is possible and understood. Error monitoring active. Basic logging present. Team aware of deployment. Operators can support the release. |
| **Needs Work** | Rollout strategy not matched to the risk. Rollback possible but not practiced or clearly defined. Monitoring coverage uncertain for new code. Logging minimal. Some operational surprises likely. |
| **Failing** | No rollout strategy for a risky change. Rollback is imaginary or not feasible in practice. No monitoring for new functionality. Team unaware of deployment. No mitigation plan. No recovery path. Flying blind. |

***

### 9. DOCUMENTATION AND COMMUNICATION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | What changed is documented clearly. User-facing changes communicated to relevant teams. API documentation updated where relevant. Architecture or convention changes captured. Decisions logged where significant. What changed and why is understandable to anyone who needs to know. |
| **Acceptable** | Change is documented sufficiently. Team is aware. Major documentation updated. Change understandable without requiring the author to explain it. |
| **Needs Work** | Minimal documentation. Team has limited awareness of what is shipping. Important context lives only in the author's head. |
| **Failing** | No documentation of what changed or why. No one besides the author understands the change. Relevant files or records outdated. Support burden not considered. |

***

### 10. RISK ASSESSMENT AND BLAST RADIUS UNDERSTANDING

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Risks identified and mitigated. Blast radius understood — affected users, systems, and high-risk surfaces known. Rollback criteria defined explicitly. Pre-mortem conducted for high-stakes changes. Worst-case scenario has a response plan. Release risk is understood, not assumed away. Ship decision is supported by evidence rather than confidence tone or time pressure. |
| **Acceptable** | Major risks identified. Rollback is possible and understood. Team understands what could go wrong. Release risk is acknowledged and proportionate to the mitigations in place. |
| **Needs Work** | Risks acknowledged vaguely. Rollback possible but criteria not defined. Blast radius only roughly understood. Some unresolved assumptions still attached to this release. |
| **Failing** | No risk assessment. High-stakes change deployed with no safety net. No rollback criteria. No monitoring plan. Blast radius not understood. Known release risks framed too softly to affect the go/no-go judgment. |

***

## SCORING SUMMARY

| Dimension | Score | Notes |
| :--- | :--- | :--- |
| Functional Completeness / Scope Clarity |||
| Code Quality |||
| Test Coverage / Verification Confidence |||
| Security Posture / Sensitivity Awareness |||
| Performance Acceptability |||
| User Experience Readiness |||
| Data Integrity / Migration Safety |||
| Operational Readiness / Rollback Readiness |||
| Documentation and Communication |||
| Risk Assessment / Blast Radius |||
***

## RELEASE DECISION FRAMEWORK

### ✅ SHIP — All dimensions Excellent or Acceptable

The release is ready. Deploy following `workflow-ship-to-production.md`.

***

### ⚠️ SHIP WITH CAUTION — 1–2 dimensions at Needs Work (non-critical)

Ship if:

- The **Needs Work** dimensions are not Security, Data Integrity, or Functional Completeness.
- The gaps are documented and follow-up work is planned.
- The risk is understood and explicitly accepted.

Document the accepted gaps before shipping:

- **[Dimension]:** [What is incomplete] — Follow-up: [planned action + timeline]
- **[Dimension]:** [What is incomplete] — Follow-up: [planned action + timeline]

***

### ❌ DO NOT SHIP — Conditions for rejection

| Condition | Why |
| :--- | :--- |
| Security Posture is Failing | Security vulnerabilities in production are unacceptable |
| Data Integrity is Failing | Data corruption is irreversible |
| Functional Completeness is Failing | Shipping broken features damages user trust |
| Test Coverage is Failing **AND** change is high-risk | No safety net for a risky change |
| 3+ dimensions at Needs Work | Too many quality gaps — risk of compounding issues |
| Any single dimension at Failing | Every Failing score represents a serious quality gap |

***

### 🔥 HOTFIX EXCEPTION

For P1 or P2 incident hotfixes:

- **Security Posture:** Must still be **Acceptable** — never ship a fix that creates a new vulnerability.
- **Functional Completeness:** May be **Needs Work** — fixing the incident is the priority.
- **Test Coverage:** Must include a regression test for the specific incident.
- **All other dimensions:** **Acceptable** minimum, with full quality follow-up within 48 hours.

***

## PRE-SHIP CONVERSATION

Before shipping, the release owner should be able to answer **YES** to all of these:

1. If this breaks at 2 AM, can the on-call engineer diagnose and fix or roll back?
2. If a user reports an issue with this feature, will our monitoring detect it?
3. If we need to roll this back, how long will it take and what is the data impact?
4. Have I tested this the way a real user would use it — not just the way a developer would?
5. Am I confident enough in this release that I would deploy it on a Friday?
   - If yes: it is ready.
   - If no: what specifically makes you uncomfortable? Fix that.

***

## MINIMUM PASS STANDARD

A release should not be considered ready if it is weak in any of these high-priority areas:

- Verification confidence — behavior tested, not assumed.
- Rollback readiness — realistic path to recovery exists.
- Migration and compatibility — downstream systems are safe.
- Observability — the team will know if something goes wrong.
- Security sensitivity — protected paths reviewed appropriately.

Code completion is not enough.

***

## COMMON FAILURE PATTERNS

### Deploy-and-Pray

The release plan relies on hope more than staged control or observability. No rollout strategy for a risky change.

### One-Size-Fits-All Rollout

A high-risk change gets the same rollout posture as a trivial one. Risk is not matched to mitigation.

### Rollback Fantasy

A rollback path is claimed but not realistic or feasible for the actual change. Tribal knowledge is the plan.

### Deployment-Success Illusion

Technical deployment success mistaken for production success without stabilization checks or monitoring.

### Open-Concern Minimization

Known release risks exist but are framed too softly to affect the go/no-go judgment. Pressure wins over readiness.

### Shipping Because Time Won

"Safe to ship" supported by confidence tone rather than evidence. Time pressure overriding honest readiness assessment.

***

## POST-RELEASE FOLLOW-UP

After shipping, within 48 hours:

- [ ] Verify all Ship with Caution gaps have follow-up tickets created.
- [ ] Verify post-deployment monitoring showed no issues.
- [ ] If issues were detected: document in postmortems.
- [ ] If significant decisions were made: update decisions log.
- [ ] If patterns were learned: update common patterns record.

***

## FINAL QUESTIONS

Before shipping, ask:

- If this fails in production, will we know quickly and know what to do?
- Are we shipping because it is ready, or because time pressure is winning?
- What is the most dangerous unresolved assumption still attached to this release?
- Is the rollback path real or imaginary?
- Would a thoughtful engineer be comfortable with this going to production right now?

***

## A release is ready not when the work is finished, but when the risk is understood, the behavior is verified, the rollout is controlled, and failure is survivable
