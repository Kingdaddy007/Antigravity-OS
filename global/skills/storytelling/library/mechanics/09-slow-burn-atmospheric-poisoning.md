# Slow-Burn Atmospheric Poisoning

**Source:** Mexican Gothic • Silvia Moreno-Garcia • 2020 • Gothic Horror
**Motion personality:** Glacial
**Density:** Maximalist
**Psychological lever:** Dread anticipation + environmental pattern violation

---

## How It Works

Front-load glamour, then slam into decay. Every subsequent element adds one
sensory degradation marker. The dread isn't from events — it's from environmental
data accumulation signaling wrongness before any confirmation.

**In the book:** Chapter 1 front-loads glamorous Mexico City society. Chapter 2
slams into mist-soaked mansion with mold, dampness, and silence. Every paragraph
adds degradation — wallpaper peeling, silver tarnished, fungal smell.

**In web design:** Environmental gradients map directly to WebGL shader transitions,
particle systems, and fog density curves. Start pristine, progressively corrupt.

---

## Web Translation

**Hero / above-the-fold:**
- Full-bleed video or R3F scene — pristine luxury environment
- Headline: "Everything here feels wrong"
- Withholds what "here" is. Scroll to reveal.

**Spatial / 3D / canvas:**
- R3F `<Fog>` component with density increasing as function of scroll position
- Scene starts chrome/glass, progressively loads corroded PBR materials
- Camera dolly-in with slight handheld shake increasing amplitude (Perlin noise via useFrame)

**Scroll pacing:**
- 4x viewport heights to full environmental corruption
- power3.inOut easing
- Micro-animation: UI chrome elements (buttons, nav) gradually degrade
- Border-radius increases, box-shadows multiply/blur, suggesting visual rot

**Micro-copy & CTA:**
- CTA only appears after fog density >70%
- Example: "Enter anyway" — center-screen, flickering opacity

---

## Build Spec

| Parameter | Value |
|-----------|-------|
| Colors | Background: #0D1F22 / Foreground: #C9D1C8 / Accent: #2D5016 (mold green) |
| Typography | Cormorant Garamond (Display) / Karla (Body) |
| Motion personality | Glacial |
| Density | Maximalist |

---

## Best For

- Luxury rebrands
- Atmospheric hospitality/real estate
- Environmental storytelling
- Slow-burn suspense

## Reference Sites

- Lusion (The Mill rebrand)
