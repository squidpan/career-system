from fastapi import APIRouter
from ..db import get_connection

router = APIRouter(tags=["dashboard"])


@router.get("/dashboard/summary")
def get_dashboard_summary():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select count(*) from career.job_application")
            application_count = cur.fetchone()[0]

            cur.execute("""
                select status, count(*)
                from career.job_application
                group by status
                order by status
            """)
            counts_by_status = {row[0]: row[1] for row in cur.fetchall()}

            cur.execute("""
                select role_code, count(*)
                from career.job_application
                group by role_code
                order by role_code
            """)
            counts_by_role_code = {row[0]: row[1] for row in cur.fetchall()}

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
                limit 10
            """)
            recent_rows = cur.fetchall()

    return {
        "application_count": application_count,
        "counts_by_status": counts_by_status,
        "counts_by_role_code": counts_by_role_code,
        "recent_applications": [
            {
                "application_id": r[0],
                "company": r[1],
                "role": r[2],
                "status": r[3],
                "last_update": r[4],
                "role_code": r[5],
            }
            for r in recent_rows
        ],
    }
