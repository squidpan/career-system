---
id: IMPLEMENTATION-ORDER-v0.4
type: implementation-order
project: career-system
status: in-progress
priority: high
tags: [requirements, implementation-order]
created: 2026-06-14
updated: 2026-07-16
---

# Mini-v0.4 Implementation Order

## Recovery Checkpoint — Functional Recovery Completed

Epic:

- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]] — completed

Completed recovery stories:

- [[US-CS-056-restore-end-to-end-workflow-orchestration]]
- [[US-CS-057-restore-final-application-package-generation]]
- [[US-CS-058-regression-validation-against-historical-application-packages]]
- [[US-CS-059-operational-verification-and-recovery-runbook]]
- [[US-CS-060-recovery-traceability-and-implementation-updates]]

Recovered operational boundary:

    normalized JD
        to deterministic Resume Asset selection
        to Full Resume and ATS Resume generation
        to HTML and ATS text export
        to complete Application Package

Validation status:

- LSEG six-artifact regression — PASS
- Broadridge six-artifact regression — PASS
- required-input failure validation — PASS
- partial-package prevention — PASS
- operational runbook — complete

Recovery evidence:

- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-ARCHITECTURE]]
- [[RECOVERY-JOURNAL]]
- [[RECOVERY-ATS-APPLICATION-PACKAGE-WORKFLOW-2026-07-01]]

Recovery closeout status:

- US-CS-060 — completed
- RTM-CS-002 — completed
- sprint closeout — completed
- superseded recovery Epic draft stash — removed
- Resume Asset standard draft — explicitly carried forward for EFK review
- EPIC-CS-003 — completed

Recovery closeout evidence:

- [[RTM-CS-002-functional-recovery]]
- [[SPRINT-2026-07-functional-recovery-closeout]]

Resume work from the existing active quality and operational priorities
below.

## P0 - Fix Application Package Quality Defects

- [[BUG-CS-001 Professional Summary overwritten by Application Summary Fit Analysis content]]
- [[BUG-CS-004 submission-notes.md template inconsistent across packages]]
- [[BUG-CS-006 JD normalizer creates unknown-company unknown-role normalized files]]
- [[BUG-CS-008 Application package generated from wrong source artifact type]]

## P1 - COMPLETED - Stabilize Career System Operational Tracker

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
