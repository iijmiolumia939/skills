# When Not To Use DevOS

DevOS is useful when engineering work needs memory, replay, validation, and review. It is not the right tool for every task.

## Probably Overkill

DevOS is probably too much for:

- tiny one-file scripts
- throwaway prototypes
- short-lived experiments
- single-session tasks
- work where no one will replay, audit, or extend the result

For those cases, use normal notes, simple tests, and ordinary commits.

## Good Fit

DevOS is a good fit for:

- long-running AI-assisted projects
- unattended engineering loops
- replay-sensitive systems
- audit-heavy workflows
- governance-sensitive repositories
- teams that need decisions, validation, and evidence to survive beyond one chat session

## Rule Of Thumb

Use DevOS when the cost of forgetting context is higher than the cost of writing a short ADR, a small manifest, and a validation command.

Keep the first version small. If the workflow starts feeling like ceremony, remove pieces until it helps again.