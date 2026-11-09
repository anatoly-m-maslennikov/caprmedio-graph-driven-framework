---
atom_id: CA-O-179
ref_id: CA-O-179
container:
  scope_unit: CA-SU-27
role: Operations
form: Step
topics:
  main_subject: 'Subject/caprmedio/Step//Release Version/Step: retire exact prior
    image'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-169
status: Active
version: 13
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-O-179-FRAMEWORK_DELIVERY-STEP--retire-the-exact-prior-image-after-promotion.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/09_operations
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Retire the exact prior image after promotion

## Step

When explicitly selected, this Step invokes CA-O-169's existing safe retirement phase for inspected selected-Project noncandidate images after verified replacement installation and MCP smoke. Normal Local release performs this work inside CA-O-178; this carrier is not an additional occurrence in CA-O-164's complete registered graph.

## Details

Retain the exact admitted image of the current package Version. Another digest, including a same-fingerprint rebuild, is eligible only under complete matching inspected Project/root/control ownership, positive runtime classification and absence of every container reference. Preserve foreign, unowned, incomplete, in-use or unverified resources and report pending work. No sealed rollback-retention condition, canonical Journal receipt, force, global prune or uncertain retry is required or permitted as an added mechanism. Record actual removal/retention and logging failures independently; no release completion is inferred from this definition or from a Journal entry alone.
