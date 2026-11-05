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
---
## Summary

Limit reporting mode effects to presentation

## Claim

### Prose Claim


the effects of the interaction reporting mode.


the interaction reporting mode **must** affect presentation **only**, **without** changing authorization, Artifact creation, workflow routing, validation, **or** safety behavior.
