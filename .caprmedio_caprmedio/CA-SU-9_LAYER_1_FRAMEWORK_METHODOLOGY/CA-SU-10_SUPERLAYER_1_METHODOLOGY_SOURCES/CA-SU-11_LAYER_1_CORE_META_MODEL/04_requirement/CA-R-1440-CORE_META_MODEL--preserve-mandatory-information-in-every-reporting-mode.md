---
atom_id: CA-R-1440
ref_id: CA-R-1440
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Interaction
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Interaction.Reporting Mode
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
tier: 2
relations:
  child_of:
  - CA-R-1402@27
status: Active
version: 24
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1440-CORE_META_MODEL-RULE--preserve-mandatory-information-in-every-reporting-mode.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Preserve mandatory information in every reporting mode

## Claim

### Prose Claim


mandatory information reported by **every** interaction reporting mode.


**every** interaction reporting mode **must** report the following mandatory information:

- blockers **and** failed operations;
- ambiguity that requires Operator input;
- permission **or** approval requests;
- safety-critical information;
- material deviations from the requested outcome.
