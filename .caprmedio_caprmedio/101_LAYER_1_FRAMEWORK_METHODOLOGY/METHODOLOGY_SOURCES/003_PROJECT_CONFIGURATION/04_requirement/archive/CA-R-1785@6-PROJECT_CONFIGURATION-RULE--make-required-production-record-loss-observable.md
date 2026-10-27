---
atom_id: CA-R-1785@6
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Engineering/Operational Diagnostics
  depends_on:
  - Subject/Engineering/Logging Policy
version: 6
updated_at: 2026-10-24 11:58:20 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Make required production-record loss observable

## Scope

logging Implementation **when** required records are lost **or** suppressed under production Logging Policies.

## Claim

logging Implementation **must** produce an observable failure signal **when** required records are lost **or** suppressed.

## Details

the signal preserves a visible failure condition **when** required records cannot be retained **or** delivered.
