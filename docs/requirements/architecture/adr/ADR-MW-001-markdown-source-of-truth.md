---
id: ADR-MW-001
type: architecture-decision-record
project: motorweb
status: draft
created: 2026-06-14
updated: 2026-06-14
tags:
  - adr
  - requirements
  - motorweb
  - markdown
---

# ADR-MW-001 Markdown Requirements Are Source of Truth

## Status

Draft

## Context

Career System uses source artifacts to generate target artifacts. Requirements System follows the same pattern.

## Decision

Markdown requirement files with YAML metadata are the source of truth.

Trello, Jira, Confluence, OpenAPI, dashboards, and reports are downstream generated or manually synchronized views.

## Rationale

Markdown files are version-controlled, readable, portable, AI-friendly, Obsidian-friendly, and suitable for future automation.

## Consequences

- Requirement changes should start in Markdown.
- Trello and Jira should not become authoritative.
- Traceability can be maintained through file links and metadata.

## Related Artifacts

- [[EPIC-MW-001 Career Center Platform]]
- [[REL-MW-0.1 PostgreSQL POC]]

