# US-MW-009E OpenAPI / Swagger Exposure

Status: Done

## User Story

As a Career Center developer,
I want the running FastAPI service to expose OpenAPI and Swagger documentation,
so that API behavior can be inspected, validated, and used by future Motorweb consumers.

## Acceptance Criteria

- FastAPI service exposes `/openapi.json`.
- FastAPI service exposes `/docs`.
- `/openapi.json` returns OpenAPI JSON.
- `/docs` returns Swagger UI HTML.
- OpenAPI output includes current Career Center API endpoints.
- Swagger UI title identifies Career Center API.

## Validation

Validated with the API running locally:

```bash
curl http://127.0.0.1:8000/openapi.json | head
curl http://127.0.0.1:8000/docs | head

GET /openapi.json returned 200 OK.
GET /docs returned 200 OK.
OpenAPI output included Career Center API endpoints.
Swagger UI rendered with title: Career Center API - Swagger UI.
Notes

No code changes were required. FastAPI provides OpenAPI and Swagger exposure automatically from the registered application routes.
