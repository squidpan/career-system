# TMP-CS-011 Template Authoring Guide

Status: Draft

## TL;DR

- Defines how Engineering Knowledge Framework templates are designed.
- Templates should teach engineering thinking, not merely enforce formatting.
- Every template should be understandable by humans and consumable by automation.
- Templates are first-class artifacts within EKF.

---

# Purpose

Define the principles, structure, and evolution of Engineering Knowledge Framework templates.

This guide serves as the architecture for all EKF templates.

---

# Why Templates Exist

Templates exist to reduce unnecessary decisions while improving consistency.

Good templates should:

- reduce cognitive load
- improve quality
- encourage complete thinking
- support validation
- support automation
- remain easy to read

Templates are guidance, not bureaucracy.

---

# Design Principles

## Teach Before Enforcing

A template should explain why a section exists.

## Encourage Thinking

Templates should prompt engineers to think about architecture, tradeoffs, validation, and learning.

## Consistency Over Creativity

Consistent artifacts improve navigation, search, validation, and publishing.

## Automation Friendly

Templates should be structured so metadata and sections can be validated automatically.

## Human First

Humans remain the primary audience.

Automation serves engineers—not the other way around.

---

# Template Anatomy

Every template follows a common structure.

```text
Metadata
    ↓
TL;DR
    ↓
Purpose
    ↓
Applies To
    ↓
Implements Standards
    ↓
Required Metadata
    ↓
Required Sections
    ↓
Recommended Sections
    ↓
Template Body
    ↓
Validation Rules
    ↓
Related Artifacts
    ↓
Notes
```

---

# Required Components

Every template should define:

- artifact purpose
- artifact scope
- required metadata
- required document sections
- recommended document sections
- validation expectations
- relationships to other artifacts

---

# Validation Philosophy

Validation should answer questions such as:

- Is the identifier valid?
- Is metadata complete?
- Are required sections present?
- Does the artifact belong in the correct folder?
- Does it reference related artifacts?
- Does it follow naming conventions?

Validation should never replace engineering judgment.

---

# Template Evolution

Templates evolve through practical use.

Possible improvements include:

- clearer guidance
- simpler structure
- improved metadata
- better validation
- new automation support
- better examples

Experience should drive template improvements.

---

# Adding New Artifact Types

When introducing a new artifact type:

1. Define the artifact type in the Artifact Type Model.
2. Assign an identifier prefix.
3. Create a canonical template.
4. Define validation rules.
5. Update README indexes.
6. Update Obsidian categories.
7. Update Bases.
8. Update Canvas views.
9. Update validators.
10. Update related architecture and standards.

---

# Relationship to Standards

Standards define the rules.

Templates implement those rules.

---

# Relationship to Validators

Validators verify template compliance.

Templates define what validators should expect.

---

# Relationship to Automation

Automation may:

- generate new artifacts
- validate metadata
- generate indexes
- publish documentation
- generate Bases
- generate Canvas views

Templates provide the structure that enables automation.

---

# Learning Outcomes

## Technical

- metadata modeling
- document validation
- template design

## Engineering

- consistent authoring
- documentation architecture
- reusable patterns

## Operational

- easier onboarding
- repeatable documentation
- scalable engineering knowledge

---

# Framework Improvements

This guide establishes templates as first-class engineering artifacts.

It also defines a repeatable process for expanding EKF without introducing inconsistency.

---

# Related Artifacts

- [[STD-CS-001-engineering-artifact-standard]]
- [[STD-CS-004-document-structure-standard]]
- [[DM-CS-004-artifact-type-model]]
- [[ARCH-CS-002-engineering-knowledge-authoring-system]]

---

# Notes

Templates should improve engineering thinking.

If a template merely enforces formatting, it has failed its purpose.
