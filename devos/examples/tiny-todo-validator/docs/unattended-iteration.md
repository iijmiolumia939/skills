# Unattended Iteration

## Cycle Limit

One cycle.

## Slice

Add replay-safe validation for `todo.json`.

## Loop

1. Planner chooses `REQ-001` as the only slice.
2. Generator writes ADR-001 and the failing `bad-todo.json` fixture.
3. Generator implements `validate_todo.py`.
4. Evaluator runs both validation commands from `devos-manifest.json`.
5. Adversary checks for hidden defaults, silent failures, and private context.
6. Recorder updates `docs/observability-run.json` with deterministic facts.

## Stop Condition

Stop after the first completed slice. Do not continue into a larger todo application unless a new ADR and requirement are added.