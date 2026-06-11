# Layered Z-Axis Depth Zoom (Telescope Scroll)

## Visual Description
As the user scrolls down, a massive central typography lockup splits horizontally down the middle, pulling apart like steel elevator doors. Simultaneously, a floating array of smaller background images rushes past the camera on the Z-axis, simulating moving physically forward through a debris field. Overlaid on the background are 6 identical copies of the main image, masked to a specific subject (e.g., a crab). These masks start at staggered scale sizes and heavy blur. As the scroll progresses, they snap into perfect 1:1 scale alignment with the background and lose their blur, creating a momentary "trailing ghost" depth effect that clicks into absolute clarity.

## Emotional Register
Cinematic, deeply immersive, and vast. Gives the user a profound sense of forward momentum and atmospheric depth.

## Technical Mechanics
* **DOM Structure:** Complex, heavy layering. Floating grid `.section__images`, split text `<span class="left">`, and 6 duplicated foreground layers `.section__media__front` utilizing CSS `mask-image`.
* **CSS Properties:** `perspective: 100vh` on the main container. Transforms utilizing `translate3d()`, `scale(var(--progress))`. `filter: blur(2px)` mapped to the ghost layers.
* **JS Engine:** GSAP ScrollSmoother (`normalizeScroll: true`), ScrollTrigger.
* **Key Timeline Logic:** Tied directly to scrubbed scroll. Custom `--progress` CSS variable updated via `onUpdate` to drive CSS transform changes. Staggered `.to()` tweens handle the Z-axis explosion (`z: "100vh"`).
* **Easing Curve:** `power1.inOut` applied to the parsed progress value to ensure a smooth acceleration and deceleration curve during the physical scroll action.
* **Performance Notes:** Requires the browser to render a high-resolution primary image 7 times simultaneously. Presents an extreme mobile performance risk and high memory payload.

## Code Snippet / Reverse Engineering Brief
```javascript
import gsap from "gsap";
import ScrollTrigger from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

// Example configuration within a class or component setup
const sectionDOM = document.querySelector(".section");
const frontImages = document.querySelectorAll(".section__media__front");

const timeline = gsap.timeline({
  scrollTrigger: {
    trigger: sectionDOM,
    start: "top top",
    end: "+=200vh", // Extended scroll distance for smoother scrub
    pin: true,
    scrub: 1, // Smooth scrub
    onUpdate: (self) => {
      // Syncing custom progress variable
      const easedProgress = gsap.parseEase("power1.inOut")(self.progress);
      sectionDOM.style.setProperty("--progress", easedProgress);
    }
  }
});

// Z-axis explosion and fading out blur progressively from the end of the stack
timeline.to(frontImages, {
  duration: 1,
  filter: "blur(0px)",
  scale: 1, // Example of resolving scale using timeline rather than CSS var
  ease: "power1.inOut",
  stagger: { amount: 0.2, from: "end" }
}, 0);
```

## Metadata
- **Industry Name(s):** Telescope Zoom, 3D Z-Axis Parallax, Layered Depth Masking
- **Rarity:** UNCOMMON
- **Implementation Confidence:** HIGH
- **Production Feasibility:** LOW (The necessity to duplicate a high-res image multiple times and apply CSS masking and filters creates a severe GPU bottleneck)
- **Accessibility / Reduced Motion:** Revert to a standard scrolling flow and disable the deep Z-axis layer duplicates to prevent visual confusion and nausea.
