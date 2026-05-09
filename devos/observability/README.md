# Deterministic Observability

DevOS observability is about making autonomous engineering state visible without turning observations into unsupported decisions.

## Philosophy

Observe facts. Preserve source paths. Declare unavailable channels. Record non-claims. Do not score, rank, diagnose, route, or optimize unless a requirement and validation path explicitly allow it.

## Replay Churn Visibility

Replay churn visibility shows which artifacts changed during replay. A safe public pattern records inventory only:

- artifact path
- artifact kind
- changed or unchanged state
- source comparison boundary
- non-claims that exclude ranking, blame, and optimization

Do not publish churn rates, instability scores, or optimization recommendations unless they have their own specification and proof path.

## Orchestration Telemetry

Orchestration telemetry records bounded execution facts such as command count, return code, output byte count, and compact output tail. It should also record unavailable channels rather than inventing them.

## Gate Instability Observability

A safe gate-instability pattern is refusal-first. Treat `gate_instability_*` requests as a namespace to refuse until there is explicit evidence. Refusal records should state that evidence class presence alone does not unblock measurement, scoring, routing, or diagnosis.

## Provenance-Flow Observability

A safe provenance-flow pattern records direct edges only. It does not compute traversal, reachability, centrality, influence, critical paths, routing, or root cause.

## Minimal Artifact Shape

A deterministic observability artifact usually includes:

- schema version
- kind
- source paths
- causal claim
- scope
- semantics
- observed facts
- unavailable channels
- non-claims
- excluded semantics
