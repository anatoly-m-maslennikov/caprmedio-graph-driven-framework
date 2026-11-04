---
atom_id: CA-R-2710
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Priority
version: 1
relations: {}
tier: 3
updated_at: 2026-11-03 20:00:05 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2710-CORE_META_MODEL-DECLARATION--declare-atom-header-role-concern-header-priority.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2710-CORE_META_MODEL-DECLARATION--declare-atom-header-role-concern-header-priority.md
  source_atom_id: CA-R-2710
  source_atom_revision: 1
  source_sha256: 7408a54ca2c03ab3aaa592b93440faac0f1976d3cfa4bab352808a8b3bdc5c04
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom/(.Header.Role := Concern).Header.Priority

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Concern).Header.Priority{:1}: [string]{:1};

Atom/(.Header.Role: Concern).Header.Priority.*[]{:0};

Atom/(.Header.Role: Concern).Header.Priority: High;

Atom/(.Header.Role: Concern).Header.Priority: Medium;

Atom/(.Header.Role: Concern).Header.Priority: Low
```
