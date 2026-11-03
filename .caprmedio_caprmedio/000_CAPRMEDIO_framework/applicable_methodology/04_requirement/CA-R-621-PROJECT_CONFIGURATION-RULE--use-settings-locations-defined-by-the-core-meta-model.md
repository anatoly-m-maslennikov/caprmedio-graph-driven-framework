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
  active: Carrier/File
claim_target_scope_unit: caprmedio
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-621-PROJECT_CONFIGURATION-RULE--use-settings-locations-defined-by-the-core-meta-model.md
  source_atom_id: CA-R-621
  source_atom_revision: 17
  source_sha256: 0dd7388a9bf89b2f0cda2224337b508a56db98fc454a5991e0140fb007aec220
  original_relations_sha256: b8cbb30ffabe4fcbb8a02dc0d203a78072d64c00f7f4b788e477136b73ff28f7
---
## Summary
Use settings locations defined by the Core Meta-Model

## Claim

the caprmedio Implementation **must** resolve both Settings Artifacts through the Core Meta-Model Carrier rules CA-D-359 **and** CA-D-364 **without** defining a Project-specific competing location.
