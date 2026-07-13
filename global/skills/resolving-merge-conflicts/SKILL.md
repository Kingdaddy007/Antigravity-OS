---
name: resolving-merge-conflicts
description: 'Use when you need to resolve an in-progress git merge/rebase conflict. Signal phrases: "resolving conflicts", "merge conflict", "rebase conflict", "git merge --continue", "git rebase --continue", "conflict hunks". Never abort a merge or rebase without explicit user consent. Always preserve both intents where possible, and verify with automated checks.'
---

# RESOLVING MERGE CONFLICTS

## WHEN TO USE THIS

- In-progress git merge conflicts
- In-progress git rebase conflicts
- Pull request synchronization conflicts
- Merging long-lived feature branches back to main

## NEVER DO

- Never run `git merge --abort` or `git rebase --abort` as a default fallback without user permission.
- Never make up or invent new behavior to bypass a conflict hunk.
- Never stage or commit unresolved conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
- Never delete the other branch's code without verifying it is obsolete or fully covered by your changes.

---

## MINDSET

You are a git surgeon. Conflicts are not errors; they are simultaneous updates to the codebase that must be merged with absolute precision.
- **Understand intent first:** Read the commit logs and PR contexts of both branches to understand why the changes were made.
- **Preserve both intents:** Do not silently throw away code. If both changes are valid, integrate them.
- **Verify relentlessly:** A resolved conflict is a modified codebase. Run full typechecking, tests, and formatting before committing.

---

## DECISION FRAMEWORK — 5 PRIORITIES (IN ORDER)

### Priority 1 — Contextual Investigation
Identify the two branch histories and the commit messages that generated the conflict. Do not start resolving until you know the "why" of both sides.

### Priority 2 — Intent Alignment
Determine if the conflicting lines can coexist or if they are mutually exclusive. Preserve both intents where possible. Where incompatible, pick the one matching the merge's stated goal and note the trade-off.

### Priority 3 — Minimal Intervention
Modify the code only as much as needed to resolve the conflict and maintain compile safety. Do not rewrite surrounding code.

### Priority 4 — Automated Verification
Compile, run tests, and run formatting tools. If the merge broke the build or tests, fix it before continuing.

### Priority 5 — Atomic Commit
Complete the merge/rebase and write a clear commit message detailing the resolution.

---

## CORE PRINCIPLES

1. **No Silent Discarding.** Always understand what you are deleting. Read the Git history to understand the author's intent.
2. **Syntactic & Semantic Integrity.** Ensure the code compiles, passes linting/formatting, and remains logically correct.
3. **Automated Validation.** Project checks are the final arbiter of a resolution. Never assume a resolution is correct without testing it.
4. **Never Abort.** Always attempt to resolve. Only abort if the merge is structurally invalid or user asks to abort.

---

## MERGE CONFLICT LENSES

| Lens | What to Inspect |
| --- | --- |
| **History** | Check commits, PR details, and issue tracking for the conflicting hunks. |
| **Syntax** | Ensure brackets, exports, and imports are balanced after resolving. |
| **Behavior** | Run tests to verify the behavior of the combined code. |

---

## BEHAVIORAL WORKFLOW

### Phase 1 — Understand & Diagnose
Run `git status` and list conflicting files. Open files and locate all conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).

### Phase 2 — Contextualize
Check log messages for the conflicting commits on both sides:
`git log --oneline --left-right HEAD...MERGE_HEAD` (or `REBASE_HEAD`).
Understand why each change was made and what the original intent was.

### Phase 3 — Analyze
For each conflict hunk:
1. Trace the logic of both sides.
2. Determine if the changes can be combined.
3. If mutually exclusive, determine which one matches the merge's stated goal.

### Phase 4 — Plan
Write out the planned resolution for each file. Confirm with the user if the resolution is complex or involves architectural trade-offs.

### Phase 5 — Resolve
Edit the files to remove conflict markers and apply the merged logic. Fix any structural conflicts (e.g. files deleted on one branch but modified on another).

### Phase 6 — Verify
Run the project's automated checks:
- Typechecking: `npm run typecheck` or equivalent
- Testing: `npm run test` or equivalent
- Formatting: `npm run format` or equivalent

### Phase 7 — Critique
Did I lose any functionality? Are there duplicate imports or variables? Did I accidentally introduce syntax errors?

### Phase 8 — Communicate
Stage the resolved files (`git add <files>`), run `git merge --continue` or `git rebase --continue`, and present the commit message.

---

## KEY DIAGNOSTIC QUESTIONS

- What branch is being merged/rebased into which?
- Why was the change on the source branch made?
- Why was the change on the target branch made?
- Can both changes coexist?
- If they are incompatible, which one aligns with the goals of the current branch?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| --- | --- | --- | --- |
| **The Eraser** | Deleting the other side's changes because yours are "better". | Breaks other developers' work and causes silent regressions. | Understand the other side's intent. Merge both blocks. |
| **The Marker Leak** | Committing files containing unresolved `<<<<<<<`, `=======`, `>>>>>>>` markers. | Breaks compilation and crashes the app. | Search for conflict markers in the files before staging. |
| **The Blind Abort** | Running `git merge --abort` when a conflict is encountered. | Prevents progress and wastes time. | Work through the conflict systematically. |

---

## OUTPUT SHAPE

```markdown
## Conflict Resolution Log

- **Target Branch**: [e.g. main]
- **Source Branch**: [e.g. feature/auth]
- **Conflict Files**:
  - `path/to/file.ts`: Resolved by combining imports and keeping both functions.
- **Verification Commands Run**:
  - `npm run typecheck` -> PASSED
  - `npm run test` -> PASSED
```

---

## NON-NEGOTIABLE CHECKLIST

- [ ] Run `git status` to verify all conflicts are resolved
- [ ] No conflict markers exist in the files
- [ ] Code typechecks and compiles successfully
- [ ] All tests pass
- [ ] Run formatters and verify styling compliance

---

**Final Rule:** A git conflict is a coordination problem, not a code problem. Treat it as a collaboration point with the author of the conflicting commit.
