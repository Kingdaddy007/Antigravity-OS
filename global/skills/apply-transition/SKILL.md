---
name: apply-transition
description: 'Use this skill when the user wants to apply a pre-built CSS transition or animation from the loading.io transition.css library to a specific element. Activated by "/apply-transition", "apply ripple", "apply loading.io transition", or when the user asks to animate an element using a CSS class effect.'
---

# Transition.css Integration & Application

## PURPOSE
This skill provides a standardized, instant way for the agent to apply high-quality CSS animations from the `transition.css` library without requiring manual CSS keyframe authoring.

## WHEN TO USE THIS
- When the user types `/apply-transition [effect] to [element]`
- When the user asks to "apply ripple" or "apply fade-in" to a specific button, image, or section.
- When you need a quick, reliable structural animation for an interaction state.

## AVAILABLE EFFECTS
The library is already installed in `src/utils/transition.min.css`. Use these specific elite effects for the BEVAMPED aesthetic:
- **Ripple**: `ld-ripple` (Best for buttons)
- **Blur-In**: `ld-blur-in` (Best for image reveals)
- **Fade-In**: `ld-fade-in` (Best for text/captions)
- **Focus**: `ld-focus-in` (Cinematic text entry)
- **Squeeze**: `ld-squeeze-in` (Structural/Industrial vibe)

## EXECUTION INSTRUCTIONS
When this skill is triggered, you MUST:
1. Locate the HTML file containing the target element.
2. Identify the specific HTML tag (e.g., `<button class="cta-btn">`).
3. Inject the `ld` base class AND the specific effect class (e.g., `ld-ripple`).
4. **Trigger State**: 
   - If the user wants it to happen on hover, also add the `ld-hover` class.
   - If the user wants it to loop infinitely, add the `x1`, `x2`, or `xhalf` speed classes or just let it loop natively depending on the effect.
   - If it should trigger via scroll, use GSAP to toggle the class in the `.ts` file instead.

**Example implementation:**
```html
<!-- Before -->
<button class="inquiry-btn">Submit</button>

<!-- After (Hover Ripple) -->
<button class="inquiry-btn ld ld-hover ld-ripple">Submit</button>
```

Do NOT ask for permission to apply the code. Execute the modification immediately and confirm completion.
