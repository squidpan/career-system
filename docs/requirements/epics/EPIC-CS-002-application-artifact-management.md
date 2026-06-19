# EPIC-CS-002 Application Artifact Management

Status: Draft

## Epic Goal

As a Career System user,
I want each application tracker row to reference its related artifacts,
so that normalized JDs, raw JDs, resumes, notes, and application packages can be accessed from Markdown, CSV, PostgreSQL, scripts, and REST APIs.

## Business Value

Application tracking should not only show status. It should also connect each application to the supporting evidence and generated artifacts used for that application.

This enables:

- Obsidian navigation
- SQL querying
- REST API payloads
- Motorweb Career Center integration
- Interview preparation
- Resume/JD traceability

## Scope

Includes:

- Artifact references in tracker data
- Artifact metadata propagation
- Dashboard links
- PostgreSQL artifact text loading
- REST API detail endpoints

## Target Architecture

Application Package
→ submission-notes.md
→ applications.csv
→ applications.md
→ PostgreSQL
→ REST API
→ Motorweb dashboard

## Related Stories

- US-CS-053 Add Artifact References to Application Tracker
- US-CS-054 Application Artifact Metadata Propagation
- US-CS-055 Application Artifact Dashboard Links
- US-MW-006 Load Application Artifacts into PostgreSQL
- US-MW-007 Application Detail REST APIs
