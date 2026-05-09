# Deterministic Observability

DevOS observability makes an engineering run easier to inspect later. It records deterministic facts about files, commands, gates, and evidence links.

It is audit-oriented, not dashboard-oriented.

## What It Is

- deterministic
- replay-safe
- provenance-safe
- audit-oriented
- based on local artifacts and explicit source paths

## What It Is Not

- an AI monitoring dashboard
- hidden scoring
- heuristic diagnostics
- autonomous interpretation
- root-cause analysis
- file ranking or optimization advice

## Core Rule

Observe facts. Preserve source paths. Declare unavailable channels. Record non-claims. Do not score, rank, diagnose, route, or optimize unless a requirement and validation path explicitly allow it.

## Four Things To Observe

```text
Replay churn        What artifacts changed?
Orchestration       What commands ran and how did they end?
Gate instability    Did a gate refuse an unsupported claim?
Provenance flow     Which source directly produced which artifact?
```

## Replay Churn Visibility

Replay churn visibility shows which artifacts changed during replay. A safe public pattern records inventory only:

```text
source snapshot --> comparison snapshot --> changed / unchanged inventory
						   |
						   v
					   explicit non-claims
```

- artifact path
- artifact kind
- changed or unchanged state
- source comparison boundary
- non-claims that exclude ranking, blame, and optimization

Do not publish churn rates, instability scores, or optimization recommendations unless they have their own specification and proof path.

## Orchestration Telemetry

Orchestration telemetry records bounded execution facts such as command count, return code, output byte count, and compact output tail. It should also record unavailable channels rather than inventing them.

```text
command label -> return code -> output size/hash/tail
						 |
						 v
			  unavailable channels named explicitly
```

Useful facts include:

- command label
- return code
- output byte count
- compact output tail
- unavailable channels

## Gate Instability Observability

A safe gate-instability pattern is refusal-first. Treat `gate_instability_*` requests as a namespace to refuse until there is explicit evidence. Refusal records should state that evidence class presence alone does not unblock measurement, scoring, routing, or diagnosis.

```text
request for instability claim
			 |
			 v
 evidence contract exists? -- no --> refuse and record why
			 |
			yes
			 v
 run only the specified check
```

The refusal is useful evidence. It prevents fake certainty.

## Provenance-Flow Observability

A safe provenance-flow pattern records direct edges only. It does not compute traversal, reachability, centrality, influence, critical paths, routing, or root cause.

```text
source file ----directly produced----> evidence artifact

No transitive closure.
No reachability graph.
No root-cause path.
```

Direct edges are enough to answer: "Where did this artifact come from?"

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

## Tiny Example

See [../examples/tiny-todo-validator/docs/observability-run.json](../examples/tiny-todo-validator/docs/observability-run.json) for a static public-safe example.

That artifact records expected command outcomes, replay-churn inventory, unavailable telemetry channels, a gate-instability non-measurement, and direct provenance edges. It does not infer quality, blame, cause, priority, or confidence.
