#!/usr/bin/env bash
set -euo pipefail

KEYWORDS="${1:-production support,oracle,linux,incident management,market data}"

python3 scripts/match_experience_keywords.py \
  data/experience-matching/mrprice-keyword-map.json \
  "$KEYWORDS"
