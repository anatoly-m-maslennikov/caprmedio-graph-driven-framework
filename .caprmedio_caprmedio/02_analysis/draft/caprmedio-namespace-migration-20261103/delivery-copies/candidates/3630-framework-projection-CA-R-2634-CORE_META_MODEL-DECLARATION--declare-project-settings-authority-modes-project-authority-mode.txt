---
atom_id: CA-R-2634
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings.Authority Modes.Project Authority Mode
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2634-CORE_META_MODEL-DECLARATION--declare-project-settings-authority-modes-project-authority-mode.md
  source_atom_id: CA-R-2634
  source_atom_revision: 1
  source_sha256: a55edc81602dcfd4d8f775be6825de263d00c53b396cb2e9234554a244c94590
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project.Settings.Authority Modes.Project Authority Mode

## Claim

The permitted values are `strict` and `casual`. The effective selection follows the applicable authority-mode resolution.

```CFEL
Project.Settings.Authority Modes.Project Authority Mode{:1}: [string]{:1};
Project.Settings.Authority Modes.Project Authority Mode.*[]{:0}
```
