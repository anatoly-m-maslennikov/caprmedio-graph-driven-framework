---
subjects:
  governs: Subject/CAPRMEDIO/Carrier
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Observability/Logging
version: 17
updated_at: 2026-10-27 19:59:24 +0400
relations: {}
atom_id: CA-D-396
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Structured Production Log Records

## Scope

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

## Details
