---
atom_id: CA-R-2748
ref_id: CA-R-2748
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Project.Settings.Name
  - CAPRMEDIO_MODEL <+ Project.Settings.Prefix
  - CAPRMEDIO_MODEL <+ Atom
tier: 1
status: Active
version: 1
updated_at: 2026-11-04 09:30:21 +0400
carrier_destination:
  file:
    name: CA-R-2748-RULE--unify-operator-selected-project-settings.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2748-CORE_META_MODEL-RULE--unify-operator-selected-project-settings.md
  source_atom_id: CA-R-2748
  source_atom_revision: 1
  source_sha256: d13a89ed6f1e86d53e030b8e191412698c5a0b5cc213442e41eaeb252cb6fac2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Unify Operator-selected Project Settings

## Claim

### Prose Claim

Project.Settings owns the Operator-selected Project initialization inputs and applicable CAPRMEDIO behavior and configuration choices. Each selected setting has one authoritative owner in its Project. Atoms define permitted parameters, constraints, and applicability without duplicating selected values or defaults.
