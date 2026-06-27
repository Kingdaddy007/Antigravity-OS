# Transition.css (Loading.io) Integration

## Overview
The `transition.css` library by loading.io is installed in the project at `src/utils/transition.min.css`. It provides a suite of pre-built, high-quality CSS animations (like ripples, fades, bounces, and flips) that can be triggered simply by appending CSS classes to an element.

## How to Trigger
To instruct Anti-Gravity to use a transition from this library, the user can use the following "Command Line" / Trigger Phrase in the chat:

**Command Pattern:**
> `/apply-transition [effect-name] to [element-description]`
> *Example: "/apply-transition ripple to the hero button"*
> *Example: "/apply-transition fade-in to the common questions"*

When this trigger is used, the Agent must:
1. Identify the target element in the HTML.
2. Add the base class `ld` to the element.
3. Add the specific animation class (e.g., `ld-ripple`).
4. (Optional) If it should trigger on hover, add `ld-hover`.
5. (Optional) If it should be triggered via JavaScript/ScrollTrigger, toggle the classes in the TS file.

## Available Elite Effects for BEVAMPED
While there are dozens of effects, these are the recommended ones that fit the high-end, structural aesthetic:
- **Ripple (Material/Fluid):** `ld-ripple` (Best for buttons or image overlays)
- **Blur (Depth of Field):** `ld-blur-in` / `ld-blur-out`
- **Focus (Cinematic):** `ld-focus-in`
- **Fade (Classic):** `ld-fade-in`
- **Squeeze (Structural):** `ld-squeeze-in`

## Implementation Example
To make a button ripple continuously:
```html
<button class="cta-btn ld ld-ripple">Click Me</button>
```

To make an image blur in on hover:
```html
<img src="house.jpg" class="portfolio-image ld ld-hover ld-blur-in">
```

If you (the Agent) read this file, you now have the context to execute any `transition.css` request seamlessly.
