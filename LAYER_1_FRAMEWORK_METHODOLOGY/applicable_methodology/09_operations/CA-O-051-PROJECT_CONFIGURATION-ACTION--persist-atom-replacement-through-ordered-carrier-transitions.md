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
  source_sha256: e987ee7284fab6a9e3270c434fb6b14f6915185479566e50af266c0e1bc30b29
  original_relations_sha256: 67577f2516b11efabad843133bbc9a2bcd11b91623e7a492544579838c61aac8
---
# Summary

Persist Atom replacement through ordered Carrier transitions

## Operation

Persist Atom Replacement **means** the reusable Action that persists **`=1`** accepted Atom replacement through its successor activation **and** predecessor archival under CA-R-1432 **and** CA-R-807. its boundary is this replacement transition; it does **not** select **or** authorize the replacement. the execution **must** perform **all** of:

1. persist the successor as Active **before** archiving the predecessor.
2. archive the predecessor as one whole Carrier under CA-D-303 **and** record the corresponding replacement **in** the authoritative Journal with explicit predecessor **and** successor Atom IDs under CA-R-807.
3. retain the predecessor's exact prior Revision bytes as history, including its prior Version, Status **and** Updated At, **without** another metadata edit to them. materialize the predecessor's Archived representation with its prior Version and Updated At, version-qualified identity and governed history location; archival alone does not increment Version or refresh Updated At. the Active successor receives Version **`N+1`** and the actual Project-time Updated At for the real replacement update. change its basename **only** by adding the canonical `@<version>` Archive suffix for that predecessor Version under CA-D-289.
4. keep replacement history out of predecessor **and** successor Atom frontmatter; formal replacement relations **and** inverse navigation remain deferred under CA-R-807.

## Details
