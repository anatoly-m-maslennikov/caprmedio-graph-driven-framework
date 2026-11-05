---
atom_id: CA-M-277
ref_id: CA-M-277
container:
  scope_unit: CA-SU-13
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings.Interaction.Reporting Mode := silent
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings.Interaction.Reporting Mode
  - CAPRMEDIO_MODEL <+ Project.Settings.Interaction
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Architecture <+ Communication
  - CAPRMEDIO_MODEL <+ Project
tier: 3
relations:
  depends_on:
  - CA-R-1440
status: Active
version: 34
updated_at: 2026-11-04 09:30:21 +0400
carrier_destination:
  file:
    name: CA-M-277-PROJECT_CONFIGURATION-IMPLEMENTATION_METHOD--report-in-silent-mode.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/05_method
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/05_method/CA-M-277-PROJECT_CONFIGURATION-IMPLEMENTATION_METHOD--report-in-silent-mode.md
  source_atom_id: CA-M-277
  source_atom_revision: 34
  source_sha256: 897be90aae95931015648500355bcd2e51b8c213ad99216f68b4c1dad38b23d1
  original_relations_sha256: 857656931241d959b1be6352fc0443b25d1f37ac23500b10876e7c5a09a5d1fb
---
## Summary

Report **in** silent mode

## Claim

### Prose Claim


silent-mode reporting.


**to** report **in** `silent` mode, answer exploratory input normally **and**, apart from the mandatory information governed by CA-R-1440-CORE_META_MODEL-GENERAL-REQUIREMENT--preserve-mandatory-information-in-every-reporting-mode, report **only** durable Artifacts **or** Project state that CAPRMEDIO created, updated, archived, committed, **or** **otherwise** changed; omit ordinary announcements of mode selection, workflow routing, Skill chaining, **and** gate transitions.
