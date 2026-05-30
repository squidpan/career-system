# Resume System README

The Career System resume module is built around a simple rule:

> Masters are the inventory. Role-specific resumes are generated derivatives.

## Current master set

```text
master-ba-resume.md
master-sre-resume.md
```

## Why only two masters?

You currently target two broad career lanes:

1. Senior BA / Application Support / Enterprise Delivery
2. SRE / Production Support / Market Data Operations

More masters would create maintenance overhead and drift.

## Working model

```text
Source PDFs
    ↓
Markdown source extracts
    ↓
Master BA / Master SRE
    ↓
Role-specific markdown resume
    ↓
Teal resume builder
    ↓
PDF export
    ↓
Application package
```

## Source of truth

- Career System owns markdown masters and version history.
- Teal owns formatting/export.
- Obsidian owns human review and thinking.
