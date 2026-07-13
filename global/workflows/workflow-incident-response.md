---
id: incident-response
version: 1
status: active
intent: Coordinate evidence-led production incident triage, authorized mitigation, recovery, and learning.
use_when: [active production outage, data-integrity threat, severe security or availability incident]
do_not_use_when: [local debugging, non-production bug, planned deployment]
inputs: [observed impact, affected environment, available telemetry, responders and authority]
required_resources: [infra context, security baseline when relevant, service runbooks, monitoring access]
mutation_class: external_or_production
approval_gates: [explicit incident-mitigate authority before external mutation, target and rollback confirmation]
states: [declare, stabilize, investigate, authorize-mitigation, mitigate, verify-recovery, monitor, close, learn]
outputs: [incident record, timeline, evidence log, mitigation record, recovery proof, follow-up actions]
verification: [impact metrics return to baseline, critical user path check, data-integrity check, observation window]
failure_paths: [escalate when authority is absent, preserve evidence, prefer containment when rollback is unsafe]
resume_contract: task-scoped .agents/workflows/incident-response.json using the workflows directory contract
next_workflows: [debug-issue, security-audit, ship-to-production]
profiles: [general]
---

# WORKFLOW: INCIDENT RESPONSE

## Authority Modes

- **Observe:** gather evidence and report only.
- **Propose mitigation:** compare containment, rollback, traffic shift, and feature-flag options.
- **Incident-mitigate:** execute only after just-in-time approval identifies environment, action, expected effect, containment or rollback, and evidence owner.

## Sequence

1. Declare incident urgency as `SEV-1`, `SEV-2`, `SEV-3`, or `SEV-4`; record impact rather than guessing cause.
2. Assign incident lead, communications owner, investigator, and operations executor when available.
3. Preserve logs, timestamps, changes, and hypotheses. Establish a pre-mitigation baseline.
4. Propose the smallest reversible mitigation. Separate mitigation from root-cause correction.
5. Obtain explicit mutation authority, then execute one controlled change at a time.
6. Verify recovery against baseline and critical user paths; monitor through a declared observation window.
7. Close only when impact is stable, ownership is clear, and evidence is recorded.
8. Continue root-cause work through `workflow-debug-issue`; create a blameless postmortem for SEV-1/2.

