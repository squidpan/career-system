# PostgreSQL Local Development Environment Audit and Standardization

## Purpose

I am preparing to use PostgreSQL as the persistence layer for Career System and Motorweb.

Before creating databases, schemas, loaders, APIs, or dashboards, I want to validate and standardize my local PostgreSQL environment on:

* System76 Pangolin 16
* Pop!_OS 22.04 LTS
* Primary user: pl
* Existing PostgreSQL installation present
* Existing pgAdmin installation present
* Existing Spring Boot project(s) already using PostgreSQL
* Existing local database(s) may already exist

The goal is to establish repeatable Linux Dev Environment standards before building application-specific databases.

---

# Current Career System Context

Career System has completed:

* Application Tracker CSV generation
* Application Tracker Dashboard
* Role Metadata Propagation
* Artifact References
* JD linkage
* Resume linkage
* Package linkage

The next major milestone is:

US-MW-006 Load Application Artifacts into PostgreSQL

followed by

US-MW-007 Application Detail REST APIs

However:

NO PostgreSQL schema work should begin until the local PostgreSQL environment has been audited and standardized.

---

# Audit Objectives

Please provide SAFE READ-ONLY scripts and commands.

Do not modify anything.

Audit the following:

## PostgreSQL Installation

Determine:

* Installed PostgreSQL packages
* Package source
* PostgreSQL server version
* PostgreSQL client version
* Available clusters
* Active cluster version
* Data directory locations
* Configuration file locations

---

## Running Services

Determine:

* PostgreSQL service status
* Startup configuration
* Listening ports
* Active processes

---

## Networking

Determine:

* Which ports PostgreSQL is listening on
* Whether localhost access is working
* Whether external access is enabled

---

## Authentication

Determine:

* Existing PostgreSQL users
* Existing PostgreSQL roles
* Existing databases
* Existing ownership relationships

WITHOUT changing passwords.

---

## pgAdmin

Determine:

* Installed version
* Install method
* Upgrade path
* Whether current version should be upgraded
* Recommended best-practice installation method

Example:

* distro package
* PGDG package
* container
* other

---

## Existing Databases

Identify:

* Databases currently present
* Which appear application-related
* Which appear system-related

No modifications.

---

## Tooling Best Practice Recommendation

Recommend:

* PostgreSQL installation standard
* pgAdmin installation standard
* Backup approach
* Restore approach
* Upgrade approach
* Local development workflow

for a single-developer Linux workstation.

---

# Desired Deliverables

Please generate:

## 1. Audit Script

Single read-only script.

Example:

audit-postgres.sh

---

## 2. Findings Summary

Explain:

* what is installed
* what is healthy
* what should be improved

---

## 3. Recommended Standard

Document:

PostgreSQL Standard v1

including:

* version strategy
* upgrade strategy
* backup strategy
* pgAdmin strategy

---

# Expected Output To Bring Back To Career System

After completing the audit, I will return with:

1. PostgreSQL version
2. pgAdmin version
3. Installed packages
4. Active databases
5. Active users/roles
6. Recommended installation standard
7. Recommended upgrade actions
8. Recommended backup approach
9. Any identified issues

Career System will then proceed with:

* career_center database creation
* schema design
* CSV loaders
* SQL dashboard queries
* REST API integration

without re-discussing infrastructure setup.

