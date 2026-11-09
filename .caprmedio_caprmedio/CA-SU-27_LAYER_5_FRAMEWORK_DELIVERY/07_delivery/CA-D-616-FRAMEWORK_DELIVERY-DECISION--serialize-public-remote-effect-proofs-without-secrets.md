---
atom_id: CA-D-616
ref_id: CA-D-616
container:
  scope_unit: CA-SU-27
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Serialization
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Carrier/Git Commit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 4
relations:
  delivery_for:
  - CA-R-1921
  - CA-R-1925
status: Active
version: 15
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-D-616-FRAMEWORK_DELIVERY-DECISION--serialize-public-remote-effect-proofs-without-secrets.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/07_delivery
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Serialize public remote effect proofs without secrets

## Scope

the remote proof of one public push.

## Claim

public remote effect evidence **must** retain the personal remote identity, branch direction, immutable commit identity, and repository-relative result/effect references without credentials, tokens, passwords, or arbitrary environment values.

## Details

An absent effect reference is not converted into a successful push claim.
