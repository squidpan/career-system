---
id: US-MW-003
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
  - data-load
created: 2026-06-14
updated: 2026-06-14
---

# US-MW-003 Load Career System Data

## User Story

As Paul,
I want Career System role, event, job description, and application-package data loaded into PostgreSQL,
so that I can query my job search data consistently from SQL and later expose the same data through APIs and dashboards.

## Business Context

The business goal of Career System is to help Paul get a job by producing better application packages, gap analysis, interview prep, and application prioritization. Motorweb supports that goal by making the underlying Career System data queryable and reusable.

## Problem Statement

Career System data exists across tracker CSVs, raw JDs, normalized JDs, resume artifacts, and generated application packages. Without a database load process, it is difficult to answer questions such as which roles are active, which roles have JDs, which roles have application packages, and which roles are ready to apply.

## Desired Outcome

Career System data can be loaded into the `career_center` PostgreSQL database using a repeatable process.

## Scope

Included:

- Identify source files from Career System.
- Define initial tables needed for the PostgreSQL POC.
- Load tracker role data.
- Load tracker event data where available.
- Load job description metadata.
- Load application package metadata where available.
- Produce a repeatable load command or script.

## Out of Scope

Not included:

- Full production ETL framework.
- Complex deduplication.
- UI-based ingestion.
- External job-board API ingestion.
- Authentication and authorization.

## Data Impact

Initial entities:

- Job Role
- Job Event
- Job Description
- Application Package

Related data model artifacts:

- [[DM-MW-001 Job Role Entity]]
- [[DM-MW-002 Job Description Entity]]
- [[DM-MW-003 Application Package Entity]]

## API Impact

No API endpoint is required in this story, but loaded data becomes the source for future REST endpoints.

## Prerequisites

- [[US-MW-002 Career Center Database Created]]

## Acceptance Criteria

- [[AC-MW-003]]

## UAT

- [[UAT-MW-003]]

## Related Artifacts

- [[EPIC-CS-001 Employment Acceleration System]]
- [[EPIC-MW-001 Career Center Platform]]
- [[REL-MW-0.1 PostgreSQL POC]]
- [[TERM-CS-003 Job Role]]
- [[TERM-CS-004 Job Description]]
- [[TERM-CS-001 Application Package]]
