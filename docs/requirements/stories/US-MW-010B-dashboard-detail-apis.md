# US-MW-010B Dashboard Detail APIs

Status: Done

## User Story

As a Career Center dashboard consumer,
I want dashboard detail APIs,
so that individual dashboard widgets can retrieve status counts, role-code counts, and recent applications independently.

## Acceptance Criteria

- API exposes `GET /dashboard/statuses`.
- API exposes `GET /dashboard/roles`.
- API exposes `GET /dashboard/recent`.
- Status endpoint returns application counts by status.
- Roles endpoint returns application counts by role code.
- Recent endpoint returns recent applications.
- Endpoints read from PostgreSQL `career.job_application`.
- Endpoints return JSON suitable for future Motorweb dashboard widgets.

## Validation

Validated locally with the API running:

```bash
curl http://127.0.0.1:8000/dashboard/statuses | jq .
curl http://127.0.0.1:8000/dashboard/roles | jq .
curl http://127.0.0.1:8000/dashboard/recent | jq '.recent_applications | length'
```

Confirmed:

```text
/dashboard/statuses returned counts by status.
/dashboard/roles returned counts by role code.
/dashboard/recent returned 10 recent applications.
```

## Notes

These endpoints split dashboard summary data into smaller widget-oriented REST resources.
