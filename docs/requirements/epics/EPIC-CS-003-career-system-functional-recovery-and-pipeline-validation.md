---
id: EPIC-CS-003
project: career-system
type: epic
status: draft

categories:
  - [[Epics]]
  - [[Requirements]]

tags:
  - career-system
  - operational-recovery
  - pipeline-validation
  - application-package
  - regression

description: Restore the Career System JD-to-Application Package workflow and establish a verified operational baseline.

created: 2026-07-14
updated: 2026-07-14
---

# EPIC-CS-003 Career System Functional Recovery and Pipeline Validation

## TL;DR

- Restore the complete Career System operational workflow.
- Reconnect all pipeline stages from imported Job Description through final Application Package.
- Re-establish LSEG and Broadridge as regression baselines.
- Produce a repeatable, validated operational workflow.
- Capture engineering knowledge discovered during recovery for future EFK adoption.

---

# Purpose

Restore Career System to a fully operational state capable of producing complete, validated application packages from imported job descriptions while preserving the quality achieved by previous successful application workflows.

This Epic defines the overall recovery effort, its scope, planning, validation strategy, and relationship to future Engineering Knowledge Framework (EFK) improvements.

---

# Background

Career System has evolved significantly through multiple implementation phases.

Core capabilities including JD normalization, candidate matching, resume tailoring, resume enhancement, application summaries, ATS resume generation, and application packaging have all been developed independently.

Operational recovery is required to reconnect these capabilities into a single validated workflow.

Repository reconnaissance completed on 2026-07-14 confirmed that sufficient engineering artifacts, regression evidence, and historical implementation knowledge exist to begin structured recovery planning.

---

# Problem Statement

The Career System contains mature implementations of individual pipeline stages, but the end-to-end workflow no longer operates as a fully connected, validated system.

Manual reconstruction is currently required to generate complete application packages.

This recovery effort reconnects the existing pipeline, restores validated operational behavior, and establishes a repeatable engineering baseline for future enhancements.

---

# Current State

The repository currently contains mature implementations of many individual pipeline stages, including JD normalization, candidate analysis, resume generation, and application packaging.

However, the complete operational workflow is not yet functioning as a single validated pipeline.

Historical application packages remain available and provide the regression baseline for recovery.

Repository reconnaissance completed on 2026-07-14 confirmed that recovery can proceed using the existing engineering artifacts without requiring additional discovery work.

---

# Business Value

Successful completion of this Epic will:

- Restore the ability to rapidly produce high-quality application packages.
- Reduce manual intervention during job applications.
- Re-establish confidence in pipeline correctness.
- Provide repeatable operational validation.
- Create an engineering baseline for future enhancements.

---

# Recovery Principles

The recovery effort follows these principles:

- Restore proven functionality before introducing enhancements.
- Use successful historical application packages as regression evidence.
- Preserve validated business content.
- Make incremental, independently verifiable improvements.
- Separate operational recovery from framework evolution.
- Record engineering knowledge for later incorporation into EFK.

---

# Recovery Objectives

- Restore the end-to-end JD-to-Application Package workflow.
- Reconnect all pipeline stages.
- Validate generated artifacts against known-good packages.
- Eliminate manual reconstruction wherever practical.
- Improve traceability between pipeline artifacts.
- Establish a repeatable operational workflow.

---

# Scope

## Included

- JD normalization
- Candidate intelligence
- Resume recommendation
- Resume tailoring
- Resume enhancement
- Application summary generation
- ATS resume generation
- Full resume generation
- Application package generation
- Operational validation
- Regression testing
- Recovery planning artifacts
- Recovery runbooks
- Traceability updates

## Excluded

- Major architectural redesign
- Repository-wide identifier renumbering
- Repository-wide metadata normalization
- Broad EFK refactoring
- New product features unrelated to operational recovery

---

# Success Criteria

Recovery is complete when:

- New job descriptions successfully produce complete application packages.
- LSEG application package can be regenerated.
- Broadridge application package can be regenerated.
- Generated outputs match validated historical quality.
- Pipeline execution becomes repeatable.
- Recovery documentation is complete.
- Validation procedures are documented.

---

# Dependencies

- [[CTX-CS-001-employment-acceleration-system]]
- [[RECOVERY-REQUIREMENTS-RECONNAISSANCE-2026-07-14]]
- Existing application-package regression artifacts
- Existing standards and templates
- Existing operational recovery branch

---

# Risks

- Regression packages may not fully represent current pipeline behavior.
- Historical assumptions may no longer be valid.
- Multiple partially completed implementations may overlap.
- Existing identifier inconsistencies may complicate traceability.

These risks will be managed without expanding project scope.

---

# Story Breakdown

The following recovery stories are planned:

- [[US-CS-056]]
- [[US-CS-057]]
- [[US-CS-058]]
- [[US-CS-059]]
- [[US-CS-060]]

Additional stories may be introduced as recovery progresses.

---

# Recovery Phases

## Phase 1

Recovery planning

## Phase 2

Pipeline restoration

## Phase 3

Regression validation

## Phase 4

Operational hardening

## Phase 5

Recovery completion

---

# Validation Strategy

Recovery validation will use:

- LSEG Senior Business Analyst package
- Broadridge Product Analyst package

Validation includes:

- artifact completeness
- document structure
- generated HTML
- ATS text
- metadata
- package manifests
- submission notes
- regression comparisons

---

# Deliverables

Successful completion of this Epic will produce:

- A validated end-to-end JD-to-Application Package workflow
- A complete Recovery Planning Package
- Recovery Epic and supporting stories
- Updated implementation roadmap
- Updated traceability
- Recovery validation procedures
- Operational runbooks
- Verified regression results

---

# Learning Outcomes

## Technical

Improve understanding of pipeline integration and artifact generation.

## Engineering

Improve operational planning, traceability, and validation practices.

## Operational

Establish a repeatable recovery methodology for future engineering efforts.

---

# Framework Improvement Opportunities

The following observations should be considered for future EFK evolution:

- Lightweight Engineering Notes
- Minimal YAML metadata for all engineering documents
- Operational reconnaissance artifacts
- Recovery planning templates
- Framework migration guidance
- Identifier governance improvements

These improvements are intentionally outside the scope of this Epic.

---

# Related Artifacts

- [[CTX-CS-001-employment-acceleration-system]]
- [[RECOVERY-REQUIREMENTS-RECONNAISSANCE-2026-07-14]]
- [[US-CS-RECOVERY-001-reconnect-new-pipeline-to-application-package]]
- [[ARCH-CS-001-engineering-operating-system]]

---

# References

- LSEG regression package
- Broadridge regression package
- Recovery validation findings
- Recovery operational branch

---

# Notes

This Epic serves as the engineering program charter for the 2026 Career System operational recovery effort.

It intentionally separates operational recovery from ongoing Engineering Knowledge Framework evolution.

Existing duplicate identifiers are preserved during this effort and will be addressed separately through future identifier governance work.
