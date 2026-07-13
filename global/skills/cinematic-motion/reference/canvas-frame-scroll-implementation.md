# Canvas Frame Scroll Implementation

## Contents

- [When To Use](#when-to-use)
- [Required Context](#required-context)
- [Video Analysis](#video-analysis)
- [Frame Extraction](#frame-extraction)
- [Page Structure](#page-structure)
- [Layout Contract](#layout-contract)
- [Lenis Setup](#lenis-setup)
- [Frame Preloader](#frame-preloader)
- [Canvas Renderer](#canvas-renderer)
- [Frame-To-Scroll Binding](#frame-to-scroll-binding)
- [Section Animation System](#section-animation-system)
- [Dark Overlay And Stats](#dark-overlay-and-stats)
- [Marquee](#marquee)
- [Circle-Wipe Hero Reveal](#circle-wipe-hero-reveal)
- [Mobile And Reduced Motion](#mobile-and-reduced-motion)
- [Troubleshooting](#troubleshooting)
- [Quality Gate](#quality-gate)

Use this when an approved spatial concept needs a real video converted into scroll-controlled canvas frames. Adapted from the installed LobeHub skill `remamare13-claude-framework-video-to-website`.

Installed source in this sandbox:

`external-skills/remamare13-claude-framework-video-to-website/SKILL.md`

Marketplace source:

https://lobehub.com/skills/remamare13-claude-framework-video-to-website/skill.md

## When To Use

- A room film, object film, or material film must scrub with scroll.
- The user provides an MP4/MOV and wants it turned into a website experience.
- AI-generated video should become frame-accurate scroll media.
- A source-image-to-video scene needs exact start/end frame control in the browser.

Do not use this for ambient loops that can remain normal video. Use canvas frames only when scroll must control the visual progression.

## Required Context

Before extracting frames, confirm:

- `contexts/spatial/showroom-choreography.md` defines the section job, scroll behavior, text zone, and fallback.
- `contexts/spatial/cinematic-prompt-pack.md` exists if the source video was generated.
- `contexts/spatial/asset-boundary.md` classifies the sequence as canvas/frame-native.
- `contexts/spatial/motion-board.md` assigns the sequence to arrival, ambient, scroll-bound, or interaction.

## Video Analysis

Verify FFmpeg and FFprobe are available.

Windows:

```powershell
where ffmpeg
where ffprobe
```

Analyze source:

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,duration,r_frame_rate,nb_frames -of csv=p=0 "<VIDEO_PATH>"
```

Choose frame extraction:

| Video Length | Target FPS | Target Frames |
| --- | --- | --- |
| Under 10s | Original or high FPS | Cap near 300 |
| 10-30s | 10-15fps | 150-300 |
| 30s+ | 5-10fps | 150-300 unless justified |

Cap output width at 1920px for desktop. Use smaller mobile tiers when needed.

## Frame Extraction

```bash
mkdir -p frames
ffmpeg -i "<VIDEO_PATH>" -vf "fps=<CALCULATED_FPS>,scale=<WIDTH>:-1" -c:v libwebp -quality 80 "frames/frame_%04d.webp"
```

Rules:

- Use WebP frames for browser weight.
- Count frames after extraction.
- Keep file names sequential and predictable.
- Store under `public/sequences/spatial/[sequence-name]/` unless the project has another convention.
- Do not hide loader until required frames are ready.

## Page Structure

Use this structure for a full frame-scroll page or section:

```html
<div id="loader">
  <div class="loader-brand"></div>
  <div id="loader-bar"></div>
  <div id="loader-percent"></div>
</div>

<header class="site-header">
  <nav></nav>
</header>

<section class="hero-standalone">
  <span class="section-label"></span>
  <h1 class="hero-heading"></h1>
  <p class="hero-tagline"></p>
</section>

<div class="canvas-wrap">
  <canvas id="canvas"></canvas>
</div>

<div id="dark-overlay" aria-hidden="true"></div>

<div class="marquee-wrap" aria-hidden="true">
  <div class="marquee-text"></div>
</div>

<main id="scroll-container">
  <section class="scroll-section align-left" data-enter="22" data-leave="38" data-animation="slide-left"></section>
  <section class="scroll-section align-right" data-enter="40" data-leave="54" data-animation="clip-reveal"></section>
  <section class="scroll-section section-stats" data-enter="56" data-leave="72" data-animation="stagger-up"></section>
  <section class="scroll-section" data-enter="78" data-leave="100" data-animation="fade-up" data-persist="true"></section>
</main>
```

Rules:

- Use semantic sections even when canvas is fixed.
- Keep text side-aligned when the media is central.
- Use a persistent final CTA/inquiry section.
- Keep navigation reachable during pinned or long scroll sequences.

## Layout Contract

```css
.align-left {
  padding-left: 5vw;
  padding-right: 55vw;
}

.align-right {
  padding-left: 55vw;
  padding-right: 5vw;
}

.align-left .section-inner,
.align-right .section-inner {
  max-width: 40vw;
}

.scroll-section {
  position: absolute;
  transform: translateY(-50%);
}
```

Interior adaptation:

- Replace massive default tech typography with typography from `DESIGN.md`.
- Use side text zones because rooms, objects, or materials usually own the center.
- Use dark overlays only for stats/proof or when the media is intentionally backgrounded.
- Avoid glassmorphism cards unless the spatial thesis specifically supports glass/reflection.

## Lenis Setup

```js
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true
});

lenis.on("scroll", ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);
```

## Frame Preloader

Use two-phase loading:

1. Load first 10 frames quickly for first paint.
2. Load remaining frames in the background.
3. Update loader percentage.
4. Draw a poster/first frame while loading.
5. Hide loader only after required frames for initial interaction are ready.

Use idle loading for later chapters when the page has multiple sequences.

## Canvas Renderer

Use padded cover mode so the subject does not collide with header/text:

```js
const IMAGE_SCALE = 0.85; // 0.82-0.90

function drawFrame(index) {
  const img = frames[index];
  if (!img) return;

  const cw = canvas.width;
  const ch = canvas.height;
  const iw = img.naturalWidth;
  const ih = img.naturalHeight;
  const scale = Math.max(cw / iw, ch / ih) * IMAGE_SCALE;
  const dw = iw * scale;
  const dh = ih * scale;
  const dx = (cw - dw) / 2;
  const dy = (ch - dh) / 2;

  ctx.fillStyle = bgColor;
  ctx.fillRect(0, 0, cw, ch);
  ctx.drawImage(img, dx, dy, dw, dh);
}
```

Rules:

- Apply devicePixelRatio scaling for crisp output.
- Sample background color from frame edges every 20 frames when padded borders need to blend.
- Redraw only when frame index changes.
- Use `requestAnimationFrame` for drawing.

## Frame-To-Scroll Binding

```js
const FRAME_SPEED = 2.0; // 1.8-2.2

ScrollTrigger.create({
  trigger: scrollContainer,
  start: "top top",
  end: "bottom bottom",
  scrub: true,
  onUpdate: (self) => {
    const accelerated = Math.min(self.progress * FRAME_SPEED, 1);
    const index = Math.min(
      Math.floor(accelerated * FRAME_COUNT),
      FRAME_COUNT - 1
    );

    if (index !== currentFrame) {
      currentFrame = index;
      requestAnimationFrame(() => drawFrame(currentFrame));
    }
  }
});
```

Interior guidance:

- Use `FRAME_SPEED` near `1.8` for slow gallery/residential motion.
- Use `2.0-2.2` when the main visual should complete earlier and leave room for proof/inquiry overlays.
- Do not let the sequence finish before the visitor understands the scene.

## Section Animation System

Sections read `data-enter`, `data-leave`, `data-animation`, and optional `data-persist`.

Supported animation types:

| Type | Use For |
| --- | --- |
| `fade-up` | Quiet caption or inquiry entrance |
| `slide-left` | Left text zone entering over central media |
| `slide-right` | Right text zone entering over central media |
| `scale-up` | Proof/stat or object emphasis |
| `rotate-in` | Use rarely; only playful or object-led brands |
| `stagger-up` | Label -> heading -> body -> CTA/proof |
| `clip-reveal` | Material, curtain, shadow, or editorial reveal |

Rules:

- Never repeat the same entrance type consecutively.
- Stagger children: label -> heading -> body -> CTA/proof.
- Sections with `data-persist="true"` stay visible at the end.
- Do not use direction variety as spectacle; the animation must match the section's spatial job.

## Dark Overlay And Stats

Use a dark overlay only when proof needs high readability over media.

Recommended opacity: `0.88-0.92`.

Use counters only for real proof:

- project count
- years
- square footage
- lead times
- install windows
- press/features
- client/property facts

Do not invent fake metrics.

## Marquee

Use marquee only when it supports:

- brand values
- material language
- portfolio archive
- inquiry rhythm
- transition between cinematic acts

Avoid generic "innovation/excellence" filler. For interiors, use material, method, or proof language.

## Circle-Wipe Hero Reveal

Use only when the hero needs to transition from static brand statement into canvas media.

```js
const wipeProgress = Math.min(1, Math.max(0, (p - 0.01) / 0.06));
const radius = wipeProgress * 75;
canvasWrap.style.clipPath = `circle(${radius}% at 50% 50%)`;
```

Interior alternatives:

- doorway mask
- curtain split
- light spill
- material wipe
- shadow pass
- gallery portal

Prefer scene-native masks over generic circles when the room provides a better transition.

## Mobile And Reduced Motion

- Mobile: reduce scroll height, frame count, and simultaneous overlays.
- Mobile: replace long pinned canvas with chapter stills or short loops when needed.
- Reduced motion: use poster frame, crossfade, or manual chapter navigation.
- Never hide content because motion is disabled.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| Frames do not load | Serve over HTTP, not `file://` |
| Choppy scroll | Reduce frames, increase scrub, lower resolution |
| White flashes | Keep loader until frames are ready |
| Blurry canvas | Apply DPR scaling |
| Header collision | Lower `IMAGE_SCALE` toward `0.82` |
| Sluggish sequence | Raise `FRAME_SPEED` toward `2.0` |
| Mobile memory issue | Use fewer frames, smaller width, or video fallback |
| Lenis conflict | Ensure `lenis.on("scroll", ScrollTrigger.update)` is connected |

## Quality Gate

Reject the implementation if:

- The frame sequence is not mapped in `showroom-choreography.md`.
- Text zones are decided only in CSS, not in the prompt/source composition.
- The canvas sequence acts like product-demo spectacle instead of spatial proof.
- Mobile has no authored fallback.
- The CTA/inquiry disappears after the sequence.
- Stats, counters, or marquees are decorative filler.
