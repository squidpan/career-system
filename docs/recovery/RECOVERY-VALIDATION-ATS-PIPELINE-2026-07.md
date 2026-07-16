---
id: RECOVERY-VALIDATION-ATS-PIPELINE-2026-07
project: career-system
type: recovery-validation
status: completed

categories:
  - "[[Recovery]]"
  - "[[Validation]]"
  - "[[Operations]]"

tags:
  - ats
  - resume-pipeline
  - application-package
  - regression
  - operational-recovery

description: Validation record for recovery of the normalized-JD-to-Application-Package pipeline.

created: 2026-07-16
updated: 2026-07-16
---

# Recovery Validation — ATS Resume Pipeline

Status: Complete

## Executive Summary

This document records the successful recovery of the Career System
JD → Resume → ATS Resume → Application Package pipeline.

The recovery restored deterministic resume generation, isolated
application-package generation, fail-fast validation, and complete
end-to-end orchestration from a normalized Job Description.

Recovery validation was performed using existing production-quality
application packages to ensure that regenerated artifacts matched
approved outputs.

---

## Recovery Objectives

- Restore deterministic Resume Asset selection
- Restore Final-Mile resume generation
- Restore ATS HTML generation
- Restore ATS TXT generation
- Restore isolated Application Package generation
- Restore complete JD → Application Package orchestration
- Eliminate partial package generation
- Preserve regression compatibility

---

## Components Restored

### Resume Assets

Role-family assets:

- BA
- Support
- Product
- Default fallback

### Resume Asset Selector

Deterministic asset selection based on role family.

### Final Mile

Produces:

- Professional Summary
- FRBNY section
- Full Resume (Markdown)
- Full Resume (HTML)
- ATS Resume (Markdown)
- ATS Resume (HTML)
- ATS Resume (TXT)

### Application Package

Produces:

- application-summary.md
- full-resume.md
- full-resume.html
- ats-resume.md
- ats-resume.html
- ats-resume.txt
- README.md
- submission-notes.md
- package-manifest.json

### End-to-End Orchestration

Normalized JD

↓

Resume Assets

↓

Final Mile

↓

Application Package

---

## Validation Strategy

Regression targets:

- LSEG Senior Business Analyst
- Broadridge Product Analyst

Validation included:

- isolated execution
- deterministic asset selection
- required artifact verification
- required content verification
- byte-for-byte regression comparison
- fail-fast package validation
- negative testing

---

## Results

Result: PASS

Validated:

✓ deterministic Resume Asset selection

✓ Final Mile generation

✓ isolated Application Package generation

✓ fail-fast validation

✓ JD → Application Package orchestration

✓ regression compatibility

---

## Recovery Outcome

The Career System recovery objectives for the ATS Resume Pipeline
were successfully completed.

The pipeline is now capable of regenerating validated application
packages directly from normalized Job Descriptions while preserving
existing regression outputs.


---

## Detailed Validation Evidence

### LSEG Senior Business Analyst

Input:

    data/jds/normalized/jd-lseg-sba-2026-v1.md

Routing result:

    role_family: ba
    content_profile: ba
    fallback_used: false

Generated package:

    application-lseg-senior-ba-2026-v1

The following regenerated artifacts were compared byte-for-byte against
the existing validated LSEG Application Package:

- application-summary.md
- full-resume.md
- full-resume.html
- ats-resume.md
- ats-resume.html
- ats-resume.txt

Result:

    6 of 6 artifacts matched
    LSEG regression: PASS

### Broadridge Product Analyst

Input:

    data/jds/normalized/jd-broadridge-product-analyst-2026-v1.md

Routing result:

    role_family: product
    content_profile: product
    fallback_used: false

Generated package:

    application-broadridge-product-analyst-2026-v1

The following regenerated artifacts were compared byte-for-byte against
the existing validated Broadridge Application Package:

- application-summary.md
- full-resume.md
- full-resume.html
- ats-resume.md
- ats-resume.html
- ats-resume.txt

Result:

    6 of 6 artifacts matched
    Broadridge regression: PASS

### Negative Preflight Validation

The ATS text source was removed from an isolated test input.

Expected result:

- package generation failed with a nonzero exit status
- the missing ats-resume.txt source was identified
- no partial Application Package directory was created

Result:

    Negative validation: PASS

## Recovery Implementation Commits

- e3d2194 — Add deterministic Resume Asset selector
- 467c514 — Add Resume Asset selection wrapper
- 4b1e45c — Add final-mile resume orchestration from normalized JD
- 9799cd0 — Support isolated Application Package generation
- 97c4bd9 — Require complete Application Package inputs
- 8530621 — Add JD-to-Application Package orchestration
- 8c5ef6b — Add validated BA and Product Resume Asset profiles

## Current Operational Boundary

The recovered orchestration begins from a normalized Job Description.

Current supported entry point:

    normalized JD
        to Resume Asset selection
        to resume generation
        to ATS export
        to Application Package

Raw clipped JD capture and JD normalization remain upstream operational
steps and are not executed by the final recovered orchestration command.

---

## Related Artifacts

- [[RECOVERY-JOURNAL]]
- [[RECOVERY-ARCHITECTURE]]
- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]]
- [[US-CS-056-restore-end-to-end-workflow-orchestration]]
- [[US-CS-057-restore-final-application-package-generation]]
- [[US-CS-058-regression-validation-against-historical-application-packages]]
- [[US-CS-059-operational-verification-and-recovery-runbook]]
- [[US-CS-060-recovery-traceability-and-implementation-updates]]
