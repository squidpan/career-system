# TMP-CS-007 Story Template

Status: Draft

## TL;DR

- Defines the canonical structure for Engineering Knowledge Framework user stories.
- Applies to `US-*` artifacts.
- Stories define deliverable units of work with clear validation criteria.
- EKF stories should capture business value, scope, validation, learning outcomes, and framework improvements.

---

# Purpose

Define the canonical template for Engineering Knowledge Framework story artifacts.

---

# Applies To

Artifacts with prefix:

```text
US
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
type: Story
status: Draft

categories:
  - "[[Stories]]"
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
User Story
Business Value
Scope
Acceptance Criteria
Validation
Learning Outcomes
Framework Improvements
Related Artifacts
Notes
```

---

# Recommended Sections

```text
Business Context
Out of Scope
Dependencies
Implementation Notes
Manual Validation
Programmatic Validation
Regression Validation
References
```

---

# Template Body

    ---
    id:
    type: Story
    status: Draft

    categories:
      - "[[Stories]]"
      - "[[Requirements]]"

    tags:

    summary:

    created:
    updated:
    ---

    # US-XXX Title

    ## TL;DR

    -

    ---

    # User Story

    As a ...

    I want ...

    so that ...

    ---

    # Business Context

    ---

    # Business Value

    ---

    # Scope

    ## Included

    -

    ## Excluded

    -

    ---

    # Dependencies

    -

    ---

    # Acceptance Criteria

    -

    ---

    # Implementation Notes

    -

    ---

    # Validation

    ## Manual Validation

    -

    ## Programmatic Validation

    -

    ## Regression Validation

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

A Story artifact should:

- use a `US-*` identifier
- describe one deliverable unit of work
- include a user story statement
- define clear business value
- define scope and out-of-scope boundaries
- include objective acceptance criteria
- include validation steps
- link to related epics, context, architecture, or data models
- include learning outcomes
- include framework improvements when applicable

---

# Related Artifacts

- [[TMP-CS-006-epic-template]]
- [[TMP-CS-005-context-template]]
- [[STD-CS-004-document-structure-standard]]

---

# Notes

A Story should be small enough to complete and validate.

If the story cannot be validated, it is not ready.
