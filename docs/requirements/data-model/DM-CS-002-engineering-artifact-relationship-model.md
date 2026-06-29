# DM-CS-002 Engineering Artifact Relationship Model

Status: Draft

## TL;DR

- EKF artifacts form a knowledge graph.
- Relationships connect artifacts into meaningful engineering context.
- Obsidian links are the first relationship representation.
- Future automation may extract links into graph, Canvas, Bases, SQL, JSON, or API views.
- Relationships should be high-signal, not exhaustive.

---

# Purpose

Define how Engineering Knowledge Framework artifacts relate to each other.

This model supports traceability, navigation, publishing, Canvas generation, and future automation.

---

# Context

Engineering artifacts do not stand alone.

A story may belong to an epic.

An architecture may reference an ADR.

A standard may constrain a template.

A runbook may operate a deployed service.

A principle may guide a standard.

These relationships are the foundation of the Engineering Knowledge Graph.

---

# Core Entity: ArtifactRelationship

```text
ArtifactRelationship
--------------------
source_artifact
target_artifact
relationship_type
description
created
updated
```

---

# Relationship Direction

Relationships should have direction.

Examples:

```text
EPIC-CS-001 contains US-CS-001

US-CS-001 realizes EPIC-CS-001

ARCH-CS-001 references ADR-CS-001

STD-CS-002 constrains Architecture Template

PR-CS-004 guides STD-CS-004
```

Direction helps future automation generate useful views.

---

# Relationship Types

Initial relationship types:

```text
references
contains
realizes
supports
constrains
guides
implements
validates
supersedes
depends_on
publishes_to
generates
operates
improves
```

These may be refined as EKF matures.

---

# Markdown Relationship Representation

Relationships are initially represented using Obsidian links.

Example:

```markdown
## Related Artifacts

- [[ARCH-CS-002-engineering-knowledge-authoring-system]]
- [[ADR-CS-003-canonical-markdown-is-source-of-truth]]
```

This is human-readable and immediately useful in Obsidian.

---

# Relationship Quality Rule

Relationships should be meaningful.

Avoid linking every artifact to every other artifact.

Good links answer:

```text
What should the reader visit next?
```

Poor links create noise.

---

# Future Extracted Relationship Model

Future automation may extract relationships from:

- `Related Artifacts` sections
- YAML metadata
- backlinks
- folder paths
- explicit relationship files
- issue/story traceability

Extracted relationships may produce:

- Graph views
- Canvas maps
- Bases
- JSON
- PostgreSQL tables
- REST APIs
- AI retrieval context

---

# Example Graph

```text
PR-CS-005 Knowledge Is A Deliverable
        ↓ guides
STD-CS-004 Document Structure Standard
        ↓ constrains
Architecture Template
        ↓ produces
ARCH-CS-002 Engineering Knowledge Authoring System
        ↓ references
ADR-CS-003 Canonical Markdown Is Source Of Truth
```

---

# Learning Outcomes

After implementing this relationship model we expect to improve understanding of:

## Engineering

- traceability
- knowledge graph modeling
- relationship direction
- documentation navigation

## Automation

- backlink extraction
- Canvas generation
- relationship validation
- future graph APIs

## Publishing

- meaningful navigation
- hover preview paths
- summary note composition

---

# Framework Improvements

This data model establishes relationships as first-class EKF concepts.

It also clarifies that links are not decoration. Links are structure.

---

# Related Artifacts

- [[DM-CS-001-engineering-knowledge-meta-model]]
- [[ARCH-CS-002-engineering-knowledge-authoring-system]]
- [[ARCH-CS-003-engineering-knowledge-repository]]
- [[STD-CS-004-document-structure-standard]]

---

# Notes

The first implementation should remain simple: Obsidian links in Markdown.

Automation should come after the linking convention is stable.
