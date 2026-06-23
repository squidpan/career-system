# US-MW-009D Python Virtual Environment Standard

Status: Done

## User Story

As a Career Center developer,

I want a documented Python virtual environment standard,

so that service deployment is consistent across users and environments.

## Acceptance Criteria

* Standard venv location is documented.
* Repository-level venv usage is prohibited.
* Service-level venv structure is documented.
* Deployment instructions reference the standard.
* Standard validated during ted deployment testing.

## Validation

* ted deployment exposed ambiguity between repository-level and service-level virtual environments.
* Standardized on:

```text
services/career-center-api/.venv
```

* Startup scripts validated successfully using the documented structure.

