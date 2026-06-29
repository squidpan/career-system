# ARCH-CS-006 EKF Validation Architecture

Status: Draft

## TL;DR

- EKF validation checks engineering artifacts against standards, templates, metadata rules, naming rules, and relationship rules.
- Validation turns EKF from documentation into an executable engineering framework.
- The validator should report errors, warnings, and improvement suggestions.
- Validation supports future commands such as `ekf validate`, `ekf doctor`, and `ekf publish`.

---

# Purpose

Define the architecture for validating Engineering Knowledge Framework artifacts.

---

# Context

EKF now has:

- standards
- artifact types
- templates
- metadata rules
- naming rules
- relationships
- PlantUML diagrams
- publishing adapters

As the number of artifacts grows, manual review will become unreliable.

A validator provides repeatable quality checks before artifacts are committed, published, or adapted into knowledge platforms.

---

# Validation Goals

The validator should:

- confirm artifact identifiers are valid
- detect duplicate identifiers
- confirm filenames match identifiers
- confirm required metadata exists
- confirm required sections exist
- confirm categories follow EKF conventions
- confirm links point to valid artifacts where possible
- confirm PlantUML files exist where referenced
- report issues clearly
- support future automation

---

# Non-Goals

The validator should not:

- replace engineering judgment
- decide whether content is “good”
- force unnecessary bureaucracy
- block experimentation too early
- require all artifacts to be perfect before useful work can continue

---

# Validation Pipeline

```text
Source Repository
    ↓
Artifact Discovery
    ↓
Artifact Parsing
    ↓
Rule Evaluation
    ↓
Validation Report
    ↓
Fix / Approve / Publish
```

---

# Major Components

## Artifact Discovery

Find candidate EKF artifacts.

Examples:

- Markdown files under `docs/requirements/`
- PlantUML files under `docs/requirements/diagrams/`
- future Obsidian template files
- future Canvas files

## Artifact Parser

Extract structure from artifacts.

Parser responsibilities:

- filename
- identifier
- artifact type
- YAML metadata
- headings
- links
- related artifacts
- code block references

## Rule Engine

Applies validation rules.

Rule categories:

- identity rules
- metadata rules
- structure rules
- relationship rules
- folder rules
- diagram rules
- publishing rules

## Validation Report

Produces human-readable output.

Example:

    PASS  ARCH-CS-002 identifier format
    PASS  ARCH-CS-002 required metadata
    WARN  ARCH-CS-002 missing Architecture Diagram section
    FAIL  TMP-CS-002 missing closing template body

## Fix Guidance

Where possible, validator output should include suggested fixes.

Example:

    FAIL  Missing required section: Learning Outcomes
    FIX   Add "# Learning Outcomes" section before "# Framework Improvements"

---

# Severity Levels

## Error

Must be fixed before publication.

Examples:

- duplicate identifier
- invalid filename
- missing required metadata
- malformed YAML

## Warning

Should be reviewed.

Examples:

- missing recommended section
- no related artifacts
- missing TL;DR
- no references

## Info

Helpful observation.

Examples:

- artifact has no outbound links
- artifact has not been updated recently
- artifact may need review

---

# Validation Rule Types

Initial rule types:

```text
IdentifierRule
FilenameRule
MetadataRule
SectionRule
CategoryRule
StatusRule
LinkRule
DiagramRule
RelationshipRule
PublicationRule
```

---

# Future CLI Commands

## ekf validate

Validate artifacts.

Example:

    ekf validate docs/requirements

## ekf doctor

Diagnose repository health.

Example:

    ekf doctor

## ekf publish

Validate before publishing.

Example:

    ekf publish --target obsidian

---

# Validation Report Example

```text
EKF Validation Report

Files scanned: 128
Artifacts found: 94
Errors: 0
Warnings: 7
Info: 12

PASS  No duplicate identifiers
PASS  All required metadata present
WARN  3 artifacts missing Related Artifacts
WARN  2 PlantUML diagrams missing README references
```

---

# Learning Outcomes

## Technical

- Markdown parsing
- YAML parsing
- file discovery
- validation rule design

## Engineering

- executable documentation standards
- quality gates
- artifact lifecycle management

## Operational

- pre-commit checks
- release validation
- publish readiness checks

---

# Framework Improvements

This architecture introduces validation as an executable layer of EKF.

It creates the bridge from standards and templates to future automation.

---

# Related Artifacts

- [[ARCH-CS-002-engineering-knowledge-authoring-system]]
- [[EKF-validation-pipeline]]
- [[DM-CS-001-engineering-knowledge-meta-model]]
- [[DM-CS-004-artifact-type-model]]
- [[TMP-CS-011-template-authoring-guide]]
- [[STD-CS-002-engineering-artifact-identification-and-naming-standard]]
- [[STD-CS-003-obsidian-metadata-standard]]
- [[STD-CS-004-document-structure-standard]]

---

# Notes

The first implementation should be simple.

Start with read-only validation.

Do not auto-fix artifacts until validation behavior is trusted.
