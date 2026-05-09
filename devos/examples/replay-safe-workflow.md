# Example: Replay-Safe Feature Slice

This example is generic. Replace names with your repository's terms.

## Slice

Add a deterministic configuration manifest for a build tool.

## Requirement

`REQ-001`: WHEN manifest validation runs, THE SYSTEM SHALL reject missing required fields and return a non-zero exit code.

## Property

`PROP-001`: Manifest validation returns zero only when schema version, source paths, and validation lane names are present.

## Test First

Create a malformed manifest with a missing `schema_version` and assert the validator fails.

## Implementation

Add the smallest validator that reads one explicit file and reports exact missing fields.

## Validation

Run the focused test, then the default validation lane.

## Adversary Review

Ask whether the validator silently skips missing files, assumes hidden defaults, or accepts partial success.

## Evidence

Record the local command, return code, and compact output tail in a repository-local checkpoint. Do not copy this evidence into another repository.
