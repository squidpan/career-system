#!/usr/bin/env bash
set -euo pipefail

INPUT="${1:?Usage: run-ats-text-export.sh <input-md> [output-txt]}"
OUTPUT="${2:-${INPUT%.md}.txt}"

python3.13 scripts/export_ats_text.py "$INPUT" "$OUTPUT"
