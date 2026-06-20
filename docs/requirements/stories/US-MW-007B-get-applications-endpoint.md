# US-MW-007B GET /applications Endpoint

Status: Done

## User Story

As an API user,
I want to retrieve application summaries,
so that dashboards can display tracked applications.

## Acceptance Criteria

- `GET /applications` returns 11 rows.
- Response includes application_id, company, role, status, last_update, and role_code.
- Data comes from `career.job_application`.
