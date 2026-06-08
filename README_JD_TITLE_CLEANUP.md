# Career System v0.5.1.3 — JD Title Cleanup

## Purpose

Fix JD Intelligence title selection so generated intelligence and candidate matching reports use clean job titles.

Problem examples before this patch:

```text
Amtrak -> **Your success is a train ride away!
Dow Jones -> **About The Team
New York Life -> **Location Designation:** Hybrid - 3 days per week
Premera Blue Cross -> Workforce Classification: Telecommuter
```

## Design

Use this title precedence in `scripts/generate_jd_intelligence.py`:

```text
source_title
  >
normalized_title
  >
title
  >
filename fallback
```

This is intentionally conservative because `source_title` is currently cleaner in the normalized JD frontmatter than some `normalized_title` values.

## Install Overlay

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v0513-jd-title-cleanup
mkdir -p /tmp/career-system-v0513-jd-title-cleanup

unzip ~/Downloads/career-system-v0.5.1.3-jd-title-cleanup-functional-overlay.zip \
  -d /tmp/career-system-v0513-jd-title-cleanup

cp -R /tmp/career-system-v0513-jd-title-cleanup/* .

chmod +x bin/run-jd-title-cleanup-patch.sh
chmod +x scripts/patch_jd_title_cleanup.py
```

## Apply Patch

```bash
./bin/run-jd-title-cleanup-patch.sh

python3 -m py_compile scripts/generate_jd_intelligence.py
```

## Regenerate JD Intelligence

```bash
rm -rf data/jd-intelligence

./bin/run-jd-intelligence.sh \
  run-2026-06-08-jd-intelligence-v6 \
  data/jds/normalized
```

## Rebuild Candidate Matching

```bash
rm -rf data/candidate-matching

./bin/run-candidate-matching.sh \
  run-2026-06-08-candidate-matching-v4 \
  data/jd-intelligence
```

## Validate

```bash
find data/jd-intelligence -name 'jd-intelligence-*.md' | wc -l
find data/candidate-matching -name 'candidate-match-*.md' | wc -l

sed -n '1,240p' \
  data/candidate-matching/candidate-matching-report-run-2026-06-08-candidate-matching-v4.md

grep -nE "Amtrak|Dow Jones|New York Life|Premera" \
  data/candidate-matching/candidate-matching-report-run-2026-06-08-candidate-matching-v4.md
```

Expected candidate count:

```text
27
```

Expected title improvements:

```text
Amtrak -> Lead Business Systems Analyst...
Dow Jones -> AI Enablement Business Analyst...
New York Life -> Senior Associate Technical Business Analyst
Premera Blue Cross -> Business Analyst III
```

## Git Commit

After reviewing output:

```bash
git add README_JD_TITLE_CLEANUP.md
git add bin/run-jd-title-cleanup-patch.sh
git add scripts/patch_jd_title_cleanup.py
git add scripts/generate_jd_intelligence.py
git add docs/standards/jd-title-standard.md
git add data/jd-intelligence
git add data/candidate-matching

git commit -m "Fix JD intelligence title selection v0.5.1.3"

git push

git tag -a v0.5.1.3-jd-title-cleanup \
  -m "JD title cleanup complete"

git push origin v0.5.1.3-jd-title-cleanup
```

## Notes

This release patches the existing script in place rather than replacing the full file. That avoids losing existing JD intelligence logic.
