# US-MW-009B PostgreSQL Permission Cleanup

Status: Done

## User Story

As a Career Center operator,
I want PostgreSQL setup scripts to avoid user-home permission assumptions,
so that setup can run reliably from developer-owned repository paths.

## Acceptance Criteria

- PostgreSQL setup script does not require the postgres OS user to read files from /home/pl or /home/ted.
- SQL files are staged in a neutral readable location before execution.
- postgres commands execute from /tmp to avoid working-directory warnings.
- Setup script completes without "could not change directory" warnings.
- Setup script completes without permission denied errors.

## Validation

Ran `bin/setup-career-center-postgres.sh` after staging SQL files in `/tmp`.
The setup completed successfully without working-directory warnings or SQL file permission errors.

