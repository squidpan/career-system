# DM-CS-004 Artifact Type Model

Status: Draft

## TL;DR

- EKF artifact types define the kinds of engineering knowledge the framework manages.
- Each artifact type has a prefix, purpose, typical folder, and template.
- Artifact types support consistent metadata, Bases, Canvas, validation, and future automation.
- This model turns document types into structured knowledge objects.

---

# Purpose

Define the artifact types used by the Engineering Knowledge Framework.

This model supports templates, validation, Obsidian Bases, Canvas generation, indexes, and future APIs.

---

# Context

EKF artifacts currently include principles, context, epics, stories, architecture, ADRs, standards, data models, runbooks, glossary terms, releases, sprints, templates, Bases, and Canvas files.

These need to be treated consistently as typed engineering knowledge objects.

---

# Core Entity: ArtifactType

```text
ArtifactType
------------
name
prefix
purpose
typical_folder
template
required_sections
recommended_categories
status_values
```

---

# Initial Artifact Types

| Type | Prefix | Purpose |
|---|---|---|
| Principle | PR | Defines an engineering belief or rule of thought |
| Context | CTX | Explains why work exists |
| Epic | EPIC | Groups related outcomes |
| User Story | US | Defines a deliverable unit of work |
| Acceptance Criteria | AC | Defines objective completion criteria |
| Architecture | ARCH | Explains system or framework structure |
| Architecture Decision Record | ADR | Records a decision and rationale |
| Standard | STD | Defines repeatable rules |
| Data Model | DM | Defines information structures |
| API Contract | API | Defines system communication |
| Runbook | RB | Defines operational procedures |
| Bug | BUG | Describes a defect or issue |
| Sprint | SPR | Describes iteration planning or closeout |
| Release | REL | Describes delivered version content |
| Spike | SPK | Captures research or proof-of-concept work |
| Glossary Term | TERM | Defines vocabulary |
| Template | TEMPLATE | Defines reusable authoring structure |
| Base | BASE | Defines Obsidian structured view |
| Canvas | CANVAS | Defines visual knowledge map |

---

# Folder Mapping

| Type | Typical Folder |
|---|---|
| Principle | `docs/requirements/principles/` |
| Context | `docs/requirements/context/` |
| Epic | `docs/requirements/epics/` |
| User Story | `docs/requirements/stories/` |
| Architecture | `docs/requirements/architecture/` |
| Architecture Decision Record | `docs/requirements/adr/` |
| Standard | `docs/requirements/standards/` |
| Data Model | `docs/requirements/data-model/` |
| Runbook | `docs/requirements/runbooks/` |
| Glossary Term | `docs/requirements/glossary/` |
| Sprint | `docs/requirements/sprints/` |
| Release | `docs/requirements/releases/` |
| Template | `docs/requirements/templates/` |
| Base | `docs/requirements/bases/` |
| Canvas | `docs/requirements/canvas/` |

---

# Category Mapping

Examples:

```yaml
categories:
  - "[[Architectures]]"
  - "[[Frameworks]]"
```

Common mappings:

| Type | Recommended Categories |
|---|---|
| Principle | `[[Principles]]`, `[[Frameworks]]` |
| Context | `[[Contexts]]`, `[[Requirements]]` |
| Epic | `[[Epics]]`, `[[Requirements]]` |
| User Story | `[[Stories]]`, `[[Requirements]]` |
| Architecture | `[[Architectures]]`, `[[Frameworks]]` |
| ADR | `[[Decisions]]`, `[[Architectures]]` |
| Standard | `[[Standards]]`, `[[Frameworks]]` |
| Data Model | `[[Data Models]]`, `[[Architectures]]` |
| Runbook | `[[Runbooks]]`, `[[Operations]]` |
| Glossary Term | `[[Glossaries]]`, `[[References]]` |
| Template | `[[Templates]]`, `[[Frameworks]]` |
| Base | `[[Bases]]`, `[[Obsidian]]` |
| Canvas | `[[Canvases]]`, `[[Obsidian]]` |

---

# Template Relationship

Each major artifact type should eventually have a template.

Examples:

```text
Architecture → Architecture Template
ADR → ADR Template
Epic → Epic Template
User Story → Story Template
Standard → Standard Template
```

Templates implement artifact type conventions.

---

# Validation Relationship

Future EKF validation may check:

- correct prefix for artifact type
- correct folder for artifact type
- required metadata
- required sections
- recommended categories
- valid status values
- broken links
- duplicate identifiers

---

# Learning Outcomes

After implementing this model we expect to improve understanding of:

## Engineering

- typed knowledge objects
- artifact taxonomy
- template design

## Automation

- template selection
- ID generation
- folder validation
- Bases generation

## Publishing

- category-driven navigation
- artifact indexes
- Canvas grouping

---

# Framework Improvements

This model defines artifact types as first-class EKF entities.

It provides the bridge between standards and templates.

---

# Related Artifacts

- [[DM-CS-001-engineering-knowledge-meta-model]]
- [[DM-CS-002-engineering-artifact-relationship-model]]
- [[STD-CS-001-engineering-artifact-standard]]
- [[STD-CS-002-engineering-artifact-identification-and-naming-standard]]
- [[STD-CS-003-obsidian-metadata-standard]]

---

# Notes

This model should evolve as real templates and validators are created.
