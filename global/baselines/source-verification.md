# Volatile Source Verification Baseline

Verification date: 2026-07-13

## Rule

Volatile platform, legal, API, pricing, product-limit, and tool-version claims require a primary source and a verification date. If no current primary source supports a claim, mark it unverified, quarantine it as historical research, and do not make production decisions from it.

## Current Records

| Area | Verified claims | Primary source | Result |
| --- | --- | --- | --- |
| Seedance 2.0 | Four input modalities; up to 9 image, 3 video, and 3 audio references; editing and extension; 15-second multi-shot audio-video output; dual-channel audio; authorization requirement for real-person portraits | [ByteDance official launch, 2026-02-12](https://seed.bytedance.com/blog/seedance-2-0-official-launch) | Verified 2026-07-13 |
| Seedance legal/API/filter narratives | Named-party enforcement causes, public API status, filter block rates, suspension dates, and universal prompt limits | No supporting current ByteDance primary source located in this pass | Unverified; historical only |
| Deriv Bot | Deriv Bot is a block-based strategy builder; strategies can be saved and imported as XML; Blockly V10 made variable names case-insensitive | [Deriv Help Centre](https://deriv.com/help-centre), [Deriv-admin Blockly V10 notice](https://community.deriv.com/t/important-google-blockly-update-v10-affects-deriv-bot-xml-files/87246) | Verified 2026-07-13 |
| Deriv XML internals | Exact block IDs, ordering, parser versions, and contract mappings | No stable public first-party schema located in this pass | Verify against a fresh official export and demo-account import |
| Google Flow / Veo / Gemini Omni | Flow is the creative interface; current Flow help lists Veo 3.1 Lite, Fast, Quality, and Gemini Omni Flash with model-dependent generation/editing features | [Flow model and feature help](https://support.google.com/flow/answer/16352836?hl=en), [Flow launch announcement](https://blog.google/innovation-and-ai/products/google-flow-veo-ai-filmmaking-tool/), [Gemini Omni](https://deepmind.google/models/gemini-omni/) | Verified 2026-07-13; recheck the active account UI before relying on labels, limits, availability, or credits |

## Reverification Trigger

Reverify before production use, when the active surface differs by region, when a dated record is older than 90 days, or when observed behavior conflicts with this baseline.
