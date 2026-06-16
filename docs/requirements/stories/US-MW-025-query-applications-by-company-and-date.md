---
id: US-MW-025
type: user-story
project: motorweb
epic: EPIC-MW-002
status: backlog
priority: high
tags: [requirements, motorweb]
created: 2026-06-14
updated: 2026-06-14
---

# US-MW-025 Query Applications by Company and Date

## User Story

As Paul, I want to query applications by company and date so that I can review application history and recent activity.

## Context

Motorweb Career Center PostgreSQL POC begins with local PostgreSQL and SQL only.

## Scope

- Define required behavior.
- Maintain traceability to source artifacts.
- Include validation as part of the story, not as an afterthought.

## Out of Scope

- REST API unless explicitly stated.
- React UI unless explicitly stated.
- Trello/Jira automation.

## Acceptance Criteria

- Requirement has a clear source artifact.
- Output or behavior is repeatable.
- Status, generated content, or SQL result can be manually validated.
- Story includes manual, programmatic, and regression validation steps.

## Manual Validation Steps

1. Open the relevant artifact, tracker file, or database view.
2. Confirm the expected content, status, or behavior is present.
3. Confirm unrelated artifacts are not polluted or overwritten.

## Programmatic Validation Steps

```bash
grep -R "US-MW-025" docs/requirements || true
```

Add story-specific validation command during implementation.

## Regression Validation Steps

1. Re-run the affected workflow.
2. Validate at least three recent examples where applicable.
3. Confirm prior approved content remains intact.

## Related Artifacts

- [[EPIC-MW-002 Motorweb Career Center PostgreSQL POC]]
