---
id: NOTE-CS-002
project: career-system
type: note
status: draft

categories:
  - "[[Recovery]]"
  - "[[Resume Assets]]"
  - "[[Design]]"

tags:
  - recovery
  - role-family
  - professional-summary
  - frbny
  - deterministic-assembly
  - validation

description: Define role-family resume asset selection and the focused validation set for Career System pipeline recovery.

created: 2026-07-15
updated: 2026-07-15
---

# Role-Family Resume Assets and Recovery Validation

## TL;DR

- Recover the pipeline using approved, reusable resume assets rather than generating every section dynamically.
- Select Professional Summary and FRBNY experience assets by canonical `role_family`.
- Provide explicit default assets so every supported role can produce a resume.
- Treat the current `application-summary.md` name as a legacy compatibility name for the resume Professional Summary.
- Validate historical behavior with LSEG, Broadridge, and Citi.
- Validate the new role-family approach against the manually approved Eclaro Production Support application.
- Use Pico SRE later as a fresh clipped-JD validation for another role family.

---

# Purpose

Document the simplified resume-assembly approach selected for Career System operational recovery.

The immediate objective is to restore a reliable JD-to-Application Package workflow. Dynamic content optimization and specialized content for every role family can be introduced after deterministic assembly is working.

---

# Problem

The existing final-mile resume generators currently require two critical resume inputs:

1. Professional Summary
2. Targeted FRBNY experience section

Historically the first artifact has been named:

```text
application-summary.md
```

However, its content is actually the Professional Summary that appears at the beginning of the resume.

This naming makes it difficult to distinguish:

- resume content
- application analysis
- application-package documentation

Generating both resume inputs dynamically also increases recovery complexity and makes regression validation harder.

---

# Recovery Decision

Recovery will use approved, reusable resume assets selected by canonical `role_family`.

The two initial asset types are:

```text
professional-summary
frbny-experience-section
```

Conceptually the recovered bridge becomes:

```text
Normalized Job Description
        ↓
Canonical role_family
        ↓
Role-family asset selection
        ├── Professional Summary
        └── FRBNY Experience Section
        ↓
Validated ATS Resume Generator
Validated Full Resume Generator
        ↓
ATS Resume
Full Resume
HTML
ATS Text
        ↓
Application Package
```

The existing generators remain intact.

Recovery simplifies the bridge into those generators rather than rewriting them.

---

# Canonical Role Families

Current registry:

```text
data/reference/role-families.json
```

Current families:

```text
ba
bsa
ops
sre
support
```

Recovery initially focuses on:

```text
ba
support
```

All other role families use the default assets until specialized assets are approved.

---

# Initial Resume Asset Library

Proposed reusable source assets:

```text
data/resume-assets/
├── professional-summaries/
│   ├── professional-summary-default.md
│   ├── professional-summary-support.md
│   └── professional-summary-ba.md
└── experience-sections/
    └── frbny/
        ├── frbny-default.md
        ├── frbny-support.md
        └── frbny-ba.md
```

Generated outputs may continue using existing directories during recovery for compatibility.

---

# Initial Content Strategy

## Default

The manually approved Eclaro Production Support Professional Summary and FRBNY section become the initial default assets.

## Support

The same approved content populates:

```text
professional-summary-support.md
frbny-support.md
```

Metadata:

```yaml
content_profile: role-specific
```

## Business Analyst

Business Analyst assets initially reuse the approved default content until specialized BA wording is available.

Metadata:

```yaml
content_profile: default-derived
fallback_asset: professional-summary-default.md
```

Later these assets become independently maintained.

---

# Resume Asset Metadata

Example:

```yaml
---
project: career-system
type: resume-asset
status: approved

role_family: support
asset_type: professional-summary
content_profile: role-specific
fallback_asset: professional-summary-default.md

categories:
  - "[[Resume Assets]]"
  - "[[Professional Summaries]]"

tags:
  - resume
  - role-family
  - support

created:
updated:
---
```

---

# Asset Selection Rules

Recovery selector:

1. Read canonical `role_family`.
2. Locate matching asset.
3. If found, use it.
4. Otherwise use the explicit default asset.
5. Record whether fallback occurred.
6. Fail only if neither asset exists.

Initial routing:

```text
support  → support asset
ba       → ba asset
other    → default asset
```

---

# Legacy Compatibility

Although the canonical concept is:

```text
Professional Summary
```

existing consumers still reference:

```text
application-summary.md
```

Recovery preserves compatibility by allowing the selected Professional Summary asset to be published using the legacy filename where existing generators expect it.

The filename can be modernized after the pipeline is stable.

---

# Recovery Validation Set

## Historical Regression

### LSEG

Purpose:

- Validate historical BA pipeline.
- Reproduce known-good outputs.

### Broadridge

Purpose:

- Validate second regression baseline.
- Confirm package generation.

### Citi

Purpose:

- Validate another historical BA package.
- Ensure recovery is not dependent on only two examples.

---

## Human Acceptance Baseline

### Eclaro Production Support Engineer

Purpose:

- Run the clipped JD through the recovered pipeline.
- Compare generated output against the manually prepared resume and cover letter submitted to recruiter Mark.

This becomes the approved human acceptance baseline.

Suggested metadata:

```yaml
validation_type: acceptance
validation_status: approved-human
approved_for_submission: true
baseline_version: 1
role_family: support
```

Evaluation focuses on:

- Professional Summary
- FRBNY section
- keyword coverage
- factual accuracy
- production-support positioning
- package completeness

Exact wording does not need to match.

---

## Future Validation

### Pico SRE

Run a freshly clipped JD after recovery is stable.

Purpose:

- Exercise the complete pipeline.
- Validate fallback asset behavior.
- Introduce SRE-specific assets later without changing the assembly contract.

---

# Recovery Sequence

1. Verify existing generator contracts.
2. Add reusable resume assets.
3. Add deterministic role-family selection.
4. Preserve legacy filename compatibility.
5. Connect selected assets into existing generators.
6. Validate LSEG.
7. Validate Broadridge.
8. Validate Citi.
9. Validate Eclaro against the approved manual package.
10. Validate Pico from a fresh clipped JD.

---

# Out of Scope

Deferred until after recovery:

- AI-generated summaries
- AI-generated FRBNY sections
- Repository-wide role-family cleanup
- Broad resume asset governance
- Removal of legacy filenames
- Cover-letter redesign beyond Eclaro validation

---

# Related Artifacts

- [[EPIC-CS-003-career-system-functional-recovery-and-pipeline-validation]]
- [[US-CS-056-restore-end-to-end-workflow-orchestration]]
- [[US-CS-057-restore-final-application-package-generation]]
- [[US-CS-058-regression-validation-against-historical-application-packages]]
- [[US-CS-059-operational-verification-and-recovery-runbook]]
- [[RECOVERY-REQUIREMENTS-RECONNAISSANCE-2026-07-14]]

---

# Framework Improvement Opportunities

Potential EFK candidates:

- Resume Asset artifact
- `content_profile` metadata
- Deterministic asset selection
- Human-approved acceptance baselines
- Compatibility migration guidance

---

# Notes

This note documents the recovery design chosen for restoring the Career System pipeline.

The objective is deterministic, repeatable resume assembly using approved reusable assets while preserving compatibility with the existing final-mile generators.
