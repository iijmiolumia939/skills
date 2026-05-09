# Lightweight Unattended Loop Prompt

Use this prompt for one bounded autonomous engineering cycle.

```text
Run one unattended engineering cycle.

Objective:
<one concrete slice>

Constraints:
- update or create a requirement first
- add a failing test or check before implementation
- keep changes minimal
- run the focused validation lane
- run adversary review
- write a compact checkpoint or ADR
- stop on blocking failure

Do not weaken validation gates. Do not publish generated evidence as reusable truth. Do not continue beyond the cycle limit.
```

## Output

End with:

- files changed
- validation commands run
- adversary result
- open follow-up
- commit hash if committed
