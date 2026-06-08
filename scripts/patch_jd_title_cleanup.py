#!/usr/bin/env python3
from pathlib import Path

p = Path("scripts/generate_jd_intelligence.py")
s = p.read_text(encoding="utf-8")

old = '    title = fm.get("normalized_title") or fm.get("title") or jd_path.stem\n'
new = """    # v0.5.1.3: prefer source_title because normalized_title can contain
    # body-derived headings for some web-clipped JDs.
    title = (
        fm.get("source_title")
        or fm.get("normalized_title")
        or fm.get("title")
        or jd_path.stem
    )
"""

if old not in s:
    raise SystemExit(
        "Expected title assignment not found. Run: "
        "grep -n \"title = fm.get\" scripts/generate_jd_intelligence.py"
    )

s = s.replace(old, new)
p.write_text(s, encoding="utf-8")
print("Patched scripts/generate_jd_intelligence.py title precedence")
