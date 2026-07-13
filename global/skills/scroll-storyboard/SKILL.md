---
name: scroll-storyboard
description: 'Use this skill when translating an approved brand narrative and visual thesis into a scroll-choreography blueprint before any section-level code or design begins. Activated by "storyboard the scroll", "map the sections", "what should each section do", "how should the scroll feel", "before we build the page", or any moment where the narrative is approved but the viewport-by-viewport experience is still undefined. Also activate when a site feels disconnected, abrupt, or like sections were designed independently. Do NOT use this as a copywriting tool or a layout tool — it only defines what the user experiences at each scroll depth and why.'
---

# Scroll Storyboard

## WHAT THIS IS

A **Scroll Storyboard Contract** is the translation layer between:

- `storytelling` skill → narrative argument, room sequence, emotional arc
- `spatial-experience-design` skill → visual system, components, motion tokens
- `→ implementation` → `index.html` section order, `main.ts` animation choreography, `style.css` section-level styles

Without it, each section gets designed in isolation. With it, every section is a sentence in one long continuous argument that the user reads by scrolling.

## THE CORE PRINCIPLE

> **A website is not a page. It is a directed experience with a singular controlling argument.**
>
> The scroll is the sentence structure. The user's hand is the pacing.

This principle applies to ALL the user's websites — interior design, brand, product, portfolio, or agency. Every site tells a story or it tells nothing.

## WHEN TO ACTIVATE

Activate at exactly one point in the build process:

**After:** Brand doctrine is approved. `story.md` or equivalent narrative artifact exists.
**Before:** Any section-level HTML, CSS, or animation work begins.

If sections already exist, activate for an audit. Produce the storyboard for the existing site and identify the disconnections.

## NEVER DO

- Never build a section before its storyboard beat exists.
- Never add an animation before asking: "what sentence is the user reading at this scroll depth?"
- Never let a section begin a new topic — every section must continue the same argument in a different register.
- Never cut between scenes without a transition ritual (an anchor object, a light shift, a register change, or a hard contrast moment).
- Never storyboard a site that has no controlling argument. Go back to `storytelling` skill first.

## THE STORYBOARD TABLE FORMAT

Produce one row per narrative beat. A beat is defined as: *any moment where the user's emotional state, visual register, or narrative argument changes.*

| Beat # | Label | Scroll Depth | Controlling Idea | What the User Sees | What the User Feels | Register | Anchor Object | Copy Mode | Transition Out |
|--------|-------|-------------|-----------------|-------------------|--------------------|---------|--------------------|-----------|---------------|

### Column Definitions

**Beat #:** Numerical sequence. Gaps allowed (1, 2, 2.5, 3) for inserted bridges.

**Label:** A short poetic name for the beat. Treat it like a scene name in a screenplay (e.g., "The Dark Threshold", "The Weight of Stone").

**Scroll Depth:** Relative depth (e.g., "0vh–100vh", "100vh–300vh", "pinned for 200vh").

**Controlling Idea:** One sentence. The claim this beat is proving or setting up.

**What the User Sees:** Concrete description of the dominant visual. Name the element — not "some animation" but "a full-bleed concrete room video zooming in from center."

**What the User Feels:** One or two words. This is the emotional target. Not the design aesthetic — the felt state.

**Register:** One of: `LIGHT`, `DARK`, `TRANSITION`. Defines the ambient context mode.

**Anchor Object:** The persistent visual element that carries continuity into or through this beat. If nothing persists, write `NONE` — this is a risk flag.

**Copy Mode:** One of: `SILENT` (no text), `ATMOSPHERIC` (mood phrase), `DECLARATIVE` (bold claim), `EDITORIAL` (quiet caption), `INVITATION` (CTA).

**Transition Out:** How this beat ends. One of: `DISSOLVE`, `HARD CUT`, `PORTAL` (camera zooms through an element into the next scene), `DRIFT` (parallel elements enter while old ones exit), `ANCHOR HOLD` (anchor object stays, content scrolls past).

---

## BEAT TAXONOMY

Use these named beat types. A site does not need all of them. Every site needs at least: THRESHOLD → one PROOF beat → INVITATION.

| Beat Type | Purpose | Register | When to Use |
|-----------|---------|----------|-------------|
| **THRESHOLD** | First 3 seconds. Establishes the world and filters attention. | LIGHT or DARK | Always first |
| **ARGUMENT** | States the controlling idea explicitly, usually in display type | Either | After Threshold |
| **IMMERSION** | Pulls the user inside the brand world. No selling. | DARK | After first argument |
| **PROOF** | Shows capability, work, transformation — earns trust | Either | After immersion |
| **PHILOSOPHY** | Explains the brand's way of seeing the world | DARK or TRANSITION | Bridges between sections |
| **MATERIAL** | Shows the sensory raw materials the brand commands | LIGHT | Before or after proof |
| **INTERACTION** | A section where user agency reveals something hidden | Either | Use sparingly |
| **HARD CUT** | Intentional abrupt register shift. Resets user attention | TRANSITION | Only when mood shift is narratively justified |
| **ANCHOR HOLD** | One object stays fixed while text scrolls past | DARK | Philosophy or method sequences |
| **INVITATION** | Calm, selective inquiry gate | DARK | Always last |

---

## REGISTER SWITCHING RULES

A **register** is the ambient emotional and visual mode. There are two: **LIGHT** and **DARK**.

- Sites should operate in **one primary register** with deliberate excursions into the other.
- A register change must be motivated by a narrative event — not arbitrary visual variety.
- Never switch register more than 2 times on a single page without a strong controlling argument for each switch.
- The switch itself is a scene. It must be designed — not assumed. Call it a `HARD CUT` or a `PORTAL` in the storyboard.

---

## THE ANCHOR OBJECT PRINCIPLE

> **A site without an anchor object is a series of slides. A site with an anchor object is a journey.**

An anchor object is a persistent visual element that travels with the user across at least two consecutive beats. It provides orientation, continuity, and a sense that the site is one coherent world.

Rules:
- Name the anchor object before designing any section that uses it.
- The anchor object does not have to be the same asset — it can be a material, a color, a motion quality, or a typographic treatment.
- Mark beats with `NONE` for anchor object as narrative risk zones. A risk zone is not banned but must be reviewed.
- A hard cut that introduces a new anchor object is a portal, not a disconnection — name it explicitly.

---

## INTEGRATION WITH OTHER FILES

The Scroll Storyboard Contract is the **source of truth** for:

| Downstream File | What It Gets From the Storyboard |
|----------------|----------------------------------|
| `index.html` | Section order, section count, semantic grouping |
| `main.ts` | Scroll depth triggers, timeline sequencing, pin durations |
| `style.css` | Register-specific token usage, light/dark section scoping |
| `story.md` | Validated narrative sequence (storyboard should not contradict story.md) |
| `DESIGN.md` | Confirms which design tokens belong to which register |
| `showroom-choreography.md` | If it exists, storyboard supersedes or updates it |
| `motion-board.md` | Scroll-bound track is directly drawn from Beat # and scroll depth columns |

---

## THE STORYBOARD PRODUCTION PROCESS

1. **Gather inputs:** Read `story.md` or narrative brief. Read brand doctrine. Read `DESIGN.md`.
2. **Name the controlling argument:** One sentence. The entire site proves this.
3. **Count the register shifts:** How many light-to-dark or dark-to-light transitions exist? Each shift needs a name and a justification.
4. **Name the anchor objects:** What travels? List them before building the table.
5. **Write the beat table:** One beat per row. Start from what the narrative requires, not from what is already coded.
6. **Audit against existing code:** If sections already exist, map them to beats. Identify unanchored sections, missing transitions, and copy mode mismatches.
7. **Produce the contract:** Save to `contexts/scroll-storyboard.md` in the project workspace.
8. **Gate the build:** Do not proceed to implementation until the storyboard is approved.

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Fix |
|--------------|--------------------|-----|
| Section Island | Each section designed without referencing adjacent beats | Run storyboard audit. Identify anchor gaps. |
| Motivation-Free Register Change | Dark section appears for visual variety | Require a controlling idea for every register change |
| No Anchor Object | User loses orientation mid-scroll | Name an anchor object. Can be a color, a sound cue, a motion quality |
| Copy Mode Collision | A PHILOSOPHY beat uses DECLARATIVE copy | Match copy mode to beat type |
| Threshold Too Long | Site tries to communicate too much before first register shift | Threshold must complete in one viewport of scroll |
| Missing Hard Cut | Narrative pivot moment is treated as a fade | Design the cut explicitly — it is a scene |
| Orphan Section | A section that does not continue the controlling argument | Delete it or rewrite it to serve the argument |

---

## OUTPUT SHAPE

**New site:** Controlling argument → register map → anchor object list → full beat table → integration notes.

**Audit:** Beat map of existing sections → disconnection flags → missing beats → anchor gaps → recommended insertions.

---

## NON-NEGOTIABLE CHECKLIST

1. Controlling argument exists before the first beat is named.
2. Every beat continues or proves the controlling argument.
3. Every register change is motivated and named.
4. Every beat has an anchor object or is explicitly marked as a risk zone.
5. Copy mode matches beat type.
6. Transition Out is specified for every beat.
7. Storyboard is saved to `contexts/scroll-storyboard.md` before implementation begins.
8. Storyboard does not contradict `story.md` or brand doctrine.
