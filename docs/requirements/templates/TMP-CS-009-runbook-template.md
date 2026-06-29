# TMP-CS-009 Runbook Template

Status: Draft

## TL;DR

- Defines the canonical structure for operational runbooks.
- Applies to `RB-*` artifacts.
- Runbooks describe repeatable operational procedures.
- Runbooks should include prerequisites, procedure, verification, rollback, and troubleshooting.

---

# Purpose

Define the canonical template for Engineering Knowledge Framework runbook artifacts.

---

# Applies To

Artifacts with prefix:

```text
RB
```

---

# Implements Standards

- [[STD-CS-002-engineering-artifact-identification-and-naming-standard]]
- [[STD-CS-003-obsidian-metadata-standard]]
- [[STD-CS-004-document-structure-standard]]

---

# Required Metadata

```yaml
---
id:
type: Runbook
status: Draft

categories:
  - "[[Runbooks]]"
  - "[[Operations]]"

tags:

summary:

created:
updated:
---
```

---

# Required Sections

```text
TL;DR
Purpose
Audience
Prerequisites
Procedure
Verification
Troubleshooting
Related Artifacts
Notes
```

---

# Recommended Sections

```text
Scope
Safety Notes
Rollback
Expected Output
Common Failures
Lessons Learned
References
```

---

# Template Body

    ---
    id:
    type: Runbook
    status: Draft

    categories:
      - "[[Runbooks]]"
      - "[[Operations]]"

    tags:

    summary:

    created:
    updated:
    ---

    # RB-XXX Title

    ## TL;DR

    -

    ---

    # Purpose

    ---

    # Audience

    ---

    # Scope

    ---

    # Prerequisites

    -

    ---

    # Safety Notes

    -

    ---

    # Procedure

    ## Step 1

    ## Step 2

    ---

    # Expected Output

    -

    ---

    # Verification

    -

    ---

    # Rollback

    -

    ---

    # Troubleshooting

    ## Symptom

    Cause:

    Fix:

    ---

    # Common Failures

    -

    ---

    # Lessons Learned

    -

    ---

    # Related Artifacts

    -

    ---

    # References

    -

    ---

    # Notes

---

# Validation Rules

A Runbook artifact should:

- use an `RB-*` identifier
- describe one repeatable operational procedure
- identify the intended audience
- include prerequisites
- include clear steps
- include verification commands or checks
- include rollback or recovery guidance when applicable
- include troubleshooting notes

---

# Related Artifacts

- [[TMP-CS-007-story-template]]
- [[STD-CS-004-document-structure-standard]]

---

# Notes

Runbooks should be usable during real operational work.

A good runbook reduces stress during incidents, releases, deployments, and recovery.
