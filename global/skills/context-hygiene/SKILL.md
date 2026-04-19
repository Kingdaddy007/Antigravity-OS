---
name: Context Hygiene & Session Management
description: >
  Monitors conversation complexity and advises the user to split work
  across separate chat sessions to avoid context bloat, token waste,
  and hallucination from overloaded context windows.
trigger_patterns:
  - long implementation sessions
  - multi-step feature builds
  - debugging sessions that shift topics
  - any session exceeding ~30 back-and-forth exchanges
---

# Context Hygiene & Session Management

## Purpose

AI context windows degrade as conversations grow. After ~30+ exchanges,
the AI loses track of earlier constraints, starts hallucinating details,
and wastes tokens re-reading irrelevant history.

This skill teaches Anti-Gravity to actively manage session boundaries.

## Rules

### When to Advise a Session Split

Recommend the user open a new chat window when:

1. **The task changes significantly.** If we finished debugging and are now
   building a new feature, that is a new session.
2. **The conversation exceeds ~30 exchanges.** Context quality degrades.
   Proactively say: "We've covered a lot. I recommend starting a fresh
   chat for the next piece so I stay sharp."
3. **Multiple unrelated tasks are being discussed.** Each task deserves
   its own clean context.
4. **A micro-task sequence is complete.** After finishing a planned set
   of tasks, suggest: "Good stopping point. For the next batch, a fresh
   session will give you better results."
5. **You notice yourself losing track.** If you catch yourself
   contradicting something from earlier, say so and recommend a split.

### How to Hand Off

When recommending a session split, generate a **Handoff Brief** — a
compact summary the user can paste into the new chat to give the fresh
agent full context instantly.

#### Handoff Brief Format

```
## Handoff Brief

**Project:** [project name]
**What was completed this session:**
- [completed task 1]
- [completed task 2]

**What needs to happen next:**
- [next task 1]
- [next task 2]

**Key decisions made:**
- [decision 1 and why]

**Files touched:**
- [file paths]

**Current branch:** [branch name]

**Important context the next agent needs to know:**
- [any constraints, gotchas, or patterns established]
```

The user copies this brief, opens a new chat, and pastes it. The fresh
agent picks up exactly where we left off — with zero context bloat.

### When NOT to Split

- In the middle of a single atomic task (don't interrupt flow)
- When the user is in a sprint and splitting would break momentum
- When the conversation is short and focused

### Integration with Memory

Before recommending a split:
1. Check if any decisions, patterns, or mistakes should be logged to
   local workspace memory first.
2. The Handoff Brief is for the NEXT session's immediate context.
   Memory files are for LONG-TERM retention across all future sessions.
   Both may be needed.
