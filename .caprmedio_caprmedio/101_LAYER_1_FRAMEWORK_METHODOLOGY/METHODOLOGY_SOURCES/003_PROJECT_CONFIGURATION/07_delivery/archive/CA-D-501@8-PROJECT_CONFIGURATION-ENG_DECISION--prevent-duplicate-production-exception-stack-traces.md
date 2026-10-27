---
atom_id: CA-D-501@8
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Carrier
  depends_on:
  - Subject/Graph Node/Engineering/Logging Policy
version: 8
updated_at: 2026-10-25 17:32:27 +0400
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
