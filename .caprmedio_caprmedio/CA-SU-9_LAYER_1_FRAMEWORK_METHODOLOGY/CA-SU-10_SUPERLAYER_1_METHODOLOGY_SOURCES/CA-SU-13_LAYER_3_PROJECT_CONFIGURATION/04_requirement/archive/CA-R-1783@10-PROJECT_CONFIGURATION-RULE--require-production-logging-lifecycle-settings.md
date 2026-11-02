---
atom_id: CA-R-1783@10
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Aspect/Engineering/Observability/Logging
  depends_on: []
version: 10
updated_at: 2026-10-29 07:45:30 +0400
relations: {}
tier: 3
type: Rule
---
## Summary

Require production logging lifecycle settings

## Claim scope

production Logging Policies **and** their retention, access, sampling, rotation, maximum size, back-pressure, unavailable-sink, **and** disk-pressure conditions.

## Claim

a production Logging Policy **must** define retention, access, sampling, rotation, maximum size, back-pressure, unavailable-sink behavior, **and** disk-pressure behavior.

## Details

these settings define the policy’s retention **and** delivery controls.
