# ARCH-CS-002 Engineering Knowledge Authoring System

Status: Draft

## TL;DR

- EKF artifacts are authored once as canonical Markdown.
- Templates guide creation but do not replace engineering judgment.
- Validation checks identity, metadata, links, naming, and structure.
- Git repositories are the system of record.
- Knowledge platform adapters publish artifacts into Obsidian, static sites, and future tools.
- Automation supports engineering; engineering does not serve automation.

---

# Purpose

Define how Engineering Knowledge Framework artifacts are created, validated, stored, adapted, and published.

This architecture describes the authoring system that supports EKF across Career System, Motorweb, Linux Dev Environment, Skills, and future repositories.

---

# Context

EKF artifacts must be useful in multiple environments:

- Git repositories
- Obsidian vaults
- Obsidian Bases
- Obsidian Canvas
- Obsidian Publish
- future static sites
- future AI-assisted tools

To support this, artifacts should be authored in a canonical source format and adapted into downstream publishing formats.

---

# Authoring Principles

## Author Once, Reuse Everywhere

Engineering artifacts should be written once and reused across multiple views.

## Markdown First, Presentation Second

Canonical Markdown is the source.

Publishing platforms consume Markdown.

## Links Over Duplication

Relationships should be expressed through links instead of repeated text.

## Knowledge Before Automation

Standards should be understood before automation is built.

## Validation Before Publication

Artifacts should be checked before they are treated as publishable knowledge.

---

# Authoring Pipeline

```text
Engineer
    ↓
Template
    ↓
Draft Artifact
    ↓
Validation
    ↓
Git Repository
    ↓
Knowledge Platform Adapter
    ↓
Published Knowledge View
```

---

# Validation Layer

The validation layer checks whether artifacts conform to EKF standards.

Validation may include:

- identifier format
- duplicate identifiers
- file naming
- YAML metadata
- required categories
- status values
- broken links
- missing TL;DR sections
- related artifact links
- PlantUML source availability
- generated SVG availability

Future command:

```text
ekf validate
```

---

# Adapter Layer

Adapters transform canonical EKF artifacts into target platform views.

## Obsidian Adapter

Produces or updates:

- `References/`
- `Templates/`
- `Templates/Bases/`
- `.canvas` files
- generated SVG references
- Obsidian-friendly wikilinks

## Static Site Adapter

Future adapter for:

- Quartz
- Jekyll
- Hugo
- Astro
- Eleventy

## AI Adapter

Future adapter for:

- summarized context packs
- retrieval-optimized exports
- prompt-ready documentation bundles

---

# Component Model

```text
Standards
    ↓
Templates
    ↓
Draft Artifacts
    ↓
Validator
    ↓
Git Repository
    ↓
Adapters
    ↓
Knowledge Platforms
```

---

# Key Components

## Standards

Define rules for identity, metadata, document structure, naming, and publishing.

## Templates

Provide starting structures for engineering artifacts.

## Draft Artifacts

Human-authored Markdown notes that may not yet fully conform to EKF standards.

## Validator

Checks artifacts against EKF standards.

## Git Repository

Authoritative source of engineering knowledge.

## Adapter

Transforms repository artifacts into target knowledge platform formats.

## Knowledge Platform

A human-facing environment such as Obsidian or a static site.

---

# Learning Outcomes

After implementing this architecture we expect to improve understanding of:

## Technical

- Markdown processing
- YAML parsing
- link validation
- PlantUML rendering
- static site generation

## Engineering

- artifact lifecycle design
- documentation architecture
- repository-as-source patterns
- validation before publication

## Operational

- repeatable publishing
- release-ready documentation
- cross-repository documentation flow

---

# Framework Improvements

This architecture introduces:

- validation as a first-class EKF concept
- adapters as a first-class publishing concept
- canonical Markdown as the source artifact model
- knowledge platform independence

---

# Related Artifacts

- [[STD-CS-002-engineering-artifact-identification-and-naming-standard]]
- [[STD-CS-003-obsidian-metadata-standard]]
- [[STD-CS-004-document-structure-standard]]
- [[ADR-CS-001-career-system-reference-implementation]]
- [[ADR-CS-002-engineering-knowledge-framework]]

---

# Notes

This architecture separates authoring from publishing.

That separation allows EKF to support Obsidian today while remaining open to future platforms.
