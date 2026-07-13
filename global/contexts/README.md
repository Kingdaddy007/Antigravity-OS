# Context Path Compatibility Notice

The authored context scaffolds moved to `global/context_templates/` in Anti-Gravity OS 3.0.

For one compatibility release, references to `global/contexts/` should be interpreted as references to the template source. New integrations must copy selected templates into the active project's `.agents/contexts/` directory and mark those copies `status: active` before treating them as project truth.

Stable cross-project policy now lives in `global/baselines/`.

