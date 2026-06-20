# US-MW-008D Smoke Test Suite

Status: Draft

## User Story

As a Career Center operator,
I want a smoke test suite,
so that every deployment can be quickly validated.

## Acceptance Criteria

- Smoke test validates GET /health.
- Smoke test validates GET /applications.
- Smoke test validates GET /applications/{id}.
- Smoke test validates GET /applications/{id}/jd.
- Smoke test validates GET /applications/{id}/artifacts.
- Smoke test exits non-zero on failure.
