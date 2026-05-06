# SYSTEM THINKING — REASONING PROTOCOL

**Load when:** Architectural tasks, multi-system problems, recurring bugs, irreversible decisions, anything that touches multiple teams or services.
**Skip when:** Single-module changes, easily reversible fixes, obvious tasks.

---

## THE 12 THINKING DIMENSIONS

Check these before acting on any non-trivial task. Not every dimension applies — but the habit of checking is mandatory.

1. **PURPOSE** — What is the real objective? Not the surface request — the actual goal. What will be different if this succeeds perfectly?
2. **DEPENDENCY MAPPING** — What does this connect to? What upstream inputs does it need? What downstream systems consume its output? What changes if this changes?
3. **TRADEOFF ANALYSIS** — What am I gaining? What am I sacrificing? Is that acceptable? Name it explicitly — never hide tradeoffs.
4. **FAILURE MODE THINKING** — How can this break? What's the blast radius? Is failure silent or visible? What's the recovery path?
5. **BOUNDARY IDENTIFICATION** — Where does this system end and another begin? Where are the trust boundaries? What data crosses boundaries — is it validated at each crossing?
6. **TEMPORAL REASONING** — Will this decision make sense in 6 months? What becomes harder to change over time? What creates future maintenance burden?
7. **CONSTRAINT SEPARATION** — What are real constraints vs assumed ones? Question assumptions before building on them.
8. **PATTERN RECOGNITION** — Have I seen this problem shape before? State management? Data flow? Coordination? Boundary? Apply known solutions — but verify the pattern actually matches.
9. **SIMPLICITY BIAS** — What is the simplest approach that actually works? Complexity is a cost, not a feature.
10. **REVERSIBILITY CHECK** — Can I undo this easily? Reversible = decide fast. Irreversible = slow down and verify.
11. **FEEDBACK LOOP AWARENESS** — Does this system signal when something is wrong? Can I observe its health? Unobservable systems are unmanageable.
12. **LEVERAGE POINT** — Where is the smallest change that produces the largest effect? Structural fixes at the right leverage point beat ten surface patches.

---

## SYSTEM DECOMPOSITION MODEL

Break every problem into these components before solving:

1. **CURRENT STATE** — What exists now? What is the actual situation?
2. **DESIRED STATE** — What should exist after? What does success look like?
3. **GAP** — What is missing between current and desired?
4. **CONSTRAINTS** — What limits our options? (real vs assumed)
5. **OPTIONS** — What approaches could work? Generate at least 3.
6. **TRADEOFFS** — What does each option cost and gain?
7. **RECOMMENDED PATH** — What will we do and in what order?
8. **VERIFICATION PLAN** — How will we confirm it worked?

**Rules:** Never skip step 1 (you can't navigate without knowing where "here" is). Never skip step 3 (the gap IS the problem). Never present fewer than 3 options. Never skip step 8 (a solution without a verification plan is a hope).

---

## SYSTEM MAPPING PROTOCOL

When facing a non-trivial task, mentally map before acting:

1. **Components** — list all major parts: services, modules, databases, APIs, queues, external deps
2. **Actors** — who or what interacts with this system?
3. **Data flow** — inputs → processing → storage → outputs. Where does data transform? Where could it be lost or corrupted?
4. **Dependencies** — runtime, build-time, operational, human
5. **Boundaries** — what does this own vs consume vs assume?
6. **Failure points** — single points of failure, cascading paths, silent failures
7. **Observation** — how do we know if it's working? What metrics and logs exist?

---

## FAILURE-MODE PROTOCOL

For any significant implementation, ask:

**Identification:** What are the most likely failure modes? The highest-impact ones? What happens with malformed, missing, or malicious input? What breaks first under load?

**Detection:** How would we know it failed? Is the failure visible or silent? How long before we detect it?

**Impact:** What's the blast radius? Does it degrade gracefully or collapse catastrophically?

**Recovery:** What's the rollback path? What data could be lost? How do we verify full health after recovery?

**Prevention:** Can we prevent it entirely? Contain the blast radius (circuit breakers, feature flags)? Detect it earlier (input validation, health checks)?

---

## TRADEOFF TABLE

| Tension | Default Resolution |
| :--- | :--- |
| Speed vs Quality | Reduce scope rather than quality. "What is the smallest correct version?" |
| Flexibility vs Simplicity | Design for requirements you have now. YAGNI. |
| Short-term vs Long-term | Reversible → favor short-term speed. Irreversible → favor long-term safety. |
| Performance vs Complexity | Write simple code first. Profile. Optimize only the measured bottleneck. |
| Security vs Convenience | Find least-friction way to maintain security. Never sacrifice security for convenience. |
| Consistency vs Optimal local | Only break consistency if the alternative is dramatically better AND you plan to migrate everything. |
| DRY vs Clarity | Duplication is cheaper than the wrong abstraction. Wait for 3+ concrete cases before abstracting. |

---

## DIAGNOSTIC TRIGGERS

### Apply full system thinking when

- Task involves multiple components or services
- Change is irreversible or expensive to reverse
- Bug keeps recurring despite previous fixes
- System exhibits spiky, unpredictable behavior
- Task affects other teams, services, or pipelines
- Designing something new that will persist (architecture, schema, API contract)

### Light system thinking minimum (always)

- Check PURPOSE: am I solving the right problem?
- Check DEPENDENCIES: what does this connect to?
- Check FAILURE MODES: how can this break?
- Check REVERSIBILITY: can I undo this?

---

## KEY INSIGHT

> Systems are perfectly designed to produce the results they are currently producing.

If the system produces bugs → the structure creates bugs.
If the system produces slow deployments → the structure slows deployments.

Do not blame components. Examine the structure. Change the structure to change the results.

When you fix a bug: ask "What about the system's structure allowed this bug to exist?"
