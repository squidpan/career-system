# Career System v0.4.6.2 Bullet Ranking Refinement

## Purpose

Refine Resume Bullet Ranking from simple Top/Bottom ranking into four action categories:

```text
Promote
Keep
Compress
Remove
```

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v0462-bullet-refinement
mkdir -p /tmp/career-system-v0462-bullet-refinement

unzip ~/Downloads/career-system-v0.4.6.2-bullet-ranking-refinement-overlay.zip \
  -d /tmp/career-system-v0462-bullet-refinement

cp -R /tmp/career-system-v0462-bullet-refinement/* .

chmod +x bin/run-resume-bullet-ranking.sh
chmod +x scripts/generate_resume_bullet_ranking.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-04-resume-bullet-ranking-v2
rm -rf data/resume-bullet-ranking

./bin/run-resume-bullet-ranking.sh \
  run-2026-06-04-resume-bullet-ranking-v2 \
  data/resume-tailoring
```

## Review

```bash
find data/resume-bullet-ranking -name 'bullet-ranking-*.md' | wc -l

sed -n '1,320p' data/resume-bullet-ranking/bullet-ranking-pico-sre-2026.md
sed -n '1,320p' data/resume-bullet-ranking/bullet-ranking-citi-support-appsupport-2026.md
sed -n '1,320p' data/resume-bullet-ranking/bullet-ranking-vns-health-support-workday-2026.md
sed -n '1,320p' data/resume-bullet-ranking/bullet-ranking-michael-baker-international-ba-requirements-2026.md
```

## Commit

```bash
git add README_RESUME_BULLET_RANKING_REFINEMENT.md
git add bin/run-resume-bullet-ranking.sh
git add scripts/generate_resume_bullet_ranking.py
git add docs/standards/resume-bullet-ranking-standard.md
git add templates/resume-bullet-ranking-template.md
git add data/resume-bullet-ranking

git commit -m "Refine resume bullet ranking categories v0.4.6.2"
git push

git tag -a v0.4.6.2-bullet-ranking-refinement \
  -m "Resume bullet ranking refinement complete"

git push origin v0.4.6.2-bullet-ranking-refinement
```
