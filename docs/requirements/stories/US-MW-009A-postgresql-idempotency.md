# US-MW-009A PostgreSQL Idempotency

Status: Done

## User Story

As a Career Center operator,
I want PostgreSQL setup scripts to be rerunnable,
so that deployment setup can safely validate or recreate expected database objects.

## Acceptance Criteria

- Database existence is checked before create.
- Role existence is checked before create.
- Setup script can be run repeatedly without fatal database/role errors.
- Setup script avoids postgres working-directory permission warnings.
- Validation confirms database, role, schema, and tables exist.

## Validation

Ran `bin/setup-career-center-postgres.sh` three times successfully.

