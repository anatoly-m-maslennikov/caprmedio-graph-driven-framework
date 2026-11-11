---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Package/Project Implementation
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO <+ MODEL <+ Term//Artifact
  - CAPRMEDIO <+ MODEL <+ Atom
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1568
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1568-CORE_META_MODEL--permit-projections-as-implementation-outputs.md
  source_atom_id: CA-R-1568
  source_atom_revision: 26
  source_sha256: 3090a38d38d30812f9a50aa3554c0cb0c7b4e39c32df7500c87a04f559ec0201
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Permit Projections as Implementation outputs

## Claim scope

non-authoritative view Projections delivered as Implementation outputs.

## Claim

a view Projection **may** be delivered as an Implementation output of its governing RMED **without** becoming an Atom **or** another source of truth for the facts it represents.

- its output contribution is I; its Artifact kind remains Projection **and** its content remains derived from its declared sources.

## Details

This permission concerns a derived view delivered as an Implementation output, not Implementation as a whole. Directly edited native Implementation realizes RMED and can be a source of truth for what actually exists; it is not a Projection. A generated dependency graph or another derived view of Implementation remains a Projection: update its sources, then rebuild the view through its Workflow.
