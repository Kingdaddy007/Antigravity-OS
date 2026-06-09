# Cognitive Dissonance via Programmed Unseeing

**Source:** The City & The City • China Miéville • 2009 • Weird Fiction / Noir
**Motion personality:** Surgical
**Density:** Maximalist
**Psychological lever:** Information asymmetry + curiosity gap

---

## How It Works

Render two overlapping realities simultaneously but strictly police what the
user is allowed to look at. Create mystery not by hiding the second reality
behind a wall, but by forcing the user to actively "unsee" it.

**In the book:** Two sovereign cities occupy the same geographical space.
Citizens must legally "unsee" the buildings and people standing right next to
them. The reader puzzles out boundaries by observing negative space.

**In web design:** Stencil Buffers in R3F render entirely distinct 3D scenes
occupying the same world coordinates. User peels back primary reality through
heavily restricted, localized interactions.

---

## Web Translation

**Hero / above-the-fold:**
- Dual-layered layout where stark noir-inspired headline "Observe The Breach"
  is partially obscured by non-interactive visual noise
- Complete visual picture of overlapping secondary state deliberately withheld
  beneath strict CSS clip-path mask

**Spatial / 3D / canvas:**
- R3F utilizing WebGL Stencil Buffer (@react-three/drei Mask and useMask)
- Two distinct 3D scenes in same coordinates
- Primary scene renders normally
- Secondary scene only writes to buffer when spatial mask mapped to cursor passes over it

**Scroll pacing:**
- Standard 1:1 scroll ratio disrupted by aggressive, sudden GSAP ScrollTrigger snap points
- elastic.out(1, 0.3) easing curve
- Micro-animations trigger "unseen" background layer to violently jitter
- Three.js geometries bleed into DOM layer if user scrolls back up

**Micro-copy & CTA:**
- Visually struck-through or slightly blurred using CSS `filter: blur()`
- Requires user to hold click interaction to bring text into focus
- Example: "Acknowledge the overlap."

---

## Build Spec

| Parameter | Value |
|-----------|-------|
| Colors | Background: #1E1E1E / Foreground: #D3D3D3 / Accent: #C75B12 |
| Typography | Anton (Display) / Roboto Mono (Body) |
| Motion personality | Surgical |
| Density | Maximalist |

---

## Best For

- Data privacy platforms
- Investigative journalism interactive pieces
- High-level corporate portals
- Cybersecurity firms

## Reference Sites

- Active Theory v5 (Internal Site)
