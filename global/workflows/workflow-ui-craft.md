---
id: ui-craft
version: 1
status: active
intent: Build a general product or application interface from an approved flow and state contract.
use_when: [implementing a SaaS screen, dashboard, application flow, form, settings surface, or general product interface]
do_not_use_when: [the request is spatial-profile work, the task is design-only with no implementation authority, the task is backend-only]
inputs: [user objective, active project context, PRODUCT.md or equivalent product requirements, DESIGN.md or existing design system, authorized implementation scope]
required_resources: [applicable AGENTS.md files, skills/ui-ux/SKILL.md, skills/coding/SKILL.md, active stack and coding contexts]
mutation_class: local_edit
approval_gates: [confirm scope expansion, dependency installation, destructive replacement, or external action before proceeding]
states: [intake, confirm-flow, define-state-matrix, plan-components, implement, verify-browser, verify-accessibility, deliver]
outputs: [implemented interface, changed-artifact list, state coverage, browser evidence, accessibility evidence, residual risks]
verification: [run project-native checks, inspect critical viewports, trace keyboard focus, verify reduced motion, record console and network failures]
failure_paths: [stop when product intent or authorization is missing, preserve project behavior on partial failure, report unverified surfaces]
resume_contract: task-scoped .agents/workflows/ui-craft.json using the workflows directory contract
next_workflows: [ui-animate]
profiles: [general]
---

# Workflow: UI Craft

## Authority

This workflow implements only the approved local interface scope. It does not change APIs, authorization, data models, dependencies, or production systems without the corresponding domain workflow and approval.

## Sequence

1. Read the nearest directory contracts and active project context.
2. Confirm the user goal, critical journey, information hierarchy, and existing design system.
3. Create a state matrix covering applicable loading, empty, error, success, disabled, permission, offline, destructive, and recovery states.
4. Map components and data boundaries. Reuse existing primitives before adding new ones.
5. Implement in small verifiable increments with semantic structure, labels, keyboard behavior, focus management, responsive rules, and error handling.
6. Run project-native tests, types, lint, and build commands that apply.
7. Inspect critical viewports and states in a browser. Record screenshots or equivalent evidence, console/network errors, keyboard traversal, and reduced-motion behavior.
8. Deliver changed files, verification evidence, unverified gaps, and residual risks.

## Completion Gate

Do not declare completion until the primary journey works, important failure states are visible and recoverable, accessibility checks are proportionate to risk, and verification evidence is recorded.

