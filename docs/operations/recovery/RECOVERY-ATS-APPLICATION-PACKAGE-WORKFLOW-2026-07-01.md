---
id: RECOVERY-ATS-APPLICATION-PACKAGE-WORKFLOW-2026-07-01
project: career-system
type: operational-runbook
status: operational

categories:
  - "[[Recovery]]"
  - "[[Operations]]"
  - "[[Runbooks]]"

tags:
  - recovery
  - resume-pipeline
  - application-package
  - final-mile
  - orchestration

description: Operational runbook for generating a complete Application Package from a normalized Job Description.

created: 2026-07-01
updated: 2026-07-16
---

# Recovery — ATS Application Package Workflow

## Purpose

This runbook describes the recovered operational workflow for generating
a complete Career System Application Package from a normalized Job
Description.

The workflow uses deterministic role-family Resume Assets and preserves
the validated Full Resume, ATS Resume, HTML, text-export, and Application
Package generators.

## Current Operational Boundary

The supported entry point is a normalized JD.

Raw JD capture and JD normalization remain upstream steps and are not
executed by this runbook.

## Prerequisites

Before running the workflow:

- switch to the intended Career System branch
- confirm the working tree state
- confirm the normalized JD exists
- determine the canonical job slug
- determine the Application Package ID
- choose an output root

Safety check:

    cd ~/pjs/repos/career-system

    git branch --show-current
    git status --short
    git stash list

## Primary Command

Command pattern:

    ./bin/run-jd-to-application-package.sh \
      <normalized-jd> \
      <job-slug> \
      <application-id> \
      <output-root>

The output root may be an isolated directory under `/tmp` or the
repository root when an intentional production regeneration is being
performed.

## Safe Isolated Validation

Use an isolated `/tmp` output root before intentionally replacing
repository Application Packages.

Example for LSEG:

    rm -rf /tmp/career-system-validation-lseg

    ./bin/run-jd-to-application-package.sh \
      data/jds/normalized/jd-lseg-sba-2026-v1.md \
      lseg-senior-ba \
      application-lseg-senior-ba-2026-v1 \
      /tmp/career-system-validation-lseg

Example for Broadridge:

    rm -rf /tmp/career-system-validation-broadridge

    ./bin/run-jd-to-application-package.sh \
      data/jds/normalized/jd-broadridge-product-analyst-2026-v1.md \
      broadridge-product-analyst \
      application-broadridge-product-analyst-2026-v1 \
      /tmp/career-system-validation-broadridge

## Expected Output

The workflow creates intermediate and final artifacts beneath the selected
output root.

Expected bridge artifacts:

    data/application-summaries/<job-slug>-summary-v1.md
    data/resume-sections/<job-slug>-frbny-section.md

Expected final-mile artifacts:

    data/full-resumes/<job-slug>-full-resume-v1.md
    data/full-resumes/<job-slug>-full-resume-v1.html
    data/full-resumes/<job-slug>-ats-resume-v1.md
    data/full-resumes/<job-slug>-ats-resume-v1.html
    data/ats-exports/<job-slug>-ats-resume-v1.txt

Expected Application Package directory:

    data/application-packages/<application-id>/

Required Application Package files:

- application-summary.md
- full-resume.md
- full-resume.html
- ats-resume.md
- ats-resume.html
- ats-resume.txt
- submission-notes.md
- README.md
- package-manifest.json

Optional recommendation and interview artifacts may be absent without
causing required package generation to fail.

## Completion Verification

Set the generated package directory:

    PACKAGE_DIR="<output-root>/data/application-packages/<application-id>"

Verify required files:

    for file in \
      application-summary.md \
      full-resume.md \
      full-resume.html \
      ats-resume.md \
      ats-resume.html \
      ats-resume.txt \
      submission-notes.md \
      README.md \
      package-manifest.json
    do
      if [[ -s "$PACKAGE_DIR/$file" ]]; then
        echo "PASS $file"
      else
        echo "FAIL $file"
      fi
    done

Verify expected resume content:

    grep -RInE \
      'Professional Summary|Federal Reserve Bank of New York|On-Site|streaming market-data' \
      "$PACKAGE_DIR/full-resume.md" \
      "$PACKAGE_DIR/ats-resume.md" \
      "$PACKAGE_DIR/ats-resume.txt"

Inspect the package manifest:

    cat "$PACKAGE_DIR/package-manifest.json"

## Regression Validation

For LSEG and Broadridge, compare the six core generated artifacts against
the existing validated repository packages.

Core comparison files:

- application-summary.md
- full-resume.md
- full-resume.html
- ats-resume.md
- ats-resume.html
- ats-resume.txt

Comparison pattern:

    OLD_PACKAGE="data/application-packages/<application-id>"
    NEW_PACKAGE="<output-root>/data/application-packages/<application-id>"

    CORE_FILES=(
      application-summary.md
      full-resume.md
      full-resume.html
      ats-resume.md
      ats-resume.html
      ats-resume.txt
    )

    for file in "${CORE_FILES[@]}"; do
      if cmp -s "$OLD_PACKAGE/$file" "$NEW_PACKAGE/$file"; then
        echo "PASS $file"
      else
        echo "FAIL $file"
      fi
    done

Validated recovery results:

- LSEG: 6 of 6 core artifacts matched
- Broadridge: 6 of 6 core artifacts matched

## Failure Behavior

Application Package generation performs required-source validation before
creating the package directory.

If a required source file is missing or empty:

- the command exits with a nonzero status
- the missing source is identified
- no partial Application Package directory is created

Required source validation covers:

- application summary
- Full Resume Markdown
- Full Resume HTML
- ATS Resume Markdown
- ATS Resume HTML
- ATS Resume text

## Production Regeneration Safeguards

Use isolated `/tmp` generation before writing intentionally to the
repository.

Before production regeneration:

- confirm the target branch
- confirm the working tree state
- confirm the normalized JD
- confirm the job slug
- confirm the Application Package ID
- preserve or compare the existing package
- review `git stash list`

After production regeneration:

- inspect the generated package
- review `git status --short`
- review the Git diff
- confirm only expected files changed
- visually inspect the final resume artifacts
- commit only intentional changes

Do not overwrite a validated repository package until isolated validation
has completed successfully.

## Known Operational Limitations

The current orchestration begins from a normalized JD.

The following remain outside this runbook:

- Obsidian Web Clipper capture
- copying the raw JD into Career System
- raw JD normalization
- browser-based PDF creation
- application submission
- submission-result updates

These remain separate upstream or downstream operational steps.

## Operational Exit Criteria

The workflow is operationally accepted when:

- the normalized-JD-to-Application-Package command completes successfully
- all required package files are present and non-empty
- expected resume content is present
- package preflight failure behavior is verified
- no partial package is created after missing-input failure
- regression validation passes for LSEG and Broadridge
- the repository remains unchanged during isolated validation
- the procedure can be repeated using this runbook

## Recovery Status

Recovery result:

    Functional recovery: PASS
    Application Package generation: PASS
    LSEG regression: PASS
    Broadridge regression: PASS
    Missing-input validation: PASS
    Partial-package prevention: PASS

## Related Artifacts

- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-ARCHITECTURE]]
- [[RECOVERY-JOURNAL]]
- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]]
- [[US-CS-056-restore-end-to-end-workflow-orchestration]]
- [[US-CS-057-restore-final-application-package-generation]]
- [[US-CS-058-regression-validation-against-historical-application-packages]]
- [[US-CS-059-operational-verification-and-recovery-runbook]]
