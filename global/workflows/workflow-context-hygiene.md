---
description:  The systematic sequence for cleanly wrapping up a long conversation, securing all state and memory to disk, and preparing the workspace for a fresh context window
id: context-hygiene
version: 1
status: active
intent: Execute context hygiene with explicit authority, state, outputs, and evidence.
use_when: [the task matches context hygiene]
do_not_use_when: [another workflow more precisely matches the requested outcome]
inputs: [user objective, workspace context, constraints, requested authority mode]
required_resources: [applicable AGENTS.md files, referenced skills and contexts]
mutation_class: local_edit
approval_gates: [confirm scope expansion or destructive action before mutation]
states: [intake, assess, propose, approve-if-needed, execute-if-authorized, verify, deliver]
outputs: [task result, changed-artifact list when applicable, evidence, residual risks]
verification: [run proportionate checks, record raw evidence, label anything unverified]
failure_paths: [stop on authority or contract conflict, preserve state, report blocker and safe next action]
resume_contract: task-scoped .agents/workflows/context-hygiene.json using the workflows directory contract
next_workflows: [none]
profiles: [general]
---

# Workflow: Context Hygiene

**Description:** The systematic sequence for cleanly wrapping up a long conversation, securing all state and memory to disk, and preparing the workspace for a fresh context window.

## Phase 1: Secure Long-Term Knowledge

- Identify any architectural decisions made in this session and log them to `.agents/memory/decisions-log.md`.
- Identify any mistakes, failed approaches, or dead-ends, and log them to `.agents/memory/mistakes-to-avoid.md`.
- Identify any new conventions or reusable code patterns and log them to `.agents/memory/common-patterns.md`.

## Phase 2: Secure Immediate State

- Read `.agents/workflows/<task-id>.json` and select the record matching the active `task_id`; do not overwrite another task's state.
- Update `workflow_id`, `mode`, `status`, `current_state`, `completed_states`, and timestamps.
- Record exactly what finished and what resumes next in `next_action`.
- Update `artifacts`, `evidence`, `approvals`, and `blockers` from the session.
- Write the updated JSON back to disk.

## Phase 3: Verification & Handoff

- Verify that both the `.agents/memory/` markdown files and `.agents/workflows/<task-id>.json` have been successfully updated.
- Output a final summary to the user detailing exactly what was saved.
- Formally advise the user to close this chat and open a new window to continue the sprint with maximum sharpness.
