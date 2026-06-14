---
id: US-MW-002
type: user-story
project: motorweb
epic: EPIC-MW-001
release: REL-MW-0.1
status: backlog
priority: high
tags:
  - requirements
  - motorweb
  - postgres
  - database
created: 2026-06-14
updated: 2026-06-14
---

# US-MW-002 Career Center Database Created

## User Story

As Paul,
I want a dedicated local PostgreSQL database for Career Center,
so that Career System data can be loaded, queried, validated, and later exposed through APIs and dashboards.

## Business Context

Career System is becoming the source of truth for job roles, job descriptions, applications, resumes, application packages, gap analysis, and interview preparation. Motorweb needs a real database foundation so the same data can eventually be viewed through SQL, command line tools, REST APIs, dashboards, and a React UI.

## Problem Statement

Career System data currently exists primarily as files. Files are useful for source control and Markdown workflows, but they are not ideal for SQL queries, dashboards, API responses, or data validation across related entities.

## Desired Outcome

A dedicated PostgreSQL database named `career_center` exists locally and can be accessed from the terminal using `psql`.

## Scope

Included:

- Create local PostgreSQL database `career_center`.
- Confirm database is reachable from terminal.
- Confirm database is separate from existing application databases.
- Establish naming convention for Career Center database objects.

## Out of Scope

Not included:

- Full schema design.
- Data loading.
- REST API implementation.
- React UI.
- Production deployment.

## Data Impact

This story creates the database container for future Career Center entities.

Related data model artifacts:

- [[DM-MW-001 Job Role Entity]]
- [[DM-MW-002 Job Description Entity]]
- [[DM-MW-003 Application Package Entity]]

## API Impact

No API endpoint is created by this story. Future REST APIs will depend on this database.

## Prerequisites

- [[PREREQ-MW-001 PostgreSQL Installed]]

## Acceptance Criteria

- [[AC-MW-002]]

## UAT

- [[UAT-MW-002]]

## Related Artifacts

- [[EPIC-MW-001 Career Center Platform]]
- [[REL-MW-0.1 PostgreSQL POC]]
- [[TERM-MW-001 Career Center]]
