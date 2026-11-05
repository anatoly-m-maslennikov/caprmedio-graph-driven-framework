---
atom_id: CA-R-1052
ref_id: CA-R-1052
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/Type: Scope Unit Graph'
  - CAPRMEDIO_MODEL <+ Projection
tier: 1
relations:
  child_of:
  - CA-R-832
status: Active
version: 41
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1052-CORE_META_MODEL-RULE--separate-project-settings-from-the-project-scope-unit-graph.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1052-CORE_META_MODEL-RULE--separate-project-settings-from-the-project-scope-unit-graph.md
  source_atom_id: CA-R-1052
  source_atom_revision: 41
  source_sha256: 23dcb3b496aead12a843dc856392599b1c3edafd9a1bdee47065850b65be1ff3
  original_relations_sha256: e4bb1ac5beed6873fcce262f203647bc69192db2e911302404b2324a7319e165
---
## Summary

Separate Project Settings from the Project Scope Unit Graph

## Claim

### Prose Claim


authoritative Project initialization Settings, Framework Instance behavior Settings, Project Structure declarations, and read-only Project Scope Unit Graph Projections.


the CAPRMEDIO Framework **must** distinguish authoritative Project initialization Settings, Framework Instance behavior Settings, **and** Project Structure declarations from read-only Project Scope Unit Graph Projections. structural observations **and** generated effective values **must not** become independent Settings **or** Project Structure authority.
