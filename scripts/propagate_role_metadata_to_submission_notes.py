#!/usr/bin/env python3

from pathlib import Path
import re

PACKAGES = Path("data/application-packages")
JDS = Path("data/jds/normalized")

FIELDS = ["role_id", "role_code", "role_family"]

PACKAGE_TO_JD = {
    "application-broadridge-product-analyst-2026-v1": "jd-broadridge-product-analyst-2026-v1.md",
    "application-citi-ba-it-2026-v1": "jd-citi-ba-it-2026-v1.md",
    "application-finbourne-technology-support-appsupport-2026-v1": "jd-finbourne-technology-support-appsupport-2026-v1.md",
    "application-ice-senior-ba-2026-v1": "jd-ice-ba-2026-v1.md",
    "application-lseg-senior-ba-2026-v1": "jd-lseg-sba-2026-v1.md",
    "application-new-york-life-technical-ba-2026-v1": "jd-new-york-life-sba-2026-v1.md",
    "application-pico-sre-2026-v1": "jd-pico-sre-2026-v1.md",
    "application-qode-ba-2026-v1": "jd-qode-bsa-2026-v1.md",
    "application-shutterstock-ba-2026-v1": "jd-shutterstock-bsa-2026-v1.md",
    "application-the-depository-trust-and-clearing-corporation-dtcc-bsa-2026-v1": "jd-the-depository-trust-and-clearing-corporation-dtcc-bsa-2026-v1.md",
    "application-upmc-systems-analyst-2026-v1": "jd-upmc-systems-analyst-2026-v1.md",
}


def get_field(text: str, field: str) -> str:
    prefix = f"{field}:"

    for line in text.splitlines():
        stripped = line.strip()

        if not stripped.startswith(prefix):
            continue

        value = stripped[len(prefix):].strip()

        if not value:
            return ""

        if value.startswith("#") or value.endswith(":"):
            return ""

        return value

    return ""


def set_field(text: str, field: str, value: str) -> str:
    lines = text.splitlines()
    prefix = f"{field}:"
    updated = False

    for i, line in enumerate(lines):
        if line.startswith(prefix):
            lines[i] = f"{field}: {value}"
            updated = True
            break

    if updated:
        return "\n".join(lines) + "\n"

    return text.replace("## Status", f"{field}: {value}\n\n## Status")


def load_jd(jd_filename: str) -> dict | None:
    jd_path = JDS / jd_filename

    if not jd_path.exists():
        return None

    text = jd_path.read_text(encoding="utf-8", errors="ignore")

    return {
        "path": jd_path,
        "role_id": get_field(text, "role_id"),
        "role_code": get_field(text, "role_code"),
        "role_family": get_field(text, "role_family"),
    }


def propagate(note_path: Path) -> bool:
    package_id = note_path.parent.name
    jd_filename = PACKAGE_TO_JD.get(package_id)

    if not jd_filename:
        print(f"skip unmapped: {package_id}")
        return False

    jd = load_jd(jd_filename)

    if not jd:
        print(f"skip missing jd: {package_id} -> {jd_filename}")
        return False

    text = note_path.read_text(encoding="utf-8")
    original = text

    for field in FIELDS:
        value = jd.get(field, "")
        if value:
            text = set_field(text, field, value)

    if text != original:
        note_path.write_text(text, encoding="utf-8")
        print(f"updated: {package_id} <- {jd['path'].name}")
        return True

    print(f"unchanged: {package_id} <- {jd['path'].name}")
    return False


def main():
    changed = 0

    for note_path in sorted(PACKAGES.glob("*/submission-notes.md")):
        if propagate(note_path):
            changed += 1

    print(f"Updated {changed} submission notes")


if __name__ == "__main__":
    main()
