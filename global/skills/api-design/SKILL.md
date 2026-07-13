---
name: api-design
description: 'Use this skill when designing, creating, or modifying API endpoints; defining contracts between services; evaluating protocol choices (REST, GraphQL, gRPC, WebSockets); versioning or deprecating an API; designing error responses or pagination; or reviewing an existing API for consistency, security, or ergonomics. Signal phrases: "design the API", "create an endpoint", "REST", "GraphQL", "gRPC", "API versioning", "backward compatible", "breaking change", "error response", "pagination", "rate limiting", "API contract", "OpenAPI", "Protobuf", "webhook", "idempotency", "deprecation", "endpoint structure".'
---

# API DESIGN & CONTRACT ENGINEERING

## WHEN TO USE THIS

- Designing, creating, or modifying API endpoints
- Defining contracts between services (internal or external)
- Evaluating API protocol choices (REST, GraphQL, gRPC, WebSockets)
- Versioning an existing API or planning a version migration
- Designing error response formats and status code usage
- Implementing pagination, filtering, sorting, or search on collection endpoints
- Reviewing existing APIs for consistency, ergonomics, or security
- Designing webhook or event notification systems

## NEVER DO

- Shape an API contract around implementation convenience or database structure
- Remove, rename, or change the type of an existing field in an active API version
- Introduce breaking changes to active versions without a new version and migration plan
- Return unbounded collection results — all collection endpoints must be paginated
- Expose internal details in error responses (stack traces, SQL errors, internal IDs, exceptions)
- Deploy an API without versioning from day one
- Leave rate limiting, authentication, or input validation as optional enhancements

---

## MINDSET

You are not an endpoint generator. You are a contract architect who designs binding agreements between systems that must remain stable long after you have moved on.

An API is a commitment. Once published and integrated by consumers — whether those are frontend clients, mobile apps, third-party developers, or internal microservices — it cannot be easily revoked, renamed, or restructured without breaking those consumers. Every field you expose, every endpoint you create, every error format you define becomes a contract that someone will depend on.

**A poor API exports internal mess forever. A strong API protects consumers from internal churn.**

The expert API designer:

- **Views an API as a long-term public interface** — not a thin wrapper around the database or internal models
- **Designs contracts first** — the specification is the source of truth, and implementation derives from it, not the other way around
- **Treats backward compatibility as law** — once a version is active, existing consumers must never be broken
- **Separates the internal data model from the external API representation** — internal schema changes should never force API consumers to change
- **Designs for the consumer's needs, not the server's convenience** — the API speaks the consumer's language, not the database's column names
- **Treats error responses as first-class features** — every error must tell the consumer what went wrong, why, and what they can do about it
- **Implements protection mechanisms by default** — pagination, rate limiting, payload size limits, and authentication are not afterthoughts
- **Applies Postel's Law**: be conservative in what you send, be liberal in what you accept — within the bounds of security and data integrity
- **Designs for the developer integrating at 2 AM with only the documentation** — if the API is confusing, it has failed regardless of how elegant the implementation is

---

## DECISION FRAMEWORK — 8 PRIORITIES (IN ORDER)

### Priority 1 — Contract

Stability

Never remove, rename, or change the type of an existing field in an active version. Only add new, optional fields. If a breaking change is truly necessary, introduce it in a new API version and maintain the old version until consumers have migrated. Backward compatibility is not a preference — it is a law once active consumers exist.

### Priority 2 — Consumer

Experience

Design resources, naming, and workflows around the consumer's mental model. Use clear, predictable naming. Provide comprehensive documentation with examples. Error messages should tell the consumer exactly what went wrong and how to fix it. If the API requires a phone call to integrate, it has failed.

### Priority 3 — Boundary

Quality

Keep the external contract stable even if the internal model changes. The API should speak domain language — not database column names, internal status flags, or service-layer concepts that consumers have no business knowing about.

### Priority 4 — Security

and Protection

Every endpoint must have explicit authentication and authorization. All input must be validated and sanitized. Rate limiting must be applied. Sensitive data must never appear in URLs or logs. The principle of least privilege governs what each consumer role can access.

### Priority 5 — Backend

Protection

All collection endpoints must be paginated with enforced maximum page sizes. Rate limiting must prevent request flooding. Payload size limits must be enforced. Timeouts must be configured. The API must protect the database and infrastructure from consumer abuse — whether intentional or accidental.

### Priority 6 — Protocol

Fit

| Protocol | Best For | Tradeoffs |
| --- | --- | --- |
| **REST** | Public APIs, web integrations, broad compatibility, cacheability | Over-fetching, multiple round trips for related data, no built-in real-time |
| **GraphQL** | Complex frontend data needs, flexible queries, reducing over-fetching | N+1 backend query risk, caching complexity, steep learning curve for consumers |
| **gRPC** | Internal service-to-service, low-latency high-throughput, strong typing | Not browser-native, debugging complexity, less human-readable |
| **WebSockets** | Real-time bidirectional communication, live updates, collaboration | Connection management overhead, scaling complexity, no built-in request/response semantics |

Do not choose a protocol because it is trendy — choose it because the consumer's needs demand it.

### Priority 7 — Evolvability

Design resources broadly enough to accommodate anticipated extensions, but do not expose speculative fields. Prefer additive changes (new optional fields, new endpoints) over modifications to existing contracts. Design the API so that the most common future changes are non-breaking by default.

### Priority 8 — Operational

Fit

Include requestId correlation in every response. Ensure errors are observable and loggable server-side without leaking internal details to consumers. Ensure rate limit state and deprecation usage are monitorable.

**Core Rule:** Design the API contract for the consumer and the future — not for the current server implementation. Internal convenience is never a justification for consumer instability.

---

## CORE PRINCIPLES

1. **Contract First.** The API specification (OpenAPI, Protobuf, GraphQL schema) is the single source of truth. Code derives from the spec — not the other way around. If the spec and the implementation disagree, the spec is authoritative and the implementation is a bug.
2. **Backward Compatibility Is Law.** Once an API version is published and consumers depend on it, the contract is binding. Never remove fields, rename fields, change field types, or alter semantic behavior in an active version. Only add new, optional fields. Breaking changes require a new version.
3. **Internal Models Are Not the API.** The database schema, internal object model, and domain implementation are not the API contract. Internal refactoring should never force API consumers to change.
4. **Design for the Consumer.** Resource names, field names, and workflows should reflect how the consumer thinks about the domain — not how the database stores it or how the code processes it.
5. **Errors Are Features.** Every error response must include: an appropriate HTTP status code, a machine-readable error identifier (for programmatic handling), a human-readable message (for debugging), and actionable guidance (what the consumer can do to resolve it).
6. **Protect by Default.** Pagination, rate limiting, payload limits, authentication, and input validation are not optional enhancements — they are baseline requirements for every API.
7. **Version from Day One.** Implement versioning before the first consumer integrates. Retrofitting versioning onto an unversioned API is painful, disruptive, and avoidable.
8. **Be Conservative in What You Send, Liberal in What You Accept.** (Postel's Law) Send responses with strict, predictable structure. Accept requests tolerantly where doing so does not compromise security or data integrity.
9. **Deprecate Gracefully.** When sunsetting an API version or endpoint: announce with ample lead time, provide comprehensive migration documentation, maintain the deprecated version for a defined transition period, monitor usage to identify consumers who have not yet migrated.
10. **Document as If You Will Not Be Available.** The API documentation should be comprehensive enough that a consumer can integrate successfully at 2 AM without being able to contact anyone on the API team.
11. **Consistency Reduces Cognitive Load.** Naming, error shapes, pagination conventions, date formats, and status code semantics must be uniform. Inconsistency forces consumers to re-learn the API for every endpoint.
12. **Evolution Should Be Planned, Not Improvised.** Deprecation, migration, and additive extension should be thought through before consumers are forced to react.

---
## REFERENCE LOADING RULES

Load `references/extended-guidance.md` when the task needs detailed implementation rules, examples, edge cases, diagnostics, or verification beyond the core workflow above. Inspect its Contents first and load only the matching sections.

## OUTPUT SHAPE

Deliver the requested artifact or decision, the key rationale and tradeoffs, and a concise verification checklist.

## NON-NEGOTIABLE CHECKLIST

1. Apply the core workflow above.
2. Load matching extended guidance for substantive or high-risk work.
3. Preserve user constraints and verify the result before delivery.