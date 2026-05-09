# Orchestration Economics

Orchestration economics makes the cost of autonomous work visible without pretending to know unavailable costs.

## What To Record

- number of commands or checks run
- return codes
- output size
- bounded output tail
- elapsed time only when measured by the local harness
- unavailable channels as explicit unavailable fields

## What Not To Infer

Do not infer total model tokens, weekly quota, monetary cost, productivity, risk, or quality from partial telemetry. If a channel is unavailable, say so.

## Compact Evidence

Long logs are not portable evidence. Prefer compact records with:

- command label
- return code
- output hash
- bounded tail
- timestamp if locally generated
- validation lane name

Compact evidence should help a reviewer decide what to rerun, not replace rerunning.
