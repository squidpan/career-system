# US-MW-011C Application Response Models

Status: Done

## User Story

As a Career Center API consumer,
I want application endpoints to have typed Pydantic response models,
so that OpenAPI and Swagger document application response structures.

## Acceptance Criteria

- `/applications` uses a typed response model.
- `/applications/{application_id}` uses a typed response model.
- `/applications/{application_id}/jd` uses a typed response model.
- `/applications/{application_id}/artifacts` uses a typed response model.
- OpenAPI includes application response schemas.
- Application endpoints continue returning working JSON.

## Validation

Validated locally:

```bash
curl http://127.0.0.1:8000/openapi.json \
  | jq '.paths["/applications"].get.responses["200"].content["application/json"].schema'

curl http://127.0.0.1:8000/openapi.json \
  | jq '.components.schemas | keys'
```

Confirmed OpenAPI schemas include:

```text
ApplicationSummary
ApplicationDetail
ApplicationJobDescriptions
ApplicationArtifacts
JobDescriptionItem
ApplicationArtifactItem
```

Confirmed /applications returns an array of:

```text
#/components/schemas/ApplicationSummary
```

## Notes

This extends v0.13.0 API Contract Hardening from dashboard endpoints to application endpoints.
