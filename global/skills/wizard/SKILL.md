---
name: WIZARD GENERATOR
description: >
  Generate an interactive bash wizard that walks a human through a manual procedure —
  third-party setup, a one-off migration, or environment state transitions.
  Signal phrases: "generate wizard", "create setup script", "interactive bash wizard",
  "manual migration assistant", "write environment secrets script".
  Always maintain absolute separation between the template library code and custom stages.
---

# WIZARD GENERATOR

## WHEN TO USE THIS

- Automating multi-step third-party credential setup (Auth0, Stripe, AWS).
- Creating interactive walk-through scripts for one-off data migrations.
- Writing helpers to configure `.env` files and push secrets to GitHub Actions.
- Guiding humans through complex state transitions that require manual web console inputs.

## NEVER DO

- Never write custom logic above the `STAGES` library marker in the template.
- Never hardcode secret values directly in the wizard script; always use hidden input helpers.
- Never execute side effects without explicit confirmation prompts.
- Never commit a temporary setup wizard to main unless requested as a permanent repository tool.

---

## MINDSET

You are a process simplifier. A wizard translates complex, error-prone manual console operations into a structured, step-by-step terminal checklist.
- **De-escalate Complexity:** Keep each stage confined to one task. Clear the screen per stage so only relevant information is visible.
- **Auto-link:** Open browser pages automatically before asking the user to copy values.
- **Secure by Default:** Capture API keys and passwords via hidden entry prompts and write them directly to their final resting place (`.env` or GitHub Secrets).

---

## DECISION FRAMEWORK — 4 PRIORITIES (IN ORDER)

### Priority 1 — Requirement Analysis
Read the project configuration files (`.env.example`, workflows, configs) to list all values the wizard must output.

### Priority 2 — Stage Choreography
Sequence stages chronologically. Ensure each stage has:
- A clear URL to open.
- Verbatim navigation instructions (e.g. "Dashboard -> Keys").
- Variables to capture.
- A destination file or secret namespace.

### Priority 3 — Template Integrity
Always duplicate the standard library from `template.sh` verbatim. Do not alter the core utility functions.

### Priority 4 — Verification
Run static analysis (`bash -n` and `shellcheck`) on the generated script. Verify variable assignments without executing interactive loops.

---

## CORE PRINCIPLES

1. **Clear Screens, Clear Minds.** Call screen-clearing before starting a stage to prevent scroll clutter.
2. **Open First, Prompt Second.** Always use `open_url` to guide the human before blocking on input.
3. **Idempotence.** Writing keys to `.env` must update existing lines rather than appending duplicate definitions.
4. **Time Awareness.** Display progress bars and estimated minutes remaining so the human has visibility on total length.

---

## WIZARD LENSES

| Lens | What to Inspect |
| --- | --- |
| **Secrets** | Are private variables captured using `ask_secret`? |
| **CI Sync** | Do GitHub secret names match definitions in `.github/workflows/`? |
| **Syntax** | Does the script pass `bash -n` checks? |

---

## BEHAVIORAL WORKFLOW

### Phase 1 — Scope the Procedure
1. Scan `.env.example`, config files, and CI workflows to list required variables.
2. Determine which values are secret (API keys) and which are public (endpoints).
3. Draft the ordered list of stages and present it to the user.

### Phase 2 — Map the Path
For each stage, write down the browser click-path. If you do not know the exact console path, ask the user or check external documentation.

### Phase 3 — Script Creation
1. Copy the standard `template.sh` base to a file under `scripts/` or `.scratch/`.
2. Define `TOTAL_STAGES` and `TOTAL_MINUTES`.
3. Add stage blocks below the marker:
   ```bash
   stage "Stripe Setup"
   open_url "https://dashboard.stripe.com/test/apikeys"
   say "Go to Developers -> API Keys and copy the Publishable Key."
   ask STRIPE_PUBLISHABLE_KEY "Enter Stripe Publishable Key"
   write_env STRIPE_PUBLISHABLE_KEY
   ```
4. Make the file executable: `chmod +x <path>`.

### Phase 4 — Validate
1. Run `bash -n <script>` to catch syntax errors.
2. Statically trace variable data-flow: make sure every key captured maps to a file-write or API push.
3. Present the script path and run instructions to the user.

---

## KEY DIAGNOSTIC QUESTIONS

- What environment variables are required by this project?
- Which values are sensitive and should not be displayed on screen during input?
- Does the human have the target console permissions to retrieve these keys?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| --- | --- | --- | --- |
| **The Scroll Wall** | Printing 50 lines of instructions without clearing the screen. | Key details scroll out of view; the human makes copy-paste errors. | Use distinct stages that clear the terminal screen. |
| **Silent Side Effects** | Deleting database tables or making git commits without prompting. | User loses state or commits garbage without realizing. | Require explicit `confirm` gates before destructive steps. |
| **Hardcoded Defaults** | Embedding API keys directly in the script for convenience. | Secrets get committed to public repositories. | Always capture keys interactively via `ask_secret`. |

---

## OUTPUT SHAPE

```markdown
## Interactive Wizard Generated

- **Script Location**: `scripts/setup-project.sh`
- **Estimated Duration**: 10 minutes (5 stages)
- **Variables Captured**:
  - `DATABASE_URL` (Public) -> written to `.env`
  - `STRIPE_SECRET_KEY` (Secret) -> written to `.env` and Github Secret
- **Verification Status**: `bash -n` passed.
```

---

## NON-NEGOTIABLE CHECKLIST

- [ ] Script is syntactically valid and executable
- [ ] No hardcoded private keys exist in the file
- [ ] Library utilities are unmodified
- [ ] Every stage clears the screen and provides a back-link URL
- [ ] Run instructions are clearly documented in README

---

**Final Rule:** A wizard should make a complex manual configuration feel like installing a desktop app. If the human has to search the internet for help during the wizard, the wizard is incomplete.
