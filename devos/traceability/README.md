# Traceability Workflow

Traceability is the evidence chain connecting intent to implementation.

## Suggested IDs

- `ADR-###` for decisions
- `REQ-###` for requirements
- `PROP-###` for properties or invariants
- `TEST-###` for tests and checks
- `IMPL-###` for implementation units
- `FIND-###` for defects found during review
- `PROOF-###` for repository-local validation evidence

## Minimal Chain

A useful chain is:

`ADR -> REQ -> PROP -> TEST -> IMPL -> local evidence`

The chain should be easy to follow from a single manifest or README. Do not require readers to load old sprint history.

## Public Package Rule

Examples may show ID formats, but they must not include private defect history or generated proof artifacts from another repository.
