---
id: DM-MW-002
type: data-model
project: motorweb
status: draft
priority: high
tags:
  - requirements
  - data-model
  - job-description
created: 2026-06-14
updated: 2026-06-14
---

# DM-MW-002 Job Description Entity

## Purpose

Represents a raw or normalized job description associated with a tracked job role.

## Business Meaning

A Job Description provides the source evidence used to decide whether to apply, generate a tailored resume, produce gap analysis, recommend skills, and prepare for interviews.

## Candidate Fields

| Field | Description |
|---|---|
| jd_id | Internal job description identifier |
| role_id | Associated job role identifier |
| source | LinkedIn, Indeed, Monster, ZipRecruiter, Dice, manual, etc. |
| source_url | Original posting URL where available |
| raw_file_path | Path to raw JD file |
| normalized_file_path | Path to normalized JD file |
| company | Company name extracted from JD |
| title | Title extracted from JD |
| location | Location or remote/hybrid information |
| employment_type | Full-time, contract, hybrid, etc. |
| captured_date | Date JD was captured |
| normalized_date | Date JD was normalized |
| status | raw, normalized, reviewed, archived |

## Relationships

- Job Description belongs to one Job Role.
- Job Description may drive one Gap Analysis Report.
- Job Description may drive one or more Resume Versions.
- Job Description may drive one Application Package.

## Related Requirements

- [[US-MW-003 Load Career System Data]]
- [[US-MW-004 Query Career Data with SQL]]
- [[TERM-CS-004 Job Description]]
