# DevOS Autonomous Engineering Substrate

DevOS is a practical workflow for AI-assisted software engineering. It helps teams make small changes with visible decisions, deterministic validation, adversary review, and compact evidence.

Start with [DevOS Quick Start](quick-start.md). It is the shortest path to using this package.

This package is intentionally small. It contains public-safe docs, templates, prompts, and examples only. It does not contain project history, generated proof archives, domain-specific validators, or experimental prototypes.

## What This Package Provides

- a five-minute [quick start](quick-start.md)
- a tiny self-contained [example project](examples/tiny-todo-validator/README.md)
- deterministic replay workflow patterns
- repository-as-memory and manifest patterns
- replay-safe validation and gate patterns
- adversary review workflow patterns
- lightweight unattended loop patterns
- deterministic observability documentation
- traceability workflow templates
- replay-safe ADR templates and examples

## What This Package Excludes

- project-specific implementation code
- generated proof and checkpoint churn
- private defect or sprint history
- domain-specific research workflows
- unstable experimental modules
- large historical decision chains
- any artifact that needs private context to understand

If an artifact is not clearly reusable, public-safe, and self-contained, leave it out.

## Structure

- `quick-start.md` gives the shortest usable workflow.
- `when-not-to-use.md` explains where DevOS is overkill.
- `concepts/` explains the substrate in project-agnostic language.
- `governance/` defines roles, invariants, and ADR boundaries.
- `replay/` describes deterministic replay-safe workflows.
- `observability/` explains deterministic engineering observability.
- `orchestration/` covers execution economics and bounded telemetry.
- `harness/` describes lightweight unattended loops.
- `traceability/` gives ID and evidence-chain practices.
- `prompts/` contains reusable prompt templates.
- `examples/` contains generic public-safe examples.

## Adoption Path

1. Read [DevOS Quick Start](quick-start.md).
2. Run through the [tiny todo validator example](examples/tiny-todo-validator/README.md).
3. Copy the smallest useful pieces into your repository: one ADR, one requirement, one validation command, one review step.
4. Add observability only as deterministic facts, not scores or diagnoses.
5. Check [When Not To Use DevOS](when-not-to-use.md) before adding more process.

DevOS should make engineering work easier to audit, not harder to understand.
