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

JD_COLUMNS = ["application_id", "jd_type", "file_path", "content_text"]
ARTIFACT_COLUMNS = ["application_id", "artifact_type", "file_path", "content_text"]


def read_text(path_value: str) -> str:
    if not path_value:
        return ""
    path = Path(path_value)
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def write_temp_csv(columns: list[str], rows: list[dict]) -> str:
    tmp = NamedTemporaryFile("w", newline="", encoding="utf-8", delete=False)
    with tmp:
        writer = csv.DictWriter(tmp, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)
    return tmp.name


def run_psql(sql: str) -> None:
    subprocess.run(
        ["psql", "-v", "ON_ERROR_STOP=1", "-h", DB_HOST, "-U", DB_USER, "-d", DB_NAME],
        input=sql,
        text=True,
        check=True,
    )


def load_copy(table: str, columns: list[str], tmp_path: str) -> None:
    columns_sql = ", ".join(columns)
    sql = f"\\copy career.{table} ({columns_sql}) FROM '{tmp_path}' WITH (FORMAT csv, HEADER true);\n"
    run_psql(sql)


def main() -> None:
    jd_rows = []
    artifact_rows = []
    missing = []

    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            app_id = row["application_package_id"]

            for jd_type, field in [
                ("normalized", "normalized_jd_file"),
                ("raw", "raw_jd_file"),
            ]:
                file_path = row.get(field, "").strip()
                content = read_text(file_path)
                if not content:
                    missing.append((app_id, jd_type, file_path))
                    continue

                jd_rows.append({
                    "application_id": app_id,
                    "jd_type": jd_type,
                    "file_path": file_path,
                    "content_text": content,
                })

            package_path = row.get("application_package_path", "").strip()
            submission_notes = str(Path(package_path) / "submission-notes.md") if package_path else ""
            submission_content = read_text(submission_notes)

            if submission_content:
                artifact_rows.append({
                    "application_id": app_id,
                    "artifact_type": "submission_notes",
                    "file_path": submission_notes,
                    "content_text": submission_content,
                })
            else:
                missing.append((app_id, "submission_notes", submission_notes))

            resume_path = row.get("final_resume_file", "").strip()
            resume_content = read_text(resume_path)

            if resume_content:
                artifact_rows.append({
                    "application_id": app_id,
                    "artifact_type": "final_resume",
                    "file_path": resume_path,
                    "content_text": resume_content,
                })
            elif resume_path:
                missing.append((app_id, "final_resume", resume_path))

    jd_tmp = write_temp_csv(JD_COLUMNS, jd_rows)
    artifact_tmp = write_temp_csv(ARTIFACT_COLUMNS, artifact_rows)

    try:
        run_psql("truncate table career.job_description;\ntruncate table career.application_artifact;\n")
        load_copy("job_description", JD_COLUMNS, jd_tmp)
        load_copy("application_artifact", ARTIFACT_COLUMNS, artifact_tmp)
    finally:
        Path(jd_tmp).unlink(missing_ok=True)
        Path(artifact_tmp).unlink(missing_ok=True)

    print(f"Loaded {len(jd_rows)} rows into career.job_description")
    print(f"Loaded {len(artifact_rows)} rows into career.application_artifact")

    if missing:
        print("Missing or empty artifacts:")
        for app_id, artifact_type, file_path in missing:
            print(f"- {app_id} {artifact_type}: {file_path}")


if __name__ == "__main__":
    main()
