---
atom_id: CA-D-500
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier
  passive:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Observability <+ Logging
version: 15
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
tier: 3
role: Delivery
form: Decision
---
## Summary

Select material production log events

## Claim scope

production log emission under Logging Policies for production-relevant components.

## Claim

production logs record material state transitions **and** boundary outcomes; ordinary internal ticks do **not** define routine production log events.

## Details

the selection preserves material operational evidence **without** treating **every** internal tick as a production event.
