# Scroll-Driven 3D Cube

## Contents

- [Concept](#concept)
- [Spatial Use Cases](#spatial-use-cases)
  - [Architectural Room Box](#architectural-room-box)
  - [Material Plinth](#material-plinth)
- [Required Context Before Implementation](#required-context-before-implementation)
- [Prompt Inheritance Rules](#prompt-inheritance-rules)
- [HTML](#html)
- [CSS](#css)
- [GSAP ScrollTrigger](#gsap-scrolltrigger)
- [Six-Sided Material Plinth Timeline](#six-sided-material-plinth-timeline)
- [Webflow Extraction Notes](#webflow-extraction-notes)
- [Composition Rules](#composition-rules)
- [Mobile And Reduced Motion](#mobile-and-reduced-motion)
- [Quality Gate](#quality-gate)
- [Anti-Patterns](#anti-patterns)

## Concept

**Name:** The Architectural Room Box or Material Plinth

Use this reference when a high-end interior, architecture, furniture, decor, or material website needs a scroll-controlled CSS 3D cube that behaves like a spatial object, not a novelty spinner.

This mechanic was extracted from the local Codrops/Webflow cube gallery extraction:

```text
<project-artifacts>/cube-gallery-extraction/
```

The useful Webflow mechanic is:

- Six image planes become cube faces.
- Each face is placed with `translateZ()` and a 90-degree `rotateX()` or `rotateY()`.
- Scroll drives the parent cube rotation.
- Supporting background images and text labels crossfade or slide as the active face changes.
- Wrapper offsets keep the cube compositionally balanced while different faces are revealed.

This reference rewrites that idea as pure CSS + GSAP + ScrollTrigger.

## Spatial Use Cases

### Architectural Room Box

Use for rotating through the four walls of a curated room, atelier, showroom, gallery, or project chapter.

The visitor should feel like they are turning inside a designed space:

- Front wall: opening mood, entry threshold, hero view.
- Right wall: material decision, joinery, furniture, lighting.
- Back wall: proof moment, before/after, client outcome, project detail.
- Left wall: closing vignette, designer's point of view, inquiry bridge.

Top and bottom faces can be omitted or used only when ceiling/floor are important to the story.

### Material Plinth

Use for inspecting six sides of a bespoke marble, timber, textile, metal, ceramic, plaster, or furniture sample.

The visitor should feel like the material is being turned under controlled studio light:

- Front: hero grain or face.
- Right: edge thickness or join.
- Back: secondary pattern, reverse, maker mark, label, or proof.
- Left: alternate grain or seam.
- Top: surface finish, polish, wear, veining, reflection.
- Bottom: construction, underside, stamp, weight, or sourcing note.

## Required Context Before Implementation

Create or update `contexts/spatial/showroom-choreography.md` before building this section.

Required fields:

```text
Mechanic: Architectural Room Box | Material Plinth
Purpose:
Journey stage:
Belief/proof job:
Face count: 4 | 6
Faces:
  - id:
    role:
    source asset:
    strategic source:
    material/room proof:
    text-safe zone:
    active rotation:
    background state:
Scroll behavior: pinned scrub
Enter range:
Leave range:
Text rhythm:
Mobile fallback:
Reduced-motion fallback:
Exit path:
```

If the mechanic does not have a belief/proof job, use a normal gallery instead.

## Prompt Inheritance Rules

This mechanic only works when the faces belong to the same story. Every face image or video prompt must inherit from `cinematic-prompt-pack.md`.

Every face prompt must include:

```text
Context Inheritance:
- Brand position:
- Visual thesis:
- Spatial concept:
- Showroom choreography section:
- Scene kit:

Strategic Source:
- Which context file made this visual decision:
- Which client belief this face is meant to change:
- Which room/material proof this face carries:

Face Contract:
- Cube face id:
- Role in the rotation:
- Required crop continuity:
- Required lighting continuity:
- Text-safe zone:
- Seam risk:
```

Reject prompts that only say "luxury room", "cinematic interior", "beautiful marble", or similar. The cube exposes inconsistency quickly; face images must share lens language, light direction, scale, material behavior, and text-safe zones.

## HTML

Use semantic page content outside the cube. The cube faces are visual chapters, not the only source of meaning.

```html
<section class="room-box-section" data-room-box>
  <div class="room-box-copy" aria-live="polite">
    <p class="room-box-kicker" data-face-kicker>Private Residence</p>
    <h2 class="room-box-title" data-face-title>The room turns from arrival to evidence.</h2>
    <p class="room-box-body" data-face-body>
      Each wall carries one design decision, so the scroll feels like inspection instead of decoration.
    </p>
  </div>

  <div class="room-box-stage" aria-hidden="true">
    <div class="room-box" data-room-box-cube>
      <figure class="room-box-face room-box-face--front" data-face="front">
        <img src="/images/project-front.webp" alt="" />
      </figure>
      <figure class="room-box-face room-box-face--right" data-face="right">
        <img src="/images/project-right.webp" alt="" />
      </figure>
      <figure class="room-box-face room-box-face--back" data-face="back">
        <img src="/images/project-back.webp" alt="" />
      </figure>
      <figure class="room-box-face room-box-face--left" data-face="left">
        <img src="/images/project-left.webp" alt="" />
      </figure>
      <figure class="room-box-face room-box-face--top" data-face="top">
        <img src="/images/project-top.webp" alt="" />
      </figure>
      <figure class="room-box-face room-box-face--bottom" data-face="bottom">
        <img src="/images/project-bottom.webp" alt="" />
      </figure>
    </div>
  </div>
</section>
```

For a four-wall room, remove the top and bottom faces from the markup and use only the Y-axis rotations.

## CSS

The key is `perspective` on the stage, `transform-style: preserve-3d` on the cube, and each face translated outward by half the cube size.

```css
.room-box-section {
  --box-size: min(64vw, 660px);
  --box-half: calc(var(--box-size) / 2);
  --surface-bg: #11110f;
  min-height: 500vh;
  position: relative;
  background: var(--surface-bg);
  color: #f5f0e8;
}

.room-box-section::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  background:
    radial-gradient(circle at 72% 24%, rgba(255, 242, 207, 0.12), transparent 30%),
    linear-gradient(90deg, rgba(0, 0, 0, 0.44), transparent 54%);
  opacity: 0;
}

.room-box-section.is-active::before {
  opacity: 1;
}

.room-box-stage {
  height: 100vh;
  width: 100%;
  display: grid;
  place-items: center;
  perspective: 1500px;
  perspective-origin: 50% 45%;
  overflow: hidden;
  position: sticky;
  top: 0;
}

.room-box {
  width: var(--box-size);
  height: var(--box-size);
  position: relative;
  transform-style: preserve-3d;
  will-change: transform;
}

.room-box-face {
  position: absolute;
  inset: 0;
  margin: 0;
  overflow: hidden;
  background: #1b1915;
  border: 1px solid rgba(255, 255, 255, 0.16);
  backface-visibility: hidden;
  box-shadow: 0 34px 90px rgba(0, 0, 0, 0.32);
}

.room-box-face img,
.room-box-face video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.room-box-face--front {
  transform: rotateY(0deg) translateZ(var(--box-half));
}

.room-box-face--right {
  transform: rotateY(90deg) translateZ(var(--box-half));
}

.room-box-face--back {
  transform: rotateY(180deg) translateZ(var(--box-half));
}

.room-box-face--left {
  transform: rotateY(-90deg) translateZ(var(--box-half));
}

.room-box-face--top {
  transform: rotateX(90deg) translateZ(var(--box-half));
}

.room-box-face--bottom {
  transform: rotateX(-90deg) translateZ(var(--box-half));
}

.room-box-copy {
  position: sticky;
  top: 0;
  z-index: 2;
  min-height: 100vh;
  width: min(34rem, 86vw);
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-left: clamp(1.25rem, 5vw, 6rem);
  pointer-events: none;
}

.room-box-kicker {
  margin: 0 0 0.75rem;
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: rgba(245, 240, 232, 0.72);
}

.room-box-title {
  margin: 0;
  max-width: 11ch;
  font-size: clamp(2.75rem, 8vw, 7.5rem);
  line-height: 0.9;
  font-weight: 500;
}

.room-box-body {
  max-width: 28rem;
  margin: 1.25rem 0 0;
  color: rgba(245, 240, 232, 0.78);
  font-size: clamp(1rem, 1.35vw, 1.2rem);
  line-height: 1.55;
}

@media (max-width: 760px) {
  .room-box-section {
    --box-size: min(82vw, 420px);
    min-height: auto;
  }

  .room-box-stage {
    position: relative;
    height: 58vh;
    perspective: 1100px;
  }

  .room-box-copy {
    position: relative;
    min-height: auto;
    padding: 1.25rem;
    width: auto;
    pointer-events: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .room-box-section {
    min-height: auto;
  }

  .room-box-stage,
  .room-box-copy {
    position: relative;
  }

  .room-box {
    transform: none !important;
  }
}
```

## GSAP ScrollTrigger

This is the pure-code equivalent of the Webflow scroll interaction. It pins the section and rotates the cube through named faces. Text changes are tied to face states, not arbitrary scroll decoration.

```js
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger);

const section = document.querySelector("[data-room-box]");
const cube = section.querySelector("[data-room-box-cube]");
const copy = {
  kicker: section.querySelector("[data-face-kicker]"),
  title: section.querySelector("[data-face-title]"),
  body: section.querySelector("[data-face-body]"),
};

const faces = [
  {
    id: "front",
    rotation: { x: -2, y: 0, z: 0 },
    stage: { xPercent: 0, yPercent: 0, z: 0 },
    kicker: "Arrival",
    title: "The first wall sets the tone.",
    body: "Use this face for the threshold: light direction, palette, and the first proof of taste.",
  },
  {
    id: "right",
    rotation: { x: -3, y: -90, z: -1 },
    stage: { xPercent: -12, yPercent: 0, z: -120 },
    kicker: "Material",
    title: "The second wall shows the decision.",
    body: "Use this face for joinery, fabric, stone, lighting, or the signature object.",
  },
  {
    id: "back",
    rotation: { x: -2, y: -180, z: 0 },
    stage: { xPercent: 8, yPercent: 4, z: -160 },
    kicker: "Proof",
    title: "The back wall makes the claim concrete.",
    body: "Use this face for before/after logic, project result, constraints, or client outcome.",
  },
  {
    id: "left",
    rotation: { x: 2, y: -270, z: 0 },
    stage: { xPercent: 14, yPercent: 0, z: -100 },
    kicker: "Inquiry",
    title: "The final wall slows the visitor down.",
    body: "Use this face to bridge from cinematic atmosphere into a consultative next step.",
  },
];

function setCopy(face) {
  gsap.to([copy.kicker, copy.title, copy.body], {
    autoAlpha: 0,
    y: 18,
    duration: 0.18,
    overwrite: true,
    onComplete: () => {
      copy.kicker.textContent = face.kicker;
      copy.title.textContent = face.title;
      copy.body.textContent = face.body;

      gsap.to([copy.kicker, copy.title, copy.body], {
        autoAlpha: 1,
        y: 0,
        duration: 0.32,
        stagger: 0.04,
        overwrite: true,
      });
    },
  });
}

gsap.set(cube, {
  rotateX: faces[0].rotation.x,
  rotateY: faces[0].rotation.y,
  rotateZ: faces[0].rotation.z,
  xPercent: faces[0].stage.xPercent,
  yPercent: faces[0].stage.yPercent,
  z: faces[0].stage.z,
});

setCopy(faces[0]);

const tl = gsap.timeline({
  defaults: { ease: "none" },
  scrollTrigger: {
    trigger: section,
    start: "top top",
    end: () => `+=${faces.length * window.innerHeight}`,
    scrub: 0.85,
    pin: true,
    anticipatePin: 1,
    onEnter: () => section.classList.add("is-active"),
    onLeave: () => section.classList.remove("is-active"),
    onEnterBack: () => section.classList.add("is-active"),
    onLeaveBack: () => section.classList.remove("is-active"),
  },
});

faces.slice(1).forEach((face, index) => {
  const position = index + 1;

  tl.to(
    cube,
    {
      rotateX: face.rotation.x,
      rotateY: face.rotation.y,
      rotateZ: face.rotation.z,
      xPercent: face.stage.xPercent,
      yPercent: face.stage.yPercent,
      z: face.stage.z,
      duration: 1,
    },
    position
  );

  tl.call(() => setCopy(face), [], position + 0.45);
});
```

## Six-Sided Material Plinth Timeline

Use this sequence when top and bottom inspection matters.

```js
const materialFaces = [
  { id: "front", rotation: { x: -4, y: 0, z: 0 } },
  { id: "right", rotation: { x: -4, y: -90, z: 0 } },
  { id: "back", rotation: { x: -4, y: -180, z: 0 } },
  { id: "left", rotation: { x: -4, y: -270, z: 0 } },
  { id: "top", rotation: { x: -92, y: -270, z: 0 } },
  { id: "bottom", rotation: { x: 88, y: -180, z: 0 } },
];
```

Top and bottom rotations are more fragile visually. Use them only with strong material texture, studio lighting, and simple copy zones.

## Webflow Extraction Notes

The extracted tutorial used embedded face CSS similar to:

```css
.pictures_cube-item:nth-child(1) {
  transform: translateZ(calc(0.5 * 100cqw)) rotateY(0deg);
}

.pictures_cube-item:nth-child(2) {
  transform: translateX(-100%) translateZ(calc(0.5 * 100cqw)) rotateY(-90deg);
}

.pictures_cube-item:nth-child(3) {
  transform: translateZ(calc(-0.5 * 100cqw)) rotateY(180deg);
}
```

The Webflow timeline rotates the cube list through `rotationY: 90deg`, `180deg`, `270deg`, `360deg`, with one `rotationX: -90deg` beat for a vertical face, while moving the wrapper on X/Y to keep the active image composed.

Our OS version keeps the geometry, but replaces the CMS/gallery premise with spatial roles, face contracts, prompt inheritance, and proof-led copy.

## Composition Rules

- Place copy in edge zones unless the active face has an authored quiet area.
- Keep the cube large enough to feel architectural, but not so large that edges leave no room for proof.
- Add small X/Y/Z wrapper offsets per face to preserve composition.
- Use linear scrub for cube rotation; use eased non-scrub animation only for text.
- Keep face borders subtle. The object should feel physical, not like a heavy UI card.
- Use consistent focal length across face assets.
- Match horizon height across architectural faces.
- Match light direction across material faces.
- Do not place important details on cube edges unless edge inspection is the point.

## Mobile And Reduced Motion

Mobile options:

- Replace the cube with stacked face cards.
- Replace it with a horizontal snap carousel.
- Keep a smaller cube but remove pinning and show only four Y-axis faces.
- Use a still image per chapter with the same copy sequence.

Reduced motion:

- Do not rotate the cube through scroll.
- Show a static face stack or manual tabs.
- Preserve the same face roles and proof copy.

## Quality Gate

Before accepting an implementation:

1. The mechanic is named as Architectural Room Box or Material Plinth.
2. Every face has a role, proof job, text-safe zone, and strategic source.
3. The cube is scroll-driven with GSAP + ScrollTrigger or an equivalent controlled playhead.
4. Face assets share lighting, crop logic, scale, and lens language.
5. Mobile and reduced-motion fallbacks exist.
6. Navigation and inquiry remain reachable.
7. The section proves spatial taste, material intelligence, portfolio quality, or process authority.
8. The result does not read as a generic spinning cube.

## Anti-Patterns

| Anti-Pattern | What It Is | Fix |
| --- | --- | --- |
| Generic Cube Demo | Any six nice images placed on a cube | Assign face roles and strategic source blocks |
| Face Mismatch | Different lighting, crops, or scale between faces | Regenerate prompts from shared context inheritance |
| Scroll Trap | Long pinned cube with no proof or exit | Shorten sequence and add edge inquiry path |
| UI Card Cube | Heavy borders, labels, and chrome make it feel like a widget | Let images/materials carry the object |
| Unreadable Overlays | Text crosses high-detail face areas | Move copy to edge zones or prompt a quiet area |
| Cargo-Cult Webflow | Copying IX2 behavior without meaning | Use the pure-code geometry and spatial choreography |
