---
id: dependency-upgrade
version: 1
status: active
intent: Upgrade dependencies with compatibility, security, and rollback evidence.
use_when: [package upgrade, framework upgrade, vulnerable dependency remediation]
do_not_use_when: [new dependency selection without an upgrade, unrelated refactor]
inputs: [dependency and target version, package manager, affected packages, reason for upgrade]
required_resources: [lockfile, official release and migration notes, project test commands]
mutation_class: dependency_or_network
approval_gates: [approve major-version migration or materially expanded dependency scope]
states: [baseline, research, impact-map, plan, implement, verify, deliver]
outputs: [updated manifests and lockfile, compatibility changes, verification evidence, rollback note]
verification: [clean install, build, typecheck, tests, dependency audit, affected behavior trace]
failure_paths: [revert scoped upgrade when compatibility fails, pin safely, document blocked transitive dependency]
resume_contract: task-scoped .agents/workflows/dependency-upgrade.json using the workflows directory contract
next_workflows: [test-strategy, review-code]
profiles: [general]
---

# WORKFLOW: DEPENDENCY UPGRADE

1. Detect the package manager and capture a passing or honestly failing baseline.
2. Read official release, migration, security, and peer-dependency notes for every crossed version.
3. Map runtime, build, type, configuration, and transitive impacts; avoid unrelated upgrades.
4. For major versions, present migration and rollback options before editing.
5. Update manifests and lockfile with the native package manager; apply required compatibility changes.
6. Run clean-install, build, type, test, security, and targeted behavior checks.
7. Deliver exact versions, changed behavior, evidence, and remaining deprecations.

