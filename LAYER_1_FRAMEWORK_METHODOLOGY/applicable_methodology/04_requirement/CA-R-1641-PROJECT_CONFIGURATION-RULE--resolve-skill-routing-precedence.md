---
subjects:
  active: Entity/Object/Continuant/Governing Objects/Governing Configuration
  passive:
  - Aspects <+ UX <+ Entry
  - Aspects <+ Engineering <+ Execution Control <+ Effect Authorization
  - Scope Unit//PROJECT_CONFIGURATION
version: 33
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-R-1641
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1641-PROJECT_CONFIGURATION-RULE--resolve-skill-routing-precedence.md
  source_atom_id: CA-R-1641
  source_atom_revision: 33
  source_sha256: 117d10026c9825f135531a5cdb2ecafbc1f6510fee809b7a9a0d5b02bea67f25
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary
Resolve skill routing precedence

## Claim scope
skill route resolution.

## Claim

skill routes **must** resolve by explicit precedence: project-local CAPRMEDIO routes override framework routes, which override provider-global routes.
