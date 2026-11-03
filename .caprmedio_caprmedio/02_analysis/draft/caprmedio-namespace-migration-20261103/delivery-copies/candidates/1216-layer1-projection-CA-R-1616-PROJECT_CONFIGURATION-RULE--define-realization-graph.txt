---
atom_id: CA-R-1616
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection/(.Form := Realization Graph)
  passive:
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Traceability
  - CAPRMEDIO <+ MODEL <+ Entity
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Projection/Type: Realization Graph'
  - CAPRMEDIO <+ MODEL <+ Journal
  - CAPRMEDIO <+ MODEL <+ Projection
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
version: 25
relations:
  depends_on:
  - CA-R-1493
  - CA-R-1568
  - CA-R-2535
tier: 3
role: Requirement
form: Rule
updated_at: 2026-11-02 18:35:20 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1616-PROJECT_CONFIGURATION-RULE--define-realization-graph.md
  source_atom_id: CA-R-1616
  source_atom_revision: 25
  source_sha256: 71929ca1f8c241156c23435b84c8cb039b56b8c34ecfa61badce96b937fb8180
  original_relations_sha256: 36b983a251288c7a82a8b58fc531b8512945c90ac25c124f675a82cc4c0b0732
---
## Summary

Define Realization Graph

## Claim scope

Realization Graphs derived from a declared selection of existing Implementation sources and available evidence.

## Claim

Realization Graph **means** a non-authoritative Projection of Entities **and** typed Relations derived from a declared selection of existing Implementation sources **and** available evidence, used **to** understand that Implementation **and** support reverse engineering into proposed RMED.

- the Projection **must** retain source traceability under CA-R-2535 **and** generation identity under CA-R-1493, using **only** the source kinds selected for the job; legacy Implementation need **not** have pre-existing RMED **or** Journal records.
- missing evidence **and** uncertain interpretations **must** be reported. observed structure **or** behavior does **not** establish intended Requirements, a passed Evaluation, **or** completeness outside the checked selection.
- the Artifact kind remains Projection, including **when** delivered as an Implementation output under CA-R-1568. views derive from its source-backed facts **without** creating another source of truth.
