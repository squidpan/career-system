# Career System Application Package Generator v0.3.8

Generates one package folder per role, containing the normalized JD, generated role, generated resume version, starter cover letter draft, and manifest.

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-application-package-generator
mkdir -p /tmp/career-system-application-package-generator

unzip ~/Downloads/career-system-v0.3.8-application-package-generator-overlay.zip \
  -d /tmp/career-system-application-package-generator

cp -R /tmp/career-system-application-package-generator/* .

chmod +x bin/run-application-package-generation.sh
chmod +x scripts/generate_application_packages.py
```

## Run

```bash
./bin/run-application-package-generation.sh \
  run-2026-06-01-application-package-v1 \
  data/roles
```

## Review

```bash
tree data/application-packages -L 3
cat data/application-packages/*/application-manifest.json
head -80 data/application-packages/*/cover-letter.md
```

## Commit

```bash
git add README_APPLICATION_PACKAGE_GENERATOR.md
git add bin/run-application-package-generation.sh
git add scripts/generate_application_packages.py
git add docs/standards/application-package-workflow.md
git add templates/application-package-cover-letter-template.md
git add templates/application-manifest-template.json
git add data/application-packages

git commit -m "Add application package generation v0.3.8"
git push
```
