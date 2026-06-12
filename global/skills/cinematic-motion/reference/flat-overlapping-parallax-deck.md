# Flat Overlapping Parallax Deck

This is a reference for a pinned overlapping GSAP parallax deck, created June 12, 2026.
It stacks cards absolutely on top of each other and uses a single ScrollTrigger timeline to slide them up from the bottom (yPercent: 100 to 0), while simultaneously scaling down and tilting the card underneath it.

## CSS Reference
``css
/* src/style.css */
:root {
  --bg-primary: #09090B;
  --text-primary: #E4E4E7;
  --text-secondary: #A1A1AA;
  --accent-primary: #D97706;
  
  --font-display: 'Cormorant Garamond', Georgia, serif;
  --font-body: 'Montserrat', Helvetica, sans-serif;
  
  --glass-bg: rgba(9, 9, 11, 0.5);
  --glass-border: rgba(228, 228, 231, 0.1);
  --glass-blur: 12px;

  /* Luxury Ivory & Warm Dark Theme */
  --ivory-main: #F7E8CF;
  --ivory-accent: #FFF2D8;
  --espresso-shadow: 0 3px 18px rgba(43, 26, 18, 0.55);
  --espresso-shadow-strong: 0 3px 18px rgba(43, 26, 18, 0.60);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html {
  width: 100%;
  height: 100%;
  background-color: var(--bg-primary); /* Canvas fallback — html keeps the dark bg */
  color: var(--text-primary);
  font-family: var(--font-body);
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

body {
  width: 100%;
  height: 100%;
  background-color: transparent; /* ROOT CAUSE FIX: opaque body was covering the fixed video */
  color: inherit;
  font-family: inherit;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

/* Lenis */
html.lenis { height: auto; }
.lenis.lenis-smooth { scroll-behavior: auto; }
.lenis.lenis-smooth [data-lenis-prevent] { overscroll-behavior: contain; }
.lenis.lenis-stopped { overflow: hidden; }
.lenis.lenis-scrolling iframe { pointer-events: none; }

/* ACT I: Hero & Pinned Scene */
.pinned-scene-wrapper {
  position: relative;
  width: 100vw;
  height: 100svh;
  overflow: hidden;
}

.act-i-foreground {
  position: absolute;
  inset: 0;
  z-index: 20;
  pointer-events: none;
  background-color: var(--bg-primary);
  will-change: mask, -webkit-mask;
}
.act-i-foreground-masked {
  mask: url(#blinds-mask);
  -webkit-mask: url(#blinds-mask);
}

.hero-container {
  position: absolute;
  inset: 0;
  overflow: hidden;
  z-index: 20;
  pointer-events: auto;
  background-color: var(--bg-primary);
  will-change: transform;
  --after-opacity: 1;
}
.hero-container::after {
  content: "";
  position: absolute;
  inset: 0;
  opacity: var(--after-opacity);
  background: linear-gradient(
    90deg,
    rgba(9, 9, 11, 0.05) 0%,
    rgba(9, 9, 11, 0.22) 55%,
    rgba(9, 9, 11, 0.48) 100%
  );
  z-index: 2;
  pointer-events: none;
}
.sanctuary-ambient {
  position: absolute;
  inset: -5%; /* Slightly larger to avoid blurred edges showing background */
  z-index: 0;
  filter: blur(80px) saturate(1.5);
  opacity: 0;
  pointer-events: none;
  will-change: opacity;
}
.sanctuary-ambient video { width: 100%; height: 100%; object-fit: cover; }

.sanctuary { position: absolute; inset: 0; z-index: 1; background-color: transparent; }
.sanctuary-video { width: 100%; height: 100%; object-fit: cover; will-change: transform, clip-path; }
.threshold { position: absolute; inset: 0; background-color: var(--bg-primary); display: flex; align-items: center; justify-content: center; z-index: 2; pointer-events: none; }
.threshold-text { 
  font-family: var(--font-display);
  font-size: clamp(3rem, 5.5vw, 6rem);
  font-weight: 700;
  text-transform: uppercase;
  margin: 0;
  line-height: 1;
  color: var(--text-primary); 
  will-change: transform, opacity; 
  transform-origin: center center; 
}

.hero-subhead {
  font-family: var(--font-body);
  font-weight: 300;
  font-size: 1.1rem;
  color: var(--text-secondary);
  max-width: 400px;
  line-height: 1.6;
}

/* Viewport Header & Footer Frame */
.viewport-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2.5rem 6vw;
  z-index: 100;
  pointer-events: none;
  opacity: 0;
  will-change: opacity;
}
.viewport-header * {
  pointer-events: auto;
}

.brand { 
  font-family: var(--font-display); 
  font-size: 1.4rem; 
  letter-spacing: 0.1em; 
  font-weight: 700;
  color: var(--ivory-main);
  text-shadow: var(--espresso-shadow);
  text-transform: uppercase;
  transition: color 0.4s ease;
}

.nav-links { display: flex; gap: 3rem; }
.nav-links a { 
  color: var(--ivory-main); 
  text-shadow: var(--espresso-shadow);
  text-decoration: none; 
  font-family: var(--font-body);
  font-size: 0.75rem; 
  letter-spacing: 0.35em; 
  text-transform: uppercase;
  font-weight: 400;
  transition: color 0.4s ease; 
}
.nav-links a:hover { color: var(--accent-primary); }

.viewport-footer {
  position: fixed;
  bottom: 2.5rem;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 6vw;
  z-index: 100;
  pointer-events: none;
  opacity: 0;
  will-change: opacity;
}
.viewport-footer * {
  pointer-events: auto;
}

/* Audio Equalizer */
.audio-control {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
  padding: 0.5rem 0;
}
.audio-label {
  font-family: var(--font-body);
  font-size: 0.7rem;
  letter-spacing: 0.35em;
  color: var(--ivory-main);
  text-shadow: var(--espresso-shadow);
  transition: color 0.4s;
}
.audio-control:hover .audio-label {
  color: var(--accent-primary);
}
.audio-equalizer {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  width: 16px;
  height: 12px;
}
.eq-bar {
  width: 2px;
  height: 100%;
  background-color: var(--ivory-main);
  transform-origin: bottom;
  transition: background-color 0.4s, transform 0.3s;
  animation: eq-scale 1.2s ease-in-out infinite alternate;
}
.audio-control:hover .eq-bar {
  background-color: var(--accent-primary);
}
.audio-equalizer.paused .eq-bar {
  animation-play-state: paused;
  transform: scaleY(0.3) !important;
}

.bar-1 { animation-delay: 0.1s; animation-duration: 0.8s; }
.bar-2 { animation-delay: 0.3s; animation-duration: 1.1s; }
.bar-3 { animation-delay: 0.0s; animation-duration: 0.9s; }
.bar-4 { animation-delay: 0.5s; animation-duration: 1.3s; }

@keyframes eq-scale {
  0% { transform: scaleY(0.25); }
  100% { transform: scaleY(1.0); }
}

/* Capsule CTA Button */
.concierge-inquiry-capsule {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  padding: 0.8rem 2.2rem;
  border: 1px solid rgba(247, 232, 207, 0.25);
  border-radius: 100px;
  background-color: rgba(9, 9, 11, 0.45);
  cursor: pointer;
  font-family: var(--font-body);
  font-size: 0.7rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--ivory-main);
  text-shadow: var(--espresso-shadow);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  backdrop-filter: blur(var(--glass-blur));
}
.concierge-inquiry-capsule:hover {
  background-color: var(--ivory-main);
  color: var(--bg-primary);
  border-color: var(--ivory-main);
  transform: translateY(-2px);
  text-shadow: none;
}
.capsule-arrow {
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.concierge-inquiry-capsule:hover .capsule-arrow {
  transform: translateX(4px);
}

/* ACT I: Cascading Staircase Hero Text */
.staircase-layout {
  position: absolute;
  top: 50%;
  right: 12%;
  transform: translateY(-50%);
  z-index: 10;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  align-items: flex-start;
  width: max-content;
  pointer-events: none;
}

.staircase-line {
  font-size: clamp(1.8rem, 3.2vw, 4.2rem);
  font-weight: 300;
  line-height: 1.1;
  color: var(--ivory-main);
  text-shadow: var(--espresso-shadow);
  transform: translateX(calc(var(--indent) * 3.2vw));
  display: flex;
  align-items: center;
  gap: 0.75rem;
  position: relative;
  opacity: 0;
  will-change: transform, opacity;
}

.word-sans {
  font-family: var(--font-body);
  font-weight: 300;
  text-transform: lowercase;
  letter-spacing: -0.02em;
}

.word-serif-italic {
  font-family: var(--font-display);
  font-weight: 400;
  font-style: italic;
  color: var(--ivory-accent);
  text-shadow: var(--espresso-shadow-strong);
  text-transform: lowercase;
}

/* Guide Lines */
.guide-line {
  position: absolute;
  top: 55%;
  right: calc(100% + 2rem);
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(247, 232, 207, 0.25));
  width: 0px; /* animated by GSAP */
  will-change: width;
}

/* Act I: The Atelier Panel (Frosted Monolith) */
.atelier-panel {
  position: absolute;
  right: 0;
  top: 0;
  height: 100svh;
  width: 45vw;
  padding: 0 6vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  opacity: 1;
  z-index: 10;
  pointer-events: none;
  background-color: transparent;
  will-change: transform;
}

.spotlight-overlay {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at var(--spotlight-x, 0%) 50%, rgba(217, 119, 6, 0.15) 0%, transparent 60%);
  pointer-events: none;
  z-index: 1;
  will-change: background;
}

.atelier-content {
  position: relative;
  z-index: 2;
  padding: 0 6vw;
}

.atelier-title {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 4vw, 4rem);
  font-weight: 400;
  color: var(--ivory-main);
  text-shadow: var(--espresso-shadow);
  margin-bottom: 2rem;
  line-height: 1.1;
}

.atelier-body p {
  font-family: var(--font-body);
  font-size: 0.8rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ivory-accent);
  text-shadow: var(--espresso-shadow);
  line-height: 1.8;
  margin-bottom: 1.5rem;
}

/* ACT I.5: The Narrative Bridge (Stationary Underlay) */
.narrative-bridge {
  position: absolute;
  inset: 0;
  z-index: 10;
  background-color: #18120e; /* Deep warm architectural umber matching the fire/dust motes */
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  overflow: hidden;
}

.bridge-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 2rem;
}

.bridge-number {
  font-family: var(--font-body);
  font-size: 0.75rem;
  letter-spacing: 0.35em;
  color: var(--text-secondary);
  text-transform: uppercase;
  margin-bottom: 1.5rem;
}

.bridge-headline {
  font-family: var(--font-display);
  font-size: clamp(3rem, 5vw, 5rem);
  font-weight: 400;
  color: var(--ivory-main);
  text-shadow: var(--espresso-shadow);
  margin-bottom: 1.5rem;
}

.bridge-body {
  font-family: var(--font-body);
  font-size: 1rem;
  line-height: 1.8;
  color: var(--ivory-accent);
  max-width: 600px;
  font-weight: 300;
  opacity: 0.8;
}

.bridge-scroll-indicator {
  font-family: var(--font-body);
  font-size: 0.7rem;
  letter-spacing: 0.25em;
  color: var(--text-secondary);
  text-transform: uppercase;
  margin-top: 4rem;
  animation: bridge-pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes bridge-pulse {
  0%, 100% { opacity: 0.3; transform: translateY(0); }
  50% { opacity: 0.8; transform: translateY(8px); }
}

/* Act II Wrapper for pinned card stacking */
.act-ii-wrapper { 
  position: relative; 
  width: 100%; 
  height: 100svh;
  z-index: 20; 
  margin-top: 0;
  overflow: hidden;
  clip-path: inset(0 0 0 0 round 40px 40px 0 0);
  background: transparent;
  box-shadow: 0 -20px 50px rgba(0,0,0,0.5);
}

.room-section { 
  position: absolute; 
  top: 0; left: 0;
  width: 100%; 
  height: 100svh; 
  display: flex; 
  align-items: flex-end; 
  z-index: 1; 
  padding: 6vw; 
  background: transparent; 
  perspective: 1500px; /* Essential for 3D tilt effect */
  transform-style: preserve-3d;
}
/* Parallax video container acting as the physical background for each room */
.room-video-container { 
  position: absolute; 
  /* Tighter inset so the cards are wider and gaps are smaller, while keeping bent edges visible */
  inset: 1.5vh 2vw; 
  z-index: -1; /* Send it behind the text */
  overflow: clip; /* Essential for parallax cropping */
  border-radius: 40px; /* Bent edges / rounded corners! */
  pointer-events: none; 
}
.room-video-container video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  will-change: transform;
}
/* Vignette completely removed for maximum clarity */
.room-caption {
  position: relative;
  z-index: 10;
  max-width: 450px;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.room-caption-title {
  font-family: var(--font-display);
  font-size: clamp(2rem, 3.5vw, 3.5rem);
  color: var(--ivory-main);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  line-height: 1.1;
  text-shadow: var(--espresso-shadow-strong);
}
.room-caption-desc {
  font-family: var(--font-body);
  font-size: 0.9rem;
  letter-spacing: 0.15em;
  color: var(--ivory-accent);
  text-transform: uppercase;
  line-height: 1.8;
  font-weight: 300;
  text-shadow: var(--espresso-shadow-strong);
}

/* Master Cinematic Background Underlay */
#master-bg-video-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1; 
  overflow: hidden;
  /* A beautiful, deep cinematic shade replacing the looping background video */
  background: radial-gradient(circle at center, #1c1a18 0%, #080808 100%);
  will-change: clip-path;
}

.bg-video {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform: translate(-50%, -50%);
  opacity: 0;
  will-change: opacity, transform, filter;
}

.bg-video.active {
  opacity: 1; /* Full brightness */
}

.master-bg-overlay {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, transparent 30%, rgba(0, 0, 0, 0.3) 100%);
  pointer-events: none;
  z-index: 1;
}

/* ACT III: Hybrid Client Storytelling */
#storytelling-section {
  position: relative;
  width: 100%;
  height: 300vh; /* Scroll-bound pinned area */
  background: transparent;
}

.storytelling-pin-container {
  position: sticky;
  top: 0;
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.storytelling-panel {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 10vw; /* 10% outer padding */
  opacity: 0;
  visibility: hidden;
  will-change: opacity, transform;
  pointer-events: none;
}

.storytelling-panel.active {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
}

.storytelling-content {
  max-width: 800px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

.story-headline {
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 4.5vw, 4.5rem);
  font-weight: 400;
  line-height: 1.2;
  color: var(--ivory-main);
  text-shadow: var(--espresso-shadow);
  text-transform: uppercase;
}

.story-body {
  font-family: var(--font-body);
  font-size: 0.95rem;
  line-height: 1.8;
  color: var(--text-secondary);
  font-weight: 300;
  max-width: 600px;
}

.testimonial-quote {
  font-family: var(--font-display);
  font-size: clamp(2rem, 3.5vw, 3.8rem);
  font-weight: 300;
  font-style: italic;
  line-height: 1.3;
  color: var(--ivory-accent);
  text-shadow: var(--espresso-shadow-strong);
}

.testimonial-meta {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  margin-top: 1rem;
}

.testimonial-client {
  font-family: var(--font-body);
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.25em;
  color: var(--ivory-main);
}

.testimonial-location {
  font-family: var(--font-body);
  font-size: 0.7rem;
  font-weight: 400;
  letter-spacing: 0.35em;
  color: var(--text-secondary);
}

/* ACT IV: Outro / The Invitation */
#outro-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10vh 10vw; /* 10% outer padding */
  background-color: transparent;
  z-index: 10;
}

.outro-content {
  max-width: 700px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2.5rem;
  width: 100%;
}

.outro-headline {
  font-family: var(--font-display);
  font-size: clamp(3rem, 5vw, 5.5rem);
  font-weight: 400;
  line-height: 1.1;
  color: var(--ivory-main);
  text-shadow: var(--espresso-shadow);
  text-transform: uppercase;
}

.outro-body {
  font-family: var(--font-body);
  font-size: 0.95rem;
  line-height: 1.8;
  color: var(--text-secondary);
  font-weight: 300;
  max-width: 550px;
}

.diagnostic-cta-wrapper {
  margin-top: 1rem;
}

.concierge-inquiry-capsule.large-cta {
  padding: 1.2rem 3rem;
  font-size: 0.8rem;
}

.outro-footer-metadata {
  display: flex;
  justify-content: center;
  gap: 4rem;
  margin-top: 4rem;
  border-top: 1px solid rgba(247, 232, 207, 0.15);
  padding-top: 2.5rem;
  width: 100%;
}

.meta-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}

.meta-label {
  font-family: var(--font-body);
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  color: var(--ivory-main);
}

.meta-value {
  font-family: var(--font-body);
  font-size: 0.8rem;
  font-weight: 300;
  color: var(--text-secondary);
}

@media (max-width: 768px) {
  .quiet-nav { flex-direction: column; align-items: center; gap: 1rem; bottom: 2rem; padding: 0 1.5rem; }
  .punchline-container { width: 80%; right: 10%; }
}

/* Cinematic Film Grain Overlay */
.film-grain {
  position: fixed;
  inset: 0;
  z-index: 9999;
  pointer-events: none;
  opacity: 0.04;
  background-image: url('data:image/svg+xml;utf8,%3Csvg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"%3E%3Cfilter id="noiseFilter"%3E%3CfeTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/%3E%3C/filter%3E%3Crect width="100%25" height="100%25" filter="url(%23noiseFilter)"/%3E%3C/svg%3E');
}

/* Premium Split Text Typography Utilities */
.split-word, .word-wrapper {
  display: inline-block;
  white-space: nowrap;
  will-change: transform, opacity, filter;
}

.split-char {
  display: inline-block;
  will-change: transform, opacity, filter;
}

/* Hide split fragments immediately on load only if motion is enabled to prevent FOUC */
.motion-ok .split-word,
.motion-ok .split-char {
  opacity: 0;
}

``

## GSAP Reference
``typescript
import './style.css'

import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

// Video underlay controller — guards against AbortError from rapid scroll triggers
let activeVideoElement = document.getElementById('master-bg-video-active') as HTMLVideoElement;
let nextVideoElement = document.getElementById('master-bg-video-next') as HTMLVideoElement;
let currentSrc = activeVideoElement ? activeVideoElement.getAttribute('src') || '' : '';
let isTransitioning = false;

// fallow-ignore-next-line complexity
function transitionToVideo(newSrc: string, duration: number = 1.5) {
  // Deduplicate: ignore if same video is already playing
  if (currentSrc === newSrc) return;
  // Guard: if a transition is mid-flight, don't stack another load() on top
  // (that's what causes the AbortError — load() interrupts an in-flight play())
  if (isTransitioning) {
    // Queue the intent: when the current transition finishes, we'll be on the right video
    // For now, just update the target src so the next onEnter picks it up
    currentSrc = newSrc;
    return;
  }

  currentSrc = newSrc;
  isTransitioning = true;

  if (!nextVideoElement || !activeVideoElement) {
    isTransitioning = false;
    return;
  }

  // Kill any existing tweens on these elements before starting new ones
  gsap.killTweensOf([activeVideoElement, nextVideoElement]);

  nextVideoElement.src = newSrc;
  nextVideoElement.load();

  const playPromise = nextVideoElement.play();
  if (playPromise === undefined) {
    // Old browser: no promise returned, just cross-fade immediately
    gsap.set(activeVideoElement, { opacity: 0 });
    gsap.set(nextVideoElement, { opacity: 0.75 });
    const temp = activeVideoElement; activeVideoElement = nextVideoElement; nextVideoElement = temp;
    isTransitioning = false;
    return;
  }

  playPromise.then(() => {
    gsap.timeline({ onComplete: () => { isTransitioning = false; } })
      .to(activeVideoElement, { opacity: 0, duration: duration, ease: "power2.inOut" })
      .to(nextVideoElement, { opacity: 0.75, duration: duration, ease: "power2.inOut" }, 0)
      .call(() => {
        const temp = activeVideoElement;
        activeVideoElement = nextVideoElement;
        nextVideoElement = temp;
      });
  }).catch((err: Error) => {
    // AbortError is expected if the user scrolls very fast — handle gracefully
    if (err.name === 'AbortError') {
      // The src was already updated; just swap state silently
      const temp = activeVideoElement; activeVideoElement = nextVideoElement; nextVideoElement = temp;
    } else {
      console.warn("Video transition error:", err);
    }
    isTransitioning = false;
  });
}

// Force scroll to top on every page load — prevents GSAP from waking mid-animation
// when Chrome restores the previous scroll position
if ('scrollRestoration' in history) {
  history.scrollRestoration = 'manual';
}
window.scrollTo(0, 0);

import { initSmoothScroll } from './utils/scroll'

// 1. Lenis Smooth Scroll Foundation
initSmoothScroll()

const actIiRooms = document.querySelectorAll('.room-section')

/**
 * Splits text contents into nested word/character spans for premium staggered reveals.
 * Preserves accessibility defaults and HTML5 inline elements like <br>.
 */
function splitTextIntoSpans(element: HTMLElement, type: 'chars' | 'words' = 'chars') {
  const originalText = element.textContent || '';
  element.setAttribute('aria-label', originalText);
  
  const childNodes = Array.from(element.childNodes);
  const newContent = document.createDocumentFragment();
  
  childNodes.forEach((node) => {
    if (node.nodeType === Node.TEXT_NODE) {
      const text = node.textContent || '';
      const parts = text.split(/(\s+)/);
      
      parts.forEach((part) => {
        if (part.trim() === '') {
          newContent.appendChild(document.createTextNode(part));
        } else {
          const wordSpan = document.createElement('span');
          wordSpan.className = type === 'chars' ? 'word-wrapper' : 'split-word';
          
          if (type === 'chars') {
            const chars = part.split('');
            chars.forEach((char) => {
              const charSpan = document.createElement('span');
              charSpan.className = 'split-char';
              charSpan.textContent = char;
              charSpan.setAttribute('aria-hidden', 'true');
              wordSpan.appendChild(charSpan);
            });
          } else {
            wordSpan.textContent = part;
            wordSpan.setAttribute('aria-hidden', 'true');
          }
          newContent.appendChild(wordSpan);
        }
      });
    } else if (node.nodeType === Node.ELEMENT_NODE) {
      const el = node as HTMLElement;
      if (el.tagName === 'BR') {
        newContent.appendChild(document.createElement('br'));
      } else {
        newContent.appendChild(el.cloneNode(true));
      }
    }
  });
  
  element.innerHTML = '';
  element.appendChild(newContent);
}

// Split text elements for kinetic and stagger reveals immediately on load
const atelierTitle = document.querySelector('.atelier-title') as HTMLElement;
const atelierParagraphs = document.querySelectorAll('.atelier-body p');
const bridgeHeadline = document.querySelector('.bridge-headline') as HTMLElement;
const bridgeBody = document.querySelector('.bridge-body') as HTMLElement;

if (atelierTitle) splitTextIntoSpans(atelierTitle, 'chars');
atelierParagraphs.forEach((p) => splitTextIntoSpans(p as HTMLElement, 'words'));
if (bridgeHeadline) splitTextIntoSpans(bridgeHeadline, 'words');
if (bridgeBody) splitTextIntoSpans(bridgeBody, 'words');

const mm = gsap.matchMedia()

// Act I Elements
const heroContainer = document.querySelector('.hero-container') as HTMLElement
const actIForeground = document.querySelector('.act-i-foreground') as HTMLElement
const threshold = document.querySelector('.threshold') as HTMLElement
const thresholdText = document.querySelector('.threshold-text') as HTMLElement
const punchlines = gsap.utils.toArray('.punchline-text') as HTMLElement[]



// fallow-ignore-next-line complexity
mm.add("(prefers-reduced-motion: no-preference)", () => {
  
  // ==========================================
  // ACT I: THE THRESHOLD (Hero Sequence)
  // ==========================================
  // Generate SVG Rects for Horizontal Blinds Transition
  const BLIND_COUNT = 30;
  const blindsGroup = document.getElementById('blinds-group');
  const topRects: SVGRectElement[] = [];
  const bottomRects: SVGRectElement[] = [];
  const h = 1.0 / BLIND_COUNT; 

  if (blindsGroup) {
    for (let i = 0; i < BLIND_COUNT; i++) {
      const yStart = i * h;
      const centerY = yStart + (h / 2);
      
      const rectTop = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rectTop.setAttribute('x', '-0.05');
      rectTop.setAttribute('y', yStart.toString());
      rectTop.setAttribute('width', '1.1');
      rectTop.setAttribute('height', (h / 2 + 0.002).toString());
      rectTop.setAttribute('fill', 'white');
      blindsGroup.appendChild(rectTop);
      topRects.push(rectTop);

      const rectBottom = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rectBottom.setAttribute('x', '-0.05');
      rectBottom.setAttribute('y', centerY.toString());
      rectBottom.setAttribute('width', '1.1');
      rectBottom.setAttribute('height', (h / 2 + 0.002).toString());
      rectBottom.setAttribute('fill', 'white');
      blindsGroup.appendChild(rectBottom);
      bottomRects.push(rectBottom);
    }
  }

  const masterTl = gsap.timeline({
    scrollTrigger: {
      trigger: '.pinned-scene-wrapper',
      start: 'top top',
      end: '+=500%', 
      pin: true,
      scrub: 1, 
      anticipatePin: 1
    }
  });

    // Open the Door
    masterTl.to(thresholdText, { scale: 25, opacity: 0, ease: "power2.inOut", duration: 1.0 }, 0)
      .to(threshold, { opacity: 0, ease: "power2.inOut", duration: 0.8 }, 0.2);

    // Fade in viewport header and footer once threshold opens
    masterTl.to(['.viewport-header', '.viewport-footer'], {
      opacity: 1,
      duration: 1.0,
      ease: "power2.out"
    }, 0.8);

    // Staircase sequential build
    punchlines.forEach((el, i) => {
      const time = 1.0 + i * 0.45; // stagger line starts
      
      // Animate the text line slide up & fade in
      masterTl.fromTo(el, 
        { y: 30, opacity: 0 },
        { y: 0, opacity: 1, ease: "power2.out", duration: 0.8 }, 
        time
      );

      // Find if this line has a guide-line and animate its width
      const guideLine = el.querySelector('.guide-line');
      if (guideLine) {
        masterTl.fromTo(guideLine,
          { width: "0vw" },
          { width: "12vw", ease: "power1.inOut", duration: 0.8 },
          time + 0.3 // start line drawing slightly after text begins revealing
        );
      }
    });

    // Fade out the entire staircase layout together before the Atelier panel appears
    masterTl.to('.staircase-layout', {
      y: -50,
      opacity: 0,
      ease: "power2.in",
      duration: 1.0
    }, 4.2);

    // Spatial Reframing: Cinematic Aspect Ratio Squeeze
    // Physically crops the video using the exact specs from the global motion library
    masterTl.fromTo('.hero-container', 
      { clipPath: "inset(0vh 0vw 0vh 0vw round 0px)" },
      { 
        clipPath: "inset(15vh 55vw 15vh 5vw round 24px)", 
        ease: "power3.inOut", 
        duration: 1.8 
      }, 
      4.6
    );
    masterTl.fromTo('.hero-container',
      { "--after-opacity": 0 },
      {
        "--after-opacity": 0.3, // Subtle dimming to focus on the Atelier Panel
        ease: "power3.inOut",
        duration: 1.8
      },
      4.6
    );

    // The Atelier Panel slides perfectly into the void created by the squeeze
    masterTl.fromTo('.atelier-panel',
      { xPercent: 100, opacity: 1 }, 
      { xPercent: 0, ease: "power3.inOut", duration: 1.8 },
      4.6
    );

    // Premium kinetic jingle reveal for Atelier Title (THE ATELIER OF SILENCE)
    const titleChars = document.querySelectorAll('.atelier-title .split-char');
    titleChars.forEach((char, index) => {
      const startTime = 5.2 + index * 0.035;
      masterTl.to(char, {
        y: -8,
        opacity: 1,
        filter: "blur(0px)",
        duration: 0.4,
        ease: "power2.out"
      }, startTime)
      .to(char, {
        x: -3,
        rotation: -4,
        duration: 0.08,
        ease: "none"
      }, startTime + 0.4)
      .to(char, {
        x: 3,
        rotation: 3,
        duration: 0.08,
        ease: "none"
      }, startTime + 0.48)
      .to(char, {
        x: -1.5,
        rotation: -2,
        duration: 0.06,
        ease: "none"
      }, startTime + 0.56)
      .to(char, {
        x: 0,
        y: 0,
        rotation: 0,
        duration: 0.18,
        ease: "power2.out"
      }, startTime + 0.62);
    });

    // Premium word stagger reveal for Atelier Body paragraphs
    const bodyWords = document.querySelectorAll('.atelier-body .split-word');
    masterTl.fromTo(bodyWords, {
      y: 30,
      opacity: 0,
      filter: "blur(4px)"
    }, {
      y: 0,
      opacity: 1,
      filter: "blur(0px)",
      stagger: 0.02,
      ease: "power3.out",
      duration: 0.8
    }, 5.8);

    // Fade out viewport UI and Atelier Panel (directly from squeezed state)
    masterTl.to(['.viewport-header', '.viewport-footer', '.atelier-panel'], {
      opacity: 0,
      y: -30,
      ease: "power2.inOut",
      duration: 1.0
    }, 8.4);

    // Apply the mask to the foreground wrapper right before the transition
    masterTl.call(() => {
      actIForeground.classList.add('act-i-foreground-masked');
    }, undefined, 8.4);

    // CURTAIN REVEAL: SVG Mask Horizontal Blinds (wiping the squeezed video)
    masterTl.to(topRects, {
      attr: {
        y: (i) => {
          const yStart = i * h;
          return yStart + (h / 2);
        },
        height: 0
      },
      stagger: { each: 0.015, from: "end" },
      ease: "power2.inOut",
      duration: 1.0
    }, 8.4);

    masterTl.to(bottomRects, {
      attr: {
        height: 0
      },
      stagger: { each: 0.015, from: "end" },
      ease: "power2.inOut",
      duration: 1.0
    }, 8.4);

    // Make the narrative bridge wrapper visible
    masterTl.to('.bridge-content', {
      opacity: 1,
      ease: "none",
      duration: 0.1
    }, 8.4);

    // Staggered reveals for Narrative Bridge elements
    masterTl.fromTo('.bridge-number', 
      { y: 30, opacity: 0 },
      { y: 0, opacity: 1, ease: "power2.out", duration: 0.8 },
      8.8
    );

    const bridgeHeadlineWords = document.querySelectorAll('.bridge-headline .split-word');
    masterTl.fromTo(bridgeHeadlineWords, {
      y: 30,
      opacity: 0,
      filter: "blur(4px)"
    }, {
      y: 0,
      opacity: 1,
      filter: "blur(0px)",
      stagger: 0.04,
      ease: "power3.out",
      duration: 0.8
    }, 9.0);

    const bridgeBodyWords = document.querySelectorAll('.bridge-body .split-word');
    masterTl.fromTo(bridgeBodyWords, {
      y: 30,
      opacity: 0,
      filter: "blur(4px)"
    }, {
      y: 0,
      opacity: 0.8,
      filter: "blur(0px)",
      stagger: 0.018,
      ease: "power3.out",
      duration: 0.8
    }, 9.4);

    masterTl.fromTo('.bridge-scroll-indicator',
      { y: 20, opacity: 0 },
      { y: 0, opacity: 1, ease: "power2.out", duration: 1.0 },
      10.2
    );
  // ==========================================
  // ACT II: THE DESCENT (Vertical Parallax)
  // ==========================================
  
  const actIiWrapper = document.querySelector('.act-ii-wrapper');
  const actIiRooms = gsap.utils.toArray<HTMLElement>('.room-section.act-ii');

  // Strict, confined snapping using GSAP so it NEVER affects Act I or Act III
  ScrollTrigger.create({
    trigger: '.act-ii-wrapper',
    start: 'top top',
    end: 'bottom bottom',
    snap: {
      snapTo: 1 / (actIiRooms.length - 1),
      duration: { min: 0.3, max: 0.8 },
      delay: 0.05,
      ease: "power2.inOut"
    }
  });



  // Reset clip-path on entering Act II
  ScrollTrigger.create({
    trigger: '.act-ii-wrapper',
    start: 'top bottom',
    onEnter: () => {
      gsap.set('#master-bg-video-container', { clipPath: "inset(0vh 0vw 0vh 0vw round 0px)" });
    }
  });

  // Parallax translation on the fixed container across the entire descent
  gsap.fromTo('#master-bg-video-container', 
    { yPercent: -10 },
    { 
      yPercent: 10, 
      ease: 'none',
      scrollTrigger: {
        trigger: '.act-ii-wrapper',
        start: 'top bottom',
        end: 'bottom top',
        scrub: true
      }
    }
  );

  // --- ACT II: 3D Overlapping Parallax Deck ---

  if (actIiWrapper && actIiRooms.length > 0) {
    const deckTimeline = gsap.timeline();

    // 1. Setup Initial States
    actIiRooms.forEach((room, index) => {
      const container = room.querySelector('.room-video-container');
      const captionTitle = room.querySelector('.room-caption-title');
      const captionDesc = room.querySelector('.room-caption-desc');
      
      // Ensure z-index layers them correctly
      gsap.set(room, { zIndex: index + 1 });
      
      if (index === 0) {
        // First card starts fully visible
        gsap.set(container, { yPercent: 0, rotationX: 0, scale: 1 });
        gsap.set([captionTitle, captionDesc], { autoAlpha: 1, y: 0 });
      } else {
        // Subsequent cards start off-screen bottom, tilted back
        gsap.set(container, { yPercent: 100, rotationX: -10, scale: 1 });
        gsap.set([captionTitle, captionDesc], { autoAlpha: 0, y: 30 });
      }
    });

    // 2. Build the Timeline
    actIiRooms.forEach((room, index) => {
      const container = room.querySelector('.room-video-container');
      const media = room.querySelector('.room-video-container video');
      const captionTitle = room.querySelector('.room-caption-title');
      const captionDesc = room.querySelector('.room-caption-desc');

      if (index > 0) {
        const prevRoomContainer = actIiRooms[index - 1].querySelector('.room-video-container');
        const prevCaptionTitle = actIiRooms[index - 1].querySelector('.room-caption-title');
        const prevCaptionDesc = actIiRooms[index - 1].querySelector('.room-caption-desc');
        
        // Incoming card slides up and flattens out
        deckTimeline.to(container, {
          yPercent: 0,
          rotationX: 0,
          ease: "none"
        }, `slide-${index}`);

        // Outgoing card scales down, tilts forward, and dims
        if (prevRoomContainer) {
          deckTimeline.to(prevRoomContainer, {
            scale: 0.85,
            rotationX: 10,
            opacity: 0.3,
            ease: "none"
          }, `slide-${index}`);
        }

        // Incoming captions fade in
        if (captionTitle && captionDesc) {
          deckTimeline.to([captionTitle, captionDesc], {
            autoAlpha: 1,
            y: 0,
            stagger: 0.1,
            ease: "power2.out"
          }, `slide-${index}`);
        }

        // Outgoing captions fade up and out
        if (prevCaptionTitle && prevCaptionDesc) {
          deckTimeline.to([prevCaptionTitle, prevCaptionDesc], {
            autoAlpha: 0,
            y: -30,
            ease: "power2.in"
          }, `slide-${index}`);
        }
      }

      // 3. Internal Media Parallax
      if (media && index > 0) {
        gsap.set(media, { yPercent: -15 });
        deckTimeline.to(media, {
          yPercent: 15,
          ease: "none"
        }, `slide-${index}`);
      } else if (media && index === 0) {
        // First media starts centered, moves down when covered
        deckTimeline.to(media, {
          yPercent: 15,
          ease: "none"
        }, `slide-1`);
      }
    });

    // 4. Pin the wrapper and scrub
    ScrollTrigger.create({
      trigger: actIiWrapper,
      start: "top top",
      end: `+=${actIiRooms.length * 100}%`,
      pin: true,
      animation: deckTimeline,
      scrub: 1, // Smooth scrubbing
      fastScrollEnd: true
    });
  }


  // ==========================================
  // ACT III: HYBRID CLIENT STORYTELLING & ACT IV OUTRO
  // ==========================================
  const storyTl = gsap.timeline({
    scrollTrigger: {
      trigger: "#storytelling-section",
      start: "top top",
      end: "bottom bottom",
      pin: true,
      scrub: 1.2,
      onEnter: () => {
        transitionToVideo('/videos/Slow_push_into_sunken_salon_202606112050.mp4', 1.5);
        gsap.to('.master-bg-overlay', { backgroundColor: 'rgba(9, 9, 11, 0.75)', duration: 0.8 }); // Increase dimming for text
      },
      onEnterBack: () => {
        transitionToVideo('/videos/Slow_push_into_sunken_salon_202606112050.mp4', 1.5);
        gsap.to('.master-bg-overlay', { backgroundColor: 'rgba(9, 9, 11, 0.75)', duration: 0.8 });
      }
    }
  });

  // Panel transitions using autoAlpha for smooth visibility + opacity
  gsap.set('.storytelling-panel', { autoAlpha: 0, y: 30 });
  
  storyTl.to(".intro-panel", { autoAlpha: 1, y: 0, duration: 1.0, ease: "power2.out" });
  storyTl.to({}, { duration: 1.5 }); // Pinned hold

  storyTl.to(".intro-panel", { autoAlpha: 0, y: -30, duration: 1.0, ease: "power2.in" })
    .to("[data-testimonial='1']", { autoAlpha: 1, y: 0, duration: 1.0, ease: "power2.out" }, "+=0.2");
  storyTl.to('#master-bg-video-container', { scale: 1, duration: 2.0, ease: "power1.inOut" }, "-=2.0"); // Camera drift
  storyTl.to({}, { duration: 1.5 });

  storyTl.to("[data-testimonial='1']", { autoAlpha: 0, y: -30, duration: 1.0, ease: "power2.in" })
    .to("[data-testimonial='2']", { autoAlpha: 1, y: 0, duration: 1.0, ease: "power2.out" }, "+=0.2");
  storyTl.to('#master-bg-video-container', { scale: 1.0, duration: 2.0, ease: "power1.inOut" }, "-=2.0"); // Return drift
  storyTl.to({}, { duration: 1.5 });

  storyTl.to("[data-testimonial='2']", { autoAlpha: 0, y: -30, duration: 1.0, ease: "power2.in" });

  // ACT IV: OUTRO RESOLUTION
  const outroTl = gsap.timeline({
    scrollTrigger: {
      trigger: "#outro-section",
      start: "top bottom",
      end: "bottom bottom",
      scrub: 1.2,
      onEnter: () => {
        transitionToVideo('/videos/Static_camera_subtle_pan_left_202606091909.mp4', 1.5);
        gsap.to('.master-bg-overlay', { backgroundColor: 'rgba(9, 9, 11, 0.4)', duration: 0.8 }); // Lighten overlay for final room glow
      },
      onEnterBack: () => {
        transitionToVideo('/videos/Static_camera_subtle_pan_left_202606091909.mp4', 1.5);
        gsap.to('.master-bg-overlay', { backgroundColor: 'rgba(9, 9, 11, 0.4)', duration: 0.8 });
      }
    }
  });

  // Cinematic Letterbox Frame Resolution
  outroTl.to("#master-bg-video-container", {
    clipPath: "inset(8vh 8vw 8vh 8vw round 24px)",
    ease: "power2.inOut",
    duration: 2.0
  });

  // Soft blur and dim overlay on active background video
  outroTl.fromTo("#master-bg-video-container .bg-video", 
    { filter: "brightness(0.75) blur(0px)" },
    { 
      filter: "brightness(0.35) blur(2px)",
      duration: 2.0
    }, 0);
})

// Reduced Motion Fallback
mm.add("(prefers-reduced-motion: reduce)", () => {
  const tl = gsap.timeline({
    scrollTrigger: { trigger: heroContainer, start: 'top top', end: 'bottom top', scrub: true }
  });
  tl.to(thresholdText, { opacity: 0, duration: 0.5 }, 0)
    .to(threshold, { opacity: 0, duration: 0.5 }, 0.5);
});

// 3. Audio Equalizer Interaction
const audioControl = document.querySelector('.audio-control');
const audioEqualizer = document.querySelector('.audio-equalizer');
if (audioControl && audioEqualizer) {
  audioControl.addEventListener('click', () => {
    audioEqualizer.classList.toggle('paused');
  });
}

``
