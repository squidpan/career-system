---
id: REL-MW-0.1
type: release
project: motorweb
status: draft
priority: high
epic: EPIC-MW-001
created: 2026-06-14
updated: 2026-06-14
tags:
  - requirements
  - motorweb
  - release
  - postgres
---

# REL-MW-0.1 PostgreSQL POC

## Release Goal

Prove that Career System data can be loaded into a local PostgreSQL database and queried reliably from SQL as the first step toward REST APIs, dashboards, and a future React UI.

## Business Value

This release supports Career System by making job search data queryable and easier to validate.

## Scope

Stories planned for this release:

- [[US-MW-001 PostgreSQL Environment Ready]]
- US-MW-002 Career Center Database Created
- US-MW-003 Load Career System Data
- US-MW-004 Query Career Data with SQL
- US-MW-005 Expose REST APIs
- US-MW-006 Generate OpenAPI Specification
- US-MW-007 Validate API vs SQL Results
- US-MW-008 Publish POC Documentation

## Release Exit Criteria

- PostgreSQL is available locally
- `career_center` database exists
- Career System data can be loaded
- core SQL queries return expected results
- documentation explains how to reproduce the POC

## Related Artifacts

- [[EPIC-MW-001 Career Center Platform]]
- [[TERM-MW-001 Career Center]]

