# TEMPLATE - STACK CONTEXT

**Use this template to create or refresh `contexts/stack-context.md`.**

This template is for authoring. The final runtime file should be factual, compact, and easy to scan during real work.

---

## WHAT TO CAPTURE

- what the stack actually is today
- what is still undecided
- the main languages, frameworks, and tooling
- the most important defaults and constraints
- the current infrastructure and operational limitations

---

## AUTHORING QUESTIONS

### Current Reality

- Is this a deployed app, a prototype, or a design/build-phase project?
- What should Anti-Gravity assume right now?
- What should it explicitly not assume yet?

### Application Stack

- What languages are in use?
- What frontend and backend frameworks are in use?
- What package manager and build tools are used?
- What validation, auth, and API style are used?

### Data And Infrastructure

- What database and data access tooling are used?
- What hosting and deployment environment exists?
- What observability exists today?
- What important integrations shape technical choices?

### Constraints

- Which dependencies are pinned?
- Which defaults should be preferred?
- What limitations should Anti-Gravity avoid tripping over?

---

## RUNTIME FILE TARGET SHAPE

When you write the actual `contexts/stack-context.md`, keep it in this shape:

1. Runtime Summary
2. Current Stack Reality
3. Stack Summary
4. Defaults And Constraints
5. Key Libraries And Integrations
6. Maintenance Notes

---

## FINAL RULE

The runtime `stack-context.md` should tell Anti-Gravity how to be right in this stack, not teach a whole class on technology choice.
