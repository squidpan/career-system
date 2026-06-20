# US-MW-007E GET /applications/{application_id}/artifacts Endpoint

Status: Done

## User Story

As an API user,
I want to retrieve application artifacts,
so that tools can access submitted resume text and submission notes.

## Acceptance Criteria

- Endpoint returns final resume where available.
- Endpoint returns submission notes.
- Data comes from `career.application_artifact`.
