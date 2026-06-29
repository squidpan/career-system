# TMP-CS-005 Context Template

Status: Draft

## TL;DR

- Defines the canonical structure for Engineering Knowledge Framework context artifacts.
- Applies to `CTX-*` artifacts.
- Context artifacts explain why work exists before requirements are written.
- Context provides business, technical, and organizational background.

---

# Purpose

Define the canonical template for Engineering Knowledge Framework context artifacts.

---

# Applies To

Artifacts with prefix:

```text
CTX
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
type: Context
status: Draft

categories:
  - "[[Contexts]]"
  - "[[Requirements]]"

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
Background
Current State
Problem Statement
Desired Future State
Related Artifacts
Notes
```

---

# Recommended Sections

```text
Business Context
Technical Context
Constraints
Assumptions
Success Criteria
References
```

---

# Template Body

    ---
    id:
    type: Context
    status: Draft

    categories:
      - "[[Contexts]]"
      - "[[Requirements]]"

    tags:

    summary:

    created:
    updated:
    ---

    # CTX-XXX Title

    ## TL;DR

    -

    ---

    # Purpose

    ---

    # Background

    ---

    # Business Context

    ---

    # Technical Context

    ---

    # Current State

    ---

    # Problem Statement

    ---

    # Desired Future State

    ---

    # Constraints

    -

    ---

    # Assumptions

    -

    ---

    # Success Criteria

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

A Context artifact should:

- use a `CTX-*` identifier
- explain why the work exists
- describe the current state
- describe the desired future state
- identify important assumptions and constraints
- provide sufficient background before requirements begin

---

# Related Artifacts

- [[TMP-CS-006-epic-template]]
- [[ARCH-CS-001-engineering-operating-system]]

---

# Notes

Context artifacts answer one question:

**"Why are we doing this work?"**

Requirements answer:

**"What should we build?"**
