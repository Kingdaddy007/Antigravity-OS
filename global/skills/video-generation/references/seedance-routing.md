# Seedance Routing

Seedance is a separate provider/model family from Google Flow, Veo, and Gemini Omni. For a Seedance request, load the canonical `seedance` skill and only the child references needed for the task (for example camera, characters, audio, motion, or prompt-short).

Keep provider claims separate. Do not transfer Flow model names, controls, durations, credits, or upload assumptions into Seedance. Verify volatile Seedance behavior against the current official source recorded in `global/baselines/source-verification.md` before production use.

If the user is comparing providers, return a capability comparison and an explicit verification note rather than silently converting one provider’s prompt syntax into another’s.
