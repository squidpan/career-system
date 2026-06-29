# TMP-CS-003 Standard Template

Status: Draft

## TL;DR

- Defines the canonical structure for Engineering Knowledge Framework standards.
- Applies to `STD-*` artifacts.
- Standards define repeatable engineering rules and conventions.
- Standards should explain both the rule and the reasoning behind it.

---

# Purpose

Define the canonical template for Engineering Knowledge Framework standards.

---

# Applies To

Artifacts with prefix:

```text
STD
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
type: Standard
status: Draft

categories:
  - "[[Standards]]"
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
Purpose
Design Principles
Standard
Examples
Related Artifacts
Notes
```

---

# Recommended Sections

```text
Scope
Definitions
Motivation
Exceptions
Future Automation
References
```

---

# Template Body

    ---
    id:
    type: Standard
    status: Draft

    categories:
      - "[[Standards]]"
      - "[[Frameworks]]"

    tags:

    summary:

    created:
    updated:
    ---

    # STD-XXX Title

    ## TL;DR

    -

    ---

    # Purpose

    ---

    # Scope

    ---

    # Definitions

    ---

    # Design Principles

    -

    ---

    # Standard

    ---

    # Examples

    ---

    # Exceptions

    -

    ---

    # Future Automation

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

A Standard artifact should:

- use a `STD-*` identifier
- define one clear engineering standard
- explain the rationale behind the standard
- include examples where appropriate
- reference related principles and architecture
- avoid implementation-specific details unless required

---

# Related Artifacts

- [[TMP-CS-001-architecture-template]]
- [[TMP-CS-002-adr-template]]
- [[STD-CS-004-document-structure-standard]]

---

# Notes

Standards define *how* engineering work should be performed.

They should be stable, broadly applicable, and understandable by future contributors.
