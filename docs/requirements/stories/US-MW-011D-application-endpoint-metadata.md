# US-MW-011D Application Endpoint Metadata

Status: Done

## User Story

As a Career Center API consumer,
I want application endpoints to include summaries and descriptions,
so that OpenAPI and Swagger provide useful documentation for application resources.

## Acceptance Criteria

- `/applications` defines summary and description metadata.
- `/applications/{application_id}` defines summary and description metadata.
- `/applications/{application_id}/jd` defines summary and description metadata.
- `/applications/{application_id}/artifacts` defines summary and description metadata.
- OpenAPI exposes application endpoint metadata.
- Swagger displays application endpoint metadata.
- Application functionality remains unchanged.

## Validation

Validated locally:

```bash
python3.13 -m py_compile services/career-center-api/app/routers/applications.py

curl http://127.0.0.1:8000/openapi.json \
  | jq '.paths["/applications"].get | {summary, description, tags}'
```

Confirmed:

```text
summary present
description present
applications tag present
```

## Notes

This story improves API self-documentation and consumer usability for Career Center application endpoints.
