# EFK / EOS Current Conventions

## Confirmed

Correct Obsidian YAML categories:

```yaml
categories:
  - [[Epics]]
  - [[Requirements]]
```

Incorrect:

```yaml
categories:
  - "[[Epics]]"
  - "[[Requirements]]"
```

Commit `2f357a7` corrected quoted examples in `STD-CS-002`, `STD-CS-003`, `DM-CS-004`, and templates `TMP-CS-001` through `TMP-CS-010`.

## Requested Front Matter Direction

For new Career System artifacts, the user requested:

```yaml
project: career-system
type: epic
status: draft
description:
```

The EFK chat should determine mandatory versus optional properties by examining standards, templates, context, architecture, data models, and current artifacts.

## Known Conditions

- Multiple generations of metadata exist.
- Multiple files use `EPIC-CS-002`.
- Some notes may be obsolete without being marked.
- Do not mass-rename or normalize without backlink and dependency analysis.
