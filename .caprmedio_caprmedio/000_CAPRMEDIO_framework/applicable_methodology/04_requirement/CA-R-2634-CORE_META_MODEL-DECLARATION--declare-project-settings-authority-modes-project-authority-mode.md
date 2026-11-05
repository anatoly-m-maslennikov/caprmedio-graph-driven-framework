---
atom_id: CA-R-2634
ref_id: CA-R-2634
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Authority Modes.Project Authority Mode
tier: 3
status: Active
version: 2
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2634-CORE_META_MODEL-DECLARATION--declare-project-settings-authority-modes-project-authority-mode.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2634-CORE_META_MODEL-DECLARATION--declare-project-settings-authority-modes-project-authority-mode.md
  source_atom_id: CA-R-2634
  source_atom_revision: 2
  source_sha256: b241e943ba8aeaa832b17bfce6a4291e2810680f09683e815d3861657a93d252
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project.Settings.Authority Modes.Project Authority Mode

## Claim

### Prose Claim


The permitted values are `strict` and `casual`. The effective selection follows the applicable authority-mode resolution.

### Formal Claim

```CFEL
# model
Project.Settings.Authority Modes.Project Authority Mode{::1}:: {::1};

Project.Settings.Authority Modes.Project Authority Mode.*[]{::0}
```

