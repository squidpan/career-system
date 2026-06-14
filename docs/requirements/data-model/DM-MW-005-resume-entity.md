---
id: DM-MW-005
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
  - resumes
created: 2026-06-14
updated: 2026-06-14
---

# DM-MW-005 Resume Entity

## Purpose

Defines the resume entity used to represent master resumes, ATS resumes, narrative resumes, and tailored resume versions created by Career System.

## Business Context

Career System helps Paul apply to roles by generating application packages. Resumes are core artifacts in that package and must be traceable to job roles and applications.

## Entity Description

A Resume is a generated or maintained document used for applying to one or more roles.

## Candidate Fields

| Field | Description | Notes |
|---|---|---|
| resume_id | Unique internal resume identifier | Motorweb-generated |
| resume_type | Resume type | master, ats, narrative, tailored |
| resume_family | Resume family | BA, SRE, support, hybrid |
| role_id | Related role if tailored | Optional FK to [[DM-MW-001 Job Role Entity]] |
| file_path | Path to resume artifact | Markdown/PDF/text export |
| status | Resume status | draft, reviewed, final, submitted |
| version | Resume version label | v1, v2, etc. |
| created_at | Record creation timestamp | System field |
| updated_at | Record update timestamp | System field |

## Relationships

- Resume may belong to one job role
- Resume may be included in one or more application packages
- Resume is related to [[TERM-CS-005 Resume Version]]

## Related Artifacts

- [[DM-MW-003 Application Package Entity]]
- [[TERM-CS-001 Application Package]]
- [[TERM-CS-005 Resume Version]]
