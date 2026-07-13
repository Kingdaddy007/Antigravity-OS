# Context Integrity Baseline

Templates under `context_templates/` are not runtime truth. A context becomes active only after it is copied into `.agents/contexts/` and its metadata identifies the current project.

Active context metadata must include:

- `status: active`
- `scope`
- `project_id`
- `updated_at`
- `owner`
- `confidence`

Reject or explicitly downgrade contexts that contain unresolved placeholders, identify another project, lack freshness metadata, or conflict with observable repository state.

