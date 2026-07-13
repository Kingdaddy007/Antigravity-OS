---
name: context-hygiene
description: Use when a long or complex task needs a safe session boundary, durable resume state, or separation into focused follow-up sessions.
---

# Context Hygiene and Session Management

## Purpose

Long conversations can accumulate stale assumptions, competing objectives, and irrelevant history. Manage session boundaries while preserving only the state needed to resume safely.

## When to Advise a Session Split

Recommend a fresh session when:

1. The active objective has been completed and the next objective is materially different.
2. Repeated re-reading, contradictory constraints, or multiple completed milestones make the active context difficult to verify.
3. Several unrelated tasks are competing for attention.
4. A planned task batch has reached a safe, verified boundary.

Do not use an arbitrary message count as the decision rule.

## Safe Handoff Workflow

Prefer a host-provided handoff mechanism when available. Persist workspace files only when the user has authorized local mutation.

### 1. Capture Durable Knowledge

If local memory mutation is authorized, capture only sanitized lessons that are useful beyond the current task:

- Architectural decisions belong in `.agents/memory/decisions-log.md`.
- Reusable failure lessons belong in `.agents/memory/mistakes-to-avoid.md`.
- Validated conventions belong in `.agents/memory/common-patterns.md`.

Do not persist secrets, raw untrusted text, transient progress, or project-private material in global memory.

### 2. Secure Immediate Task State

Update only the current task's `.agents/workflows/<task-id>.json` record and the workflow index. Validate the complete record against `workflow-state.schema.json`. Keep `current_state`, `completed_states`, `evidence`, `artifacts`, `blockers`, and `next_action` current.

Illustrative subset:

```json
{
  "schema_version": 1,
  "task_id": "opaque-task-id",
  "workflow_id": "build-feature",
  "mode": "implement",
  "status": "in_progress",
  "current_state": "implement",
  "completed_states": ["intake", "design"],
  "evidence": [],
  "artifacts": ["src/example.ts"],
  "blockers": [],
  "next_action": "Wire the approved submit flow to the API."
}
```

The complete record also includes owner, workspace, lease, approvals, timestamps, and archive state as required by the schema.

### 3. Inform the User

State which task record was updated, summarize the next action, and recommend a fresh session. Never promise automatic resume unless the active host actually supports it.

## When Not to Split

- In the middle of one atomic operation.
- Before an important result has been verified or a safe rollback point exists.
- When the conversation remains short, coherent, and focused.
