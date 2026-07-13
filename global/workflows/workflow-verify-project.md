---
description: The systematic sequence for running automated project verification checks — security scan, code quality, accessibility, and performance profiling before deployment.
id: verify-project
version: 1
status: active
intent: Execute verify project with explicit authority, state, outputs, and evidence.
use_when: [the task matches verify project]
do_not_use_when: [another workflow more precisely matches the requested outcome]
inputs: [user objective, workspace context, constraints, requested authority mode]
required_resources: [applicable AGENTS.md files, referenced skills and contexts]
mutation_class: read_only
approval_gates: [confirm scope expansion or destructive action before mutation]
states: [intake, assess, propose, approve-if-needed, execute-if-authorized, verify, deliver]
outputs: [task result, changed-artifact list when applicable, evidence, residual risks]
verification: [run proportionate checks, record raw evidence, label anything unverified]
failure_paths: [stop on authority or contract conflict, preserve state, report blocker and safe next action]
resume_contract: task-scoped .agents/workflows/verify-project.json using the workflows directory contract
next_workflows: [none]
profiles: [general]
---

# WORKFLOW: VERIFY PROJECT (MASTER)

> **[CONTEXT AMNESIA FAILSAFE]**
> YOU MUST USE TOOL CALLS TO READ THE FULL SOURCE FILE AND THE REQUIRED SKILLS/CONTEXTS BEFORE EXECUTING THIS.
> Verify silently in your internal reasoning that you have done this.

> **IMPORTANT [REQUIRED]:** Resolve `ANTIGRAVITY_HOME` through the installed-tool registry or environment, verify the selected Python interpreter and script exist, then run the baseline scanners. If discovery fails, report the check as unavailable rather than guessing a path.

## WHAT THIS WORKFLOW DOES

Runs automated quality checks against the project to catch security issues, code quality problems, accessibility violations, and performance concerns BEFORE deployment. This adds executable teeth to our rubric-based quality bar.

---

## WHEN TO USE

- Before any deployment or push to production
- After completing a major feature build
- During Phase 6 (Verify) of the execution workflow
- When the user says "verify", "check", or "is this ready to ship?"
- Anti-Gravity should SUGGEST (not force) running this before deployments

## WHEN NOT TO USE

- During active development (too noisy — wait for a natural checkpoint)
- For tiny changes (single line fix, comment update)

---

## EXECUTION

### Quick Check (Most Common)

```bash
python "$ANTIGRAVITY_HOME/scripts/verify.py" <project_path>
```

This runs all 4 checks in priority order:

1. **Order 1: Security Scan** — Hardcoded secrets, dangerous code, env exposure
2. **Order 2: Code Quality** — Console.log, empty catch, unhandled fetch
3. **Order 3: Accessibility** — WCAG basics on HTML files
4. **Order 4: Performance** — File sizes, bundle analysis

### Targeted Check

```bash
python "$ANTIGRAVITY_HOME/scripts/verify.py" <project_path> --only security
python "$ANTIGRAVITY_HOME/scripts/verify.py" <project_path> --only quality
python "$ANTIGRAVITY_HOME/scripts/verify.py" <project_path> --only accessibility
python "$ANTIGRAVITY_HOME/scripts/verify.py" <project_path> --only performance
```

### Skip Specific Checks

```bash
python "$ANTIGRAVITY_HOME/scripts/verify.py" <project_path> --skip performance
```

---

## INTERPRETING RESULTS

| Exit Code | Meaning | Action |
| :--- | :--- | :--- |
| 0 | Configured baseline scans passed | Continue with project-native tests, typecheck, build, CI, and the production-readiness workflow |
| 1 | Issues found | Review output, fix critical/high issues before deployment |

### Severity Levels

| Severity | Meaning | Must Fix Before Deploy? |
| :--- | :--- | :--- |
| CRITICAL | Security vulnerability or data exposure | ✅ YES — stop everything |
| HIGH | Significant issue that could cause problems | ✅ YES |
| MEDIUM | Quality issue worth addressing | ⚠️ Recommended |
| LOW | Minor issue or style concern | ❌ Optional |
| INFO | Observation, no action needed | ❌ No |

---

## QUALITY GATES

- **G1 (Security):** CRITICAL security findings = deployment blocked
- **G2 (Quality):** More than 10 MEDIUM code quality issues = review before deployment
- **G3 (Accessibility):** More than 5 HIGH accessibility issues = fix before deployment
