---
atom_id: CA-R-2173
ref_id: CA-R-2173
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Package/Implementation
tier: 1
status: Active
version: 9
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-2173-CORE_META_MODEL-RULE--define-implementation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2173-CORE_META_MODEL-RULE--define-implementation.md
  source_atom_id: CA-R-2173
  source_atom_revision: 9
  source_sha256: 2ff0826e904dedbbe1f4acc012e579e23c3c290e43917d6e1a616469ea8b9586
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Implementation

## Claim

### Prose Claim


Implementation **means** the actual Code, Prompts, Documentation and Resources that realize RMED for a Project. Directly edited Implementation can be authoritative for what is actually implemented.

## Semantics

Implementation is not a Projection merely because it realizes RMED. Its logical artifacts remain distinct from their Carriers and from the Runtime in which technical execution occurs.

A Projection is a non-authoritative output produced from a declared source selection through a Workflow: source of truth → Workflow → Projection. Changes to a Projection belong in its authoritative sources, followed by a rebuild through its Workflow. A generated view of Implementation is a Projection; that does not make its directly edited sources Projections.

## Details

CA-R-2535 defines Projection and its source-only editing boundary. CA-R-1568 permits a derived view to be delivered as an Implementation output without classifying Implementation as a whole as Projection.
