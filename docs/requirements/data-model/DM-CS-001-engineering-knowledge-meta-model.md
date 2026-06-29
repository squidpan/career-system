# DM-CS-001 Engineering Knowledge Meta-Model

Status: Draft

## TL;DR

- EKF artifacts are different views of one underlying engineering knowledge model.
- The core entity is `EngineeringArtifact`.
- Artifacts have identity, metadata, content, relationships, lifecycle status, and publishing views.
- Markdown, Obsidian Bases, Canvas, PlantUML, and future APIs are different representations of the same knowledge model.
- This meta-model guides future templates, validators, adapters, and automation.

---

# Purpose

Define the semantic model underlying the Engineering Knowledge Framework.

This model explains what engineering knowledge objects exist and how they relate.

---

# Core Concept

The Engineering Knowledge Framework is based on this idea:

```text
Engineering Knowledge
    ↓
Engineering Artifact
    ↓
Relationships
    ↓
Views
```

An artifact may appear as:

- Markdown note
- Obsidian note
- Base row
- Canvas node
- PlantUML diagram
- static site page
- AI retrieval unit
- future REST resource

Each view represents the same underlying artifact.

---

# Core Entity: EngineeringArtifact

```text
EngineeringArtifact
-------------------
id
type
status
summary
categories
tags
created
updated
content
relationships
source_repository
publication_views
```

## Required Fields

| Field | Purpose |
|---|---|
| id | Stable unique identifier |
| type | Artifact type |
| status | Lifecycle state |
| summary | One-line description |
| categories | Primary organization |
| tags | Descriptive topics |
| created | Creation date |
| updated | Last meaningful update |

---

# Artifact Types

```text
Principle
Context
Epic
User Story
Acceptance Criteria
Architecture
Architecture Decision Record
Standard
Data Model
API Contract
Runbook
Bug
Sprint
Release
Spike
Glossary Term
Template
Base
Canvas
```

---

# Relationship Model

Artifacts are connected by meaningful relationships.

Examples:

```text
Architecture references ADR

Standard constrains Template

Epic contains Story

Story implements Requirement

Data Model supports API Contract

Runbook operates System

Principle guides Standard

Learning improves Framework
```

Relationships should be expressed with Obsidian links in Markdown.

Future automation may extract relationship graphs from links and metadata.

---

# View Model

An artifact may have multiple views.

```text
EngineeringArtifact
    ├── Markdown View
    ├── Obsidian View
    ├── Base View
    ├── Canvas View
    ├── Diagram View
    ├── Static Site View
    └── AI Retrieval View
```

Views are generated or adapted from the canonical artifact.

---

# Repository Model

```text
Repository
----------
name
path
remote
owns_artifacts
publishes_to
```

Examples:

```text
career-system
motorweb
linux-dev-env
obsidian-skills-ng
plvault
```

Repositories own source artifacts.

Publishing targets consume them.

---

# Publication Model

```text
PublicationView
---------------
target_platform
target_path
generated
public
source_artifact
```

Examples:

```text
Obsidian References/career-system/
Obsidian References/engineering-framework/
GitHub README
Obsidian Canvas
Static Site Page
```

---

# Lifecycle Model

```text
Draft
Active
Accepted
Proposed
Done
Superseded
Archived
```

Status vocabulary may be refined by future standards.

---

# Learning Outcomes

After implementing this meta-model we expect to improve understanding of:

## Engineering

- semantic modeling
- artifact relationships
- source versus view separation
- traceability

## Automation

- metadata validation
- link extraction
- graph generation
- future API modeling

## Publishing

- Obsidian Bases
- Canvas generation
- static site exports
- AI retrieval exports

---

# Framework Improvements

This data model introduces the idea that EKF artifacts are not just Markdown files.

They are structured engineering knowledge objects with multiple representations.

---

# Related Artifacts

- [[ARCH-CS-002-engineering-knowledge-authoring-system]]
- [[ARCH-CS-003-engineering-knowledge-repository]]
- [[ARCH-CS-004-engineering-knowledge-lifecycle]]
- [[ARCH-CS-005-engineering-knowledge-framework-overview]]
- [[STD-CS-002-engineering-artifact-identification-and-naming-standard]]
- [[STD-CS-003-obsidian-metadata-standard]]

---

# Notes

This meta-model is intentionally conceptual.

Future implementation may produce JSON schemas, PostgreSQL tables, Python classes, or REST resources based on this model.
