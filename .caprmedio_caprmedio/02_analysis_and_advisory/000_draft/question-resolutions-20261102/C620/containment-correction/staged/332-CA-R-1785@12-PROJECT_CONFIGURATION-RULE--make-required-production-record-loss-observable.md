---
atom_id: CA-R-1785@12
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
subjects:
  active: Entity/Aspect/Engineering/Observability
  passive:
  - Entity/Aspect/Engineering/Observability/Logging
version: 12
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Make required production-record loss observable

## Claim scope

logging Implementation **when** required records are lost **or** suppressed under production Logging Policies.

## Claim

logging Implementation **must** produce an observable failure signal **when** required records are lost **or** suppressed.

## Details

the signal preserves a visible failure condition **when** required records cannot be retained **or** delivered.
