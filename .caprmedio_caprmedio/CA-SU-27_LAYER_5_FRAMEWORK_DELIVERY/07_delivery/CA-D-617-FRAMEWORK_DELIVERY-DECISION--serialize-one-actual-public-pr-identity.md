---
atom_id: CA-D-617
ref_id: CA-D-617
container:
  scope_unit: CA-SU-27
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Pull Request.ID
  - Subject/CAPRMEDIO/Carrier/Git Branch
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
tier: 4
relations:
  delivery_for:
  - CA-R-1926
  - CA-R-1927
status: Active
version: 14
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-D-617-FRAMEWORK_DELIVERY-DECISION--serialize-one-actual-public-pr-identity.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/07_delivery
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Serialize one actual public PR identity

## Scope

the PR result of one public-release remote action.

## Claim

public PR evidence **must** retain one actual HTTPS PR URL, positive PR number, open Draft state, `amm/dev` head, `main` base, and repository-relative Tool-call result reference.

## Details

This representation records PR maintenance only. A created PR is Draft, and an existing open PR is converted to Draft before its body is edited. It contains no merge effect, merge receipt, or target-branch adoption claim.
