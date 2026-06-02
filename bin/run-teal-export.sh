#!/usr/bin/env bash
set -euo pipefail

RUN_ID="${1:-}"
ASSEMBLED_DIR="${2:-data/resume-versions/assembled}"

if [[ -z "$RUN_ID" ]]; then
  echo "Usage: $0 <run_id> [assembled_resume_dir]"
  exit 1
fi

if [[ ! -d "$ASSEMBLED_DIR" ]]; then
  echo "ERROR: Assembled resume directory does not exist: $ASSEMBLED_DIR"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_DIR="$ROOT_DIR/ops/runs/$RUN_ID"
INPUT_DIR="$RUN_DIR/input"
OUTPUT_DIR="$RUN_DIR/output"
LOG_DIR="$RUN_DIR/logs"
TEAL_DIR="$ROOT_DIR/data/resume-versions/teal-export"

mkdir -p "$INPUT_DIR" "$OUTPUT_DIR" "$LOG_DIR" "$TEAL_DIR"

cp "$ASSEMBLED_DIR"/*.md "$INPUT_DIR"/ 2>/dev/null || {
  echo "ERROR: No .md files found in $ASSEMBLED_DIR"
  exit 1
}

cat > "$RUN_DIR/run-manifest.md" <<EOF
---
id: $RUN_ID
type: teal_export_run
title: Teal Export Run $RUN_ID
categories:
  - "[[Careers]]"
  - "[[Runs]]"
tags:
  - career
  - resume
  - teal
  - export
status: running
created: $(date +%F)
last: $(date +%F)
---

# Teal Export Run

- Run ID: $RUN_ID
- Assembled resume directory: $ASSEMBLED_DIR
- Started: $(date -Is)
EOF

python3 "$ROOT_DIR/scripts/generate_teal_export_resumes.py" \
  --input-dir "$INPUT_DIR" \
  --output-dir "$OUTPUT_DIR" \
  --run-id "$RUN_ID" \
  | tee "$LOG_DIR/generate-teal-export.log"

cp "$OUTPUT_DIR"/*.md "$TEAL_DIR"/

cat >> "$RUN_DIR/run-manifest.md" <<EOF

## Completed

- Completed: $(date -Is)
- Status: complete
EOF

echo "Done."
echo "Run output: $OUTPUT_DIR"
echo "Teal export resumes copied to: $TEAL_DIR"
