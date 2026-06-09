# Triple-Helix Temporal Fracture

**Source:** The Fifth Season • N.K. Jemisin • 2015 • Apocalyptic Fantasy
**Motion personality:** Stuttered
**Density:** Moderate
**Psychological lever:** Information asymmetry + pattern-matching compulsion + loss aversion

---

## How It Works

Interleave multiple parallel timelines without clarifying they're the same
person. Force the user to pattern-match through tonal and sensory repetition.
The world is demonstrated through consequence, never explained.

**In the book:** Three simultaneous timelines — 2nd person present, 3rd person
past, 3rd person present — without clarifying they're the same person. Chapter 1
withholds protagonist identity entirely. Readers track three threads with zero
exposition glue.

**In web design:** Scroll-triggered section transitions with parallel content
streams that converge. Split-screen triptych with independently scrolling sections.

---

## Web Translation

**Hero / above-the-fold:**
- Split-screen triptych with three independently scrolling vertical sections
- Headline: "You are the last seismologist"
- Withholds product/service name entirely above fold

**Spatial / 3D / canvas:**
- Three.js instanced mesh system — fractured geological planes that reform on scroll
- Camera locked to orbital path around central void
- `useScroll` from @react-three/drei drives timeline convergence at 60% scroll depth

**Scroll pacing:**
- 2.5x viewport heights per narrative reveal
- expo.out for section transitions, power4.inOut for geological object reveals
- Micro-animation: text characters fracture/reassemble character-by-character (SplitText)
- Mirrors seismic disruption rhythm

**Micro-copy & CTA:**
- CTA appears only after all three timelines visible on screen simultaneously
- Example: "See the pattern" — positioned at convergence point, bottom-center

---

## Build Spec

| Parameter | Value |
|-----------|-------|
| Colors | Background: #1C1410 / Foreground: #E8DCC4 / Accent: #8B4513 (burnt earth) |
| Typography | Chakra Petch (Display) / IBM Plex Mono (Body) |
| Motion personality | Stuttered |
| Density | Moderate |

---

## Best For

- High-end product launches with staggered feature reveals
- Complex narratives
- Multi-section storytelling
- Parallel content streams

## Reference Sites

- Active Theory (Stripe Sessions site)
