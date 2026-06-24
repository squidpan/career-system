from fastapi import APIRouter
from ..db import get_connection
from ..models import (
    DashboardRecentApplications,
    DashboardRoleCounts,
    DashboardStatusCounts,
    DashboardSummary,
)

router = APIRouter(tags=["dashboard"])


def fetch_counts_by_status():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                select status, count(*)
                from career.job_application
                group by status
                order by status
            """)
            rows = cur.fetchall()

    return {row[0]: row[1] for row in rows}


def fetch_counts_by_role_code():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                select role_code, count(*)
                from career.job_application
                group by role_code
                order by role_code
            """)
            rows = cur.fetchall()

    return {row[0]: row[1] for row in rows}


def fetch_recent_applications(limit: int = 10):
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
                limit %s
            """, (limit,))
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


@router.get("/dashboard/summary", response_model=DashboardSummary)
def get_dashboard_summary():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select count(*) from career.job_application")
            application_count = cur.fetchone()[0]

    return {
        "application_count": application_count,
        "counts_by_status": fetch_counts_by_status(),
        "counts_by_role_code": fetch_counts_by_role_code(),
        "recent_applications": fetch_recent_applications(),
    }


@router.get("/dashboard/statuses", response_model=DashboardStatusCounts)
def get_dashboard_statuses():
    return {
        "counts_by_status": fetch_counts_by_status()
    }


@router.get("/dashboard/roles", response_model=DashboardRoleCounts)
def get_dashboard_roles():
    return {
        "counts_by_role_code": fetch_counts_by_role_code()
    }


@router.get("/dashboard/recent", response_model=DashboardRecentApplications)
def get_dashboard_recent():
    return {
        "recent_applications": fetch_recent_applications()
    }
