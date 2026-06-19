#!/usr/bin/env python3

import csv
from pathlib import Path

ROOT = Path("data/application-packages")
JD_NORMALIZED = Path("data/jds/normalized")
JD_RAW = Path("data/jds/raw")
OUT = Path("data/application-tracker/applications.csv")

FIELDS = [
    "application_package_id",
    "company",
    "role",
    "role_id",
    "role_code",
    "role_family",
    "status",
    "date_applied",
    "last_update",
    "source",
    "location",
    "employment_type",
    "resumes",
    "cover_letters",
    "normalized_jd_file",
    "raw_jd_file",
    "final_resume_file",
    "application_package_path",
    "notes",
]

PACKAGE_TO_NORMALIZED_JD = {
    "application-broadridge-product-analyst-2026-v1": "data/jds/normalized/jd-broadridge-product-analyst-2026-v1.md",
    "application-citi-ba-it-2026-v1": "data/jds/normalized/jd-citi-ba-it-2026-v1.md",
    "application-finbourne-technology-support-appsupport-2026-v1": "data/jds/normalized/jd-finbourne-technology-support-appsupport-2026-v1.md",
    "application-ice-senior-ba-2026-v1": "data/jds/normalized/jd-ice-ba-2026-v1.md",
    "application-lseg-senior-ba-2026-v1": "data/jds/normalized/jd-lseg-sba-2026-v1.md",
    "application-new-york-life-technical-ba-2026-v1": "data/jds/normalized/jd-new-york-life-sba-2026-v1.md",
    "application-pico-sre-2026-v1": "data/jds/normalized/jd-pico-sre-2026-v1.md",
    "application-qode-ba-2026-v1": "data/jds/normalized/jd-qode-bsa-2026-v1.md",
    "application-shutterstock-ba-2026-v1": "data/jds/normalized/jd-shutterstock-bsa-2026-v1.md",
    "application-the-depository-trust-and-clearing-corporation-dtcc-bsa-2026-v1": "data/jds/normalized/jd-the-depository-trust-and-clearing-corporation-dtcc-bsa-2026-v1.md",
    "application-upmc-systems-analyst-2026-v1": "data/jds/normalized/jd-upmc-systems-analyst-2026-v1.md",
}

PACKAGE_TO_RAW_JD = {
    "application-broadridge-product-analyst-2026-v1": "data/jds/raw/jd-raw-broadridge-product-analyst.md",
    "application-citi-ba-it-2026-v1": "data/jds/raw/jd-raw-citi-it-ba.md",
    "application-finbourne-technology-support-appsupport-2026-v1": "data/jds/raw/jd-raw-finbourne-appsupport-api.md",
    "application-ice-senior-ba-2026-v1": "data/jds/raw/jd-raw-ice-ba.md",
    "application-lseg-senior-ba-2026-v1": "data/jds/raw/jd-raw-lseg-ba-product-development-tradeagent.md",
    "application-new-york-life-technical-ba-2026-v1": "data/jds/raw/jd-raw-new-york-life-senior-associate-technical-business-analyst.md",
    "application-pico-sre-2026-v1": "data/jds/raw/jd-raw-pico-sre.md",
    "application-qode-ba-2026-v1": "data/jds/raw/jd-raw-qode-ba.md",
    "application-shutterstock-ba-2026-v1": "data/jds/raw/jd-raw-shutterstock-ba.md",
    "application-the-depository-trust-and-clearing-corporation-dtcc-bsa-2026-v1": "data/jds/raw/jd-raw-dtcc-lead-bsa.md",
    "application-upmc-systems-analyst-2026-v1": "data/jds/raw/jd-raw-upmc-systems-analyst.md",
}

def parse_note(path: Path) -> dict:
    data = {field: "" for field in FIELDS}
    data["application_package_id"] = path.parent.name
    data["application_package_path"] = str(path.parent)

    current_list = None
    lists = {"resumes": [], "cover_letters": [], "notes": []}

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()

        if not line or line.startswith("#"):
            continue

        if line in ("resumes:", "cover_letters:", "notes:"):
            current_list = line[:-1]
            continue

        if line.startswith("- ") and current_list:
            value = line[2:].strip()
            if value:
                lists[current_list].append(value)
            continue

        current_list = None

        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key in data:
                data[key] = value

    for key, values in lists.items():
        data[key] = "|".join(values)

    populate_artifact_references(data, path.parent)

    return data


def populate_artifact_references(data: dict, package_dir: Path) -> None:
    application_id = data["application_package_id"]
    role_id = data.get("role_id", "").strip()

    data["normalized_jd_file"] = find_normalized_jd(application_id, role_id)
    data["raw_jd_file"] = find_raw_jd(application_id)
    data["final_resume_file"] = find_final_resume(package_dir, data.get("resumes", ""))


def find_normalized_jd(application_id: str, role_id: str) -> str:
    mapped = PACKAGE_TO_NORMALIZED_JD.get(application_id)
    if mapped and Path(mapped).exists():
        return mapped

    candidates = []

    if role_id.startswith("role-"):
        stem = "jd-" + role_id.removeprefix("role-")
        candidates.append(JD_NORMALIZED / f"{stem}.md")

    app_stem = application_id.removeprefix("application-")
    candidates.append(JD_NORMALIZED / f"jd-{app_stem}.md")

    for candidate in candidates:
        if candidate.exists():
            return str(candidate)

    return ""

def find_raw_jd(application_id: str) -> str:
    mapped = PACKAGE_TO_RAW_JD.get(application_id)
    if mapped and Path(mapped).exists():
        return mapped

    app_stem = application_id.removeprefix("application-")
    candidates = [
        JD_RAW / f"jd-raw-{app_stem}.md",
        JD_RAW / f"raw-{app_stem}.md",
    ]

    for candidate in candidates:
        if candidate.exists():
            return str(candidate)

    matches = sorted(JD_RAW.glob(f"*{app_stem}*.md"))
    if matches:
        return str(matches[0])

    return ""

def find_final_resume(package_dir: Path, resumes_value: str) -> str:
    resume_names = [r.strip() for r in resumes_value.split("|") if r.strip()]

    preferred = [
        "ats-resume.html",
        "full-resume.html",
        "ats-resume.md",
        "full-resume.md",
    ]

    for name in preferred:
        if name in resume_names and (package_dir / name).exists():
            return str(package_dir / name)

    for name in resume_names:
        candidate = package_dir / name
        if candidate.exists():
            return str(candidate)

    for name in preferred:
        candidate = package_dir / name
        if candidate.exists():
            return str(candidate)

    return ""


def main():
    rows = []
    for note in sorted(ROOT.glob("*/submission-notes.md")):
        rows.append(parse_note(note))

    OUT.parent.mkdir(parents=True, exist_ok=True)

    with OUT.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {OUT} with {len(rows)} rows")


if __name__ == "__main__":
    main()
