---
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Project.Settings.Name
  - CAPRMEDIO_MODEL <+ Project.Settings.Prefix
  - CAPRMEDIO_MODEL <+ Atom
version: 1
updated_at: 2026-11-04 09:30:21 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-R-2748
status: Active
tier: 1
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-2748-CORE_META_MODEL-RULE--unify-operator-selected-project-settings.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2748-CORE_META_MODEL-RULE--unify-operator-selected-project-settings.md
  source_atom_id: CA-R-2748
  source_atom_revision: 1
  source_sha256: aee50dd9308c89d6ff68605aa4e1c643071be28bb5da1ec3dd362f8ea6a70cef
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Unify Operator-selected Project Settings

## Claim

### Prose Claim

Project.Settings owns the Operator-selected Project initialization inputs and applicable CAPRMEDIO behavior and configuration choices. Each selected setting has one authoritative owner in its Project. Atoms define permitted parameters, constraints, and applicability without duplicating selected values or defaults.
