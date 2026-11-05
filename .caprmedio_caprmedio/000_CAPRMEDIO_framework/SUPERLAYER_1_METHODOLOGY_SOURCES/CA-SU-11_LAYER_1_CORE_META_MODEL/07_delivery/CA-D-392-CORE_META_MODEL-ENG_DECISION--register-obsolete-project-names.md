---
atom_id: CA-D-392
ref_id: CA-D-392
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/(.Form: Scope Unit Graph)'
  dependencies:
  - CAPRMEDIO_MODEL <+ Project.Settings
  - CAPRMEDIO_MODEL <+ Project.Settings.Name
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Obsolete Names
tier: 3
relations:
  child_of:
  - CA-R-1052
status: Active
version: 27
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-392-CORE_META_MODEL-DECISION--register-obsolete-project-names.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register obsolete project names

## Claim

### Prose Claim


Project identity in Project Scope Unit Graph Projections.


the Project Scope Unit Graph Projections **must** expose Project identity from the Project Settings Artifact with `project.name` as the canonical name **and** `project.obsolete_names` as the registered prior names **without** becoming authority for (Project Settings Name **or** Obsolete Project Name).

### Current source pin

Proposed N+1 successor of `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-392-CORE_META_MODEL-ENG_DECISION--register-obsolete-project-names.md`, CA-D-392@24, SHA-256 `384bfda590d882b143ab76b14854621d123a24026f7d90710da83ea50a3f79ca`. Current bytes remain unchanged; this Draft preserves the `project.obsolete_names` encoding and performs no projection refresh.
