---
atom_id: CA-R-1779
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Observability/Logging
  depends_on:
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Catalog'
version: 12
updated_at: 2026-10-27 20:00:03 +0400
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
