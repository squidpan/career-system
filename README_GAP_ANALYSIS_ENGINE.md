# Career System v0.4.2 Gap Analysis Engine

## Purpose

Generate deterministic gap analysis reports from normalized JDs, role files, and resume masters.

This release helps answer:

```text
Should I apply?
How close am I?
What is missing?
How hard is the gap to close?
What should the resume emphasize?
```

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v042-gap-analysis
mkdir -p /tmp/career-system-v042-gap-analysis

unzip ~/Downloads/career-system-v0.4.2-gap-analysis-engine-overlay.zip \
  -d /tmp/career-system-v042-gap-analysis

cp -R /tmp/career-system-v042-gap-analysis/* .

chmod +x bin/run-gap-analysis.sh
chmod +x scripts/generate_gap_analysis.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-03-gap-analysis-v1
rm -rf data/gap-analysis

./bin/run-gap-analysis.sh \
  run-2026-06-03-gap-analysis-v1 \
  data/jds/normalized
```

## Review Counts

```bash
find data/gap-analysis -name 'gap-*.md' | wc -l
find data/gap-analysis -name 'gap-*.json' | wc -l
```

## Review Key Roles

```bash
ls -1 data/gap-analysis | sort

sed -n '1,220p' data/gap-analysis/gap-vns-health-support-workday-2026.md
sed -n '1,220p' data/gap-analysis/gap-icf-ba-it-2026.md
sed -n '1,220p' data/gap-analysis/gap-michael-baker-international-ba-requirements-2026.md
sed -n '1,220p' data/gap-analysis/gap-citi-support-appsupport-2026.md
```

## Git Add

```bash
git add README_GAP_ANALYSIS_ENGINE.md
git add docs/standards/gap-analysis-standard.md
git add templates/gap-analysis-template.md
git add bin/run-gap-analysis.sh
git add scripts/generate_gap_analysis.py
git add data/gap-analysis
```

## Commit

```bash
git commit -m "Add gap analysis engine v0.4.2"
git push
```

## Tag

```bash
git tag -a v0.4.2-gap-analysis \
  -m "Gap analysis engine complete"

git push origin v0.4.2-gap-analysis
```
