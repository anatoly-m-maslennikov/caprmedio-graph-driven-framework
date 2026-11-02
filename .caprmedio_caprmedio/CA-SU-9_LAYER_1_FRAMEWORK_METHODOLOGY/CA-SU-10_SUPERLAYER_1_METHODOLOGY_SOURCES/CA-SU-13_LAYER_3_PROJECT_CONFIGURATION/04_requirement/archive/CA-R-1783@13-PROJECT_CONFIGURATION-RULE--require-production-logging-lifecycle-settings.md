---
atom_id: CA-R-1783@13
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
subjects:
  active: Aspects <+ Engineering <+ Observability <+ Logging
  passive: []
version: 13
updated_at: 2026-11-02 18:35:20 +0400
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
