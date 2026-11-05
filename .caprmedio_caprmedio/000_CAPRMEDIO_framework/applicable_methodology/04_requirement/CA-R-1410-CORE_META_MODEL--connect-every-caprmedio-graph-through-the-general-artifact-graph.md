---
atom_id: CA-R-1410
ref_id: CA-R-1410
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term//Artifact
tier: 1
status: Active
version: 22
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1410-CORE_META_MODEL-RULE--connect-every-caprmedio-graph-through-the-general-artifact-graph.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1410-CORE_META_MODEL--connect-every-caprmedio-graph-through-the-general-artifact-graph.md
  source_atom_id: CA-R-1410
  source_atom_revision: 22
  source_sha256: 653cd61a8199e6de09ab0697a151c52b9bdb622910467dcd3886ac57ebace903
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Connect Every CAPRMEDIO Graph through the General Artifact Graph

## Claim

### Prose Claim


CAPRMEDIO Graphs and their connections to the General Artifact Graph.


**every** CAPRMEDIO Graph **must** connect **to** the General Artifact Graph through **`>=1`** shared **or** referenced source Artifact **or** Structural Entity. the connection preserves the existing source identity **without** creating a duplicate source **or** requiring an artificial Artifact for a structural-only source.
