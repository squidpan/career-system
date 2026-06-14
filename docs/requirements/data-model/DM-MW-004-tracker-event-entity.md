---
id: DM-MW-004
type: data-model
project: motorweb
epic: EPIC-MW-001
release: REL-MW-0.1
status: draft
priority: high
tags:
  - requirements
  - motorweb
  - data-model
  - tracker-events
created: 2026-06-14
updated: 2026-06-14
---

# DM-MW-004 Tracker Event Entity

## Purpose

Defines the tracker event entity used to represent job-search activities and lifecycle events imported from Career System tracker event CSVs.

## Business Context

Career System tracks job search activity over time. Motorweb must preserve this event history so Paul can understand the timeline of each job opportunity and application.

## Entity Description

A Tracker Event is a dated activity associated with a job role, application, resume, interview, follow-up, or other job-search milestone.

## Candidate Fields

| Field | Description | Notes |
|---|---|---|
| event_id | Unique internal event identifier | Motorweb-generated |
| source_event_id | Source event identifier if available | From tracker export when present |
| role_id | Related job role | FK to [[DM-MW-001 Job Role Entity]] |
| event_type | Type of event | applied, interview, follow_up, rejected, offer, note |
| event_date | Date event occurred | Required when known |
| event_status | Current status of event | planned, completed, cancelled |
| source | Original source system | Teal, manual, generated |
| notes | Human-readable notes | Optional |
| created_at | Record creation timestamp | System field |
| updated_at | Record update timestamp | System field |

## Relationships

- Tracker Event belongs to one [[DM-MW-001 Job Role Entity]]
- Tracker Event may reference one [[DM-MW-003 Application Package Entity]]
- Tracker Event may support future dashboard timelines

## Related Artifacts

- [[EPIC-MW-001 Career Center Platform]]
- [[REL-MW-0.1 PostgreSQL POC]]
- [[US-MW-003 Load Career System Data]]
- [[US-MW-004 Query Career Data with SQL]]
