---
atom_id: CA-R-1783
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: Entity/Aspect/Engineering/Observability/Logging
  passive: []
version: 11
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Require production logging lifecycle settings

## Claim scope

production Logging Policies **and** their retention, access, sampling, rotation, maximum size, back-pressure, unavailable-sink, **and** disk-pressure conditions.

## Claim

a production Logging Policy **must** define retention, access, sampling, rotation, maximum size, back-pressure, unavailable-sink behavior, **and** disk-pressure behavior.

## Details

these settings define the policy’s retention **and** delivery controls.
