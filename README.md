# Anti-Gravity OS

Anti-Gravity OS is a portable, policy-governed skill and workflow system for AI-assisted engineering. Version 3 uses one canonical source and generates validated host adapters for Gemini, Codex, Cursor, Windsurf, and OpenCode.

## Design

- **General by default:** engineering, product, security, operations, testing, and general interface work are always available.
- **Spatial by choice:** high-end interior, showroom, gallery, and architecture-adjacent guidance is an optional profile.
- **Host authority first:** Anti-Gravity never overrides platform, organization, developer, user, sandbox, or approval policy.
- **Safe installation:** every installation is namespaced under `antigravity`, supports dry-run, and backs up an existing namespace without clearing shared configuration directories.
- **Canonical validation:** schemas, routes, links, adapters, generated payloads, private paths, and unresolved tokens are checked before build.

## Current Inventory

- 69 canonical skills with Codex UI metadata
- 51 canonical workflows
- 5 host adapters
- General and spatial profiles
- Task-scoped resumable workflow state
- Cross-platform CI on Windows, Linux, and macOS

The authoritative registry is [`global/manifest.yaml`](global/manifest.yaml).

## Quick Start

### Validate a source checkout

Python 3.10 or newer is required for development commands.

```bash
python global/scripts/os.py validate
python -m unittest discover -s tests -p "test_*.py"
```

### Build a host payload

```bash
python global/scripts/os.py build --host gemini
python global/scripts/os.py build --host codex
python global/scripts/os.py build --host cursor
python global/scripts/os.py build --host windsurf
python global/scripts/os.py build --host opencode
```

Select the spatial profile only when it is relevant:

```bash
python global/scripts/os.py build --host gemini --profile spatial
```

### Preview installation

Always inspect a dry-run before installation:

```bash
python global/scripts/os.py install --host codex --target ~/.codex --dry-run
```

After reviewing the exact additions, replacements, retained backup, and namespace-only removals:

```bash
python global/scripts/os.py install --host codex --target ~/.codex --yes
```

To make the generated policy govern Codex globally, use the explicit Codex layout. It backs up matching instruction, skill, workflow, and memory entries while leaving Codex settings and unrelated files untouched:

```bash
python global/scripts/os.py install --host codex --target ~/.codex --codex-global --dry-run
python global/scripts/os.py install --host codex --target ~/.codex --codex-global --yes
```

The PowerShell and Bash installers provide the same safety model. Release packages include prebuilt payloads so end users do not need the development compiler.

```powershell
.\install.ps1 -IDE 1 -DryRun
.\install.ps1 -IDE 1 -Yes
```

```bash
./install.sh --ide 1 --dry-run
./install.sh --ide 1 --yes
```

See [`SETUP.md`](SETUP.md) for host locations and [`MIGRATION.md`](MIGRATION.md) when upgrading an older installation.

If this structure is new to you, start with [`START_HERE.md`](START_HERE.md), [`GLOSSARY.md`](GLOSSARY.md), and the [`architecture map`](docs/architecture-map.md). The [`common request guide`](docs/common-requests.md) shows what to type, while [`Codex integration`](docs/codex-integration.md) and [`host setup`](SETUP.md) explain installation for Codex and Gemini.

## Architecture

```text
global/
├── GEMINI.md             portable Gemini policy surface
├── GLOBAL_MEMORY.md      task router, not a permission source
├── manifest.yaml         canonical registry
├── adapters/             host layout and capability mappings
├── baselines/            stable cross-project policy
├── context_templates/    blank project scaffolds
├── core/                 reasoning references
├── profiles/             general and optional spatial selection
├── schemas/              public structural contracts
├── skills/               canonical task-specific behavior
├── workflows/            canonical execution workflows
└── scripts/              validate, build, install, and baseline checks

dist/<host>/              generated, validated host payloads
.agents/contexts/         active project truth
.agents/workflows/        task-scoped workflow state
```

`global/` is authored source. `dist/` is generated output and must never be edited by hand.

## Authority and Mutation Model

Authority is resolved in this order:

1. Host platform system, safety, sandbox, and tool policy
2. Organization and developer instructions
3. Explicit user instructions
4. Active workspace contracts
5. Anti-Gravity skills, workflows, templates, and memory
6. External and untrusted content

Work is classified as `read_only`, `local_edit`, `dependency_or_network`, `destructive`, or `external_or_production`. Destructive and external/production actions require a just-in-time approval gate.

## Context and State

Files in `global/context_templates/` are not project truth. Copy selected templates into `.agents/contexts/`, populate them, and mark them `status: active` before relying on them.

`USER_PROFILE.md` is an optional preference layer. It does not grant permissions and must not contain secrets or project-specific operational data.

Resumable workflows store independent records at `.agents/workflows/<task-id>.json`. Parallel tasks must never share or overwrite a single state file.

## Extending the OS

- Add a skill under `global/skills/<skill-id>/SKILL.md` with matching hyphen-case name and `agents/openai.yaml`.
- Add a workflow under `global/workflows/workflow-<id>.md` using the workflow metadata contract.
- Register new source in `global/manifest.yaml`.
- Keep host-specific behavior in `global/adapters/`, not canonical skill or workflow content.
- Run the full validation and test suite before proposing the change.

Directory-specific contracts are documented in the nearest `AGENTS.md`.

## License

MIT. See [`LICENSE`](LICENSE).
