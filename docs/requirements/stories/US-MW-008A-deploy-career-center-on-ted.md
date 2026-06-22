# US-MW-008A Deploy Career Center on ted

Status: Done

## User Story

As a Career System / Motorweb developer,
I want to deploy Career Center under the `ted` local user,
so that the system can be validated from a fresh operational user environment.

## Acceptance Criteria

- Repo is available under ted.
- Python 3.13 virtual environment can be created under ted.
- PostgreSQL setup can be validated from ted.
- Application data can be loaded into PostgreSQL.
- Artifact data can be loaded into PostgreSQL.
- FastAPI service starts under ted.
- Swagger UI is accessible.
- Smoke tests pass:
  - GET /health
  - GET /applications
  - GET /applications/{id}
  - GET /applications/{id}/jd
  - GET /applications/{id}/artifacts

## Out of Scope

- Production deployment
- Cloud deployment
- React UI
- Authentication
- HTTPS
