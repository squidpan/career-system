# US-MW-006A Create career_center Database and Application User

Status: Done

## User Story

As a Career System / Motorweb developer,
I want a dedicated local PostgreSQL database, schema, and application user,
so that Career System application tracking data can be loaded into PostgreSQL without reusing unrelated existing databases.

## Background

PostgreSQL local environment audit completed on 2026-06-19.

Approved environment:

- OS: Pop!_OS 22.04 LTS
- PostgreSQL: 14.23
- pgAdmin4: 9.15
- Cluster: 14/main
- Port: 5432
- Access: localhost only

Existing databases must not be reused:

- demo
- mydb
- questiondb
- quizdb
- squidpan

## Target Database Setup

- Database: `career_center`
- Application user/role: `career_app`
- Schema: `career`

## Acceptance Criteria

- `career_center` database exists.
- `career_app` role exists.
- `career` schema exists inside `career_center`.
- `career_app` has appropriate privileges on the `career` schema.
- Connectivity verified from `psql`.
- Connectivity verified from pgAdmin.
- Existing databases are not modified.
- Setup steps are repeatable and documented.
- No application tables are created in this story.

## Out of Scope

- Creating application tables
- Loading CSV data
- Creating REST APIs
- Creating Motorweb FastAPI endpoints

## Implementation Notes

This story follows the approved PostgreSQL standard:

- PostgreSQL infrastructure investigation is complete.
- Infrastructure standard remains owned by Linux Dev Environment / Tooling Best Practices.
- Career System owns only application-specific database objects and loaders.

## Validation Commands

Expected validation examples:

```sql
select current_database();
select current_schema();
select current_user;
