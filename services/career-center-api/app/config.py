import os

DB_HOST = os.getenv("CAREER_DB_HOST", "localhost")
DB_NAME = os.getenv("CAREER_DB_NAME", "career_center")
DB_USER = os.getenv("CAREER_DB_USER", "career_app")
DB_PASSWORD = os.getenv("CAREER_DB_PASSWORD", "")
