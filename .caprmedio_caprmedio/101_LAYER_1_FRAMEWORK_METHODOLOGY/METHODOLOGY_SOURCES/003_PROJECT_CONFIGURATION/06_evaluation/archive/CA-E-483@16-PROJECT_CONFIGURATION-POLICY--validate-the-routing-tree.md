---
subjects:
  governs: Entity/Aspect/Engineering/Architecture/Communication
  depends_on: []
version: 16
updated_at: 2026-10-29 07:45:31 +0400
relations:
  evaluation_for:
  - CA-R-1640
atom_id: CA-E-483@16
content_role: Evaluation
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 2
---
## Summary

Validate the routing tree

## Claim scope

the CAPRMEDIO Routing Tree.

## Claim

the Evaluation of the CAPRMEDIO Routing Tree registered under CA-R-1640-PROJECT_CONFIGURATION-RULE--register-one-canonical-routing-tree **must** reject a routing tree **when** **any** of the following is present:

## Details

- an invalid schema;
- an unknown target;
- ambiguous precedence;
- a duplicate route identity;
- an authority effect that is **not** explicitly declared.
