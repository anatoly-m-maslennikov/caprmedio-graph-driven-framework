---
atom_id: CA-R-621
ref_id: CA-R-621
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
tier: 2
relations:
  depends_on:
  - CA-D-359
  - CA-D-364
  child_of:
  - CA-R-622
status: Active
version: 17
updated_at: 2026-11-02 19:44:26 +0400
subject_scopes:
- scope-topology
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: caprmedio
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-621-PROJECT_CONFIGURATION-RULE--use-settings-locations-defined-by-the-core-meta-model.md
  source_atom_id: CA-R-621
  source_atom_revision: 17
  source_sha256: 726ab50955f8255df9fb4c8a4f634bd91d6d04f67d6041239d424fcd68a4f407
  original_relations_sha256: b8cbb30ffabe4fcbb8a02dc0d203a78072d64c00f7f4b788e477136b73ff28f7
---
## Summary
Use settings locations defined by the Core Meta-Model

## Claim

### Prose Claim


the caprmedio Implementation **must** resolve both Settings Artifacts through the Core Meta-Model Carrier rules CA-D-359 **and** CA-D-364 **without** defining a Project-specific competing location.
