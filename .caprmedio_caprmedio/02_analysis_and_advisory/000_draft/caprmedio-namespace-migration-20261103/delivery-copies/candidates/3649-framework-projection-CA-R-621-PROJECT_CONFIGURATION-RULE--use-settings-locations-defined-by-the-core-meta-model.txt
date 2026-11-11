---
subject_scopes:
- scope-topology
version: 17
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  depends_on:
  - CA-D-359
  - CA-D-364
  child_of:
  - CA-R-622
current_scope_unit: PROJECT_CONFIGURATION
status: Active
atom_id: CA-R-621
tier: 2
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File
claim_target_scope_unit: caprmedio
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-621-PROJECT_CONFIGURATION-RULE--use-settings-locations-defined-by-the-core-meta-model.md
  source_atom_id: CA-R-621
  source_atom_revision: 17
  source_sha256: 3ec13e80635ea66b1355cbdd24f494ee510678be7888c2ab9690e28ade0e039f
  original_relations_sha256: b8cbb30ffabe4fcbb8a02dc0d203a78072d64c00f7f4b788e477136b73ff28f7
---
## Summary
Use settings locations defined by the Core Meta-Model

## Claim

the caprmedio Implementation **must** resolve both Settings Artifacts through the Core Meta-Model Carrier rules CA-D-359 **and** CA-D-364 **without** defining a Project-specific competing location.
