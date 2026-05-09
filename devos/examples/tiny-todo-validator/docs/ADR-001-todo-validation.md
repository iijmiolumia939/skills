# ADR-001: Validate The Todo File Shape

## Status

Accepted

## Context

The toy project needs one replay-safe validation lane. The validation should be small enough to run locally and strict enough to fail when required fields are missing.

## Decision

Validate `todo.json` with a standard-library Python script. A valid todo file must contain a `tasks` list. Each task must contain a non-empty `title` string and a `done` boolean.

## Consequences

- The validation command is deterministic and has no external dependencies.
- Invalid files fail with exit code `1` and exact field errors.
- The example remains copyable into a new repository.
- This ADR does not claim the toy project is a task manager or production schema.