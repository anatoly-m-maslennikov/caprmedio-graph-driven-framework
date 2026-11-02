---
subjects:
  governs: Entity/Carrier
  depends_on:
  - Entity/Aspect/Engineering/Observability/Logging
version: 20
updated_at: 2026-10-29 10:13:51 +0400
relations: {}
atom_id: CA-D-396@20
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
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
