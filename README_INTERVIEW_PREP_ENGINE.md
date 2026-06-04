# Career System v0.4.3 Interview Prep Engine

## Purpose

Generate interview preparation notes from gap-analysis outputs, normalized JDs, roles, and Teal-ready resumes.

This release helps answer:

```text
What questions should I expect?
How should I talk about my strongest experience?
How do I answer questions about gaps?
What should I study before the interview?
```

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v043-interview-prep
mkdir -p /tmp/career-system-v043-interview-prep

unzip ~/Downloads/career-system-v0.4.3-interview-prep-engine-overlay.zip \
  -d /tmp/career-system-v043-interview-prep

cp -R /tmp/career-system-v043-interview-prep/* .

chmod +x bin/run-interview-prep.sh
chmod +x scripts/generate_interview_prep.py
```

## Run

Make sure gap analysis already exists:

```bash
ls data/gap-analysis
```

Generate interview prep:

```bash
rm -rf ops/runs/run-2026-06-03-interview-prep-v1
rm -rf data/interview-prep

./bin/run-interview-prep.sh \
  run-2026-06-03-interview-prep-v1 \
  data/gap-analysis
```

## Review Counts

```bash
find data/interview-prep -name 'interview-prep-*.md' | wc -l
ls -1 data/interview-prep | sort
```

## Review Key Prep Files

```bash
sed -n '1,260p' data/interview-prep/interview-prep-citi-support-appsupport-2026.md
sed -n '1,260p' data/interview-prep/interview-prep-vns-health-support-workday-2026.md
sed -n '1,260p' data/interview-prep/interview-prep-michael-baker-international-ba-requirements-2026.md
sed -n '1,260p' data/interview-prep/interview-prep-pico-sre-2026.md
```

## Git Add

```bash
git add README_INTERVIEW_PREP_ENGINE.md
git add docs/standards/interview-prep-standard.md
git add templates/interview-prep-template.md
git add bin/run-interview-prep.sh
git add scripts/generate_interview_prep.py
git add data/interview-prep
```

## Commit

```bash
git commit -m "Add interview prep engine v0.4.3"
git push
```

## Tag

```bash
git tag -a v0.4.3-interview-prep \
  -m "Interview prep engine complete"

git push origin v0.4.3-interview-prep
```
