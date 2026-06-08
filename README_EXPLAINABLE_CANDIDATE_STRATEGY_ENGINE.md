# Career System v0.7.0 — Explainable Candidate Strategy Engine

## Purpose

Add an explainability layer on top of v0.6.0 Personalized Candidate Strategy.

v0.6.0 answers: which jobs should Paul pursue first?
v0.7.0 answers: why, what resume story to use, what risks to watch, and what to do next.

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v070-candidate-explainability
mkdir -p /tmp/career-system-v070-candidate-explainability

unzip ~/Downloads/career-system-v0.7.0-explainable-candidate-strategy-engine-overlay.zip \
  -d /tmp/career-system-v070-candidate-explainability

cp -R /tmp/career-system-v070-candidate-explainability/* .

chmod +x bin/run-candidate-explainability.sh
chmod +x scripts/generate_candidate_explainability.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-08-candidate-explainability-v1
rm -rf data/candidate-explainability

./bin/run-candidate-explainability.sh \
  run-2026-06-08-candidate-explainability-v1 \
  data/candidate-strategy
```

## Validate

```bash
find data/candidate-explainability -name 'candidate-explainability-*.md' | wc -l

sed -n '1,260p' \
  data/candidate-explainability/candidate-explainability-report-run-2026-06-08-candidate-explainability-v1.md

sed -n '1,240p' \
  data/candidate-explainability/candidate-explainability-dow-jones-ba-ai-2026.md

sed -n '1,240p' \
  data/candidate-explainability/candidate-explainability-citi-support-appsupport-2026.md
```

Expected: 27 explainability files plus one report.

## Commit

```bash
git add README_EXPLAINABLE_CANDIDATE_STRATEGY_ENGINE.md
git add bin/run-candidate-explainability.sh
git add scripts/generate_candidate_explainability.py
git add docs/standards/candidate-explainability-standard.md
git add templates/candidate-explainability-template.md
git add data/candidate-explainability

git commit -m "Add explainable candidate strategy engine v0.7.0"

git push

git tag -a v0.7.0-explainable-candidate-strategy-engine \
  -m "Explainable candidate strategy engine complete"

git push origin v0.7.0-explainable-candidate-strategy-engine
```
