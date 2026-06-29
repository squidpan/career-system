# DM-CS-003 Repository and Publication View Model

Status: Draft

## TL;DR

- Source repositories own canonical engineering artifacts.
- Publishing targets provide views of those artifacts.
- Obsidian, Canvas, Bases, static sites, and AI exports are publication views.
- Generated artifacts should be reproducible from source.
- Source and publication responsibilities must remain separate.

---

# Purpose

Define how source repositories, publishing targets, and generated views relate within the Engineering Knowledge Framework.

---

# Context

EKF artifacts are authored in Git repositories but consumed through many views.

A single engineering artifact may appear in:

- a Git repository
- an Obsidian note
- an Obsidian Base row
- an Obsidian Canvas node
- a generated SVG diagram
- a static site page
- an AI retrieval bundle

These are different views of the same source artifact.

---

# Core Entity: KnowledgeRepository

```text
KnowledgeRepository
-------------------
name
repo_type
local_path
remote_url
owns_artifacts
publishes_to
status
```

Examples:

```text
career-system
motorweb
linux-dev-env
obsidian-skills-ng
plvault
```

---

# Core Entity: PublicationTarget

```text
PublicationTarget
-----------------
name
target_type
local_path
public_url
publishes_artifacts
visibility
status
```

Examples:

```text
plvault References/career-system
plvault References/engineering-framework
Obsidian Publish
Static Site
GitHub Pages
```

---

# Core Entity: PublicationView

```text
PublicationView
---------------
source_artifact
target
target_path
view_type
generated
public
last_generated
```

Examples:

```text
Markdown source artifact
    ↓
Obsidian note under References/

PlantUML source
    ↓
generated SVG

Engineering artifact
    ↓
Canvas node

Artifact metadata
    ↓
Base row
```

---

# View Types

Initial view types:

```text
Markdown
ObsidianNote
BaseRow
CanvasNode
PlantUMLSource
GeneratedSVG
StaticSitePage
AIContextBundle
```

---

# Source Versus Generated

## Source Artifacts

Examples:

- Markdown artifacts
- PlantUML `.puml` files
- source templates
- source Base definitions
- source Canvas definitions when intentionally authored

## Generated Artifacts

Examples:

- SVG diagrams
- copied Obsidian notes
- generated Canvas files
- generated Bases
- static site pages
- AI context bundles

Generated artifacts should be reproducible.

---

# Publication Flow

```text
Source Repository
    ↓
Canonical Artifact
    ↓
Validation
    ↓
Adapter
    ↓
Publication Target
    ↓
Publication View
```

---

# Obsidian Publication Model

Target structure:

```text
References/
  career-system/
  motorweb/
  linux-dev-env/
  skills/
  engineering-framework/
```

Administrative target folders:

```text
Templates/
Templates/Bases/
Attachments/
```

---

# Visibility

Publication views may be:

```text
Private
Published
Draft
Internal
```

Visibility controls whether an artifact is appropriate for public publication.

---

# Learning Outcomes

After implementing this model we expect to improve understanding of:

## Engineering

- source/view separation
- repository ownership
- generated artifact boundaries

## Automation

- copy pipelines
- generation pipelines
- repeatable publication
- future static-site publishing

## Publishing

- Obsidian Publish
- References folder layout
- public/private boundary management

---

# Framework Improvements

This model defines publication as a view over canonical source artifacts.

It supports future adapters without changing the source artifact model.

---

# Related Artifacts

- [[DM-CS-001-engineering-knowledge-meta-model]]
- [[DM-CS-002-engineering-artifact-relationship-model]]
- [[ARCH-CS-003-engineering-knowledge-repository]]
- [[ADR-CS-003-canonical-markdown-is-source-of-truth]]

---

# Notes

Publication views are not the same as source artifacts.

This distinction protects EKF from tool lock-in.
