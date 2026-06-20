# US-MW-007D GET /applications/{application_id}/jd Endpoint

Status: Done

## User Story

As an API user,
I want to retrieve normalized and raw JD text for an application,
so that tools can display or analyze JD content.

## Acceptance Criteria

- Endpoint returns normalized JD where available.
- Endpoint returns raw JD where available.
- Data comes from `career.job_description`.
