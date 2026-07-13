---
name: seedance-prompt-short
description: 'Build, validate, and compress Seedance 2.0 prompts to a hard 2000-character limit using the Five-Layer Stack, @Tag delegation, and the new Compression Engine. Use when constructing or debugging any T2V, I2V, V2V, or R2V prompt for the short-form workflow.'
license: MIT
---
## STATUS VERIFICATION GATE

Treat platform availability, model limits, filter behavior, enforcement actions, and API status dated February-March 2026 as historical snapshots. Before relying on them, verify current official ByteDance/Seedance documentation. If verification is unavailable, label the claim unverified and avoid presenting it as current fact.

# seedance-prompt-short

This skill helps construct and compress prompts for Seedance 2.0, with a recommended target of **30-100 words**.

## The 30-100 Word Target

| Layer | Budget (chars) | Purpose |
|:---|:---:|:---|
| **1. Core Intent** | ~20-40 words | Subject + Action. The emotional and narrative heart. |
| **2. Visuals** | ~20-30 words | Camera + Lighting + Style. The cinematic eye. |
| **3. Audio** | ~10-20 words | Music + SFX + Ambience. The soundscape. |
| **4. Technical** | ~10-20 words | @Tags + Constraints + Physics. The rules. |

| **Total** | **~30-100 words** | **Recommended Target** |

## The Compression Engine

- **Verbs > Adjectives**: `A woman's face, catching the last light` not `A beautiful, stunning shot`.
- **Show, Don't Tell Emotion**: `His shoulders slump` not `He is sad`.
- **Use Film Language**: `Dolly shot, camera-left` not `The camera moves smoothly`.
- **Trust the Model**: `Gourmet hamburger ad, macro shot` not a long description of a hamburger.

---

For a guided workflow that builds a prompt, use [skill:seedance-interview].
