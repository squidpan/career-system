# Career System v0.4.5 Interview Intelligence Integration

## Purpose

Integrate JD-aware intelligence into interview prep.

This release upgrades the v0.4.3 Interview Prep Engine so it consumes `data/jd-intelligence/` from v0.4.4 and injects JD-specific tools, platforms, products, domains, methodologies, JD-aware questions, and story mappings into interview prep outputs.

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v045-interview-intel
mkdir -p /tmp/career-system-v045-interview-intel

unzip ~/Downloads/career-system-v0.4.5-interview-intelligence-integration-overlay.zip \
  -d /tmp/career-system-v045-interview-intel

cp -R /tmp/career-system-v045-interview-intel/* .

chmod +x bin/run-interview-prep.sh
chmod +x scripts/generate_interview_prep.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-03-interview-prep-v2
rm -rf data/interview-prep

./bin/run-interview-prep.sh \
  run-2026-06-03-interview-prep-v2 \
  data/gap-analysis
```

## Review

```bash
find data/interview-prep -name 'interview-prep-*.md' | wc -l

sed -n '1,320p' data/interview-prep/interview-prep-pico-sre-2026.md
sed -n '1,320p' data/interview-prep/interview-prep-vns-health-support-workday-2026.md
sed -n '1,320p' data/interview-prep/interview-prep-michael-baker-international-ba-requirements-2026.md
sed -n '1,320p' data/interview-prep/interview-prep-citi-support-appsupport-2026.md
```

## Commit

```bash
git add README_INTERVIEW_INTELLIGENCE_INTEGRATION.md
git add bin/run-interview-prep.sh
git add scripts/generate_interview_prep.py
git add docs/standards/interview-intelligence-integration-standard.md
git add templates/interview-prep-template.md
git add data/interview-prep

git commit -m "Integrate JD intelligence into interview prep v0.4.5"
git push

git tag -a v0.4.5-interview-intelligence-integration \
  -m "Interview intelligence integration complete"

git push origin v0.4.5-interview-intelligence-integration
```
