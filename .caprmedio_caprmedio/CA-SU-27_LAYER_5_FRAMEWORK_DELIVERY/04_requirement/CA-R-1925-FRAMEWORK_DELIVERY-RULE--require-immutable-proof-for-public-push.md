---
atom_id: CA-R-1925
ref_id: CA-R-1925
container:
  scope_unit: CA-SU-27
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Git Commit
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 15
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-R-1925-FRAMEWORK_DELIVERY-RULE--require-immutable-proof-for-public-push.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/04_requirement
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
relations: {}
---

# Summary

Require immutable proof for public push

## Scope

one public `amm/dev` push effect.

## Claim

**the Operator** **must** retain an immutable commit identity and remote effect reference for every public push of the selected public source/material bindings.

## Details

The proof is evidence on the parent Action Run. Failure, partial effect, or absent proof does not permit PR advancement or inferred success.
