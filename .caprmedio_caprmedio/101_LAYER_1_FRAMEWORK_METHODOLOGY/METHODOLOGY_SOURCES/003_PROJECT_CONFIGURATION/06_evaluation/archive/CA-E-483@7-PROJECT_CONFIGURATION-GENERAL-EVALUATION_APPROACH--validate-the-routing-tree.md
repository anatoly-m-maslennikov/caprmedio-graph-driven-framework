---
subjects:
  governs: CAPRMEDIO Routing Tree
  depends_on: []
version: 7
updated_at: 2026-10-22 16:18:21 +0000
relations:
  evaluation_for:
  - CA-R-1640
atom_id: CA-E-483@7
content_role: Evaluation
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: General
status: Archived
author: Anatoly Maslennikov
type: Policy
global_tier: 10
---
# Summary

Validate the routing tree

## Scope

the CAPRMEDIO Routing Tree.

## Claim

the Evaluation of the CAPRMEDIO Routing Tree registered under CA-R-1640-PROJECT_CONFIGURATION-CORE-REQUIREMENT--register-one-canonical-routing-tree **must** reject a routing tree **when** **any** of the following is present:

## Details

- an invalid schema;
- an unknown target;
- ambiguous precedence;
- a duplicate route identity;
- an authority effect that is **not** explicitly declared.
