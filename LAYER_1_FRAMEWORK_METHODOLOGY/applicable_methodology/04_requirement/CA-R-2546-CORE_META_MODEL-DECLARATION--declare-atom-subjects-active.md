---
atom_id: CA-R-2546
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom.Subjects.Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2546-CORE_META_MODEL-DECLARATION--declare-atom-subjects-active.md
  source_atom_id: CA-R-2546
  source_atom_revision: 2
  source_sha256: 0bfe5c05b570fd531fcf0f1d9f7e980166a4d3cac89a69cf7ced62ea5d9e2da6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Subjects.Active

## Claim

```CFEL
Atom.Subjects.Active{:0..1}: [string]{:1};
Atom.Subjects.Active.*[]{:0};
IF (Atom.Status >| Status Group = Current)
THEN (Atom.Subjects.Active{==1})
```
