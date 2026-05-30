#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${1:-$HOME/pjs/repos/career-system}"
OVERLAY_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$REPO_DIR"
cd "$REPO_DIR"

if [ ! -d .git ]; then
  git init
  git branch -M main
fi

cp -R "$OVERLAY_DIR"/data "$REPO_DIR"/
cp -R "$OVERLAY_DIR"/docs "$REPO_DIR"/
cp -R "$OVERLAY_DIR"/obsidian "$REPO_DIR"/
cp -R "$OVERLAY_DIR"/templates "$REPO_DIR"/
cp "$OVERLAY_DIR"/README_RESUME_OVERLAY.md "$REPO_DIR"/
cp "$OVERLAY_DIR"/INSTALL_FROM_ZIP.md "$REPO_DIR"/

rm -rf "$REPO_DIR/career-system-v0.2.2-resume-overlay"

echo "Overlay installed into: $REPO_DIR"
echo "Next: cd $REPO_DIR && git status && git add . && git commit -m 'Initial Career System v0.2.2 resume foundation'"
