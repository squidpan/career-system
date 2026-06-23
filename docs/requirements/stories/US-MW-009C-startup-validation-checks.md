# US-MW-009C Startup Validation Checks

Status: Done

## User Story

As a Career Center operator,
I want the API startup script to validate required prerequisites,
so that startup failures are clear and actionable.

## Acceptance Criteria

- Startup script validates service virtual environment exists.
- Startup script validates CAREER_DB_PASSWORD is set.
- Startup script validates required application files exist.
- Startup script shows clear remediation guidance when validation fails.
- API starts successfully when validation passes.

## Validation

- Ran `./bin/run-career-center-api.sh` without `CAREER_DB_PASSWORD`.
- Confirmed clear failure message.
- Ran `CAREER_DB_PASSWORD='career_app_dev_password' ./bin/run-career-center-api.sh`.
- Confirmed FastAPI/Uvicorn started successfully.

