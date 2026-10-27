---
atom_id: CA-R-1620@13
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Projection/Type: Realization Graph'
  depends_on:
  - Subject/Graph Relation
  - Subject/Graph Node/Domain/Continuant/Projection
version: 13
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-R-1246
  - CA-R-1494
  - CA-R-1616
  - CA-R-1746
tier: 3
type: Definition
---
# Summary

Define the Realization Graph dependency view

## Scope

optional dependency views of Realization Graphs.

## Claim

the dependency view of a Realization Graph **means** an optional derived view of the selected declarations, resources, internal dependency targets, external dependency targets, **and** admitted typed Relations among them.

## Details

- its specification identifies the selected population, Relation Types, source boundary, **and** limits of dependency traversal; recursive reachability does **not** establish complete coverage by itself.
- the view **must** derive from the same source-backed graph facts **without** another independently maintained dependency authority. cycles are represented **when** evidenced; their validity is checked against applicable Claims rather than assumed from the view name.
- this view does **not** require a second universal view.
