---
id: AC-MW-001
type: acceptance-criteria
project: motorweb
story: US-MW-001
status: draft
priority: high
created: 2026-06-14
updated: 2026-06-14
tags:
  - requirements
  - motorweb
  - postgres
  - acceptance-criteria
---

# AC-MW-001 PostgreSQL Environment Ready

## Acceptance Criteria

### AC-001.1 PostgreSQL Client Available

Given Paul is working from the terminal,
when he runs `psql --version`,
then PostgreSQL client version information is displayed.

### AC-001.2 PostgreSQL Service Running

Given PostgreSQL is installed locally,
when Paul checks the PostgreSQL service,
then the service is confirmed running or otherwise accessible locally.

### AC-001.3 Admin Connection Works

Given Paul has local PostgreSQL admin credentials,
when he connects to PostgreSQL,
then the connection succeeds.

### AC-001.4 Ready for Career Center Database Creation

Given PostgreSQL is accessible,
when this story is complete,
then the next story can create the `career_center` database.

## Related Artifacts

- [[US-MW-001 PostgreSQL Environment Ready]]
- [[UAT-MW-001]]

