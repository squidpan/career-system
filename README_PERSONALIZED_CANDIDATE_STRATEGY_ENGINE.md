# Career System v0.6.0 — Personalized Candidate Strategy Engine

## Purpose

Add a personal strategy layer on top of candidate matching.

v0.5.1.x answers: how well does this job match the JD/resume profile?
v0.6.0 answers: which jobs should Paul pursue first, given current priorities?

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v060-candidate-strategy
mkdir -p /tmp/career-system-v060-candidate-strategy

unzip ~/Downloads/career-system-v0.6.0-personalized-candidate-strategy-engine-overlay.zip \
  -d /tmp/career-system-v060-candidate-strategy

cp -R /tmp/career-system-v060-candidate-strategy/* .

chmod +x bin/run-candidate-strategy.sh
chmod +x scripts/generate_candidate_strategy.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-08-candidate-strategy-v1
rm -rf data/candidate-strategy

./bin/run-candidate-strategy.sh \
  run-2026-06-08-candidate-strategy-v1 \
  data/candidate-matching
```

## Validate

```bash
find data/candidate-strategy -name 'candidate-strategy-*.md' | wc -l

sed -n '1,260p' \
  data/candidate-strategy/candidate-strategy-report-run-2026-06-08-candidate-strategy-v1.md
```

Expected: 27 strategy files and one ranked strategy report.

## Commit

```bash
git add README_PERSONALIZED_CANDIDATE_STRATEGY_ENGINE.md
git add bin/run-candidate-strategy.sh
git add scripts/generate_candidate_strategy.py
git add docs/standards/candidate-strategy-standard.md
git add templates/candidate-strategy-template.md
git add data/candidate-strategy

git commit -m "Add personalized candidate strategy engine v0.6.0"

git push

git tag -a v0.6.0-personalized-candidate-strategy-engine \
  -m "Personalized candidate strategy engine complete"

git push origin v0.6.0-personalized-candidate-strategy-engine
```
