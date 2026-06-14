---
id: CTX-MW-001
type: context-package
project: motorweb
epic: EPIC-MW-001
release: REL-MW-0.1
status: draft
priority: high
tags:
  - requirements
  - motorweb
  - postgresql
  - poc
  - context-package
created: 2026-06-14
updated: 2026-06-14
---

# CTX-MW-001 Career Center PostgreSQL POC

## Purpose

This context package explains the first Motorweb proof of concept for Career Center data.

The POC proves that Career System data can be loaded into PostgreSQL and accessed consistently through SQL, command line workflows, REST APIs, and future dashboard or React UI views.

## Related Epic

- [[EPIC-MW-001 Career Center Platform]]

## Related Release

- [[REL-MW-0.1 PostgreSQL POC]]

## Business Driver

Career System needs reliable, queryable job search data so Paul can understand active roles, application status, job descriptions, application packages, and future fit/gap analysis results.

## Solution Goal

Create a PostgreSQL-backed Career Center foundation that can support:

- SQL queries
- command line data validation
- REST API access
- OpenAPI specification
- future dashboard views
- future React UI
- future JD ingestion workflow

## Architecture View

```text
Career System Files
  ↓
Load Script / ETL
  ↓
PostgreSQL career_center Database
  ↓
SQL Queries
  ↓
REST API / OpenAPI
  ↓
CLI / Dashboard / React UI
```

## In Scope

- Career Center database creation
- Career System data loading
- SQL query validation
- initial REST API requirements
- OpenAPI traceability
- data model artifacts
- UAT procedures

## Out of Scope

- full React implementation
- production deployment
- authentication / authorization
- Trello API synchronization
- Jira export
- Confluence export

## Related Stories

- [[US-MW-001 PostgreSQL Environment Ready]]
- [[US-MW-002 Career Center Database Created]]
- [[US-MW-003 Load Career System Data]]
- [[US-MW-004 Query Career Data With SQL]]

## Related Data Models

- [[DM-MW-001 Job Role Entity]]
- [[DM-MW-002 Job Description Entity]]
- [[DM-MW-003 Application Package Entity]]
- [[DM-MW-004 Tracker Event Entity]]
- [[DM-MW-005 Resume Entity]]
- [[DM-MW-006 Gap Analysis Entity]]

## Related API Requirements

- [[API-MW-001 Roles API]]
- [[API-MW-002 Job Descriptions API]]
- [[API-MW-003 Application Packages API]]
- [[API-MW-004 Tracker Events API]]

## Success Criteria

The POC is successful when Career System data can be queried from PostgreSQL and the same information can later be exposed through REST APIs and dashboard views without redefining the underlying source concepts.
