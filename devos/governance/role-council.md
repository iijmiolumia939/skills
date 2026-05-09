# Role Council Protocol

Use a role council when a non-trivial decision would otherwise be sent back to the user for confirmation.

## Roles

- Architect: scope, direction, boundaries, ADRs.
- Spec Builder: measurable requirements and non-goals.
- Adversary: failure modes, leakage, slop, missing tests.
- Verifier: deterministic validation and evidence chain.
- Research Librarian: source separation and unsupported claims.

## Procedure

1. Frame the decision and options.
2. Ask each role for an independent verdict.
3. Require each verdict to include risk, blockers, impacted IDs, and rationale.
4. Synthesize using a fixed tie-break order.
5. Record the decision as an ADR.
6. Proceed without asking for preference unless all roles reject or a real external authorization is required.

## Tie-Break Order

Verifier, then Adversary, then Architect, then Spec Builder, then Research Librarian.

Verification correctness wins over a convenient implementation path.
