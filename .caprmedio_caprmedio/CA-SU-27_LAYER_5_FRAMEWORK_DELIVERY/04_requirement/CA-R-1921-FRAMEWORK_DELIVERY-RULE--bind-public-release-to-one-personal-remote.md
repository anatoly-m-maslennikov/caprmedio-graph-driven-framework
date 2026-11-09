---
atom_id: CA-R-1921
ref_id: CA-R-1921
container:
  scope_unit: CA-SU-27
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Carrier/Git Branch
tier: 3
status: Active
version: 14
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-R-1921-FRAMEWORK_DELIVERY-RULE--bind-public-release-to-one-personal-remote.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/04_requirement
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
relations: {}
---

# Summary

Bind public release to one personal remote

## Scope

the selected remote boundary of one public release.

## Claim

**the Operator** **must** bind one public-release invocation to an explicit personal remote identity and the exact `amm/dev` to `main` branch direction.

## Details

The binding contains no credential or secret. A different remote, owner, head, base, or branch direction is out of scope and stops the invocation.
