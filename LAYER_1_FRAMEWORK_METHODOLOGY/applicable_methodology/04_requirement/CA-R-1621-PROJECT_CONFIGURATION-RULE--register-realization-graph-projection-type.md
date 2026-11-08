---
atom_id: CA-R-1621
ref_id: CA-R-1621
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form:=Realization Graph)
  dependencies:
  - CAPRMEDIO_MODEL <+ Projection/(.Form:=Realization Graph)
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
tier: 3
relations:
  depends_on:
  - CA-R-1568
  - CA-R-1631
  - CA-R-2535
status: Active
version: 19
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-1621-PROJECT_CONFIGURATION-RULE--register-realization-graph-projection-type.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1621-PROJECT_CONFIGURATION-RULE--register-realization-graph-projection-type.md
  source_atom_id: CA-R-1621
  source_atom_revision: 19
  source_sha256: 722e6cf382b9b55a8041eea0eb70690e14b4467760459acc754917be650f8e85
  original_relations_sha256: ca4f19a04ef603d0119ba0e2515933c7f693ac2b776d27f253b80e34776cb913
---
## Summary

Register Realization Graph Projection Type

## Claim

### Prose Claim


the caprmedio Project Configuration registration of the `realization_graph` Projection Type.


the caprmedio Project Configuration **must** register `realization_graph` as a specialized non-authoritative Projection Type for understanding existing Implementation **and** supporting reverse engineering into proposed RMED.

## Details

- registration uses the accepted specialized graph specification **and** the general Projection guarantees of CORE_META_MODEL; it does **not** add this Type **to** the universal Core requirements of other Projects.
- registration **and** activation remain distinct. the configured activation follows CA-R-1631; accepting this registration does **not** activate the Projection.
- the output remains a Projection under CA-R-2535. its permitted Implementation contribution under CA-R-1568 is **not** an Atom Content Role assigned **to** the Projection.
