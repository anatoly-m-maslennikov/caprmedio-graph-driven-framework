---
atom_id: CA-O-195
ref_id: CA-O-195
container:
  scope_unit: CA-SU-27
role: Operations
form: Step
topics:
  main_subject: 'Subject/caprmedio/Step//Public release/Step: push and upsert main
    PR'
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery/Git Commits
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Carrier/Pull Request
tier: 3
relations:
  part_of:
  - CA-O-188
  invokes:
  - CA-O-196
status: Active
version: 12
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-O-195-FRAMEWORK_DELIVERY-STEP--push-the-public-closure-and-upsert-main-pr.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/09_operations
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Push the public closure and upsert `main` PR

## Step

This Step invokes CA-O-196 once after the content prompt to commit and push the prepared closure on `amm/dev`, then find its one matching open `main` PR or create it as Draft. An existing matching open PR is converted to Draft before its body is edited.

## Details

The Step records the pushed commit and actual Draft PR identity. It cannot merge, retarget, or silently retry an unknown push or PR effect.
