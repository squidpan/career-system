---
id: INDEX-CS-MW-v0.4
type: index
project: career-system
status: draft
priority: high
tags: [requirements, index, career-center]
created: 2026-06-14
updated: 2026-06-14
---

# Career Center v0.4 Requirements Index

## Epics

- [[EPIC-CS-002 Application Tracking and Continuous Improvement]]
- [[EPIC-MW-002 Motorweb Career Center PostgreSQL POC]]

## Career System Stories

- [[US-CS-041 Application Tracker Foundation]]
- [[US-CS-042 Standardize Submission Notes Format]]
- [[US-CS-043 Normalize Application Status Lifecycle]]
- [[US-CS-044 Detect Unknown Company During JD Normalization]]
- [[US-CS-045 Detect Unknown Role During JD Normalization]]
- [[US-CS-046 Separate Fit Analysis from Professional Summary]]
- [[US-CS-047 Preserve Approved Resume Experience Facts]]
- [[US-CS-048 Application Tracker Update Workflow]]

## Motorweb PostgreSQL POC Stories

- [[US-MW-020 Create Local career_center PostgreSQL Database]]
- [[US-MW-021 Create Application Status Reference Table]]
- [[US-MW-022 Create Application Table]]
- [[US-MW-023 Load Career System applications.csv]]
- [[US-MW-024 Query Applications by Status]]
- [[US-MW-025 Query Applications by Company and Date]]
- [[US-MW-026 Validate Career System CSV Matches PostgreSQL Rows]]

## Bug Stories

- [[BUG-CS-001 Professional Summary overwritten by Application Summary Fit Analysis content]]
- [[BUG-CS-002 PlanetCAD client references lost or attributed incorrectly]]
- [[BUG-CS-003 Real-time streaming market data wording lost during tailoring enhancement]]
- [[BUG-CS-004 submission-notes.md template inconsistent across packages]]
- [[BUG-CS-005 Application status requires manual update in multiple locations]]
- [[BUG-CS-006 JD normalizer creates unknown-company unknown-role normalized files]]
- [[BUG-CS-007 JD normalizer run_id polluted with source file path]]
- [[BUG-CS-008 Application package generated from wrong source artifact type]]

## Planning

- [[IMPLEMENTATION-ORDER-v0.4]]
- [[RTM-CS-MW-v0.4 Career Center Traceability]]
