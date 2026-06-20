from fastapi import APIRouter, HTTPException
from ..db import get_connection

router = APIRouter(tags=["applications"])


@router.get("/applications")
def get_applications():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                select
                    application_id,
                    company,
                    role,
                    status,
                    last_update,
                    role_code
                from career.job_application
                order by last_update desc nulls last, company
            """)

            rows = cur.fetchall()

    return [
        {
            "application_id": r[0],
            "company": r[1],
            "role": r[2],
            "status": r[3],
            "last_update": r[4],
            "role_code": r[5],
        }
        for r in rows
    ]

@router.get("/applications/{application_id}")
def get_application(application_id: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select
                    application_id,
                    company,
                    role,
                    role_id,
                    role_code,
                    role_family,
                    status,
                    date_applied,
                    last_update,
                    source,
                    location,
                    employment_type,
                    normalized_jd_file,
                    raw_jd_file,
                    final_resume_file,
                    application_package_path,
                    notes
                from career.job_application
                where application_id = %s
                """,
                (application_id,)
            )
            row = cur.fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Application not found")

    return {
        "application_id": row[0],
        "company": row[1],
        "role": row[2],
        "role_id": row[3],
        "role_code": row[4],
        "role_family": row[5],
        "status": row[6],
        "date_applied": row[7],
        "last_update": row[8],
        "source": row[9],
        "location": row[10],
        "employment_type": row[11],
        "normalized_jd_file": row[12],
        "raw_jd_file": row[13],
        "final_resume_file": row[14],
        "application_package_path": row[15],
        "notes": row[16],
        }

@router.get("/applications/{application_id}/jd")
def get_application_jd(application_id: str):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select
                    jd_type,
                    file_path,
                    content_text
                from career.job_description
                where application_id = %s
                order by jd_type
                """,
                (application_id,)
            )
            rows = cur.fetchall()

    if not rows:
        raise HTTPException(status_code=404, detail="Job descriptions not found")

    return {
        "application_id": application_id,
        "job_descriptions": [
            {
                "jd_type": r[0],
                "file_path": r[1],
                "content_text": r[2],
            }
            for r in rows
        ],
    }


@router.get("/applications/{application_id}/artifacts")
def get_application_artifacts(application_id: str):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                select
                    artifact_type,
                    file_path,
                    content_text
                from career.application_artifact
                where application_id = %s
                order by artifact_type
                """,
                (application_id,)
            )

            rows = cur.fetchall()

    if not rows:
        raise HTTPException(
            status_code=404,
            detail="Artifacts not found"
        )

    return {
        "application_id": application_id,
        "artifacts": [
            {
                "artifact_type": r[0],
                "file_path": r[1],
                "content_text": r[2],
            }
            for r in rows
        ]
    }


