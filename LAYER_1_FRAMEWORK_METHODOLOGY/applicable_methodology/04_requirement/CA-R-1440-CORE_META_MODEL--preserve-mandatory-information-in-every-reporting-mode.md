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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1440-CORE_META_MODEL--preserve-mandatory-information-in-every-reporting-mode.md
  source_atom_id: CA-R-1440
  source_atom_revision: 24
  source_sha256: 868cad0fea6d7a48727b48818dbd8248ce2ddd0e09400465b4c129ece0270063
  original_relations_sha256: 00e97614aa8f831b27af9608de052e62a7eacf810958ad3399e14a4c1e665b55
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
