---
atom_id: CA-R-1620
ref_id: CA-R-1620
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form:=Realization Graph)
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Projection
tier: 3
status: Active
version: 21
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-1620-PROJECT_CONFIGURATION-RULE--define-the-realization-graph-dependency-view.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Define the Realization Graph dependency view

## Claim

### Prose Claim


optional dependency views of Realization Graphs.


the dependency view of a Realization Graph **means** an optional derived view of the selected declarations, resources, internal dependency targets, external dependency targets, **and** admitted typed Relations among them.

## Details

- its specification identifies the selected population, Relation Types, source boundary, **and** limits of dependency traversal; recursive reachability does **not** establish complete coverage by itself.
- the view **must** derive from the same source-backed graph facts **without** another independently maintained dependency authority. cycles are represented **when** evidenced; their validity is checked against applicable Claims rather than assumed from the view name.
- this view does **not** require a second universal view.
