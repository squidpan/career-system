# US-CS-051 Role Metadata Propagation From Normalized JD

Status: Planned

## Business Context

Role metadata such as role_code and role_family should come from normalized JD metadata, not manual entry.

## Acceptance Criteria

- role_code remains optional until normalization is reliable.
- role_family remains optional until normalization is reliable.
- Future tracker generation can enrich applications.csv from normalized JD metadata.

## Validation

Manual review of normalized JD front matter and generated application tracker.
