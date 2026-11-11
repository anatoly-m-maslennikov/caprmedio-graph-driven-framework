---
atom_id: CA-R-2630
ref_id: CA-R-2630
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.RMED Review.Max Atoms
tier: 3
status: Active
version: 2
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2630-CORE_META_MODEL-DECLARATION--declare-project-settings-rmed-review-max-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2630-CORE_META_MODEL-DECLARATION--declare-project-settings-rmed-review-max-atoms.md
  source_atom_id: CA-R-2630
  source_atom_revision: 2
  source_sha256: b87dc1118dbf853201d0c589e955c852f29da0e148f0a273c99690d8943de1ee
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project.Settings.RMED Review.Max Atoms

## Claim

### Prose Claim


When present, the value is positive. Its absence supplies no default.

### Formal Claim

```CFEL
# model
Project.Settings.RMED Review.Max Atoms:: [int]{::0..1};

Project.Settings.RMED Review.Max Atoms.*[]{::0}
```

