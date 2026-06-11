# Text Path Morphing (SVG Text Distortion)

## Visual Description
Text rendered as SVG `<text>` or converted to `<path>` elements, allowing individual letter outlines to be morphed via animated SVG path data. Letters can stretch, compress, wave, or distort along Bezier curves. The effect is liquid and organic — letterforms appear to bend, drip, or flow. Unlike CSS transforms (which are rigid affine transformations), path morphing can create non-uniform distortions where the top of a letter moves independently from the bottom. Often used for loading states, hover interactions, or rhythmic background elements. Requires matching point counts between start and end paths for smooth interpolation.

## Emotional Register
Playful, fluid, experimental, organic. Breaks the rigidity of digital type and introduces handcrafted or natural motion. Appropriate for creative agencies, music/art brands, and editorial experiments.

## Technical Mechanics
* **DOM Structure:** SVG `<text>` element converted to `<path>` (can use GSAP's DrawSVG or custom conversion)
* **CSS Properties:** N/A (SVG attributes manipulated)
* **JS Engine:** GSAP with MorphSVGPlugin (premium) or custom path interpolation
* **Key Timeline Logic:** `.to(textPath, {morphSVG: alteredPath, duration: 1.5, ease: "elastic.out(1, 0.5)"})`
* **Easing Curve:** `elastic.out` or `back.out` for bounce, `power2.inOut` for smooth flow
* **Performance Notes:** Path morphing can be CPU-intensive for complex shapes; use simplified paths when possible. Not suitable for body text or small sizes (legibility issues).

## Code Snippet / Reverse Engineering Brief
GSAP's MorphSVGPlugin (premium/members-only) is the industry standard, but source code is proprietary. To recreate without plugin:

1. **Convert Text to Paths**: Use tool like `textToSVG` (Node) or Adobe Illustrator to convert typography to `<path>` elements.
2. **Match Point Counts**: Both start and end paths must have identical number of points. Use SVG path manipulation libraries (e.g., `flubber.js`) to interpolate between shapes.
3. **Animate Path Data**: Use GSAP to animate the `d` attribute of the `<path>` element from start shape to morphed shape.
4. **Define Morph Targets**: Create alternate path shapes (waved, stretched, etc.) manually in design tool or mathematically via Bezier curve manipulation.
5. **Timing**: Use 1-2 second duration with `elastic.out` or `back.out` easing for bouncy morph.

Alternative: Use `filter: url(#displacement)` with animated SVG displacement maps for pseudo-morphing without path manipulation.

## Metadata
- **Industry Name(s):** SVG Text Morph, Path-Based Type Animation, Bezier Text Warp
- **Rarity:** RARE
- **Implementation Confidence:** MEDIUM (requires premium plugin or complex custom implementation)
- **Production Feasibility:** LOW without GSAP Club membership; MEDIUM with plugin.
- **Accessibility / Reduced Motion:** For `prefers-reduced-motion`, show static final path with no morphing. Ensure SVG has `role="img"` and `<title>` element for screen readers. Test contrast at all morph states.
