---
atom_id: CA-R-2630
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.RMED Review.Max Atoms
version: 2
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-04 05:21:15 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2630-CORE_META_MODEL-DECLARATION--declare-project-settings-rmed-review-max-atoms.md
  source_atom_id: CA-R-2630
  source_atom_revision: 2
  source_sha256: 2d07824c87546c00b1937f300a176d503b26700db0ccfdee3891ce6896efc70a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project.Settings.RMED Review.Max Atoms

## Claim

### Formal Claim

```CFEL
# model
Project.Settings.RMED Review.Max Atoms: [int]{:0..1};

Project.Settings.RMED Review.Max Atoms.*[]{:0}
```

### Prose Claim


When present, the value is positive. Its absence supplies no default.

