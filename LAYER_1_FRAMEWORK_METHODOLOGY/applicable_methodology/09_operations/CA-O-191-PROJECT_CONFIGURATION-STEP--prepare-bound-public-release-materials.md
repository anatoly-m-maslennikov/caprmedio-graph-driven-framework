---
atom_id: CA-O-191
ref_id: CA-O-191
container:
  scope_unit: CA-SU-13
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
version: 12
updated_at: 2026-10-27 19:59:47 +0400
carrier_destination:
  file:
    name: CA-O-191-PROJECT_CONFIGURATION-STEP--prepare-bound-public-release-materials.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
current_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-191-PROJECT_CONFIGURATION-STEP--prepare-bound-public-release-materials.md
  source_atom_id: CA-O-191
  source_atom_revision: 12
  source_sha256: 306794d2f844a1e68d2a5c3be19de89f5ab91be69c906ce33c89fe00650492d5
  original_relations_sha256: 56d4df112ff24ffa18942f29e6e03506a0d66e7a58931abef8ae2e5e4370860b
---
# Summary

Prepare bound public-release materials

## Step

This Step invokes CA-O-192 once for the sole public-release content prompt: the full PR description and concise selected-Version History summary.

## Details

README, Version History, Git, and PR updates are mechanical later steps. A newly created actual PR URL is appended only by CA-O-198; this Step does not guess a URL, publish, or merge.
