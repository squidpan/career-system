#!/usr/bin/env python3

import csv
import os
import subprocess
from pathlib import Path
from tempfile import NamedTemporaryFile

CSV_PATH = Path("data/application-tracker/applications.csv")
DB_NAME = os.getenv("CAREER_DB_NAME", "career_center")
DB_USER = os.getenv("CAREER_DB_USER", "career_app")
DB_HOST = os.getenv("CAREER_DB_HOST", "localhost")

COLUMNS = [
    "application_id",
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

CSV_TO_DB = {
    "application_package_id": "application_id",
}


def normalize_row(row: dict) -> dict:
    normalized = {}
    for col in COLUMNS:
        source_col = next((k for k, v in CSV_TO_DB.items() if v == col), col)
        value = row.get(source_col, "")
        normalized[col] = value.strip() if value else ""
    return normalized


def main() -> None:
    rows = []

    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(normalize_row(row))

    with NamedTemporaryFile("w", newline="", encoding="utf-8", delete=False) as tmp:
        writer = csv.DictWriter(tmp, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
        tmp_path = tmp.name

    columns_sql = ", ".join(COLUMNS)
    copy_sql = (
        f"\\copy career.job_application ({columns_sql}) "
        f"FROM '{tmp_path}' WITH (FORMAT csv, HEADER true);\n"
    )

    try:
        subprocess.run(
            [
                "psql",
                "-v",
                "ON_ERROR_STOP=1",
                "-h",
                DB_HOST,
                "-U",
                DB_USER,
                "-d",
                DB_NAME,
                "-c",
                "truncate table career.job_application cascade;",
            ],
            check=True,
        )

        subprocess.run(
            [
                "psql",
                "-v",
                "ON_ERROR_STOP=1",
                "-h",
                DB_HOST,
                "-U",
                DB_USER,
                "-d",
                DB_NAME,
            ],
            input=copy_sql,
            text=True,
            check=True,
        )
    finally:
        Path(tmp_path).unlink(missing_ok=True)

    print(f"Loaded {len(rows)} rows into career.job_application")


if __name__ == "__main__":
    main()
