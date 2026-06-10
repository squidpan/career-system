#!/usr/bin/env bash
set -euo pipefail

SCORED_MATCH="${1:?Usage: run-resume-recommendation.sh <scored-match-json> [output-json]}"

OUTPUT="${2:-data/experience-matches/resume-recommendation.json}"

python3 scripts/recommend_resume_assets.py \
    "$SCORED_MATCH" \
    "$OUTPUT"
