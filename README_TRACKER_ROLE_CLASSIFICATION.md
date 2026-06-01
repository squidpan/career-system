# Career System Tracker Role Classification v0.3.7

Classifies normalized tracker role records using tracker title rules and the role-code registry.

## New tracker fields

```yaml
role_family:
role_level:
role_qualifiers:
role_code:
role_code_confidence:
recommended_resume_family:
recommended_resume_master_id:
recommended_resume_file:
classification_status:
classification_source:
```

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-tracker-role-classification
mkdir -p /tmp/career-system-tracker-role-classification

unzip ~/Downloads/career-system-v0.3.7-tracker-role-classification-overlay.zip \
  -d /tmp/career-system-tracker-role-classification

cp -R /tmp/career-system-tracker-role-classification/* .

chmod +x bin/run-tracker-role-classification.sh
chmod +x scripts/classify_tracker_roles.py
```

## Run

```bash
./bin/run-tracker-role-classification.sh \
  run-2026-06-01-tracker-role-classify-v1 \
  data/tracker/normalized
```

## Review

```bash
grep -n "role_code:" data/tracker/normalized/*.md
grep -n "recommended_resume_master_id:" data/tracker/normalized/*.md
cat data/tracker/reports/tracker-role-classification-report-run-2026-06-01-tracker-role-classify-v1.md
```

## Commit

```bash
git add README_TRACKER_ROLE_CLASSIFICATION.md
git add bin/run-tracker-role-classification.sh
git add scripts/classify_tracker_roles.py
git add docs/standards/tracker-role-classification-workflow.md
git add templates/tracker-role-template.md
git add data/tracker/normalized
git add data/tracker/reports

git commit -m "Add tracker role classification v0.3.7"
git push
```
