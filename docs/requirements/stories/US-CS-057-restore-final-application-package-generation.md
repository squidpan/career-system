---
id: US-CS-057
project: career-system
type: user-story
status: draft

categories:
  - [[Stories]]
  - [[Requirements]]

tags:
  - recovery
  - application-package
  - ats
  - regression

description: Restore generation of complete validated Career System Application Packages.

created: 2026-07-14
updated: 2026-07-14
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
- [[US-CS-056]]
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

Focus on restoring the bridge into the validated final-mile workflow and enforcing required package completeness before introducing enhancements.

Historical application packages remain the regression baseline.

---

# Validation

## Manual Validation

Generate packages for:

- LSEG Senior Business Analyst
- Broadridge Product Analyst

Confirm package completeness.

## Programmatic Validation

Verify:

- expected files
- expected directory layout
- manifest integrity
- artifact counts

## Regression Validation

Compare generated packages with previously validated historical packages.

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
- [[US-CS-056]]
- [[US-CS-058]]

---

# References

- LSEG regression package
- Broadridge regression package
- Existing Application Package documentation

---

# Notes

This story restores the operational deliverable produced by Career System.

Completion of this story establishes the foundation for formal regression validation in the following recovery story.
