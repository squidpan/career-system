# US-MW-007 Application Detail REST APIs

Status: Draft

## User Story

As a Motorweb Career Center API user,
I want REST endpoints that expose application summaries and related artifact details,
so that applications, JDs, resumes, and notes can be consumed by UI dashboards or other tools.

## Proposed Endpoints

- GET /applications
- GET /applications/{application_id}
- GET /applications/{application_id}/jd
- GET /applications/{application_id}/resume
- GET /applications/{application_id}/notes

## Acceptance Criteria

- `/applications` returns summary application rows.
- `/applications/{application_id}` returns application metadata.
- JD endpoint returns normalized JD text where available.
- Resume endpoint returns final resume text where available.
- Notes endpoint returns submission notes or related application notes.
- Missing artifacts return a clear empty/null response rather than failing unexpectedly.

## Implementation Notes

Initial implementation may be read-only.

OpenAPI should be treated as the contract for future UI and integration work.
