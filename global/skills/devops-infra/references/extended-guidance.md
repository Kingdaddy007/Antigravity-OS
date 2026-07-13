# Extended Guidance

## Contents

- [KEY DIAGNOSTIC QUESTIONS](#key-diagnostic-questions)
  - [Before Designing](#before-designing)
  - [During Design](#during-design)
  - [Before Deploying](#before-deploying)
  - [During Incident Response](#during-incident-response)
  - [After Incident](#after-incident)
- [BEHAVIORAL WORKFLOW](#behavioral-workflow)
  - [Phase 1 — Understand](#phase-1-understand)
  - [Phase 2 — Contextualize](#phase-2-contextualize)
  - [Phase 3 — Analyze](#phase-3-analyze)
  - [Phase 4 — Plan](#phase-4-plan)
  - [Phase 5 — Execute](#phase-5-execute)
  - [Phase 6 — Verify](#phase-6-verify)
  - [Phase 7 — Critique](#phase-7-critique)
  - [Phase 8 — Communicate](#phase-8-communicate)
- [NON-NEGOTIABLE CHECKLIST](#non-negotiable-checklist)
  - [Infrastructure as Code](#infrastructure-as-code)
  - [Deployment Pipeline](#deployment-pipeline)
  - [Observability](#observability)
  - [Alerting](#alerting)
  - [Security](#security)
  - [Reliability](#reliability)

## KEY DIAGNOSTIC QUESTIONS

### Before Designing

- What are the reliability and availability requirements? (SLOs)
- What is the team's current operational maturity? What tooling already exists?
- What is the deployment frequency requirement?
- Who will be on call? What is their experience level?
- Are we solving a current problem, or a prestige future problem?

### During Design

- Is this configuration captured in code, or am I configuring something manually that should be codified?
- If this instance dies right now, will it be automatically replaced? How long until recovery?
- Can I trace a single request across all services using the telemetry I am implementing?
- Is every alert I am creating actionable? What is the runbook for each alert?
- Am I storing any secrets outside a dedicated secret management system?
- What is the blast radius if this change fails?

### Before Deploying

- Has this change been tested in staging with production-like configuration?
- What is the rollback plan if this change causes problems?
- Are health checks configured to detect if this change causes degradation?
- Have I reviewed the plan/dry-run output for unexpected changes?

### During Incident Response

- What changed recently? (Deployments, configuration changes, traffic patterns)
- What is the blast radius? Which services, users, and functionality are affected?
- Can the issue be mitigated immediately by rollback, traffic rerouting, or scaling?
- What do the logs and traces show? Can we reconstruct the failing request path?

### After Incident

- What was the root cause? (Not the trigger — the structural reason the system was vulnerable)
- What monitoring or alerting would have detected this earlier?
- What structural change would prevent this class of failure from recurring?
- Has the post-mortem been documented and shared?

---

## BEHAVIORAL WORKFLOW

### Phase 1 — Understand

Clarify the task (IaC, observability, incident, scaling, security hardening, environment consistency). Clarify scope: which services, environments, and systems. Identify what already exists. Identify risks or constraints.

### Phase 2 — Contextualize

Identify existing IaC tooling, CI/CD pipelines, cloud provider, and hosting model. Identify the current observability stack. Understand the secret management approach. Identify the environments and how much they drift. Check whether hidden manual state, snowflake configurations, or undocumented dependencies exist.

### Phase 3 — Analyze

- *For IaC/Delivery:* Map path from code change to production. Identify failures, delays, manual interventions. Evaluate declarativeness and version-control. Design failure domains.
- *For Observability:* Map critical paths. Identify what signals exist at each step. Determine what failures would be invisible. Check whether alerts are symptom-oriented and SLO-linked.
- *For Incident/Audit:* Identify what the team needs to diagnose a bad release. Identify missing evidence or undocumented recovery paths.

### Phase 4 — Plan

Define components to create or modify. Define IaC structure, deployment pipeline stages, observability instrumentation, rollback procedures. Estimate blast radius. Confirm recommendation matches team's operational maturity.

### Phase 5 — Execute

- *5A IaC:* Define all infrastructure as version-controlled code. Organize into reusable modules. Use environment-specific variable files. Apply changes through the pipeline only.
- *5B Deployment Pipeline:* Automate full pipeline (source → build → test → security scan → staging → verify → production → verify). Build immutable artifacts. Implement health checks at each stage. Configure auto-rollback on health check failure. Implement rolling/blue-green/canary strategies. Separate schema migrations from code deployments.
- *5C Structured Logging:* Emit JSON logs with consistent schema (timestamp, level, service, traceId, spanId, message, userId, durationMs). Include trace IDs in every entry. Use canonical log lines. Scrub PII before ingestion.
- *5D Distributed Tracing:* Inject unique trace ID at entry point. Propagate through every downstream service, DB query, and external API call. Include trace ID in all log entries and error responses.
- *5E Metrics & Alerting:* Define core metrics: error rate, latency (p50/p95/p99), throughput, availability, saturation. Define SLOs. Alert on SLO violations only. Require runbook for every alert. Review and prune alerts quarterly.
- *5F Secret Management:* Store all secrets in dedicated secret management system. Never commit to repos. Configure apps to retrieve secrets at runtime. Implement 90-day max rotation. Audit access. Implement least-privilege.
- *5G Disaster Recovery:* Configure automated backups. Test restoration on a quarterly schedule. Define RTO and RPO. Document DR as step-by-step runbook. Practice DR drills.
- *5H Incident Readiness:* Create runbooks for common critical failures. Ensure releases and incidents can be traced to code/infra/config/dependency changes. Document blameless postmortems.

### Phase 6 — Verify

IaC applies cleanly (plan/dry-run). Pipeline completes end-to-end. Health checks correctly distinguish healthy from unhealthy. Rollback works (intentionally deploy failing version, confirm auto-rollback). Logs are structured and searchable. Alerts fire when SLOs are violated. Secrets not exposed in logs or config files. Environment parity confirmed. Backups restore successfully.

### Phase 7 — Critique

Is any infrastructure component only manual config? If primary AZ went down, how long until recovery — tested? Are all alerts actionable? Is the pipeline fast enough? Are there unaddressed single points of failure? Is the on-call experience sustainable? Is rollback real and tested, or just imagined?

### Phase 8 — Communicate

Lead with operational reality. Explain the recommended delivery/observability/runtime design. Make tradeoffs explicit. Document rollout, rollback, and monitoring implications. Identify known gaps. Define next steps.

---

## NON-NEGOTIABLE CHECKLIST

### Infrastructure as Code

- [ ] All infrastructure configuration defined in version-controlled code
- [ ] No manual configuration that is not captured in code
- [ ] IaC code reviewed with the same rigor as application code
- [ ] Changes applied through the pipeline — not from local machines
- [ ] State management (remote state, locking) configured to prevent concurrent conflicts
- [ ] Environment differences managed through parameterization, not separate codebases

### Deployment Pipeline

- [ ] Pipeline fully automated from commit to production
- [ ] Build artifacts are immutable — same artifact promoted through all environments
- [ ] Automated tests run on every commit and block merges on failure
- [ ] Health checks gate promotion between deployment stages
- [ ] Rollback automated or executable in under 5 minutes
- [ ] Schema migrations and code deployments decoupled

### Observability

- [ ] Logs structured (JSON) with consistent field schemas across all services
- [ ] Trace IDs injected at entry point and propagated through all downstream services
- [ ] Metrics capture error rate, p95/p99 latency, throughput, and resource utilization
- [ ] PII scrubbed from all log output before ingestion
- [ ] Dashboards exist for core service-level metrics

### Alerting

- [ ] Alerts defined on user-facing symptoms — not system-level causes
- [ ] Every alert has a documented runbook with response steps
- [ ] No alerts routinely ignored (alert fatigue addressed)
- [ ] Alert thresholds based on SLO definitions, not arbitrary round numbers

### Security

- [ ] All secrets in a dedicated secret management system — not in code, env files, or chat
- [ ] Secret rotation configured on a defined schedule
- [ ] Production access restricted to minimum necessary set of people
- [ ] SSH access to production disabled or audited

### Reliability

- [ ] Health checks and readiness probes configured and verified
- [ ] Circuit breakers implemented between services to prevent cascading failure
- [ ] Disaster recovery tested in the last 90 days
- [ ] Backups restoration tested successfully
