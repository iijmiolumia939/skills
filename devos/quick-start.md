# DevOS Quick Start

DevOS is a lightweight workflow for AI-assisted engineering. It helps you keep decisions, validation, review, and evidence visible while an agent works through small changes.

Use this page when you want the shortest practical path.

## The Five-Minute Version

DevOS asks you to keep five things in your repository:

1. A short decision note for important choices.
2. A tiny requirement for the next change.
3. A validation command that fails when the change is wrong.
4. A review step that tries to find defects before you call the work done.
5. A compact note of what changed and what was observed.

That is the whole starting point. You can add more structure later only if the project earns it.

## Minimal Workflow

```text
Pick one small change
        |
        v
Write ADR-001 and REQ-001
        |
        v
Add a failing check
        |
        v
Implement the smallest fix
        |
        v
Run validation and record facts
        |
        v
Run adversary review
        |
        v
Commit the slice
```

## First Steps

1. Create `docs/adr/ADR-001-first-slice.md` and write the decision in plain language.
2. Create a repository manifest such as `devos-manifest.json` that points to the current ADR, requirement, validation command, and example files.
3. Write one requirement using a simple format: `WHEN <trigger>, THE SYSTEM SHALL <response>.`
4. Add the smallest validation command you can run locally.
5. Ask an adversary reviewer to check whether the change hides defaults, skips errors, or depends on private context.

## Repository As Memory

DevOS treats the repository as the source of truth. Important state should live in files that can be reviewed, diffed, replayed, and restored.

A small manifest is enough at first:

```json
{
  "schema_version": 1,
  "active_slice": "REQ-001",
  "current_decision": "docs/adr/ADR-001-first-slice.md",
  "validation": ["python validate.py"],
  "latest_checkpoint": "docs/checkpoints/latest.md"
}
```

The manifest is not a history archive. It is a map to the current working context.

## Replay-Safe Workflow

Replay-safe work means another engineer or agent can understand what happened without reading a private chat log.

Keep the chain short:

`decision -> requirement -> validation -> implementation -> observed facts -> review`

Do not copy generated proof, old logs, or private project history into a public package.

## Lightweight Unattended Loop

An unattended loop is one bounded pass through the workflow:

1. Plan one slice.
2. Write or update the requirement.
3. Add the failing check.
4. Implement.
5. Run validation.
6. Run adversary review.
7. Stop on failure, ambiguity, or the cycle limit.

Start with a one-cycle limit. The point is reliable progress, not endless autonomy.

## Observability In One Minute

DevOS observability records deterministic facts about the engineering run:

- what artifacts changed during replay
- which commands ran and how they ended
- whether a gate refused to make an unsupported claim
- which source files directly produced which evidence files

It does not score engineers, diagnose root causes, rank files, or run an AI monitoring dashboard.

## Adversary Review

Adversary review is a final skeptical pass. It asks:

- Does the change satisfy the requirement?
- Does validation fail closed?
- Are there hidden defaults or silent failures?
- Is the evidence local to this repository?
- Is anything presented with more certainty than the facts allow?

Use [examples/tiny-todo-validator/README.md](examples/tiny-todo-validator/README.md) for a complete toy slice.