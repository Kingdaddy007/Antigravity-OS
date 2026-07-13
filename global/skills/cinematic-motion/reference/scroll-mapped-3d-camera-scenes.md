# Scroll-Mapped 3D Camera Scenes

## Contents

- [When To Use](#when-to-use)
- [Never Use](#never-use)
- [Core Mechanic](#core-mechanic)
- [Required Context](#required-context)
- [Camera Path Rules](#camera-path-rules)
- [Implementation Notes](#implementation-notes)
- [Interior Adaptation](#interior-adaptation)
- [Mobile And Fallback](#mobile-and-fallback)
- [Quality Gate](#quality-gate)

Use this when a spatial website needs a 3D walkthrough, object inspection, architectural model, room world, or cinematic camera path controlled by scroll. Adapted from the Codrops `codrops-cinematic-scroll-animations` 3D scene showcase.

Source:

- Repository: https://github.com/JosephASG/codrops-cinematic-scroll-animations
- Local source: `external-references/codrops-cinematic-scroll-animations/src/components/pages/variant-2/cinematic-scene-showcase.tsx`
- Scene map: `external-references/codrops-cinematic-scroll-animations/src/lib/variant-2/scene-data.ts`

## When To Use

- Architecture-adjacent studios with real spatial models.
- Signature object spine using a chair, lamp, staircase, doorway, or material object.
- 3D showroom walkthrough where camera movement is the story.
- Portfolio or method section where the visitor needs to inspect spatial relationships.

## Never Use

- When a still image or video can carry the idea.
- When no GLB/model or coherent 3D scene exists.
- When text, proof, and inquiry would be swallowed by 3D spectacle.
- Without fallback for mobile and reduced motion.

## Core Mechanic

Define a scene map:

```ts
type ScenePerspective = {
  title: string;
  subtitle: string;
  position: 'top' | 'top-left' | 'left' | 'right' | 'center' | 'top-right' | 'bottom' | 'bottom-left' | 'bottom-right';
  camera: { x: number; y: number; z: number };
  target: { x: number; y: number; z: number };
  rotation?: { x: number; y: number; z: number };
  scrollProgress: { start: number; end: number };
  hideText?: boolean;
};
```

Use one scroll timeline to animate:

- camera position
- camera target / lookAt point
- optional object rotation
- progress indicator

Use separate text timelines for each perspective.

## Required Context

Add this mechanic to `contexts/spatial/showroom-choreography.md`:

```text
Mechanic: Scroll-Mapped 3D Camera Scene
Purpose:
3D asset:
Camera path:
Target path:
Text positions:
Hidden-text transition beats:
Scroll ranges:
Proof role:
Mobile fallback:
Reduced-motion fallback:
```

## Camera Path Rules

- Each camera beat must reveal something: threshold, material, proportion, object relation, room volume, or method logic.
- Text position must avoid the focal object and light behavior.
- Use `hideText: true` for pure transition beats.
- Keep camera movement slow and legible.
- Use a progress rail when the scene is long.

## Implementation Notes

Camera refs:

```js
const cameraAnimRef = useRef({ x: -20, y: 0, z: 0 });
const targetAnimRef = useRef({ x: 0, y: 15, z: 0 });
```

R3F update:

```js
useFrame(() => {
  camera.position.set(cameraAnimRef.current.x, cameraAnimRef.current.y, cameraAnimRef.current.z);
  camera.lookAt(targetAnimRef.current.x, targetAnimRef.current.y, targetAnimRef.current.z);
});
```

Scroll mapping:

```js
scenePerspectives.forEach((perspective) => {
  const startProgress = perspective.scrollProgress.start / 100;
  const endProgress = perspective.scrollProgress.end / 100;

  tl.to(cameraAnimRef.current, {
    x: perspective.camera.x,
    y: perspective.camera.y,
    z: perspective.camera.z,
    duration: endProgress - startProgress,
    ease: 'none'
  }, startProgress);

  tl.to(targetAnimRef.current, {
    x: perspective.target.x,
    y: perspective.target.y,
    z: perspective.target.z,
    duration: endProgress - startProgress,
    ease: 'none'
  }, startProgress);
});
```

## Interior Adaptation

Good 3D scene subjects:

- a room shell with material zones
- a staircase or doorway threshold
- a sculptural lamp/chair/table object
- a gallery wall or material library
- a simplified floor-plan-to-room world

Avoid:

- cyberpunk/demo aesthetics unless the brand truly needs it
- generic tech words like "innovation" and "future"
- 3D scenes that do not prove interior taste, process, or authority

## Mobile And Fallback

- Desktop: R3F/WebGL scene.
- Tablet: shorter camera path, fewer effects.
- Mobile: poster/video loop or chapter still stack.
- Reduced motion: static annotated stills or manual section navigation.

## Quality Gate

Reject if:

- The 3D asset is decorative.
- Scroll ranges are not mapped before implementation.
- Text positions collide with focal objects.
- There is no mobile fallback.
- Inquiry is unreachable during or after the scene.
