---
atom_id: CA-R-1621@10
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Realization Graph'
  depends_on:
  - Subject/Engineering/Graph Projection
  - Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Selection
version: 10
updated_at: 2026-10-24 22:06:39 +0400
relations:
  relates_to:
  - CA-R-1568
  - CA-R-1616
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
