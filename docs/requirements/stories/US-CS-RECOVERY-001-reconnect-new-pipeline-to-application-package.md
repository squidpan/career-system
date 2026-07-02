# US-CS-RECOVERY-001
## Reconnect New Resume Pipeline to Application Package Generation

Status: Draft

Priority: Critical

Epic:
- EPIC-CS-001 Employment Acceleration System

---

## Problem

The employer-aware resume pipeline successfully generates intermediate resume artifacts.

However, it no longer produces application packages equivalent to the proven LSEG and Broadridge workflows.

The final application package is the operational deliverable used for job applications.

---

## Business Value

A user must be able to import a new JD and produce a complete application package identical in quality and structure to previous successful submissions.

---

## Acceptance Criteria

1. Existing LSEG application package can be regenerated from source artifacts.

2. Existing Broadridge application package can be regenerated from source artifacts.

3. Regenerated outputs differ only where intentional content improvements exist.

4. Imported JDs follow the identical operational workflow.

5. New application packages contain all expected artifacts.

6. submission-notes.md is generated.

7. package-manifest.json is complete.

8. HTML export is generated.

9. ATS text export is generated.

10. PDFs can be produced without manual reconstruction.

---

## Technical Tasks

Restore the missing bridge between:

~~~text
JD Intelligence
↓

Resume Recommendation

↓

Resume Tailoring

↓

Resume Enhancement

↓

Application Summary

↓

Targeted FRBNY Resume Section

↓

ATS Resume

↓

Full Resume

↓

Application Package
~~~

---

## Validation

LSEG and Broadridge remain the regression test cases for the complete workflow.

