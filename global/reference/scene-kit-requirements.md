# Scene Kit Requirements

Use this file when a spatial concept depends on real or generated imagery.

## Required Fields

Every scene kit must define:

- Hero asset and supporting assets.
- Camera angle.
- Lens feel: wide architectural, editorial portrait, macro, overhead, or frontal gallery.
- Light direction.
- Light temperature.
- Shadow softness.
- Contact shadows.
- Crop boundaries for desktop, tablet, and mobile.
- Foreground blur assets, if any.
- Midground object/assets.
- Background atmosphere.
- Text-safe zones.
- Accepted placeholders and forbidden placeholders.

## Asset Family Coherence

All assets in a single scene must share:

- Perspective.
- Lighting direction.
- Shadow density.
- Color grade.
- Grain/noise level.
- Material finish.
- Edge treatment.
- Scale logic.

Mismatch breaks the premium illusion.

## Image-Native Assets

Treat these as image-native by default:

- Finished rooms.
- Before/after interiors.
- Furniture/object product renders.
- Fabric, stone, plaster, wood, metal, glass macro surfaces.
- Murals, artworks, gallery walls.
- Foreground foliage or curtains.
- Human hands/process shots.
- Architectural exteriors or entry thresholds.

## Placeholder Rules

- Good placeholder: a clearly labeled temporary crop with matching aspect ratio and approximate light direction.
- Bad placeholder: gradient block, CSS blob, empty rectangle, generic stock photo with wrong lighting.
- Forbidden: shipping a CSS-only fake for a concept whose value depends on tactile realism.

## Mobile Kit

Require mobile-specific crops for:

- full-bleed rooms
- before/after reveals
- object spines
- gallery procession images
- macro material closeups

Do not rely on desktop crop scaling.
