---
id: API-MW-001
type: openapi-requirement
project: motorweb
epic: EPIC-MW-001
release: future
status: draft
priority: high
tags:
  - requirements
  - motorweb
  - openapi
  - roles-api
created: 2026-06-14
updated: 2026-06-14
---

# API-MW-001 Roles API

## Purpose

Define REST API requirements for retrieving Career Center job role data.

## Resource

```text
/jobs/roles
/jobs/roles/{role_id}
```

## Business Context

Career System role data must be accessible through SQL, command-line scripts, REST APIs, and future dashboard/UI views.

## Related Data Model

- [[DM-MW-001 Job Role Entity]]

## Candidate Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | /jobs/roles | List job roles |
| GET | /jobs/roles/{role_id} | Retrieve one job role |

## Response Data

Responses should include role identifier, company, title, status, source, and timestamps.

## Traceability Requirement

API output must match equivalent SQL query output for the same role records.

## Related Stories

- [[US-MW-004 Query Career Data with SQL]]
