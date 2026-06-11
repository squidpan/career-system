#!/usr/bin/env python3

import json
import sys
from pathlib import Path


REQUIRED_FILES = [
    "resume.md",
    "resume-final.md",
    "application-summary.md",
    "interview-prep.md",
    "cover-letter-notes.md",
    "package-manifest.json",
]


def read_text_if_exists(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def check_phrase(text: str, phrase: str) -> bool:
    return phrase.lower() in text.lower()


def main():
    if len(sys.argv) != 3:
        print("Usage: generate_application_readiness_report.py <application-package-dir> <output-md>")
        sys.exit(1)

    package_dir = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    checks = []
    missing = []

    for filename in REQUIRED_FILES:
        path = package_dir / filename
        exists = path.exists()
        checks.append((filename, exists))
        if not exists:
            missing.append(filename)

    resume_final = read_text_if_exists(package_dir / "resume-final.md")
    application_summary = read_text_if_exists(package_dir / "application-summary.md")
    interview_prep = read_text_if_exists(package_dir / "interview-prep.md")
    manifest_text = read_text_if_exists(package_dir / "package-manifest.json")

    application_id = package_dir.name
    source_jd = ""

    if manifest_text:
        try:
            manifest = json.loads(manifest_text)
            source_jd = manifest.get("source_resume_recommendation", "")
        except json.JSONDecodeError:
            source_jd = "package-manifest.json is not valid JSON"

    readiness_items = []

    if resume_final:
        readiness_items.append(("Final resume exists", True))
    else:
        readiness_items.append(("Final resume exists", False))

    if check_phrase(resume_final, "Federal Reserve Bank of New York (On-Site via Gresham)"):
        readiness_items.append(("Preferred FRBNY/Gresham wording present", True))
    else:
        readiness_items.append(("Preferred FRBNY/Gresham wording present", False))

    if check_phrase(resume_final, "Relevant Experience"):
        readiness_items.append(("Relevant Experience section present", True))
    else:
        readiness_items.append(("Relevant Experience section present", False))

    if application_summary:
        readiness_items.append(("Application summary exists", True))
    else:
        readiness_items.append(("Application summary exists", False))

    if interview_prep:
        readiness_items.append(("Interview prep exists", True))
    else:
        readiness_items.append(("Interview prep exists", False))

    # Role-specific soft checks
    finbourne_terms = [
        "streaming",
        "market-data",
        "production support",
        "application support",
        "REST API",
        "AWS",
        "disaster-recovery",
    ]

    citi_terms = [
        "requirements",
        "stakeholder",
        "SDLC",
        "UAT",
        "business",
        "system requirements",
        "risk",
    ]

    if "finbourne" in application_id.lower():
        for term in finbourne_terms:
            readiness_items.append((f"Finbourne keyword present: {term}", check_phrase(resume_final, term)))

    if "citi" in application_id.lower():
        for term in citi_terms:
            readiness_items.append((f"Citi keyword present: {term}", check_phrase(resume_final, term)))

    failed_items = [label for label, ok in readiness_items if not ok]

    status = "READY TO APPLY" if not missing and not failed_items else "NEEDS REVIEW"

    lines = []
    lines.append("# Application Readiness Report")
    lines.append("")
    lines.append(f"Application Package: `{application_id}`")
    lines.append(f"Status: **{status}**")
    lines.append("")
    lines.append("## Required Files")
    lines.append("")

    for filename, exists in checks:
        mark = "✅" if exists else "❌"
        lines.append(f"- {mark} `{filename}`")

    lines.append("")
    lines.append("## Readiness Checks")
    lines.append("")

    for label, ok in readiness_items:
        mark = "✅" if ok else "❌"
        lines.append(f"- {mark} {label}")

    lines.append("")
    lines.append("## Source References")
    lines.append("")
    lines.append(f"- Package directory: `{package_dir}`")
    if source_jd:
        lines.append(f"- Source recommendation: `{source_jd}`")

    lines.append("")
    lines.append("## Review Notes")
    lines.append("")

    if status == "READY TO APPLY":
        lines.append("- Resume-final exists and passes core readiness checks.")
        lines.append("- Application package is ready for final human review and submission.")
    else:
        lines.append("- Review missing files or failed checks before submitting.")
        for item in missing:
            lines.append(f"- Missing required file: `{item}`")
        for item in failed_items:
            lines.append(f"- Failed readiness check: {item}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
