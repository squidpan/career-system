# US-MW-011B Dashboard Endpoint Metadata

Status: Done

## User Story

As a Career Center API consumer,

I want dashboard endpoints to include summaries and descriptions,

so that OpenAPI and Swagger provide useful documentation.

## Acceptance Criteria

- Dashboard endpoints define summaries.
- Dashboard endpoints define descriptions.
- OpenAPI exposes endpoint metadata.
- Swagger displays endpoint metadata.
- Dashboard functionality remains unchanged.

## Validation

Validated locally:

```bash
curl http://127.0.0.1:8000/openapi.json \
  | jq '.paths["/dashboard/summary"].get | {summary, description, tags}'
```

Confirmed:

```text
summary present
description present
dashboard tag present
```

## Notes

This story improves API self-documentation and consumer usability without changing endpoint behavior.
