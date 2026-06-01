# Career System Role Registry v0.3.2

Generates role Markdown records from normalized JD files.

## Workflow

```text
Raw JD
  -> Normalized JD
  -> Role Registry
```

## Install

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-role-registry
mkdir -p /tmp/career-system-role-registry

unzip ~/Downloads/career-system-v0.3.2-role-registry-overlay.zip \
  -d /tmp/career-system-role-registry

cp -R /tmp/career-system-role-registry/* .

chmod +x bin/run-role-generation.sh
chmod +x scripts/generate_roles_from_jds.py
```

## Run

```bash
./bin/run-role-generation.sh run-2026-06-01-role-generate-v1 data/jds/normalized
```

## Review

```bash
tree data/roles -L 2
head -80 data/roles/*.md
```

## Commit

```bash
git add README_ROLE_REGISTRY.md bin scripts data/roles docs/standards templates
git commit -m "Add role registry generation v0.3.2"
git push
```
