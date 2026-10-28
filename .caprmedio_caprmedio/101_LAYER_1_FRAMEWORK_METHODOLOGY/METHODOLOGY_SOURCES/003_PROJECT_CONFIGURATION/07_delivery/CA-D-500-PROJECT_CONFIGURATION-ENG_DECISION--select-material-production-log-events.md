---
atom_id: CA-D-500
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Carrier
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Observability/Logging
version: 10
updated_at: 2026-10-27 19:59:26 +0400
relations: {}
tier: 3
type: Eng Decision
---
# Summary

Select material production log events

## Scope

production log emission under Logging Policies for production-relevant components.

## Claim

production logs record material state transitions **and** boundary outcomes; ordinary internal ticks do **not** define routine production log events.

## Details

the selection preserves material operational evidence **without** treating **every** internal tick as a production event.
