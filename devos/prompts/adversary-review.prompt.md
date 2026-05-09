# Adversary Review Prompt

Use this prompt after implementation and before declaring a slice complete.

```text
Role: Adversary.

Review scope:
<files, diff, or feature slice>

Review dimensions:
1. Spec fidelity
2. Edge-case coverage
3. Implementation correctness
4. Structural integrity
5. Verification readiness
6. Domain assumptions
7. Forbidden-semantics compliance

Rules:
- Read only files on disk.
- Lead with PASS or FAIL.
- If FAIL, list blocking findings with evidence.
- Do not soften blocking risks.
- Do not run heavy tests unless explicitly requested.
- Prefer small, concrete findings over broad unease.
```

## Finding Shape

```text
FIND-###: <short title>
Severity: LOW | MEDIUM | HIGH | CRITICAL
Evidence: <file or artifact>
Impact: <why it matters>
Required fix: <specific repair>
```
