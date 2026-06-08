# Career System v0.5.1 Candidate Matching Engine

## Purpose

Rank normalized JD intelligence files by practical fit for Paul Lyu's current job search.

This release turns Career System from a document-generation pipeline into a decision-support tool:

- Which jobs should be prioritized?
- Which jobs are strong fits?
- Which jobs have manageable gaps?
- Which resume family should be used?
- What should be emphasized when tailoring?

## Inputs

```text
data/jd-intelligence/
```

The engine reads `jd-intelligence-*.json` files.

## Outputs

```text
data/candidate-matching/
ops/runs/<run-id>/output/candidate-matching/
```

Generated artifacts include:

- `candidate-match-<slug>.md`
- `candidate-match-<slug>.json`
- `candidate-matching-report-<run-id>.md`
- `candidate-matching-report-<run-id>.json`

## Scoring Model

The first version is deterministic and conservative.

### Positive signals

- Business analysis / BSA alignment
- Application support / production support alignment
- Operations support alignment
- Financial services / insurance / healthcare domain fit
- API / data / SQL / Oracle / Linux / runbook / UAT / Jira / release readiness language
- AI mention as strategic interest, not as a separate resume family

### Gap signals

- Heavy hands-on software engineering
- Deep cloud engineering ownership
- Heavy Workday/HRIS specialization
- Pure sales / marketing / content ownership
- Senior leadership or people-management expectations beyond the target profile

## Recommendation Bands

| Score | Recommendation |
|---:|---|
| 85+ | apply_now |
| 70-84 | apply_selectively |
| 55-69 | possible_but_tailor_carefully |
| <55 | deprioritize |

## Install Overlay

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v051-candidate-matching
mkdir -p /tmp/career-system-v051-candidate-matching

unzip ~/Downloads/career-system-v0.5.1-candidate-matching-engine-overlay.zip \
  -d /tmp/career-system-v051-candidate-matching

cp -R /tmp/career-system-v051-candidate-matching/* .

chmod +x bin/run-candidate-matching.sh
chmod +x scripts/generate_candidate_matching.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-08-candidate-matching-v1
rm -rf data/candidate-matching

./bin/run-candidate-matching.sh \
  run-2026-06-08-candidate-matching-v1 \
  data/jd-intelligence
```

## Review

```bash
find data/candidate-matching -name 'candidate-match-*.md' | wc -l

sed -n '1,260p' data/candidate-matching/candidate-matching-report-run-2026-06-08-candidate-matching-v1.md

ls -1 data/candidate-matching | sort | head
```

## Commit

```bash
git add README_CANDIDATE_MATCHING_ENGINE.md
git add bin/run-candidate-matching.sh
git add scripts/generate_candidate_matching.py
git add docs/standards/candidate-matching-standard.md
git add templates/candidate-matching-template.md
git add data/candidate-matching

git commit -m "Add candidate matching engine v0.5.1"

git push

git tag -a v0.5.1-candidate-matching-engine \
  -m "Candidate matching engine complete"

git push origin v0.5.1-candidate-matching-engine
```
