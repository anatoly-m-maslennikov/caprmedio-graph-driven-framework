---
atom_id: CA-R-1608
ref_id: CA-R-1608
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Status'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern)
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
tier: 2
status: Active
version: 21
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1608-CORE_META_MODEL-RULE--register-core-concern-status-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1608-CORE_META_MODEL-RULE--register-core-concern-status-values.md
  source_atom_id: CA-R-1608
  source_atom_revision: 21
  source_sha256: 2b24dda8e394f94c29429149d696dc5c94bfa53317015167bddfe4b5f80849a8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Core Concern Status Values

## Claim

### Prose Claim


the Core Concern Status model.


the Core Concern Status model **must** inherit the allowed values of Atom.Header.Status and add (Resolved, Canceled).
