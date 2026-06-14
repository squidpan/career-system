---
id: DM-MW-003
type: data-model
project: motorweb
status: draft
priority: high
tags:
  - requirements
  - data-model
  - application-package
created: 2026-06-14
updated: 2026-06-14
---

# DM-MW-003 Application Package Entity

## Purpose

Represents the complete set of generated artifacts used to apply for a specific job role.

## Business Meaning

The Application Package is the final job-application output of Career System. It should help Paul apply faster and better by bundling role-specific documents and preparation materials.

## Candidate Fields

| Field | Description |
|---|---|
| application_package_id | Internal identifier |
| role_id | Associated job role |
| jd_id | Associated job description |
| resume_version_id | Associated tailored resume |
| cover_letter_id | Associated cover letter where available |
| gap_analysis_id | Associated gap analysis report where available |
| interview_prep_id | Associated interview prep artifact where available |
| package_path | File-system path to generated package |
| status | generated, reviewed, applied, archived |
| generated_date | Date package was generated |
| updated_date | Date package was updated |

## Relationships

- Application Package belongs to one Job Role.
- Application Package may reference one Job Description.
- Application Package may reference one Resume Version.
- Application Package may reference one Gap Analysis Report.
- Application Package may reference one Interview Prep artifact.

## Related Requirements

- [[US-MW-003 Load Career System Data]]
- [[US-MW-004 Query Career Data with SQL]]
- [[TERM-CS-001 Application Package]]
