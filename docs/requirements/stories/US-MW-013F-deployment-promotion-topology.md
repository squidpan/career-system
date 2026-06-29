# US-MW-013F Deployment Promotion Topology

Status: Proposed

## User Story

As a platform administrator,

I want a documented deployment promotion model,

so that software moves through development, validation, and production using a repeatable release process.

## Business Context

Career System currently uses feature branches, tagged releases, and manual deployment.

As the platform matures, deployments should follow a consistent promotion model separating development, QA validation, and production execution.

## Promotion Workflow

```text
Developer (pl)
        │
Feature Branch
        │
Merge to Main
        │
Tagged Release
        │
TED Validation
        │
Approved Release
        │
Deployment
        │
/opt/projects
        │
systemd
        │
career-api
```

## Scope

Define standards for:

- Feature branches
- Merge strategy
- Tagged releases
- QA validation
- Deployment ownership
- Rollback strategy
- Production startup
- Release documentation

## Acceptance Criteria

- Promotion stages are documented.
- Human responsibilities are documented.
- Future service account responsibilities are documented.
- Relationship to tagged releases is documented.
- Deployment workflow is documented.

## Related Stories

- US-LNX-001
- US-MW-013A
- US-MW-013B
- US-MW-013E

## Notes

This story documents the intended operational deployment model without implementing production deployment.
