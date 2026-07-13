# Career System Functional Recovery Journal

## Metadata

- Date: 2026-07-13
- Phase: 0
- Branch: ops/recover-ats-html-workflow
- Status: COMPLETE
- Result: PASS

---

# Recovery Day 1 — Phase 0

## Objective

Validate:

- Git repository health
- repository structure
- operational scripts
- bridge artifacts
- known-good regression packages
- application-package contract
- ops/runs execution-history
- manifests
- logs
- Git-ignore behavior

---

# 1. Git Repository Validation

Verified:

- branch: ops/recover-ats-html-workflow
- working tree clean
- remote verified
- no stashes
- using git switch instead of git checkout

---

# 2. Repository Structure Validation

Verified:

- bin/
- scripts/
- templates/
- docs/
- data/
- ops/
- tests/

Verified application output folders:

- data/application-packages/
- data/application-summaries/
- data/resume-sections/
- data/full-resumes/
- data/ats-exports/

Verified operations folders:

- docs/operations/
- docs/operations/recovery/
- docs/operations/diagrams/


# 3. Operational Script Validation

Verified final-mile wrappers:

- run-full-resume-generator.sh
- run-ats-resume-generator.sh
- run-resume-html-export.sh
- run-ats-text-export.sh
- run-application-package.sh

Verified corresponding Python implementations.

Wrappers are executable.

---

# 4. Regression Package Validation

Known-good packages:

- application-lseg-senior-ba-2026-v1
- application-broadridge-product-analyst-2026-v1

Verified package contents:

- application-summary.md
- ats-resume.md
- ats-resume.html
- ats-resume.txt
- full-resume.md
- full-resume.html
- package-manifest.json
- README.md
- submission-notes.md

Manual browser-generated PDFs are considered user artifacts and are not part of automated regression testing.

Interview recommendation artifacts are outside the current recovery scope.

---

# 5. Canonical Deliverable

The authoritative operational output is:

data/application-packages/application-<job-slug>-2026-v1/

All final ATS and narrative resume artifacts belong inside the application package.


# 6. Ops Run-System Audit

Summary:

- ops size approximately 23 MB
- 96 historical runs
- every run contains output/
- 54 runs contain input/
- 54 runs contain logs/
- 52 runs contain run-manifest.md
- 44 runs use output-only pattern

No empty logs.

No empty output directories.

No runtime failures detected.

Git ignore:

    ops/runs/*
    !ops/runs/.gitkeep

Only .gitkeep is tracked.

Historical runs are intentionally excluded from Git.


# 7. Architectural Findings

Three execution patterns exist.

Pattern A

input/
logs/
output/
run-manifest.md

Pattern B

output/

Pattern C

Direct generation into:

- data/full-resumes/
- data/ats-exports/
- data/application-packages/

without a unified run record.

Observed malformed hierarchy:

ops/runs/data/jds/raw/...

Likely caused by an unsafe run_id containing path separators.

No cleanup will occur during Phase 0.


# 8. Permanent Artifact References

Permanent JSON files currently reference historical paths inside ops/runs.

Examples include:

- assembled-v2
- assembled-v3
- final resume metadata
- application-manifest
- gap-analysis

This creates coupling between permanent artifacts and runtime history.

The issue is documented for future hardening but is not part of Phase 0.

---

# 9. Deferred Hardening

Deferred until recovery is complete:

1. Reject unsafe run IDs.
2. Standardize manifests.
3. Standardize run envelopes.
4. Add final-mile run records.
5. Remove absolute paths.
6. Archive historical runs.
7. Remove malformed ops/runs/data after verification.
8. Define retention policy.

---

# 10. Phase 0 Acceptance

- [x] Repository validated
- [x] Scripts validated
- [x] Regression packages validated
- [x] Ops structure audited
- [x] Git-ignore verified
- [x] Architectural seams documented

Result:

PASS

Next:

Phase 1 — Final-Mile Regression Validation


---

# Recovery Day 1 — Phase 1

## Objective

Validate that the known-good final-mile workflow still produces exact,
submission-ready resume artifacts when supplied with valid application
summary and targeted FRBNY section inputs.

## Regression Method

Created an isolated detached Git worktree at:

    /tmp/career-system-final-mile-regression-20260713

The canonical working repository remained on:

    ops/recover-ats-html-workflow

Regression execution used the production wrappers:

- bin/run-full-resume-generator.sh
- bin/run-ats-resume-generator.sh
- bin/run-resume-html-export.sh
- bin/run-ats-text-export.sh
- bin/run-application-package.sh

PDF files were excluded from regression validation.

## LSEG Result

Regression package:

    application-lseg-senior-ba-2026-v1

Verified required package files:

- application-summary.md
- ats-resume.md
- ats-resume.html
- ats-resume.txt
- full-resume.md
- full-resume.html
- package-manifest.json
- README.md
- submission-notes.md

The following core artifacts matched the canonical package byte-for-byte
using SHA-256 checksums and unified diffs:

- application-summary.md
- ats-resume.md
- ats-resume.html
- ats-resume.txt
- full-resume.md
- full-resume.html

Result:

PASS — exact regression match.

## Broadridge Result

Regression package:

    application-broadridge-product-analyst-2026-v1

Verified required package files:

- application-summary.md
- ats-resume.md
- ats-resume.html
- ats-resume.txt
- full-resume.md
- full-resume.html
- package-manifest.json
- README.md
- submission-notes.md

The following core artifacts matched the canonical package byte-for-byte
using SHA-256 checksums and unified diffs:

- application-summary.md
- ats-resume.md
- ats-resume.html
- ats-resume.txt
- full-resume.md
- full-resume.html

Result:

PASS — exact regression match.

## Findings

- The final-mile workflow is functional.
- The final-mile workflow is deterministic for both regression baselines.
- The final-mile scripts are not the current recovery defect.
- The application-package builder successfully assembles the required final
  ATS and narrative resume artifacts.
- The main working repository remained unchanged during regression testing.
- No Git stashes were created.

The confirmed recovery gap is upstream:

    modern JD pipeline
    → application summary
    → targeted FRBNY section
    → proven final-mile workflow

## Phase 1 Result

PASS

## Next Phase

Phase 2 — Missing Bridge Contract and Recovery

Objectives:

1. Compare LSEG and Broadridge application-summary structures.
2. Compare LSEG and Broadridge targeted FRBNY-section structures.
3. Identify the modern-pipeline artifacts that contain the required source
   information.
4. Define deterministic generation contracts for both bridge artifacts.
5. Implement the bridge without changing the validated final-mile scripts.
