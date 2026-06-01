#!/usr/bin/env bash
set -euo pipefail

RUN_ID="${1:-}"
ROLES_CSV="${2:-}"

if [[ -z "$RUN_ID" || -z "$ROLES_CSV" ]]; then
  echo "Usage: $0 <run_id> <roles_csv>"
  exit 1
fi

if [[ ! -f "$ROLES_CSV" ]]; then
  echo "ERROR: Roles CSV file does not exist: $ROLES_CSV"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_DIR="$ROOT_DIR/ops/runs/$RUN_ID"
INPUT_DIR="$RUN_DIR/input"
OUTPUT_DIR="$RUN_DIR/output"
LOG_DIR="$RUN_DIR/logs"
NORMALIZED_DIR="$ROOT_DIR/data/tracker/normalized"
REPORT_DIR="$ROOT_DIR/data/tracker/reports"

mkdir -p "$INPUT_DIR" "$OUTPUT_DIR" "$LOG_DIR" "$NORMALIZED_DIR" "$REPORT_DIR"

cp "$ROLES_CSV" "$INPUT_DIR"/

cat > "$RUN_DIR/run-manifest.md" <<EOF
---
id: $RUN_ID
type: tracker_role_import_run
title: Tracker Role Import Run $RUN_ID
categories:
  - "[[Careers]]"
  - "[[Runs]]"
tags:
  - career
  - tracker
  - import
status: running
created: $(date +%F)
last: $(date +%F)
---

# Tracker Role Import Run

- Run ID: $RUN_ID
- Roles CSV: $ROLES_CSV
- Started: $(date -Is)

## Input Files

$(find "$INPUT_DIR" -maxdepth 1 -type f -printf "- %f\n" | sort)
EOF

python3 "$ROOT_DIR/scripts/import_tracker_roles.py" \
  --roles-csv "$ROLES_CSV" \
  --output-dir "$OUTPUT_DIR" \
  --report-dir "$REPORT_DIR" \
  --run-id "$RUN_ID" \
  | tee "$LOG_DIR/import-tracker-roles.log"

cp "$OUTPUT_DIR"/*.md "$NORMALIZED_DIR"/

cat >> "$RUN_DIR/run-manifest.md" <<EOF

## Output Files

$(find "$OUTPUT_DIR" -maxdepth 1 -type f -name "*.md" -printf "- %f\n" | sort)

## Reports

$(find "$REPORT_DIR" -maxdepth 1 -type f -name "*$RUN_ID*" -printf "- %f\n" | sort)

## Completed

- Completed: $(date -Is)
- Status: complete
EOF

echo "Done."
echo "Run output: $OUTPUT_DIR"
echo "Tracker roles copied to: $NORMALIZED_DIR"
echo "Reports written to: $REPORT_DIR"
