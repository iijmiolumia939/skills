# Tiny Example: Todo Validator

This is a complete toy project for trying DevOS without any private context or extra tooling.

The project validates a tiny `todo.json` file. It demonstrates one DevOS slice:

- ADR flow
- replay-safe validation
- deterministic observability artifact
- adversary review
- lightweight unattended iteration

## Files

```text
tiny-todo-validator/
  README.md
  todo.json
  bad-todo.json
  validate_todo.py
  devos-manifest.json
  docs/
    ADR-001-todo-validation.md
    adversary-review.md
    observability-run.json
    unattended-iteration.md
```

## Requirement

`REQ-001`: WHEN todo validation runs, THE SYSTEM SHALL reject a todo file unless it contains a `tasks` list where every task has a non-empty `title` string and a `done` boolean.

## Run It

From this directory:

```bash
python validate_todo.py todo.json
```

Expected result: exit code `0` and a deterministic JSON summary with `"ok": true`.

Then run the failing example:

```bash
python validate_todo.py bad-todo.json
```

Expected result: exit code `1` and a deterministic JSON summary naming the invalid fields.

## What DevOS Adds

This example is intentionally small. DevOS adds just enough structure to make the work replayable:

- `docs/ADR-001-todo-validation.md` explains the decision.
- `devos-manifest.json` points to the active requirement and validation commands.
- `validate_todo.py` is the replay-safe validation lane.
- `docs/observability-run.json` shows deterministic facts from one run.
- `docs/adversary-review.md` shows the skeptical review step.
- `docs/unattended-iteration.md` shows how one bounded agent cycle would stop.

Do not turn this into a framework. Copy only the pieces that help your project.