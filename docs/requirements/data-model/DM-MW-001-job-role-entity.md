---
id: DM-MW-001
type: data-model
project: motorweb
status: draft
priority: high
tags:
  - requirements
  - data-model
  - job-role
created: 2026-06-14
updated: 2026-06-14
---

# DM-MW-001 Job Role Entity

## Purpose

Represents a job opportunity being tracked by Career System and exposed through Motorweb Career Center.

## Business Meaning

A Job Role is the central object in the job-search workflow. It connects the job posting, job description, gap analysis, resume version, application package, application events, and interview preparation.

## Candidate Fields

| Field | Description |
|---|---|
| role_id | Internal Career Center role identifier |
| source_role_id | Identifier from original source where available |
| company | Hiring company or client |
| title | Role title as captured from source |
| normalized_title | Normalized title used for grouping/search |
| role_family | BA, SRE, PM, App Support, etc. |
| role_level | Senior, Lead, Junior, etc. |
| source | Teal, LinkedIn, Indeed, Dice, ZipRecruiter, manual, etc. |
| status | tracked, apply, applied, interviewing, skipped, closed, etc. |
| fit_score | Future fit score from gap analysis |
| recommendation | apply, maybe, skip, research |
| created_date | Date role was first captured |
| updated_date | Date role was last updated |

## Relationships

- Job Role may have one or more Job Descriptions.
- Job Role may have zero or more Job Events.
- Job Role may have zero or more Application Packages.
- Job Role may have zero or more Resume Versions.
- Job Role may have zero or one current Gap Analysis Report.

## Related Requirements

- [[US-MW-003 Load Career System Data]]
- [[US-MW-004 Query Career Data with SQL]]
- [[TERM-CS-003 Job Role]]
