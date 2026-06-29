# TMP-CS-002 ADR Template

Status: Draft

## TL;DR

- Defines the canonical structure for Architecture Decision Records.
- Applies to `ADR-*` artifacts.
- Records significant engineering decisions and their rationale.
- Complements architecture documents by explaining *why* decisions were made.

---

# Purpose

Define the standard structure for Architecture Decision Records (ADRs).

---

# Applies To

Artifacts with prefix:

```text
ADR
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
type: ADR
status: Proposed

categories:
  - "[[Decisions]]"
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
Decision
Context
Consequences
Learning Outcomes
Framework Improvements
Related Artifacts
Notes
```

---

# Recommended Sections

```text
Problem Statement
Alternatives Considered
Decision Drivers
Tradeoffs
Implementation Notes
References
```

---

# Template Body

    ---
    id:
    type: ADR
    status: Proposed

    categories:
      - "[[Decisions]]"
      - "[[Architectures]]"

    tags:

    summary:

    created:
    updated:
    ---

    # ADR-XXX Title

    Status:

    ## TL;DR

    -

    ---

    # Purpose

    ---

    # Problem Statement

    ---

    # Context

    ---

    # Decision

    ---

    # Decision Drivers

    -

    ---

    # Alternatives Considered

    -

    ---

    # Tradeoffs

    -

    ---

    # Consequences

    ## Positive

    -

    ## Negative

    -

    ---

    # Implementation Notes

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

An ADR artifact should:

- use an `ADR-*` identifier
- include YAML metadata
- clearly state the decision
- explain the context and rationale
- document positive and negative consequences
- include learning outcomes
- include framework improvements when applicable
- reference related architecture artifacts

---

# Related Artifacts

- [[TMP-CS-001-architecture-template]]
- [[ARCH-CS-002-engineering-knowledge-authoring-system]]
- [[STD-CS-004-document-structure-standard]]

---

# Notes

Architecture Decision Records explain **why** a significant engineering decision was made.

Architecture documents explain **what** the resulting architecture looks like.

Together they provide both the rationale and the design, making engineering decisions understandable long after implementation.
