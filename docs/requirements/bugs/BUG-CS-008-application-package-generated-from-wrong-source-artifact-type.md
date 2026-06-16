---
id: BUG-CS-008
type: bug-story
project: career-system
epic: EPIC-CS-002
status: backlog
priority: high
tags: [requirements, career-system, bug]
created: 2026-06-14
updated: 2026-06-14
---

# BUG-CS-008 Application package generated from wrong source artifact type

## Problem

Application package workflow can use the wrong source artifact type.

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
grep -R "BUG-CS-008" docs/requirements || true
```

Add defect-specific grep, diff, or script validation during implementation.

## Regression Validation Steps

1. Regenerate ICE, QODE, and LSEG packages where applicable.
2. Confirm defect does not reappear.
3. Confirm unrelated approved content is not changed incorrectly.

## Related Artifacts

- [[EPIC-CS-002 Application Tracking and Continuous Improvement]]
