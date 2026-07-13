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

