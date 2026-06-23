# US-MW-010C Dashboard SQL Query Standard

Status: Done

## User Story

As a Career Center developer,
I want dashboard API SQL documented as reference queries,
so that REST endpoint behavior can be traced back to PostgreSQL queries.

## Acceptance Criteria

- Dashboard endpoint SQL is documented under `sql/postgres/queries/`.
- Reference SQL includes total application count.
- Reference SQL includes application counts by status.
- Reference SQL includes application counts by role code.
- Reference SQL includes recent applications query.
- SQL file maps queries to dashboard REST endpoints.
- Standard supports future validation that SQL and REST return equivalent data.

## Validation

Created:

```text
sql/postgres/queries/dashboard_api_queries.sql
```

Mapped SQL to:

```text
GET /dashboard/summary
GET /dashboard/statuses
GET /dashboard/roles
GET /dashboard/recent
```

Verified SQL aligns with:

```text
services/career-center-api/app/routers/dashboard.py
```

## Notes

This story establishes the traceability pattern:

```text
PostgreSQL query
→ FastAPI endpoint
→ OpenAPI contract
→ Motorweb dashboard consumer
```
