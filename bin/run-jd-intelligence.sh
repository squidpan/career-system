#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <run_id> <normalized_jds_dir>" >&2
  exit 2
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

RUN_ID="$1"
JDS_DIR="$2"

python3 scripts/generate_jd_intelligence.py "$RUN_ID" "$JDS_DIR"
