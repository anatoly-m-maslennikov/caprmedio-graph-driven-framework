---
atom_id: CA-R-1926
ref_id: CA-R-1926
container:
  scope_unit: CA-SU-27
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Pull Request.ID
  - Subject/CAPRMEDIO/Carrier/Git Branch
  - Subject/CAPRMEDIO/Carrier/Git Repository
tier: 3
status: Active
version: 13
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-R-1926-FRAMEWORK_DELIVERY-RULE--maintain-one-matching-open-main-pr.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/04_requirement
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
relations: {}
---

# Summary

Maintain one matching open `main` PR

## Scope

one public release Pull Request boundary.

## Claim

**the Operator** **must** discover, create, or update exactly one actual open PR from the selected `amm/dev` head to `main` on the selected personal remote.

## Details

Zero matches permits create after the actual initial push. More than one match, a changed existing identity, or an unsafe/nonmatching URL blocks the Workflow.
