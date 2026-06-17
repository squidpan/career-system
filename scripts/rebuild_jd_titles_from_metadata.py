#!/usr/bin/env python3

from pathlib import Path
import re

ROOT = Path("data/jds/normalized")

BAD_MARKETING_PATTERNS = [
    "Your success is a train ride away",
    "About The Team",
    "Role profile",
    "Location Designation",
]

def get_field(text: str, field: str) -> str:
    m = re.search(rf"^{re.escape(field)}:\s*(.*)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""

def set_field(text: str, field: str, value: str) -> str:
    pattern = rf"^({re.escape(field)}:\s*)(.*)$"
    replacement = rf"\1{value}"
    return re.sub(pattern, replacement, text, flags=re.MULTILINE)

def clean(value: str) -> str:
    value = (value or "").strip()
    value = value.replace("**", "").strip()
    value = value.strip(" -:").strip()
    return value

def is_bad(value: str) -> bool:
    value = clean(value)
    if not value:
        return True
    lowered = value.lower()
    return any(pattern.lower() in lowered for pattern in BAD_MARKETING_PATTERNS)

def rebuild(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")

    source_title = clean(get_field(text, "source_title"))
    company = clean(get_field(text, "company"))
    current_title = clean(get_field(text, "title"))
    current_normalized = clean(get_field(text, "normalized_title"))

    if not source_title:
        return False

    new_title = f"{source_title} - {company}" if company else source_title
    new_normalized_title = source_title

    should_update = (
        is_bad(current_title)
        or is_bad(current_normalized)
        or current_title != new_title
        or current_normalized != new_normalized_title
    )

    if not should_update:
        return False

    text = set_field(text, "title", new_title)
    text = set_field(text, "normalized_title", new_normalized_title)

    path.write_text(text, encoding="utf-8")
    print(f"rebuilt: {path}")
    return True

def main():
    count = 0
    for path in sorted(ROOT.glob("*.md")):
        if rebuild(path):
            count += 1
    print(f"Rebuilt {count} files")

if __name__ == "__main__":
    main()
