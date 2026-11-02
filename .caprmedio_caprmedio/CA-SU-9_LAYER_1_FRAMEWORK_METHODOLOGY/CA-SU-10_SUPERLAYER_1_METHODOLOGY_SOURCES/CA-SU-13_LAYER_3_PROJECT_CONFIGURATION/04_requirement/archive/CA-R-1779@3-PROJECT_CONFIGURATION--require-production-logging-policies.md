---
atom_id: CA-R-1779@3
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Logging Policy
  depends_on:
  - Subject/Engineering/Carrier
  - Evaluation Control
  - Implementation
  - 'Projection/Type: Catalog'
version: 3
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
---
# Summary

Require production Logging Policies

## Scope

production-relevant components **and** their Logging Policies.

## Claim

**every** production-relevant component **must** define a Logging Policy. that policy:

- governs required log coverage, structure, severity, safety, **and** retention **before** failures occur;
- supports its Evaluation Controls;
- is referenced by the Catalog Projection over its applicable Evaluation Control Atoms; **and**
- identifies the events **and** context required **to** understand normal operation, detect failure, correlate distributed work, **and** investigate real production issues.

## Details

the policy describes the evaluation boundary, while logger Implementation **and** emitted record Carriers realize it.
