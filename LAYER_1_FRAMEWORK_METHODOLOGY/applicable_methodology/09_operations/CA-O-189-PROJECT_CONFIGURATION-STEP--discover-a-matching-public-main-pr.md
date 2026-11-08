---
atom_id: CA-O-189
ref_id: CA-O-189
container:
  scope_unit: CA-SU-13
role: Operations
form: Step
topics:
  main_subject: 'Subject/caprmedio/Step//Public release/Step: discover matching main PR'
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
version: 8
updated_at: 2026-10-27 19:59:47 +0400
carrier_destination:
  file:
    name: CA-O-189-PROJECT_CONFIGURATION-STEP--discover-a-matching-public-main-pr.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
current_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-189-PROJECT_CONFIGURATION-STEP--discover-a-matching-public-main-pr.md
  source_atom_id: CA-O-189
  source_atom_revision: 8
  source_sha256: 1299128d64f0b819fe4042f43d9ed5a7729a98f300def0e9bf4d43e27a7a0847
  original_relations_sha256: afa15fce2aa6f2c148c2715f5a404bb9243ec264f7ffb3e6b8c6da0596a37b1c
---
# Summary

Discover a matching public `main` PR

## Step

This Step invokes CA-O-190 once before public-source freeze and records zero or one actual open Pull Request from `amm/dev` to `main` on the selected personal remote.

## Details

More than one match, a nonmatching base/head, an unsafe URL, or unavailable observation stops the Workflow. Discovery is read-only and does not infer a future URL.
