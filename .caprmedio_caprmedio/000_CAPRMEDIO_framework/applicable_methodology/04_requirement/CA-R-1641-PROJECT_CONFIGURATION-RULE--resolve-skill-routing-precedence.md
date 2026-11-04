---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
  passive:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ UX <+ Entry
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Effect Authorization
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
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
  source_sha256: 2d19363233c17a6402287a89c0f1ef9bc49c36be9c8de34fdf31a4b69ff9f1cb
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary
Resolve skill routing precedence

## Claim

### Prose Claim

skill route resolution.


skill routes **must** resolve by explicit precedence: project-local CAPRMEDIO routes override framework routes, which override provider-global routes.
