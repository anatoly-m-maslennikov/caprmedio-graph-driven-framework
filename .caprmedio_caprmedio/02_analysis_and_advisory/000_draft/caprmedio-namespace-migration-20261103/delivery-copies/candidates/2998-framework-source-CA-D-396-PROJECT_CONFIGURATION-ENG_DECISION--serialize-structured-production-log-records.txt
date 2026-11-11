---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier
  passive:
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Observability <+ Logging
version: 23
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-D-396
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Structured Production Log Records

## Claim scope

structured production log records.

## Claim

**every** structured production log record **must** include, **where** applicable:

- UTC timestamp, severity, **and** a stable event name;
- component, environment, **and** deployed version;
- run, request, job, workflow, session, correlation, **or** trace identity;
- relevant domain entity identity **and** lifecycle state;
- outcome, duration, attempt number, **and** retry disposition;
- stable error code **and** exception class for failures; **and**
- a concise human-readable message with sanitized diagnostic context.
