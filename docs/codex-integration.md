# Codex Integration

Codex discovers global instructions from its home directory. On Windows this is normally `%USERPROFILE%\\.codex`; on other systems it is `~/.codex` unless `CODEX_HOME` is set. The global instruction file is `AGENTS.md` (or a temporary `AGENTS.override.md`). Project-level `AGENTS.md` files are then combined from the project root downward, with closer contracts taking precedence.

Anti-Gravity therefore installs in two layers:

1. A namespaced copy under `.codex/antigravity/` for rollback, inspection, and the complete generated payload.
2. The generated `AGENTS.md`, skills, workflows, and memory in the Codex discovery locations so Codex can actually use them.

The installer must never replace `config.toml`, `config.json`, permissions, trusted-project registrations, plugins, or unrelated skills. It creates a timestamped backup before replacing a matching file or skill directory and supports a dry-run.

## Verify the active installation

1. Open a new Codex task after installation so instructions reload.
2. Ask: “Which global instruction file are you using, and what is the Anti-Gravity default profile?”
3. Ask for a diagnosis-only task and confirm that it proposes no edits.
4. Inspect the installation record at `.codex/antigravity/installation.json`.

The source-of-truth workflow is: edit `global/` → run `validate` → run `build --host codex` → review dry-run → install with backup → start a new Codex task.

Official references: [Codex customization](https://developers.openai.com/codex/concepts/customization), [AGENTS.md configuration](https://learn.chatgpt.com/docs/agent-configuration/agents-md), and [Codex skills](https://developers.openai.com/api/docs/guides/tools-skills).
