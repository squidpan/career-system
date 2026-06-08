# Career System v0.5.1.2 Candidate Matching Functional Fix

## Purpose

Fix the v0.5.1/v0.5.1.1 candidate matching behavior so the engine becomes a useful prioritization tool rather than only a file generator.

## Fixes

- Skips `jd-intelligence-report-*.json` files.
- Candidate count should match actual JD count.
- Prevents generated `candidate-match-report-run-*` fake candidates.
- Adds more realistic scoring spread.
- Uses JD intelligence metadata for company/title/role identity.
- Keeps output deterministic and reviewable.

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v0512-candidate-matching-fix
mkdir -p /tmp/career-system-v0512-candidate-matching-fix

unzip ~/Downloads/career-system-v0.5.1.2-candidate-matching-functional-fix-overlay.zip \
  -d /tmp/career-system-v0512-candidate-matching-fix

cp -R /tmp/career-system-v0512-candidate-matching-fix/* .

chmod +x bin/run-candidate-matching.sh
chmod +x scripts/generate_candidate_matching.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-08-candidate-matching-v3
rm -rf data/candidate-matching

./bin/run-candidate-matching.sh \
  run-2026-06-08-candidate-matching-v3 \
  data/jd-intelligence
```

## Validate

```bash
find data/candidate-matching -name 'candidate-match-*.md' | wc -l

sed -n '1,260p' \
  data/candidate-matching/candidate-matching-report-run-2026-06-08-candidate-matching-v3.md

ls -1 data/candidate-matching | sort | grep 'candidate-match-report-run' || true
```

Expected:

```text
27
```

and no `candidate-match-report-run-*` output.

## Commit

```bash
git add README_CANDIDATE_MATCHING_FUNCTIONAL_FIX.md
git add bin/run-candidate-matching.sh
git add scripts/generate_candidate_matching.py
git add docs/standards/candidate-matching-standard.md
git add templates/candidate-matching-template.md
git add data/candidate-matching

git commit -m "Fix candidate matching engine v0.5.1.2"

git push

git tag -a v0.5.1.2-candidate-matching-functional-fix \
  -m "Candidate matching functional fix complete"

git push origin v0.5.1.2-candidate-matching-functional-fix
```
