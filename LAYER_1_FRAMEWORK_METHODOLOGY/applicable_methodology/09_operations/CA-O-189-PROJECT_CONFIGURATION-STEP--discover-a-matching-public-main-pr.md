---
atom_id: CA-O-189
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/caprmedio/Step//Public release/Step: discover matching main PR'
  depends_on:
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Carrier/Git Repository
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 8
updated_at: 2026-10-27 19:59:47 +0400
relations:
  part_of:
  - CA-O-188
  invokes:
  - CA-O-190
tier: 3
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-189-PROJECT_CONFIGURATION-STEP--discover-a-matching-public-main-pr.md
  source_atom_id: CA-O-189
  source_atom_revision: 8
  source_sha256: efda22a534c8b9d32301df7025b04a7007f097d70516155886018f8d3e4b5624
  original_relations_sha256: afa15fce2aa6f2c148c2715f5a404bb9243ec264f7ffb3e6b8c6da0596a37b1c
---
# Summary

Discover a matching public `main` PR

## Step

This Step invokes CA-O-190 once before public-source freeze and records zero or one actual open Pull Request from `amm/dev` to `main` on the selected personal remote.

## Details

More than one match, a nonmatching base/head, an unsafe URL, or unavailable observation stops the Workflow. Discovery is read-only and does not infer a future URL.
