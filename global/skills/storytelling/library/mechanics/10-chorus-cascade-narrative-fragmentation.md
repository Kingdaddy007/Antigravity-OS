# Chorus-Cascade Narrative Fragmentation

**Source:** Lincoln in the Bardo • George Saunders • 2017 • Historical Experimental Fiction
**Motion personality:** Stuttered
**Density:** Maximalist
**Psychological lever:** Curiosity gap + pattern-matching compulsion + social proof

---

## How It Works

Assemble a story through testimonial shards from many voices. No narrator.
No exposition. Each micro-chapter ends mid-thought, and the next voice adds
one puzzle piece. Attention locks because incompleteness IS the hook.

**In the book:** 166 voices in the first three chapters — ghosts in a graveyard,
each speaking 2-4 sentences before cutting to next. Readers assemble Lincoln's
grief through testimonial shards.

**In web design:** Rapid-fire text carousel with testimonial fragments. Each slide
is one voice. The story emerges from the accumulation.

---

## Web Translation

**Hero / above-the-fold:**
- Rapid-fire text carousel (1.5–3 second intervals)
- Each slide is one testimonial fragment (12–20 words max)
- Headline cycles through fragments, never resolves
- No "read more" button above fold

**Spatial / 3D / canvas:**
- R3F scene with instanced text meshes floating in z-space
- `<Text>` components from @react-three/drei, each representing one voice
- Camera weaves through them
- Click any text to freeze and expand

**Scroll pacing:**
- 0.5x viewport per testimonial cluster (5–7 voices)
- elastic.out for text entrances
- Micro-animation: individual word-level fade-ins (stagger: 0.02s) within each testimonial
- Creates cascading read rhythm

**Micro-copy & CTA:**
- CTA appears after 30+ fragments viewed
- Example: "Hear them all" — top-right corner, persistent

---

## Build Spec

| Parameter | Value |
|-----------|-------|
| Colors | Background: #0A0A0A / Foreground: #F4F4F4 / Accent: #6B4423 (sepia) |
| Typography | Playfair Display (Display) / Source Sans 3 (Body) |
| Motion personality | Stuttered |
| Density | Maximalist |

---

## Best For

- Testimonial-heavy B2B SaaS
- Social proof campaigns
- Community-driven brands
- Multi-voice storytelling

## Reference Sites

- Resn (Everpress 2019)
