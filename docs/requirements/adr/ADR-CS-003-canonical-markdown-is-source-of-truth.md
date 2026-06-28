# ADR-CS-003 Canonical Markdown Is Source Of Truth

Status: Accepted

## TL;DR

- EKF artifacts are authored as canonical Markdown.
- Git repositories are the system of record.
- Obsidian, static sites, Canvas, Bases, and AI exports are publishing or consumption views.
- Publishing tools must adapt from Markdown rather than becoming the source.
- This keeps EKF portable and platform-independent.

---

# Decision

Engineering Knowledge Framework artifacts shall be maintained as canonical Markdown files in Git repositories.

Publishing environments consume or transform those Markdown files.

No publishing platform becomes the authoritative source of EKF artifacts.

---

# Context

EKF artifacts need to work across multiple environments:

- Career System repository
- Motorweb repository
- Linux Dev Environment repository
- Skills repository
- Obsidian vault
- Obsidian Publish
- static site generators
- future AI-assisted tooling

Obsidian is the preferred knowledge environment, but it should not become the only place where engineering knowledge can exist.

---

# Consequences

## Positive

- Git remains the source of truth.
- Artifacts remain portable.
- Obsidian can be used without lock-in.
- Static sites can be added later.
- AI-ready exports can be generated later.
- Repository history remains authoritative.

## Negative

- Publishing requires adapters or copy/generation workflows.
- Obsidian-specific features must be handled carefully.
- Generated outputs must not be edited as primary source.

---

# Alternatives Considered

## Obsidian Vault As Source Of Truth

Rejected.

This would make the vault the primary system of record and weaken Git-first engineering workflows.

## Static Site As Source Of Truth

Rejected.

Static sites are publishing outputs, not authoring systems.

## Duplicate Markdown Per Platform

Rejected.

Duplicating Markdown across tools creates maintenance risk and inconsistent knowledge.

---

# Related Artifacts

- [[ARCH-CS-002-engineering-knowledge-authoring-system]]
- [[STD-CS-002-engineering-artifact-identification-and-naming-standard]]
- [[STD-CS-003-obsidian-metadata-standard]]
- [[STD-CS-004-document-structure-standard]]

---

# Notes

This ADR supports the file-over-app philosophy while allowing EKF to take advantage of Obsidian, Bases, Canvas, and future publishing platforms.
