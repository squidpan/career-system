#!/usr/bin/env bash
set -euo pipefail

RUN_ID="${1:-}"
NORMALIZED_JD_DIR="${2:-data/jds/normalized}"

if [[ -z "$RUN_ID" ]]; then
  echo "Usage: $0 <run_id> [normalized_jd_dir]"
  exit 1
fi

if [[ ! -d "$NORMALIZED_JD_DIR" ]]; then
  echo "ERROR: Normalized JD directory does not exist: $NORMALIZED_JD_DIR"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_DIR="$ROOT_DIR/ops/runs/$RUN_ID"
INPUT_DIR="$RUN_DIR/input"
OUTPUT_DIR="$RUN_DIR/output"
LOG_DIR="$RUN_DIR/logs"
ROLE_DIR="$ROOT_DIR/data/roles"

mkdir -p "$INPUT_DIR" "$OUTPUT_DIR" "$LOG_DIR" "$ROLE_DIR"

cp "$NORMALIZED_JD_DIR"/*.md "$INPUT_DIR"/ 2>/dev/null || {
  echo "ERROR: No .md files found in $NORMALIZED_JD_DIR"
  exit 1
}

cat > "$RUN_DIR/run-manifest.md" <<EOF
---
id: $RUN_ID
type: role_generation_run
title: Role Generation Run $RUN_ID
categories:
  - "[[Careers]]"
  - "[[Runs]]"
tags:
  - career
  - role
  - generation
status: running
created: $(date +%F)
last: $(date +%F)
---

# Role Generation Run

- Run ID: $RUN_ID
- Normalized JD directory: $NORMALIZED_JD_DIR
- Started: $(date -Is)

## Input Files

$(find "$INPUT_DIR" -maxdepth 1 -type f -name "*.md" -printf "- %f\n" | sort)
EOF

python3 "$ROOT_DIR/scripts/generate_roles_from_jds.py" \
  --input-dir "$INPUT_DIR" \
  --output-dir "$OUTPUT_DIR" \
  --run-id "$RUN_ID" \
  | tee "$LOG_DIR/generate-roles.log"

cp "$OUTPUT_DIR"/*.md "$ROLE_DIR"/

cat >> "$RUN_DIR/run-manifest.md" <<EOF

## Output Files

$(find "$OUTPUT_DIR" -maxdepth 1 -type f -name "*.md" -printf "- %f\n" | sort)

## Completed

- Completed: $(date -Is)
- Status: complete
EOF

echo "Done."
echo "Run output: $OUTPUT_DIR"
echo "Roles copied to: $ROLE_DIR"
