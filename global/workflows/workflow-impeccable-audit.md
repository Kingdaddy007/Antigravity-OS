---
name: workflow-impeccable-audit
description: Impeccable UI/UX audit workflow
id: impeccable-audit
version: 1
status: active
intent: Execute impeccable audit with explicit authority, state, outputs, and evidence.
use_when: [the task matches impeccable audit]
do_not_use_when: [another workflow more precisely matches the requested outcome]
inputs: [user objective, workspace context, constraints, requested authority mode]
required_resources: [applicable AGENTS.md files, referenced skills and contexts]
mutation_class: read_only
approval_gates: [confirm implement mode before any mutation]
states: [intake, assess, propose, approve-if-needed, execute-if-authorized, verify, deliver]
outputs: [task result, changed-artifact list when applicable, evidence, residual risks]
verification: [run proportionate checks, record raw evidence, label anything unverified]
failure_paths: [stop on authority or contract conflict, preserve state, report blocker and safe next action]
resume_contract: task-scoped .agents/workflows/impeccable-audit.json using the workflows directory contract
next_workflows: [none]
profiles: [general]
---

Run systematic **technical** quality checks and generate a comprehensive report. Don't fix issues — document them for other commands to address.

This is a code-level audit, not a design critique. Check what's measurable and verifiable in the implementation.

## Diagnostic Scan

Run comprehensive checks across 5 dimensions. Score each dimension 0-4 using the criteria below.

### 1. Accessibility (A11y)

**Check for**:
- **Contrast issues**: Text contrast ratios < 4.5:1 (or 7:1 for AAA)
- **Missing ARIA**: Interactive elements without proper roles, labels, or states
- **Keyboard navigation**: Missing focus indicators, illogical tab order, keyboard traps
- **Semantic HTML**: Improper heading hierarchy, missing landmarks, divs instead of buttons
- **Alt text**: Missing or poor image descriptions
- **Form issues**: Inputs without labels, poor error messaging, missing required indicators

**Score 0-4**: 0=Inaccessible (fails WCAG A), 1=Major gaps (few ARIA labels, no keyboard nav), 2=Partial (some a11y effort, significant gaps), 3=Good (WCAG AA mostly met, minor gaps), 4=Excellent (WCAG AA fully met, approaches AAA)

### 2. Performance

**Check for**:
- **Layout thrashing**: Reading/writing layout properties in loops
- **Expensive animations**: Casual layout-property animation, unbounded blur/filter/shadow effects, or effects that visibly drop frames
- **Missing optimization**: Images without lazy loading, unoptimized assets, missing will-change
- **Bundle size**: Unnecessary imports, unused dependencies
- **Render performance**: Unnecessary re-renders, missing memoization

**Score 0-4**: 0=Severe issues (layout thrash, unoptimized everything), 1=Major problems (no lazy loading, expensive animations), 2=Partial (some optimization, gaps remain), 3=Good (mostly optimized, minor improvements possible), 4=Excellent (fast, lean, well-optimized)

### 3. Theming

**Check for**:
- **Hard-coded colors**: Colors not using design tokens
- **Broken dark mode**: Missing dark mode variants, poor contrast in dark theme
- **Inconsistent tokens**: Using wrong tokens, mixing token types
- **Theme switching issues**: Values that don't update on theme change

**Score 0-4**: 0=No theming (hard-coded everything), 1=Minimal tokens (mostly hard-coded), 2=Partial (tokens exist but inconsistently used), 3=Good (tokens used, minor hard-coded values), 4=Excellent (full token system, dark mode works perfectly)

### 4. Responsive Design

**Check for**:
- **Fixed widths**: Hard-coded widths that break on mobile
- **Touch targets**: Interactive elements < 44x44px
- **Horizontal scroll**: Content overflow on narrow viewports
- **Text scaling**: Layouts that break when text size increases
- **Missing breakpoints**: No mobile/tablet variants

**Score 0-4**: 0=Desktop-only (breaks on mobile), 1=Major issues (some breakpoints, many failures), 2=Partial (works on mobile, rough edges), 3=Good (responsive, minor touch target or overflow issues), 4=Excellent (fluid, all viewports, proper touch targets)

### 5. Anti-Patterns (CRITICAL)

Check against `skills/ui-ux/reference/design-bans.md` for the current list of absolute bans and AI slop tells. Look for AI color palette, gradient text, glassmorphism, hero metrics, card grids, generic fonts, and general design anti-patterns (gray on color, nested cards, bounce easing, redundant copy).

**Score 0-4**: 0=AI slop gallery (5+ tells), 1=Heavy AI aesthetic (3-4 tells), 2=Some tells (1-2 noticeable), 3=Mostly clean (subtle issues only), 4=No AI tells (distinctive, intentional design)

## Generate Report

### Audit Health Score

| # | Dimension | Score | Key Finding |
|---|-----------|-------|-------------|
| 1 | Accessibility | ? | [most critical a11y issue or "--"] |
| 2 | Performance | ? | |
| 3 | Responsive Design | ? | |
| 4 | Theming | ? | |
| 5 | Anti-Patterns | ? | |
| **Total** | | **??/20** | **[Rating band]** |

**Rating bands**: 18-20 Excellent (minor polish), 14-17 Good (address weak dimensions), 10-13 Acceptable (significant work needed), 6-9 Poor (major overhaul), 0-5 Critical (fundamental issues)

### Anti-Patterns Verdict
**Start here.** Pass/fail: Does this look AI-generated? List specific tells. Be brutally honest.

### Executive Summary
- Audit Health Score: **??/20** ([rating band])
- Total issues found (count by severity: critical/high/medium/low)
- Top 3-5 critical issues
- Recommended next steps

### Detailed Findings by Severity

Tag every issue with **critical/high/medium/low severity** (consistent with `workflow-impeccable-critique.md`):
- **Critical / blocking**: Prevents task completion — fix immediately
- **High / major**: Significant difficulty or WCAG AA violation (including contrast failures) — fix before release
- **Medium / minor**: Annoyance, workaround exists — fix in next pass
- **Low / polish**: Nice-to-fix, no real user impact — fix if time permits

For each issue, document:
- **[severity] Issue name**
- **Location**: Component, file, line
- **Category**: Accessibility / Performance / Theming / Responsive / Anti-Pattern
- **Impact**: How it affects users
- **WCAG/Standard**: Which standard it violates (if applicable)
- **Recommendation**: How to fix it
- **Suggested command**: Which command to use (prefer: the installed workflow registry)

### Patterns & Systemic Issues

Identify recurring problems that indicate systemic gaps rather than one-off mistakes:
- "Hard-coded colors appear in 15+ components, should use design tokens"
- "Touch targets consistently too small (<44px) throughout mobile experience"

### Positive Findings

Note what's working well — good practices to maintain and replicate.

## Recommended Actions

List recommended commands in priority order (critical first, then high, then medium):

1. **[severity] `/command-name`** — Brief description (specific context from audit findings)
2. **[severity] `/command-name`** — Brief description (specific context)

**Rules**: Only recommend commands from: the installed workflow registry. Map findings to the most appropriate command. End with `/impeccable-polish` as the final step if any fixes were recommended.

After presenting the summary, tell the user:

> You can ask me to run these one at a time, all at once, or in any order you prefer.
>
> Re-run `/impeccable-audit` after fixes to see your score improve.

### Machine-Readable Issue List (Output Artifact)

At the end of every audit run, append a structured fix list to `.agents/contexts/audit-issues.md`:

```
[critical] Issue: [description] | Location: [file/component] | Fix: [action]
[high] Issue: [description] | Location: [file/component] | Fix: [action]
[medium] Issue: [description] | Location: [file/component] | Fix: [action]
[low] Issue: [description] | Location: [file/component] | Fix: [action]
```

This file is consumed by `/impeccable-polish` alongside `.agents/contexts/critique-issues.md` to ensure all identified issues are addressed before shipping. Overwrite the file on each new audit run.

**IMPORTANT**: Be thorough but actionable. Too many low-severity issues creates noise. Focus on what actually matters.

**NEVER**:
- Report issues without explaining impact (why does this matter?)
- Provide generic recommendations (be specific and actionable)
- Skip positive findings (celebrate what works)
- Forget to prioritize (everything cannot be critical)
- Report false positives without verification

Remember: You're a technical quality auditor. Document systematically, prioritize ruthlessly, cite specific code locations, and provide clear paths to improvement.

---

## WHAT'S NEXT

After audit is complete (findings presented, action plan created):

1. **Fix the issues** → Run the recommended commands from the action summary (critical first, then high, then medium).
2. **After all fixes** → Run `/impeccable-polish` for the final detail pass.
3. **Re-run audit** → After fixes, re-run `/impeccable-audit` to see the score improve.
4. **If ready to ship** → Deploy.

The golden path: craft → audit → fix → polish → ship.

