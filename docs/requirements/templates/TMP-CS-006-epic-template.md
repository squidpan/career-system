# TMP-CS-006 Epic Template

Status: Draft

## TL;DR

- Defines the canonical structure for Engineering Knowledge Framework Epic artifacts.
- Applies to `EPIC-*` artifacts.
- Epics describe major engineering outcomes composed of multiple stories.
- Every Epic should trace back to Context and forward to implementation.

---

# Purpose

Define the canonical template for Engineering Knowledge Framework Epic artifacts.

---

# Applies To

Artifacts with prefix:

```text
EPIC
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
type: Epic
status: Draft

categories:
  - "[[Epics]]"
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
Business Value
Scope
Success Criteria
Stories
Learning Outcomes
Framework Improvements
Related Artifacts
Notes
```

---

# Recommended Sections

```text
Background
Out of Scope
Dependencies
Risks
Implementation Roadmap
References
```

---

# Template Body

    ---
    id:
    type: Epic
    status: Draft

    categories:
      - "[[Epics]]"
      - "[[Requirements]]"

    tags:

    summary:

    created:
    updated:
    ---

    # EPIC-XXX Title

    ## TL;DR

    -

    ---

    # Purpose

    ---

    # Background

    ---

    # Business Value

    ---

    # Scope

    ### Included

    -

    ### Excluded

    -

    ---

    # Success Criteria

    -

    ---

    # Dependencies

    -

    ---

    # Risks

    -

    ---

    # Stories

    - [[US-XXX]]

    ---

    # Implementation Roadmap

    ## Phase 1

    ## Phase 2

    ## Future

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

An Epic artifact should:

- use an `EPIC-*` identifier
- describe one major engineering outcome
- contain multiple stories
- reference supporting context
- define measurable business value
- define scope boundaries
- include learning outcomes
- identify framework improvements

---

# Related Artifacts

- [[TMP-CS-005-context-template]]
- [[TMP-CS-007-story-template]]
- [[ARCH-CS-001-engineering-operating-system]]

---

# Notes

An Epic defines a destination.

Stories define the individual steps needed to reach that destination.
