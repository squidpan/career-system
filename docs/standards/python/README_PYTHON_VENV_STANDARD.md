# Python Virtual Environment Standard

Status: Active Standard

## Purpose

Provide a consistent Python virtual environment structure across Career System, Motorweb, and future Python services.

## Standard

Each Python service owns its own virtual environment.

Recommended structure:

```text
repo-root/
├── services/
│   ├── career-center-api/
│   │   ├── .venv/
│   │   ├── requirements.txt
│   │   └── app/
│   └── future-service/
│       ├── .venv/
│       └── requirements.txt
```

## Do Not Use

Repository-level virtual environments:

```text
repo-root/.venv
```

Reason:

* Multiple services may require different dependencies.
* Multiple services may require different Python versions.
* Service deployment becomes less portable.
* User validation (pl, ted, bas) becomes more difficult.

## Career Center Standard

Current service:

```text
services/career-center-api
```

Virtual environment location:

```text
services/career-center-api/.venv
```

Create:

```bash
cd services/career-center-api

python3.13 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Deployment Validation

Validated successfully by:

* pl
* ted

during Career Center v0.12 operational hardening.

## Future Alignment

This standard should be adopted by:

* Career System
* Motorweb
* Linux Dev Environment standards
* Future Python microservices

## Multi-User Validation

This standard was validated using:

- pl (primary developer account)
- ted (deployment validation account)

Future validation should include:

- bas (standard developer account)

Each user should create and manage their own service-local virtual environments.

Virtual environments should never be shared between Linux users.

## Lessons Learned

During ted deployment validation, a repository-level virtual environment was initially created.

This caused confusion because:

* Startup scripts expected a service-local virtual environment.
* Different users could create virtual environments in different locations.
* Deployment instructions became inconsistent.

Service-local virtual environments eliminate this ambiguity.

