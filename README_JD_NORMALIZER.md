# Career System JD Normalizer v0.3.0

This overlay adds the first script-based normalization pipeline for raw JD clips.

## Core idea

Web Clipper captures raw JD content. Career System scripts normalize it.

```text
Web Clipper
  -> data/jds/raw/*.md
  -> bin/run-jd-normalization.sh
  -> scripts/normalize_jd.py
  -> ops/runs/<run_id>/
  -> data/jds/normalized/*.md
```

## Install overlay

From repo root:

```bash
cd ~/pjs/repos/career-system

rm -rf /tmp/career-system-jd-normalizer
mkdir -p /tmp/career-system-jd-normalizer

unzip ~/Downloads/career-system-v0.3.0-jd-normalizer-overlay.zip \
  -d /tmp/career-system-jd-normalizer

cp -R /tmp/career-system-jd-normalizer/* .

chmod +x bin/run-jd-normalization.sh
chmod +x scripts/normalize_jd.py
chmod +x scripts/normalize_jd_oo.py
```

## Place raw clips

```bash
mkdir -p data/jds/raw
cp /path/to/jd-raw-makai-ba-ai.md data/jds/raw/
cp /path/to/jd-raw-tata-ba-ai.md data/jds/raw/
```

## Run

```bash
./bin/run-jd-normalization.sh run-2026-06-01-jd-normalize-v1 data/jds/raw
```

## Review

```bash
tree ops/runs/run-2026-06-01-jd-normalize-v1 -L 3
tree data/jds/normalized -L 2
```

## Commit

```bash
git status
git add bin scripts data/reference data/jds docs/standards templates README_JD_NORMALIZER.md ops/runs
git commit -m "Add JD normalization pipeline v0.3.0"
git push
```
