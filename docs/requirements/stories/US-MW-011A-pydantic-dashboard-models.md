# US-MW-011A Pydantic Dashboard Models

Status: Done

## User Story

As a Career Center API consumer,
I want dashboard API responses to have typed Pydantic models,
so that OpenAPI and Swagger document the dashboard response structures.

## Acceptance Criteria

- Dashboard summary endpoint uses a Pydantic response model.
- Dashboard statuses endpoint uses a Pydantic response model.
- Dashboard roles endpoint uses a Pydantic response model.
- Dashboard recent endpoint uses a Pydantic response model.
- OpenAPI includes dashboard response schemas.
- Swagger no longer shows empty dashboard response schemas.
- Dashboard endpoints continue returning working JSON.

## Validation

Validated with API running locally:

```bash
curl http://127.0.0.1:8000/openapi.json | jq '.components.schemas'

curl http://127.0.0.1:8000/openapi.json \
  | jq '.paths["/dashboard/summary"].get.responses["200"].content["application/json"].schema'
```

Confirmed OpenAPI schemas include:

```text
DashboardSummary
DashboardStatusCounts
DashboardRoleCounts
DashboardRecentApplications
RecentApplication
```

Confirmed /dashboard/summary now references:

```text
#/components/schemas/DashboardSummary
```

## Notes

This story begins v0.13.0 Career Center API Contract Hardening.

The API moved from untyped response dictionaries to typed response contracts for dashboard endpoints.
