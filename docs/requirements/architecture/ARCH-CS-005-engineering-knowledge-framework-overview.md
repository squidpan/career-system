# ARCH-CS-005 Engineering Knowledge Framework Overview

Status: Draft

## TL;DR

- The Engineering Knowledge Framework (EKF) organizes engineering knowledge so it can be authored, validated, reused, published, and improved.
- The Engineering Operating System (EOS) describes how engineering work operates.
- EKF describes what engineering knowledge exists and how it is structured.
- Career System is the first reference implementation.
- Git repositories are the source of truth.
- Knowledge platforms such as Obsidian consume and publish EKF artifacts through adapters.

---

# Purpose

Provide the high-level overview of the Engineering Knowledge Framework and explain how its major architecture components relate.

---

# Context

Career System has evolved from an employment acceleration project into the reference implementation of a broader engineering methodology.

The framework now includes:

- principles
- standards
- context
- epics
- stories
- architecture
- ADRs
- templates
- validation
- repositories
- publishing adapters
- learning outcomes

---

# Conceptual Model

```text
Engineering Operating System
        ↓
Engineering Knowledge Framework
        ↓
Engineering Knowledge Repository
        ↓
Authoring System
        ↓
Engineering Artifacts
        ↓
Validation
        ↓
Knowledge Platform Adapters
        ↓
Published Knowledge Views
```

---

# Architecture View

```text
                 Engineering Operating System
                           (EOS)
                              │
                              ▼
              Engineering Knowledge Framework
                           (EKF)
                              │
      ┌───────────────────────┼───────────────────────┐
      ▼                       ▼                       ▼
 Authoring System      Knowledge Repository      Knowledge Lifecycle
      │                       │                       │
      └───────────────┬───────┴───────────────┬───────┘
                      ▼                       ▼
              Engineering Artifacts      Framework Improvement
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      Validation   Templates   Standards
                      │
                      ▼
             Knowledge Platform Adapters
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
    Obsidian      Static Site      AI Exports
```

---

# Major Architecture Components

## Engineering Operating System

Defines how engineering work operates.

Related artifact:

- [[ARCH-CS-001-engineering-operating-system]]

## Engineering Knowledge Authoring System

Defines how engineering artifacts are created, validated, stored, adapted, and published.

Related artifact:

- [[ARCH-CS-002-engineering-knowledge-authoring-system]]

## Engineering Knowledge Repository

Defines where engineering knowledge lives and how repositories participate in EKF.

Related artifact:

- [[ARCH-CS-003-engineering-knowledge-repository]]

## Engineering Knowledge Lifecycle

Defines how engineering knowledge evolves over time through learning and continuous improvement.

Related artifact:

- [[ARCH-CS-004-engineering-knowledge-lifecycle]]

---

# Core Standards

The EKF foundation currently includes:

- [[STD-CS-001-engineering-artifact-standard]]
- [[STD-CS-002-engineering-artifact-identification-and-naming-standard]]
- [[STD-CS-003-obsidian-metadata-standard]]
- [[STD-CS-004-document-structure-standard]]

---

# Core Principles

The EKF foundation currently includes:

- [[PR-CS-001-small-incremental-changes]]
- [[PR-CS-002-learn-by-building]]
- [[PR-CS-003-documentation-is-part-of-the-product]]
- [[PR-CS-004-consistency-reduces-cognitive-load]]
- [[PR-CS-005-knowledge-is-a-deliverable]]

---

# Reference Implementation

Career System is the initial reference implementation of EKF.

Motorweb, Linux Dev Environment, Skills, and future repositories may adopt the framework incrementally.

---

# Knowledge Platform Integration

Obsidian is the first target knowledge platform.

Future platforms may include:

- Obsidian Publish
- Quartz
- Jekyll
- Hugo
- Astro
- AI retrieval systems

EKF should remain platform-independent by using canonical Markdown and adapters.

---

# Learning Outcomes

After implementing this overview we expect to improve understanding of:

## Engineering

- framework architecture
- architectural views
- cross-repository knowledge flow
- artifact relationships

## Documentation

- overview documents
- architecture navigation
- framework entry points

## Publishing

- knowledge platform adapters
- Obsidian References structure
- static site readiness

---

# Framework Improvements

This overview provides a single entry point for understanding EKF.

It also clarifies the relationship between EOS, EKF, repositories, artifacts, validation, adapters, and publishing platforms.

---

# Related Artifacts

- [[ARCH-CS-001-engineering-operating-system]]
- [[ARCH-CS-002-engineering-knowledge-authoring-system]]
- [[ARCH-CS-003-engineering-knowledge-repository]]
- [[ARCH-CS-004-engineering-knowledge-lifecycle]]
- [[ADR-CS-003-canonical-markdown-is-source-of-truth]]

---

# Notes

This document should become the primary architecture entry point for the Engineering Knowledge Framework.
