#!/usr/bin/env bash
set -euo pipefail

RUN_ID="${1:-}"
INPUT_DIR="${2:-data/jd-intelligence}"

if [[ -z "$RUN_ID" ]]; then
  echo "Usage: $0 <run-id> [jd-intelligence-dir]" >&2
  exit 1
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="$REPO_ROOT/ops/runs/$RUN_ID/output/candidate-matching"
FINAL_DIR="$REPO_ROOT/data/candidate-matching"

mkdir -p "$OUTPUT_DIR"

python3 "$REPO_ROOT/scripts/generate_candidate_matching.py" \
  --run-id "$RUN_ID" \
  --input-dir "$REPO_ROOT/$INPUT_DIR" \
  --output-dir "$OUTPUT_DIR"

rm -rf "$FINAL_DIR"
mkdir -p "$FINAL_DIR"
cp -R "$OUTPUT_DIR"/* "$FINAL_DIR"/

echo "Done."
echo "Run output: $OUTPUT_DIR"
echo "Candidate matching copied to: $FINAL_DIR"
