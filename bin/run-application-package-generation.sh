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
PACKAGE_DIR="$ROOT_DIR/data/application-packages"

mkdir -p "$INPUT_DIR" "$OUTPUT_DIR" "$LOG_DIR" "$PACKAGE_DIR"

cp "$ROLE_DIR"/*.md "$INPUT_DIR"/ 2>/dev/null || {
  echo "ERROR: No .md files found in $ROLE_DIR"
  exit 1
}

python3 "$ROOT_DIR/scripts/generate_application_packages.py" \
  --input-dir "$INPUT_DIR" \
  --output-dir "$OUTPUT_DIR" \
  --run-id "$RUN_ID" \
  | tee "$LOG_DIR/generate-application-packages.log"

cp -R "$OUTPUT_DIR"/* "$PACKAGE_DIR"/

echo "Done."
echo "Run output: $OUTPUT_DIR"
echo "Application packages copied to: $PACKAGE_DIR"
