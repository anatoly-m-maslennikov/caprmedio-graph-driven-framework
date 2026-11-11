---
atom_id: CA-O-195
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/caprmedio/Step//Public release/Step: push and upsert main PR'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery/Git Commits
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Carrier/Pull Request
version: 11
updated_at: 2026-10-27 19:59:47 +0400
relations:
  part_of:
  - CA-O-188
  invokes:
  - CA-O-196
tier: 3
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-195-PROJECT_CONFIGURATION-STEP--push-the-public-closure-and-upsert-main-pr.md
  source_atom_id: CA-O-195
  source_atom_revision: 11
  source_sha256: b1afc1d861e32952ee12f8cc50d67f2430ff1b72890b9a43f44e9f1a758d75cb
  original_relations_sha256: bec494665aab40a5f3d5356d8722502019e739f5ba2f0c7614c5aef62d572009
---
# Summary

Push the public closure and upsert `main` PR

## Step

This Step invokes CA-O-196 once after the content prompt to commit and push the prepared closure on `amm/dev`, then find its one matching open `main` PR or create it as Draft. An existing matching open PR is converted to Draft before its body is edited.

## Details

The Step records the pushed commit and actual Draft PR identity. It cannot merge, retarget, or silently retry an unknown push or PR effect.
