---
atom_id: CA-R-1658
ref_id: CA-R-1658
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
tier: 1
status: Active
version: 32
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1658-CORE_META_MODEL-RULE--prohibit-skipped-scope-unit-ownership.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1658-CORE_META_MODEL-RULE--prohibit-skipped-scope-unit-ownership.md
  source_atom_id: CA-R-1658
  source_atom_revision: 32
  source_sha256: 7f7b22649b31ce48a324218b3a754dcfeb6c599c81347656e8d23cec8efa6787
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Prohibit skipped Scope Unit ownership

## Claim

### Prose Claim


Scope Unit ownership through a stored structural-parent relation.


a Scope Unit **must not** own a descendant Scope Unit through a stored structural-parent relation **when** another active Scope Unit lies between them.
