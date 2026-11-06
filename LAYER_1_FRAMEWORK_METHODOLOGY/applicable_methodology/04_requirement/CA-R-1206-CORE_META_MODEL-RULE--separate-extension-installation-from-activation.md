---
atom_id: CA-R-1206
ref_id: CA-R-1206
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Effect Authorization
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//INSTALLED_EXTENSIONS
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
tier: 1
status: Active
version: 28
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1206-CORE_META_MODEL-RULE--separate-extension-installation-from-activation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1206-CORE_META_MODEL-RULE--separate-extension-installation-from-activation.md
  source_atom_id: CA-R-1206
  source_atom_revision: 28
  source_sha256: 67c073b095aeb86385e7fc682da82647391e0981081c07b2f3cb2d01a7f03d8d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Separate Extension Installation from Activation

## Claim

### Prose Claim


Extension installation and activation applicability in the current Project.


installing an Extension **must** make its immutable authority available **to** Project Configuration **without** making the Extension authority applicable **to** the current Project.
