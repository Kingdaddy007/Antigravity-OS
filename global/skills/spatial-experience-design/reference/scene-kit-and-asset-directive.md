# Scene Kit And Beloved's Asset Directive

Use this when a spatial concept depends on imagery, generated pictures, video, rendered objects, SVG masks, or WebGL/canvas scenes. The assistant must create this directive after `room-sequence.md` and before layout styling.

## Build Gate

Pause after writing the directive.

Do not write final layout styling for image-native scenes until Beloved has placed the required assets in the specified folders, or explicitly approves temporary stand-ins.

## Asset Directive Checklist

For each required asset, output:

```text
Asset ID:
Chapter / room:
Purpose:
Visitor belief this asset supports:
Taste world:
Enemy/cliche this asset avoids:
Mechanic source from design-audit:
Asset type: image | transparent PNG | SVG mask | video source image | WebM/MP4 | GLB | canvas frames
Needed file path:
Format and dimensions:
Subject:
Composition:
Cinematic room grammar used:
Camera angle:
Lens / framing:
Perspective:
Lighting highlight direction:
Shadow behavior:
Material finish:
Color grade:
Crop rules:
Foreground / midground / background role:
Blur role:
Text-safe zone:
Text overlay / text-safe rule:
Motion role:
Website section placement:
Scroll choreography role:
Can be placeholdered temporarily:
Forbidden substitute:
Blocking before build: yes | no
```

## Image Generation Prompt Template

Use when Beloved needs a still image or source image for later video.

```text
Create a high-end editorial interior design image.
Strategic Source:
Perception goal: [what this asset must make the visitor believe]
Taste world: [quiet collected residence / sculptural warm minimalism / layered art-led / material-led modern craft / etc.]
Section / journey stage: [Atmosphere / Taste / Transformation / Proof / Method / Inquiry]
Visual thesis connection: [how this image serves the approved thesis]
Enemy / cliche rejected: [template decor / Pinterest taste / generic showroom / overdesigned spectacle]
Subject: [room/object/material/person/action]
Space type: [entry, living room, dining room, bedroom, studio, gallery, showroom]
Design language: [quiet collected residence / sculptural warm minimalism / layered art-led / material-led modern craft / etc.]
Composition: [dominant focal point, negative space, text-safe zone]
Camera angle: [eye-level frontal / 3/4 corner / low architectural / overhead / macro / close detail]
Lens feel: [24mm architectural / 35mm editorial / 50mm natural / 85mm portrait compression / macro]
Lighting: [one dominant source: daylight from left / warm lamp glow from right / gallery spotlight / doorway light spill / shadow pass]
Highlight direction: [top-left, side-left, back-right, etc.]
Camera side: [shadow-side / highlight-side / threshold-side / detail-side / POV]
Materials: [wood, stone, plaster, textile, glass, metal]
Depth: [foreground blur / midground subject / background atmosphere]
Mood: [calm, seductive, ceremonial, intimate, restrained]
Color grade: [warm neutral, cool limestone, amber evening, gallery white, etc.]
Texture detail: [grain, weave, plaster irregularity, stone veining]
Website use: [hero source image / portfolio chapter / material proof / method proof / inquiry atmosphere]
Aspect ratio: [16:9 / 4:5 / 1:1 / 9:16]
Negative prompt: no generic showroom, no overdecorated luxury, no stock-photo staging, no fake smiles, no cluttered template composition, no plastic CGI look, no text artifacts, no full-room reveal if the scene requires withholding.
```

## Video Source Image Rule

For AI video, create a strong source image first. Do not prompt video from nothing when continuity matters.

The source image must lock:

- Subject identity.
- Room/object geometry.
- Camera angle.
- Material placement.
- Lighting direction.
- Text-safe zones.
- Start frame composition.

Then write the video prompt from that still.

## Video Prompt Template

```text
Use the provided source image as the exact start frame.
Strategic Source:
Perception goal: [what this video must make the visitor believe]
Taste world: [approved taste world]
Section / journey stage: [Atmosphere / Taste / Transformation / Proof / Method / Inquiry]
Desired visitor belief: [belief]
Visual thesis connection: [connection]
Room / material / object source: [source]
Motion role: [arrival / ambient / scroll-bound / interaction]
Website placement: [section]
Text-safe requirement: [zone and protected subject]
Enemy / cliche rejected: [cliche]
Duration: [5-10 seconds]
Camera: [slow dolly forward / lateral slide / tilt down / push through doorway / orbit around object / locked tripod]
Movement speed: [barely perceptible / slow ceremonial / steady architectural / precise mechanical]
Subject movement: [curtain drifting, light moving across wall, hand pulling fabric, shadow passing, door opening, dust motes, plant shadow, object rotating]
Spatial action: [what physically changes in the room]
Lighting behavior: [sunlight spill grows, lamp glow flickers softly, gallery spotlight shifts]
Material behavior: [fabric ripples, glass catches highlight, plaster texture emerges, stone reflects soft light]
Camera constraints: preserve the same room geometry, same materials, same object positions, no new furniture, no warped walls.
End frame: [specific end state]
Mood: [quiet, seductive, gallery-like, intimate, monumental]
No audio unless requested.
Negative prompt: no fast cuts, no handheld shake, no morphing furniture, no new objects, no surreal warping, no glossy plastic render, no text artifacts.
```

## Prompt Pack Gate

`cinematic-prompt-pack.md` must include `Context Inheritance` before any prompt.

Each prompt must trace to approved context files and include a `Strategic Source` block. If the prompt cannot explain its perception goal, taste world, section role, visual thesis connection, text-safe requirement, and rejected cliche, rewrite it before asset generation.

## Asset Path Defaults

Use these unless the project already has conventions:

- `public/images/spatial/` for room and material images.
- `public/images/spatial/cutouts/` for transparent PNG/WebP layers.
- `public/video/spatial/` for WebM/MP4 loops.
- `public/svg/spatial/` for masks, floor lines, labels, and transition edges.
- `public/models/spatial/` for GLB/GLTF objects.
- `public/sequences/spatial/[sequence-name]/` for frame sequences.
