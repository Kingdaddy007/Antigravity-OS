---
name: motion-library
description: >
  Use this skill when the user wants to browse, find, or apply a pre-built animation, transition, GSAP effect, or WebGL motion from the existing references. Activated by "/motion-library", "/effect", "/apply-motion", "find a transition", "show me effects", or "what animations do we have".
---

# Motion Library Index & Router

## PURPOSE
This skill acts as a direct router to the vast library of cinematic motion references, transitions, and effects stored within the `cinematic-motion` reference folders. It ensures the agent knows exactly where to look for pre-built motion strategies before trying to write animations from scratch.

## WHEN TO USE THIS
- When the user types `/motion-library`, `/effect`, `/apply-motion`, or `/transition`.
- When the user asks "what transitions do we have?" or "apply an effect here."
- When you are tasked with adding motion and need to consult the reference library to see what is already available.

## INSTRUCTIONS FOR THE AGENT
When this skill is triggered, you MUST immediately execute the following steps:

1. **Acknowledge and List**: Run the `list_dir` tool on the following two directories to see what elite effects and references are currently available:
   - `C:\Users\godsw\.gemini\config\skills\cinematic-motion\reference\`
   - `C:\Users\godsw\.gemini\config\skills\cinematic-motion\reference\motion-library\` (and its subdirectories)
   
2. **Read the Reference**: Once you identify a file or effect that matches the user's request (e.g., `loading-io-transitions.md`, `scroll-driven-3d-cube.md`, `transition-library.md`), run `view_file` to read the exact implementation instructions.

3. **Present Options (If Vague)**: If the user just asked "show me effects" or triggered the slash command without a specific target, present a curated, visually formatted markdown list of the best available effects found in those directories. Use bold text and short descriptions so the user can easily pick one.

4. **Apply (If Specific)**: If the user asked to apply a specific effect to a specific element (e.g., "apply the ripple effect to the submit button"), execute the code modification immediately using the exact code patterns defined in the reference file.

## WHY WE DO THIS
We do not write generic animations from scratch. We rely on the highly-crafted, premium motion references stored in our library to maintain the "BEVAMPED" luxury aesthetic. This skill guarantees you always consult the library first, saving time and ensuring quality.
