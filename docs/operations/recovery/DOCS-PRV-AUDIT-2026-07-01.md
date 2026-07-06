# Docs PRV Audit — 2026-07-01

## Purpose

Verify that the Obsidian `docs-prv` copy did not contain documentation missing from the Career System repository.

## Initial Concern

A recursive diff between:

- `../../vaults/plvault/References/career-system/docs-prv/`
- `docs/requirements/`

showed many differences.

## Finding

The comparison was misleading because `docs-prv` is a copy of the repository-level `docs/` folder, not only `docs/requirements/`.

A relative-path comparison was performed between:

- repo `docs/`
- vault `docs-prv/`

Result:

- Files only in vault `docs-prv`: none
- Files only in repo `docs/`: current repo has additional newer documentation

## Conclusion

No documentation from `docs-prv` appears to be missing from the repository.

The repository `docs/` folder is the current source of truth.

## Rule Going Forward

When auditing Obsidian copies against the repository, compare matching roots:

- `docs-prv/` ↔ `docs/`
- not `docs-prv/` ↔ `docs/requirements/`

