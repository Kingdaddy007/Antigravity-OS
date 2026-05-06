# Anti-Gravity OS: The Master User Manual

Welcome to the Anti-Gravity OS. If you've just installed this system, you might be wondering: *"How do I actually use this day-to-day? How do I make sure the AI doesn't drift? How do I ensure my UI/UX looks incredible every time?"*

This document is your definitive guide to piloting the OS. It explains exactly what the AI should be doing, how to monitor it, and how to harness the workflows (especially for design and feature building).

---

## 1. The Core Philosophy: You Are the Pilot

Anti-Gravity OS turns your AI into a highly disciplined Senior Engineer. However, **you are still the Tech Lead.** 

The AI is programmed to follow strict instructions, load specific skills, and announce its "Mode" (e.g., ARCHITECT, BUILDER, DEBUGGER). But AI models can sometimes be lazy or forget to load a skill. **Your job is to hold it accountable to its own rules.**

**What you should monitor every session:**
- **Did it announce its mode?** (If it starts writing code without saying `[Mode: BUILDER]`, stop it).
- **Did it read the context files?** (If it builds a UI without reading `contexts/visual-identity.md` or `skill-ui-ux/SKILL.md`, it will give you generic trash. Force it to read them).
- **Did it verify its code?** (It is strictly forbidden from handing over code without a "Verification Trace". If it skips this, remind it: *"You forgot your Phase 6 verification trace."*)

---

## 2. Starting a Project: `/workflow-project-inception`

This is where every new project begins. If you skip this, your project will likely fail or turn into spaghetti code.

**How to trigger it:**
Type in your IDE chat:
> *"I have a new idea for a project. Let's run `/workflow-project-inception`."*

### What the AI is meant to do during Inception:
Instead of immediately writing code, the AI will walk you through a structured planning phase. It will act as a Product Manager and Architect.

1. **Problem & MVP Scope:** It will force you to define the exact problem and strip away "nice-to-have" features until you have a bare-bones MVP (Minimum Viable Product).
2. **App Flow & Visual Identity:** It will help you define how the app navigates and what it looks like *before* writing a single line of CSS.
3. **Architecture & Stack:** It will define your frontend, backend, and database.
4. **Build Sequence:** It will create a step-by-step roadmap (Step 1, Step 2, etc.) for how to build the app.

### What files you should check for:
By the end of the Inception workflow, the AI **must** have created or initialized the following files in your project workspace:
- `contexts/project-context.md` (The core brief)
- `contexts/stack-context.md` (Your tech stack)
- `contexts/architecture-context.md` (How the app is structured)
- `contexts/visual-identity.md` (Your UI/UX design tokens, colors, typography)
- `.agents/workflow-state.json` (To track progress)
- `.agents/memory/decisions-log.md` (To log architectural decisions)

**⚠️ Monitoring Tip:** If the AI tries to skip creating these files and jump straight to coding, stop it. Say: *"Generate the runtime context files and memory files as dictated by the inception workflow first."*

---

## 3. Designing the UI/UX: Achieving the "Impeccable" Standard

You asked: *"How is it going to apply the UI/UX?"*

Anti-Gravity OS comes with incredibly powerful, premium design workflows (the `workflow-impeccable-*` series and `skill-ui-ux`). But the AI needs to know *when* to use them.

### How it works:
During `/workflow-project-inception`, the AI creates `contexts/visual-identity.md`. This file holds your colors, typography, spacing, and "vibe" (e.g., Premium, Dark Mode, Glassmorphism).

When you are ready to actually build the UI, you trigger:
> *"Let's build the frontend. Run `/workflow-design-ui` and make sure you load `skill-ui-ux`."*

### The "Impeccable" Guarantee:
If you want ultra-premium, award-winning interfaces, you can invoke the Impeccable workflows directly:
- `/workflow-impeccable-craft` (For building high-end components)
- `/workflow-impeccable-animate` (For adding smooth motion and micro-interactions)
- `/workflow-impeccable-polish` (For final UX refinement)

**⚠️ Monitoring Tip:** The AI defaults to generic, static UI if left unchecked. You must enforce the standard. If the AI gives you a boring, static component, reply: *"This is too basic. Load `skill-ui-ux`, use the `motion` library, and apply the Impeccable design standard. Do not give me MVP-looking UI."*

---

## 4. Building Features: `/workflow-build-feature`

Once your inception is done and your UI is planned, you build features one by one using your Build Sequence.

**How to trigger it:**
> *"Let's move to Step 2 of the build sequence. Run `/workflow-build-feature`."*

### What you must make sure the AI does:
1. **Load Skills:** For a frontend feature, it MUST load `skill-coding` AND `skill-ui-ux`. If it's a backend feature, it MUST load `skill-coding` AND `skill-api-design` (or database).
2. **Read Contexts:** It MUST read `stack-context.md` and `visual-identity.md` before coding.
3. **Execution Spine:** It must follow the strict stop-and-verify process:
   - *Understand*
   - *Contextualize*
   - *Execute (Write the code)*
   - *Verify (Show the data trace)*

**⚠️ Monitoring Tip:** Sometimes the AI will just spit out a massive block of code without planning. This is a failure. Tell it: *"Stop. Follow the execution spine. Plan it out first, then write the code."*

---

## 5. Summary of the Day-to-Day Flow

1. **New Idea?** → Run `/workflow-project-inception`. Lock down the MVP and generate context files.
2. **Need to Design?** → Run `/workflow-design-ui` or any `workflow-impeccable-*` command.
3. **Ready to Code?** → Run `/workflow-build-feature`. Force the AI to load `skill-coding`.
4. **Hit a Bug?** → Stop building. Run `/workflow-debug-issue`. Make it load `skill-debugging` so it does a root-cause analysis instead of randomly guessing.
5. **Session Ending?** → Tell the AI: *"Log today's major decisions and mistakes to `.agents/memory/`."*

### The Ultimate Benefit of this OS
Without Anti-Gravity, the AI is a goldfish. It forgets your stack, writes ugly generic UI, and creates spaghetti architecture. 

With Anti-Gravity, the AI reads your `contexts/` so it knows your exact tech stack. It reads `skills/` so it thinks like a senior engineer. It uses `workflows/` so it follows a professional process. And it uses `memory/` so it never repeats the same mistake twice. 

You are no longer begging a chatbot for code snippets. You are managing a highly capable software engineering partner.
