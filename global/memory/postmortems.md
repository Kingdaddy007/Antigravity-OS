# MEMORY: POSTMORTEMS

**Version:** Gold v1.0
**Layer:** 12 — Institutional Learning
**Tier:** 3 — Loaded on demand
**File:** memory/postmortems.md
**Purpose:** Post-incident analysis and lessons learned from production incidents. Captures what happened, why, and what systemic changes prevent recurrence. BLAMELESS — focuses on systems, not individuals.
**Loaded When:** Investigating an incident similar to a past one. Reviewing operational readiness or release safety. Improving processes after a failure or near-miss. Onboarding team members to understand operational history.
**Format:** Append-only. Postmortems are permanent records.

---

## WHEN TO ADD AN ENTRY

Add an entry when:

- A P1 or P2 incident occurs — MANDATORY within 48 hours
- A P3 incident reveals a systemic issue worth documenting
- A near-miss occurs that could have been a major incident
- Multiple related minor incidents suggest an underlying pattern
- A failed release or broken migration produced real user impact

Do NOT use for:

- Regular bug documentation — use the debug report template
- Feature retrospectives not related to an incident
- Performance improvement tracking — use `benchmark-results.md`
- Trivial bugs with no lasting structural lesson
- Recurring anti-pattern summaries — those belong in `mistakes-to-avoid.md`

---

## HOW TO USE THIS FILE

Anti-Gravity should consult this file when:

- Investigating an incident that looks similar to a past one
- Reviewing release or operational readiness after a failure
- Debugging repeated problem shapes
- Architecture or process changes are being considered after pain

A postmortem is only useful if it changes future behavior, design, instrumentation, or process. If nothing changes, the lesson was not captured.

---

## BLAMELESS POSTMORTEM PRINCIPLES

1. **Focus on systems, not people.** — "The deployment pipeline did not catch this" — NOT "Developer X did not test properly."
2. **Assume good intent.** — Everyone was trying to do the right thing given what they knew at the time.
3. **Look for structural causes.** — If a person could make this mistake, the system allowed it. Fix the system.
4. **Identify contributing factors, not just root cause.** — Multiple things usually go wrong together.
5. **Action items must be specific, owned, and deadlined.** — "Be more careful" is not an action item.

---

## ENTRY FORMAT

[YYYY-MM-DD] — [Incident Title]

### Severity

[P1 / P2 / P3 / Near-Miss]

### Duration

[When detected → When resolved. Total impact time.]

### Impact

[Who was affected? How many users? What functionality was broken? Any data loss or corruption? Business or operational cost?]

### Detection

[How was this discovered? Alert, user report, or internal observation?]

**Detection gap:** [How long between incident start and detection? Could detection have been faster? How?]

### Timeline

| Time | Event |
| --- | --- |
| [HH:MM] | [What happened] |
| [HH:MM] | [What happened] |
| [HH:MM] | [Incident resolved] |

### Root Cause Analysis

#### What Failed

[Technical description of what went wrong]

#### 5 Whys

1. Why did [symptom] happen? → [cause]
2. Why did [cause] happen? → [deeper cause]
3. Why did [deeper cause] happen? → [structural cause]
4. Why? → [systemic cause]
5. Why? → [organizational or process root]

#### Contributing Factors

- [Factor 1]
- [Factor 2]
- [Factor 3]

#### Why the System Allowed This

[What structural weakness, missing guardrail, or hidden assumption made this possible? Not WHO but WHAT in the system failed to prevent it]

### Resolution

[What was done to fix the immediate incident?]

### What Went Well

- [Positive 1]
- [Positive 2]

### What Went Poorly

- [Problem 1]
- [Problem 2]

### Where We Got Lucky

- [Lucky break 1]

### Action Items

| # | Action | Type | Owner | Deadline | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | [Specific action] | Prevent / Detect / Mitigate | [Who] | [When] | [Status] |
| 2 | [Specific action] | Prevent / Detect / Mitigate | [Who] | [When] | [Status] |
| 3 | [Specific action] | Prevent / Detect / Mitigate | [Who] | [When] | [Status] |

### Action types

- **Prevent** — stop this class of incident from happening
- **Detect** — catch it faster next time
- **Mitigate** — reduce the impact when it happens

### Lessons Learned

[What did this teach us about the system, the process, or prior assumptions? One sentence if possible: what to remember next time.]

Related Files / Areas:

- [debug report / risk assessment / benchmark / workflow / ADR]
- [related module or feature area]

Tags: #database #deployment #auth #performance #infrastructure #monitoring

---

## QUALITY BAR FOR ENTRIES

A strong entry:

- Captures a meaningful failure or near-miss with real structural learning
- Uses the 5 Whys to reach structural and systemic causes, not just the surface event
- Extracts a reusable lesson that changes future behavior or design
- Produces specific, owned, deadlined action items
- Is blameless — focuses on what the system allowed, not who failed

A weak entry:

- Is mostly narrative with no extractable lesson
- Stops at the surface cause without asking why the system allowed it
- Focuses on blame instead of structural improvement
- Has no action items, or action items too vague to execute
- Records something too small or trivial to warrant a postmortem

---

## USAGE RULES

1. Record recurring mistakes and mistakes with real cost — not one-off trivial errors.
2. Focus on mistakes that produced:
   - Real bugs or production incidents
   - Repeated confusion or regressions
   - Security risk or data integrity issues
   - Structural weakness that persisted over time
3. Keep corrective guidance concrete and actionable.
4. Do not delete history silently — if a mistake is no longer relevant, mark it as historical rather than removing it.
5. Use this file to improve future recommendations, reviews, and workflow discipline.
6. Most recent entries appear at the top.

---

## EXAMPLE ENTRY

2024-07-15 — Login Outage Due to Database Connection Exhaustion

### Severity (Example)

P1

### Duration (Example)

22:14 → 22:47 — 33 minutes total impact

### Impact (Example)

All users unable to log in. Approximately 150 active users affected during the window. No data loss or corruption.

### Detection (Example)

Detected via error tracking alert — spike in 500 errors on the login endpoint.

**Detection gap:** approximately 4 minutes from incident start to alert fire.

### Timeline (Example)

| Time | Event |
| --- | --- |
| 22:14 | Traffic spike begins — customer demo driving 3x normal login volume |
| 22:18 | Error tracking fires — 500 errors on login endpoint |
| 22:21 | On-call engineer begins triage |
| 22:28 | Root cause identified — connection pool exhausted |
| 22:31 | Immediate mitigation applied — reduced per-function connection limit |
| 22:47 | Login fully restored and stable |

### Root Cause Analysis (Example)

#### What Failed (Example)

Database connection pool exhausted. Serverless functions each opened their own connection pool without a connection pooler. A traffic spike pushed connections past the RDS maximum limit of 83.

#### 5 Whys (Example)

1. Why could not users log in? → Database connections timed out.
2. Why did connections time out? → All 83 connections were in use.
3. Why were all connections in use? → Each serverless function opens its own pool with no shared pooler.
4. Why no connection pooler? → Never implemented — was not needed at previous scale.
5. Why was the scaling gap not identified? → No monitoring alert on connection count approaching the limit.

#### Contributing Factors (Example)

- No alert on connection count approaching the limit
- Connection limit per function was set higher than necessary
- Traffic spike from customer demo was not anticipated or staged

#### Why the System Allowed This (Example)

The serverless architecture creates a structural connection pool problem that does not exist in traditional server deployments. The system had no protection — no pooler, no alert, no per-function limit matched to the constraint.

### Resolution (Example)

Reduced Prisma connection limit per function immediately as mitigation. PgBouncer implementation planned as structural fix.

### What Went Well (Example)

- Error tracking alert fired within 4 minutes
- On-call engineer identified root cause quickly
- Mitigation was available without redeployment

### What Went Poorly (Example)

- No connection count monitoring or alert existed
- No runbook for this class of incident
- Communication to affected users was delayed

### Where We Got Lucky (Example)

- The traffic spike was during a demo, not a peak business hour
- No data corruption or loss occurred
- The mitigation was reversible

### Action Items (Example)

| # | Action | Type | Owner | Deadline | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Implement connection pooler | Prevent | Backend | 2024-08-01 | In Progress |
| 2 | Add CloudWatch alert at 70% connection usage | Detect | Backend | 2024-07-22 | Done |
| 3 | Reduce per-function connection limit | Mitigate | Backend | 2024-07-16 | Done |

### Lessons Learned (Example)

Serverless architectures require explicit connection pool management that traditional deployments handle automatically — this must be treated as a first-class infrastructure concern, not an afterthought.

Related Files / Areas:

- memory/mistakes-to-avoid.md
- contexts/infra-context.md
- contexts/database-context.md

Tags: #database #infrastructure #scaling #connection-pool

---

## ENTRIES

<!-- Append new entries below this line. Most recent at the top. -->
