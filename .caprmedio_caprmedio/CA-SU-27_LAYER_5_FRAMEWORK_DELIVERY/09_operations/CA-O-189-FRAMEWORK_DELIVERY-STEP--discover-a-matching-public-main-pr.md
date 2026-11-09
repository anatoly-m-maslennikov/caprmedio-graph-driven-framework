---
atom_id: CA-O-189
ref_id: CA-O-189
container:
  scope_unit: CA-SU-27
role: Operations
form: Step
topics:
  main_subject: 'Subject/caprmedio/Step//Public release/Step: discover matching main
    PR'
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
relations:
  part_of:
  - CA-O-188
  invokes:
  - CA-O-190
status: Active
version: 9
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-O-189-FRAMEWORK_DELIVERY-STEP--discover-a-matching-public-main-pr.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/09_operations
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Discover a matching public `main` PR

## Step

This Step invokes CA-O-190 once before public-source freeze and records zero or one actual open Pull Request from `amm/dev` to `main` on the selected personal remote.

## Details

More than one match, a nonmatching base/head, an unsafe URL, or unavailable observation stops the Workflow. Discovery is read-only and does not infer a future URL.
