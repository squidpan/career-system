# Career System v0.4.7 Role-Aware Resume Assembly Engine

## Purpose

Generate assembled v2 resume markdown files using the outputs from:

```text
Resume Tailoring Intelligence
Resume Bullet Ranking
Teal-export resume markdown
```

This is the first Career System release that moves from analysis reports into resume generation.

## Inputs

```text
data/resume-bullet-ranking/
data/resume-tailoring/
data/resume-versions/teal-export/
```

## Output

```text
data/resume-versions/assembled-v2/
```

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-v047-role-aware-assembly
mkdir -p /tmp/career-system-v047-role-aware-assembly

unzip ~/Downloads/career-system-v0.4.7-role-aware-resume-assembly-overlay.zip \
  -d /tmp/career-system-v047-role-aware-assembly

cp -R /tmp/career-system-v047-role-aware-assembly/* .

chmod +x bin/run-role-aware-resume-assembly.sh
chmod +x scripts/assemble_role_aware_resumes.py
```

## Run

```bash
rm -rf ops/runs/run-2026-06-04-role-aware-resume-assembly-v1
rm -rf data/resume-versions/assembled-v2

./bin/run-role-aware-resume-assembly.sh \
  run-2026-06-04-role-aware-resume-assembly-v1 \
  data/resume-bullet-ranking
```

## Review

```bash
find data/resume-versions/assembled-v2 -name 'resume-*-assembled-v2.md' | wc -l

sed -n '1,260p' data/resume-versions/assembled-v2/resume-pico-sre-2026-assembled-v2.md
sed -n '1,260p' data/resume-versions/assembled-v2/resume-citi-support-appsupport-2026-assembled-v2.md
sed -n '1,260p' data/resume-versions/assembled-v2/resume-vns-health-support-workday-2026-assembled-v2.md
sed -n '1,260p' data/resume-versions/assembled-v2/resume-michael-baker-international-ba-requirements-2026-assembled-v2.md
```

## Commit

```bash
git add README_ROLE_AWARE_RESUME_ASSEMBLY.md
git add bin/run-role-aware-resume-assembly.sh
git add scripts/assemble_role_aware_resumes.py
git add docs/standards/role-aware-resume-assembly-standard.md
git add templates/role-aware-assembled-resume-template.md
git add data/resume-versions/assembled-v2

git commit -m "Add role-aware resume assembly engine v0.4.7"
git push

git tag -a v0.4.7-role-aware-resume-assembly \
  -m "Role-aware resume assembly complete"

git push origin v0.4.7-role-aware-resume-assembly
```
