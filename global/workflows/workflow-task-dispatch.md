---
id: task-dispatch
version: 1
status: active
intent: Execute task dispatch with explicit authority, state, outputs, and evidence.
use_when: [the task matches task dispatch]
do_not_use_when: [another workflow more precisely matches the requested outcome]
inputs: [user objective, workspace context, constraints, requested authority mode]
required_resources: [applicable AGENTS.md files, referenced skills and contexts]
mutation_class: local_edit
approval_gates: [confirm scope expansion or destructive action before mutation]
states: [intake, assess, propose, approve-if-needed, execute-if-authorized, verify, deliver]
outputs: [task result, changed-artifact list when applicable, evidence, residual risks]
verification: [run proportionate checks, record raw evidence, label anything unverified]
failure_paths: [stop on authority or contract conflict, preserve state, report blocker and safe next action]
resume_contract: task-scoped .agents/workflows/task-dispatch.json using the workflows directory contract
next_workflows: [none]
profiles: [general]
---

# WORKFLOW: TASK DISPATCH (ORCHESTRATION)

**Version:** Gold v1.2
**Layer:** 7 — Orchestration Workflow
**Tier:** 2 — Loaded by task
**Primary Mode:** Architect / Orchestrator
**Purpose:** Handles the safe handoff of isolated micro-tasks to separate chat sessions or subagents.

## WHEN TO USE

Use this workflow when you have broken down an implementation plan into micro-tasks, and one or more of those tasks is highly isolated, tedious, or time-consuming.

Instead of doing it all in one long, sequential, context-bloating session, you act as the Orchestrator and dispatch the work.

## THE DISPATCH PROCESS

### 1. Identify Dispatchable Tasks

A task is dispatchable if:

- It is highly isolated (e.g., writing tests for a pure function, styling a simple component, writing documentation).
- It does not require deep knowledge of the entire system architecture.
- Its inputs and expected outputs are clear.
- Its blocking edges are known and it does not overlap another worker's file ownership.
- It can return useful evidence independently. Task count alone is never a reason to dispatch.

### 2. Prepare the Task Brief

For each task, create a task ID and self-contained brief. Use available subagent tooling directly when authorized and available; otherwise present the brief for a separate session.

### Format

```

## Task Brief: [Task Name]

**Goal:** [What needs to be achieved]
**Inputs:** [Specific files to read or APIs to use]
**Expected Outputs:** [Specific files to write or changes to make]
**Constraints:** [Formatting rules, performance needs, etc.]
**Verification:** [How the new agent should prove it works]
**Context Needed:** [A 1-2 sentence summary of what the agent needs to know]
**Blocked By / Blocks:** [Task IDs]
**Owned Files:** [Exclusive write scope; overlaps are forbidden]
**Authority Mode:** [diagnose / propose / implement]
**Return Contract:** [Touched files, commands, raw evidence, assumptions, residual risks]
```

### 3. Handoff

Dispatch only tasks whose dependencies are satisfied. Record task ID, worker ID, status, ownership, and expected evidence in the task-scoped workflow state. Limit concurrency to the available platform slots and useful independent work; never create workers merely to appear parallel.

### 4. Re-integration

When a worker or sub-session returns:

1. Review the changes made (using git status/diff or by reading the touched files).
2. Verify the subagent followed the brief and didn't break adjacent behavior.
3. Mark the task as complete in your master checklist.
4. Proceed to the next task.
5. On failure or timeout, preserve evidence, release ownership, and either retry with a narrower brief or return the task to the orchestrator.

## WHY WE DO THIS

- **Context Protection:** Complex tasks bloat context windows. Splitting them saves tokens and prevents hallucination.
- **Parallelization:** The user can have multiple agents working on isolated tasks simultaneously.
- **Focus:** The master agent (you) stays focused on the big picture, architecture, and integration.
