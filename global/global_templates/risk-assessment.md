# TEMPLATE: RISK ASSESSMENT

**Version:** Gold v1.0
**Layer:** 9 — Output Contract
**Tier:** 3 — Loaded on demand
**File:** templates/risk-assessment.md
**Purpose:** Standardized format for evaluating risks associated with technical decisions, feature launches, infrastructure changes, or any significant engineering initiative.
**Loaded When:** Evaluating risk before a major decision, deployment, architecture change, or when risk assessment is requested.

***

## WHEN TO USE THIS TEMPLATE

Use this template when:

- Making a Type 1 decision (irreversible, high-stakes)
- Planning a significant deployment or migration
- Launching a feature to a large user base
- Evaluating whether to proceed with a risky initiative
- Post-incident: assessing residual risk after a fix
- Release-risk assessment
- Security or architecture risk summary
- Feature or initiative planning with meaningful uncertainty
- Tradeoff decisions where explicit risk ownership matters

Do NOT use for routine decisions or low-risk changes.

***

## THE TEMPLATE

***

### Risk Assessment: [Initiative / Decision / Change]

***

## Metadata

| Field | Value |
| :--- | :--- |
| Date | [YYYY-MM-DD] |
| Assessor | [Who conducted this assessment] |
| Owner(s) | [Name / Team / Role] |

***

## Scope

- What is being assessed?
- Why now?

***

## Context

<!-- Brief description of what is being assessed and why. -->
[What are we evaluating the risk of? What change, feature, migration, or system is this about? Why does this deserve explicit risk review?]

***

## Risk Summary

[Short high-level summary of the overall risk picture. What is the dominant concern? What is the general posture?]

***

## Risk Inventory

### Risk 1: [Risk Name]

| Dimension | Assessment |
| :--- | :--- |
| Description | [What could go wrong?] |
| Category | [Technical / Security / Data / Performance / Business / Operational / UX / Compliance / Other] |
| Likelihood | [High / Medium / Low] — [Why this rating] |
| Impact | [Critical / High / Medium / Low] — [What happens if it occurs] |
| Risk Score | [Likelihood × Impact: Critical / High / Medium / Low] |
| Consequence | [What is the real-world outcome if this risk materializes?] |
| Why It Matters | [Why this risk deserves attention in this context] |
| Detection | [How would we know this happened? Monitoring, alerts, user reports?] |
| Blast Radius | [How many users/systems affected? Contained or cascading?] |
| Reversibility | [Can we undo the damage? How quickly? At what cost?] |
| Current Mitigation | [What protection already exists?] |
| Additional Mitigation | [What else should be done to reduce this risk?] |
| Mitigation Owner | [Who is responsible for implementing mitigation?] |
| Residual Risk | [After mitigation: what risk remains?] |
| Acceptance Decision | [Accept / Mitigate further / Block — and who decided] |

***

### Risk 2: [Risk Name]

| Dimension | Assessment |
| :--- | :--- |
| Description ||
| Category ||
| Likelihood ||
| Impact ||
| Risk Score ||
| Consequence ||
| Why It Matters ||
| Detection ||
| Blast Radius ||
| Reversibility ||
| Current Mitigation ||
| Additional Mitigation ||
| Mitigation Owner ||
| Residual Risk ||
| Acceptance Decision ||
***

### Risk 3: [Risk Name]

| Dimension | Assessment |
| :--- | :--- |
| Description ||
| Category ||
| Likelihood ||
| Impact ||
| Risk Score ||
| Consequence ||
| Why It Matters ||
| Detection ||
| Blast Radius ||
| Reversibility ||
| Current Mitigation ||
| Additional Mitigation ||
| Mitigation Owner ||
| Residual Risk ||
| Acceptance Decision ||
> Add more risks as needed using the same structure.

***

## Risk Matrix Summary

```text
                    IMPACT
              Low    Medium   High    Critical
         ┌────────┬────────┬────────┬────────┐
  High   │ Medium │  High  │Critical│Critical│
L        ├────────┼────────┼────────┼────────┤
I Medium │  Low   │ Medium │  High  │Critical│
K        ├────────┼────────┼────────┼────────┤
E Low    │  Low   │  Low   │ Medium │  High  │
         └────────┴────────┴────────┴────────┘
```

| Risk | Likelihood | Impact | Score | Matrix Position |
| :--- | :--- | :--- | :--- | :--- |
| [Risk 1] | [L/M/H] | [L/M/H/C] | [Score] | [Position] |
| [Risk 2] | [L/M/H] | [L/M/H/C] | [Score] | [Position] |
| [Risk 3] | [L/M/H] | [L/M/H/C] | [Score] | [Position] |

***

## Highest-Priority Risks

- [Risk 1] — [Why it matters most]
- [Risk 2] — [Why it matters most]

***

## Tradeoffs

- What is being gained?
- What risk is being accepted in exchange?
- [Tradeoff 1]
- [Tradeoff 2]
- [Tradeoff 3]

***

## Reversibility

[How easy is it to undo or recover if something goes wrong? What is the cost and time of recovery?]

***

## Decision Implications

- What should we do differently because of these risks?
- What can proceed now?
- What should be deferred or gated?

***

## Monitoring / Detection Plan

How will emerging or materialized risk be detected?

- [Signal / alert / log / metric 1]
- [Signal 2]
- [Signal 3]

Examples to consider:

- Logs and error rates
- Alerts and thresholds
- Metrics dashboards
- Manual review checkpoints
- Support signals and user reports
- Audit trails

***

## Rollback / Containment Plan

If the risk materializes, what is the fallback or containment plan?

- [Rollback step 1]
- [Rollback step 2]
- [Rollback step 3]

***

## Pre-Mortem Results *(for high-stakes initiatives)*

> "It is 6 months from now and this failed. What went wrong?"

| # | Imagined Failure Scenario | Addressed By Risk # | Additional Action Needed |
| :--- | :--- | :--- | :--- |
| 1 | [Failure scenario] | [Risk #] | [Any gap not covered] |
| 2 | [Failure scenario] | [Risk #] | [Any gap] |
| 3 | [Failure scenario] | [Risk #] | [Any gap] |

***

## Overall Risk Assessment

**Overall Risk Level:** [Low / Medium / High / Critical]

### Recommendation

[Proceed / Proceed with mitigations / Defer until mitigations are in place / Do not proceed]

***

## Conditions for Proceeding

What must be true before this initiative moves forward?

- [ ] [Condition 1]
- [ ] [Condition 2]
- [ ] [Condition 3]

***

## Review Schedule

- **Next review:** [Date or trigger condition]
- **Reassess if:** [Condition that would change the assessment]

- **Review triggers:**
  - Before production rollout
  - After first deployment
  - After traffic reaches threshold
  - After architectural milestone

***

## Related Files

- [contexts/...]
- [workflows/...]
- [templates/...]
- [skills/...]

***

## QUALITY CHECKLIST

Before submitting this risk assessment, verify:

- [ ] Risks are specific — not vague "something might go wrong"
- [ ] Likelihood and impact have reasoning, not just labels
- [ ] Detection method is defined for each risk
- [ ] Blast radius is assessed — not just "it breaks" but "how much breaks"
- [ ] Reversibility is evaluated — can we recover, how fast?
- [ ] Mitigations are actionable with clear owners
- [ ] Residual risk after mitigation is acknowledged
- [ ] Overall recommendation is explicit
- [ ] Pre-mortem was conducted for high-stakes initiatives
- [ ] Review schedule is defined — this is not a one-time document
