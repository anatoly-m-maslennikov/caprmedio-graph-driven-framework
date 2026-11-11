---
atom_id: CA-R-1788
ref_id: CA-R-1788
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Updated At
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
relations:
  child_of:
  - CA-R-1416
status: Active
version: 20
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-1788-CORE_META_MODEL-RULE--initialize-version-creation-timestamp.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
claim_target_scope_unit: CORE_META_MODEL
current_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1788-CORE_META_MODEL-RULE--initialize-version-creation-timestamp.md
  source_atom_id: CA-R-1788
  source_atom_revision: 20
  source_sha256: fa312a06c2ee056ee2de82070b3650a3375afc699848650cc8ae40b9caa1ae82
  original_relations_sha256: f928d2096b701aa0e7852bc6d06e4620a81315e585b6a1074e66973879d77cf5
---
## Summary

Initialize Version creation timestamp

## Claim

### Prose Claim

Initialize Updated At to the actual Project-time creation instant when a new Atom Version is created. In-place edits, Status-only changes, archival, and promotion preserve the existing Version's Updated At. An ancestor-only move also preserves a descendant's Updated At. Timestamp encoding follows CA-D-270.
