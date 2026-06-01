#!/usr/bin/env bash
set -euo pipefail

RUN_ID="${1:-}"
ROLE_DIR="${2:-data/roles}"

if [[ -z "$RUN_ID" ]]; then
  echo "Usage: $0 <run_id> [role_dir]"
  exit 1
fi

if [[ ! -d "$ROLE_DIR" ]]; then
  echo "ERROR: Role directory does not exist: $ROLE_DIR"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_DIR="$ROOT_DIR/ops/runs/$RUN_ID"
INPUT_DIR="$RUN_DIR/input"
OUTPUT_DIR="$RUN_DIR/output"
LOG_DIR="$RUN_DIR/logs"
RESUME_VERSION_DIR="$ROOT_DIR/data/resume-versions/generated"

mkdir -p "$INPUT_DIR" "$OUTPUT_DIR" "$LOG_DIR" "$RESUME_VERSION_DIR"

cp "$ROLE_DIR"/*.md "$INPUT_DIR"/ 2>/dev/null || {
  echo "ERROR: No .md files found in $ROLE_DIR"
  exit 1
}

cat > "$RUN_DIR/run-manifest.md" <<EOF
---
id: $RUN_ID
type: resume_version_generation_run
title: Resume Version Generation Run $RUN_ID
categories:
  - "[[Careers]]"
  - "[[Runs]]"
tags:
  - career
  - resume
  - generation
status: running
created: $(date +%F)
last: $(date +%F)
---

# Resume Version Generation Run

- Run ID: $RUN_ID
- Role directory: $ROLE_DIR
- Started: $(date -Is)

## Input Files

$(find "$INPUT_DIR" -maxdepth 1 -type f -name "*.md" -printf "- %f\n" | sort)
EOF

python3 "$ROOT_DIR/scripts/generate_resume_versions_from_roles.py" \
  --input-dir "$INPUT_DIR" \
  --output-dir "$OUTPUT_DIR" \
  --run-id "$RUN_ID" \
  | tee "$LOG_DIR/generate-resume-versions.log"

cp "$OUTPUT_DIR"/*.md "$RESUME_VERSION_DIR"/

cat >> "$RUN_DIR/run-manifest.md" <<EOF

## Output Files

$(find "$OUTPUT_DIR" -maxdepth 1 -type f -name "*.md" -printf "- %f\n" | sort)

## Completed

- Completed: $(date -Is)
- Status: complete
EOF

echo "Done."
echo "Run output: $OUTPUT_DIR"
echo "Resume versions copied to: $RESUME_VERSION_DIR"
