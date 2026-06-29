# TMP-CS-008 Data Model Template

Status: Draft

## TL;DR

- Defines the canonical structure for Engineering Knowledge Framework data models.
- Applies to `DM-*` artifacts.
- Data models describe engineering concepts, entities, relationships, and semantics.
- Data models are technology-independent unless explicitly stated.

---

# Purpose

Define the canonical template for Engineering Knowledge Framework data model artifacts.

---

# Applies To

Artifacts with prefix:

```text
DM
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
type: Data Model
status: Draft

categories:
  - "[[Data Models]]"
  - "[[Architectures]]"

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
Scope
Core Concepts
Entity Definitions
Relationships
Learning Outcomes
Framework Improvements
Related Artifacts
Notes
```

---

# Recommended Sections

```text
Assumptions
Constraints
Examples
Future Extensions
References
```

---

# Template Body

    ---
    id:
    type: Data Model
    status: Draft

    categories:
      - "[[Data Models]]"
      - "[[Architectures]]"

    tags:

    summary:

    created:
    updated:
    ---

    # DM-XXX Title

    ## TL;DR

    -

    ---

    # Purpose

    ---

    # Scope

    ---

    # Core Concepts

    ---

    # Entity Definitions

    ## Entity

    Purpose:

    Attributes:

    ---

    # Relationships

    ---

    # Assumptions

    -

    ---

    # Constraints

    -

    ---

    # Examples

    -

    ---

    # Future Extensions

    -

    ---

    # Learning Outcomes

    ## Technical

    -

    ## Engineering

    -

    ## Operational

    -

    ---

    # Framework Improvements

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

A Data Model artifact should:

- use a `DM-*` identifier
- define concepts before implementation
- describe entities and relationships
- remain technology-independent unless explicitly stated
- include related architecture and standards
- include learning outcomes

---

# Related Artifacts

- [[TMP-CS-001-architecture-template]]
- [[DM-CS-001-engineering-knowledge-meta-model]]
- [[STD-CS-004-document-structure-standard]]

---

# Notes

A data model explains **what information exists and how it relates**.

Implementation details belong in architecture or code, not in the conceptual model.
