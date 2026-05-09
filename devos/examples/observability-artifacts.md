# Example: Deterministic Observability Artifacts

This example describes artifact shapes, not executable code. Use these shapes to record facts, not interpretations.

```text
facts in local files -> deterministic artifact -> human review

No dashboard.
No hidden scoring.
No heuristic diagnosis.
```

## Replay Churn Inventory

Purpose: show what changed during replay without ranking or diagnosis.

Fields:

- schema_version
- kind
- source_snapshot
- comparison_snapshot
- artifact_records
- non_claims
- excluded_semantics

Non-claims:

- no churn score
- no instability ranking
- no optimization recommendation
- no root-cause attribution

## Orchestration Telemetry

Purpose: record bounded execution facts.

Fields:

- command_label
- return_code
- output_bytes
- output_hash
- output_tail
- unavailable_channels

Unavailable channels should be named explicitly rather than inferred.

## Gate Instability Refusal

Purpose: refuse `gate_instability_*` requests until a separate evidence contract exists.

Fields:

- rejected_request
- status: refused_pending_evidence
- current_action: fail_closed
- unblocking_non_claims

## Provenance-Flow Direct Edges

Purpose: record direct source-to-artifact edges only.

Fields:

- source_node_id
- target_node_id
- edge_semantics: direct_artifact_production_not_transitive_flow

Excluded semantics:

- no transitive closure
- no reachability
- no centrality
- no routing
- no diagnosis
- no optimization
