---
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on: []
version: 13
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-R-1640
atom_id: CA-E-483@13
content_role: Evaluation
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 2
---
# Summary

Validate the routing tree

## Scope

the CAPRMEDIO Routing Tree.

## Claim

the Evaluation of the CAPRMEDIO Routing Tree registered under CA-R-1640-PROJECT_CONFIGURATION-RULE--register-one-canonical-routing-tree **must** reject a routing tree **when** **any** of the following is present:

## Details

- an invalid schema;
- an unknown target;
- ambiguous precedence;
- a duplicate route identity;
- an authority effect that is **not** explicitly declared.
