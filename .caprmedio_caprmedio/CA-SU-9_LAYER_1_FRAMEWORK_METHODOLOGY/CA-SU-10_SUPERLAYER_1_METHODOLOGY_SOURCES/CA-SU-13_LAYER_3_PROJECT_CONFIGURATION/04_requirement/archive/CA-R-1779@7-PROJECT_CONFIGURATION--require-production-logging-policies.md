---
atom_id: CA-R-1779@7
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Engineering/Logging Policy
  depends_on:
  - Subject/Engineering/Carrier
  - Evaluation Control
  - Subject/Engineering/Runtime/Journal Logging
  - 'Subject/Domain/Node/Continuant/Projection/Type: Catalog'
version: 7
updated_at: 2026-10-24 06:47:02 +0400
relations: {}
tier: 3
type: Rule
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
