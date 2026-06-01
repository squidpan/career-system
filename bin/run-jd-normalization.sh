#!/usr/bin/env bash
set -euo pipefail

RUN_ID="${1:-}"
RAW_DIR="${2:-data/jds/raw}"

if [[ -z "$RUN_ID" ]]; then
  echo "Usage: $0 <run_id> [raw_dir]"
  exit 1
fi

if [[ ! -d "$RAW_DIR" ]]; then
  echo "ERROR: Raw JD directory does not exist: $RAW_DIR"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_DIR="$ROOT_DIR/ops/runs/$RUN_ID"
INPUT_DIR="$RUN_DIR/input"
OUTPUT_DIR="$RUN_DIR/output"
LOG_DIR="$RUN_DIR/logs"
NORMALIZED_DIR="$ROOT_DIR/data/jds/normalized"

mkdir -p "$INPUT_DIR" "$OUTPUT_DIR" "$LOG_DIR" "$NORMALIZED_DIR"

cp "$RAW_DIR"/*.md "$INPUT_DIR"/ 2>/dev/null || {
  echo "ERROR: No .md files found in $RAW_DIR"
  exit 1
}

cat > "$RUN_DIR/run-manifest.md" <<EOF
---
id: $RUN_ID
type: normalization_run
title: JD Normalization Run $RUN_ID
categories:
  - "[[Careers]]"
  - "[[Runs]]"
tags:
  - career
  - jd
  - normalization
status: running
created: $(date +%F)
last: $(date +%F)
---

# JD Normalization Run

- Run ID: $RUN_ID
- Raw directory: $RAW_DIR
- Started: $(date -Is)

## Input Files

$(find "$INPUT_DIR" -maxdepth 1 -type f -name "*.md" -printf "- %f\n" | sort)
EOF

python3 "$ROOT_DIR/scripts/normalize_jd.py" \
  --input-dir "$INPUT_DIR" \
  --output-dir "$OUTPUT_DIR" \
  --run-id "$RUN_ID" \
  | tee "$LOG_DIR/normalize.log"

cp "$OUTPUT_DIR"/*.md "$NORMALIZED_DIR"/

cat >> "$RUN_DIR/run-manifest.md" <<EOF

## Output Files

$(find "$OUTPUT_DIR" -maxdepth 1 -type f -name "*.md" -printf "- %f\n" | sort)

## Completed

- Completed: $(date -Is)
- Status: complete
EOF

echo "Done."
echo "Run output: $OUTPUT_DIR"
echo "Normalized JDs copied to: $NORMALIZED_DIR"
