# Career System Reference Registries v0.3.3

This overlay adds controlled reference registries for:

- Companies
- Role codes
- Resume families

## Why this exists

The normalizer can identify metadata from JDs, but Career System needs stable vocabulary files so generated IDs, role codes, resume recommendations, and future database/API fields stay consistent.

## Files

```text
data/reference/
├── company-registry.json
├── role-code-registry.json
├── resume-family-registry.json
├── role-families.json
├── role-levels.json
└── role-qualifiers.json
```

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-reference-registries
mkdir -p /tmp/career-system-reference-registries

unzip ~/Downloads/career-system-v0.3.3-reference-registries-overlay.zip \
  -d /tmp/career-system-reference-registries

cp -R /tmp/career-system-reference-registries/* .

chmod +x bin/list-reference-registries.sh
chmod +x scripts/list_reference_registries.py
```

## Review

```bash
./bin/list-reference-registries.sh
```

## Commit

```bash
git add README_REFERENCE_REGISTRIES.md
git add data/reference/company-registry.json
git add data/reference/role-code-registry.json
git add data/reference/resume-family-registry.json
git add docs/standards/company-registry-standard.md
git add docs/standards/role-code-registry-standard.md
git add docs/standards/resume-family-registry-standard.md
git add bin/list-reference-registries.sh
git add scripts/list_reference_registries.py

git commit -m "Add reference registries v0.3.3"
git push
```
