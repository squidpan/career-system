---
id: US-CS-057
project: career-system
type: user-story
status: completed

categories:
  - "[[Stories]]"
  - "[[Requirements]]"

tags:
  - recovery
  - application-package
  - ats
  - regression

description: Restore generation of complete validated Career System Application Packages.

created: 2026-07-14
updated: 2026-07-16
---

# US-CS-057 Restore Final Application Package Generation

## TL;DR

- Restore complete Application Package generation.
- Produce all expected deliverables.
- Eliminate manual package reconstruction.
- Preserve historical package quality.
- Establish the Application Package as the operational output of the workflow.

---

# User Story

As a Career System operator,

I want the pipeline to automatically generate a complete Application Package,

so that every imported Job Description results in a submission-ready set of validated application artifacts.

---

# Business Context

The Application Package is the final product delivered by Career System.

Although many upstream processing stages exist, the operational workflow is not complete unless all required application artifacts are generated consistently.

Historically validated LSEG and Broadridge packages define the expected quality and structure.

---

# Current State

Phase 1 regression validation confirmed that the existing final-mile generators and Application Package builder reproduce the LSEG and Broadridge core artifacts byte-for-byte when valid Application Summary and targeted FRBNY section inputs already exist.

The remaining recovery gap is upstream:

- generate a valid Application Summary
- generate a valid targeted FRBNY section
- pass those artifacts into the proven final-mile workflow
- reject or clearly report incomplete package assembly

Recovery therefore requires restoring the bridge into final-mile generation and enforcing package completeness rather than rewriting the validated final-mile scripts.

---

# Business Value

Successful restoration will:

- Eliminate manual package assembly.
- Restore repeatable application preparation.
- Improve confidence in generated deliverables.
- Reduce operational effort during job applications.

---

# Scope

## Included

- Package generation
- Manifest generation
- ATS resume generation
- Full resume generation
- Submission notes
- Package validation

## Excluded

- Resume rewriting
- New package features
- Interview preparation enhancements

---

# Dependencies

- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]]
- [[US-CS-056-restore-end-to-end-workflow-orchestration]]
- [[US-CS-RECOVERY-001-reconnect-new-pipeline-to-application-package]]

---

# Acceptance Criteria

- A valid Application Summary is available for final-mile generation.
- A valid targeted FRBNY section is available for final-mile generation.
- The proven ATS and full-resume generators consume those bridge artifacts without manual reconstruction.
- The canonical Application Package directory is created.
- Required ATS Markdown, HTML, and text artifacts are produced.
- Required full-resume Markdown and HTML artifacts are produced.
- `application-summary.md`, `package-manifest.json`, `README.md`, and `submission-notes.md` are present and non-empty.
- Missing required source artifacts cause a detectable failure or an explicit incomplete-package result.
- Package generation does not silently report success for an incomplete required deliverable.
- Existing validated final-mile scripts remain unchanged unless regression evidence demonstrates a defect.

---

# Implementation Notes

The final-mile bridge was restored using approved Resume Assets selected
deterministically from normalized JD role-family metadata.

The selector publishes the legacy-compatible bridge artifacts consumed by
the existing final-mile generators:

- `data/application-summaries/<job-slug>-summary-v1.md`
- `data/resume-sections/<job-slug>-frbny-section.md`

The first artifact remains named `application-summary.md` inside the
Application Package for compatibility, although its resume-content meaning
is Professional Summary.

Application Package generation was updated to support isolated input and
output roots and to validate all required source artifacts before package
creation.

Implemented components:

- `scripts/select_resume_assets.py`
- `bin/run-resume-asset-selection.sh`
- `bin/run-resume-final-mile-from-jd.sh`
- `scripts/build_application_package.py`
- `bin/run-application-package.sh`
- `bin/run-jd-to-application-package.sh`

Required package source artifacts are validated before the package
directory is created.

Primary implementation commits:

- `e3d2194` — Add deterministic Resume Asset selector
- `467c514` — Add Resume Asset selection wrapper
- `4b1e45c` — Add final-mile resume orchestration from normalized JD
- `9799cd0` — Support isolated Application Package generation
- `97c4bd9` — Require complete Application Package inputs
- `8530621` — Add JD-to-Application Package orchestration

---

# Validation

## Manual Validation

Complete Application Packages were generated in isolated `/tmp` roots for:

- LSEG Senior Business Analyst
- Broadridge Product Analyst
- Citi Application and Production Support

Each generated package contained the required core files:

- `application-summary.md`
- `full-resume.md`
- `full-resume.html`
- `ats-resume.md`
- `ats-resume.html`
- `ats-resume.txt`
- `submission-notes.md`
- `README.md`
- `package-manifest.json`

## Programmatic Validation

Validation confirmed:

- required files were present and non-empty
- expected package directory structure was produced
- package manifest recorded copied and optional artifacts
- isolated input and output roots worked correctly
- missing required sources caused a nonzero exit status
- no partial package directory was created after preflight failure

## Regression Validation

The six core resume artifacts generated for LSEG and Broadridge were
compared byte-for-byte with their existing validated Application Packages.

Results:

- LSEG: 6 of 6 matched — PASS
- Broadridge: 6 of 6 matched — PASS
- missing ATS text preflight test — PASS
- partial-package prevention — PASS

Detailed evidence is recorded in:

- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-ARCHITECTURE]]

---

# Learning Outcomes

## Technical

Improve understanding of final package generation.

## Engineering

Improve validation of operational deliverables.

## Operational

Reduce manual work required to prepare job applications.

---

# Framework Improvement Opportunities

Candidate EFK improvements:

- Package validation patterns
- Operational deliverable validation
- Artifact completeness verification

---

# Related Artifacts

- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]]
- [[US-CS-056-restore-end-to-end-workflow-orchestration]]
- [[US-CS-058-regression-validation-against-historical-application-packages]]

---

# References

- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-ARCHITECTURE]]
- [[RECOVERY-JOURNAL]]
- LSEG regression package
- Broadridge regression package
- Existing Application Package documentation

---

# Notes

This story restored the complete operational deliverable produced by
Career System.

Completion status:

- legacy-compatible bridge restored
- Full Resume generation complete
- ATS Resume generation complete
- HTML and ATS text export complete
- required package validation complete
- incomplete-package protection complete
- isolated package generation complete
- regression evidence documented

Optional recommendation and interview artifacts remain optional and do
not prevent generation of the required core Application Package.
