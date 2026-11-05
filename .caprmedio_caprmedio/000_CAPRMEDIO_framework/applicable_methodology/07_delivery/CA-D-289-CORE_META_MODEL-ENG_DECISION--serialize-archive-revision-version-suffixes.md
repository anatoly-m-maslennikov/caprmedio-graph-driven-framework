---
atom_id: CA-D-289
ref_id: CA-D-289
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Version
tier: 3
status: Active
version: 25
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-289-CORE_META_MODEL-DECISION--serialize-archive-revision-version-suffixes.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-289-CORE_META_MODEL-ENG_DECISION--serialize-archive-revision-version-suffixes.md
  source_atom_id: CA-D-289
  source_atom_revision: 25
  source_sha256: 3c30f981df672317aeece5f8879ab534f3f8a1102b07a1817a90a8018d1b7095
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Archive Revision Version Suffixes

## Claim

### Prose Claim


Archive Carrier basenames for Archived Atom versions.


**every** Archived Atom Carrier basename **must** serialize the archived Atom's canonical ID with exactly one `@<version>` marker, where `<version>` is the unchanged numeric Version Number of that Archived Atom version. The marker **must** occur in the filename's Atom-ID segment under CA-D-283; do **not** append a second `@<version>` to a basename that already carries the marker. Existing legacy archive basenames are not normalized automatically.
