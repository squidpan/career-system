---
id: RECOVERY-ARCHITECTURE
project: career-system
type: recovery-architecture
status: completed

categories:
  - "[[Recovery]]"
  - "[[Architecture]]"
  - "[[Operations]]"

tags:
  - ats
  - resume-pipeline
  - resume-assets
  - application-package
  - orchestration

description: Architecture of the recovered normalized-JD-to-Application-Package pipeline.

created: 2026-07-16
updated: 2026-07-16
---

# ATS Pipeline Recovery Architecture

## Purpose

This document describes the recovered Career System pipeline from a
normalized Job Description through a complete Application Package.

## Recovered Pipeline

    Normalized JD
          |
          v
    Resume Asset Selection
          |
          +----------------------+
          |                      |
          v                      v
    Professional Summary     FRBNY Experience
    Resume Asset             Resume Asset
          |                      |
          +----------+-----------+
                     |
                     v
             Full Resume Generator
                     |
                     v
              ATS Resume Generator
                     |
          +----------+-----------+
          |                      |
          v                      v
       HTML Export          ATS Text Export
          |                      |
          +----------+-----------+
                     |
                     v
         Application Package Builder
                     |
                     v
             Application Package

## Role-Family Selection

The Resume Asset selector reads the canonical role family from the
normalized JD metadata.

Current routing includes:

- ba to BA assets
- bsa to BA assets
- support to Support assets
- product to Product assets
- unsupported role families to Default assets

## Resume Asset Inputs

The initial Resume Asset types are:

- Professional Summary
- FRBNY Experience

Assets are stored under:

    data/resume-assets/professional-summary/
    data/resume-assets/frbny/

## Compatibility Outputs

The selector publishes the existing final-mile input filenames:

    data/application-summaries/<job-slug>-summary-v1.md
    data/resume-sections/<job-slug>-frbny-section.md

This preserves compatibility with the existing resume generators.

## Final-Mile Outputs

The final-mile workflow generates:

- Full Resume Markdown
- Full Resume HTML
- ATS Resume Markdown
- ATS Resume HTML
- ATS Resume text

## Application Package Outputs

The Application Package contains these required core files:

- application-summary.md
- full-resume.md
- full-resume.html
- ats-resume.md
- ats-resume.html
- ats-resume.txt
- submission-notes.md
- README.md
- package-manifest.json

## Operational Commands

Resume final-mile generation:

    bin/run-resume-final-mile-from-jd.sh

Application Package generation:

    bin/run-application-package.sh

Normalized JD through Application Package:

    bin/run-jd-to-application-package.sh

## Failure Behavior

The Application Package builder validates required source artifacts
before creating the package directory.

When a required source is missing or empty:

- generation exits with a nonzero status
- the missing artifact is identified
- no partial package directory is created

## Validation

The recovered architecture was validated using:

- LSEG Senior Business Analyst
- Broadridge Product Analyst
- Citi Application and Production Support

LSEG and Broadridge core outputs matched their historical validated
packages byte-for-byte.

## Architectural Characteristics

- deterministic
- role-family aware
- reusable Resume Assets
- backward compatible
- isolated-output capable
- fail-fast
- regression validated
- operationally repeatable

---

## Related Artifacts

- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-JOURNAL]]
- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]]
- [[NOTE-CS-002-role-family-resume-assets-and-recovery-validation]]
