---
id: NOTE-CS-001
project: career-system
type: note
status: completed

categories:
  - [[Recovery]]
  - [[Requirements]]
  - [[Planning]]

tags:
  - recovery
  - reconnaissance
  - operational-baseline
  - planning

description: Repository reconnaissance performed before authoring the Career System Functional Recovery Planning Package.

created: 2026-07-14
updated: 2026-07-14
---

# Recovery Requirements Reconnaissance (2026-07-14)

## Purpose

Capture the verified repository state before beginning the Career System Functional Recovery Planning Package. This document records the current operational baseline, summarizes key findings, identifies decisions that will guide recovery planning, and distinguishes recovery work from future Engineering Knowledge Framework (EFK) improvements.

---

# Repository Baseline

| Item | Value |
|------|-------|
| Repository | career-system |
| Branch | `ops/recover-ats-html-workflow` |
| HEAD | `ca5b3ae` |
| Working Tree | Clean |
| Date | 2026-07-14 |
| Preserved Stash | `ops: preserve EPIC-CS-003 recovery draft` |

The preserved stash was inspected but intentionally not applied.

---

# Repository Summary

Reconnaissance confirmed the current requirements repository contains:

- 191 requirements-related Markdown artifacts
- Engineering standards, templates, architecture, ADRs, contexts, data models, traceability, and implementation planning
- Existing Career System and Motorweb requirements
- Operational recovery documentation
- Existing recovery-related stories and bugs
- Regression evidence for previously successful application packages

The repository provides sufficient engineering context to begin formal recovery planning.

---

# Key Findings

## RR-001 — Duplicate artifact identifiers

Duplicate identifiers currently exist for several published artifacts.

Examples include:

- `EPIC-CS-002`
- `CTX-CS-002`
- `EPIC-MW-002`

### Decision

Operational recovery will **not** renumber existing artifacts.

Identifier governance will be addressed separately as future EFK work.

---

## RR-002 — Recovery Epic does not yet exist

No committed `EPIC-CS-003` currently exists.

A partial draft was found only inside the preserved Git stash.

### Decision

A new `EPIC-CS-003` will be authored from scratch.

The preserved stash will remain as historical reference until the replacement Epic has been committed.

---

## RR-003 — Existing recovery story

The repository currently contains:

`US-CS-RECOVERY-001`

This identifier does not follow the current sequential numbering standard.

### Decision

Future recovery stories will continue using sequential identifiers beginning with:

- `US-CS-056`

The existing recovery story will be evaluated for migration or supersession rather than modified during initial recovery planning.

---

## RR-004 — Framework standards have evolved

The operational branch contains older copies of several EFK standards and templates.

The dedicated EFK branch contains newer conventions, including:

- unquoted Obsidian category links
- updated metadata conventions
- improved authoring guidance

### Decision

Recovery planning will follow the newer conventions for newly authored artifacts while avoiding repository-wide normalization during operational recovery.

---

## RR-005 — Existing recovery evidence is sufficient

Repository inspection confirmed the existence of:

- architecture documentation
- contexts
- ADRs
- standards
- traceability artifacts
- implementation order
- regression packages
- recovery run documentation

Recovery planning can therefore proceed without additional discovery work.

---

# Recovery Scope

This planning effort will focus on:

- Functional recovery of the JD-to-Application Package workflow
- Operational planning
- Requirements
- Traceability
- Recovery stories
- Validation strategy

The following work is intentionally excluded:

- Repository-wide identifier cleanup
- Metadata normalization across all artifacts
- EFK framework redesign
- Historical artifact refactoring

---

# Confirmed Planning Decisions

The following decisions were established during reconnaissance:

- Preserve existing historical identifiers.
- Create `EPIC-CS-003`.
- Create sequential recovery stories beginning with `US-CS-056`.
- Keep the preserved recovery stash until replacement artifacts are committed.
- Separate operational recovery from EFK evolution.
- Record framework improvement opportunities separately.

---

# Immediate Next Artifacts

The following artifacts will be authored next:

1. EFK Candidate Register
2. `EPIC-CS-003 Career System Functional Recovery and Pipeline Validation`
3. Recovery user stories (`US-CS-056+`)
4. Recovery implementation roadmap
5. Traceability updates

---

# Framework Knowledge Captured

The following observations should be proposed to the Engineering Knowledge Framework project:

- Introduce a lightweight **Engineering Note** artifact.
- Require minimal YAML metadata for all engineering documents.
- Document branch-aware framework evolution.
- Improve identifier governance guidance.
- Define migration guidance for framework changes.
- Capture operational recovery lessons as reusable engineering knowledge.

---

# Notes

This reconnaissance establishes the operational baseline for the Career System Functional Recovery Planning Package.

Future planning artifacts should reference this document rather than repeating repository discovery activities.
