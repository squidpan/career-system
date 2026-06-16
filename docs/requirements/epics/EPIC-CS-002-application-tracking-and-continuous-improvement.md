---
id: EPIC-CS-002
type: epic
project: career-system
status: draft
priority: high
tags: [requirements, career-system, application-tracking, continuous-improvement]
created: 2026-06-14
updated: 2026-06-14
---

# EPIC-CS-002 Application Tracking and Continuous Improvement

## Business Objective

Create a reliable Career System application tracking capability that records applications, statuses, submission notes, outcomes, and operational issues discovered while applying for jobs.

## Business Rationale

Career System is now being used operationally. Application history must become structured, traceable, and reusable so the system improves over time.

## In Scope

- Application tracker foundation
- Canonical application status lifecycle
- Submission notes standardization
- Fit analysis separation from resume-ready content
- Approved resume fact preservation
- JD normalization defects related to unknown company and role
- Application tracker update workflow

## Out of Scope

- REST API implementation
- React UI
- PostgreSQL implementation details
- Automated Trello/Jira integration

## Success Criteria

- Application tracker is the operational source for application status.
- Every application status has a canonical meaning.
- Generated packages preserve approved resume facts.
- Application package defects are tracked as formal bug stories.
- Application data is ready to become the first Motorweb PostgreSQL POC dataset.

## Related Artifacts

- [[BR-CS-002 Application Package Quality Improves Over Time]]
- [[CTX-CS-001 Employment Acceleration System]]
