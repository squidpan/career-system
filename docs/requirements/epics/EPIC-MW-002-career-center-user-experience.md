---
id: EPIC-MW-002
type: epic
project: motorweb
status: draft
priority: medium
tags:
  - requirements
  - motorweb
  - frontend
  - react
  - user-experience
created: 2026-06-14
updated: 2026-06-14
---

# EPIC-MW-002 Career Center User Experience

## Epic Statement

Create a simple, modern, elegant Career Center user experience that allows Paul to view, understand, and eventually manage Career System data through a browser-based UI.

## Business Context

The initial Motorweb POC exposes Career System data through command line, SQL, and REST APIs. A future React frontend will make the same data easier to view, demonstrate, and operate.

## Business Objective

Provide a clean dashboard and landing page that demonstrates Paul’s ability to connect requirements, data, APIs, and frontend experience into a usable career platform.

## Scope

Initial UX scope may include:

- Landing page
- Job roles dashboard
- Job role detail view
- Application package view
- Gap analysis dashboard
- JD ingestion UI in a later phase

## Out of Scope for Initial POC

- Full authentication
- Multi-user administration
- Complex workflow engine
- Production hosting
- Advanced visualizations

## Candidate Stories

- US-MW-020 Landing Page
- US-MW-021 Job Roles Dashboard
- US-MW-022 Job Details View
- US-MW-023 Application Package View
- US-MW-024 Gap Analysis Dashboard
- US-MW-025 JD Ingestion UI

## Traceability

This epic depends on the Motorweb backend and API foundations:

- [[EPIC-MW-001 Career Center Platform]]
- [[API-MW-001 Roles API]]
- [[API-MW-002 Job Descriptions API]]
- [[API-MW-003 Application Packages API]]
- [[API-MW-004 Tracker Events API]]

## Learning Objective

This epic supports Paul’s learning goals around React, frontend architecture, and writing useful UI-centered user stories with clear behavior, states, validation rules, and UAT.
