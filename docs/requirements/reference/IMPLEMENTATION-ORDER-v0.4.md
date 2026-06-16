---
id: IMPLEMENTATION-ORDER-v0.4
type: implementation-order
project: career-system
status: draft
priority: high
tags: [requirements, implementation-order]
created: 2026-06-14
updated: 2026-06-14
---

# Mini-v0.4 Implementation Order

## P0 - Fix Application Package Quality Defects

- [[BUG-CS-001 Professional Summary overwritten by Application Summary Fit Analysis content]]
- [[BUG-CS-004 submission-notes.md template inconsistent across packages]]
- [[BUG-CS-006 JD normalizer creates unknown-company unknown-role normalized files]]
- [[BUG-CS-008 Application package generated from wrong source artifact type]]

## P1 - Stabilize Career System Operational Tracker

- [[US-CS-041 Application Tracker Foundation]]
- [[US-CS-042 Standardize Submission Notes Format]]
- [[US-CS-043 Normalize Application Status Lifecycle]]
- [[US-CS-048 Application Tracker Update Workflow]]
- [[BUG-CS-005 Application status requires manual update in multiple locations]]

## P2 - Preserve Resume and JD Quality

- [[BUG-CS-002 PlanetCAD client references lost or attributed incorrectly]]
- [[BUG-CS-003 Real-time streaming market data wording lost during tailoring enhancement]]
- [[US-CS-046 Separate Fit Analysis from Professional Summary]]
- [[US-CS-047 Preserve Approved Resume Experience Facts]]

## P3 - Prepare Motorweb PostgreSQL POC

- [[US-MW-020 Create Local career_center PostgreSQL Database]]
- [[US-MW-021 Create Application Status Reference Table]]
- [[US-MW-022 Create Application Table]]
- [[US-MW-023 Load Career System applications.csv]]

## P4 - Validate Motorweb SQL Dashboard Queries

- [[US-MW-024 Query Applications by Status]]
- [[US-MW-025 Query Applications by Company and Date]]
- [[US-MW-026 Validate Career System CSV Matches PostgreSQL Rows]]
