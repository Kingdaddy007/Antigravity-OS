# INFRA CONTEXT

**Version:** Gold v1.2 (Master Merge)
**Layer:** 6 — Context (Ground Truth)
**Tier:** 2 — Loaded by task
**File:** contexts/infra-context.md
**Purpose:** Defines hosting, deployment, environments, monitoring, observability, incident response, and operational infrastructure. Anti-Gravity uses this to make recommendations compatible with YOUR operational reality — not theoretical best practices.
**Loaded When:** Deployment discussions, infrastructure changes, incident response, performance investigation, DevOps work, CI/CD modifications, or any task affecting runtime behavior.
**Maintenance:** Update when infrastructure changes, new monitoring is added, CI/CD pipeline changes, or incident response procedures evolve. Review quarterly.

---

## HOW ANTI-GRAVITY USES THIS FILE

This file maps the operational reality of your application. It tells Anti-Gravity where things run, how they deploy, how they are monitored, and what to do when things break.

All deployment, performance, reliability, and production advice should respect the actual runtime and infrastructure reality of this system — not an imagined ideal platform. If a recommendation depends on stronger infrastructure capabilities than currently exist, that gap must be stated explicitly rather than assumed away.

**When loaded**, Anti-Gravity will:

- Suggest solutions compatible with YOUR hosting constraints such as serverless timeout limits and cold start behavior
- Reference YOUR CI/CD pipeline when discussing deployment
- Recommend monitoring and alerting improvements based on YOUR current observability gaps
- Follow YOUR incident response procedures when discussing error handling
- Respect YOUR environment architecture when suggesting configuration changes
- Know YOUR scaling limits and plan recommendations within them
- Treat environment differences as serious context, especially in debugging
- Make operational constraints visible when they affect architecture or implementation advice

**When missing or incomplete**, Anti-Gravity will:

- Suggest infrastructure patterns that may not work on your hosting platform
- Miss deployment constraints such as timeout limits and cold starts
- Not know your monitoring stack, leading to generic observability advice
- Suggest incident response approaches that conflict with your team's procedures
- Assume production behaves like local by default

**When stale**, Anti-Gravity will:

- Reference deprecated infrastructure components
- Miss new monitoring or alerting tools that have been added
- Suggest deployments through old pipeline configurations
- Not account for capacity changes such as upgraded instances or new services

---

## INFRA SUMMARY

<!-- Fill in a short summary of the actual infrastructure reality.

Template:
The system is deployed on [platform/runtime] using [deployment method].
Core runtime dependencies include [database, cache, queue, object
storage, third-party systems].
Deployments are managed through [CI/CD tool or process], and
observability currently relies on [logs, metrics, traces, tooling].
Operational maturity is currently [early / moderate / mature / mixed].

Example:
The system runs in AWS ECS using Docker containers, with PostgreSQL,
Redis, and S3 as core dependencies. Deployments happen through GitHub
Actions, and observability is split between CloudWatch logs, Sentry
for app errors, and limited metrics dashboards. Infra maturity is
moderate, but rollback and tracing are still uneven.
-->

[Fill in]

---

## HOSTING ARCHITECTURE

<!-- WHY THIS MATTERS: Anti-Gravity needs to understand the physical
     and logical architecture to make compatible recommendations.
     Serverless has different constraints than containers. Managed
     services have different failure modes than self-hosted. -->

### Architecture Diagram

```text
┌─────────────────────────────────────────────────────────┐
│                        INTERNET                         │
└──────────────┬──────────────────────────┬───────────────┘
               │                          │
               ▼                          ▼
   ┌───────────────────┐      ┌───────────────────┐
   │   CDN / Edge      │      │  External Services │
   │   (SSL + Cache)   │      │  (Webhooks IN)     │
   └─────────┬─────────┘      └─────────┬──────────┘
             │                          │
             ▼                          ▼
┌────────────────────────────────────────────────────────┐
│                   APPLICATION LAYER                    │
│                                                        │
│   ┌──────────────┐  ┌──────────────┐  ┌────────────┐  │
│   │  Web App     │  │  API Routes  │  │  Webhook   │  │
│   │              │  │              │  │  Handlers  │  │
│   └──────┬───────┘  └──────┬───────┘  └─────┬──────┘  │
│          └─────────────────┴────────────────┘         │
│                             │                          │
└─────────────────────────────┼──────────────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
   │   Database   │  │    Cache     │  │   Storage    │
   │  PostgreSQL  │  │    Redis     │  │     S3       │
   └──────────────┘  └──────────────┘  └──────────────┘
```

[Fill in your actual architecture diagram]

### Component Details

| Component | Provider | Service / Tier | Region | Key Constraints |
| --- | --- | --- | --- | --- |
| Application | [provider] | [service] | [region] | [constraints] |
| Database | [provider] | [service] | [region] | [constraints] |
| Cache | [provider] | [service] | [region] | [constraints] |
| File Storage | [provider] | [service] | [region] | [constraints] |
| Email | [provider] | [service] | — | [constraints] |
| Error Tracking | [provider] | [service] | — | [constraints] |
| DNS | [provider] | [service] | — | [constraints] |

---

## ENVIRONMENTS

### Environment Overview

| Environment | Host | URL | Database | Purpose | Deploy Trigger |
| --- | --- | --- | --- | --- | --- |
| Local | Developer machine | localhost:3000 | [local DB] | Development | Manual |
| Preview | [host] | [url pattern] | [database] | PR preview | Auto on PR |
| Staging | [host] | [url] | [database] | Pre-production | Auto on merge |
| Production | [host] | [url] | [database] | Live users | Manual promotion |

### Environment Rules

| Rule | Why |
| --- | --- |
| [rule 1] | [reason] |
| [rule 2] | [reason] |
| [rule 3] | [reason] |

### Environment Parity

| Aspect | Local | Staging | Production | Parity? |
| --- | --- | --- | --- | --- |
| Database engine | [version] | [version] | [version] | ✅ / ⚠️ |
| Cache version | [version] | [version] | [version] | ✅ / ⚠️ |
| Node.js version | [version] | [version] | [version] | ✅ / ⚠️ |
| Email sending | [behavior] | [behavior] | [behavior] | ✅ / ⚠️ |
| Payments | [behavior] | [behavior] | [behavior] | ✅ / ⚠️ |
| File storage | [behavior] | [behavior] | [behavior] | ✅ / ⚠️ |

### Works Locally But Not In Production Traps

- [trap 1]
- [trap 2]
- [trap 3]

### Known Environment Drift or Risks

- [risk 1]
- [risk 2]

### Guidance for Anti-Gravity (Environments)

- Do not suggest "works locally" as meaningful proof when environment gaps exist
- Use environment differences explicitly when debugging or recommending rollout paths
- Do not assume local behavior equals production behavior

---

## CI/CD PIPELINE

### PR Created or Updated

```text
┌─────────────────────────────────────────────────────────────────┐
│                     PR CREATED / UPDATED                        │
│                                                                 │
│  ┌──────────────┐  ┌───────────────┐  ┌──────────────────┐     │
│  │  Type Check  │  │  Lint         │  │  Build Check     │     │
│  │  [duration]  │  │  [duration]   │  │  [duration]      │     │
│  └──────┬───────┘  └──────┬────────┘  └────────┬─────────┘     │
│         │                 │                    │               │
│         └─────────────────┴────────────────────┘               │
│                                │                               │
│                                ▼                               │
│         ┌──────────────────────────────────────────┐           │
│         │     Unit + Integration Tests             │           │
│         │     [duration]                           │           │
│         └──────────────────────┬───────────────────┘           │
│                                │                               │
│                                ▼                               │
│         ┌──────────────────────────────────────────┐           │
│         │     Preview Deploy                       │           │
│         │     [duration]                           │           │
│         └──────────────────────────────────────────┘           │
│                                                                 │
│         ALL CHECKS MUST PASS TO MERGE                          │
└─────────────────────────────────────────────────────────────────┘
```

### Merge to Main

```text
┌─────────────────────────────────────────────────────────────────┐
│                        MERGE TO MAIN                            │
│                                                                 │
│         ┌──────────────────────────────────────────┐           │
│         │     All PR checks re-run                 │           │
│         └──────────────────────┬───────────────────┘           │
│                                │                               │
│                                ▼                               │
│         ┌──────────────────────────────────────────┐           │
│         │     E2E Tests                            │           │
│         │     [duration]                           │           │
│         └──────────────────────┬───────────────────┘           │
│                                │                               │
│                                ▼                               │
│         ┌──────────────────────────────────────────┐           │
│         │     Auto-deploy to STAGING               │           │
│         └──────────────────────────────────────────┘           │
│                                                                 │
│         E2E MUST PASS — BLOCKS STAGING DEPLOY IF FAILED        │
└─────────────────────────────────────────────────────────────────┘
```

### Production Deploy (Manual)

```text
┌─────────────────────────────────────────────────────────────────┐
│                   PRODUCTION DEPLOY (Manual)                    │
│                                                                 │
│         ┌──────────────────────────────────────────┐           │
│         │     Manual trigger                       │           │
│         │     [describe how — GitHub Action / etc] │           │
│         └──────────────────────┬───────────────────┘           │
│                                │                               │
│                                ▼                               │
│         ┌──────────────────────────────────────────┐           │
│         │     Smoke tests against staging          │           │
│         │     (verify staging healthy first)       │           │
│         └──────────────────────┬───────────────────┘           │
│                                │                               │
│                                ▼                               │
│         ┌──────────────────────────────────────────┐           │
│         │     Promote to production                │           │
│         └──────────────────────────────────────────┘           │
│                                                                 │
│         REQUIRES: approval from engineer who is NOT PR author  │
└─────────────────────────────────────────────────────────────────┘
```

### Pipeline Time Budgets

| Stage | Current Duration | Budget | If Exceeded |
| --- | --- | --- | --- |
| PR checks total | [duration] | [target] | [action] |
| E2E tests | [duration] | [target] | [action] |
| Full pipeline PR to staging | [duration] | [target] | [action] |
| Production deploy | [duration] | [target] | [action] |

### Pipeline Rules

| Rule | Why |
| --- | --- |
| All CI checks must pass before merge | No exceptions. Broken builds on main break everyone. |
| E2E failures block staging deploy | Prevents known-broken code from reaching staging |
| Production deploy requires human approval | Deliberate decision to ship. Safety net. |
| [rule 4] | [reason] |
| [rule 5] | [reason] |

### Guidance for Anti-Gravity (CI/CD)

- Recommendations about release confidence should reflect what CI actually enforces
- If CI does not protect something important, mention it
- Do not assume a gate exists unless it is listed here

---

## INFRASTRUCTURE COMPONENTS

### Core Runtime Components

| Component | Technology | Notes |
| --- | --- | --- |
| Web app | [tech] | [notes] |
| Database | [tech] | [notes] |
| Cache | [tech] | [notes] |
| Queue | [tech] | [notes] |
| Object storage | [tech] | [notes] |
| Worker / cron | [tech] | [notes] |
| Auth provider | [tech] | [notes] |

### External Services and Providers

- [service 1]
- [service 2]
- [service 3]

### Critical Dependencies

- [dependency 1]
- [dependency 2]
- [dependency 3]

---

## MONITORING AND OBSERVABILITY

### Current Monitoring Stack

| Layer | Tool | What It Covers | Alert Channel |
| --- | --- | --- | --- |
| Error tracking | [tool] | [coverage] | [channel] |
| Frontend performance | [tool] | [coverage] | [channel] |
| Database monitoring | [tool] | [coverage] | [channel] |
| Cache monitoring | [tool] | [coverage] | [channel] |
| Uptime monitoring | [tool] | [coverage] | [channel] |
| Application logs | [tool] | [coverage] | [channel] |

### Logging Conventions

| Convention | Implementation |
| --- | --- |
| Log format | [format] |
| Log levels | [levels] |
| Required fields | [fields] |
| Sensitive data rules | [rules] |
| Request correlation | [approach] |
| Error logging requirements | [requirements] |

### What We CAN Observe Currently

- ✅ [observable 1]
- ✅ [observable 2]
- ✅ [observable 3]

### Observability Gaps — What We CANNOT Observe

| Gap | Impact | Why It Exists | Plan |
| --- | --- | --- | --- |
| [gap 1] | [impact] | [reason] | [plan] |
| [gap 2] | [impact] | [reason] | [plan] |
| [gap 3] | [impact] | [reason] | [plan] |

### Guidance for Anti-Gravity (Monitoring)

- Observability recommendations should fit what exists
- If tracing is weak, say so explicitly
- If logging exists but is unstructured or low-signal, do not call that good observability
- If customer report is the main detection path, treat that as low maturity
- Do not assume observability maturity that does not exist

---

## INCIDENT RESPONSE

### On-Call Structure

| Setting | Value |
| --- | --- |
| Rotation | [describe] |
| Schedule tool | [tool] |
| Primary contact | [method] |
| Escalation path | [describe] |

### Severity Levels

| Level | Definition | Example | Response Time | Resolution Target |
| --- | --- | --- | --- | --- |
| P1 — Critical | Service down or data integrity at risk | [example] | [time] | [target] |
| P2 — Major | Major feature broken, many users affected | [example] | [time] | [target] |
| P3 — Minor | Minor feature broken, workaround exists | [example] | [time] | [target] |
| P4 — Cosmetic | Visual issue, no functional impact | [example] | [time] | [target] |

### Incident Workflow

```text
DETECT
  │
  ▼
Alert fires or user report received
On-call engineer acknowledges within response time
  │
  ▼
ASSESS
  │
  ├── Determine severity (P1 / P2 / P3 / P4)
  ├── Identify blast radius (how many users affected?)
  └── Communicate status in [Slack channel or equivalent]
  │
  ▼
MITIGATE
  │
  ├── P1/P2: Can we rollback?
  ├── P1/P2: Can we disable the broken feature?
  └── P3/P4: Document and schedule fix
  │
  ▼
FIX
  │
  ├── Root cause analysis
  ├── Targeted fix with regression test
  └── Deploy through normal pipeline (hotfix for P1/P2)
  │
  ▼
REVIEW
  │
  ├── P1/P2: Post-mortem required within 48 hours
  ├── Timeline, Impact, Root Cause, Contributing Factors,
  │   Action Items with owners and deadlines
  └── Blameless culture — focus on systems, not individuals
```

### Rollback Procedure

| Method | How | Time | When to Use |
| --- | --- | --- | --- |
| [method 1] | [how] | [time] | [when] |
| [method 2] | [how] | [time] | [when] |
| [method 3] | [how] | [time] | [when] |

---

## SCALING CONSTRAINTS AND PLAN

### Current Capacity Estimates

| Component | Current Capacity | Current Usage Peak | Bottleneck Threshold | Scaling Trigger |
| --- | --- | --- | --- | --- |
| Application | [capacity] | [usage] | [threshold] | [trigger] |
| Database | [capacity] | [usage] | [threshold] | [trigger] |
| Cache | [capacity] | [usage] | [threshold] | [trigger] |
| Background jobs | [capacity] | [usage] | [threshold] | [trigger] |
| File storage | [capacity] | [usage] | [threshold] | [trigger] |
| Email | [capacity] | [usage] | [threshold] | [trigger] |

### Scaling Playbook

| Traffic Threshold | Expected Bottleneck | Action | Estimated Cost Impact |
| --- | --- | --- | --- |
| [threshold 1] | [bottleneck] | [action] | [cost] |
| [threshold 2] | [bottleneck] | [action] | [cost] |
| [threshold 3] | [bottleneck] | [action] | [cost] |
| [threshold 4] | [bottleneck] | [action] | [cost] |
| [threshold 5] | [bottleneck] | Full architecture review | Significant investment |

---

## DISASTER RECOVERY

| Scenario | Recovery Method | RTO | RPO | Last Tested |
| --- | --- | --- | --- | --- |
| Application deployment failure | [method] | [time] | [data loss] | [date] |
| Database corruption | [method] | [time] | [data loss] | [date] |
| Database instance failure | [method] | [time] | [data loss] | [date] |
| Cache failure | [method] | [time] | [data loss] | [date] |
| File storage loss | [method] | [time] | [data loss] | [date] |
| Full region outage | [method] | [time] | [data loss] | [date] |

### DR Gaps

| Gap | Risk Level | Plan |
| --- | --- | --- |
| [gap 1] | [low/medium/high] | [plan] |
| [gap 2] | [low/medium/high] | [plan] |
| [gap 3] | [low/medium/high] | [plan] |

---

## COST MANAGEMENT

### Current Monthly Infrastructure Costs

| Service | Current Cost | Growth Driver |
| --- | --- | --- |
| [service 1] | [cost] | [driver] |
| [service 2] | [cost] | [driver] |
| [service 3] | [cost] | [driver] |
| [service 4] | [cost] | [driver] |
| **Total** | **[total]** ||

### Cost Constraints

- Total infrastructure budget: [amount per month]
- Any single service addition above [threshold] requires team discussion
- [other constraint]

---

## CONFIG AND SECRETS MANAGEMENT

### How Secrets Are Managed

[Fill in]

### Who Has Access to What

| Environment | Who Has Access | How Access Is Granted |
| --- | --- | --- |
| Production | [who] | [how] |
| Staging | [who] | [how] |
| Local | [who] | [how] |

### Config Notes

- [note 1]
- [note 2]

### Guidance for Anti-Gravity (Secrets)

- Recommendations must respect how config is actually managed
- Treat secret handling as part of infra reality, not an afterthought
- If config drift or secret inconsistency is known, surface it

---

## INFRASTRUCTURE AS CODE REALITY

### Current IaC Maturity

[Fill in]

### IaC Notes

- [note 1]
- [note 2]

### Guidance for Anti-Gravity (IaC)

- If infra is not fully codified, do not assume reproducibility is strong
- If click-ops reality exists, flag the operational risk rather than normalizing it
- If recommending new infra, consider whether the team can actually maintain it at current maturity

---

## OPERATIONAL RUNBOOKS

### Common Operational Tasks

| Task | How To Do It | When |
| --- | --- | --- |
| Deploy to production | [steps] | [when] |
| Rollback production | [steps] | [when] |
| Clear cache | [steps] | [when] |
| Run database migration | [steps] | [when] |
| Manual data fix | [steps] | [when] |
| Rotate API keys | [steps] | [when] |
| Check database performance | [steps] | [when] |
| View application errors | [steps] | [when] |
| Seed staging database | [steps] | [when] |

### Runbook Rules

| Rule | Description |
| --- | --- |
| Data Backup | All production data operations require a backup or snapshot first |
| Testing | All manual fixes must be scripted, reviewed, and tested on staging before running on production |
| Connection | No direct database connections to production without documented reason |
| Logging | Operational actions are logged in [channel] for team visibility |

---

## KNOWN OPERATIONAL PAIN POINTS

| Pain Point | Impact | Status |
| --- | --- | --- |
| [pain point 1] | [impact] | [tolerated / being addressed] |
| [pain point 2] | [impact] | [tolerated / being addressed] |
| [pain point 3] | [impact] | [tolerated / being addressed] |

---

## INFRASTRUCTURE ANTI-PATTERNS

### Manual-ops fantasy

**What it looks like:** Designing operations as if manual environment edits, tribal deployment knowledge, and person-dependent workflows are acceptable defaults.
**Why it is harmful:** Creates fragile systems that cannot scale safely.
**What to do instead:** Preserve reproducibility, reviewability, and explicit operational procedure as defaults.

### Premature platform lock-in

**What it looks like:** Casually assuming one provider, tool, or orchestration model as if the decision has already been made.
**Why it is harmful:** Narrows future architecture options without explicit project agreement.
**What to do instead:** Label concrete platforms explicitly as examples, recommendations, or locked decisions.

### Invisible runtime assumptions

**What it looks like:** Deployment or monitoring guidance that only works under one unstated platform model.
**Why it is harmful:** Makes documents look general while hiding constraint-specific logic.
**What to do instead:** Surface assumptions whenever guidance depends on a specific runtime model.

### Delivery without operability

**What it looks like:** Discussing deployment paths without considering rollback, observability, incident diagnosis, or release safety.
**Why it is harmful:** Creates infrastructure plans that are optimistic but not survivable.
**What to do instead:** Treat run, observe, recover, and change as one operational system.

### Complexity beyond team maturity

**What it looks like:** Recommending infra patterns the current team cannot realistically operate or maintain.
**Why it is harmful:** Creates operational burden that exceeds capacity and leads to fragility.
**What to do instead:** Recommend proportionate improvements that fit current team size and maturity.

---

## WHAT GOOD OPERATIONS LOOKS LIKE IN THIS PROJECT

Operations are in good shape when:

- deploys are predictable and low-drama
- runtime behavior is observable enough to debug incidents without guesswork
- environment differences are known and managed explicitly
- rollback is feasible and practiced, not theoretical
- critical dependencies are visible and monitored
- logs are useful without leaking sensitive data
- changes are traceable from code to runtime
- operators can regain control without heroics
- incident detection does not depend on customer reports
- post-mortems produce real action items with owners

Operations are not in good shape when:

- manual steps are required and undocumented
- an incident requires tribal knowledge to diagnose
- rollback requires a hotfix instead of a revert
- observability gaps mean flying blind in production
- environment drift creates production-only surprises

---

## OPEN INFRA QUESTIONS

- [question 1]
- [question 2]
- [question 3]

---

## CROSS-REFERENCES

| Related Context File | Relationship |
| --- | --- |
| `stack-context.md` | Technology choices implemented on this infrastructure |
| `architecture-context.md` | Application architecture deployed on this infrastructure |
| `database-context.md` | Database hosting, backups, and performance |
| `security-baselines.md` | Infrastructure security, secret management, compliance |
| `testing-standards.md` | CI/CD pipeline test requirements |
| `business-priorities.md` | Infrastructure investment priorities |
| `coding-standards.md` | CI pipeline enforces coding standards |

---

## FINAL RULE

All deployment, performance, reliability, and production advice should respect the actual runtime and infrastructure reality of this system — not an imagined ideal platform.

If a recommendation depends on stronger infrastructure capabilities than currently exist, that gap must be stated explicitly rather than assumed away.
