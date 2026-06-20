from fastapi import FastAPI
from .db import get_connection
from .routers import applications

app = FastAPI(
    title="Career Center API",
    version="1.0.0"
)

app.include_router(applications.router)


@app.get("/health")
def health():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "select current_database(), current_user, current_schema();"
            )
            row = cur.fetchone()

    return {
        "status": "UP",
        "database": row[0],
        "user": row[1],
        "schema": row[2],
    }
