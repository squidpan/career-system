# Gap Analysis Standard v0.4.2

## Purpose

The Gap Analysis Engine helps decide whether a role is worth pursuing and how much tailoring or learning is needed.

## Inputs

- Normalized JD from `data/jds/normalized`
- Role file from `data/roles`
- Resume master from `data/resume-masters`

## Outputs

- Markdown reports in `data/gap-analysis`
- JSON reports in `data/gap-analysis`
- Run outputs in `ops/runs/<run_id>/output`

## Scoring

| Category | Weight |
|---|---:|
| Skills | 40% |
| Tools | 20% |
| Domain | 20% |
| Role Alignment | 20% |

## Recommendation Bands

| Score | Recommendation |
|---:|---|
| 85+ | strong_apply |
| 70-84 | apply |
| 55-69 | stretch_apply |
| below 55 | strategic_only |

## Design Notes

v0.4.2 uses deterministic keyword matching. This makes reports explainable, testable, and easy to improve with registries later.
