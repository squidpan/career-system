---
id: AC-MW-004
type: acceptance-criteria
project: motorweb
story: US-MW-004
status: backlog
created: 2026-06-14
updated: 2026-06-14
---

# AC-MW-004 Query Career Data with SQL

## Acceptance Criteria

### AC1 Active Roles Query

Given role data is loaded,
when the active roles query is run,
then it returns a table of active job roles.

### AC2 JD Coverage Query

Given role and JD data are loaded,
when the JD coverage query is run,
then it identifies roles with and without associated job descriptions.

### AC3 Application Package Coverage Query

Given application package data is loaded,
when the application package coverage query is run,
then it identifies roles with and without generated application packages.

### AC4 Dashboard Candidate Query

Given Career Center data is loaded,
when the dashboard query is run,
then it returns a table suitable for later REST API and UI display.
