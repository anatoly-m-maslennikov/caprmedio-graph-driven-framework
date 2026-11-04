---
atom_id: CA-R-2701
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.ID
version: 1
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2701-CORE_META_MODEL-DECLARATION--declare-atom-header-id.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2701-CORE_META_MODEL-DECLARATION--declare-atom-header-id.md
  source_atom_id: CA-R-2701
  source_atom_revision: 1
  source_sha256: 5d96f3e98a7d43efba676cd1fe027ca3f514e0e7fbb0be7fa536b5567a602d5e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Header.ID

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.ID{:1}: [string]{:1};

Atom.Header.ID.*[]{:0};

# instances
Atom//$atom;

IF (($atom.Header.Status >| Status Group = Current) OR ($atom.Header.Status >| Status Group = Archived))
THEN (IMMUTABLE($atom.Header.ID))
```
