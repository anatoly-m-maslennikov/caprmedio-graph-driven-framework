---
atom_id: CA-R-1785
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Observability
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Observability/Logging
version: 9
updated_at: 2026-10-27 20:00:03 +0400
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
