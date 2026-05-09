# Autonomous Engineering Substrate

An autonomous engineering substrate is a small operating model for letting AI agents do useful engineering work while preserving human-auditable evidence.

It has five parts:

1. A decision protocol for non-trivial choices.
2. A traceability scheme for requirements, tests, implementation, and evidence.
3. A replay-safe validation lane that fails closed.
4. A manifest-memory pattern for compact context loading.
5. An adversary review step before work is declared complete.

## Design Principles

- Prefer small vertical slices over giant plans.
- Write requirements before implementation.
- Add a failing test before production changes.
- Treat generated evidence as local to the repository that generated it.
- Use explicit non-claims to prevent hidden interpretation.
- Keep reusable templates separate from repository-specific gates.

## Non-Goals

DevOS is not a dashboard, project management system, model benchmark, or replacement for engineering judgment. It is a substrate for making autonomous work inspectable, repeatable, and reviewable.
