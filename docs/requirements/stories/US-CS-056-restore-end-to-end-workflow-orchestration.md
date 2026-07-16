---
id: US-CS-056
project: career-system
type: user-story
status: completed

categories:
  - "[[Stories]]"
  - "[[Requirements]]"

tags:
  - recovery
  - orchestration
  - pipeline
  - application-package

description: Restore orchestration of the complete Career System JD-to-Application Package workflow.

created: 2026-07-14
updated: 2026-07-16
---

# US-CS-056 Restore End-to-End Workflow Orchestration

## TL;DR

- Restore the complete operational workflow.
- Reconnect all existing pipeline stages.
- Eliminate manual transitions between stages.
- Produce a repeatable workflow suitable for operational use.
- Establish the foundation for subsequent recovery stories.

---

# User Story

As a Career System operator,

I want the complete JD-to-Application Package workflow to execute as a single orchestrated process,

so that imported job descriptions consistently produce validated application packages with minimal manual intervention.

---

# Business Context

Career System contains mature implementations of many individual processing stages.

Over time those stages evolved independently, resulting in an operational workflow that no longer executes end-to-end without manual intervention.

Recovery requires reconnecting those stages before additional enhancements can be safely introduced.

---

# Current State

Repository reconnaissance confirmed that the following pipeline stages already exist:

- JD Normalization
- Candidate Intelligence
- Candidate Recommendation
- Resume Tailoring
- Resume Enhancement
- Application Summary
- ATS Resume
- Full Resume
- Application Package

The primary recovery objective is orchestration rather than redevelopment.

---

# Business Value

Successful orchestration will:

- Restore operational productivity.
- Reduce manual recovery work.
- Improve repeatability.
- Reduce regression risk.
- Enable reliable application package generation.

---

# Scope

## Included

- Pipeline sequencing
- Stage integration
- Artifact handoffs
- Workflow validation
- Operational execution

## Excluded

- Resume content redesign
- New application features
- Repository-wide refactoring
- EFK improvements

---

# Dependencies

- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]]
- [[CTX-CS-001-employment-acceleration-system]]
- [[RECOVERY-REQUIREMENTS-RECONNAISSANCE-2026-07-14]]

---

# Acceptance Criteria

- The workflow executes from imported JD through Application Package.
- Every expected pipeline stage executes exactly once.
- Expected artifacts are generated at every stage.
- Artifact handoffs occur without manual reconstruction.
- Pipeline failures are detectable.
- Workflow can be repeated using multiple regression job descriptions.

---

# Implementation Notes

The existing final-mile generators were preserved and reconnected through
deterministic Resume Asset selection and new orchestration wrappers.

Implemented components:

- `scripts/select_resume_assets.py`
- `bin/run-resume-asset-selection.sh`
- `bin/run-resume-final-mile-from-jd.sh`
- `bin/run-jd-to-application-package.sh`

The recovered orchestration begins from a normalized JD and performs:

- role-family Resume Asset selection
- Professional Summary publication
- FRBNY experience-section publication
- Full Resume generation
- ATS Resume generation
- HTML export
- ATS text export
- Application Package generation

Primary implementation commits:

- `e3d2194` — Add deterministic Resume Asset selector
- `467c514` — Add Resume Asset selection wrapper
- `4b1e45c` — Add final-mile resume orchestration from normalized JD
- `8530621` — Add JD-to-Application Package orchestration

---

# Validation

## Manual Validation

The recovered workflow was executed in isolated `/tmp` output roots using:

- LSEG Senior Business Analyst
- Broadridge Product Analyst
- Citi Application and Production Support

Each run completed from normalized JD through final Application Package.

## Programmatic Validation

Validation confirmed:

- deterministic role-family routing
- expected bridge artifacts
- expected Full Resume and ATS Resume outputs
- HTML and ATS text exports
- required package filenames
- expected directory structure
- successful nonzero failure behavior for missing required inputs

## Regression Validation

LSEG and Broadridge were regenerated in isolated output directories.

For each role, these six core artifacts were compared byte-for-byte with
the existing validated Application Package:

- `application-summary.md`
- `full-resume.md`
- `full-resume.html`
- `ats-resume.md`
- `ats-resume.html`
- `ats-resume.txt`

Results:

- LSEG: 6 of 6 matched — PASS
- Broadridge: 6 of 6 matched — PASS

Detailed evidence is recorded in:

- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-ARCHITECTURE]]

---

# Learning Outcomes

## Technical

Improve understanding of workflow orchestration across multiple independent pipeline stages.

## Engineering

Improve recovery planning and validation methodology.

## Operational

Produce a repeatable operational workflow suitable for daily job applications.

---

# Framework Improvement Opportunities

Candidate observations for future EFK work:

- Workflow orchestration guidance
- Operational recovery patterns
- Pipeline validation patterns

These improvements remain outside the scope of this story.

---

# Related Artifacts

- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]]
- [[US-CS-057-restore-final-application-package-generation]]
- [[CTX-CS-001-employment-acceleration-system]]
- [[RECOVERY-REQUIREMENTS-RECONNAISSANCE-2026-07-14]]

---

# References

- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-ARCHITECTURE]]
- [[RECOVERY-JOURNAL]]
- LSEG regression package
- Broadridge regression package
- Recovery planning documentation

---

# Notes

This story restored orchestration of existing capabilities without replacing
the verified final-mile generators.

Completion boundary:

- orchestration begins from a normalized JD
- raw JD capture and normalization remain upstream workflow steps
- production-package regeneration and visual review remain operational confirmation activities

Completion status:

- implementation complete
- isolated execution complete
- regression validation complete
- recovery evidence documented
