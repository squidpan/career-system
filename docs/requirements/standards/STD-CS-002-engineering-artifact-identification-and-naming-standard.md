# STD-CS-002 Engineering Artifact Identification and Naming Standard

Status: Draft

## TL;DR

- Every Engineering Knowledge Framework (EKF) artifact has a globally unique identifier.
- Artifact identifiers never change once published.
- Sequential numbering is used for every artifact type.
- Markdown files are the authoritative source.
- Git repositories are the source of truth.
- Obsidian is the preferred engineering knowledge environment.
- File names, note titles, and identifiers follow a consistent convention.
- The standard is designed to support future automation.

---

# Purpose

Define a consistent identification and naming convention for all Engineering Knowledge Framework (EKF) artifacts.

This standard provides stable identities that support:

- Git repositories
- Obsidian
- Bases
- Canvas
- PlantUML
- Publishing
- Future automation
- Cross-repository traceability

---

# Design Principles

The identification system should be:

- Human readable
- Stable
- Predictable
- Sequential
- Automation friendly
- Git friendly
- Obsidian native
- Easy to teach
- Easy to remember

---

# Artifact Identifier

Every artifact receives a unique identifier.

Format:

```text
<PREFIX>-<DOMAIN>-<NUMBER>
```

Examples:

```text
PR-CS-001
CTX-CS-003
EPIC-CS-007
US-MW-024
ARCH-CS-001
ADR-CS-002
STD-CS-002
DM-MW-004
```

---

# Sequential Numbering

EKF adopts sequential numbering.

Example:

```text
ARCH-CS-001
ARCH-CS-002
ARCH-CS-003
```

Reserved number ranges are intentionally not used.

Sequential numbering minimizes future maintenance and supports simple automation.

---

# Artifact Prefixes

| Prefix | Artifact |
|---------|----------|
| PR | Principle |
| CTX | Context |
| EPIC | Epic |
| US | User Story |
| AC | Acceptance Criteria |
| ARCH | Architecture |
| ADR | Architecture Decision Record |
| STD | Standard |
| DM | Data Model |
| API | API Contract |
| RB | Runbook |
| BUG | Bug |
| SPR | Sprint |
| REL | Release |
| SPK | Spike |
| TERM | Glossary |

---

# Domain Codes

| Code | Meaning |
|------|---------|
| CS | Career System |
| MW | Motorweb |
| LNX | Linux Dev Environment |
| OBS | Obsidian |
| EKF | Engineering Knowledge Framework |

Additional domain codes may be introduced as new repositories adopt EKF.

---

# File Naming Convention

Markdown files use:

```text
<PREFIX>-<DOMAIN>-<NUMBER>-short-description.md
```

Example:

```text
ARCH-CS-001-engineering-operating-system.md
```

File names should be:

- descriptive
- lowercase
- hyphen separated
- stable

---

# Markdown Title Convention

The first heading is the canonical title.

Example:

```text
# ARCH-CS-001 Engineering Operating System
```

The H1 heading is considered authoritative.

The document title should not be duplicated in YAML metadata.

---

# YAML Metadata

Every major EKF artifact should include a minimal YAML header.

Example:

```yaml
---
id: ARCH-CS-001
type: Architecture
status: Draft

categories:
  - "[[Architectures]]"
  - "[[Frameworks]]"

tags:
  - ekf
  - architecture

summary: Engineering Operating System architecture.

created:
updated:
---
```

Metadata should remain intentionally small.

Document content belongs in Markdown rather than YAML.

---

# Categories

Categories provide primary organization.

Categories should:

- use plural names
- be internal links
- remain reusable across repositories

Example:

```yaml
categories:
  - "[[Architectures]]"
  - "[[Frameworks]]"
```

---

# Tags

Tags provide descriptive context.

Tags answer:

"What topics are discussed?"

Categories answer:

"What kind of artifact is this?"

---

# Related Artifacts

Relationships should be expressed using Obsidian links.

Example:

```markdown
## Related Artifacts

- [[PR-CS-001-small-incremental-changes]]
- [[ADR-CS-001-career-system-reference-implementation]]
```

Avoid manually repeating identifiers when links provide the same information.

---

# Identifier Stability

Artifact identifiers never change after publication.

If an artifact is replaced:

- retain the identifier
- change Status to Superseded
- reference the replacement artifact

Historical references should remain valid indefinitely.

---

# Future Automation

Future EKF tooling may automatically:

- assign identifiers
- validate uniqueness
- rename files
- update links
- generate indexes
- generate Bases
- generate Canvas
- generate publishing artifacts

The simplicity of this standard intentionally supports automation.

---

# Notes

This standard applies to every repository adopting the Engineering Knowledge Framework.

Career System is the initial reference implementation.

Future repositories should adopt this standard rather than creating repository-specific naming conventions.
