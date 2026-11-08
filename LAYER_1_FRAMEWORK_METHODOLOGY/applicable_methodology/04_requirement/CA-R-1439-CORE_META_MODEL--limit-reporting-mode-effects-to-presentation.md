---
atom_id: CA-R-1439
ref_id: CA-R-1439
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Interaction
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings.Interaction.Reporting Mode
tier: 2
relations:
  child_of:
  - CA-R-1402@27
status: Active
version: 24
updated_at: 2026-11-04 09:30:21 +0400
carrier_destination:
  file:
    name: CA-R-1439-CORE_META_MODEL-RULE--limit-reporting-mode-effects-to-presentation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1439-CORE_META_MODEL--limit-reporting-mode-effects-to-presentation.md
  source_atom_id: CA-R-1439
  source_atom_revision: 24
  source_sha256: 5703b7a26a5be7ee2ac553d0b11e3c5cda4d7b26f9f745ccd647b593b0f2c85c
  original_relations_sha256: 00e97614aa8f831b27af9608de052e62a7eacf810958ad3399e14a4c1e665b55
---
## Summary

Limit reporting mode effects to presentation

## Claim

### Prose Claim


the effects of the interaction reporting mode.


the interaction reporting mode **must** affect presentation **only**, **without** changing authorization, Artifact creation, workflow routing, validation, **or** safety behavior.
