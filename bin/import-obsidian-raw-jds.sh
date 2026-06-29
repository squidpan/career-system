#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="${SOURCE_DIR:-$HOME/pjs/vaults/plvault/Clippings/Careers/JDs/Raw}"
TARGET_DIR="${TARGET_DIR:-$HOME/pjs/repos/career-system/data/jds/raw}"

mkdir -p "$TARGET_DIR"

copy_one() {
  local input="$1"
  local src
  local base

  base="$(basename "$input")"

  if [[ "$input" = /* || "$input" == */* ]]; then
    src="$input"
  else
    src="$SOURCE_DIR/$input"
  fi

  if [[ ! -f "$src" ]]; then
    echo "MISS  $src"
    return 1
  fi

  if [[ -f "$TARGET_DIR/$base" ]]; then
    echo "SKIP  $base"
  else
    cp -n "$src" "$TARGET_DIR/"
    echo "COPY  $base"
  fi
}

echo "Source: $SOURCE_DIR"
echo "Target: $TARGET_DIR"
echo

if [[ "$#" -gt 0 ]]; then
  for file in "$@"; do
    copy_one "$file"
  done
else
  find "$SOURCE_DIR" -maxdepth 1 -type f -name 'jd-raw-*.md' -print0 \
    | sort -z \
    | while IFS= read -r -d '' file; do
        copy_one "$file"
      done
fi

echo
echo "Done."
