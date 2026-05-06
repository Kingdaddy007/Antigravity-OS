---
name: API DESIGN & CONTRACT ENGINEERING
description: >
  Use this skill when designing, creating, or modifying API endpoints; defining
  contracts between services; evaluating protocol choices (REST, GraphQL, gRPC,
  WebSockets); versioning or deprecating an API; designing error responses or
  pagination; or reviewing an existing API for consistency, security, or
  ergonomics. Signal phrases: "design the API", "create an endpoint", "REST",
  "GraphQL", "gRPC", "API versioning", "backward compatible", "breaking change",
  "error response", "pagination", "rate limiting", "API contract", "OpenAPI",
  "Protobuf", "webhook", "idempotency", "deprecation", "endpoint structure".
  Also activate when API responses expose database column names, collection
  endpoints return unbounded results, or breaking changes are being introduced
  to active versions without a migration plan. Do NOT shape the API contract
  around implementation convenience — design for the consumer and the future.
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

## API DESIGN LENSES

| Lens | What to Inspect |
| --- | --- |
| **Resource** | Core resources exposed? Named consistently as plural nouns (`/users`, not `/getUser`)? Reflect consumer's mental model? Appropriately granular? Nested resources used correctly (≤2 levels deep)? |
| **Contract** | Explicitly defined in a specification (OpenAPI, Protobuf, GraphQL schema)? Every field documented with type, constraints, optionality? Are internals leaking (database IDs, internal status codes, model names)? |
| **Versioning** | Is the API versioned? What strategy (URL path, header)? Is the current version backward-compatible with its initial release? Deprecation policy with sunset dates? Can multiple versions run simultaneously during migration? |
| **Error** | Every endpoint has documented error responses for common failure cases? Consistent error format across all endpoints? Every error includes: HTTP status code, machine-readable error code, human-readable message, remediation guidance? No internal details exposed? requestId in every response? |
| **Protection** | All collection endpoints paginated with enforced max page sizes? Rate limiting applied with rate limit headers? Request payload size limits enforced? Authentication required on all non-public endpoints? Authorization verifies specific resource permission? |
| **Idempotency** | Unsafe operations (POST, PUT, DELETE) designed to be safely retryable? Idempotency keys supported for creation operations? Retry behavior documented for consumers? |
| **Payload** | Response payloads appropriately sized? Date/time in ISO 8601 with timezone? Consistent identifier types (UUIDs or integers — not mixed)? Null field handling consistent? |
| **Discovery** | Can a new consumer understand the API from documentation alone? All endpoints, parameters, request bodies, and responses documented? Example requests and responses for every endpoint including error cases? |
| **Evolution** | If a new requirement arrives next month, can it be met with an additive (non-breaking) change? Clear taxonomy of breaking vs non-breaking changes? Breaking: field removal, rename, type change, semantic behavior change, new required fields. Non-breaking: new optional fields, new endpoints, new optional parameters. |
| **Integration** | How will consumers actually use this API? Multi-step operations that should be atomic? Batch operations needed? Webhook patterns needed for async updates? |

---

## BEHAVIORAL WORKFLOW

### Phase 1 — Understand

Identify who the consumers of this API are (frontend app, mobile app, third-party developers, internal services). Understand what operations the consumers need to perform and what data they need. Determine the communication pattern: synchronous request/response, asynchronous events, real-time streaming. Identify authentication and authorization requirements. Determine: new API, modification to an existing API, or version migration?

### Phase 2 — Contextualize

Check if existing API conventions exist in the project (naming, versioning, error formats, pagination style). Identify the current API specification format. Understand the deployment model — can multiple API versions run simultaneously? Identify existing consumers and their integration constraints. Determine the data model that underlies the API resources — but do NOT assume the API should mirror it. Identify compatibility obligations and exposure level (public, partner, internal).

### Phase 3 — Analyze

*For New API Design:*

1. Identify the core resources or operations.
2. Evaluate protocol fit using the decision framework (Priority 6).
3. Define request/response shape.
4. Design the error model.
5. Design pagination, filtering, and limits for collection endpoints.
6. Define authentication and authorization behavior per endpoint.
7. Define idempotency behavior for mutating operations.
8. Define how the contract will evolve — what future changes are anticipated, and are they non-breaking by design?

*For API Modification:*

1. Identify all current consumers of the affected endpoints.
2. Classify the change:
   - **Additive** — new optional field, new endpoint, new optional parameter (non-breaking)
   - **Behavioral** — same structure, different semantics (breaking)
   - **Structural** — field removed, renamed, or type-changed (breaking)
   - **Deprecating** — endpoint or version being sunset (requires migration strategy)
3. Evaluate compatibility impact.
4. If breaking: plan a new version with migration guide and transition timeline.
5. If additive: preserve existing consumer behavior explicitly and update the spec first.

*For API Review:*

1. Inspect consistency — naming, error shape, pagination, date formats.
2. Inspect contract leakage — are internals exposed?
3. Inspect error design — are errors specific, actionable, consistent?
4. Inspect protection — pagination, rate limiting, auth, authorization, payload limits.
5. Inspect idempotency — are mutating operations safely retryable?
6. Inspect documentation gaps — is the spec complete and accurate?

### Phase 4 — Plan

Define the complete API specification (endpoints, methods, request/response schemas, error codes). Define the URL structure and naming conventions. Define the authentication and authorization model. Define the pagination, filtering, and sorting conventions. Define the error response format. Define idempotency strategy for mutating operations. Define rate limiting rules.

### Phase 5A — Resource and URL Design

1. Use plural nouns for resource collections: `/users`, `/orders`, `/products`.
2. Use resource IDs for specific items: `/users/{userId}`, `/orders/{orderId}`.
3. Use nesting for clear ownership relationships: `/users/{userId}/orders`.
4. Limit nesting depth to 2 levels — deeper nesting creates rigid, brittle URLs.
5. Use HTTP methods semantically:
   - `GET` — read (safe, idempotent, cacheable)
   - `POST` — create (not idempotent without idempotency key)
   - `PUT` — full replace (idempotent)
   - `PATCH` — partial update (document idempotency behavior explicitly)
   - `DELETE` — remove (idempotent)
6. For actions that do not map to CRUD: use sub-resource verbs — `POST /orders/{id}/cancel`.

### Phase 5B — Request and Response Design

```json
{
  "data": { ... },
  "meta": { "page": 1, "pageSize": 20, "totalCount": 142 }
}
```

- Consistent field naming (camelCase or snake_case — pick one, apply everywhere)
- ISO 8601 for all date/time values with timezone: `"2024-01-15T14:30:00Z"`
- Consistent identifier types (string UUIDs or integer IDs — not mixed)
- Include only fields the consumer needs — do not dump the entire internal model
- Creation: return the created resource with its server-generated ID and `201 Created`
- Update: return the updated resource with `200 OK`
- Deletion: return `204 No Content` (be consistent)
- Accepted async operations: return `202 Accepted` with a status/polling URL

### Phase 5C — Error Response Design

```json
{
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "The request body contains invalid fields.",
    "details": [
      { "field": "email", "issue": "Must be a valid email address.", "received": "not-an-email" }
    ],
    "requestId": "req_abc123"
  }
}
```

HTTP status code semantics:

| Code | When |
| --- | --- |
| `400` | Client sent an invalid request (validation errors, malformed JSON) |
| `401` | Not authenticated (missing or invalid credentials) |
| `403` | Authenticated but not authorized for this resource |
| `404` | Resource does not exist |
| `409` | Conflict (duplicate creation, concurrent modification) |
| `422` | Semantically invalid (well-formed but business rules prevent processing) |
| `429` | Rate limited |
| `500` | Server error (never expose internal details — log them server-side) |

- Never expose stack traces, SQL errors, or internal exception details
- Include a requestId in every response
- For validation errors, identify the specific field and the specific constraint that failed

### Phase 5D — Pagination Design

- All collection endpoints must be paginated — unbounded result sets are a denial-of-service vector
- Enforce a maximum page size (e.g., max 100 items) — never allow unlimited results

| Strategy | Use When |
| --- | --- |
| **Offset-based** (`?page=3&pageSize=20`) | Simple use cases; allows jumping to arbitrary pages; slow for large datasets; subject to drift with concurrent inserts/deletes |
| **Cursor-based** (`?cursor=eyJ...&limit=20`) | Large datasets; stable under concurrent mutations; no random page access |

Include pagination metadata in responses: current page/cursor, page size, total count (if feasible), next/previous links.

### Phase 5E — Versioning and Deprecation

- Version from the first release — do not wait for a breaking change
- Preferred: URL path versioning (`/v1/users`, `/v2/users`) — most explicit, easiest for consumers to understand
- Increment the version number only for breaking changes — additive changes do not require a new version

Deprecation lifecycle:

1. **Announce** — publish notice in docs, changelog, and `Deprecation`/`Sunset` response headers
2. **Transition period** — both versions run simultaneously; consumers migrate
3. **Monitor** — track usage on deprecated version to identify unmigrated consumers
4. **Remind** — re-communicate sunset date as it approaches
5. **Remove** — decommission only after usage has reached zero or an agreed-upon threshold

### Phase 5F — Rate Limiting

- Apply rate limiting to all endpoints — not just public-facing ones
- Return rate limit information in response headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`
- Return `429 Too Many Requests` with a `Retry-After` header when the limit is exceeded
- Rate limit by authenticated identity — not just by IP address (IPs are shared, spoofable, and unreliable)

### Phase 5G — Documentation

- Maintain the API specification (OpenAPI/Swagger, GraphQL schema, Protobuf) as the source of truth
- For every endpoint: description, authentication requirements, all parameters (path/query/header/body) with types and constraints, example request, response schema, example responses (success and error cases)
- Include a getting-started guide with authentication setup and first-request walkthrough
- Include an error code catalog with every error code, its meaning, and recommended consumer action
- Include a changelog documenting all changes across versions

### Phase 6 — Verify

- Every endpoint matches its specification exactly (contract testing)
- Backward compatibility verified — existing consumer requests still produce correct responses
- Error responses follow the consistent format for every failure case
- Pagination works correctly (boundary cases: empty results, last page, single item)
- Rate limiting triggers correctly and returns appropriate headers
- Authentication and authorization enforced on every non-public endpoint
- No internal implementation details leak into responses
- Idempotency behavior — duplicate requests with the same idempotency key produce the same result
- requestId is present and unique in every response

### Phase 7 — Critique

Does the API expose the right abstraction, or is it leaking internal structure? Are there endpoints that exist only because the database has a table — not because a consumer needs the resource? Is naming consistent across all endpoints? Are error responses specific enough to debug integration issues without contacting the API team? Is pagination implemented on ALL collection endpoints? Is the API versioned? Would a new developer on the consumer side be able to integrate using only the documentation?

### Phase 8 — Communicate

Provide the complete API specification. Document all design decisions and their rationale. Document the error code catalog. Document the pagination, rate limiting, and authentication conventions. If modifying: document backward-compatibility impact analysis. If new version: provide the migration guide from the previous version.

### Pre-Finalization Re-Check

- The consumer and use case are clear
- The contract is coherent, stable, and does not expose internals
- Auth, error behavior, idempotency, and protection are explicit
- Scaling and collection constraints were considered
- Compatibility and evolution implications are understood
- Documentation is complete and accurate

---

## KEY DIAGNOSTIC QUESTIONS

### Before Designing

- Who are the consumers? What are their technical capabilities and constraints?
- Is this a public, partner, or internal contract? (This affects versioning strategy, documentation depth, and backward-compatibility strictness.)
- What operations do consumers need to perform? What data do they need?
- Are there existing API conventions in this project that must be followed?

### During Design

- Does this contract expose domain resources — or does it expose database tables?
- If I change the internal database schema, will this API contract break? (It should not.)
- Can a consumer predict how a new endpoint would look based on existing endpoints?
- Is every error case documented with a specific, actionable error response?
- What happens if a consumer sends a request with 1,000,000 items? (Protection check)
- Is this endpoint idempotent? What happens if the consumer retries?

### Before Modifying

- Which existing consumers could break?
- Is this change additive or breaking? (Field removal/rename/type change/semantic change = breaking; new optional fields/endpoints = non-breaking.)
- Can this evolve without a new version? If not, what is the migration path and transition timeline?
- Have I updated the specification BEFORE modifying the implementation?

### After Design / During Review

- Can a consumer integrate from the docs alone — at 2 AM, without contacting the team?
- Can operators trace and debug failures using requestId?
- Does the API surface match real consumer workflows?
- Are deprecated endpoints monitored for usage to track migration progress?

---

## ANTI-PATTERNS

| Anti-Pattern | What It Looks Like | Why It's Harmful | Fix |
| --- | --- | --- | --- |
| **The Database Mirror API** | Endpoints directly expose database tables. `/api/user_profiles` returns columns like `created_at_utc`, `fk_organization_id`, `is_deleted_flag`. Renaming a DB column requires updating the API, which breaks consumers. | Internal data model and external API contract serve different purposes and evolve at different rates. Coupling them means every internal refactoring is a breaking API change. Consumers must understand the database schema to use the API. | Design API resources as deliberate, stable representations of domain concepts. Map between internal models and API representations explicitly. The mapping layer absorbs internal changes without affecting consumers. |
| **The Versionless API** | All endpoints are unversioned: `/api/users`. When a breaking change is needed, the team modifies existing endpoints and hopes consumers adapt quickly. | Without versioning, every breaking change is an emergency for all consumers — no migration period, no parallel operation. Consumers break without warning. | Version from day one: `/v1/users`. When a breaking change is needed, introduce `/v2/users` while maintaining `/v1/users` for a defined transition period. Provide a migration guide. Monitor `/v1` usage and communicate sunset timelines. |
| **The Generic Error** | Every error returns `{ "error": "Something went wrong" }` with a 500. Validation errors return `{ "error": "Invalid request" }` with no indication of which field failed. | Consumers cannot programmatically handle errors. Developers cannot debug integration issues. Support receives tickets impossible to diagnose without server-side log access. | Define a consistent error format: HTTP status code, machine-readable error code, human-readable message, specific field-level details for validation errors, and a requestId. |
| **The Unbounded Collection** | `GET /api/orders` returns all 2 million orders in a single response. Or the endpoint accepts `?pageSize=1000000` with no maximum. | Unbounded collections exhaust server memory, overwhelm network bandwidth, and crash consumer applications. They are also an unintentional denial-of-service vector. | Paginate all collection endpoints by default. Enforce a maximum page size. Return pagination metadata. |
| **The Leaky Abstraction** | Error responses include stack traces, SQL query text, internal class names, or server file paths. Response fields include `_internal_status`, `__debug_info`, or `db_row_version`. | Internal details are security vulnerabilities — stack traces reveal tech stack, SQL errors reveal database structure. Consumers start parsing internal fields, making internal changes into breaking changes. | Strip all internal details from API responses. Log them server-side. Return only: a specific error code, a clear message, actionable guidance, and a requestId. |
| **The Breaking "Bug Fix"** | A field is renamed from `userName` to `username` because "it was a typo." The team considers this a "bug fix" rather than a breaking change. | From the consumer's perspective, there is no difference between a breaking change and a breaking "fix." Both destroy working integrations. | Any change that breaks existing consumers requires a new version, a migration guide, and a transition period. "It should have been this way" is not a justification for breaking consumers without warning. |
| **The Consumer-Blind Design** | The API is shaped for backend convenience rather than consumer workflows. Consumers must make 5 requests to accomplish one logical task. | Integration becomes awkward, chatty, and fragile. Consumers couple tightly to implementation-shaped endpoints that change when the backend changes. | Design from the consumer's use case. What does the consumer need to accomplish? How many requests should that require? Build the API around those answers. |
| **The Style Mix** | Some endpoints are REST-style, others are RPC-style action methods (`/api/doSomething`). Some use camelCase, others snake_case. Some paginate, others do not. | Consumers cannot build consistent expectations or write generic integration code. Each endpoint must be treated as a special case. | Choose a contract style and apply it coherently across the entire API surface. Establish conventions for naming, casing, pagination, and error format and enforce them without exception. |
| **The Non-Idempotent Mutation** | `POST /api/orders` creates a new order on every call. When the consumer's network request times out and they retry, they end up with two identical orders. | Networks are unreliable. Consumers must retry. If retrying creates duplicate resources or side effects, the API forces consumers into a race condition they cannot safely resolve. | Support idempotency keys for creation operations (`Idempotency-Key: <uuid>`). The server stores the key and returns the same response for subsequent requests with the same key within a defined window. |
| **The Silent Deprecation** | An API endpoint is removed or changed without advance notice, migration documentation, or a transition period. | Consumer applications break unexpectedly. Trust is destroyed. Support costs spike as consumers scramble to identify what changed and how to fix it. | Follow the full deprecation lifecycle: announce → transition period → monitor → remind → remove. Never silently change behavior within an active version. |

---

## OUTPUT SHAPE

```markdown

## API Specification

- Endpoint: METHOD /vN/resource/{id}
- Description: what this endpoint does and when to use it
- Authentication: required / optional / none

| - Parameters: [path | query | header | body] with types, constraints, optionality |

- Request body: schema with field descriptions
- Response (success): HTTP status + response schema + example
- Response (error): documented error cases with codes and guidance

## Design Decisions

- Protocol choice: [chosen] because [consumer/workload rationale]
- Versioning strategy: [strategy] with backward-compatibility implications
- Pagination strategy: [offset/cursor] with max page size enforcement
- Idempotency: [behavior for each mutating operation]

## Backward Compatibility Impact

- What existing consumers are affected
- Classification: additive / behavioral / structural / deprecating
- Migration guide (if breaking): step-by-step consumer migration path
- Transition timeline and sunset date (if deprecating)

```

---

## NON-NEGOTIABLE CHECKLIST

### Contract Integrity

- [ ] The API specification (OpenAPI, Protobuf, GraphQL schema) exists and is the source of truth
- [ ] The implementation matches the specification exactly
- [ ] No internal model or database structure is exposed directly through the API
- [ ] Backward compatibility is preserved for all active versions
- [ ] Breaking changes exist only in new version numbers

### Consistency

- [ ] URL structure follows a consistent naming convention (plural nouns, consistent casing)
- [ ] Request and response shapes follow a consistent format across all endpoints
- [ ] Error responses use a single, consistent structure across all endpoints
- [ ] Date/time values use ISO 8601 with timezone consistently
- [ ] Field naming convention (camelCase or snake_case) is uniform throughout

### Error Handling

- [ ] Every endpoint has documented error responses for common failure cases
- [ ] Error responses include: HTTP status code, machine-readable error code, human-readable message, actionable guidance
- [ ] Validation errors identify the specific field and constraint that failed
- [ ] No internal details (stack traces, SQL errors, exceptions) exposed in error responses
- [ ] A requestId is included in every response

### Protection

- [ ] All collection endpoints paginated with enforced maximum page sizes
- [ ] Rate limiting applied and rate limit headers included in responses
- [ ] Request payload size limits enforced
- [ ] Authentication required on all non-public endpoints
- [ ] Authorization verifies the authenticated consumer has permission for the specific resource
- [ ] Input validation applied to all request parameters and body fields

### Idempotency

- [ ] Idempotency behavior defined and documented for all mutating operations
- [ ] Creation operations support idempotency keys where duplicate prevention matters
- [ ] Retry behavior is safe, documented, and predictable for the consumer

### Versioning

- [ ] The API is versioned from its first release
- [ ] The versioning strategy is consistent and documented
- [ ] Deprecated versions have announced sunset dates and migration guides
- [ ] Multiple versions can run simultaneously during migration periods
- [ ] Old version usage is monitored to track migration progress

### Documentation

- [ ] Every endpoint documented with description, parameters, request/response examples, and error cases
- [ ] Authentication setup documented end-to-end
- [ ] Error code catalog complete and up to date
- [ ] Changelog documents all changes across versions
- [ ] Documentation matches the current implementation — no stale or inaccurate content

---

**Final Rule:** An API is a contract, not a convenience. Design for the consumer who will depend on your decisions long after you have moved on. The internal model can change freely — the published contract cannot.
