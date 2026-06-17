---
id: BUG-CS-004
type: bug-story
project: career-system
epic: EPIC-CS-002
status: completed
completed: 2026-06-16
priority: high
tags: [requirements, career-system, bug]
created: 2026-06-14
updated: 2026-06-14
---

# BUG-CS-004 submission-notes.md template inconsistent across packages

## Problem

Application packages do not use a consistent submission-notes.md structure.

## Business Impact

This defect can reduce application package quality, corrupt resume-ready content, or reduce confidence in Career System outputs.

## Expected Behavior

Career System should produce application artifacts that preserve approved facts, separate analysis from resume content, and avoid silent metadata errors.

## Acceptance Criteria

- Defect can be reproduced or confirmed from existing artifacts.
- Fix prevents the defect in future generated packages.
- Manual validation steps are documented.
- Programmatic validation steps are documented.
- Regression validation steps are documented.

## Manual Validation Steps

1. Open the affected generated artifact.
2. Confirm whether the defect is present.
3. After fix, confirm the corrected behavior appears in regenerated artifacts.

## Programmatic Validation Steps

```bash
grep -R "BUG-CS-004" docs/requirements || true
```

Add defect-specific grep, diff, or script validation during implementation.

## Regression Validation Steps

1. Regenerate ICE, QODE, and LSEG packages where applicable.
2. Confirm defect does not reappear.
3. Confirm unrelated approved content is not changed incorrectly.

## Related Artifacts

- [[EPIC-CS-002 Application Tracking and Continuous Improvement]]

## Implementation Notes

Implemented during Sprint 1.

Results:
- Canonical submission-notes template created.
- Existing application packages standardized.
- Canonical status values normalized.
- Application tracker aligned with submission notes.
