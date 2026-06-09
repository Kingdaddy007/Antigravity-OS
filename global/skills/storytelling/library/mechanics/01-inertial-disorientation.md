# Inertial Disorientation Onboarding

**Source:** The Rook • Daniel O'Malley • 2012 • Urban Fantasy
**Motion personality:** Brutal
**Density:** Minimal
**Psychological lever:** Information asymmetry + status threat

---

## How It Works

Drop the user into the middle of a high-stakes crisis before establishing any context.
They don't need to understand the world to be compelled by it — they only need to
survive it. The act of learning is indistinguishable from the act of moving through it.

**In the book:** Protagonist wakes in a rain-slicked park surrounded by unconscious
bodies. A letter in her pocket begins: "The body you are wearing used to be mine."
No world-building. No exposition. Just immediate crisis.

**In web design:** Zero-load-time entry sequences where visual motion precedes
cognitive comprehension. Bypass the user's analytical filters and trigger pure,
visceral engagement.

---

## Web Translation

**Hero / above-the-fold:**
- Full-viewport absolute DOM overlay
- Headline at maximum viewport width (100vw)
- Navigation and brand context deliberately withheld from initial state

**Spatial / 3D / canvas:**
- R3F with postprocessing (ChromaticAberration, MotionBlur)
- Camera travels on high-velocity CatmullRomCurve3 spline
- Stabilizes only upon first user interaction

**Scroll pacing:**
- Aggressive 1:3 scroll-distance-to-event ratio
- expo.out easing curve — massive Z-depth leaps per scroll tick
- DOM text micro-animates by snapping into alignment from scattered positions

**Micro-copy & CTA:**
- Pinned to absolute bottom edge of viewport
- Forces visual traversal of chaotic canvas
- Example: "Follow the instructions left behind."

---

## Build Spec

| Parameter | Value |
|-----------|-------|
| Colors | Background: #0A0A0C / Foreground: #E8E8E8 / Accent: #FF2A2A |
| Typography | Monument Extended (Display) / Space Grotesk (Body) |
| Motion personality | Brutal |
| Density | Minimal |

---

## Best For

- High-kinetic Web3 product launches
- E-sports platforms
- Disruptive tech startups
- Gaming launch sites

## Reference Sites

- Lusion (Choo Choo World)
- Active Theory (high-energy launches)
