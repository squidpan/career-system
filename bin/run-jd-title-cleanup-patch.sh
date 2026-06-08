#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

python3 scripts/patch_jd_title_cleanup.py
python3 -m py_compile scripts/generate_jd_intelligence.py

echo "JD title cleanup patch applied."
