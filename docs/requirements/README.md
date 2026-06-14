---
id: RS-CS-README-001
type: requirements-readme
project: career-system
status: draft
created: 2026-06-14
updated: 2026-06-14
tags:
  - requirements
  - career-system
  - motorweb
  - markdown
---

# Career System Requirements System v0.1

## Purpose

The Requirements System is a Requirements-as-Markdown framework for capturing useful, traceable requirements that can support real project delivery.

Markdown files are the source of truth. Trello, Jira, Confluence, OpenAPI, dashboards, and reports are generated or downstream views.

## Primary Business Goal

The top-level Career System business objective is to help Paul obtain suitable employment by producing high-quality application packages and supporting artifacts.

This includes:

- job opportunity evaluation
- gap analysis
- application prioritization
- resume tailoring
- application package generation
- interview preparation
- skills and glossary development

## Motorweb Relationship

Motorweb is the technical implementation platform that consumes Career System data and requirements.

Motorweb initially provides access to Career System data through:

- command line workflows
- PostgreSQL tables and SQL queries
- REST APIs
- OpenAPI contracts
- dashboard/table views
- future React frontend
- future JD ingestion UI

## Source of Truth

```text
Career System Requirements Markdown
        ↓
Generated / downstream artifacts
        ↓
Trello, Jira, OpenAPI, SQL, dashboards, documentation
```

## Folder Structure

```text
docs/requirements/
├── README.md
├── epics/
├── stories/
├── prerequisites/
├── acceptance-criteria/
├── uat/
├── releases/
├── indexes/
├── reference/
├── glossary/
├── architecture/
│   └── adr/
├── data-model/
├── openapi/
└── trello/
```

## Artifact Types

| Type | Prefix | Purpose |
|---|---|---|
| Business Requirement | BR | Business outcome or need |
| Functional Requirement | FR | System behavior needed to support a business outcome |
| Technical Requirement | TR | Implementation/platform requirement |
| Epic | EPIC | Large business or platform objective |
| User Story | US | Deliverable unit of work |
| Prerequisite | PREREQ | Required condition before a story can proceed |
| Acceptance Criteria | AC | Objective completion criteria |
| UAT | UAT | User/business validation procedure |
| Release | REL | Group of stories delivered together |
| Data Model | DM | Data entities and relationships |
| API Requirement | API | REST/OpenAPI requirement |
| Architecture Decision Record | ADR | Design decision and rationale |
| Glossary Term | TERM | Shared project vocabulary |

## Traceability Goal

```text
Epic
 ↓
Story
 ↓
Prerequisite
 ↓
Acceptance Criteria
 ↓
UAT
 ↓
Data Model / API / Implementation
 ↓
Dashboard / Operational Use
```

## Initial Scope

Initial implementation scope:

- `EPIC-CS-001 Employment Acceleration System`
- `EPIC-MW-001 Career Center Platform`
- `REL-MW-0.1 PostgreSQL POC`
- `US-MW-001 PostgreSQL Environment Ready`

