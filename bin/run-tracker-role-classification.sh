#!/usr/bin/env bash
set -euo pipefail

RUN_ID="${1:-}"
TRACKER_ROLE_DIR="${2:-data/tracker/normalized}"

if [[ -z "$RUN_ID" ]]; then
  echo "Usage: $0 <run_id> [tracker_role_dir]"
  exit 1
fi

if [[ ! -d "$TRACKER_ROLE_DIR" ]]; then
  echo "ERROR: Tracker role directory does not exist: $TRACKER_ROLE_DIR"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_DIR="$ROOT_DIR/ops/runs/$RUN_ID"
INPUT_DIR="$RUN_DIR/input"
OUTPUT_DIR="$RUN_DIR/output"
LOG_DIR="$RUN_DIR/logs"
REPORT_DIR="$ROOT_DIR/data/tracker/reports"

mkdir -p "$INPUT_DIR" "$OUTPUT_DIR" "$LOG_DIR" "$REPORT_DIR"

cp "$TRACKER_ROLE_DIR"/*.md "$INPUT_DIR"/ 2>/dev/null || {
  echo "ERROR: No .md files found in $TRACKER_ROLE_DIR"
  exit 1
}

cat > "$RUN_DIR/run-manifest.md" <<EOF
---
id: $RUN_ID
type: tracker_role_classification_run
title: Tracker Role Classification Run $RUN_ID
categories:
  - "[[Careers]]"
  - "[[Runs]]"
tags:
  - career
  - tracker
  - classification
status: running
created: $(date +%F)
last: $(date +%F)
---

# Tracker Role Classification Run

- Run ID: $RUN_ID
- Tracker role directory: $TRACKER_ROLE_DIR
- Started: $(date -Is)
EOF

python3 "$ROOT_DIR/scripts/classify_tracker_roles.py" \
  --input-dir "$INPUT_DIR" \
  --output-dir "$OUTPUT_DIR" \
  --report-dir "$REPORT_DIR" \
  --run-id "$RUN_ID" \
  | tee "$LOG_DIR/classify-tracker-roles.log"

cp "$OUTPUT_DIR"/*.md "$TRACKER_ROLE_DIR"/

cat >> "$RUN_DIR/run-manifest.md" <<EOF

## Completed

- Completed: $(date -Is)
- Status: complete
EOF

echo "Done."
echo "Run output: $OUTPUT_DIR"
echo "Tracker roles updated in: $TRACKER_ROLE_DIR"
echo "Reports written to: $REPORT_DIR"
