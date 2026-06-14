---
id: EPIC-MW-001
type: epic
project: motorweb
parent_business_epic: EPIC-CS-001
status: draft
priority: high
created: 2026-06-14
updated: 2026-06-14
tags:
  - requirements
  - motorweb
  - career-center
  - postgres
  - api
  - react
---

# EPIC-MW-001 Career Center Platform

## Business Alignment

This epic supports [[EPIC-CS-001 Employment Acceleration System]].

Motorweb Career Center is the technical platform that exposes Career System data through multiple access paths.

## Platform Goal

Build a Career Center platform that allows Career System data to be queried, validated, displayed, and eventually managed through:

- command line workflows
- PostgreSQL and SQL queries
- REST APIs
- OpenAPI contracts
- dashboard/table views
- future React frontend
- future JD ingestion UI

## Problem Statement

Career System data currently exists primarily as files and generated artifacts. This is powerful, but it limits queryability, dashboarding, API access, and UI-driven workflows.

Motorweb will provide a technical implementation layer that makes Career System data operational.

## Desired Outcome

Users should be able to see the same Career System truth through multiple access paths:

```text
Career System data
      ↓
PostgreSQL
      ↓
SQL queries
      ↓
REST API
      ↓
CLI / dashboard / React UI
```

## Scope

Initial POC scope:

- PostgreSQL environment readiness
- Career Center database creation
- Career System data loading
- SQL query validation
- REST API read endpoints
- OpenAPI specification
- API vs SQL result validation
- basic dashboard/table-view thinking

Future scope:

- simple, modern React UI
- elegant landing page
- JD ingestion UI
- dashboard filters and sorting
- application workflow management

## Out of Scope for Initial POC

- full authentication
- production deployment
- complex UI workflows
- Trello API synchronization
- Jira export
- Confluence export

## Related Artifacts

- [[EPIC-CS-001 Employment Acceleration System]]
- [[REL-MW-0.1 PostgreSQL POC]]
- [[US-MW-001 PostgreSQL Environment Ready]]
- [[TERM-MW-001 Career Center]]

