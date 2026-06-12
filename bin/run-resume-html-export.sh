#!/usr/bin/env bash
set -euo pipefail

INPUT="${1:?Usage: run-resume-html-export.sh <input-md> [output-html]}"
OUTPUT="${2:-${INPUT%.md}.html}"

python3.13 scripts/export_resume_html.py "$INPUT" "$OUTPUT"
