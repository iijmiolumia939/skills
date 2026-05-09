# Compact Context Engineering

Context engineering is deciding what an agent should load, remember, summarize, and ignore while doing engineering work.

## Manifest-Memory Pattern

Use a manifest as a compact index of authoritative files. The manifest tells an agent where to find current requirements, active decisions, validation commands, and examples. It should not replay history.

A useful manifest answers:

- What files are authoritative right now?
- Which IDs are active?
- Which validation commands matter?
- What was intentionally excluded?
- Where is the latest checkpoint?

## Checkpoint Pattern

A checkpoint is a compact recovery artifact. It should contain enough state to resume work without loading full logs.

A checkpoint usually includes:

- objective
- active IDs
- changed files
- blockers
- latest validation status
- next action

## Budget Discipline

Context budgets should trigger action, not anxiety. A soft budget asks the agent to checkpoint and prune. A hard budget asks the agent to stop loading more history and resume from the manifest plus latest checkpoint.
