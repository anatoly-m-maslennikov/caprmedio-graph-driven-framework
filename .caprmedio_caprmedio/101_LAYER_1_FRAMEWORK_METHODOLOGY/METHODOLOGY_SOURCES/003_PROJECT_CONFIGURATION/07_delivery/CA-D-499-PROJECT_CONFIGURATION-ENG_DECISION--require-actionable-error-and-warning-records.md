---
atom_id: CA-D-499
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Carrier
  depends_on: []
version: 8
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
tier: 3
type: Eng Decision
---
# Summary

Require actionable ERROR and WARNING records

## Scope

ERROR **and** WARNING production log records.

## Claim

an `ERROR` **or** `WARNING` record **must** be actionable: it identifies the failed **or** degraded condition, affected scope, expected operator **or** automated response, **and** whether retry is safe.

## Details

the required context makes the response **and** retry disposition explicit for the failed **or** degraded condition.
