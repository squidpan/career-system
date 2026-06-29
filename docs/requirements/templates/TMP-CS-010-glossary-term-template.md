# TMP-CS-010 Glossary Term Template

Status: Draft

## TL;DR

- Defines the canonical structure for Engineering Knowledge Framework glossary terms.
- Applies to `TERM-*` artifacts.
- Glossary terms establish a shared engineering vocabulary.
- Terms should define concepts rather than repeat dictionary definitions.

---

# Purpose

Define the canonical template for Engineering Knowledge Framework glossary artifacts.

---

# Applies To

Artifacts with prefix:

```text
TERM
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
type: Glossary Term
status: Active

categories:
  - "[[Glossaries]]"
  - "[[References]]"

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
Definition
Why It Matters
Related Concepts
Related Artifacts
Notes
```

---

# Recommended Sections

```text
Examples
Synonyms
Common Misunderstandings
References
```

---

# Template Body

    ---
    id:
    type: Glossary Term
    status: Active

    categories:
      - "[[Glossaries]]"
      - "[[References]]"

    tags:

    summary:

    created:
    updated:
    ---

    # TERM-XXX Title

    ## TL;DR

    -

    ---

    # Definition

    ---

    # Why It Matters

    ---

    # Examples

    -

    ---

    # Related Concepts

    -

    ---

    # Common Misunderstandings

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

A Glossary artifact should:

- use a `TERM-*` identifier
- define one engineering concept
- explain why the concept matters
- link to related concepts
- avoid circular definitions
- remain implementation independent

---

# Related Artifacts

- [[STD-CS-004-document-structure-standard]]
- [[ARCH-CS-005-engineering-knowledge-framework-overview]]

---

# Notes

Glossary terms establish the shared vocabulary of the Engineering Knowledge Framework.

A consistent vocabulary improves communication, architecture, documentation, and automation.
