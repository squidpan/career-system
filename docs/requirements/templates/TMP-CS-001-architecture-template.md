# TMP-CS-001 Architecture Template

Status: Draft

## TL;DR

- Defines the standard structure for EKF architecture artifacts.
- Applies to `ARCH-*` documents.
- Implements EKF identity, metadata, document structure, learning, and relationship standards.
- Architecture artifacts should explain structure, tradeoffs, decisions, and evolution.

---

# Purpose

Define the canonical template for architecture artifacts.

---

# Applies To

Artifacts with prefix:

```text
ARCH
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
type: Architecture
status: Draft

categories:
  - "[[Architectures]]"
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
Context
Architecture Overview
Major Components
Learning Outcomes
Framework Improvements
Related Artifacts
Notes
```

---

# Recommended Sections

```text
Problem Statement
Goals
Non-Goals
Architecture Diagram
Design Decisions
Constraints
Risks
Alternatives Considered
Implementation Roadmap
References
```

---

# Template Body

```markdown
---
id:
type: Architecture
status: Draft

categories:
  - "[[Architectures]]"
  - "[[Frameworks]]"

tags:

summary:

created:
updated:
---

# ARCH-XXX Title

## TL;DR

- 

---

# Purpose



---

# Context



---

# Problem Statement



---

# Goals

- 

---

# Non-Goals

- 

---

# Architecture Overview



---

# Architecture Diagram



---

# Major Components

## Component Name

Purpose:

Responsibilities:

Interfaces:

Dependencies:

---

# Design Decisions

- 

---

# Constraints

- 

---

# Risks

- 

---

# Alternatives Considered

- 

---

# Implementation Roadmap

## Current State



## Next Milestone



## Future Evolution



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


```

---

# Validation Rules

An architecture artifact should:

- use an `ARCH-*` identifier
- include YAML metadata
- include a TL;DR
- explain why the architecture exists
- include related artifacts
- include learning outcomes
- include framework improvements
- link to related ADRs when decisions exist

---

# Related Artifacts

- [[DM-CS-004-artifact-type-model]]
- [[ARCH-CS-002-engineering-knowledge-authoring-system]]
- [[STD-CS-004-document-structure-standard]]

---

# Notes

Architecture templates should guide architectural thinking, not merely enforce formatting.
