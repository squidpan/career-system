---
id: API-MW-004
type: openapi-requirement
project: motorweb
epic: EPIC-MW-001
release: future
status: draft
priority: medium
tags:
  - requirements
  - motorweb
  - openapi
  - tracker-events-api
created: 2026-06-14
updated: 2026-06-14
---

# API-MW-004 Tracker Events API

## Purpose

Define REST API requirements for exposing job-search tracker events.

## Resource

```text
/jobs/tracker-events
/jobs/tracker-events/{event_id}
/jobs/roles/{role_id}/events
```

## Related Data Model

- [[DM-MW-004 Tracker Event Entity]]

## Candidate Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | /jobs/tracker-events | List tracker events |
| GET | /jobs/tracker-events/{event_id} | Retrieve one tracker event |
| GET | /jobs/roles/{role_id}/events | Retrieve events for a role |

## Response Data

Responses should include event identifier, role identifier, event type, event date, status, source, and notes.

## Related Stories

- [[US-MW-003 Load Career System Data]]
- [[US-MW-004 Query Career Data with SQL]]
