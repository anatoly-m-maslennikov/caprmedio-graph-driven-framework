---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Scope Unit
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-395
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-395-CORE_META_MODEL-ENG_DECISION--serialize-ambient-project-scope-paths.md
  source_atom_id: CA-D-395
  source_atom_revision: 24
  source_sha256: 5acdef2bb33f053ca5280cf5d79ce11db699fad677bcadb5f02aada504d11e1c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Ambient Project Scope Paths

## Claim

### Prose Claim


the `scope_path` encoding of a Carrier.


a Carrier encoding of `scope_path` **must** omit the ambient current Project **and** use an empty path for Project Scope.
