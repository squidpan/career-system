# ARCH-CS-003 Engineering Knowledge Repository

Status: Draft

## TL;DR

- The Engineering Knowledge Repository stores canonical EKF artifacts.
- Git repositories remain the system of record.
- Career System is the first reference implementation.
- Obsidian is a working and publishing environment, not the source of truth.
- Repository artifacts can be adapted into Obsidian, static sites, Canvas, Bases, and AI-ready exports.

---

# Purpose

Define where Engineering Knowledge Framework artifacts live and how repositories participate in the EKF ecosystem.

---

# Context

EKF knowledge will exist across multiple repositories:

- Career System
- Motorweb
- Linux Dev Environment
- Skills
- future repositories

Each repository may contain source engineering artifacts.

A publishing pipeline may copy, adapt, or generate these artifacts into an Obsidian vault under `References/`.

---

# Repository Model

```text
Git Repository
    ↓
Canonical Markdown Artifacts
    ↓
Validation
    ↓
Knowledge Platform Adapter
    ↓
Published Knowledge View
```

---

# Source Repository Responsibilities

A source repository owns:

- canonical Markdown artifacts
- source PlantUML files
- source templates
- source standards
- source requirements
- source architecture
- source ADRs
- source runbooks
- Git history

---

# Publishing Target Responsibilities

A publishing target owns:

- browsing experience
- Bases
- Canvas views
- graph navigation
- hover previews
- public/private publishing selection
- generated SVG assets
- static site rendering

---

# References Folder Model

The Obsidian vault should use `References/` as the target location for repository-sourced knowledge.

Example:

```text
References/
  career-system/
  motorweb/
  linux-dev-env/
  skills/
  engineering-framework/
```

---

# Boundaries

## Repository Is Authoritative

The repository is the source of truth.

## Vault Is Navigational

The vault is the working and publishing environment.

## Generated Outputs Are Not Primary Source

Generated SVG, Canvas, Bases, and static site files may be regenerated.

They should not replace canonical source artifacts.

---

# Learning Outcomes

After implementing this architecture we expect to improve understanding of:

## Technical

- Git-based knowledge management
- Markdown publishing pipelines
- Obsidian References layout
- generated artifacts

## Engineering

- source versus generated artifact boundaries
- cross-repository traceability
- knowledge repository design

## Operational

- repeatable publishing workflows
- public/private content boundaries
- repository migration planning

---

# Framework Improvements

This architecture clarifies:

- repository ownership
- vault ownership
- source versus publishing boundaries
- how multiple repositories participate in EKF

---

# Related Artifacts

- [[ARCH-CS-002-engineering-knowledge-authoring-system]]
- [[ADR-CS-003-canonical-markdown-is-source-of-truth]]
- [[STD-CS-002-engineering-artifact-identification-and-naming-standard]]
- [[STD-CS-003-obsidian-metadata-standard]]

---

# Notes

This architecture allows EKF to remain repository-first while still taking full advantage of Obsidian as a knowledge platform.
