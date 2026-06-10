#!/usr/bin/env bash
set -euo pipefail

JD_FILE="${1:?Usage: run-jd-match.sh <jd-file> [output-json]}"

OUTPUT_FILE="${2:-data/experience-matches/jd-experience-match.json}"

python3 scripts/match_jd.py \
  "$JD_FILE" \
  data/experience-matching/mrprice-keyword-map.json \
  "$OUTPUT_FILE"
