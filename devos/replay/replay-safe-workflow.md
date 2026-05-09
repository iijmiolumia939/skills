# Replay-Safe Workflow

A replay-safe workflow can be rerun from visible inputs and produce the same conclusion or fail closed.

## Pattern

1. Write the requirement.
2. Write the validation property.
3. Add a failing test or check.
4. Implement the smallest change that satisfies it.
5. Generate only repository-local evidence.
6. Run validation.
7. Run adversary review.
8. Record the outcome in an ADR or compact checkpoint.

## Replay-Safe Validation

A replay-safe check should:

- read explicit files
- avoid hidden environment assumptions
- produce deterministic output
- return non-zero on failure
- explain missing prerequisites
- avoid modifying source files during check mode

## Unsafe Patterns

Avoid checks that infer success from logs, silently skip missing inputs, mutate files while validating, or depend on private history that is not in the target repository.
