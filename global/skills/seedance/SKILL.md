---
name: seedance
description: Generate and direct Seedance video workflows using text, image, audio, and video references. Use for prompt direction, multimodal reference planning, scene consistency, audio design, troubleshooting, or post-processing.
license: MIT
---

# Seedance

## Verified Capability Baseline

As of 2026-07-13, ByteDance's official Seedance 2.0 launch material verifies:

- text, image, audio, and video inputs;
- combined reference input of up to 9 images, 3 video clips, and 3 audio clips;
- multimodal reference for composition, motion, camera, visual effects, and sound;
- video generation, editing, and extension;
- 15-second high-quality multi-shot audio-video output and dual-channel audio;
- identity verification or prior legal authorization for real-person portrait references.

See [platform constraints](references/platform-constraints.md) and [source verification](../../baselines/source-verification.md) before relying on platform limits or availability. Dated filter behavior, API status, named-party enforcement narratives, prompt-length claims, pricing, and surface-specific controls are not part of the verified baseline.

## Routing

Choose the smallest applicable skill:

- Vague concept or guided direction: `seedance-interview` or `seedance-interview-short`.
- Direct prompt construction: `seedance-prompt` or `seedance-prompt-short`.
- Camera, motion, lighting, characters, style, VFX, or audio: load only that specialist skill.
- Known genre structure: `seedance-recipes`.
- Failed output: `seedance-troubleshoot`.
- Copyright, likeness, or brand risk: `seedance-copyright`.
- Post-processing or automation: `seedance-pipeline`.

Language vocabulary and worked-example skills are optional references, not prerequisites.

## Core Workflow

1. Confirm the active surface and discover its current controls.
2. Identify the generation mode and available referenced assets.
3. Define subject, action, environment, camera, timing, style, lighting, audio, and continuity constraints.
4. Use references for information they can convey more reliably than prose.
5. Keep the prompt concise enough for the active surface; do not claim a universal character limit without current official evidence.
6. Generate a low-risk test, inspect drift and failure modes, then revise one causal dimension at a time.
7. Obtain authorization for any external upload, purchase, publication, or use of a real person's likeness.

## Evidence Rules

- Treat all February-March 2026 operational claims outside the verified baseline as historical snapshots.
- Verify current platform behavior using official ByteDance documentation and the active product surface.
- If official evidence is unavailable, label the claim unverified and avoid production dependency on it.
- Community examples may inspire prompts but cannot establish legal, policy, API, pricing, or model-limit facts.

## Conditional References

Start with [resource-index.md](references/resource-index.md) and load only the references needed for the task. Historical package changes live in [version-history.md](references/version-history.md); they are not runtime platform facts.
