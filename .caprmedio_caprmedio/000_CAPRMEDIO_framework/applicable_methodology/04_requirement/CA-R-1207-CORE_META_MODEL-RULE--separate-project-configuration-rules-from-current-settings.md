---
atom_id: CA-R-1207
ref_id: CA-R-1207
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Extension Sources
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
tier: 1
status: Active
version: 31
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1207-CORE_META_MODEL-RULE--separate-project-configuration-rules-from-current-settings.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1207-CORE_META_MODEL-RULE--separate-project-configuration-rules-from-current-settings.md
  source_atom_id: CA-R-1207
  source_atom_revision: 31
  source_sha256: fcffdb13a3b728db3dad1d18d9a765a30394abbb92fbab290ceea5eeed3e0910
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Separate Project Configuration Rules from Current Settings

## Claim

### Prose Claim


Ownership of Project-specific expansion rules, constraints, defaults, current Extension activation, and selected Extension revisions.


the Project Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated **in** Project Configuration Atoms.
