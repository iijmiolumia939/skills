# Autonomous Engineering Substrate

An autonomous engineering substrate is a small set of repository habits for AI-assisted software work. It helps an agent make progress while leaving decisions, checks, and evidence that a human can review later.

DevOS starts with five parts:

1. A decision protocol for non-trivial choices.
2. A traceability scheme for requirements, tests, implementation, and evidence.
3. A replay-safe validation lane that fails closed.
4. A manifest-memory pattern for compact context loading.
5. An adversary review step before work is called complete.

## Design Principles

- Prefer small vertical slices over giant plans.
- Write requirements before implementation.
- Add a failing test before production changes.
- Treat generated evidence as local to the repository that generated it.
- Use explicit non-claims to prevent hidden interpretation.
- Keep reusable templates separate from repository-specific gates.

## Non-Goals

DevOS is not a dashboard, project management system, model benchmark, or replacement for engineering judgment. It is a practical way to make AI-assisted work inspectable, repeatable, and reviewable.
