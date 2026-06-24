# US-MW-011E OpenAPI Contract Review

Status: Done

## User Story

As a Career Center API consumer,
I want the OpenAPI contract reviewed for application and dashboard endpoints,
so that Motorweb and future API consumers can rely on documented response schemas and endpoint metadata.

## Acceptance Criteria

- OpenAPI exposes all application endpoints.
- OpenAPI exposes all dashboard endpoints.
- Application endpoints include response schemas.
- Dashboard endpoints include response schemas.
- Application endpoints include summaries and descriptions.
- Dashboard endpoints include summaries and descriptions.
- Remaining contract gaps are documented.

## Validation

Validated locally:

```bash
curl http://127.0.0.1:8000/openapi.json \
  | jq '.paths | keys'

curl http://127.0.0.1:8000/openapi.json \
  | jq '.components.schemas | keys'

curl http://127.0.0.1:8000/openapi.json \
  | jq '.paths
    | to_entries[]
    | {
        path: .key,
        summary: .value.get.summary,
        description: .value.get.description,
        schema: .value.get.responses["200"].content["application/json"].schema
      }'
```

Confirmed:

```text
/application endpoints expose typed schemas and metadata.
/dashboard endpoints expose typed schemas and metadata.
```

Reviewed endpoints:

```text
/applications
/applications/{application_id}
/applications/{application_id}/jd
/applications/{application_id}/artifacts
/dashboard/summary
/dashboard/statuses
/dashboard/roles
/dashboard/recent
```

Reviewed schemas:

```text
ApplicationSummary
ApplicationDetail
ApplicationJobDescriptions
ApplicationArtifacts
DashboardSummary
DashboardStatusCounts
DashboardRoleCounts
DashboardRecentApplications
```

## Remaining Gaps

- /health still has an empty response schema.
- /health has no description metadata.
- Error response model standard is not yet defined.
- Response examples are not yet defined.

## Notes

This story completes the first pass of v0.13.0 Career Center API Contract Hardening.

The API is now substantially more consumable by Swagger, Postman, future automated tests, and Motorweb.
