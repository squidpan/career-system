# US-MW-010D Dashboard OpenAPI Review

Status: Done

## User Story

As a Career Center API consumer,
I want dashboard endpoints to appear in the generated OpenAPI contract,
so that future Motorweb clients can discover and validate dashboard API behavior.

## Acceptance Criteria

- `/dashboard/summary` appears in `/openapi.json`.
- `/dashboard/statuses` appears in `/openapi.json`.
- `/dashboard/roles` appears in `/openapi.json`.
- `/dashboard/recent` appears in `/openapi.json`.
- Dashboard endpoints are tagged as `dashboard`.
- Dashboard endpoints are visible through Swagger UI.

## Validation

Validated with the API running locally:

```bash
curl http://127.0.0.1:8000/openapi.json | jq '.paths | keys'
curl http://127.0.0.1:8000/openapi.json | jq '.paths["/dashboard/summary"]'
curl http://127.0.0.1:8000/openapi.json | jq '.paths["/dashboard/statuses"]'
curl http://127.0.0.1:8000/openapi.json | jq '.paths["/dashboard/roles"]'
curl http://127.0.0.1:8000/openapi.json | jq '.paths["/dashboard/recent"]'
```

Confirmed dashboard paths:

```text
/dashboard/recent
/dashboard/roles
/dashboard/statuses
/dashboard/summary
```

## Notes

This completes the traceability chain from dashboard SQL to REST endpoints to generated OpenAPI documentation.
