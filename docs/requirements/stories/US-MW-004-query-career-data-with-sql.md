---
id: US-MW-004
type: user-story
project: motorweb
epic: EPIC-MW-001
release: REL-MW-0.1
status: backlog
priority: high
tags:
  - requirements
  - motorweb
  - sql
  - reporting
created: 2026-06-14
updated: 2026-06-14
---

# US-MW-004 Query Career Data with SQL

## User Story

As Paul,
I want useful SQL queries against Career Center data,
so that I can inspect job-search status, application readiness, JD coverage, and future dashboard metrics directly from the terminal or pgAdmin.

## Business Context

Before building REST APIs or a React UI, Motorweb should prove that Career System data can answer useful job-search questions. SQL is the first dashboard and validation layer.

## Problem Statement

Without defined SQL queries, the database may contain data but still fail to answer practical questions. A useful POC must demonstrate business value, not just prove that tables exist.

## Desired Outcome

A small set of SQL queries produces meaningful table-style views of Career System data.

## Scope

Included:

- Query active roles.
- Query roles with and without job descriptions.
- Query roles with and without application packages.
- Query role status summary counts.
- Query recent job-search events.
- Query candidate dashboard data for later API/UI use.

## Out of Scope

Not included:

- Complex analytics.
- AI-generated recommendations.
- React UI.
- Full dashboard layout.
- Production reporting layer.

## Data Impact

No new data is created. This story validates loaded data through SQL queries.

## API Impact

The SQL query outputs should inform later REST API response shape.

## Prerequisites

- [[US-MW-003 Load Career System Data]]

## Acceptance Criteria

- [[AC-MW-004]]

## UAT

- [[UAT-MW-004]]

## Related Artifacts

- [[EPIC-CS-001 Employment Acceleration System]]
- [[EPIC-MW-001 Career Center Platform]]
- [[REL-MW-0.1 PostgreSQL POC]]
- [[TERM-CS-006 Fit Score]]
