---
atom_id: CA-R-626
ref_id: CA-R-626
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form:=Scope Unit Graph)
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Projection
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Goal)'
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
tier: 3
relations:
  child_of:
  - CA-R-960
  - CA-R-2531
  - CA-R-962
status: Active
version: 43
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-626-CORE_META_MODEL-RULE--project-the-current-scope-unit-graph-without-owning-authority.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Project the current Scope Unit Graph without owning authority

## Claim

### Prose Claim


Project Scope Unit Graph Projections.


**every** Project Scope Unit Graph Projection **must** distinguish declared Scope Unit facts from Project Structure, derived structural values, effective Settings, **and** observed Carrier materialization. a discrepancy, missing Goal, undeclared candidate directory, **or** declared unit with no existing Carrier **must** remain visible as a separate finding **without** silently changing the declaration **or** inventing source authority.
