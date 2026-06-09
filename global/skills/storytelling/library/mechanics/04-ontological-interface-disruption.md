# Ontological Interface Disruption

**Source:** The Raw Shark Texts • Steven Hall • 2007 • Meta-fiction
**Motion personality:** Stuttered
**Density:** Moderate
**Psychological lever:** Information asymmetry + status threat

---

## How It Works

Weaponize typography — turn the act of reading into an encounter with an
active, hostile entity. The narrative reality fractures when language itself
becomes a visual, spatial threat. Trust is disrupted.

**In the book:** Protagonist wakes with memory loss. Letters from his past
self create a split timeline. A conceptual shark feeds on human memory and
the text on the page. The literal pages become an unreliable, decaying interface.

**In web design:** Leverage R3F and @react-three/drei to project HTML directly
into the 3D scene. Custom noise shaders dissolve and manipulate what the user
assumes is static DOM text. The digital environment proves it's unstable.

---

## Web Translation

**Hero / above-the-fold:**
- Stark, clinical layout where headline "You Do Not Remember This" appears
  perfectly static for exactly 2.5 seconds before DOM nodes subtly rearrange
- Stability of site's state deliberately withheld

**Spatial / 3D / canvas:**
- @react-three/drei `<Html>` to project text onto 3D plane
- Custom WebGL fragment shader applies simplex noise
- Dynamically dissolves geometry into floating particles based on user's idle time

**Scroll pacing:**
- Erratic scroll ratio where GSAP dynamically alters end trigger value on the fly
- power2.in easing curve that stutters
- Micro-animation randomly alters opacity and y-transform of previously viewed sections
- Simulates memory loss

**Micro-copy & CTA:**
- Hidden within dense block of visually degraded body copy
- Requires user to physically highlight text with cursor to reveal
- Example: "Do not pass go. Contact Dr. Randle."

---

## Build Spec

| Parameter | Value |
|-----------|-------|
| Colors | Background: #F5F5F5 / Foreground: #111111 / Accent: #0044CC |
| Typography | Helvetica Now Display (Display) / GT America (Body) |
| Motion personality | Stuttered |
| Density | Moderate |

---

## Best For

- Cybersecurity firms
- Experimental creative studios
- Data privacy platforms
- Mystery/thriller brands

## Reference Sites

- Lusion (Oryzo AI)
