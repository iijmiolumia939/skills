# Lightweight Unattended Loop

An unattended loop lets an agent progress through one small engineering slice without waiting for repeated approval.

## Loop Shape

1. Planner frames the slice and decision boundary.
2. Generator writes the spec, failing test, and implementation.
3. Evaluator runs the validation lane.
4. Adversary reviews for defects and slop.
5. Recorder writes an ADR, checkpoint, or evidence note.
6. The loop stops on failure or continues to the next bounded slice.

## Stop Conditions

Stop when validation fails and cannot be repaired, adversary finds a blocking defect, external authorization is required, or the cycle limit is reached.

## Safety Rules

- Never weaken a failing gate to continue.
- Never treat a clean boundary as permission to export history.
- Never copy generated evidence between repositories.
- Prefer a small failing test over a broad claim of correctness.
