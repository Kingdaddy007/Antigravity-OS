---
name: video-generation
description: Use when planning, prompting, routing, or reviewing AI-generated video across Google Flow/Veo/Gemini Omni, Seedance, or another named provider. Do not use for ordinary frontend animation, CSS transitions, or editing a finished video file.
---

# Video Generation

## WHEN TO USE THIS

- The user wants a video concept, shot plan, prompt, storyboard, continuity plan, or model/provider recommendation.
- The user names Google Flow, Veo, Gemini Omni, Seedance, or another video-generation surface.
- The user wants to compare a provider’s current model options before drafting a prompt.

## NEVER DO

- Never claim that a platform label, duration, cost, region, or capability is current without checking the active provider surface or a dated primary source.
- Never treat Flow (an interface) as if it were the same thing as Veo, Gemini Omni, or Seedance (model/provider choices).
- Never upload references, publish media, spend credits, or contact an external service without a just-in-time approval gate.
- Never use this skill for CSS/UI motion; route that work to `cinematic-motion`, `motion-library`, or the relevant UI workflow.

## ROUTING

1. Identify the platform/interface, provider, model label, intended output, and constraints.
2. If the platform is Google Flow, load `references/google-flow.md`; treat the model list as a current snapshot and inspect the user’s active UI.
3. If the provider is Seedance, load `references/seedance-routing.md` and then the existing `seedance` skill or one of its targeted child skills.
4. Otherwise ask for the provider documentation or record the capability as unverified before relying on it.
5. Build the creative brief before writing a final prompt: subject, action, setting, shot, camera, temporal beats, audio, continuity, aspect ratio, duration, and delivery target.

## REFERENCE LOADING RULES

- Always read this skill’s reference index rules before selecting a provider reference.
- Load `references/google-flow.md` only for Google Flow, Veo, Gemini Omni, or an “OmniVision” alias.
- Load `references/seedance-routing.md` only for Seedance or a ByteDance/Dreamina/Jimeng request.
- Load both when the user is comparing Google and Seedance; keep claims and approval gates separate.
- Do not load dated provider details for unrelated coding, UI, or post-production tasks.

## OUTPUT SHAPE

Return:

1. Provider/interface and exact model label (or an explicit “verify in current UI” note).
2. Creative brief and shot-by-shot temporal plan.
3. Copy-pasteable prompt(s), separated from explanation.
4. Reference assets and continuity locks.
5. Verification checklist and any approval needed for upload, generation, publishing, or paid credits.

## NON-NEGOTIABLE CHECKLIST

- [ ] Interface, provider, and model are not conflated.
- [ ] Current or volatile claims have a primary source/date or are marked unverified.
- [ ] Camera movement, subject motion, duration, and audio intent are explicit.
- [ ] Character/product/environment continuity is locked where needed.
- [ ] External uploads, paid generation, publishing, and other mutations stop for approval.
- [ ] Final output is usable without requiring the user to infer missing fields.
