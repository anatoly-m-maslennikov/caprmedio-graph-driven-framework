---
atom_id: CA-D-396
ref_id: CA-D-396
container:
  scope_unit: CA-SU-13
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Observability <+ Logging
tier: 3
status: Active
version: 23
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-D-396-PROJECT_CONFIGURATION-DECISION--serialize-structured-production-log-records.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Serialize Structured Production Log Records

## Claim

### Prose Claim


structured production log records.


**every** structured production log record **must** include, **where** applicable:

- UTC timestamp, severity, **and** a stable event name;
- component, environment, **and** deployed version;
- run, request, job, workflow, session, correlation, **or** trace identity;
- relevant domain entity identity **and** lifecycle state;
- outcome, duration, attempt number, **and** retry disposition;
- stable error code **and** exception class for failures; **and**
- a concise human-readable message with sanitized diagnostic context.
