# ADR-0001: Public DevOS Extraction Boundary

Status: Accepted
Date: 2026-05-09

## Context

The goal is to publish a reusable autonomous-engineering substrate for general AI-assisted software projects. The extraction must be public-safe, project-agnostic, small, and understandable without private repository history.

The extraction is not a migration of a full engineering repository. It is a curated teaching and template package.

## Decision

Include reusable public-safe substrate patterns as docs, prompts, templates, and generic examples. Exclude implementation history, domain-specific artifacts, generated evidence churn, unstable experiments, private defect history, and anything that requires private context to understand.

## Included Categories

- deterministic replay patterns
- manifest-memory infrastructure patterns
- replay-safe validation patterns
- governance invariant patterns
- adversary review workflow patterns
- lightweight unattended harness patterns
- observability and telemetry patterns
- orchestration economics patterns
- traceability workflow patterns
- replay-safe ADR workflow templates
- compact context-engineering utilities described as patterns
- generic reusable prompts and templates
- public-safe diagrams and examples

## Excluded Categories

- domain-specific logic or examples
- research-only workflows
- private defect or issue history
- large proof archives
- generated checkpoint churn
- experimental cognition prototypes
- project-specific provenance chains
- scripts with hard-coded private repository assumptions
- historical decision chains that are not needed for adoption

## Replay-Safety Rationale

A public package should be replay-safe by construction: readers should be able to reconstruct the intended workflow from stable docs and templates. Generated artifacts, private history, and copied validation outputs are excluded because they become stale immediately and can misrepresent the target repository's actual state.

## Anti-Slop Rationale

The package favors explicit constraints over impressive-looking architecture. Every template should name what it does not claim. Examples must avoid scoring, hidden defaults, silent downgrade, and vague success claims. If a template cannot explain how it fails closed, it is not ready for publication.

## Observability Rationale

The observability guidance is included because autonomous engineering needs visible operational state. The package documents deterministic observability for replay churn visibility, orchestration telemetry, gate instability refusal, provenance-flow visibility, and bounded execution economics without dashboards, rankings, hidden inference, or automatic routing.

## Consequences

- The package is small and readable.
- Users implement their own repository-specific gates.
- Examples are generic and non-authoritative.
- Future utilities may be added only after import and coupling audits.
