---
id: US-CS-059
project: career-system
type: user-story
status: completed

categories:
  - "[[Stories]]"
  - "[[Requirements]]"

tags:
  - recovery
  - operations
  - runbook
  - verification

description: Verify that Career System can be operated end-to-end using documented recovery procedures.

created: 2026-07-15
updated: 2026-07-16
---

# US-CS-059 Operational Verification and Recovery Runbook

## TL;DR

- Verify Career System is operational after recovery.
- Execute the complete workflow using documented procedures.
- Confirm recovery is repeatable by following the runbook.
- Establish operational acceptance criteria.
- Define the transition from recovery planning to implementation.

---

# User Story

As a Career System operator,

I want to verify the recovered workflow using documented operational procedures,

so that the system can be used confidently for real job applications.

---

# Business Context

Recovery is not complete simply because individual scripts execute successfully.

The complete operational workflow must be executable using documented procedures without relying on undocumented knowledge or manual reconstruction.

---

# Current State

Recovery planning has defined the target workflow, recovery stories, and regression validation strategy.

Operational verification will confirm that the restored workflow functions as a complete, repeatable process.

---

# Business Value

Operational verification will:

- Demonstrate recovery success.
- Improve operational confidence.
- Reduce dependence on tribal knowledge.
- Provide a repeatable recovery process for future releases.

---

# Scope

## Included

- End-to-end workflow execution
- Recovery checklist
- Runbook verification
- Operational readiness
- Recovery acceptance review

## Excluded

- New feature development
- Architecture redesign
- Workflow optimization beyond recovery

---

# Dependencies

- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]]
- [[US-CS-056-restore-end-to-end-workflow-orchestration]]
- [[US-CS-057-restore-final-application-package-generation]]
- [[US-CS-058-regression-validation-against-historical-application-packages]]

---

# Acceptance Criteria

- The documented workflow can be executed from Job Description through Application Package.
- Required recovery runbooks are complete and current.
- Recovery checklist is executed successfully.
- Regression validation has passed.
- No undocumented manual recovery steps remain.
- Recovery completion can be demonstrated by following the documented procedures alone.

---

# Implementation Notes

The existing recovery workflow document was converted into the current
operational runbook:

- [[RECOVERY-ATS-APPLICATION-PACKAGE-WORKFLOW-2026-07-01]]

The runbook now documents:

- repository safety checks
- normalized-JD entry boundary
- primary orchestration command
- isolated `/tmp` validation
- expected bridge and final-mile artifacts
- required Application Package files
- completion verification
- LSEG and Broadridge regression comparison
- missing-input failure behavior
- partial-package prevention
- production-regeneration safeguards
- known operational limitations
- operational exit criteria

The implemented workflow remains intentionally bounded at normalized JD
input. Raw capture and normalization remain documented upstream steps.

---

# Validation

## Manual Validation

The documented orchestration procedure was exercised using isolated
output roots for:

- LSEG Senior Business Analyst
- Broadridge Product Analyst
- Citi Application and Production Support

The procedure generated complete Application Packages without modifying
the repository baselines.

## Programmatic Validation

Validation confirmed:

- required bridge artifacts were generated
- Full Resume and ATS Resume artifacts were generated
- HTML and ATS text exports were generated
- all nine required package files were present and non-empty
- missing required input produced a nonzero exit status
- missing input was identified clearly
- no partial package directory was created
- isolated validation left the repository unchanged

## Operational Validation

The operational runbook now contains the commands, safeguards, expected
outputs, failure behavior, and verification steps required to repeat the
normalized-JD-to-Application-Package workflow.

Operational result:

- documented workflow execution: PASS
- regression validation: PASS
- failure-path validation: PASS
- partial-package prevention: PASS
- operational documentation: COMPLETE

---

# Operational Exit Criteria

Operational recovery exit criteria were evaluated as follows:

- normalized-JD-to-Application-Package workflow executes successfully — PASS
- US-CS-058 regression validation passed — PASS
- recovery runbook describes the implemented workflow — PASS
- final-mile manual reconstruction is no longer required — PASS
- required recovery implementation artifacts are documented — PASS
- isolated execution preserves repository state — PASS
- failure behavior is documented and validated — PASS

Upstream raw JD capture and normalization remain separate documented
workflow stages rather than undocumented recovery steps.

Completion of this story represents operational acceptance rather than
new feature completion.

---

# Learning Outcomes

## Technical

Improve confidence in the operational workflow.

## Engineering

Strengthen operational documentation and recovery discipline.

## Operational

Establish a repeatable recovery process for future maintenance.

---

# Framework Improvement Opportunities

Potential future EFK improvements:

- Operational readiness checklist
- Recovery acceptance template
- Standard operational verification artifact

---

# Related Artifacts

- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]]
- [[US-CS-058-regression-validation-against-historical-application-packages]]
- [[US-CS-060-recovery-traceability-and-implementation-updates]]

---

# References

- [[RECOVERY-ATS-APPLICATION-PACKAGE-WORKFLOW-2026-07-01]]
- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-ARCHITECTURE]]
- [[RECOVERY-JOURNAL]]
- Operational branch history

---

# Notes

Completion status:

- functional workflow verified
- operational runbook completed
- isolated execution verified
- package completeness verified
- regression validation verified
- failure behavior verified
- production safeguards documented

This story completes operational verification and prepares the recovery
effort for traceability and sprint closeout.
