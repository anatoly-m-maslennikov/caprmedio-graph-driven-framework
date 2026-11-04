---
atom_id: CA-R-2698
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Relations.IS_CONTAINED_BY
version: 2
updated_at: 2026-11-04 07:31:50 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2698-CORE_META_MODEL-DECLARATION--declare-atom-header-relations-is-contained-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2698-CORE_META_MODEL-DECLARATION--declare-atom-header-relations-is-contained-by.md
  source_atom_id: CA-R-2698
  source_atom_revision: 2
  source_sha256: 669672c32d618a63cd81611b5daf3eef6ba090e30780f66f057b19a9c9d257bd
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Header.Relations.IS_CONTAINED_BY

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Relations.IS_CONTAINED_BY{:1}: []{:0};

Atom.Header.Relations.IS_CONTAINED_BY.*[in(atom,scope_unit)]{:1}
```
