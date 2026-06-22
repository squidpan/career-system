# SPRINT-2026-07 Operational Hardening and Dashboard Foundation

Target Release:
v0.12.0-operational-hardening

## Objective

Improve deployment reliability, environment consistency, and operational readiness while beginning the transition from deployment validation to operational Career Center usage.

## Epic A — Operational Hardening

### US-MW-009A PostgreSQL Idempotency

Ensure database and role creation scripts can be executed repeatedly without errors.

### US-MW-009B PostgreSQL Permission Cleanup

Remove postgres working-directory warnings and standardize deployment execution paths.

### US-MW-009C Startup Validation Checks

Validate required environment variables, database connectivity, and application prerequisites during startup.

### US-MW-009D Python Virtual Environment Standard

Define and document standard venv location and activation conventions.

### US-MW-009E Developer Bootstrap Standard

Create repeatable setup process for new Linux users (pl, ted, bas, future users).

## Epic B — API and Dashboard Foundation

### US-MW-010A Application Dashboard API

Expose dashboard summary data through REST endpoints.

Examples:

* Applications by status
* Application counts
* Recent applications

### US-MW-010B OpenAPI / Swagger Completion

Make OpenAPI specification authoritative and validate Swagger exposure from the running service.

### US-MW-010C Dashboard Query API

Expose existing dashboard SQL queries through REST endpoints.

## Expected Outcome

Career Center can be installed, deployed, and operated consistently by approved Linux users while providing dashboard-oriented APIs that can be consumed by future Motorweb applications.

## Deferred

* React UI
* Authentication
* HTTPS
* Containers
* Kubernetes
* Cloud deployment

