---
id: API-MW-002
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
  - job-descriptions-api
created: 2026-06-14
updated: 2026-06-14
---

# API-MW-002 Job Descriptions API

## Purpose

Define REST API requirements for retrieving job description metadata and normalized JD references.

## Resource

```text
/jobs/descriptions
/jobs/descriptions/{jd_id}
```

## Related Data Model

- [[DM-MW-002 Job Description Entity]]

## Candidate Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | /jobs/descriptions | List job descriptions |
| GET | /jobs/descriptions/{jd_id} | Retrieve one job description |

## Response Data

Responses should include JD identifier, related role, source, raw file reference, normalized file reference, and status.

## Traceability Requirement

API output must support linking each JD back to the related role and source artifact.

## Related Stories

- [[US-MW-003 Load Career System Data]]
- [[US-MW-004 Query Career Data with SQL]]
