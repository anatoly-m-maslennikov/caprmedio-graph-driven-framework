---
atom_id: CA-R-2493
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom.ID
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2493-CORE_META_MODEL-DECLARATION--declare-atom-id.md
  source_atom_id: CA-R-2493
  source_atom_revision: 2
  source_sha256: fb5e63d1f8a318206e8e885df3ff21aa891e1988124b13e91be23ee75b2640a3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.ID

## Claim

```CFEL
Atom.ID{:1}: [string]{:1};
Atom.ID.*[]{:0};
IF ((Atom.Status >| Status Group = Current) OR (Atom.Status >| Status Group = Archived))
THEN (IMMUTABLE(Atom.ID))
```
