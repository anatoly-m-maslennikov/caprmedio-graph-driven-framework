---
atom_id: CA-R-1206
ref_id: CA-R-1206
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization"
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
---
## Summary

Separate Extension Installation from Activation

## Claim

### Prose Claim


Extension installation and activation applicability in the current Project.


installing an Extension **must** make its immutable authority available **to** Project Configuration **without** making the Extension authority applicable **to** the current Project.
