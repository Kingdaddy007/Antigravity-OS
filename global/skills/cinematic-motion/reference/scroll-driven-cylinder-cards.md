# Scroll-Driven Cylinder Cards

## Contents

- [Core Mechanic](#core-mechanic)
- [HTML Structure](#html-structure)
- [CSS Contract](#css-contract)
- [GSAP & TS Implementation](#gsap-ts-implementation)
- [Notes & Limitations](#notes-limitations)

Use this when you want a sequence of vertical sections to feel like cards rolling over a massive 3D cylinder. Unlike true overlapping parallax, these cards stack normally but use `rotateX` and 3D perspective to simulate depth.

## Core Mechanic

1. The parent container must have a `perspective` applied to establish 3D depth.
2. The child container (the card) uses `position: absolute` with an `inset` to create margins.
3. The child container must have `border-radius` to look like a physical card.
4. GSAP ScrollTrigger interpolates `rotationX` from `-15deg` (top of screen) to `15deg` (bottom of screen).
5. A secondary GSAP animation handles the standard vertical parallax of the image/video inside the card.

## HTML Structure

```html
<section class="room-section">
  <div class="room-video-container">
    <video autoplay muted loop playsinline src="video.mp4"></video>
  </div>
  <div class="room-caption">
    <h2>THE SALON</h2>
  </div>
</section>
```

## CSS Contract

```css
.room-section { 
  position: relative; 
  width: 100%; 
  height: 100svh; 
  display: flex; 
  align-items: flex-end; 
  padding: 6vw; 
  perspective: 1500px; /* Essential for the 3D tilt effect */
}

.room-video-container { 
  position: absolute; 
  inset: 1vh 3vw; /* Creates the gap around the card */
  z-index: -1; 
  overflow: clip; 
  border-radius: 40px; /* Essential for card aesthetic */
  pointer-events: none; 
}

.room-video-container video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  will-change: transform;
}
```

## GSAP & TS Implementation

```typescript
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const rooms = gsap.utils.toArray<HTMLElement>('.room-section');

rooms.forEach((room) => {
  const container = room.querySelector('.room-video-container');
  const media = room.querySelector('.room-video-container video');
  
  if (container && media) {
    // 1. The 3D Cylinder Tilt on the Card
    gsap.fromTo(container,
      { rotationX: -15, scale: 1 }, 
      {
        rotationX: 15, scale: 1,
        ease: "none",
        scrollTrigger: {
          trigger: room,
          start: "top bottom", 
          end: "bottom top",
          scrub: true
        }
      }
    );

    // 2. The Internal Media Parallax
    gsap.fromTo(media,
      { yPercent: -30 }, 
      {
        yPercent: 30, 
        ease: "none",
        scrollTrigger: {
          trigger: room,
          start: "top bottom", 
          end: "bottom top",
          scrub: true
        }
      }
    );
  }
});
```

## Notes & Limitations
- If you use `scale` > 1 on the container, the expanded size will eat up the `inset` margins, causing the card to bleed off the edge of the screen when `rotateX` reaches `0` (flat in the center of the viewport). If you want larger cards, use smaller `inset` values instead of GSAP scaling.
- This creates a sequential block stack. If you want cards to truly slide *over* one another, use `infinite-parallax-gallery-loop.md` instead.
