---
atom_id: CA-O-191
ref_id: CA-O-191
container:
  scope_unit: CA-SU-27
role: Operations
form: Step
topics:
  main_subject: 'Subject/caprmedio/Step//Public release/Step: prepare materials'
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Documentation
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Release.ID
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
relations:
  part_of:
  - CA-O-188
  invokes:
  - CA-O-192
status: Active
version: 13
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-O-191-FRAMEWORK_DELIVERY-STEP--prepare-bound-public-release-materials.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/09_operations
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Prepare bound public-release materials

## Step

This Step invokes CA-O-192 once for the sole public-release content prompt: the full PR description and concise selected-Version History summary.

## Details

README, Version History, Git, and PR updates are mechanical later steps. A newly created actual PR URL is appended only by CA-O-198; this Step does not guess a URL, publish, or merge.
