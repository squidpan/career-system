---
id: US-CS-058
project: career-system
type: user-story
status: draft

categories:
  - [[Stories]]
  - [[Requirements]]

tags:
  - recovery
  - regression
  - validation
  - application-package

description: Validate recovered Career System output against historical production-quality application packages.

created: 2026-07-15
updated: 2026-07-15
---

# US-CS-058 Regression Validation Against Historical Application Packages

## TL;DR

- Define objective recovery validation.
- Use LSEG and Broadridge as canonical regression packages.
- Verify package completeness before implementation is considered complete.
- Distinguish intentional improvements from regressions.
- Establish repeatable validation for future releases.

---

# User Story

As a Career System operator,

I want every recovery change to be validated against previously successful application packages,

so that pipeline improvements do not unintentionally reduce application quality.

---

# Business Context

Career System has already produced successful application packages used for real job applications.

These packages represent proven operational output and provide an objective baseline for validating recovery work.

Without regression validation, future fixes could unknowingly degrade resume quality, package completeness, or operational behavior.

---

# Current State

Phase 1 recovery planning identified the LSEG Senior Business Analyst and Broadridge Product Analyst application packages as the primary regression baselines.

Recovery implementation must demonstrate that the restored pipeline produces equivalent operational results.

---

# Business Value

Regression validation will:

- Prevent accidental degradation.
- Increase confidence in recovery changes.
- Provide measurable completion criteria.
- Enable future enhancements with lower risk.

---

# Scope

## Included

- Regression package selection
- Validation checklist
- Artifact comparison
- Package completeness verification
- Acceptance documentation

## Excluded

- New package features
- Resume content optimization
- Interview recommendation enhancements

---

# Dependencies

- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]]
- [[US-CS-056]]
- [[US-CS-057]]

---

# Acceptance Criteria

- LSEG package is regenerated successfully.
- Broadridge package is regenerated successfully.
- Required artifacts exist in both packages.
- Directory structures match the canonical layout.
- ATS resume artifacts are generated.
- Full resume artifacts are generated.
- Package manifest is complete.
- Submission notes are present.
- Unchanged regression inputs reproduce the validated core artifacts byte-for-byte.
- Any intentional difference is documented with its source, rationale, and approval result.
- Differences are documented as either intentional improvements or regressions.
- Recovery is not considered complete until regression validation passes.

---

# Implementation Notes

For unchanged regression inputs and validated final-mile scripts, the core generated artifacts should match the canonical LSEG and Broadridge baselines byte-for-byte.

The core comparison set is:

- `application-summary.md`
- `ats-resume.md`
- `ats-resume.html`
- `ats-resume.txt`
- `full-resume.md`
- `full-resume.html`

When recovery intentionally changes an upstream bridge artifact, any resulting difference must be reviewed, documented, and classified as an approved improvement or a regression.

Package metadata and operational files that are expected to change between executions should be validated by structure, required content, and completeness rather than checksum alone.

---

# Validation

## Manual Validation

Review:

- package structure
- resume quality
- application summary
- manifest
- submission notes

## Programmatic Validation

Verify:

- required files
- directory structure
- manifest entries
- artifact counts
- required metadata

## Regression Validation

Compare regenerated packages against:

- LSEG Senior Business Analyst
- Broadridge Product Analyst

Document all intentional differences.

---

# Learning Outcomes

## Technical

Improve repeatable validation of document-generation pipelines.

## Engineering

Strengthen regression discipline before introducing enhancements.

## Operational

Provide objective evidence that recovery is complete.

---

# Framework Improvement Opportunities

Potential future EFK improvements:

- Regression-validation template
- Engineering validation checklist
- Golden-reference artifact pattern

---

# Related Artifacts

- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]]
- [[US-CS-056]]
- [[US-CS-057]]
- [[US-CS-059]]

---

# References

- LSEG application package
- Broadridge application package
- Recovery validation documentation

---

# Notes

Regression validation defines the completion criteria for operational recovery.

Future enhancements should extend this regression suite rather than replacing it.
