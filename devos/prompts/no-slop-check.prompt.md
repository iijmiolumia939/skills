# No-Slop Check Prompt

Use this prompt before commit or publication.

```text
Role: no-slop-check.

Scan the proposed change for:
- vague claims without measurable criteria
- hidden defaults
- weak assertions
- silent failure
- generated artifacts presented as reusable truth
- scoring, diagnosis, routing, or optimization not explicitly specified
- private or project-specific references
- examples that need external private context

Return PASS or FAIL. If FAIL, list blockers only.
```
