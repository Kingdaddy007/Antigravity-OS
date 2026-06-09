# Motion Personalities

Seven distinct approaches to how things move on screen. Each personality
is a complete motion strategy — not just easing curves, but a philosophy
of movement.

---

## 1. BRUTAL

**Feeling:** Fast, snapping, aggressive. High contrast, sharp transitions.
**When to use:** Tech startups, gaming, disruptive brands, high-energy launches.
**Easing:** expo.out, power2.out (fast start, decisive stop)
**Speed:** 200-400ms (snappy)
**Scroll pacing:** Aggressive 1:3 scroll-distance-to-event ratio
**Micro-animations:** Violent snapping into alignment from scattered positions
**Character:** The interface moves like it has somewhere to be. No hesitation.

**Technical spec:**
- GSAP: `expo.out` easing, short durations (0.2-0.4s)
- ScrollTrigger: Fast scrub (1-2), tight start/end triggers
- Framer Motion: `spring` with high stiffness, low damping
- CSS: `transition: 150ms cubic-bezier(0.16, 1, 0.3, 1)`

---

## 2. GLACIAL

**Feeling:** Very slow, deliberate, suspenseful. Long pauses, gradual reveals.
**When to use:** Luxury, wellness, atmospheric brands, slow-burn storytelling.
**Easing:** power1.inOut, power4.inOut (smooth, unhurried)
**Speed:** 600-1200ms (deliberate, breathing)
**Scroll pacing:** Long scroll distances per event (4-6x viewport)
**Density:** Often minimal — one idea per section, generous whitespace

**Technical spec:**
- GSAP: Long durations (0.8-1.5s), slow stagger (0.1-0.2s)
- ScrollTrigger: Slow scrub (1.5-3), extended start/end range
- Framer Motion: `transition: { duration: 0.8, ease: [0.25, 1, 0.5, 1] }`
- CSS: `transition: 800ms cubic-bezier(0.25, 1, 0.5, 1)`

---

## 3. MECHANICAL

**Feeling:** Steady, controlled, precise. Fixed rhythms, typewriter effects.
**When to use:** SaaS, professional services, structured/clinical brands.
**Easing:** power2.inOut, linear (predictable, no surprises)
**Speed:** 200-400ms (responsive, consistent)
**Scroll pacing:** Standard 1:1 scroll-to-event ratio
**Density:** Moderate — structured hierarchy, clear sections

**Technical spec:**
- GSAP: Medium durations (0.3-0.5s), consistent stagger (0.05s)
- ScrollTrigger: Standard scrub (1), predictable triggers
- Framer Motion: `transition: { duration: 0.3, ease: 'easeInOut' }`
- CSS: `transition: 300ms ease-in-out`
- Typewriter effect: Print characters at fixed 15ms interval

---

## 4. STUTTERED

**Feeling:** Irregular, fragmented, disrupted. Glitch effects, variable timing.
**When to use:** Experimental studios, cybersecurity, fractured narratives.
**Easing:** Custom curves with pauses, `elastic.out` with low bounce
**Speed:** Variable — fast bursts (100ms) then long pauses (500ms)
**Scroll pacing:** Variable scroll speed, erratic triggers
**Density:** Moderate to maximalist — fragmented elements

**Technical spec:**
- GSAP: Variable durations, `.call()` for pauses, glitch transforms
- ScrollTrigger: Dynamic end triggers, snap points with elastic
- Framer Motion: `transition: { type: 'spring', stiffness: 100, damping: 10 }`
- CSS: `animation: glitch 0.3s ease-in-out infinite alternate`
- Glitch effects: Random opacity/transform shifts, chromatic aberration

---

## 5. LIQUID

**Feeling:** Smooth, flowing, organic. Fluid simulations, buttery interpolation.
**When to use:** Lifestyle brands, intimate/coaching, warm/inviting brands.
**Easing:** sine.inOut, expo.out (smooth, natural)
**Speed:** 400-800ms (flowing, not rushed)
**Scroll pacing:** Smooth 1:1.5 scroll ratio, mathematically perfect
**Density:** Minimal to moderate — breathing room, organic shapes

**Technical spec:**
- GSAP: Smooth durations (0.5-0.8s), sine easing
- ScrollTrigger: Lenis for smooth scroll, 1.5x ratio
- Framer Motion: `transition: { duration: 0.6, ease: [0.22, 1, 0.36, 1] }`
- FBO fluid simulations for cursor interaction
- CSS: `transition: 600ms cubic-bezier(0.22, 1, 0.36, 1)`

---

## 6. SURGICAL

**Feeling:** Precise, clean, exact. Sharp cuts, minimal decoration.
**When to use:** Data platforms, investigative brands, mystery/hidden layers.
**Easing:** power2.out, expo.out (snappy, decisive)
**Speed:** 200-400ms (quick, precise)
**Scroll pacing:** Standard 1:1 with sharp snap points
**Density:** Minimal — clean, focused, no decoration

**Technical spec:**
- GSAP: Short durations (0.2-0.4s), sharp easing
- ScrollTrigger: Snap points, precise triggers
- Framer Motion: `transition: { duration: 0.25, ease: [0.16, 1, 0.3, 1] }`
- CSS: `transition: 250ms cubic-bezier(0.16, 1, 0.3, 1)`
- Stencil buffers for hidden layers

---

## 7. JITTERY

**Feeling:** Uneasy, abrupt, unsettling. Quick micro-movements, flashes.
**When to use:** Horror, psychological brands, tension-building.
**Easing:** Custom curves with sudden stops, `elastic.out` with high bounce
**Speed:** Variable — very fast (50ms) then sudden stops
**Scroll pacing:** Quick micro-scrolls (100px triggers), sharp transitions
**Density:** Maximalist — many small elements, intense detail

**Technical spec:**
- GSAP: Very short durations (0.05-0.2s), abrupt stops
- ScrollTrigger: Short triggers, sudden snap points
- Framer Motion: `transition: { type: 'spring', stiffness: 300, damping: 5 }`
- CSS: `animation: jitter 0.1s ease-in-out infinite`
- Micro-movements: Random opacity/transform shifts, camera shake
