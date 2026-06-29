# TMP-CS-004 Principle Template

Status: Draft

## TL;DR

- Defines the canonical structure for Engineering Knowledge Framework principles.
- Applies to `PR-*` artifacts.
- Principles capture enduring engineering beliefs and philosophies.
- Principles guide standards, architecture, and implementation decisions.

---

# Purpose

Define the canonical template for Engineering Knowledge Framework principles.

---

# Applies To

Artifacts with prefix:

```text
PR
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
type: Principle
status: Active

categories:
  - "[[Principles]]"
  - "[[Frameworks]]"

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
Principle
Rationale
Examples
Related Artifacts
Notes
```

---

# Recommended Sections

```text
Implications
Exceptions
History
References
```

---

# Template Body

    ---
    id:
    type: Principle
    status: Active

    categories:
      - "[[Principles]]"
      - "[[Frameworks]]"

    tags:

    summary:

    created:
    updated:
    ---

    # PR-XXX Title

    ## TL;DR

    -

    ---

    # Principle

    ---

    # Rationale

    ---

    # Examples

    -

    ---

    # Implications

    -

    ---

    # Exceptions

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

A Principle artifact should:

- use a `PR-*` identifier
- define one enduring engineering belief
- explain why the principle exists
- include practical examples
- guide multiple standards or architectures
- remain stable over time

---

# Related Artifacts

- [[TMP-CS-003-standard-template]]
- [[ARCH-CS-001-engineering-operating-system]]

---

# Notes

Principles explain **why engineers think a certain way**.

Standards explain **how engineers consistently apply those principles**.
