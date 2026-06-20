# US-MW-008B Automated PostgreSQL Deployment

Status: Draft

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
