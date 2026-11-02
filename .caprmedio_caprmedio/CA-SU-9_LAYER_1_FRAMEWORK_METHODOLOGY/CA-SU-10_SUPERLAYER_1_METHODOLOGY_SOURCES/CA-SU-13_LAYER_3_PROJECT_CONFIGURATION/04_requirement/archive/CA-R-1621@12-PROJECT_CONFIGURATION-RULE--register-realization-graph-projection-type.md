---
atom_id: CA-R-1621@12
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Projection/Type: Realization Graph'
  depends_on:
  - Subject/Graph Node/Engineering/Graph Projection
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Domain/Continuant/Selection
version: 12
updated_at: 2026-10-26 05:59:45 +0400
relations:
  depends_on:
  - CA-R-1568
  - CA-R-1631
  - CA-R-1746
tier: 3
type: Rule
---
# Summary

Register Realization Graph Projection Type

## Scope

the caprmedio Project Configuration registration of the `realization_graph` Projection Type.

## Claim

the caprmedio Project Configuration **must** register `realization_graph` as a specialized non-authoritative Projection Type for understanding existing Implementation **and** supporting reverse engineering into proposed RMED.

## Details

- registration uses the accepted specialized graph specification **and** the general Projection guarantees of CORE_META_MODEL; it does **not** add this Type **to** the universal Core requirements of other Projects.
- registration **and** activation remain distinct. the configured activation follows CA-R-1631; accepting this registration does **not** activate the Projection.
- the output remains a Projection under CA-R-1746. its permitted Implementation contribution under CA-R-1568 is **not** an Atom Content Role assigned **to** the Projection.
