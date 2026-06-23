# US-MW-010A Dashboard Summary API

Status: Done

## User Story

As a Career Center dashboard consumer,
I want a dashboard summary API,
so that application counts, status distribution, role-code distribution, and recent applications can be retrieved from PostgreSQL through REST.

## Acceptance Criteria

- API exposes `GET /dashboard/summary`.
- Response includes total application count.
- Response includes counts by application status.
- Response includes counts by role code.
- Response includes recent applications.
- Endpoint reads from PostgreSQL `career.job_application`.
- Endpoint returns JSON suitable for future Motorweb dashboard use.

## Validation

Validated locally with the API running:

```bash
curl http://127.0.0.1:8000/dashboard/summary | jq .
```

Confirmed response included:
```text
application_count
counts_by_status
counts_by_role_code
recent_applications
```

Example validation result:
```text
application_count = 11
APPLIED = 7
POSITION_CLOSED = 2
NOT_PURSUED = 1
REJECTED = 1
```

### Notes

This is the first dashboard-oriented REST endpoint for Career Center.
