#!/usr/bin/env bash
set -euo pipefail

SCORED_MATCH="${1:?Usage: run-interview-recommendation.sh <scored-match-json> [output-json]}"

OUTPUT="${2:-data/experience-matches/interview-recommendation.json}"

python3 scripts/recommend_interview_assets.py \
    "$SCORED_MATCH" \
    "$OUTPUT"
