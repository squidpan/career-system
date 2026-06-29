# DM-CS-005 EKF Validation Result Model

Status: Draft

## TL;DR

- Defines the data model for EKF validation results.
- Supports future commands such as `ekf validate`, `ekf doctor`, and `ekf publish`.
- Validation results should identify the artifact, rule, severity, message, and suggested fix.
- This model turns validation output into structured engineering knowledge.

---

# Purpose

Define the conceptual data model for Engineering Knowledge Framework validation results.

---

# Scope

This model covers:

- validation runs
- validation rules
- validation findings
- severity levels
- suggested fixes

It does not define implementation code yet.

---

# Core Concepts

```text
ValidationRun
    ↓
ValidationFinding
    ↓
ValidationRule
    ↓
Artifact
```

---

# Entity Definitions

## ValidationRun

Purpose:

Represents one execution of EKF validation.

Attributes:

```text
run_id
started_at
completed_at
repository
path_scanned
files_scanned
artifacts_found
errors
warnings
info
status
```

---

## ValidationRule

Purpose:

Defines one validation rule.

Attributes:

```text
rule_id
rule_type
name
description
severity
applies_to
enabled
```

Examples:

```text
ID_FORMAT
FILENAME_MATCHES_ID
REQUIRED_METADATA
REQUIRED_SECTION
BROKEN_LINK
DUPLICATE_ID
```

---

## ValidationFinding

Purpose:

Represents one validation issue or result.

Attributes:

```text
finding_id
run_id
artifact_id
file_path
rule_id
severity
message
fix_hint
line_number
status
```

---

## Severity

Purpose:

Classifies the importance of a validation finding.

Values:

```text
Error
Warning
Info
```

---

# Relationships

```text
ValidationRun contains ValidationFinding

ValidationFinding references ValidationRule

ValidationFinding references EngineeringArtifact

ValidationRule applies to ArtifactType
```

---

# Example Validation Finding

```text
finding_id: VF-001
artifact_id: TMP-CS-002
file_path: docs/requirements/templates/TMP-CS-002-adr-template.md
rule_id: REQUIRED_SECTION
severity: Error
message: Missing required section: Validation Rules
fix_hint: Add "# Validation Rules" after "# Template Body"
```

---

# Validation Output Views

Validation results may be represented as:

- console output
- Markdown report
- JSON
- CSV
- Obsidian note
- GitHub Action summary
- future dashboard row

---

# Learning Outcomes

## Technical

- validation result modeling
- CLI report design
- JSON/report serialization

## Engineering

- quality gates
- repeatable review
- executable standards

## Operational

- pre-commit checks
- release readiness
- publish readiness

---

# Framework Improvements

This model makes validation results first-class engineering artifacts.

It allows validation output to become part of the Engineering Knowledge Graph.

---

# Related Artifacts

- [[ARCH-CS-006-ekf-validation-architecture]]
- [[DM-CS-001-engineering-knowledge-meta-model]]
- [[DM-CS-004-artifact-type-model]]
- [[TMP-CS-011-template-authoring-guide]]

---

# Notes

The first implementation should prioritize human-readable console output.

Structured output can come later after the validation rules stabilize.
