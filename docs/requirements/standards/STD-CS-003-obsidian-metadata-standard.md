# STD-CS-003 Obsidian Metadata Standard

Status: Draft

## TL;DR

- Obsidian Properties are the canonical metadata model for EKF.
- YAML metadata should remain intentionally small.
- Categories organize notes.
- Tags describe topics.
- The Markdown document is the authoritative content.
- Git repositories remain the source of truth.

---

# Purpose

Define the standard metadata used by Engineering Knowledge Framework artifacts.

The metadata is designed for:

- Obsidian
- Bases
- Canvas
- Git
- Publishing
- Future automation

---

# Design Principles

Metadata should:

- answer questions quickly
- avoid duplication
- remain stable
- support Bases
- support automation
- remain easy to maintain

---

# Required Properties

```yaml
---
id:
type:
status:

categories:

tags:

summary:

created:
updated:
---
```

---

# Property Definitions

| Property | Purpose |
|----------|---------|
| id | Unique artifact identifier |
| type | Artifact type |
| status | Lifecycle state |
| categories | Primary organization |
| tags | Descriptive topics |
| summary | One-line description |
| created | Creation date |
| updated | Last significant update |

---

# Categories

Categories represent:

"What kind of engineering knowledge is this?"

Rules:

- plural
- internal links
- reusable
- small vocabulary

Example:

```yaml
categories:
  - "[[Architectures]]"
  - "[[Frameworks]]"
```

---

# Tags

Tags represent:

"What concepts appear in this note?"

Rules:

- lowercase
- reusable
- descriptive
- multiple allowed

Example:

```yaml
tags:
  - ekf
  - metadata
  - obsidian
```

---

# Summary

Summary is a single sentence intended for:

- Bases
- Search
- Publishing
- AI retrieval

It should not replace the document's TL;DR.

---

# Title

The H1 heading is the canonical title.

The title should not be duplicated in YAML.

---

# Notes

Metadata supports navigation.

Markdown contains engineering knowledge.
