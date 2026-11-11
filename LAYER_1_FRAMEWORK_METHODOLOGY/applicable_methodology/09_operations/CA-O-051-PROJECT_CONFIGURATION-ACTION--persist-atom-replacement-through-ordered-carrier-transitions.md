---
atom_id: CA-O-051
ref_id: CA-O-051
container:
  scope_unit: CA-SU-13
role: Operations
form: Action
topics:
  main_subject: Subject/caprmedio/Action//Persist Atom Replacement
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Version Number
  - Subject/CAPRMEDIO/Carrier/File
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Carrier/File.Filename
tier: 3
relations:
  depends_on:
  - CA-R-807
status: Active
version: 21
updated_at: 2026-10-27 19:59:44 +0400
carrier_destination:
  file:
    name: CA-O-051-PROJECT_CONFIGURATION-ACTION--persist-atom-replacement-through-ordered-carrier-transitions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-051-PROJECT_CONFIGURATION-ACTION--persist-atom-replacement-through-ordered-carrier-transitions.md
  source_atom_id: CA-O-051
  source_atom_revision: 21
  source_sha256: 35888258b3cb3faae4cbbdfc12f723ca599c5decd9c9d6153b5abd53a40ee2c2
  original_relations_sha256: 67577f2516b11efabad843133bbc9a2bcd11b91623e7a492544579838c61aac8
---
# Summary

Persist Atom replacement through ordered Carrier transitions

## Operation

Persist an accepted Atom replacement by resolving every distinct `IS_REPLACEMENT_FOR` target, including targets with different IDs and many-to-one replacement. Before publishing the Draft as Current, archive each eligible Current target once and skip every target already Archived, including one archived by composed Update. Archival preserves each target's Version and Updated At. Then publish the Draft with the supplied allowed Current Status and remove its Draft carrier. A changed Summary or Content Role creates a new identity promoted at Version 1; otherwise retain the Draft Version without a further increment. Derive carrier filename and location from the model.

Record actual business observations in the Journal independently; recording failure does not block the lifecycle effect. Stop on an effect failure and report completed and incomplete effects without retry, rollback, recovery or repair.
