#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <run_id> <bullet_ranking_dir> [tailoring_dir]" >&2
  exit 2
fi
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
python3 scripts/generate_resume_enhancement.py "$1" "$2" "${3:-data/resume-tailoring}"
