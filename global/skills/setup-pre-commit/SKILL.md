---
name: setup-pre-commit
description: 'Use when the task requires setup pre commit guidance. Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Signal phrases: "setup pre-commit", "add husky", "setup lint-staged", "git commit hooks", "configure prettier". Always detect the local package manager first and check for existing scripts before configuration.'
---

# SETUP PRE-COMMIT

## WHEN TO USE THIS

- Adding git pre-commit hooks to ensure code quality before commits.
- Setting up Husky and lint-staged for a new or existing repository.
- Auto-formatting staged code files with Prettier.
- Preventing broken builds or tests from being committed.

## NEVER DO

- Never overwrite an existing Prettier config without checking for custom settings.
- Never add typecheck or test steps if they are missing from `package.json` without notifying the user.
- Never install dependencies using a different package manager than the one detected (e.g. don't run `npm install` in a pnpm project).

---

## MINDSET

You are a gatekeeper of codebase quality.
- **Automate the boring stuff:** Format, lint, and typecheck should run on every commit automatically so code reviews focus on logic, not formatting.
- **Fail fast:** If a commit is broken, prevent it from entering the git tree immediately.
- **Respect conventions:** Detect and adapt to the project's package manager and tools.

---

## DECISION FRAMEWORK — 4 PRIORITIES (IN ORDER)

### Priority 1 — Package Manager Auto-Detection
Detect which lockfile exists (`package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `bun.lockb`) and use the corresponding package manager.

### Priority 2 — Dependency Integrity
Install only the necessary devDependencies: `husky`, `lint-staged`, and `prettier` (if missing).

### Priority 3 — Script Compatibility
Ensure typecheck and test hooks exist in `package.json` before registering them in Husky.

### Priority 4 — Verification
Smoke test the hooks by staging files and running the pre-commit manually or making a test commit.

---

## CORE PRINCIPLES

1. **Format Staged Only.** Prettier should only run on staged files using `lint-staged` to keep commit speeds fast.
2. **Typecheck & Test Globally.** Type checking cannot be done on isolated staged files; always run global checks if available.
3. **No Shebangs for Husky v9+** Husky v9+ files in `.husky/` do not require bash shebang lines.

---

## SETUP PRE-COMMIT LENSES

| Lens | What to Inspect |
| --- | --- |
| **Lockfile** | Which package manager is used? |
| **Package.json** | Are `typecheck` and `test` scripts present? |
| **Prettier Config** | Does a `.prettierrc` or similar configuration exist? |

---

## BEHAVIORAL WORKFLOW

### Phase 1 — Detect Package Manager
Search the repository root for lockfiles:
- `package-lock.json` -> npm
- `pnpm-lock.yaml` -> pnpm
- `yarn.lock` -> yarn
- `bun.lockb` -> bun
Default to npm if no lockfile is found.

### Phase 2 — Install Dependencies
Install the required tooling as devDependencies:
- npm: `npm install -D husky lint-staged prettier`
- pnpm: `pnpm add -D husky lint-staged prettier`
- yarn: `yarn add -D husky lint-staged prettier`
- bun: `bun add -d husky lint-staged prettier`

### Phase 3 — Initialize Husky
Run the initialization command:
`npx husky init`
Verify this creates a `.husky/` directory and registers the `prepare` script in `package.json`.

### Phase 4 — Configure Hook Scripts
Create or update `.husky/pre-commit` with:
```
npx lint-staged
npm run typecheck
npm run test
```
*Note: Replace `npm` with the detected package manager. Omit typecheck or test lines if those scripts do not exist in package.json.*

### Phase 5 — Create Configurations
1. **`.lintstagedrc`**:
   ```json
   {
     "*": "prettier --ignore-unknown --write"
   }
   ```
2. **`.prettierrc`** (only if missing):
   ```json
   {
     "useTabs": false,
     "tabWidth": 2,
     "printWidth": 80,
     "singleQuote": false,
     "trailingComma": "es5",
     "semi": true,
     "arrowParens": "always"
   }
   ```

### Phase 6 — Verify & Commit
1. Verify files exist: `.husky/pre-commit`, `.lintstagedrc`, `.prettierrc`.
2. Run `npx lint-staged` directly to smoke-test formatting.
3. Stage changes: `git add .`
4. Commit: `git commit -m "Add pre-commit hooks (husky + lint-staged + prettier)"`

---

## KEY DIAGNOSTIC QUESTIONS

- Did Husky create the `.husky/` directory?
- Are the `typecheck` and `test` scripts defined in `package.json`?
- Does the git hooks script run successfully on git commit?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| --- | --- | --- | --- |
| **The Blind Overwrite** | Overwriting a custom `.prettierrc` with default values. | Destroys team formatting rules and creates massive diffs. | Check if Prettier config exists before writing defaults. |
| **Package Manager Mix** | Running `npm install` in a pnpm repository. | Creates duplicate lockfiles and confuses dependencies. | Detect lockfiles first. |
| **Slow Hooks** | Running a full codebase lint or test in lint-staged. | Makes commits take minutes, leading developers to skip hooks. | Keep lint-staged restricted to Prettier on staged files. |

---

## OUTPUT SHAPE

```markdown
## Pre-commit Hook Setup Summary

- **Package Manager Detected**: [e.g. pnpm]
- **Installed Packages**: husky, lint-staged, prettier
- **Files Created/Modified**:
  - `package.json` (prepare script)
  - `.husky/pre-commit`
  - `.lintstagedrc`
  - `.prettierrc`
- **Hook Test Output**: [Logs from npx lint-staged]
```

---

## NON-NEGOTIABLE CHECKLIST

- [ ] `.husky/pre-commit` exists and is executable
- [ ] `.lintstagedrc` exists and formats staged files
- [ ] `prettier` config matches existing style if present
- [ ] Hooks run successfully during a test commit

---

**Final Rule:** Pre-commit hooks must be fast and invisible. If a commit takes longer than 15 seconds to pass hooks, the hook suite is too bloated.
