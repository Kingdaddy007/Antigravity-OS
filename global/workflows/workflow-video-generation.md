---
id: video-generation
version: 1
status: active
intent: Plan and draft provider-aware AI video work with explicit current-capability checks.
use_when: [video prompt, video storyboard, AI video, Google Flow, Veo, Gemini Omni, Seedance, model comparison]
do_not_use_when: [CSS animation, frontend motion, editing an existing finished video, ordinary image generation]
inputs: [creative goal, provider or interface, model label if known, duration, aspect ratio, references, audio intent, delivery target]
required_resources: [video-generation skill, provider reference when applicable, active project context]
mutation_class: read_only
approval_gates: [confirm reference upload, paid generation, external service use, publishing, or delivery]
states: [identify-provider, inspect-current-capabilities, plan-shot, draft, review, deliver]
outputs: [provider/model record, creative brief, shot plan, copy-pasteable prompt, continuity locks, verification checklist]
verification: [exact provider/model recorded, volatile claims sourced or marked unverified, prompt fields complete, approval gates recorded]
failure_paths: [ask for missing provider or goal, quarantine unsupported capability claims, never claim generation or upload occurred without evidence]
resume_contract: task-scoped .agents/workflows/<task-id>.json using the workflows directory contract
next_workflows: [review-code, verify-project]
profiles: [general, spatial]
---

# WORKFLOW: VIDEO GENERATION

1. Identify whether the user means a platform/interface, a model, or a provider.
2. Inspect current model capabilities and record what is verified versus uncertain.
3. Build the shot plan and prompt using the video-generation skill.
4. Review continuity, safety, rights, audio, duration, and delivery constraints.
5. Stop for approval before uploading references, spending credits, using an external service, publishing, or delivering externally.
6. Return the prompt, evidence, and next action; do not imply that a video was generated unless the host provides execution evidence.
