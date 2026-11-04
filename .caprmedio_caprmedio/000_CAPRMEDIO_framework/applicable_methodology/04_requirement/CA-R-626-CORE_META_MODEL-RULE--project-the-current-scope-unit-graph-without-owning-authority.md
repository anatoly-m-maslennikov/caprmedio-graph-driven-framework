---
subjects:
  active: CAPRMEDIO_MODEL <+ Projection/(.Form:=Scope Unit Graph)
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Projection
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)'
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
version: 43
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-960
  - CA-R-2531
  - CA-R-962
atom_id: CA-R-626
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-626-CORE_META_MODEL-RULE--project-the-current-scope-unit-graph-without-owning-authority.md
  source_atom_id: CA-R-626
  source_atom_revision: 43
  source_sha256: a722e6d734ff0945ff9ec4ed8d2c4cd76ab028b0d903aeb69a02297ee442a956
  original_relations_sha256: f992d3b2b1d966bc2994ace3778a06f70686b8b65d6aaebe3bb12e3bf9a5483c
---
## Summary

Project the current Scope Unit Graph without owning authority

## Claim

### Prose Claim


Project Scope Unit Graph Projections.


**every** Project Scope Unit Graph Projection **must** distinguish declared Scope Unit facts from Project Structure, derived structural values, effective Settings, **and** observed Carrier materialization. a discrepancy, missing Goal, undeclared candidate directory, **or** declared unit with no existing Carrier **must** remain visible as a separate finding **without** silently changing the declaration **or** inventing source authority.
