---
atom_id: CA-R-2709
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Relations
version: 1
relations: {}
tier: 3
updated_at: 2026-11-03 20:00:05 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2709-CORE_META_MODEL-DECLARATION--declare-atom-header-relations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2709-CORE_META_MODEL-DECLARATION--declare-atom-header-relations.md
  source_atom_id: CA-R-2709
  source_atom_revision: 1
  source_sha256: 3f759fcf082e94dd20b07d243edd7daaf374e23a80033c4246ad2c01b3d1df17
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Header.Relations

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Relations{:1}: []{:0};

# instances
Atom.Header.Relations.*[Relation//$relation]{:0+}
```
