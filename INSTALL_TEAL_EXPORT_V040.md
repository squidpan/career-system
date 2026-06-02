# Install Career System v0.4.0 Teal Export Engine

## A. Install Overlay

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-teal-export
mkdir -p /tmp/career-system-teal-export

unzip ~/Downloads/career-system-v0.4.0-teal-export-engine-overlay.zip \
  -d /tmp/career-system-teal-export

cp -R /tmp/career-system-teal-export/* .

chmod +x bin/run-teal-export.sh
chmod +x scripts/generate_teal_export_resumes.py
```

## B. Run

```bash
./bin/run-teal-export.sh \
  run-2026-06-02-teal-export-v1 \
  data/resume-versions/assembled
```

## C. Review

```bash
ls -1 data/resume-versions/teal-export | sort

grep -R "Assembly Summary" data/resume-versions/teal-export || true
grep -R "Tailoring Checklist" data/resume-versions/teal-export || true
grep -R "JD Keywords" data/resume-versions/teal-export || true
grep -R "run_id" data/resume-versions/teal-export || true

grep -n "^## Professional Summary" data/resume-versions/teal-export/*.md
grep -n "^## Work Experience" data/resume-versions/teal-export/*.md
grep -n "^## Skills" data/resume-versions/teal-export/*.md

sed -n '1,220p' data/resume-versions/teal-export/resume-citi-support-appsupport-2026-teal-v1.md
```

## D. Teal Test

Use Teal:

```text
Import → Merge Content
```

Start with:

```text
data/resume-versions/teal-export/resume-citi-support-appsupport-2026-teal-v1.md
```

## E. Git Commit

```bash
git add README_TEAL_EXPORT_ENGINE.md
git add INSTALL_TEAL_EXPORT_V040.md
git add bin/run-teal-export.sh
git add scripts/generate_teal_export_resumes.py
git add docs/standards/teal-export-workflow.md
git add templates/teal-export-resume-template.md
git add data/resume-versions/teal-export

git status

git commit -m "Add Teal export engine v0.4.0"
git push
```

## F. Tag After Teal Test

```bash
git tag -a v0.4.0-teal-export \
  -m "Teal export engine complete"

git push origin v0.4.0-teal-export
```
