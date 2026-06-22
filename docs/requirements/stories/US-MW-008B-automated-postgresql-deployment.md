# US-MW-008B Automated PostgreSQL Deployment

Status: Done

## User Story

As a Career Center operator,
I want a repeatable PostgreSQL deployment script,
so that the database, role, schema, and tables can be provisioned consistently.

## Acceptance Criteria

- Script creates or validates `career_center`.
- Script creates or validates `career_app`.
- Script creates or validates `career` schema.
- Script creates or validates application tables.
- Script can be rerun safely.
- Script documents required privileges.

## Deployment Findings

During ted deployment validation, the PostgreSQL setup script exposed two deployment concerns:

1. The postgres operating-system user cannot reliably access SQL files stored under another user's home directory (e.g. /home/pl/...).

2. Database and role creation scripts are not yet fully idempotent and produce "already exists" messages when rerun.

Future improvements:

* Execute PostgreSQL setup from a neutral location such as /tmp.
* Add existence checks for database and role creation.
* Eliminate permission-related warnings during deployment validation.

