# Career System v0.4.6.1 Resume Bullet Ranking

## Purpose

Rank existing resume bullets using Resume Tailoring Intelligence.

This release helps answer:

```text
Which bullets should move up?
Which bullets should move down?
Which bullets should be compressed or removed?
```

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v0461-bullet-ranking
mkdir -p /tmp/career-system-v0461-bullet-ranking

unzip ~/Downloads/career-system-v0.4.6.1-resume-bullet-ranking-overlay.zip \
  -d /tmp/career-system-v0461-bullet-ranking

cp -R /tmp/career-system-v0461-bullet-ranking/* .

chmod +x bin/run-resume-bullet-ranking.sh
chmod +x scripts/generate_resume_bullet_ranking.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-04-resume-bullet-ranking-v1
rm -rf data/resume-bullet-ranking

./bin/run-resume-bullet-ranking.sh \
  run-2026-06-04-resume-bullet-ranking-v1 \
  data/resume-tailoring
```

## Review

```bash
find data/resume-bullet-ranking -name 'bullet-ranking-*.md' | wc -l

sed -n '1,260p' data/resume-bullet-ranking/bullet-ranking-pico-sre-2026.md
sed -n '1,260p' data/resume-bullet-ranking/bullet-ranking-citi-support-appsupport-2026.md
sed -n '1,260p' data/resume-bullet-ranking/bullet-ranking-vns-health-support-workday-2026.md
sed -n '1,260p' data/resume-bullet-ranking/bullet-ranking-michael-baker-international-ba-requirements-2026.md
```

## Commit

```bash
git add README_RESUME_BULLET_RANKING.md
git add bin/run-resume-bullet-ranking.sh
git add scripts/generate_resume_bullet_ranking.py
git add docs/standards/resume-bullet-ranking-standard.md
git add templates/resume-bullet-ranking-template.md
git add data/resume-bullet-ranking

git commit -m "Add resume bullet ranking v0.4.6.1"
git push

git tag -a v0.4.6.1-resume-bullet-ranking \
  -m "Resume bullet ranking complete"

git push origin v0.4.6.1-resume-bullet-ranking
```
