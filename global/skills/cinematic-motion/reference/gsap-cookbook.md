# GSAP Cookbook

Use these templates for spatial storytelling implementation. Keep GSAP scoped, disposable, and tied to the motion board.

## Registration

```js
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);
```

## Scoped React Pattern

```jsx
import { useEffect, useRef } from "react";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

export function SpatialSection() {
  const rootRef = useRef(null);

  useEffect(() => {
    const ctx = gsap.context(() => {
      // timelines here
    }, rootRef);

    return () => ctx.revert();
  }, []);

  return <section ref={rootRef} />;
}
```

## ScrollTrigger Scrub

```js
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".chapter",
    start: "top top",
    end: "+=180%",
    scrub: 0.8,
    pin: true,
    anticipatePin: 1,
    invalidateOnRefresh: true
  }
});
```

Use `scrub: true` for precise mechanical motion. Use `scrub: 0.6-1.2` for heavy interior/gallery motion.

## Stacked Room Panels

```js
const panels = gsap.utils.toArray(".room-panel");

panels.slice(1).forEach((panel) => {
  gsap.set(panel, { yPercent: 100 });
});

const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".room-stack",
    start: "top top",
    end: () => `+=${panels.length * window.innerHeight}`,
    scrub: 0.8,
    pin: true
  }
});

panels.slice(1).forEach((panel) => {
  tl.to(panel, { yPercent: 0, ease: "none", duration: 1 });
});
```

## Curtain Split Arrival

```js
const tl = gsap.timeline({ defaults: { ease: "expo.out" } });

tl.to(".curtain-left", { xPercent: -100, duration: 1.35 })
  .to(".curtain-right", { xPercent: 100, duration: 1.35 }, "<")
  .from(".hero-room", { scale: 1.04, opacity: 0, duration: 1.1 }, "-=0.75")
  .from(".hero-caption", { y: 18, opacity: 0, duration: 0.7 }, "-=0.45");
```

## Zero-Safe Modulo Carousel

```js
const getIndexAt = (currentIndex, offset, length) => {
  const target = currentIndex + offset;
  return ((target % length) + length) % length;
};
```

Use for circular project indexes, material swatches, gallery rails, and motif-driven card systems.

## Living Mockup Ticker

```js
const values = [
  { label: "Sourcing", value: "Italian limestone" },
  { label: "Install window", value: "Sep 18-22" },
  { label: "Finish", value: "Warm plaster" }
];

const startTicker = (setState) => {
  let index = 0;
  const id = window.setInterval(() => {
    index = getIndexAt(index, 1, values.length);
    setState(values[index]);
  }, 2200);

  return () => window.clearInterval(id);
};
```

Use for living proof panels, not fake metrics. Values must be plausible for the studio's method.

## Ambient Loop

```js
const ambient = gsap.to(".dust-layer", {
  x: 10,
  y: -8,
  rotation: 0.4,
  duration: 12,
  repeat: -1,
  yoyo: true,
  ease: "sine.inOut"
});

ScrollTrigger.create({
  trigger: ".scene",
  onEnter: () => ambient.play(),
  onLeave: () => ambient.pause(),
  onEnterBack: () => ambient.play(),
  onLeaveBack: () => ambient.pause()
});
```
