---
id: RTM-CS-MW-001
type: requirements-traceability-matrix
project: career-system
status: draft
priority: high
tags:
  - requirements
  - traceability
  - career-system
  - motorweb
created: 2026-06-14
updated: 2026-06-14
---

# RTM-CS-MW-001 Career System to Motorweb Traceability

## Purpose

This traceability matrix connects Career System business goals to Motorweb solution requirements, technical artifacts, data models, APIs, acceptance criteria, and UAT.

## Traceability Philosophy

```text
Business Goal
  ↓
Business Epic
  ↓
Solution Epic
  ↓
Release
  ↓
Story
  ↓
Data Model / API
  ↓
Acceptance Criteria
  ↓
UAT
  ↓
Implementation
```

## Matrix

| Business Objective | Business Epic | Solution Epic | Release | Story | Data Model | API | AC | UAT |
|---|---|---|---|---|---|---|---|---|
| Help Paul get a job | [[EPIC-CS-001 Employment Acceleration System]] | [[EPIC-MW-001 Career Center Platform]] | [[REL-MW-0.1 PostgreSQL POC]] | [[US-MW-001 PostgreSQL Environment Ready]] | n/a | n/a | [[AC-MW-001]] | [[UAT-MW-001]] |
| Store Career System data in queryable form | [[EPIC-CS-001 Employment Acceleration System]] | [[EPIC-MW-001 Career Center Platform]] | [[REL-MW-0.1 PostgreSQL POC]] | [[US-MW-002 Career Center Database Created]] | [[DM-MW-001 Job Role Entity]] | n/a | [[AC-MW-002]] | [[UAT-MW-002]] |
| Load roles, JDs, and application artifacts | [[EPIC-CS-001 Employment Acceleration System]] | [[EPIC-MW-001 Career Center Platform]] | [[REL-MW-0.1 PostgreSQL POC]] | [[US-MW-003 Load Career System Data]] | [[DM-MW-001 Job Role Entity]], [[DM-MW-002 Job Description Entity]], [[DM-MW-003 Application Package Entity]] | n/a | [[AC-MW-003]] | [[UAT-MW-003]] |
| Query career data for operational decisions | [[EPIC-CS-001 Employment Acceleration System]] | [[EPIC-MW-001 Career Center Platform]] | [[REL-MW-0.1 PostgreSQL POC]] | [[US-MW-004 Query Career Data With SQL]] | [[DM-MW-001 Job Role Entity]], [[DM-MW-004 Tracker Event Entity]], [[DM-MW-006 Gap Analysis Entity]] | future [[API-MW-001 Roles API]] | [[AC-MW-004]] | [[UAT-MW-004]] |
| Expose role data through service contracts | [[EPIC-CS-001 Employment Acceleration System]] | [[EPIC-MW-001 Career Center Platform]] | future REST POC | future story | [[DM-MW-001 Job Role Entity]] | [[API-MW-001 Roles API]] | future AC | future UAT |
| Expose JD data through service contracts | [[EPIC-CS-001 Employment Acceleration System]] | [[EPIC-MW-001 Career Center Platform]] | future REST POC | future story | [[DM-MW-002 Job Description Entity]] | [[API-MW-002 Job Descriptions API]] | future AC | future UAT |
| Expose application packages through service contracts | [[EPIC-CS-001 Employment Acceleration System]] | [[EPIC-MW-001 Career Center Platform]] | future REST POC | future story | [[DM-MW-003 Application Package Entity]] | [[API-MW-003 Application Packages API]] | future AC | future UAT |
| Expose tracker events through service contracts | [[EPIC-CS-001 Employment Acceleration System]] | [[EPIC-MW-001 Career Center Platform]] | future REST POC | future story | [[DM-MW-004 Tracker Event Entity]] | [[API-MW-004 Tracker Events API]] | future AC | future UAT |

## Review Notes

This matrix should be updated whenever a story, data model, API artifact, AC, or UAT artifact is added.
