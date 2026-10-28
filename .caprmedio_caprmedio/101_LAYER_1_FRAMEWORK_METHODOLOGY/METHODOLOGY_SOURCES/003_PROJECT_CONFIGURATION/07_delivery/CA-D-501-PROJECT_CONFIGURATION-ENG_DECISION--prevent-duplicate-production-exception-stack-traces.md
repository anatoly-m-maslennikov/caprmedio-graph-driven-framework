---
atom_id: CA-D-501
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

Prevent duplicate production exception stack traces

## Scope

exceptions handled **or** escalated through production-relevant components’ Logging Policies.

## Claim

an exception is emitted once at the boundary responsible for handling **or** escalating it; lower layers preserve structured context **without** duplicating the same stack trace at **every** call boundary.

## Details

the exception boundary retains structured context for handling **or** escalation **without** repeating the same stack trace through lower layers.
