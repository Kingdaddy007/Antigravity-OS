# Lenis GSAP Scroll Foundation

## Contents

- [When To Use](#when-to-use)
- [Core Rule](#core-rule)
- [Vanilla GSAP Pattern](#vanilla-gsap-pattern)
- [React / Next.js Pattern](#react-nextjs-pattern)
- [Parallax QuickSetter Pattern](#parallax-quicksetter-pattern)
- [Snap](#snap)
- [Nested Scroll And Modals](#nested-scroll-and-modals)
- [Infinite Scroll](#infinite-scroll)
- [Quality Gate](#quality-gate)

Use this when a spatial website needs smooth scroll that drives GSAP ScrollTrigger, parallax, frame sequences, infinite galleries, or WebGL camera choreography.

Sources:

- Lenis repository: https://github.com/darkroomengineering/lenis
- Lenis React package: `external-references/lenis/packages/react/README.md`
- Lenis Snap package: `external-references/lenis/packages/snap/README.md`
- Next.js Lenis example: https://github.com/codebucks27/Smooth-Scroll-Next.js

## When To Use

- Scroll-driven interior showroom pages.
- GSAP ScrollTrigger scenes with smooth scroll.
- Canvas frame sequences.
- Parallax room/material galleries.
- Infinite showroom loops.
- Next.js/React spatial sites that need a stable smooth-scroll wrapper.

## Core Rule

Lenis is the scroll foundation, not the concept. It must support the approved `showroom-choreography.md`, not become a decorative smoothness layer.

## Vanilla GSAP Pattern

```js
import Lenis from 'lenis';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true,
  anchors: true
});

lenis.on('scroll', ScrollTrigger.update);

gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});

gsap.ticker.lagSmoothing(0);
```

Rules:

- Use `anchors: true` when navigation links must scroll to sections.
- Connect Lenis to `ScrollTrigger.update`.
- Drive Lenis through GSAP ticker when GSAP controls the motion system.
- Disable GSAP lag smoothing to avoid delayed scroll animation response.

## React / Next.js Pattern

```jsx
'use client';

import { ReactLenis } from 'lenis/react';

export function SmoothScrollProvider({ children }) {
  return (
    <ReactLenis root options={{ duration: 1.2, anchors: true }}>
      {children}
    </ReactLenis>
  );
}
```

For GSAP integration:

```jsx
import { ReactLenis } from 'lenis/react';
import gsap from 'gsap';
import { useEffect, useRef } from 'react';

export function SmoothScrollProvider() {
  const lenisRef = useRef(null);

  useEffect(() => {
    function update(time) {
      lenisRef.current?.lenis?.raf(time * 1000);
    }

    gsap.ticker.add(update);
    return () => gsap.ticker.remove(update);
  }, []);

  return <ReactLenis root options={{ autoRaf: false }} ref={lenisRef} />;
}
```

Rules:

- Use a client component in Next.js.
- Import `lenis/dist/lenis.css` where the app expects global CSS.
- Use the modern `lenis/react` package for new work.
- Treat older `@studio-freight/react-lenis` examples as migration references only.

## Parallax QuickSetter Pattern

The Codebucks example shows a useful lightweight parallax pattern:

```js
const setY = gsap.quickSetter(target.current, 'y', 'px');

gsap.timeline({
  scrollTrigger: {
    trigger: trigger.current,
    start: 'top bottom',
    end: 'bottom top',
    scrub: true,
    onUpdate: (self) => setY(self.progress * distance)
  }
});
```

Interior adaptation:

- Use small parallax distances for room photography.
- Tie speed to depth layer: foreground moves more, background less.
- Do not parallax text and room evidence in a way that causes collisions.
- Use this for image lists, material studies, and editorial project previews.

## Snap

Use `lenis/snap` when sections must land as deliberate scenes:

```js
import Snap from 'lenis/snap';

const snap = new Snap(lenis, {
  type: 'mandatory',
  debounce: 500,
  duration: 0.9
});

snap.addElements(document.querySelectorAll('.showroom-section'), {
  align: 'start'
});
```

Use:

- showroom panel loops
- full-screen room chapters
- portfolio project procession
- reading moments where copy must not flash past

Avoid:

- snapping forms while the visitor is typing
- snapping every small section
- trapping inquiry behind mandatory scroll choreography

## Nested Scroll And Modals

Use one of:

```html
<div data-lenis-prevent>...</div>
```

or:

```js
const lenis = new Lenis({
  prevent: (node) => node.id === 'modal'
});
```

Use this for:

- project modals
- inquiry forms
- material selectors
- private portfolio panels

## Infinite Scroll

Lenis supports `infinite: true`, but use it only through `infinite-parallax-gallery-loop.md` or another authored loop mechanic.

Rules:

- Require an exit path to project or inquiry.
- Hide duplicate loop content from assistive technology.
- Provide finite mobile/reduced-motion fallback.

## Quality Gate

Reject the setup if:

- Lenis breaks anchor navigation.
- ScrollTrigger is not synchronized.
- Motion remains active behind modals/forms.
- Mobile touch behavior is unstable.
- Reduced motion has no alternate path.
- Smooth scrolling is used to make a generic layout feel premium.
