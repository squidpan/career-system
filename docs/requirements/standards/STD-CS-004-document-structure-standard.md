# STD-CS-004 Document Structure Standard

Status: Draft

## TL;DR

- Engineering documents should follow a consistent structure.
- Readers should be able to understand the purpose within seconds.
- Longer documents should begin with a TL;DR.
- Markdown remains the primary content format.
- Obsidian links should be preferred over duplicated text.

---

# Purpose

Define a consistent document structure for Engineering Knowledge Framework (EKF) artifacts.

The goal is to reduce cognitive overhead while improving readability, navigation, and long-term maintainability.

---

# Design Principles

Documents should be:

- easy to scan
- easy to maintain
- easy to link
- easy to publish
- easy to automate

---

# Recommended Structure

```text
YAML Properties

H1 Title

TL;DR

Purpose

Context

Main Content

Related Artifacts

References

Notes
```

Not every document requires every section.

Use the sections appropriate for the artifact.

---

# YAML Properties

YAML metadata appears first.

See:

[[STD-CS-003-obsidian-metadata-standard]]

---

# H1 Title

Every document begins with a single H1.

Example:

```text
# ARCH-CS-001 Engineering Operating System
```

The H1 is the canonical title.

---

# TL;DR

Longer documents should include a TL;DR immediately after the title.

Purpose:

- quick review
- executive summary
- AI retrieval
- publishing

Typical size:

- 3–10 bullets

---

# Purpose

Describe why the artifact exists.

Readers should understand its intent within a few sentences.

---

# Context

Provide background when needed.

Not every artifact requires this section.

---

# Main Content

This is the primary engineering content.

Its structure depends on the artifact type.

Examples:

Architecture

Decision

Standard

User Story

Runbook

Data Model

---

# Related Artifacts

Use Obsidian links.

Example:

```markdown
## Related Artifacts

- [[ARCH-CS-001-engineering-operating-system]]
- [[PR-CS-002-learn-by-building]]
```

Keep relationships meaningful.

Avoid excessive linking.

---

# References

External references.

Examples:

- standards
- books
- articles
- GitHub repositories
- official documentation

---

# Notes

Optional observations that do not naturally fit elsewhere.

---

# Document Philosophy

Metadata answers:

"What is this?"

TL;DR answers:

"Should I read this?"

Markdown answers:

"Teach me."

Links answer:

"Where should I go next?"

---

# Notes

Consistency reduces future decisions.

The document structure should become familiar enough that authors naturally write within it rather than having to decide on a new organization for every artifact.
