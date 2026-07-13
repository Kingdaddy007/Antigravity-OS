---
name: prompt-engineering
description: 'Use this skill when generating, writing, or refining prompts for AI image or video generation models (Midjourney, DALL-E, Stable Diffusion, Runway, Kling, Sora). Activated when the user asks for "high-detail prompts", "better image prompts", "create a prompt for", or complains that existing prompts are "rubbish", "generic", or "not professional". Do NOT use for text-to-text LLM prompt engineering.'
---

# Prompt Engineering (Image & Video)

## WHEN TO USE THIS

- The user requests prompts to generate images or videos.
- Existing visual prompts are rejected as too vague or generic.
- You are writing visual asset placeholders or asset generation instructions.

## NEVER DO

- Never write vague, conceptual prompts (e.g., "cool city vibes").
- Never start a prompt with abstract ideas; always start with the physical subject and camera shot.
- Never write a video prompt without specifying camera movement and duration.
- Never output an image prompt without defining lighting and composition.
- Never use long lists of negative exclusions unless writing specifically for Stable Diffusion negative prompt fields.

## THE UNIVERSAL FIELD SCHEMA

Always construct visual prompts using this exact sequence. Models prioritize words at the beginning of the string (attention decay).

### 1. Image Prompt Structure (The Core Spine)
Follow this exact comma-separated order:
`[Shot Type/Composition] of [SUBJECT] [ACTION/STATE] in [ENVIRONMENT], [STYLE/MEDIUM], [LIGHTING], [COLOR & MOOD], [TECHNICAL SPECS], [QUALITY MODIFIERS]`

### 2. Video Prompt Structure (The Temporal Spine)
Follow this exact comma-separated order:
`[Shot Type] of [SUBJECT] doing [ACTION] in [ENVIRONMENT], [CAMERA MOVEMENT], [SCENE MOTION], [STYLE & LIGHTING], [TECHNICAL SPECS: Lens, FPS, Duration]`

## DOMAIN RULES: WRITING THE FIELDS

- **Subject & Action:** Be highly specific. Define clothing, texture, posture, and exact action.
- **Environment:** Detail the physical space, weather, and time of day.
- **Composition / Shot Type:** Use strict cinematic terms (Extreme close-up, medium tracking shot, aerial view, 85mm macro lens).
- **Lighting:** Use physical light descriptors (Volumetric lighting, golden hour, harsh fluorescent, soft rim light, chiaroscuro).
- **Camera Movement (Video):** Explicitly define the rig (Slow dolly forward, steady handheld tracking, static tripod, fast orbit).
- **Scene Motion (Video):** Define what moves besides the subject (Dust motes floating, heavy rain, curtain blowing softly).

## ANTI-PATTERNS

| Anti-Pattern | What It Is | Fix |
| --- | --- | --- |
| Conceptual Fluff | "A beautiful and moody representation of sadness" | Describe the physical scene: "Medium shot of a woman looking down in a dimly lit, rain-streaked room." |
| Missing Camera | "A man walking" | Specify the shot: "Wide tracking shot of a man walking." |
| Lighting Omission | Leaving lighting up to the model's default | Always specify light: "Soft diffused morning light" or "Harsh dramatic rim lighting." |

## OUTPUT SHAPE

**When providing prompts to the user:**
1. State the Asset/Goal briefly.
2. Provide the raw, copy-pasteable prompt string inside a markdown quote `>`.
3. (Optional) Provide a 1-sentence rationale for the camera/lighting choices.

Example:
**Asset 1: The Monolith Room**
> `Wide 16:9 architectural shot of a monolithic brutalist living room, raw board-formed concrete walls, massive floor-to-ceiling windows looking into a dark pine forest, photorealistic interior design photography, soft volumetric sunlight piercing through the glass, deep chiaroscuro shadows, desaturated bone gray and obsidian black color palette, 35mm lens, 8k resolution, highly detailed.`

## NON-NEGOTIABLE CHECKLIST

- [ ] Prompt begins with Shot Type/Composition and Subject.
- [ ] Lighting is explicitly defined in physical terms.
- [ ] Video prompts contain explicit Camera Movement and Scene Motion.
- [ ] Vague, conceptual adjectives have been replaced with physical visual descriptors.
- [ ] The prompt is formatted as a copy-pasteable string in the specified structure.
