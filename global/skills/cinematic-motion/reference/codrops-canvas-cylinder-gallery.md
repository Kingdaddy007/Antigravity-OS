# WebGL Cylindrical Gallery (Codrops Canvas Method)

Use this when a portfolio or material archive should feel like a rotating private gallery, panoramic room wall, or immersive showroom object. Adapted from the Codrops `codrops-cinematic-scroll-animations` cylinder carousel.

Source:
- Repository: https://github.com/JosephASG/codrops-cinematic-scroll-animations
- Local source: `external-references/codrops-cinematic-scroll-animations/src/components/pages/variant-1/cylinder-carousel.tsx`

## When To Use
- Signature portfolio reel where rooms wrap around the visitor.
- Material library as a rotating tactile archive.
- Gallery-like residential curation where images become an environment.
- Hero or interstitial scene where the visitor moves around an object made of project images.

## Never Use
- For ordinary project grids.
- When project proof needs readable captions more than spectacle.
- When there are not enough high-quality, consistently cropped images.
- Without mobile and reduced-motion fallbacks.
- With particle effects unless they belong to the brand world.

## Core Mechanic
1. Load a curated image set.
2. Draw all images into one canvas texture.
3. Map that texture onto a custom cylinder geometry.
4. Use scroll to rotate the cylinder and move the camera.
5. Overlay text chapters keyed to scroll percentages.
6. Add a loader until all images are drawn.
7. Resize carefully for mobile to prevent stretched imagery.

## Required Context
Add this mechanic to `contexts/spatial/showroom-choreography.md`:

```text
Mechanic: WebGL Cylindrical Gallery
Purpose:
Journey stage:
Image set:
Proof job per image:
Cylinder role:
Camera path:
Text chapter positions:
Fallback:
Exit path:
```

## Image Requirements
- Use consistent aspect ratio and lighting family.
- Avoid mixing unrelated taste worlds.
- Treat each image as a proof panel: room, material, object, threshold, before/after, or process.
- Use `cinematic-prompt-pack.md` for generated images.
- Do not use source repo demo images.

## Implementation Notes
Core geometry concept:

```js
for (let y = 0; y <= heightSegments; y++) {
  const v = y / heightSegments;
  const yPos = (v - 0.5) * height;

  for (let x = 0; x <= radialSegments; x++) {
    const u = x / radialSegments;
    const theta = u * Math.PI * 2;
    positions.push(Math.cos(theta) * radius, yPos, Math.sin(theta) * radius);
    uvs.push(u, 1 - v);
  }
}
```

Texture assembly:
- Draw each image into a horizontal strip canvas.
- Use object-fit cover behavior.
- Respect GPU `MAX_TEXTURE_SIZE`; scale texture down on mobile.
- Disable mipmaps when using large dynamic canvas textures if needed.

Scroll choreography:
- Use one long scroll container, usually `500svh+`.
- Rotate cylinder with `ease: none`.
- Move camera in staged phases.
- Crossfade text chapters by scroll segment.

## Interior Adaptation
Good uses:
- "A private archive of rooms" for a gallery-led designer.
- "Material orbit" around stone, linen, timber, plaster, metal, glass.
- "Project wall" before the visitor enters deep project chapters.

Bad uses:
- A rotating slideshow with no proof.
- Every client getting the same cylinder.
- Overpowering the designer's real work with WebGL vanity.

## Mobile And Fallback
- Mobile: use a finite stacked gallery or horizontal project rail.
- Reduced motion: static project chapter stack.
- Low GPU: use image/video fallback.
- Always keep inquiry reachable after the gallery.

## Quality Gate
Reject if:
- Images do not share a coherent taste world.
- Captions/proof are unreadable.
- The cylinder is used before atmosphere or story is established.
- It cannot explain why this brand needs a cylindrical gallery.
- It causes mobile crop/stretch problems.
