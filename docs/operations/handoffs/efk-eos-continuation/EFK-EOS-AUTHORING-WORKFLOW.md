# EFK / EOS Authoring and Validation Workflow

## Startup

```bash
git branch --show-current
git status --short
git stash list
git fetch --prune
```

## Authoring Sequence

1. Determine artifact type.
2. Confirm identifier uniqueness.
3. Read applicable standards.
4. Read the template.
5. Read related context.
6. Read architecture and ADRs.
7. Read related data models.
8. Read glossary terms.
9. Read parent, child, and sibling artifacts.
10. Read indexes and traceability.
11. Resolve conflicts before writing.
12. Generate one artifact.
13. Validate metadata, structure, links, and diff.
14. Commit one bounded conceptual change.

## Validation

```bash
git status --short
git diff --stat
git diff --check
grep -RIn '"\[\[' docs/requirements || true
git diff --cached --stat
git diff --cached --check
```

## Closeout

```bash
git status --short
git stash list
git log -1 --oneline --decorate
git branch -vv
```
