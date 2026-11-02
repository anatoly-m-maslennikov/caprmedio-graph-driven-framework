---
atom_id: CA-R-1784@10
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Aspect/Engineering/Execution Control/Failure Handling
  depends_on: []
version: 10
updated_at: 2026-10-29 07:45:30 +0400
relations: {}
tier: 3
type: Rule
---
## Summary

Protect primary operations from logging failure

## Claim scope

logging Implementation for production-relevant components.

## Claim

logging Implementation **must not** make the primary operation silently fail.

## Details

the boundary prevents a logging failure from silently becoming a primary-operation failure.
