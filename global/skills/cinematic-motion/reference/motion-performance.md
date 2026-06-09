# Motion Performance

Use this before approving motion-heavy spatial concepts.

## Budget Rules

- First viewport can contain one hero media system only.
- Do not combine WebGL, image sequence, and autoplay video in the first viewport.
- Keep ambient loops low-amplitude and pause them offscreen.
- Use poster frames for all videos.
- Lazy-load below-fold room/project media.
- Use responsive image sizes and mobile-specific crops.

## WebGL Rules

- Use WebGL only for camera depth, object inspection, material behavior, or generative atmosphere that DOM cannot express.
- Dispose geometry, textures, and materials on unmount.
- Avoid real-time shadows for complex interiors; prefer baked shadows or rendered media.
- Provide mobile video/still fallback.

## Canvas Sequence Rules

- Use WebP/AVIF frames when possible.
- Preload in chunks.
- Cap DPR on large canvases.
- Draw only on frame index change.
- Keep frame maps explicit: scroll range, frame range, caption cues.

## Verification

Check:

- no long main-thread stalls
- no unbounded intervals
- no hidden autoplay videos offscreen
- no massive uncompressed room images
- no mobile scroll traps
