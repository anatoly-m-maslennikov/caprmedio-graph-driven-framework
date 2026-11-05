---
atom_id: CA-R-2565
ref_id: CA-R-2565
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2565-CORE_META_MODEL-RULE--preserve-atom-version-and-updated-at-when-archiving.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2565-CORE_META_MODEL-RULE--preserve-atom-version-and-updated-at-when-archiving.md
  source_atom_id: CA-R-2565
  source_atom_revision: 2
  source_sha256: d20a3d943c8ca88467d07dd5b5c373b391f86035537d4e51acda426e1899d1c7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Preserve Atom Version and Updated At When Archiving

## Claim

### Prose Claim


When a Workflow archives an Atom:

1. Keep Atom.Header.Version unchanged.
2. Keep Atom.Header.Updated At unchanged.
3. Do not create a new Atom Version solely for archiving.
