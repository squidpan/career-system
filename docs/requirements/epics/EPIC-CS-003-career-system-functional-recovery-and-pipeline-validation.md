---
id: EPIC-CS-003
project: career-system
type: epic
status: completed

categories:
  - "[[Epics]]"
  - "[[Requirements]]"

tags:
  - career-system
  - operational-recovery
  - pipeline-validation
  - application-package
  - regression

description: Restore the Career System JD-to-Application Package workflow and establish a verified operational baseline.

created: 2026-07-14
updated: 2026-07-16
---

# EPIC-CS-003 Career System Functional Recovery and Pipeline Validation

## TL;DR

- Functional recovery from normalized JD through Application Package is complete.
- Deterministic Resume Asset selection now supplies the validated final-mile generators.
- LSEG and Broadridge reproduce all six core artifacts byte-for-byte.
- Operational procedures and failure safeguards are documented.
- Traceability, Implementation Order, and sprint closeout are complete.
- Engineering knowledge discovered during recovery remains queued for separate EFK review.

---

# Purpose

Restore Career System to a fully operational state capable of producing complete, validated Application Packages from normalized Job Descriptions while preserving the quality achieved by previous successful application workflows.

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

Functional recovery is complete for the validated operational boundary:

    normalized JD
        to deterministic Resume Asset selection
        to Full Resume generation
        to ATS Resume generation
        to HTML and ATS text export
        to complete Application Package

The existing final-mile generators were preserved and reconnected through
approved role-family Resume Assets.

Validated content profiles currently include:

- BA
- Product
- Support
- Default fallback

LSEG and Broadridge were regenerated in isolated output roots. For each
role, all six core artifacts matched the existing validated package
byte-for-byte.

Application Package generation now validates required inputs before
creating the package directory. Missing required inputs produce a
nonzero failure and no partial package.

Raw JD capture, JD normalization, candidate analysis, and other upstream
decision-support stages remain separate capabilities outside the recovered
final orchestration command.

Traceability synchronization, Implementation Order updates, stash
disposition, and sprint closeout are complete.

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

- deterministic Resume Asset selection from normalized JD metadata
- Professional Summary bridge-artifact publication
- FRBNY experience bridge-artifact publication
- Full Resume Markdown generation
- Full Resume HTML generation
- ATS Resume Markdown generation
- ATS Resume HTML generation
- ATS text generation
- complete Application Package generation
- required-input preflight validation
- partial-package prevention
- isolated-output support
- LSEG and Broadridge regression validation
- operational recovery documentation
- recovery runbook updates
- recovery traceability and closeout updates

## Existing Upstream Capabilities

The repository retains separate upstream capabilities including:

- raw JD capture
- JD normalization
- role generation
- candidate intelligence
- candidate matching
- candidate strategy
- candidate explainability
- resume tailoring guidance
- resume bullet ranking

These capabilities were not all incorporated into the recovered final
orchestration command.

## Excluded

- orchestration from raw clipped JD
- automatic JD normalization inside the recovered final command
- broad candidate-decision pipeline redesign
- dynamic AI generation of Resume Assets
- major architectural redesign
- repository-wide identifier renumbering
- repository-wide metadata normalization
- broad EFK refactoring
- new product features unrelated to operational recovery

---

# Success Criteria

Functional recovery criteria:

- normalized JDs produce complete Application Packages — PASS
- deterministic role-family Resume Asset selection operates — PASS
- required Full Resume and ATS Resume artifacts are generated — PASS
- required Application Package files are present and non-empty — PASS
- missing required inputs cause detectable failure — PASS
- missing-input failure creates no partial package — PASS
- LSEG Application Package is regenerated — PASS
- Broadridge Application Package is regenerated — PASS
- LSEG six-artifact regression comparison passes — PASS
- Broadridge six-artifact regression comparison passes — PASS
- isolated execution preserves repository state — PASS
- operational procedures are documented — PASS

Epic closeout criteria:

- Implementation Order is synchronized — PASS
- recovery traceability is finalized — PASS
- US-CS-060 is completed — PASS
- sprint closeout artifact is completed — PASS
- remaining stashes are explicitly carried forward or resolved — PASS

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

Recovery story status:

- [[US-CS-056-restore-end-to-end-workflow-orchestration]] — completed
- [[US-CS-057-restore-final-application-package-generation]] — completed
- [[US-CS-058-regression-validation-against-historical-application-packages]] — completed
- [[US-CS-059-operational-verification-and-recovery-runbook]] — completed
- [[US-CS-060-recovery-traceability-and-implementation-updates]] — completed

Functional implementation and operational verification are complete.

The final story synchronized traceability, implementation planning,
Epic status, sprint closeout, and carried-forward recovery artifacts.

---

# Recovery Phases

## Phase 1 — Recovery Planning

Status: completed

Recovery scope, regression anchors, and supporting stories were defined.

## Phase 2 — Pipeline Restoration

Status: completed

Deterministic Resume Asset selection, final-mile orchestration, and
Application Package generation were restored.

## Phase 3 — Regression Validation

Status: completed

LSEG and Broadridge each matched six validated core artifacts
byte-for-byte.

## Phase 4 — Operational Hardening

Status: completed

Required-input preflight validation, partial-package prevention, isolated
output support, and the operational runbook were completed.

## Phase 5 — Recovery Closeout

Status: completed

Completed work:

- completed US-CS-060
- synchronized Implementation Order
- finalized RTM-CS-002 recovery traceability
- created the sprint closeout artifact
- removed the superseded recovery Epic draft stash
- explicitly carried forward the Resume Asset standard draft for EFK review
- updated this Epic to completed

---

# Validation Strategy

Recovery validation used:

- LSEG Senior Business Analyst
- Broadridge Product Analyst
- Citi Application and Production Support

Validation included:

- deterministic role-family routing
- bridge-artifact generation
- Full Resume Markdown and HTML generation
- ATS Resume Markdown, HTML, and text generation
- required Application Package completeness
- manifest and submission-notes presence
- isolated-output execution
- missing-required-input failure behavior
- partial-package prevention
- byte-for-byte regression comparison

Results:

- LSEG: 6 of 6 core artifacts matched — PASS
- Broadridge: 6 of 6 core artifacts matched — PASS
- missing ATS text negative test — PASS
- no partial package after failure — PASS

Detailed evidence:

- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-ARCHITECTURE]]
- [[RECOVERY-JOURNAL]]
- [[RECOVERY-ATS-APPLICATION-PACKAGE-WORKFLOW-2026-07-01]]

---

# Deliverables

Completed deliverables:

- validated normalized-JD-to-Application-Package workflow
- approved BA, Product, Support, and Default Resume Assets
- deterministic Resume Asset selector
- final-mile orchestration wrapper
- JD-to-Application Package orchestration wrapper
- isolated Application Package generation
- required-input preflight validation
- partial-package prevention
- LSEG and Broadridge regression evidence
- recovery validation report
- recovery architecture document
- recovery journal
- operational recovery runbook
- completed US-CS-056 through US-CS-059

Completed closeout deliverables:

- completed US-CS-060
- updated Implementation Order
- finalized RTM-CS-002 recovery traceability
- completed sprint closeout artifact
- explicit stash disposition
- completed Epic status

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
- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-ARCHITECTURE]]
- [[RECOVERY-JOURNAL]]
- [[RECOVERY-ATS-APPLICATION-PACKAGE-WORKFLOW-2026-07-01]]
- [[US-CS-056-restore-end-to-end-workflow-orchestration]]
- [[US-CS-057-restore-final-application-package-generation]]
- [[US-CS-058-regression-validation-against-historical-application-packages]]
- [[US-CS-059-operational-verification-and-recovery-runbook]]
- [[US-CS-060-recovery-traceability-and-implementation-updates]]
- [[US-CS-RECOVERY-001-reconnect-new-pipeline-to-application-package]]
- [[ARCH-CS-001-engineering-operating-system]]

---

# References

- [[RECOVERY-VALIDATION-ATS-PIPELINE-2026-07]]
- [[RECOVERY-ARCHITECTURE]]
- [[RECOVERY-JOURNAL]]
- [[RECOVERY-ATS-APPLICATION-PACKAGE-WORKFLOW-2026-07-01]]
- [[IMPLEMENTATION-ORDER-v0.4]]
- LSEG regression package
- Broadridge regression package
- Recovery operational branch

---

# Notes

This Epic serves as the engineering program charter for the 2026 Career System operational recovery effort.

It intentionally separates operational recovery from ongoing Engineering Knowledge Framework evolution.

Existing duplicate identifiers are preserved during this effort and will be addressed separately through future identifier governance work.
