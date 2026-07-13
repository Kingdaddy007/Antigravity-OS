---
status: template
scope: project
project_id: null
updated_at: null
owner: null
confidence: unset
---

# API CONVENTIONS

**Version:** Gold v1.2 (Master Merge)
**Layer:** 6 — Context (Ground Truth)
**Tier:** 2 — Loaded by task
**File:** contexts/api-conventions.md
**Purpose:** Defines how APIs are designed, structured, versioned, and consumed in this project. Anti-Gravity uses this to generate API code and contract designs that match established patterns, stay consumer-oriented, and avoid premature protocol lock-in.
**Loaded When:** Building API endpoints, integrating with external APIs, designing data contracts, reviewing API code, or any task involving request/response handling.
**Maintenance:** Update when API patterns change, new endpoint conventions are adopted, authentication approach changes, or versioning strategy evolves. Review quarterly.

---

## HOW ANTI-GRAVITY USES THIS FILE

APIs are long-lived contracts. Once published, they are hard to change. This file governs how Anti-Gravity generates and evaluates all API-related work in this project — both contract design and implementation.

Good API conventions reduce:

- consumer confusion
- accidental breakage
- inconsistency across teams or services
- hidden coupling to internals
- integration friction

The goal is not endless flexibility or stylistic novelty. The goal is predictable contracts, clear semantics, stable patterns, useful errors, safe evolution, and consumer-friendly design.

**When loaded**, Anti-Gravity will:

- Generate API endpoints following YOUR URL structure and HTTP method conventions
- Format responses using YOUR exact response shape
- Handle authentication using YOUR token/session approach
- Apply YOUR versioning strategy to new endpoints
- Include YOUR standard error codes and HTTP status code mapping
- Enforce YOUR rate limiting and pagination conventions
- Respect what is still undecided at the protocol level

**When missing or incomplete**, Anti-Gravity will:

- Generate responses inconsistent with your existing endpoints
- Use generic error shapes that don't match your client-side handling
- Miss your authentication patterns
- Apply inconsistent URL naming conventions

**When stale**, Anti-Gravity will:

- Generate endpoints using deprecated patterns
- Miss conventions adopted since the last update
- Reference old authentication approaches

---

## CURRENT PROJECT POSITION

Anti-Gravity Gold has **not yet** locked a final runtime API surface.

The project does **not** yet officially commit to:

- REST as the definitive external contract style
- GraphQL as the definitive external contract style
- gRPC as the definitive internal service contract style
- event-driven interfaces as the definitive integration mechanism
- exact transport-level status mapping
- exact endpoint/resource naming scheme
- exact SDK generation model

### What this means for Anti-Gravity

API-related work at this stage should focus on:

- consumer-oriented contract design
- explicit request/response structure
- clear error modeling
- compatibility-aware evolution
- auth/authz clarity where relevant

Do not pretend the final transport or protocol choice is already settled. If a protocol assumption is being made, state it explicitly.

---

## SAFE ASSUMPTIONS RIGHT NOW

The following assumptions are safe at this stage:

| # | Assumption |
| --- | --- |
| 1 | Contracts should be designed for consumer tasks, not storage shape |
| 2 | Request and response shape should be explicit and intentional |
| 3 | Additive evolution is preferred before any breaking change |
| 4 | Errors should be distinguishable where consumer behavior differs |
| 5 | Authorization assumptions should be explicit at the contract boundary |
| 6 | Consumer clarity is more important than implementation convenience |

## WHAT IS NOT SAFE TO ASSUME YET

Do not silently assume any of the following unless a later context file explicitly locks them:

- REST-first architecture as already chosen
- GraphQL-first architecture as already chosen
- gRPC-first internal topology as already chosen
- Event-first integration as already chosen
- Exact HTTP status conventions as already fixed
- Exact resource naming scheme as already fixed
- Public/private API segmentation model as already fixed
- Field-selection, pagination, or filtering style as already fixed

---

## API ARCHITECTURE

### Our API Approach

| API Type | Technology | Usage | When to Use |
| --- | --- | --- | --- |
| [type 1] | [technology] | [usage] | [when] |
| [type 2] | [technology] | [usage] | [when] |

### Main API Consumers

- [consumer 1]
- [consumer 2]
- [consumer 3]

Examples:

- frontend web app
- mobile app
- internal services
- admin tools
- third-party integrations

---

## URL CONVENTIONS

### Base Path

- Internal API routes: [define your base path]
- External/versioned API: [define if applicable]

### URL Structure Rules

| Rule | Example | Counter-Example |
| --- | --- | --- |
| Resources are plural nouns | `/api/projects` | `/api/project` |
| Resource IDs in path | `/api/projects/:projectId` | `/api/projects?id=123` |
| Nested resources for clear ownership | `/api/projects/:id/tasks` | [your counter-example] |
| Actions as POST with verb | `/api/tasks/:id/archive` | `/api/archiveTask/:id` |
| No trailing slashes | `/api/projects` | `/api/projects/` |
| Lowercase kebab-case | `/api/project-memberships` | `/api/projectMemberships` |
| IDs are UUIDs | `/api/projects/550e8400-...` | `/api/projects/123` |

### URL Hierarchy

```text
/api/
├── projects/
│   ├── GET        → List projects (for current user)
│   ├── POST       → Create project
│   └── :projectId/
│       ├── GET    → Get project details
│       ├── PATCH  → Update project
│       ├── DELETE → Soft-delete project
│       ├── tasks/
│       │   ├── GET  → List tasks in project
│       │   └── POST → Create task in project
│       ├── sprints/
│       │   ├── GET  → List sprints in project
│       │   └── POST → Create sprint
│       └── members/
│           ├── GET    → List project members
│           ├── POST   → Add member
│           └── :memberId/
│               ├── PATCH  → Update member role
│               └── DELETE → Remove member
├── tasks/
│   └── :taskId/
│       ├── GET    → Get task details
│       ├── PATCH  → Update task
│       ├── DELETE → Soft-delete task
│       ├── archive   → POST → Archive task
│       └── comments/
│           ├── GET  → List comments on task
│           └── POST → Add comment
└── users/
    └── me/
        ├── GET   → Get current user profile
        └── PATCH → Update current user profile
```

### Naming Rules (URLs)

- [rule 1]
- [rule 2]
- [rule 3]

### Naming Patterns To Avoid (URLs)

- mixed singular/plural usage
- database-style names in public contracts
- verb-heavy REST routes unless action-specific
- exposing storage implementation details in names

---

## HTTP METHOD USAGE

| Method | Usage | Idempotent | Request Body | Success Code |
| --- | --- | --- | --- | --- |
| GET | Read resource(s). Never modifies data. | Yes | None | 200 |
| POST | Create new resource or trigger action. | No | JSON body | 201 or 200 |
| PATCH | Partial update. Send only changed fields. | Yes | JSON body | 200 |
| PUT | Full replacement. Prefer PATCH. | Yes | JSON body | 200 |
| DELETE | Remove resource. Soft-delete preferred. | Yes | None | 204 or 200 |

### Method Rules

- GET requests must NEVER modify data
- POST is not idempotent — clients should not retry blindly
- PATCH over PUT — partial updates are simpler and safer
- DELETE is idempotent — deleting already-deleted resource returns 204

---

## REQUEST CONVENTIONS

### Content Type

- All request bodies: `Content-Type: application/json`
- File uploads: `Content-Type: multipart/form-data`

### Authentication

- [describe your authentication approach]
- See `security-baselines.md` for full auth conventions

### Query Parameters (GET requests)

| Parameter | Format | Example | Default |
| --- | --- | --- | --- |
| Pagination — page | `?page=1` | `?page=2` | `1` |
| Pagination — limit | `?limit=20` | `?limit=50` | `20` (max: `100`) |
| Sorting — field | `?sort=created_at` | `?sort=priority` | Resource default |
| Sorting — direction | `?order=desc` | `?order=asc` | `desc` |
| Filtering | `?status=active` | `?status=in_progress` | No filter |
| Search | `?q=search+term` | `?q=bug` | No search |

### Request Body Validation

- [describe your validation approach and library]
- Validation happens FIRST — before business logic or database access
- Invalid requests receive 400 with field-level error details

---

## RESPONSE CONVENTIONS

### Success Responses

#### Single Resource

```json
{
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "fieldName": "value",
    "createdAt": "2024-03-15T10:30:00Z",
    "updatedAt": "2024-03-15T14:22:00Z"
  }
}
```

#### Collection (Paginated)

```json
{
  "data": [
    { "id": "...", "fieldName": "value" },
    { "id": "...", "fieldName": "value" }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 145,
    "totalPages": 8,
    "hasNextPage": true,
    "hasPreviousPage": false
  }
}
```

#### Mutation Success

```json
{
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000"
  },
  "message": "Resource created successfully"
}
```

#### Deletion Success

```http
HTTP 204 No Content
(empty body)
```

### Response Shape Rules

- All successful responses wrap the resource in a `"data"` envelope
- Collections always include `"pagination"` metadata
- Mutation successes include optional `"message"` for user-facing feedback
- Dates are ISO 8601 format with timezone
- IDs are UUIDs as strings
- Null fields are included in the response — not omitted
- camelCase field names in JSON

---

## ERROR CONVENTIONS

### Error Response Shape

#### Validation Error (400)

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid data",
    "details": [
      { "field": "title", "message": "Title is required" }
    ]
  }
}
```

#### Authentication Error (401)

```json
{
  "error": {
    "code": "UNAUTHORIZED",
    "message": "Authentication required"
  }
}
```

#### Authorization Error (403)

```json
{
  "error": {
    "code": "FORBIDDEN",
    "message": "You do not have permission to perform this action"
  }
}
```

#### Not Found (404)

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Resource not found"
  }
}
```

#### Conflict (409)

```json
{
  "error": {
    "code": "CONFLICT",
    "message": "A resource with this identifier already exists"
  }
}
```

#### Business Logic Error (422)

```json
{
  "error": {
    "code": "BUSINESS_RULE_VIOLATION",
    "message": "This action violates a domain rule"
  }
}
```

#### Rate Limited (429)

```json
{
  "error": {
    "code": "RATE_LIMITED",
    "message": "Too many requests. Please try again later."
  }
}
```

#### Internal Error (500)

```json
{
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "An unexpected error occurred. Please try again."
  }
}
```

### HTTP Status Code Reference

| Code | Meaning | When to Use |
| --- | --- | --- |
| 200 | OK | Successful read, update, or action |
| 201 | Created | Successful resource creation |
| 204 | No Content | Successful deletion |
| 400 | Bad Request | Malformed request, validation error |
| 401 | Unauthorized | No valid authentication credentials |
| 403 | Forbidden | Authenticated but not authorized |
| 404 | Not Found | Resource genuinely does not exist |
| 409 | Conflict | Duplicate resource, version conflict |
| 422 | Unprocessable Entity | Business logic violation |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Unexpected server failure |

### Status Code Rules

- **401 vs 403:** 401 = not authenticated. 403 = authenticated but not authorized.
- **404 vs 403:** Use 404 only when the resource genuinely does not exist. If the user lacks permission, use 403 — do not pretend it does not exist.
- **422 vs 400:** 400 = structurally invalid request. 422 = valid request that violates business rules.
- **Never expose** stack traces, SQL errors, or internal details in 500 responses.

### Error Design Rules

- [rule 1]
- [rule 2]
- [rule 3]

---

## AUTH AND AUTHORIZATION CONVENTIONS

### Authentication Style

[Example: bearer token / session cookie / API key / provider token]

### Auth Expectations

- Auth check is ALWAYS the first operation — fail fast
- Authorization check follows immediately after authentication
- [expectation 3]

### Authorization Expectations

- Sensitive or scoped actions should not rely on implied access behavior
- Make explicit: who may call something, what resources they may see, what actions they may perform
- [expectation 3]

### Sensitive Endpoint Rules

- [rule 1]
- [rule 2]
- Webhook endpoints use their own auth (signature verification)
- Public endpoints must be explicitly marked — default is authenticated

---

## PAGINATION / FILTERING / SORTING

### Pagination Style

[Example: cursor-based / offset-based / page + size]

### Pagination Rules

| Rule | Value |
| --- | --- |
| Default page size | 20 |
| Maximum page size | 100 |
| Minimum page size | 1 |
| Page numbering | 1-based (not 0-based) |
| Out-of-range pages | Return empty data array with correct metadata |
| Sorting default | Resource-specific (usually `createdAt desc`) |

### Filtering Conventions

- [rule 1]
- [rule 2]

### Sorting Conventions

- [rule 1]
- [rule 2]

---

## VERSIONING

### Versioning Strategy

[Example: /v1/ URL versioning / header-based / none yet but planned]

### Backward Compatibility Expectations

- Never remove a field in an active version — only add new optional fields
- Never rename a field — add new field with new name, keep old
- Never change a field's type — add new field, deprecate old
- [expectation 4]

### Breaking Change Policy

- Additive changes are preferred before version bumps
- Breaking changes require explicit migration strategy
- [policy 3]

### Deprecation Expectations

- Minimum notice period before removing a version: [define]
- Deprecation communication method: [define]
- Maximum active versions at once: [define]

---

## PROTECTION AND OPERATIONAL RULES

### Rate Limiting Expectations

- [rule 1]
- [rule 2]
- [rule 3]

### Request Size and Abuse Guardrails

- [rule 1]
- [rule 2]

### Observability and Traceability Expectations

- Include requestId in error responses
- Log auth failures
- Monitor deprecated endpoint usage
- [expectation 4]

---

## FILE UPLOADS

| Setting | Value |
| --- | --- |
| Upload method | [presigned URL / direct / multipart] |
| Max file size | [define] |
| Allowed types | [define] |
| Type validation | [define] |
| Storage | [define] |
| Access | [define] |

---

## WEBHOOK CONVENTIONS

### Incoming Webhooks

| Source | Endpoint | Auth Method | Handler Location |
| --- | --- | --- | --- |
| [source] | [endpoint] | [auth method] | [location] |

### Incoming Webhook Rules

- Verify webhook signature BEFORE processing
- Return 200 immediately, process async if heavy
- Idempotent processing — use event ID to prevent duplicates
- Log all webhook events

### Outgoing Webhooks

[Status: implemented / not yet implemented / planned]

---

## LONG-RUNNING OPERATIONS

### Pattern (Async)

[Describe your async job or polling approach]

### Long-Running Operation Rules

- Operations expected to take >[threshold] seconds must be async
- [rule 2]
- [rule 3]

---

## API DOCUMENTATION

| Setting | Value |
| --- | --- |
| Documentation approach | [define] |
| Planned approach | [define] |
| Current documentation | [define] |
| Update rule | [define] |

---

## API RISKS TO WATCH

| Risk | Description |
| --- | --- |
| Storage-leak contracts | Shaping APIs around tables or internal structures rather than consumer tasks |
| Silent breaking change | Treating field changes or removals as if contracts were purely internal |
| Generic error collapse | Treating all failures as one vague response class |
| Hidden auth assumptions | Leaving access rules implicit for consumers to discover through failure |
| Protocol certainty without decision | Designing as if a transport choice is finalized when it is not |

---

## API ANTI-PATTERNS

### Storage-leak contracts

**What it looks like:** Exposing internal schema or storage layout directly as interface shape.
**Why it is harmful:** Contract becomes tied to implementation detail and may be awkward for real consumers.
**What to do instead:** Design around the consumer's task and domain meaning.

### Silent breaking change (Anti-Pattern)

**What it looks like:** Renaming, removing, or reinterpreting fields as if contracts are internal details.
**Why it is harmful:** Clients break or drift silently, and trust in the contract weakens.
**What to do instead:** Preserve additive evolution thinking unless a deliberate breaking change is explicitly planned.

### Generic error collapse (Anti-Pattern)

**What it looks like:** Treating all failures as one vague response class even when consumers need to react differently.
**Why it is harmful:** Client behavior becomes brittle or under-informed.
**What to do instead:** Keep meaningful failure distinctions visible where they affect behavior.

### Hidden auth assumptions (Anti-Pattern)

**What it looks like:** Leaving access rules implicit and expecting consumers to discover them through failure.
**Why it is harmful:** Protected operations become harder to reason about and easier to misuse.
**What to do instead:** Make auth/authz expectations explicit where relevant.

### Protocol certainty without decision (Anti-Pattern)

**What it looks like:** Designing downstream work as if a transport choice is finalized when it has not been.
**Why it is harmful:** The project acquires accidental lock-in and constraint leakage.
**What to do instead:** State protocol assumptions explicitly until a formal decision exists.

---

## ANTI-GRAVITY GUIDANCE (API Work)

When designing or reviewing APIs in this project, Anti-Gravity should:

- Follow the local API style consistently
- Preserve contract clarity and predictability
- Match the project's response and error conventions
- Respect versioning and compatibility expectations
- Treat endpoint naming and request/response shape as part of consistency, not personal taste
- Surface protocol and transport assumptions explicitly instead of hiding them inside design examples
- Ask who is using this contract, what they are trying to accomplish, and what shape makes that task easier

Anti-Gravity should avoid:

- Introducing inconsistent endpoint naming
- Leaking internal implementation models into the API without reason
- Inventing new response or error shapes casually
- Suggesting API designs that conflict with current project conventions
- Pretending the final transport/protocol decision is already complete

---

## OPEN API QUESTIONS

- [question 1]
- [question 2]
- [question 3]

These are areas where API conventions are still evolving.

---

## CROSS-REFERENCES

| Related File | Relationship |
| --- | --- |
| `stack-context.md` | Framework and runtime for API routes |
| `architecture-context.md` | Data flow through API layer |
| `coding-standards.md` | Error handling patterns, TypeScript conventions |
| `security-baselines.md` | Authentication, authorization, input validation, CORS |
| `database-context.md` | Query patterns, pagination queries, data access |
| `domain-rules.md` | Business logic rules enforced in API responses |
| `infra-context.md` | Rate limiting infrastructure, monitoring |
| `skills/skill-api-design.md` | API design skill layer |

---

## FINAL RULE

A technically valid API that violates local contract conventions still increases integration cost and inconsistency — so it is not the right API for this project.

A more sophisticated protocol is not automatically better if it makes the contract harder to understand, evolve, or support for the actual consumer.
