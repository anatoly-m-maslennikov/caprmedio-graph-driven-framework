---
version: 34
updated_at: 2026-11-02 18:35:20 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  depends_on:
  - CA-R-1750
  - CA-R-2532
  - CA-R-1402@27
  child_of:
  - CA-M-446
  - CA-R-1421
cce_version: cce_1
cce_form: obligation
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project.Settings
  passive:
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Term//Artifact
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Source Selection
current_scope_unit: PROJECT_CONFIGURATION
status: Active
atom_id: CA-R-622
tier: 1
claim_target_scope_unit: caprmedio
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-622-PROJECT_CONFIGURATION-RULE--keep-selected-settings-in-their-authoritative-settings-artifact.md
  source_atom_id: CA-R-622
  source_atom_revision: 34
  source_sha256: 4ec207740df960abeba56fe5d867c8c341423ea5ffeb6bc5db21a7c285f5396b
  original_relations_sha256: e871e62bb800dd80294c2ca2aee838cc2530615370df370a5d32fd9d770b0002
---
## Summary
Keep selected settings in their authoritative Settings Artifact

## Claim

the CAPRMEDIO Framework Instance serving caprmedio **must** consume Project Settings **and** Framework Instance Settings according **to** Core Meta-Model authority under CA-R-1750, **without** redefining their purpose, locations, **or** selected values **in** Project Atoms.
