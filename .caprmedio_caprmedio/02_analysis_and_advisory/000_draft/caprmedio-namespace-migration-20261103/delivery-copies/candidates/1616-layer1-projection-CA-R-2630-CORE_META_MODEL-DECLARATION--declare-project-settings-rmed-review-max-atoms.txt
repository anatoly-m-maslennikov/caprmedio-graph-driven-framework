---
atom_id: CA-R-2630
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings.RMED Review.Max Atoms
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2630-CORE_META_MODEL-DECLARATION--declare-project-settings-rmed-review-max-atoms.md
  source_atom_id: CA-R-2630
  source_atom_revision: 1
  source_sha256: 84a5e8f1fe5e36fcfa2a32f8690b63feea0cf97e6dfb7ba9a3bff98ad6748be5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project.Settings.RMED Review.Max Atoms

## Claim

When present, the value is positive. Its absence supplies no default.

```CFEL
Project.Settings.RMED Review.Max Atoms{:0..1}: [int]{:1};
Project.Settings.RMED Review.Max Atoms.*[]{:0}
```
