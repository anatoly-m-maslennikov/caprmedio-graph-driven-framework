---
version: 35
updated_at: 2026-11-04 09:30:21 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  depends_on:
  - CA-R-2748
  - CA-R-2532
  - CA-R-1402@27
  child_of:
  - CA-M-446
  - CA-R-1421
cce_version: cce_1
cce_form: obligation
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Project.Settings
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Source Selection
current_scope_unit: PROJECT_CONFIGURATION
status: Active
atom_id: CA-R-622
ref_id: CA-R-622
tier: 1
claim_target_scope_unit: caprmedio
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-622-PROJECT_CONFIGURATION-RULE--keep-selected-settings-in-their-authoritative-settings-artifact.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
container:
  scope_unit: CA-SU-13
---
## Summary
Keep selected settings in their authoritative Settings Artifact

## Claim

### Prose Claim


the CAPRMEDIO Framework Instance serving caprmedio **must** consume Project Settings according **to** Core Meta-Model authority under CA-R-2748, **without** redefining their purpose, locations, **or** selected values **in** Project Atoms.
