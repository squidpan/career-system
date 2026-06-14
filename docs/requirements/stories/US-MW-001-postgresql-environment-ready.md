---
id: US-MW-001
type: user-story
project: motorweb
epic: EPIC-MW-001
release: REL-MW-0.1
status: backlog
priority: high
created: 2026-06-14
updated: 2026-06-14
tags:
  - requirements
  - motorweb
  - postgres
  - environment
---

# US-MW-001 PostgreSQL Environment Ready

## Story

As Paul,
I want my local PostgreSQL environment verified and ready,
so that Motorweb Career Center can load and query Career System data locally.

## Business Context

Motorweb Career Center depends on a local PostgreSQL environment for the initial POC. Paul already has local PostgreSQL installed and wants to use a separate `career_center` database for Career System data.

This story ensures the database platform is ready before schema creation and data loading begin.

## Problem Statement

Without a verified PostgreSQL environment, later stories may fail due to unclear installation state, credentials, permissions, or connection issues.

## Desired Outcome

Paul can connect to local PostgreSQL from the terminal and confirm that PostgreSQL is running and accessible.

## Scope

Included:

- verify PostgreSQL service is running
- verify `psql` command works
- verify connection as PostgreSQL admin user
- confirm ability to create a separate Career Center database in a later story

Out of scope:

- schema creation
- data loading
- REST API work
- React UI work

## Prerequisites

- [[PREREQ-MW-001 PostgreSQL Installed]]

## Acceptance Criteria

- [[AC-MW-001]]

## UAT

- [[UAT-MW-001]]

## Technical Notes

Expected local database context:

```text
host: localhost
port: 5432
admin user: postgres
future database: career_center
```

## Trello Mapping

Suggested Trello card:

```text
US-MW-001 PostgreSQL Environment Ready
```

List:

```text
Backlog
```

## Related Artifacts

- [[EPIC-MW-001 Career Center Platform]]
- [[REL-MW-0.1 PostgreSQL POC]]
- [[TERM-MW-001 Career Center]]

