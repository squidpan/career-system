---
id: DM-MW-006
type: data-model
project: motorweb
epic: EPIC-CS-001
release: future
status: draft
priority: medium
tags:
  - requirements
  - motorweb
  - data-model
  - gap-analysis
created: 2026-06-14
updated: 2026-06-14
---

# DM-MW-006 Gap Analysis Entity

## Purpose

Defines the future gap analysis entity used to evaluate Paul’s fit for a role and support application prioritization.

## Business Context

The primary Career System business goal is to help Paul obtain suitable employment efficiently. Gap Analysis helps decide whether a role is worth pursuing and what preparation is needed.

## Entity Description

A Gap Analysis compares a job role or JD against Paul’s experience, skills, resume evidence, and learning needs.

## Candidate Fields

| Field | Description | Notes |
|---|---|---|
| gap_analysis_id | Unique gap analysis identifier | System-generated |
| role_id | Related job role | FK to [[DM-MW-001 Job Role Entity]] |
| jd_id | Related job description | FK to [[DM-MW-002 Job Description Entity]] |
| fit_score | Overall match score | See [[TERM-CS-006 Fit Score]] |
| strengths | Matching qualifications | Structured text or JSON |
| partial_matches | Areas with partial fit | Structured text or JSON |
| gaps | Missing or weak areas | Structured text or JSON |
| effort_estimate | Estimated effort to close gaps | low, medium, high |
| recommendation | Apply recommendation | apply, maybe, skip |
| created_at | Record creation timestamp | System field |
| updated_at | Record update timestamp | System field |

## Relationships

- Gap Analysis belongs to a job role
- Gap Analysis may reference a job description
- Gap Analysis supports resume tailoring, interview prep, and application prioritization

## Related Artifacts

- [[EPIC-CS-001 Employment Acceleration System]]
- [[TERM-CS-002 Gap Analysis]]
- [[TERM-CS-006 Fit Score]]
