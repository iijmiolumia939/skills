# Governance Invariants

Governance invariants are simple rules that keep autonomous work auditable.

## Core Invariants

- Every non-trivial feature has a decision record.
- Every requirement has at least one verification path.
- Every implementation unit names the requirement or property it serves.
- Every validation lane fails closed.
- Every adversary failure is resolved or explicitly deferred with a decision record.
- Generated evidence is never reused as proof in a different repository.
- Public examples do not include private repository history.

## Anti-Slop Checks

Before declaring work complete, check for:

- vague claims without criteria
- hidden defaults
- weak truthy assertions
- silent failure
- scoring or routing that was not specified
- generated artifacts presented as reusable truth
- examples that depend on private context
