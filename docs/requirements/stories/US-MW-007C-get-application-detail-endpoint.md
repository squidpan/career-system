# US-MW-007C GET /applications/{application_id} Endpoint

Status: Draft

## User Story

As an API user,
I want to retrieve one application by ID,
so that I can view full application metadata.

## Acceptance Criteria

- Existing application_id returns HTTP 200.
- Missing application_id returns HTTP 404.
- Data comes from `career.job_application`.
