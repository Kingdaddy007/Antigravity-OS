# Material Recipes

## Contents

- [Gallery Label](#gallery-label)
- [Quiet Concierge CTA](#quiet-concierge-cta)
- [Plaster Surface](#plaster-surface)
- [Glass Caption Panel](#glass-caption-panel)
- [Textile Edge Mask](#textile-edge-mask)
- [Stacked Room Panel](#stacked-room-panel)
- [Reduced Motion Baseline](#reduced-motion-baseline)

Use these as implementation recipes only after the material script and scene kit exist. Do not let CSS material effects replace required real assets.

## Gallery Label

```css
.gallery-label {
  font-size: clamp(0.68rem, 0.62rem + 0.2vw, 0.78rem);
  line-height: 1.45;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: oklch(31% 0.018 75);
  max-width: 28ch;
}
```

## Quiet Concierge CTA

```css
.concierge-cta {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  min-height: 44px;
  color: oklch(24% 0.018 70);
  text-decoration: none;
  border-bottom: 1px solid currentColor;
  transition: color 220ms cubic-bezier(0.16, 1, 0.3, 1), border-color 220ms cubic-bezier(0.16, 1, 0.3, 1);
}
.concierge-cta:focus-visible {
  outline: 2px solid oklch(55% 0.08 70);
  outline-offset: 4px;
}
```

## Plaster Surface

```css
.material-plaster {
  background:
    radial-gradient(circle at 20% 12%, oklch(96% 0.012 85), transparent 32%),
    linear-gradient(135deg, oklch(91% 0.014 82), oklch(84% 0.018 78));
  position: relative;
}
.material-plaster::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: 0.08;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140' viewBox='0 0 140 140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='140' height='140' filter='url(%23n)' opacity='.45'/%3E%3C/svg%3E");
}
```

## Glass Caption Panel

```css
.glass-caption {
  background: color-mix(in oklch, oklch(98% 0.006 80) 72%, transparent);
  border: 1px solid color-mix(in oklch, oklch(96% 0.006 80) 42%, transparent);
  backdrop-filter: blur(18px) saturate(1.05);
  box-shadow: 0 18px 60px color-mix(in oklch, oklch(18% 0.02 70) 16%, transparent);
}
```

## Textile Edge Mask

```css
.textile-reveal {
  clip-path: inset(0 0 0 var(--reveal, 0%));
  transition: clip-path 900ms cubic-bezier(0.16, 1, 0.3, 1);
}
```

## Stacked Room Panel

```css
.room-panel {
  position: absolute;
  inset: 0;
  overflow: clip;
  background: oklch(92% 0.012 80);
  box-shadow: 0 -24px 70px color-mix(in oklch, oklch(16% 0.02 70) 26%, transparent);
}
.room-panel img,
.room-panel video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

## Reduced Motion Baseline

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
  }
}
```
