---
id: test-strategy
version: 1
status: active
intent: Create or implement a risk-based test strategy with behavior-level evidence.
use_when: [planning coverage, adding regression defense, validating a major change, improving weak tests]
do_not_use_when: [style-only linting, performance profiling without correctness risk]
inputs: [behavior contract, risk surfaces, existing tests, available environments]
required_resources: [testing standards, project test configuration, acceptance criteria]
mutation_class: local_edit
approval_gates: [confirm implement mode before adding or changing tests]
states: [inventory, risk-model, propose, implement, execute, evaluate, deliver]
outputs: [risk matrix, test plan, tests when authorized, execution evidence, coverage gaps]
verification: [red-green evidence for regressions, behavior-focused assertions, failure-path execution, stable rerun]
failure_paths: [report unavailable environment, quarantine only with owner and expiry, never claim unrun coverage]
resume_contract: task-scoped .agents/workflows/test-strategy.json using the workflows directory contract
next_workflows: [review-code, verify-project]
profiles: [general]
---

# WORKFLOW: TEST STRATEGY

## Modes

- **Propose:** produce a risk matrix and test plan without editing.
- **Implement:** add or revise tests after the user requests implementation.

## Sequence

1. Define observable behavior, invariants, trust boundaries, and highest-cost failures.
2. Inventory current unit, integration, contract, end-to-end, accessibility, performance, and operational checks.
3. Allocate tests by risk, not by arbitrary coverage percentage. Prefer the lowest layer that proves behavior without hiding integration risk.
4. Include success, boundary, malformed-input, dependency-failure, authorization, concurrency, and regression cases as applicable.
5. In implement mode, capture red-green evidence for a regression and avoid assertions tied only to implementation detail.
6. Run targeted tests, then the proportionate broader suite. Repeat flaky-looking failures before classifying them.
7. Deliver executed evidence, untested risks, environment limitations, and recommended next checks.

