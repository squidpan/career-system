#!/usr/bin/env bash
set -euo pipefail

RUN_ID="${1:?run id required}"
INPUT_DIR="${2:?input dir required}"

REPO_ROOT="$(git rev-parse --show-toplevel)"
OUT_DIR="$REPO_ROOT/ops/runs/$RUN_ID/output/candidate-explainability"
DATA_DIR="$REPO_ROOT/data/candidate-explainability"

mkdir -p "$OUT_DIR"

python3 "$REPO_ROOT/scripts/generate_candidate_explainability.py" \
  --run-id "$RUN_ID" \
  --input-dir "$REPO_ROOT/$INPUT_DIR" \
  --output-dir "$OUT_DIR"

rm -rf "$DATA_DIR"
mkdir -p "$DATA_DIR"
cp -R "$OUT_DIR"/* "$DATA_DIR"/

echo "Done."
echo "Run output: $OUT_DIR"
echo "Candidate explainability copied to: $DATA_DIR"
