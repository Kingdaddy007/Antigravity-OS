# RUBRIC: API QUALITY

**Version:** Gold v1.0
**Layer:** 10 — Evaluation
**Tier:** 3 — Loaded on demand
**File:** rubrics/api-quality-rubric.md
**Purpose:** Self-assessment matrix for evaluating API design and implementation quality — contract clarity, consistency, security, error handling, and consumer experience.
**Loaded When:** Phase 7 of any API design or implementation task. Evaluating whether an API endpoint is ready for consumers (internal or external).
**References:** skill-api-design.md, workflow-design-api.md, api-conventions.md

***

## HOW TO USE THIS RUBRIC

After designing or implementing an API endpoint, evaluate it against
each dimension below. APIs are contracts — once consumed, they are
expensive to change. This rubric ensures the contract is right
**BEFORE** consumers depend on it.

Use this rubric:

- When designing APIs or reviewing API changes
- During Phase 7 of any API design or implementation task
- When evaluating internal or external service contracts
- During API contract comparison or compatibility-risk critique
- During pre-implementation API evaluation
- During benchmark comparison of API design approaches

***

## WHAT THIS RUBRIC EVALUATES

This rubric evaluates API quality across:

- Contract clarity and consumer fit
- URL and method correctness
- Response consistency and naming discipline
- Error handling completeness and error model quality
- Authentication and authorization explicitness
- Input validation and protection
- Data exposure discipline and internal detail leakage
- Pagination and bulk safety
- Backward compatibility and evolvability
- Documentation and implementation readiness
- Operational supportability

This rubric is for judging whether an API is not just technically
workable, but durable and trustworthy as a contract. A good API
is not just an interface that works — it is a contract consumers
can understand, depend on, and survive changes to.

***

## EVALUATION MATRIX

### 1. CONTRACT CLARITY AND CONSUMER FIT

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Contract fully defined before implementation. Request schema, response schema, and all error responses documented. Consumer can integrate without reading source code. Contract is shaped around the consumer's actual workflow and domain intent — not internal storage convenience. API is clearly designed for its actual consumer. Types derived from schema. Single source of truth for the contract. |
| **Acceptable** | Contract defined for primary request and response. Most error scenarios documented. Consumer can integrate with minimal questions. Contract reasonably consumer-oriented even if not perfectly shaped. |
| **Needs Work** | Contract partially defined. Some response fields undocumented. Consumer would need to read source code or experiment to understand behavior. Contract shaped more around backend convenience than consumer task. Naming only makes sense to internal developers. |
| **Failing** | No contract defined. API implemented ad-hoc. Response shape is whatever the data layer returns. Consumer is guessing at the interface. API serves the backend, not the consumer. Database-shaped payloads with no consumer-task orientation. |

***

### 2. URL AND METHOD CORRECTNESS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | URLs follow project conventions exactly: plural nouns, nested resources for ownership, kebab-case, no trailing slashes. HTTP methods used correctly — GET reads, POST creates, PATCH updates, DELETE removes. Methods are idempotent where they should be. Semantics are understandable and predictable. |
| **Acceptable** | URLs and methods are generally correct. Minor deviations from convention that do not cause confusion. Semantics are clear even if not perfectly convention-aligned. |
| **Needs Work** | Inconsistent URL patterns. Mixed conventions. Verbs in URLs where nouns should be. Semantics require interpretation. Awkward multi-call flow for a common use case. |
| **Failing** | URLs expose implementation details. Wrong HTTP methods — GET with side effects, POST for reads. No consistent pattern. Endpoint semantics confusing or misleading. |

***

### 3. RESPONSE CONSISTENCY AND NAMING DISCIPLINE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | All responses follow project conventions exactly. Single resources and collections wrapped consistently. Pagination included on collections. Errors use standard envelope with code, message, and details. Dates in ISO 8601. IDs as consistent types. Field names follow naming convention throughout. Null fields included rather than omitted. Response behaves like all related APIs in the system. |
| **Acceptable** | Response shape matches convention for primary cases. Minor inconsistencies in edge cases. Mostly consistent with other endpoints in the system. |
| **Needs Work** | Response shape inconsistent with other endpoints. Some fields use different naming conventions. Pagination format varies. API feels like a different system from related endpoints. |
| **Failing** | Raw database objects returned. Internal field names exposed. No consistent envelope. Different error formats across endpoints. API does not feel like one coherent system. |

***

### 4. ERROR HANDLING COMPLETENESS AND ERROR MODEL QUALITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Every failure scenario returns the correct HTTP status code with a structured error response. Validation, authentication, authorization, not-found, conflict, business-rule, rate-limit, and server-error cases each handled correctly and distinctly. Error messages are helpful without leaking internals. Field-level validation errors included where relevant. Consumer can identify what failed and why, and can respond programmatically. |
| **Acceptable** | Major error scenarios handled with correct status codes. Standard error response shape used. Most failure paths return meaningful messages. Consumer can understand primary error states. |
| **Needs Work** | Some error scenarios return generic status codes. Error messages are vague. Status codes used inconsistently — 403 versus 404 confusion. Generic "something went wrong" with no machine-readable error code. |
| **Failing** | Errors return raw exception messages or stack traces. Wrong status codes — 200 with error body. No structured error format. Consumer cannot distinguish between error types programmatically. Internal details leaking publicly. |

***

### 5. AUTHENTICATION AND AUTHORIZATION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Authentication checked as the first operation before validation or data access. Authorization verifies both role **AND** resource ownership. 401 for unauthenticated, 403 for unauthorized — not 404. Auth logic follows security baselines exactly. No auth bypass paths. Auth and authz assumptions explicit by contract and behavior. Protected operations are visibly protected. |
| **Acceptable** | Auth and authz correctly implemented. Correct status codes returned. Resource-level access controlled. Authentication and authorization expectations clear. |
| **Needs Work** | Auth present but authz incomplete. Some endpoints do not verify resource ownership. 401 and 403 used interchangeably. Auth assumptions implicit rather than explicit. |
| **Failing** | Missing auth checks. Endpoints accessible without authentication. Users can access other users' data. Privilege escalation possible. Auth bypass paths exist. |

***

### 6. INPUT VALIDATION AND PROTECTION

| Score | Criteria |
| :--- | :--- |
| **Excellent** | All input validated server-side via schema before any processing. Validation errors return structured response with field-level details. Query parameters validated for type, range, and allowed values. Path parameters validated for expected format. Pagination limits enforced with a maximum page size. Payload size limited. Abuse and misuse paths considered. Interface cannot be overloaded or misused easily. |
| **Acceptable** | Primary input fields validated. Validation errors return structured response. Basic parameter validation present. Major protection concerns addressed. |
| **Needs Work** | Some input fields not validated server-side. Validation errors are generic. Query parameters accepted without checking. Pagination limits not enforced. |
| **Failing** | No server-side validation. Raw input passed to data queries. Invalid data can enter the system. Injection risk present. Interface can be abused or overloaded without friction. |

***

### 7. DATA EXPOSURE DISCIPLINE AND INTERNAL DETAIL LEAKAGE

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Response returns only the fields the consumer needs — not the entire data record. Sensitive fields explicitly excluded. Response shape designed for the consumer, not derived from the internal model. Nested related data included only when necessary. Contract is cleaner than the internals behind it. No implementation or storage details leaking. |
| **Acceptable** | Response is reasonably scoped. Most sensitive fields excluded. Some unnecessary fields included but nothing harmful. Contract generally cleaner than the internal model. |
| **Needs Work** | Response returns most of the internal record. Some internal fields exposed. Consumer receives more data than needed. Contract shaped more by storage convenience than consumer need. |
| **Failing** | Raw internal model exposed through API. Sensitive data — password hashes, internal metadata, admin flags — included in responses. API leaks implementation details directly. Storage layer fully visible to consumer. |

***

### 8. PAGINATION AND BULK SAFETY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | All collection endpoints paginated with enforced limits. Default page size is reasonable. Maximum page size enforced. Pagination metadata included in response. Sorting supported with validated fields. Filtering on appropriate fields. No endpoint can return unbounded results. Collection access is bounded by contract. |
| **Acceptable** | Pagination implemented on primary collection endpoints. Limits enforced. Pagination metadata present. Major collection safety concerns addressed. |
| **Needs Work** | Some collection endpoints not paginated. No maximum page size enforcement. Missing pagination metadata. Some unbounded access paths still possible. |
| **Failing** | No pagination. Collection endpoints return all records. Unbounded requests possible. Database or service exhaustion possible under normal or adversarial usage. |

***

### 9. BACKWARD COMPATIBILITY AND EVOLVABILITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | No existing fields removed, renamed, or type-changed without versioning. New fields are optional and do not break existing consumers. Error codes unchanged. URL structure unchanged for existing endpoints. Versioning strategy followed when breaking changes are necessary. Contract preserves additive-evolution thinking. Likely breaking-risk areas are visible. Design avoids casual semantic drift. |
| **Acceptable** | Backward compatibility maintained for active endpoints. Any additions are non-breaking. Compatibility risks acknowledged and handled deliberately. |
| **Needs Work** | Minor breaking changes without consumer notification. Field renamed or type changed without versioning. Compatibility risks not made explicit. |
| **Failing** | Breaking changes deployed without versioning or consumer notification. Existing integrations will fail. No migration path. No compatibility discipline. |

> [!NOTE]
> For internal-only APIs not yet consumed externally, backward compatibility is important but not critical — dependent code can be updated simultaneously.

***

### 10. DOCUMENTATION AND IMPLEMENTATION READINESS

| Score | Criteria |
| :--- | :--- |
| **Excellent** | API contract documented with examples for request and response. All error scenarios documented. Documentation updated with the code change. Consumer can self-serve integration. Contract is specific enough that implementation and review can proceed without inventing core semantics later. Assumptions and examples visible enough to reduce ambiguity. |
| **Acceptable** | Basic documentation exists. Primary request and response documented. Consumer can integrate with minimal follow-up questions. Core semantics defined even if edge cases need clarification. |
| **Needs Work** | Minimal documentation. Consumer would need to ask questions to integrate. Contract leaves important behavior ambiguous. Implementation would need to invent or guess some behaviors. |
| **Failing** | No documentation. API discoverable only by reading source code. Contract so under-specified that implementation and review cannot proceed confidently. |

***

### 11. OPERATIONAL SUPPORTABILITY

| Score | Criteria |
| :--- | :--- |
| **Excellent** | Requests can be traced and failures investigated. Enough observability and request correlation to support the contract in production. Version usage visible. Auth and access failures traceable. Incidents diagnosable without heroic effort. |
| **Acceptable** | Basic observability present. Major failures traceable. Request correlation available for primary paths. |
| **Needs Work** | Limited observability. Some failure modes difficult to trace. Consumer issues hard to connect to server events. |
| **Failing** | No request correlation. Failures invisible from the server side. Version usage unknown. Incidents cannot be diagnosed reliably. Consumer reports the only signal available. |

***

## SCORING SUMMARY

| Dimension | Score | Notes |
| :--- | :--- | :--- |
| Contract Clarity / Consumer Fit |||
| URL and Method Correctness |||
| Response Consistency / Naming Discipline |||
| Error Handling / Error Model Quality |||
| Authentication and Authorization |||
| Input Validation / Protection |||
| Data Exposure / Internal Detail Leakage |||
| Pagination and Bulk Safety |||
| Backward Compatibility / Evolvability |||
| Documentation / Implementation Readiness |||
| Operational Supportability |||
***

## DELIVERY DECISION

| Result | Decision |
| :--- | :--- |
| All Excellent / Acceptable | ✅ API is ready for consumers |
| Auth / Authorization Failing | ❌ BLOCK — security vulnerability |
| Input Validation Failing | ❌ BLOCK — injection risk |
| Data Exposure Failing | ❌ BLOCK — sensitive data leak |
| Backward Compatibility Failing (external API) | ❌ BLOCK — will break consumers |
| Any 3+ Needs Work | ⚠️ API needs improvement before external consumers depend on it |

***

## MINIMUM PASS STANDARD

An API should not be considered strong if it is weak in any
of these high-priority areas:

- Contract clarity — consumer can integrate without guessing
- Error quality — failures are actionable and distinguishable
- Protection — auth, validation, and limits are enforced
- Backward compatibility — existing consumers are safe
- Consumer fit — contract serves the consumer's real task

An API that works today but breaks consumers, confuses
integrators, or leaks internals is not high quality.

***

## COMMON FAILURE PATTERNS

### Storage-Leak Contract

The contract mirrors internal data structures instead of the consumer's task. Raw ORM output presented as an API.

### Pretty Happy Path, Weak Failure Story

The success path looks neat but auth or error behavior is too vague for reliable use. Consumers cannot respond to failure states programmatically.

### Casual Breaking-Change Mindset

The design treats field changes and semantic drift too lightly. Existing consumers break without warning or migration path.

### Verbose But Still Unclear

The contract contains many fields or examples but still leaves important behavior ambiguous. Length is not clarity.

### Protocol Sophistication Masking Contract Weakness

The transport style sounds advanced but the underlying contract quality is still weak. The interface is not actually trustworthy as a durable contract.

### No Pagination on Collections

Collection endpoints return all records. One large dataset or adversarial request exhausts the database or service.

### Auth Without Authz

Authentication is present but resource-level authorization is missing. Any authenticated user can access any record.

***

## FINAL QUESTIONS

Before releasing this API to consumers, ask:

- Is this API easier for consumers to understand than the system behind it?
- What would most likely break or confuse consumers here?
- If this API lives for two years, will this contract age well?
- Can a consumer integrate without reading the source code?
- Would another team or client be able to adopt this without unnecessary friction?
- If this contract changes, will existing consumers survive?

***

## A good API is not just an interface that works — it is a contract consumers can understand, depend on, and survive changes to
