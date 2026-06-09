# Infinite Parallax Gallery Loop

Use this when a spatial website needs the feeling of an endless private showroom, gallery corridor, material archive, or portfolio reel. Adapted from Joe Ben Taylor's "Infinite Scroll with Parallax" demo and Codrops tutorial.

Sources:

- Repository: https://github.com/joebentaylor1995/infinite-scroll-with-parallax
- Live demo: https://joebentaylor1995.github.io/infinite-scroll-with-parallax/
- Codrops tutorial: https://tympanus.net/codrops/2026/05/28/the-never-ending-story-building-a-seamless-infinite-scroll-experience-with-gsap-lenis/
- CodePen: https://codepen.io/joebentaylor/pen/emBEyNa

## When To Use

- Portfolio preview before deeper project chapters.
- Material or room archive that should feel like a continuous gallery wall.
- Taste-world introduction where multiple rooms prove range without becoming a grid.
- Designer's-eye reel: details, objects, textures, thresholds, light, and rooms passing as a curated sequence.
- Transitional showroom corridor between Atmosphere and Proof.

## Never Use

- As decorative endless scrolling with no proof or inquiry path.
- For important copy that needs normal reading flow.
- When there are fewer than three strong scenes.
- When mobile/reduced-motion fallback cannot preserve the same content.
- With licensed demo images or assets from the source repository.

## Core Mechanic

The loop is a staged illusion:

1. Create fullscreen sections.
2. Duplicate the first section at the end.
3. Hide the duplicate from assistive technology with `aria-hidden`.
4. Enable Lenis infinite scrolling.
5. Add snap control so each section lands deliberately.
6. Proxy ScrollTrigger to the Lenis wrapper when using a custom scroll container.
7. Animate section media with GSAP parallax while each section crosses the viewport.

The effect works because the visitor feels a continuous showroom, while the browser sees a carefully disguised loop.

## Required Structure

```html
<div class="wrapper">
  <div class="content">
    <section class="loop-panel">
      <picture class="loop-media"><img src="..." alt="..." /></picture>
      <div class="loop-caption">...</div>
    </section>
    <section class="loop-panel">...</section>
    <section class="loop-panel">...</section>
    <section class="loop-panel" aria-hidden="true">
      <picture class="loop-media" aria-hidden="true">
        <img src="..." alt="" aria-hidden="true" />
      </picture>
    </section>
  </div>
</div>
```

Rules:

- Use at least three real panels before the duplicate.
- Duplicate only the first panel at the end.
- Keep duplicate content hidden from screen readers.
- Do not duplicate inquiry forms, navigation landmarks, or primary CTAs.

## CSS Contract

```css
.wrapper {
  position: relative;
  height: 100svh;
  overflow: hidden;
}

.loop-panel {
  position: relative;
  display: grid;
  place-items: center;
  width: 100%;
  height: 100svh;
  overflow: clip;
}

.loop-media {
  position: absolute;
  inset: 0;
  z-index: -1;
}

.loop-media img,
.loop-media video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

Rules:

- Use `100svh` for viewport sections to reduce mobile browser toolbar issues.
- Use `overflow: hidden` on wrapper and `overflow: clip` on panels.
- Keep media full-bleed, but preserve text-safe zones in the source asset.

## JavaScript Contract

```js
gsap.registerPlugin(ScrollTrigger);

const wrapper = document.querySelector(".wrapper");
const content = document.querySelector(".content");

const lenis = new Lenis({
  infinite: true,
  wrapper,
  content,
  syncTouch: true
});

const snap = new Snap(lenis, {
  type: "mandatory",
  debounce: 500,
  duration: 0.9,
  easing: (t) => 1 - Math.pow(1 - t, 4)
});

snap.addElements(document.querySelectorAll(".loop-panel"), {
  align: "start"
});

ScrollTrigger.scrollerProxy(wrapper, {
  scrollTop(value) {
    if (arguments.length) lenis.scrollTo(value, { immediate: true });
    return lenis.scroll;
  },
  getBoundingClientRect() {
    return {
      top: 0,
      left: 0,
      width: wrapper.clientWidth,
      height: wrapper.clientHeight
    };
  },
  pinType: "transform"
});

lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);
```

Parallax panel animation:

```js
document.querySelectorAll(".loop-panel").forEach((panel) => {
  const media = panel.querySelector(".loop-media");

  gsap.fromTo(
    media,
    { yPercent: -50 },
    {
      yPercent: 50,
      ease: "none",
      scrollTrigger: {
        scroller: wrapper,
        trigger: panel,
        start: "top bottom",
        end: "bottom top",
        scrub: true,
        fastScrollEnd: true
      }
    }
  );
});
```

Rules:

- Use `ScrollTrigger.scrollerProxy` when Lenis uses a custom wrapper.
- Add `scroller: wrapper` to all ScrollTriggers inside the loop.
- Keep parallax simple. Depth comes from the media lag, not from many competing transforms.
- Avoid pinning inside the infinite loop unless there is a strong reason.

## Spatial Adaptation

Use the loop as a **showroom corridor**, not a generic carousel.

Each panel must have:

```text
Panel:
Journey stage:
Belief/proof job:
Room/material/object:
Image/video prompt source:
Caption:
Text-safe zone:
Parallax depth role:
Click/tap destination:
Fallback:
```

Interior use cases:

- Gallery wall of signature projects.
- Material archive: stone, linen, timber, plaster, metal, glass.
- Threshold reel: doorway, corridor, curtain, stair, arch, gallery portal.
- Designer's eye reel: close detail -> selected object -> room context.
- Before/after preview loop, with deeper chapters outside the loop.

## Prompt Requirements

Loop assets still inherit from `cinematic-prompt-pack.md`.

Each panel prompt must include:

- Strategic Source block.
- Same crop ratio and light discipline across the loop.
- Clear text-safe zone.
- Foreground/midground/background role.
- Whether the image must work as the duplicate seam.
- Negative prompt against stock-gallery sameness.

## Mobile And Reduced Motion

- Mobile default: replace infinite loop with a finite stacked chapter sequence or swipe/tap gallery.
- Reduced motion: static panels with normal scroll; no infinite Lenis loop.
- Keep all panels reachable without scroll trapping.
- Do not hide the inquiry path after the loop.

## Quality Gate

Reject the mechanic if:

- It does not support atmosphere, taste, proof, or portfolio browsing.
- The visitor can keep scrolling forever without reaching an inquiry path.
- Repeated panels feel like a screensaver.
- The duplicate seam is visible.
- Screen readers encounter duplicate content.
- Mobile becomes jittery or impossible to navigate.

## Output

When this mechanic is selected, add it to `contexts/spatial/showroom-choreography.md` as:

```text
Mechanic: Infinite Parallax Gallery Loop
Purpose:
Panels:
Duplicate seam strategy:
Lenis wrapper:
ScrollTrigger scroller:
Snap behavior:
Parallax range:
Mobile fallback:
Reduced-motion fallback:
Exit path to project/inquiry:
```
