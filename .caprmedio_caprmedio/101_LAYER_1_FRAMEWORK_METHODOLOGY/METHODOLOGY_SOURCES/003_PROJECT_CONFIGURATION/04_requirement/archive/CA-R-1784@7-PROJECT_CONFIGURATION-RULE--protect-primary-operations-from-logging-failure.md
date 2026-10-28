---
atom_id: CA-R-1784@7
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control/Failure Handling
  depends_on: []
version: 7
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Protect primary operations from logging failure

## Scope

logging Implementation for production-relevant components.

## Claim

logging Implementation **must not** make the primary operation silently fail.

## Details

the boundary prevents a logging failure from silently becoming a primary-operation failure.
