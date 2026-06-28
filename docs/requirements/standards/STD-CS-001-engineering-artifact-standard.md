# STD-CS-001 Engineering Artifact Standard

Status: Draft

## Purpose

Define standard engineering artifact types, prefixes, and purposes used by the Career System Engineering Operating System.

## Artifact Types

| Prefix | Artifact Type | Primary Question |
|---|---|---|
| PR | Principle | What do we believe? |
| CTX | Context | Why does this exist? |
| EPIC | Epic | What business outcome do we want? |
| US | User Story | What should be built? |
| AC | Acceptance Criteria | How do we know it is done? |
| ARCH | Architecture | How does it fit together? |
| ADR | Architecture Decision Record | Why did we choose this approach? |
| STD | Standard | What rules should we follow? |
| DM | Data Model | What information exists? |
| API | API Contract | How do systems communicate? |
| UAT | User Acceptance Test | How is user-facing behavior validated? |
| BUG | Bug | What is broken? |
| SPR | Sprint | What did we accomplish during an iteration? |
| REL | Release | What version was delivered? |
| RB | Runbook | How do we operate or recover it? |
| GLO | Glossary | What does this term mean? |
| SPK | Spike | What do we need to research or prove? |

## Naming Convention

Use this general pattern:

```text
<PREFIX>-<DOMAIN>-<NUMBER>-short-description.md
```

Examples:

```text
ADR-CS-001-career-system-reference-implementation.md
ARCH-CS-001-engineering-operating-system.md
STD-CS-001-engineering-artifact-standard.md
PR-CS-001-small-incremental-changes.md
US-MW-013C-api-gateway-learning-spike.md
```

## Domain Codes

| Code | Meaning |
|---|---|
| CS | Career System |
| MW | Motorweb |
| LNX | Linux Dev Environment |
| OBS | Obsidian |
| API | API / OpenAPI |
| DB | Database |

## Ownership Model

| Artifact | Typical Owner |
|---|---|
| Principle | Architect |
| Context | Product Owner / Business Analyst |
| Epic | Product Owner |
| Story | Business Analyst / Developer |
| ADR | Architect |
| Architecture | Architect |
| Data Model | Data Architect |
| OpenAPI | API Designer |
| Runbook | Operations |
| Standard | Platform Engineering |
| Glossary | Everyone |
| Sprint | Scrum Team |
| Release | Release Manager |

## Notes

In this repository, one person may perform multiple roles.

The purpose of ownership is not bureaucracy. The purpose is to encourage thinking from the correct engineering perspective.
