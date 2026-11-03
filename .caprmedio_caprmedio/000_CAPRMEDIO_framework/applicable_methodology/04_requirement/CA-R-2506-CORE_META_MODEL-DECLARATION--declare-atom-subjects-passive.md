---
atom_id: CA-R-2506
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom.Subjects.Passive
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2506-CORE_META_MODEL-DECLARATION--declare-atom-subjects-passive.md
  source_atom_id: CA-R-2506
  source_atom_revision: 2
  source_sha256: d079df9afe660fa695b466b69db67e43a88207217b20994810fefe829117dccc
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Subjects.Passive

## Claim

Passive Subjects identify direct contextual dependencies.

```CFEL
Atom.Subjects.Passive{:0..1}: [string]{:0+};
Atom.Subjects.Passive.*[]{:0};
COUNT(Atom.Subjects.Passive: $) = COUNT(DISTINCT Atom.Subjects.Passive: $)
```
