---
id: US-CS-058
project: career-system
type: user-story
status: completed

categories:
  - "[[Stories]]"
  - "[[Requirements]]"

tags:
  - recovery
  - regression
  - validation
  - application-package

description: Validate recovered Career System output against historical production-quality application packages.

created: 2026-07-15
updated: 2026-07-16
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
- [[US-CS-056-restore-end-to-end-workflow-orchestration]]
- [[US-CS-057-restore-final-application-package-generation]]

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

Regression validation was implemented using isolated generation roots under
`/tmp` so the repository baselines remained unchanged during testing.

The recovered workflow regenerated complete Application Packages from the
normalized JDs for:

- LSEG Senior Business Analyst
- Broadridge Product Analyst

Initial validation identified intentional content differences caused by
default-derived Resume Assets.

Those differences were reviewed and resolved by promoting the validated
historical content into role-family assets:

- LSEG content became the validated BA profile
- Broadridge content became the validated Product profile
- Eclaro-derived content remained the validated Support profile

The selector was updated to route Product roles to Product assets rather
than the Default profile.

The core comparison set was:

- `application-summary.md`
- `ats-resume.md`
- `ats-resume.html`
- `ats-resume.txt`
- `full-resume.md`
- `full-resume.html`

Core artifacts were compared using byte-for-byte file comparison.

Package metadata and operational files were validated by structure,
required content, non-empty status, and manifest completeness.

Primary implementation commit:

- `8c5ef6b` — Add validated BA and Product Resume Asset profiles

---

# Validation

## Manual Validation

Generated packages were reviewed for:

- package structure
- Professional Summary content
- FRBNY experience content
- ATS and Full Resume generation
- manifest presence
- submission-notes presence
- role-family routing

Routing results:

- LSEG: `role_family: ba`, `content_profile: ba`, no fallback
- Broadridge: `role_family: product`, `content_profile: product`, no fallback

## Programmatic Validation

Both generated packages contained all nine required package files:

- `application-summary.md`
- `full-resume.md`
- `full-resume.html`
- `ats-resume.md`
- `ats-resume.html`
- `ats-resume.txt`
- `submission-notes.md`
- `README.md`
- `package-manifest.json`

Validation also confirmed:

- expected directory structure
- non-empty required artifacts
- successful orchestration completion
- clean repository state after isolated generation
- concise failure reporting for a missing required source
- no partial package directory after preflight failure

## Regression Validation

The six core artifacts for each regenerated package were compared
byte-for-byte against the existing validated baselines.

Results:

- LSEG: 6 of 6 matched — PASS
- Broadridge: 6 of 6 matched — PASS
- remaining LSEG differences: none
- remaining Broadridge differences: none
- missing ATS text negative test: PASS
- partial-package prevention: PASS

Recovery regression criteria are satisfied.

Detailed evidence is recorded in:

- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-ARCHITECTURE]]
- [[RECOVERY-JOURNAL]]

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
- [[US-CS-056-restore-end-to-end-workflow-orchestration]]
- [[US-CS-057-restore-final-application-package-generation]]
- [[US-CS-059-operational-verification-and-recovery-runbook]]

---

# References

- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-ARCHITECTURE]]
- [[RECOVERY-JOURNAL]]
- LSEG application package
- Broadridge application package

---

# Notes

Regression validation defined the objective completion criterion for the
functional recovery.

Completion status:

- LSEG package regenerated successfully
- Broadridge package regenerated successfully
- package completeness validated
- deterministic role-family routing validated
- 12 of 12 core artifact comparisons passed
- failure-path behavior validated
- no unexplained differences remain

Future enhancements should extend this regression suite rather than
replacing the LSEG and Broadridge baselines.
