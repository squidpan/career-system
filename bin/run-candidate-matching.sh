#!/usr/bin/env bash
set -euo pipefail

RUN_ID="${1:?usage: run-candidate-matching.sh <run-id> <jd-intelligence-dir>}"
JD_INTEL_DIR="${2:?usage: run-candidate-matching.sh <run-id> <jd-intelligence-dir>}"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_DIR="$REPO_ROOT/ops/runs/$RUN_ID"
OUT_DIR="$RUN_DIR/output/candidate-matching"
DATA_OUT="$REPO_ROOT/data/candidate-matching"

mkdir -p "$OUT_DIR"

python3 "$REPO_ROOT/scripts/generate_candidate_matching.py" \
  --run-id "$RUN_ID" \
  --input-dir "$REPO_ROOT/$JD_INTEL_DIR" \
  --output-dir "$OUT_DIR"

rm -rf "$DATA_OUT"
mkdir -p "$(dirname "$DATA_OUT")"
cp -R "$OUT_DIR" "$DATA_OUT"

echo "Done."
echo "Run output: $OUT_DIR"
echo "Candidate matching copied to: $DATA_OUT"
