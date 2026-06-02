# Teal Export Workflow

## Purpose

Generate a clean resume-only artifact for Teal import.

## Source

```text
data/resume-versions/assembled/*.md
```

## Target

```text
data/resume-versions/teal-export/*.md
```

## Export Rules

Exclude:

- YAML frontmatter
- Assembly Summary
- Tailoring Checklist
- JD Keywords Detected
- Manual Tailoring Steps
- internal IDs
- run IDs
- application package IDs

Include:

- contact
- target positioning
- professional summary
- core strengths
- work experience
- education
- publications
- skills
- languages

## Design Decision

Career System remains the source of truth.

Teal is a downstream consumer for import, match analysis, and PDF export.
