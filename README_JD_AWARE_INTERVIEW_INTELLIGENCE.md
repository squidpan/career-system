# Career System v0.4.4 JD-Aware Interview Intelligence

## Purpose

Extract JD-specific intelligence from normalized job descriptions so Career System can move beyond role templates.

This release creates:

```text
data/jd-intelligence/
```

with one Markdown and one JSON file per normalized JD.

## What It Extracts

- Tools
- Platforms
- Products
- Domains
- Methodologies
- JD-aware interview questions
- Resume story mapping

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v044-jd-intelligence
mkdir -p /tmp/career-system-v044-jd-intelligence

unzip ~/Downloads/career-system-v0.4.4-jd-aware-interview-intelligence-overlay.zip \
  -d /tmp/career-system-v044-jd-intelligence

cp -R /tmp/career-system-v044-jd-intelligence/* .

chmod +x bin/run-jd-intelligence.sh
chmod +x scripts/generate_jd_intelligence.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-03-jd-intelligence-v1
rm -rf data/jd-intelligence

./bin/run-jd-intelligence.sh \
  run-2026-06-03-jd-intelligence-v1 \
  data/jds/normalized
```

## Review

```bash
find data/jd-intelligence -name 'jd-intelligence-*.md' | wc -l
find data/jd-intelligence -name 'jd-intelligence-*.json' | wc -l
ls -1 data/jd-intelligence | sort

sed -n '1,220p' data/jd-intelligence/jd-intelligence-pico-sre-2026.md
sed -n '1,220p' data/jd-intelligence/jd-intelligence-vns-health-support-workday-2026.md
sed -n '1,220p' data/jd-intelligence/jd-intelligence-michael-baker-international-ba-requirements-2026.md
sed -n '1,220p' data/jd-intelligence/jd-intelligence-citi-support-appsupport-2026.md
```

## Commit

```bash
git add README_JD_AWARE_INTERVIEW_INTELLIGENCE.md
git add bin/run-jd-intelligence.sh
git add scripts/generate_jd_intelligence.py
git add docs/standards/jd-aware-interview-intelligence-standard.md
git add templates/jd-intelligence-template.md
git add data/jd-intelligence

git commit -m "Add JD-aware interview intelligence v0.4.4"
git push

git tag -a v0.4.4-jd-aware-interview-intelligence \
  -m "JD-aware interview intelligence complete"

git push origin v0.4.4-jd-aware-interview-intelligence
```
