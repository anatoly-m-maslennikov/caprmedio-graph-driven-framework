---
atom_id: CA-R-1784@5
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Engineering/Operation-Local Failure Containment
  depends_on: []
version: 5
updated_at: 2026-10-24 11:58:20 +0400
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
