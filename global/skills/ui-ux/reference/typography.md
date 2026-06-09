# Typography Reference

## Font Pairing Rules

### Brand Register
- **Display + Body pairing:** Distinctive display font (serif or rule-breaking sans) paired with a readable body font
- **Two families minimum** only when voice needs it; one family is often enough for restrained brands
- **Display fonts:** Editorial serif, geometric sans, or expressive display type
- **Body fonts:** Humanist sans, neutral sans, or warm serif for long-form reading
- **Avoid reflex defaults:** See `brand.md` reflex-reject list (Playfair Display, Inter, DM Sans, Outfit, etc.)

### Product Register
- **System fonts are legitimate.** One family is often right.
- **Fixed rem scale**, not fluid clamp
- **Tighter scale ratio** (1.125–1.2) for dense data interfaces

## Scale System

### Brand Register Scale (fluid for headings, fixed for body)
| Role | Size | Weight | Line Height | Use |
|------|------|--------|-------------|-----|
| Display | `clamp(2.5rem, 7vw, 4.5rem)` | 300–400 | 1.0–1.1 | Hero headlines only |
| Headline | `clamp(1.75rem, 4vw, 3rem)` | 400–500 | 1.1–1.2 | Section headings |
| Title | `clamp(1.25rem, 3vw, 1.75rem)` | 500–600 | 1.2–1.3 | Card titles, subheads |
| Body | `1rem` (16px) | 400–500 | 1.5–1.7 | Paragraph text |
| Label | `0.875rem` (14px) | 500–600 | 1.4 | Captions, metadata |

### Product Register Scale (fixed rem)
| Role | Size | Weight | Line Height | Use |
|------|------|--------|-------------|-----|
| H1 | `1.5rem` | 600 | 1.3 | Page titles |
| H2 | `1.25rem` | 600 | 1.3 | Section headings |
| H3 | `1.125rem` | 600 | 1.4 | Sub-sections |
| Body | `1rem` | 400 | 1.5 | Default text |
| Small | `0.875rem` | 400 | 1.4 | Metadata, captions |

## Weight Rules

### Brand Register
- **Light-heavy contrast** creates visual drama
- Display can be light (300) while body is medium (500)
- ALL-CAPS labels need tracking: `letter-spacing: 0.05em–0.12em`

### Product Register
- **Functional hierarchy** over drama
- Use weight to distinguish importance, not to create mood
- Minimum 1.25 ratio between type steps

## Line Height & Letter Spacing Standards

| Situation | Rule |
|-----------|------|
| Body text on dark background | Bump line-height +0.05–0.1, add letter-spacing 0.01–0.02em |
| ALL-CAPS text | Add `letter-spacing: 0.05em–0.12em` |
| Headings | `text-wrap: balance` |
| Prose/paragraphs | `text-wrap: pretty` |
| Body line length | Cap at `max-width: 65ch` |
| Body text minimum | 16px (1rem) — below this fails WCAG on mobile |

## Web Font Loading

- Use `font-display: swap`
- Preload the critical weight only
- Match fallback metrics to minimize CLS
- Use `@font-face` with `unicode-range` for subset loading

## Cross-References

- **Brand register font selection:** See `skills/ui-ux/reference/brand.md` > Font Selection (4-step procedure + reflex-reject list)
- **Product register typography:** See `skills/ui-ux/reference/product.md` > Product Register
- **General typography rules:** See `skills/ui-ux/SKILL.md` Layer 2 > Typography
