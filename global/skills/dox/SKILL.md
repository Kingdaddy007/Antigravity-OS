---
name: DOX Framework & Directory Contracts
description: Evaluates and updates hierarchical AGENTS.md documentation to enforce folder-level contracts and prevent cascade effects during modifications.
---

# DOX Framework & Directory Contracts

**DOX** is a decentralized, subtree-focused documentation framework that ensures AI agents respect local directory boundaries, contracts, and architecture rules before modifying any files. It achieves this by maintaining a hierarchy of `AGENTS.md` files from the repository root down to individual directories.

## When to Use This Skill
- **ALWAYS active** when editing code, fixing bugs, or implementing features.
- When traversing a project directory structure to locate files.
- When a folder lacks an `AGENTS.md` file and one needs to be created to define its purpose.
- When an architectural change or new dependency is introduced to a directory, requiring a documentation update.

## The Cascade Effect & Why DOX Matters
Without DOX, AI agents tend to modify target files in isolation. If a small change requires adding a new import or altering an exported interface, the AI might unintentionally break sibling files or violate directory-level constraints (e.g., importing a database model into a UI component). DOX forces the agent to read the local `AGENTS.md` file (and its parent path) to understand the **contract** of that folder before making any changes.

## Core Directives

### 1. The Traversal Rule (Read Before Edit)
Before proposing or applying an edit to *any* file, you MUST:
1. Start from the project root and locate the root `AGENTS.md` file.
2. Traverse the directory path down to the target file's directory.
3. Read the `AGENTS.md` file in the target directory. If it exists, you must obey its rules, dependency constraints, and testing commands.
4. If it does not exist, check the nearest parent directory's `AGENTS.md`.

### 2. The Contract Rule (Folder Boundaries)
Every `AGENTS.md` file acts as a local contract. It defines:
- **Purpose:** What this directory does (and what it doesn't do).
- **Dependencies:** What this directory is allowed to import (e.g., "Only UI components, no database access").
- **Exposed APIs:** What this directory exports for other folders to use.
- **Verification:** Specific commands or tests to run after modifying files in this directory.

You may NEVER violate the local contract. If a user request forces a violation, you must STOP and point out the conflict to the user, proposing either an alternative implementation or an explicit update to the `AGENTS.md` contract.

### 3. The Update Rule (Leave It Better)
When you complete a task that changes the architecture, adds new files, or alters the exposed interface of a directory, you MUST update that directory's `AGENTS.md` to reflect the new state. If you create a new major directory, you MUST initialize an `AGENTS.md` file inside it.

### 4. Legacy Projects (Fallback)
If you traverse a project directory structure and find **zero** `AGENTS.md` files (even at the root), this means DOX has not been initialized for this project. 
- Do NOT halt work or hallucinate rules. 
- **Gracefully degrade** to standard project-wide guidelines and continue your task.
- Proactively suggest to the user that they initialize DOX by running the DOX Initialization Prompt.

## Initialization Template
When creating a new `AGENTS.md` file in a directory, use the following structure:

```markdown
# [Directory Name] Context & Contract

## 1. Purpose
[Brief explanation of what this folder contains and its role in the system.]

## 2. Rules & Constraints
- [Rule 1: e.g., No direct database access]
- [Rule 2: e.g., All components must be pure functions]

## 3. Exposed Interfaces
- [File/Module A]: [Brief description of what it exports]
- [File/Module B]: [Brief description of what it exports]

## 4. Internal Dependencies
- [Sibling/Parent Directory]: [Why it is imported]

## 5. Verification
- Run `[test command]` before committing changes in this folder.
```
