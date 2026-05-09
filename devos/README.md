# DevOS Autonomous Engineering Substrate

DevOS is a reusable operating model for AI-assisted software engineering. It helps teams run autonomous engineering work in small, replay-safe slices with visible decisions, explicit validation, and adversarial review.

This package is intentionally small. It contains public-safe docs, templates, prompts, and examples only. It does not contain project history, generated proof archives, domain-specific validators, or experimental prototypes.

## What This Package Provides

- deterministic replay workflow patterns
- manifest-memory and context loading patterns
- replay-safe validation and gate patterns
- governance invariant patterns
- adversary review workflow patterns
- lightweight unattended loop patterns
- observability and telemetry documentation
- orchestration economics patterns
- traceability workflow templates
- replay-safe ADR templates and examples
- compact context-engineering guidance

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

1. Read the extraction boundary in `governance/adr/ADR-0001-public-extraction-boundary.md`.
2. Pick one workflow slice from `examples/replay-safe-workflow.md`.
3. Add a small manifest and traceability scheme for your repository.
4. Define one validation lane that can run locally and fail closed.
5. Add adversary review before declaring the slice done.

DevOS should make engineering work easier to audit, not harder to understand.
