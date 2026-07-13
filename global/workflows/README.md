# Workflows

`global/workflows/` is the single canonical workflow source. Each active workflow declares portable metadata, task-scoped state, mutation authority, approval gates, outputs, evidence, failure behavior, and routing profiles. See `AGENTS.md` for the enforced contract.

## Core Routing

| Intent | Workflow |
| --- | --- |
| Start a general product, service, tool, or application | `workflow-project-inception.md` |
| Start a high-end interior or spatial storytelling site | `workflow-spatial-project-inception.md` |
| Build a feature | `workflow-build-feature.md` |
| Diagnose or fix a defect | `workflow-debug-issue.md` |
| Respond to an active production incident | `workflow-incident-response.md` |
| Plan architecture | `workflow-plan-architecture.md` |
| Design an API | `workflow-design-api.md` |
| Design general product UI | `workflow-design-ui.md` |
| Design a spatial brand UI | `workflow-spatial-design-ui.md` |
| Review, secure, refactor, or optimize | `workflow-review-code.md`, `workflow-security-audit.md`, `workflow-refactor-module.md`, `workflow-optimize-performance.md` |
| Plan tests or verify a project | `workflow-test-strategy.md`, `workflow-verify-project.md` |
| Migrate data or upgrade dependencies | `workflow-database-migration.md`, `workflow-dependency-upgrade.md` |
| Plan an AI-generated video | `workflow-video-generation.md` |
| Ship to production | `workflow-ship-to-production.md` |
| Maintain Anti-Gravity OS | `workflow-os-maintenance.md` |
| Dispatch independent work | `workflow-task-dispatch.md` |

## Spatial Profile

The spatial path is:

`workflow-spatial-project-inception.md` → `workflow-spatial-concept.md` → `workflow-visual-brainstorm.md` → `workflow-spatial-design-ui.md` → `workflow-impeccable-craft.md` → `workflow-impeccable-animate.md`

General product UI uses `workflow-design-ui.md` → `workflow-ui-craft.md` → `workflow-ui-animate.md` as needed.

Spatial implementation remains blocked until its required creative-contract artifacts and director gate pass. General product and UI work must not be forced through this profile.

## Authority Rule

Diagnose and propose are read-only. Workspace implementation requires requested or confirmed implement authority. Production, database, deployment, traffic, publication, or other external mutation requires a just-in-time approval naming target, action, expected effect, rollback or containment, and evidence plan.
