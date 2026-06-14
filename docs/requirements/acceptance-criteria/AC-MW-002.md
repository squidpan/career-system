---
id: AC-MW-002
type: acceptance-criteria
project: motorweb
story: US-MW-002
status: backlog
created: 2026-06-14
updated: 2026-06-14
---

# AC-MW-002 Career Center Database Created

## Acceptance Criteria

### AC1 Database Exists

Given PostgreSQL is installed locally,
when the database list is displayed,
then a database named `career_center` is present.

### AC2 Database Is Reachable

Given the `career_center` database exists,
when Paul connects using `psql`,
then the connection succeeds without error.

### AC3 Database Is Separate

Given existing local databases may already exist,
when the database list is reviewed,
then `career_center` is separate from unrelated databases such as `squidpan`.

### AC4 Naming Convention Is Documented

Given the database is created,
when the requirements are reviewed,
then the database name and initial naming convention are documented.
