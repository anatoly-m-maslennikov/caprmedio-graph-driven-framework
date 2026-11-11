---
atom_id: CA-R-1568
ref_id: CA-R-1568
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
  dependencies:
  - CAPRMEDIO_MODEL <+ Package/Project Package
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Atom
tier: 2
status: Active
version: 27
updated_at: 2026-11-10 14:38:45 +0400
carrier_destination:
  file:
    name: CA-R-1568-CORE_META_MODEL--permit-projections-as-implementation-outputs.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Permit Projections as Implementation outputs

## Claim

### Prose Claim


non-authoritative view Projections delivered as Implementation outputs.


a view Projection **may** be delivered as an Implementation output of its governing RMED **without** becoming an Atom **or** another source of truth for the facts it represents.

- its output contribution is I; its Artifact kind remains Projection **and** its content remains derived from its declared sources.

## Details

This permission concerns a derived view delivered as an Implementation output, not Implementation as a whole. Directly edited native Implementation realizes RMED and can be a source of truth for what actually exists; it is not a Projection. A generated dependency graph or another derived view of Implementation remains a Projection: update its sources, then rebuild the view through its Workflow.
