# Example: Lightweight Unattended Workflow

## Cycle Limit

Use a small cycle limit, such as one to four slices. A clean boundary is not automatically a stop condition, but the cycle limit is.

## Cycle

1. Council chooses a bounded slice.
2. Agent writes ADR and requirement.
3. Agent adds a failing test.
4. Agent implements the slice.
5. Agent runs focused validation.
6. Agent runs adversary and no-slop checks.
7. Agent commits if all gates pass.
8. Agent opens the next question or stops at the cycle limit.

## Stop Conditions

- validation cannot be repaired
- adversary has a blocking finding
- authorization is required
- the cycle limit is reached

## Safety Note

Do not continue by weakening assertions, deleting checks, or converting a failure into a warning.
