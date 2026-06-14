---
id: API-MW-003
type: openapi-requirement
project: motorweb
epic: EPIC-MW-001
release: future
status: draft
priority: high
tags:
  - requirements
  - motorweb
  - openapi
  - application-packages-api
created: 2026-06-14
updated: 2026-06-14
---

# API-MW-003 Application Packages API

## Purpose

Define REST API requirements for viewing application package records.

## Resource

```text
/jobs/application-packages
/jobs/application-packages/{application_package_id}
```

## Related Data Model

- [[DM-MW-003 Application Package Entity]]
- [[DM-MW-005 Resume Entity]]

## Candidate Endpoints

| Method | Path | Purpose |
|---|---|---|
| GET | /jobs/application-packages | List application packages |
| GET | /jobs/application-packages/{application_package_id} | Retrieve one application package |

## Response Data

Responses should include application package identifier, role, resume, cover letter if applicable, package status, and artifact file references.

## Related Glossary

- [[TERM-CS-001 Application Package]]
- [[TERM-CS-005 Resume Version]]
