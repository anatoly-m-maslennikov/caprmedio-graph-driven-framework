---
subjects:
  active: CAPRMEDIO <+ STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  passive:
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ STRUCTURE <+ Entity/Object/Continuant/Selection//Extension Sources
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
version: 31
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1207
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1207-CORE_META_MODEL-RULE--separate-project-configuration-rules-from-current-settings.md
  source_atom_id: CA-R-1207
  source_atom_revision: 31
  source_sha256: 7b93175ec3106c2acbe210b6f82ef6c74527bf03b76f949e2400c4fe8e0295b5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Separate Project Configuration Rules from Current Settings

## Claim scope

Ownership of Project-specific expansion rules, constraints, defaults, current Extension activation, and selected Extension revisions.

## Claim

the Project Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated **in** Project Configuration Atoms.
