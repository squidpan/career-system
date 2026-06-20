from fastapi import APIRouter
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
