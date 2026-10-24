---
atom_id: CA-R-1783
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Logging Policy
  depends_on: []
version: 3
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Require production logging lifecycle settings

## Scope

production Logging Policies **and** their retention, access, sampling, rotation, maximum size, back-pressure, unavailable-sink, **and** disk-pressure conditions.

## Claim

a production Logging Policy **must** define retention, access, sampling, rotation, maximum size, back-pressure, unavailable-sink behavior, **and** disk-pressure behavior.

## Details

these settings define the policy’s retention **and** delivery controls.
