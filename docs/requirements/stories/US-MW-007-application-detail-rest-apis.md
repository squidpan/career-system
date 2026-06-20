# US-MW-007 Application Detail REST APIs

Status: Draft

## User Story

As a Motorweb Career Center API user,
I want read-only REST endpoints for applications, JDs, and artifacts,
so that dashboards and tools can retrieve Career System data from PostgreSQL through a stable API contract.

## Scope

- GET /applications
- GET /applications/{application_id}
- GET /applications/{application_id}/jd
- GET /applications/{application_id}/artifacts

## Acceptance Criteria

- API contract is defined in OpenAPI.
- Endpoints are read-only.
- API reads from PostgreSQL, not the filesystem.
- Application summary endpoint returns 11 rows.
- Detail endpoint returns one application by ID.
- JD endpoint returns normalized and raw JD text.
- Artifacts endpoint returns final resume and submission notes where available.
